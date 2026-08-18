# AI Research Weekly — 2025-W36

> Coverage Window: 2025-09-01～2025-09-07 (ISO Monday～Sunday)
> Research Mode: Historical Discovery Replay + Primary-Source Review
> First Backfill: 2026-07-31
> Re-audited: 2026-08-24
> Weekly Candidate Gate: Pass with one explicit blocked-skip item
> Historical Books Gate: Closed — this reconstruction does not modify Books

## Executive Summary

The legacy archive retained only one infrastructure event. A full replay restored 65 canonical W36 candidates: 24 scored `20+` and received non-template Full Source Reviews; 41 scored below 20 and received source/date/score/rejection closure. The week is not a one-paper Kubernetes week.

Six durable system lines emerge:

1. Agent training moved from single-answer RL to stateful multi-turn rollouts, tool/environment contracts, streaming rollout pools, and explicit verifier ownership.
2. Post-training and evaluation evidence became more structural: process/outcome reward coupling, online/offline data mixing, benchmark paraphrase sensitivity, and incentives to guess rather than abstain.
3. Inference explored a new branch between autoregressive and masked generation: Set Block Decoding changes the prediction set while preserving exact KV reuse, but its forward-pass reduction is not automatically an end-to-end serving speedup.
4. Evaluation became a typed pipeline: prompt variant, parser, semantic judge, human calibration, and abstention policy own different evidence, so score movement cannot automatically be attributed to the model.
5. Multimodal systems exposed two distinct transitions: arbitrary-interval generation changes the compute-quality budget, while camera-specific geometry correction inserts an explicit observation state before physical action.
6. Model and safety infrastructure both challenged convenient proxies: activation deltas can assist registry discovery but do not prove quality, and high in-distribution probe accuracy does not establish semantic harmfulness detection under shift.

One item remains `Unverified / Blocked`: the event-time Robix full text could not be recovered through arXiv HTML, while identity and abstract are verified. It is carried under the user-approved blocked-skip rule with an exact material request. `Review Pending = 0`; the annual Archive Completion Gate remains open until that material is recovered or formally waived.

## Coverage Window and Limitations

- Owner dates use arXiv v1 / first-public date or official release date, never discovery-feed submission date.
- Hugging Face Daily Papers was used only for discovery. arXiv HTML/PDF, official repositories, official release notes, and Kubernetes documentation are the evidence owners.
- The Sep 1～7 Daily/weekly discovery feeds and the Sep 8 delayed feed were reconciled title by title because submission-day popularity pages mix Aug 29～31 and Sep 1～5 v1 owners. Sep 6～7 introduced no additional arXiv first-public owner after identifier/date routing; Sep 9 onward was sampled only for spillback.
- Google Scholar, OpenAlex, DBLP, Semantic Scholar, and Crossref were used as metadata/deduplication lanes; they do not replace primary mechanism evidence.
- Author benchmarks remain author evidence. Results are not generalized beyond the disclosed model, data, evaluator, decoding, hardware, or task contract.
- Several papers do not disclose hardware, precision, serving concurrency, or SLO; those fields are recorded as `Not Disclosed`, not inferred.

## 1. 模型与研究机构

### Source Coverage

The fixed institution lane was replayed across OpenAI, Anthropic, Google/DeepMind, Meta, Microsoft, NVIDIA, ByteDance Seed, Baichuan, Qwen, DeepSeek, Hugging Face, and major university/industry labs.

- Retained as mechanism evidence: UI-TARS-2, Baichuan-M2, OpenVision 2, Why Language Models Hallucinate.
- Official product/policy facts below the core threshold: OpenAI sensitive-conversation routing plans and Anthropic regional sales restrictions. Both are explicit policy facts; neither discloses enough mechanism to infer internal training or runtime behavior.
- Anthropic financing/education announcements and general corporate commentary were scanned and rejected as non-mechanism events.

## 2. 论文与学术来源

### Source Coverage

The academic lane replayed arXiv v1 batches first public on Sep 1～5 plus delayed discovery feeds, including a title-by-title reconciliation against the Hugging Face W36 feed and W37 spillback ledger. Sixty in-window research candidates were identity/date checked; twenty-three reached `20+` and completed Full Source Review. Papers first public on Aug 29～31 were routed to W35 rather than duplicated here.

The restored coverage spans agentic RL/tool use, verifier systems, multimodal representation, world-model planning, post-training objectives, evaluation reliability, hallucination incentives, decoding acceleration, robotics, generative vision, and domain benchmarks. Low relevance or insufficiently general mechanisms remain in the closure ledger rather than being silently omitted.

## 3. AI Infra 与工程项目

### Source Coverage

The fixed engineering lane replayed PyTorch, JAX, CUDA, Triton, vLLM, SGLang, Dynamo, TensorRT-LLM, Ray, KServe, Kubeflow, Kubernetes, Hugging Face, DeepSpeed, Megatron-LM, llama.cpp, ONNX Runtime, and OpenXLA.

- Kubernetes DRA GA design follow-up is retained as a W35→W36 layering event, not a second GA announcement.
- Ray 2.49.1 is retained below threshold as a patch/version fact; no independent durable mechanism was disclosed.
- TensorRT-LLM 1.1.0rc3 is retained below threshold as an experimental prerelease fact. A prerelease cannot establish a stable production contract.
- No in-window vLLM, KServe, Kubeflow, PyTorch, JAX, or OpenXLA GA event was found that changes a durable design conclusion. Absence is recorded rather than filled with later release notes.

## Candidate Scoring

| Candidate | First Public | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Final Disposition |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| UI-TARS-2 Technical Report | 2025-09-02 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete; Books Pending |
| SimpleTIR | 2025-09-02 | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete; Books Pending |
| VerlTool | 2025-09-01 | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Source Review Complete; Books Pending |
| Baichuan-M2 | 2025-09-02 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| OpenVision 2 | 2025-09-01 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| DynaGuard | 2025-09-02 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete; Books Pending |
| LMEnt | 2025-09-03 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete; Books Pending |
| Planning with Reasoning using Vision Language World Model | 2025-09-02 | 4 | 4 | 3 | 4 | 5 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| Beyond Correctness | 2025-09-03 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| Towards a Unified View of LLM Post-Training | 2025-09-04 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete; Books Pending |
| DeepResearch Arena | 2025-09-01 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete; Books Pending |
| Why Language Models Hallucinate | 2025-09-04 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete; Books Pending |
| Set Block Decoding | 2025-09-04 | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete; Books Pending |
| On Robustness and Reliability of Benchmark-Based Evaluation of LLMs | 2025-09-04 | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| Loong | 2025-09-03 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| Emergent Hierarchical Reasoning through RL (HICRA) | 2025-09-03 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete; Books Pending |
| Hunyuan-MT Technical Report | 2025-09-05 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs | 2025-09-01 | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| Manipulation as in Simulation | 2025-09-02 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete; Books Pending |
| Inverse IFEval | 2025-09-04 | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete; Books Pending |
| Transition Models | 2025-09-04 | 5 | 4 | 3 | 4 | 5 | 4 | 25/30 | Full Source Review Complete; Books Pending |
| Delta Activations | 2025-09-04 | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete; Books Pending |
| False Sense of Security: Why Probing-based Malicious Input Detection Fails to Generalize | 2025-09-04 | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete; Books Pending |
| Kubernetes DRA GA design details | 2025-09-01 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete; Refine W35 packet |
| Landscape of Agentic RL for LLMs | 2025-09-02 | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Weekly Only — survey, no new primary mechanism |
| Reasoning Vectors | 2025-09-01 | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Emerging / Experimental |
| POINTS-Reader | 2025-09-01 | 3 | 3 | 4 | 4 | 2 | 3 | 19/30 | Weekly Only — document conversion specialization |
| Gated Associative Memory | 2025-09-01 | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Emerging / Experimental |
| Kwai Keye-VL 1.5 | 2025-09-01 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Weekly Only — model report |
| Implicit Actor-Critic Coupling for RLVR | 2025-09-02 | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Emerging / Experimental |
| GenCompositor | 2025-09-02 | 3 | 2 | 2 | 3 | 2 | 3 | 15/30 | Reject — narrow video composition workload |
| Jointly Reinforcing Diversity and Quality | 2025-09-02 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Emerging / Experimental |
| Benchmarking Optimizers for LLM Pretraining | 2025-09-01 | 3 | 4 | 4 | 4 | 2 | 2 | 19/30 | Weekly Only — bounded optimizer comparison |
| Flavors of Moonshine | 2025-09-02 | 3 | 3 | 4 | 3 | 3 | 3 | 19/30 | Weekly Only — edge ASR specialization |
| DCPO | 2025-09-02 | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Emerging / Experimental |
| FlashAdventure | 2025-09-01 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Weekly Only — GUI evaluation case |
| Fantastic Pretraining Optimizers | 2025-09-02 | 3 | 4 | 4 | 3 | 3 | 2 | 19/30 | Emerging / Experimental |
| M3Ret | 2025-09-01 | 3 | 3 | 3 | 3 | 2 | 3 | 17/30 | Weekly Only — domain representation evidence |
| ViSTA-SLAM | 2025-09-01 | 3 | 3 | 3 | 3 | 2 | 3 | 17/30 | Reject — robotics perception specialization |
| Robix | 2025-09-01 | 4 | 4 | 3 | 2 | 4 | 2 | 19/30 | Unverified / Blocked — full text unavailable |
| LuxDiT | 2025-09-03 | 3 | 2 | 2 | 3 | 2 | 3 | 15/30 | Reject — lighting estimation specialization |
| WildScore | 2025-09-05 | 2 | 3 | 3 | 3 | 3 | 3 | 17/30 | Weekly Only — domain benchmark |
| LatticeWorld | 2025-09-05 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Emerging / Experimental |
| WinT3R | 2025-09-05 | 3 | 3 | 3 | 3 | 2 | 3 | 17/30 | Reject — reconstruction specialization |
| Bootstrapping Task Spaces for Self-Improvement | 2025-09-04 | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Emerging / Experimental |
| U-ARM | 2025-09-02 | 3 | 3 | 4 | 3 | 2 | 3 | 18/30 | Weekly Only — teleoperation hardware case |
| Behavioral Fingerprinting of LLMs | 2025-09-02 | 3 | 3 | 4 | 3 | 3 | 3 | 19/30 | Emerging — LLM-judge dependence |
| MedVista3D | 2025-09-04 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Weekly Only — medical benchmark/model case |
| Symbolic Graphics Programming with LLMs | 2025-09-05 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Emerging / Experimental |
| Attributes as Textual Genes | 2025-09-02 | 3 | 3 | 3 | 3 | 4 | 3 | 19/30 | Emerging / Experimental |
| Discrete Noise Inversion for Next-scale Autoregressive Image Editing | 2025-09-02 | 3 | 2 | 3 | 3 | 3 | 3 | 17/30 | Reject — narrow image-editing branch |
| AMBEDKAR | 2025-09-02 | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Emerging / Experimental |
| Panel of Peers | 2025-09-01 | 3 | 3 | 3 | 3 | 4 | 3 | 19/30 | Emerging — self-generated preference evidence |
| MedDINOv3 | 2025-09-02 | 3 | 3 | 3 | 3 | 2 | 3 | 17/30 | Weekly Only — medical segmentation specialization |
| Self-Supervised Cross Reconstruction for Point Clouds | 2025-09-01 | 3 | 2 | 3 | 3 | 2 | 3 | 16/30 | Reject — point-cloud pretraining specialization |
| MOSAIC | 2025-09-02 | 3 | 2 | 3 | 3 | 2 | 3 | 16/30 | Reject — personalized image-generation specialization |
| Drivel-ology | 2025-09-04 | 2 | 3 | 3 | 3 | 4 | 3 | 18/30 | Weekly Only — bounded diagnostic benchmark |
| From Editor to Dense Geometry Estimator | 2025-09-04 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Emerging — diffusion geometry estimator |
| NER Retriever | 2025-09-04 | 3 | 3 | 4 | 3 | 3 | 3 | 19/30 | Weekly Only — typed retrieval specialization |
| Few-step Flow for 3D Generation | 2025-09-04 | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Emerging — bounded 3D distillation branch |
| Durian | 2025-09-04 | 3 | 2 | 3 | 3 | 2 | 3 | 16/30 | Reject — portrait-animation specialization |
| Ray 2.49.1 | 2025-09-03 | 1 | 2 | 4 | 5 | 3 | 3 | 18/30 | Weekly Only — patch fact |
| TensorRT-LLM 1.1.0rc3 | 2025-09-04 | 3 | 3 | 3 | 5 | 4 | 1 | 19/30 | Weekly Only — prerelease fact |
| OpenAI sensitive-conversation routing plan | 2025-09-02 | 2 | 4 | 3 | 5 | 4 | 1 | 19/30 | Version Fact / Mechanism Not Disclosed |
| Anthropic regional sales restrictions | 2025-09-04 | 1 | 3 | 2 | 5 | 3 | 2 | 16/30 | Weekly Only — governance policy fact |

Score reconciliation: `65` total rows = `24` Full Source Reviews + `41` low-score closures. Six-dimensional arithmetic was mechanically recomputed; no Total mismatch remains.

## Deep Analysis 1 — Stateful multi-turn Agent RL becomes a systems problem

### Why → Principle → Mechanism

Single-turn RL assumes a bounded prompt, immediate reward, and disposable environment. GUI/tool agents violate all three assumptions: trajectories are long and heterogeneous, rewards are delayed, and an environment crash can destroy the state needed to interpret later actions. UI-TARS-2 therefore treats rollout infrastructure, session identity, leases, checkpointing, streaming partially filled rollout pools, value initialization, and environment recovery as part of the learning algorithm rather than background plumbing.

The important evolution is:

```text
static demonstrations
→ single-turn verifiable RL
→ multi-turn stateful rollout
→ asynchronous rollout/training overlap
→ environment and trajectory become versioned training state
```

### Trade-off and evidence boundary

The design increases utilization and supports long-tail trajectories, but it introduces policy-lag, partial-pool bias, environment nondeterminism, and a larger rollback surface. The paper reports strong benchmark results and analyses of PPO/GRPO, value pretraining, interaction rounds, and quantization, but these remain author-run experiments in their sandbox and cannot establish a universal agent-training recipe.

## Deep Analysis 2 — Hallucination is partly an incentive contract

### Why → Principle → Mechanism

Why Language Models Hallucinate separates two causes that are often collapsed. Pretraining induces unavoidable estimation errors for facts that cannot be statistically distinguished from unseen facts; post-training/evaluation then often rewards guessing because abstention receives no credit. A model can therefore improve benchmark score while becoming less calibrated for deployment.

The durable system conclusion is not “make the model always refuse.” It is to align the scoring contract with the desired operating point:

```text
claim opportunity
→ evidence/uncertainty estimate
→ answer, qualify, retrieve, or abstain
→ score all four actions under deployment cost
```

### Trade-off and evidence boundary

Abstention-aware evaluation reduces confident guessing only when the scoring rule and downstream product tolerate non-answers. It does not solve retrieval errors, reasoning errors, tool failures, or adversarial prompts. The paper offers a statistical framework and evaluation-design argument, not a production hallucination detector or a calibrated universal confidence score.

## Deep Analysis 3 — Set Block Decoding changes the unit of prediction

### Why → Principle → Mechanism

Autoregressive decoding serializes every token; masked/diffusion decoding exposes parallelism but often loses exact KV-cache compatibility. Set Block Decoding fine-tunes an NTP model with masked-token prediction so it can propose a set of not-necessarily-consecutive future tokens and iteratively correct them while preserving exact KV reuse.

The evolution branch is:

```text
one exact next token
→ contiguous speculative block
→ parallel masked block
→ set-valued future-token proposal with exact cache reuse
```

### Trade-off and evidence boundary

The paper reports 3～5× fewer forward passes on fine-tuned Llama-3.1-8B and Qwen3-8B settings and provides 3B/1T-token ablations plus a roofline analysis. Forward-pass reduction is not identical to wall-clock speedup: masked work per pass, solver scheduling, kernel shapes, batching, memory traffic, acceptance/correction, and serving concurrency determine end-to-end benefit.

## Full Source Review

### UI-TARS-2 Technical Report

- **Candidate / Week / Score:** UI-TARS-2 / 2025-W36 / 29/30.
- **Source Family / Type:** `UI-TARS-2-2509.02544`; technical report + official repositories.
- **Event Date / Revision:** arXiv v1 2025-09-02; later revisions remain the same family.
- **Primary Sources / Access:** arXiv HTML read across formulation, sandbox, data flywheel, multi-turn RL, implementation, experiments, analyses, conclusion; ByteDance repositories checked. `Full Source Review Complete`.
- **Original Problem / Previous Design:** Modular GUI pipelines and demonstration learning were reasonable for short tasks but brittle under scarce trajectories, delayed rewards, GUI-only actions, and fragile environments.
- **Changed Constraint / Mechanism:** Millions of long-horizon episodes require stateful asynchronous rollout, streaming partially filled pools, reward shaping, decoupled/length-adaptive GAE, value pretraining, and a hybrid GUI/filesystem/terminal sandbox.
- **State / Control / Data Ownership:** Session IDs bind task to VM/browser state; manager owns leases/reclamation; policy server emits action; environment returns observation/reward; rollout pool bridges asynchronous inference and training; checkpoints and event handlers own recovery evidence.
- **Implementation:** Thousands of VM instances, browser sandboxes, Playwright/CDP-compatible control, shared filesystem, process monitoring, checkpointing, time control, and CT→SFT→RL data recycling are disclosed; proprietary cluster details remain Not Disclosed.
- **Evaluation Contract:** Online-Mind2Web, OSWorld, WindowsAgentArena, AndroidWorld, 15 games, LMGame-Bench, BrowseComp, Terminal Bench, and SWE-Bench Verified; analyses cover PPO vs GRPO, value pretraining, interaction rounds, verifier viability, inference scaling, and latency-oriented quantization.
- **Hardware / precision / batch / concurrency / SLO:** VM/browser concurrency is described at thousands-QPS scale; exact training hardware, precision, batch, and production SLO are Not Disclosed.
- **Proves / Does Not Prove:** Proves one integrated system can improve author-run GUI/game/tool benchmarks; does not prove safe autonomous deployment, cross-environment reproducibility, or that end-to-end learned agents dominate modular systems under all workloads.
- **Trade-offs / Failure Modes / Coexistence:** Higher utilization and richer tasks add policy lag, stale rollouts, environment skew, leaked sessions, reward hacking, and recovery complexity. Modular agents remain appropriate when tool semantics are stable and auditability outweighs policy generality.
- **Evolution / Owner:** `Direct Evolution`; `AGENT-WORKFLOW` Ch81 (legacy Ch77), with handoffs to `TRAIN-PPO` Ch32 and `PLATFORM-EVALUATION-SYSTEM` Ch66. Adjacent Ch80/82 and Ch31/33 reviewed.
- **Existing Coverage / Integration / Open Question:** Books already describe durable workflow state; candidate can refine rollout-state ownership after Historical Books Gate opens. Open: how to bound off-policy drift when partial pools mix policy versions?

### SimpleTIR

- **Candidate / Week / Score:** SimpleTIR / 2025-W36 / 26/30.
- **Source Family / Type:** `SIMPLETIR-2509.02479`; research paper + code artifact.
- **Event Date / Revision / Access:** v1 2025-09-02; arXiv Method, training/evaluation, ablations, limitations, appendices and repository read. `Full Source Review Complete`.
- **Problem / Previous Design:** Single-turn reasoning or manually staged tool traces were simple and reproducible, but could not assign outcome credit across tool-mediated multi-turn trajectories.
- **Changed Constraint / Mechanism:** End-to-end RL optimizes interleaved reasoning, tool call, observation, and answer sequences rather than separately supervising each stage.
- **State / Flow / Implementation:** The policy owns textual action decisions; tool runtime owns execution state; observation is appended to trajectory; verifier owns terminal reward. Training couples rollout generation, tool execution, reward, and policy update.
- **Evaluation Contract / Ablation:** Multi-turn tool-integrated reasoning tasks compare against prompting/SFT/RL baselines; reported training curves and ablations test the components; exact serving hardware/SLO are Not Disclosed.
- **Proves / Does Not Prove:** Shows author-run gains from end-to-end trajectory optimization; does not establish tool correctness, production isolation, or transfer to arbitrary non-verifiable tools.
- **Trade-offs / Failure Modes / Coexistence:** Better credit assignment costs environment execution and increases tool nondeterminism, reward sparsity, and unsafe-action surface. Staged SFT remains preferable for deterministic workflows and scarce online environments.
- **Evolution / Owner:** `Direct Evolution`; `AGENT-TOOL-CALLING` Ch78 (legacy Ch74), handoff to `TRAIN-GRPO` Ch33 and `AGENT-WORKFLOW` Ch81; adjacent Ch77/79 reviewed.
- **Integration / Open:** `Books Pending`; refine tool-trajectory ownership, not a framework listing. Open: how are tool failures separated from policy failures during reward assignment?

### VerlTool

- **Candidate / Week / Score:** VerlTool / 2025-W36 / 27/30.
- **Source Family / Type:** `VERLTOOL-2509.01055`; systems/research paper + framework repository.
- **Event Date / Revision / Access:** v1 2025-09-01; architecture, tool-environment abstraction, rollout, training, experiments, appendices and artifact read. `Full Source Review Complete`.
- **Problem / Previous Design:** Bespoke agent-RL stacks worked for one tool family but duplicated environment adapters, rollout orchestration, and reward plumbing.
- **Changed Constraint / Mechanism:** A modular environment/tool interface decouples policy training from heterogeneous execution backends while retaining multi-turn state and scalable rollout.
- **State / Flow / Implementation:** Trainer owns policy/version; rollout workers own sampled trajectory; environment manager owns tool lifecycle; tool server owns external effects; reward/verifier owns outcome. Requests flow policy→tool→observation→trajectory→reward→update.
- **Evaluation Contract:** Multiple tool-use tasks and algorithms exercise extensibility and scaling; published comparisons are framework-author evidence. Hardware/precision/concurrency vary by experiment; undisclosed values remain Not Disclosed.
- **Proves / Does Not Prove:** Demonstrates a reusable training substrate and reported task gains; does not prove semantic equivalence across tools or eliminate sandbox/security requirements.
- **Trade-offs / Failure Modes / Coexistence:** Modularity improves reuse but adds RPC/schema skew, timeout semantics, partial failure, versioned environment state, and observability burden. Bespoke in-process tools remain simpler for small deterministic experiments.
- **Evolution / Owner:** `Layering / Dependency`; `TRAIN-GRPO` Ch33 (legacy Ch29) owns RL runtime contract, with handoff to `AGENT-TOOL-CALLING` Ch78. Adjacent Ch32/34 and Ch77/79 reviewed.
- **Integration / Open:** `Books Pending`; candidate refines algorithm/runtime coupling. Open: which trajectory metadata is sufficient to replay a tool-involving update exactly?

### Baichuan-M2

- **Candidate / Week / Score:** Baichuan-M2 / 2025-W36 / 24/30.
- **Source Family / Type:** `BAICHUAN-M2-2509.02208`; model technical report.
- **Event Date / Revision / Access:** v1 2025-09-02; training, verifier system, evaluation, safety/limitations and appendices read. `Full Source Review Complete`.
- **Problem / Previous Design:** Domain SFT and answer-only medical benchmarks were reasonable first steps but underrepresent reasoning quality and verifier reliability.
- **Changed Constraint / Mechanism:** A large verifier system supplies process/outcome signals for medical capability scaling and creates a separate evidence owner from the answer generator.
- **State / Flow / Implementation:** Generator owns candidate response; verifier ensemble/system owns scoring signal; training pipeline selects/weights trajectories; deployment still requires external clinical policy and human review.
- **Evaluation Contract:** Medical exams and reasoning evaluations compare model/verifier variants; clinical deployment, prospective trials, hardware, precision, concurrency, and SLO are Not Disclosed.
- **Proves / Does Not Prove:** Supports the claim that verifier-scaled training improves disclosed benchmarks; does not prove diagnostic safety, calibration, or replacement of clinicians.
- **Trade-offs / Failure Modes / Coexistence:** Verifier scale improves signal coverage but can synchronize evaluator bias, amplify hidden label errors, and add compute. Human review and narrow task-specific validation remain necessary.
- **Evolution / Owner:** `Layering / Dependency`; `PLATFORM-EVALUATION-SYSTEM` Ch66 (legacy Ch62), handoff to `TRAIN-RLHF` Ch31. Adjacent Ch65/67 and Ch30/32 reviewed.
- **Integration / Open:** `Books Pending`; use only for verifier ownership/evidence boundary. Open: how is correlated verifier error measured under domain shift?

### OpenVision 2

- **Candidate / Week / Score:** OpenVision 2 / 2025-W36 / 24/30.
- **Source Family / Type:** `OPENVISION2-2509.01644`; multimodal pretraining paper + models/code.
- **Event Date / Revision / Access:** v1 2025-09-01; architecture, objectives, implementation, evaluation, caption/masking ablations and conclusion read. `Full Source Review Complete`.
- **Problem / Previous Design:** Contrastive image-text encoders provided aligned representations but required a text encoder and contrastive objective, increasing training memory/complexity.
- **Changed Constraint / Mechanism:** Generative visual pretraining removes the text encoder and contrastive loss, using masked image-token prediction plus caption supervision to scale encoders beyond 1B parameters.
- **State / Flow / Implementation:** Visual encoder owns representation; masking process owns corruption state; decoder/objective owns reconstruction/caption signal; downstream multimodal model consumes the frozen/tuned encoder.
- **Evaluation Contract:** Classification/retrieval/multimodal downstream tasks compare prior encoders; ablations vary caption supervision and mask ratio. Exact end-to-end serving SLO and some hardware details are Not Disclosed.
- **Proves / Does Not Prove:** Shows competitive author-evaluated representations with reduced reported training time/memory; does not prove generative pretraining universally dominates contrastive learning.
- **Trade-offs / Failure Modes / Coexistence:** Simpler pretraining may reduce explicit cross-modal alignment and shift quality dependence to captions/masking. Contrastive objectives remain useful when retrieval alignment is the primary contract.
- **Evolution / Owner:** `Alternative Branch`; `MULTIMODAL-REPRESENTATION` Ch23, adjacent Ch22/24 reviewed.
- **Integration / Open:** `Books Pending`; refine representation-objective branches. Open: which downstream tasks lose calibration when explicit contrastive alignment is removed?

### DynaGuard

- **Candidate / Week / Score:** DynaGuard / 2025-W36 / 25/30.
- **Source Family / Type:** `DYNAGUARD-2509.02563`; safety-model paper + dataset/artifact.
- **Event Date / Revision / Access:** v1 2025-09-02; user-policy formulation, data generation, model training, benchmark, category analysis, explanations and limitations read. `Full Source Review Complete`.
- **Problem / Previous Design:** Fixed safety taxonomies are easy to benchmark but cannot express tenant/application-specific policy and age quickly.
- **Changed Constraint / Mechanism:** The guard model receives a natural-language policy at inference and judges content/action against that policy, returning violation decision plus explanation.
- **State / Flow / Implementation:** Policy owner supplies versioned rule; guard owns classification/explanation; gateway/workflow owns enforcement; recovery/human appeal remains external. Dataset covers roughly 5,000 generated rules with post-hoc categories.
- **Evaluation Contract:** Policy-following safety tasks compare fixed-policy guard models and general LMs; human trust, multi-agent recovery, production latency/SLO, and adversarial policy conflicts are not established.
- **Proves / Does Not Prove:** Supports dynamic-policy classification on the released benchmark; does not prove arbitrary policies are internally consistent or explanations are faithful.
- **Trade-offs / Failure Modes / Coexistence:** Flexibility reduces taxonomy lock-in but adds policy injection, contradictory rules, version skew, judge/explanation disagreement, and enforcement latency. Fixed classifiers remain appropriate for stable high-volume policies.
- **Evolution / Owner:** `Direct Evolution`; `PLATFORM-SECURITY` Ch72 (legacy Ch68), handoff to `PLATFORM-GATEWAY` Ch62. Adjacent Ch71/73 and Ch61/63 reviewed.
- **Integration / Open:** `Books Pending`; refine policy-as-versioned-input contract. Open: who resolves conflicting tenant, platform, and legal policies?

### LMEnt

- **Candidate / Week / Score:** LMEnt / 2025-W36 / 25/30.
- **Source Family / Type:** `LMENT-2509.03405`; interpretability/evaluation suite paper + artifacts.
- **Event Date / Revision / Access:** v1 2025-09-03; data index, pretrained models, retrieval design, experiments, knowledge-acquisition analyses, applications and limitations read. `Full Source Review Complete`.
- **Problem / Previous Design:** Post-hoc probing of opaque pretrained corpora cannot cleanly connect a fact to exposure, training time, and representation.
- **Changed Constraint / Mechanism:** The suite co-releases indexed pretraining chunks, checkpoints/models, entity-based retrieval, and controlled probes so exposure and latent representation can be compared.
- **State / Flow / Implementation:** Dataset index owns evidence provenance; checkpoint owns training-time state; retrieval maps entity/query to chunks; probe/evaluator owns representation claim.
- **Evaluation Contract:** Model knowledge, chunk retrieval, rare-entity coverage, scale, mention-source ablation, and acquisition over training are analyzed against retrieval/model baselines.
- **Hardware / SLO:** Training/evaluation configurations are paper-bound; production concurrency and SLO are Not Applicable/Not Disclosed.
- **Proves / Does Not Prove:** Enables stronger causal diagnostics than model-only probing in its controlled corpus; does not prove a retrieved chunk caused a specific internal circuit or generalize to proprietary corpora.
- **Trade-offs / Failure Modes / Coexistence:** Traceability costs constrained data/model scale and may create synthetic regularities. Black-box probes remain necessary for inaccessible models but support weaker causal claims.
- **Evolution / Owner:** `Layering / Dependency`; `WORLDVIEW-REPRESENTATION` Ch5, handoff to `PLATFORM-EVALUATION-SYSTEM` Ch66. Adjacent Ch4/6 reviewed.
- **Integration / Open:** `Books Pending`; strengthen the interpretability evidence ladder. Open: what minimum provenance is needed before claiming memorization rather than generalization?

### Planning with Reasoning using Vision Language World Model

- **Candidate / Week / Score:** VLWM / 2025-W36 / 24/30.
- **Source Family / Type:** `VLWM-2509.02722`; world-model/planning paper.
- **Event Date / Revision / Access:** v1 2025-09-02; semantic state/action representation, policy/dynamics/critic, experiments, ablations, appendices and limitations read. `Full Source Review Complete`.
- **Problem / Previous Design:** Pixel prediction is expressive but expensive and can model visual detail unrelated to plan success; direct VLM planning lacks an explicit transition model.
- **Changed Constraint / Mechanism:** The model predicts semantically abstracted action-conditioned transitions and uses a critic to search/rank plans rather than forecasting raw pixels.
- **State / Flow / Implementation:** Language state description owns abstract world state; policy proposes action sequences; dynamics predicts state transition; critic scores trajectory against goal; search selects among 20 candidate plans in the disclosed System-2 setup.
- **Evaluation Contract:** COIN, CrossTask, EgoExo4D; 8B critic; leading multimodal models and ground-truth plans as baselines; critic-input ablations remove goal/state descriptions.
- **Proves / Does Not Prove:** Supports semantic world-state planning on instructional-video tasks; does not establish physical causality, closed-loop robot control, or robustness to observation errors.
- **Trade-offs / Failure Modes / Coexistence:** Abstraction reduces pixel cost but can discard geometry/contact constraints; critic search adds inference cost and evaluator bias. Pixel simulators remain useful where visual dynamics are the task.
- **Evolution / Owner:** `Direct Evolution`; `MULTIMODAL-WORLD-MODELS` Ch25, handoff to Ch26 and `AGENT-PLANNING` Ch79. Adjacent Ch24/26 reviewed.
- **Integration / Open:** `Books Pending`; refine generation→transition→planning distinction. Open: how is latent-state invalidation handled after an unexpected observation?

### Beyond Correctness

- **Candidate / Week / Score:** Beyond Correctness / 2025-W36 / 24/30.
- **Source Family / Type:** `PROF-2509.03403`; RL data-curation/reward paper.
- **Event Date / Revision / Access:** v1 2025-09-03; process/outcome reward formulation, oversample-filter method, experiments, rollout-budget ablation and limitations read. `Full Source Review Complete`.
- **Problem / Previous Design:** Outcome rewards are robust but sparse; process reward models give dense signals but can be noisy. Using either alone was a reasonable simplification.
- **Changed Constraint / Mechanism:** PROF oversamples candidate trajectories, filters with process reward, then trains with outcome-grounded objectives to preserve correctness while improving reasoning steps.
- **State / Flow / Implementation:** Generator owns candidates; PRM owns step score; outcome verifier owns final correctness; curator selects retained trajectories; trainer consumes filtered data.
- **Evaluation Contract:** Mathematical reasoning benchmarks compare vanilla GRPO, Blend, RAFT++ and PROF variants; rollout-budget ablation shows quality/compute sensitivity.
- **Proves / Does Not Prove:** Shows gains under the paper's PRM/verifier/task setup; does not prove process scores are faithful or the extra sampling is cost-effective in production.
- **Trade-offs / Failure Modes / Coexistence:** Better intermediate quality costs oversampling/filter compute and can inherit PRM bias. Outcome-only RL remains preferable when verification is cheap and process labels unreliable.
- **Evolution / Owner:** `Layering / Dependency`; `TRAIN-GRPO` Ch33 (legacy Ch29), handoff to `PLATFORM-EVALUATION-SYSTEM` Ch66. Adjacent Ch32/34 reviewed.
- **Integration / Open:** `Books Pending`; add reward-owner and compute boundary. Open: can PRM uncertainty rather than a hard filter improve efficiency?

### Towards a Unified View of LLM Post-Training

- **Candidate / Week / Score:** Unified Post-Training / 2025-W36 / 25/30.
- **Source Family / Type:** `UNIFIED-POSTTRAIN-2509.04419`; post-training theory/experiment paper.
- **Event Date / Revision / Access:** v1 2025-09-04; unified gradient derivation, component analysis, hybrid feedback gate, experiments, gate ablation and appendices read. `Full Source Review Complete`.
- **Problem / Previous Design:** SFT and RL were treated as sequential recipes, obscuring that both contribute gradient estimators with different data/reward ownership.
- **Changed Constraint / Mechanism:** A unified policy-gradient view decomposes online RL and offline supervised components; Hybrid Post-Training gates/mixes them based on performance feedback.
- **State / Flow / Implementation:** Online rollout owns exploration samples/rewards; offline corpus owns demonstration likelihood; gate owns mixing decision; policy update consumes both gradients.
- **Evaluation Contract:** Qwen2.5-Math-1.5B/7B math settings compare SFT-only, GRPO-only, SFT→GRPO and HPT; threshold ablation tracks reward and offline-data ratio.
- **Proves / Does Not Prove:** Establishes a useful decomposition and author-run gains in math; does not collapse safety alignment, preference optimization, and all RL into one universally optimal algorithm.
- **Trade-offs / Failure Modes / Coexistence:** Feedback gating can balance exploration/exploitation but adds validation leakage, threshold sensitivity, and data-source skew. Sequential SFT→RL remains simpler when phase boundaries are operationally valuable.
- **Evolution / Owner:** `Principle Reuse`; `TRAIN-RLHF` Ch31 (legacy Ch27), handoff to Ch29/33/34. Adjacent Ch30/32 reviewed.
- **Integration / Open:** `Books Pending`; refine branch conditions instead of replacing SFT/RL chapters. Open: what feedback signal remains trustworthy under distribution shift?

### DeepResearch Arena

- **Candidate / Week / Score:** DeepResearch Arena / 2025-W36 / 25/30.
- **Source Family / Type:** `DEEPRESEARCH-ARENA-2509.01396`; benchmark/evaluation paper + dataset/prompts.
- **Event Date / Revision / Access:** v1 2025-09-01; task creation, seminar grounding, ACE evaluation, model comparison, leakage and human-alignment appendices read. `Full Source Review Complete`.
- **Problem / Previous Design:** Static benchmark corpora risk training contamination; expert-curated research tasks are expensive and narrow.
- **Changed Constraint / Mechanism:** Seminar-grounded contemporary tasks reduce contamination opportunity; an automated checklist evaluator (ACE) decomposes research-answer quality into auditable criteria.
- **State / Flow / Implementation:** Seminar source owns task provenance; research agent owns evidence gathering/output; checklist generator owns criteria; evaluator owns per-criterion judgment; leakage analysis owns contamination evidence.
- **Evaluation Contract:** Multiple frontier/research models, task categories, leakage checks, automated-vs-human alignment, and prompt templates are reported; browsing availability and model versions are part of the workload contract.
- **Proves / Does Not Prove:** Measures performance on this seminar-grounded harness and improves evaluation granularity; does not isolate base-model capability from search/tool/harness opportunity.
- **Trade-offs / Failure Modes / Coexistence:** Fresh tasks reduce leakage but age quickly and checklist judges can miss novel valid reasoning. Human expert review remains necessary for high-stakes research claims.
- **Evolution / Owner:** `Direct Evolution`; `PLATFORM-EVALUATION-SYSTEM` Ch66, handoff to `AGENT-RAG` Ch76 and `AGENT-WORKFLOW` Ch81. Adjacent Ch65/67 reviewed.
- **Integration / Open:** `Books Pending`; refine model≠harness≠tool-opportunity separation. Open: how often must seminar tasks rotate to preserve freshness?

### Why Language Models Hallucinate

- **Candidate / Week / Score:** Why Language Models Hallucinate / 2025-W36 / 29/30.
- **Source Family / Type:** `HALLUCINATION-INCENTIVES-2509.04664`; statistical/theoretical research paper.
- **Event Date / Revision / Access:** v1 2025-09-04; statistical derivation, pretraining/post-training arguments, examples, discussion, limitations and appendices read. `Full Source Review Complete`.
- **Problem / Previous Design:** Accuracy-only benchmarks reward a guess whenever abstention is always wrong, even when deployment cost favors calibrated uncertainty.
- **Changed Constraint / Mechanism:** The paper frames pretraining hallucination as estimation/classification error and persistence as a scoring-rule incentive; changing abstention penalties changes the optimal policy.
- **State / Flow / Implementation:** Model weights encode distributional estimate; decoder emits claim/abstention; evaluation policy owns reward; deployment controller must route uncertain cases to retrieval, qualification, or refusal.
- **Evaluation Contract:** Primarily theoretical/statistical with examples and benchmark-incentive analysis; no production detector, hardware, batch, concurrency, precision, or SLO experiment.
- **Proves / Does Not Prove:** Shows why some errors are statistically unavoidable and why common scoring encourages guessing; does not prove all hallucinations share one cause or provide a calibrated per-claim confidence estimator.
- **Trade-offs / Failure Modes / Coexistence:** Abstention reduces false confident answers but raises non-answer rate and may be gamed by excessive refusal. Accuracy-only scoring remains useful when every query must receive a forced choice.
- **Evolution / Owner:** `Principle Reuse`; `PLATFORM-EVALUATION-SYSTEM` Ch66, handoff to `WORLDVIEW-WHY-MODELS-LEARN` Ch4 and `AGENT-RAG` Ch76. Adjacent Ch65/67 reviewed.
- **Integration / Open:** `Books Pending`; refine evidence/abstention operating points. Open: how should correlated atomic-claim confidence aggregate without multiplying independent probabilities?

### Set Block Decoding

- **Candidate / Week / Score:** Set Block Decoding / 2025-W36 / 27/30.
- **Source Family / Type:** `SBD-2509.04185`; inference/training research paper.
- **Event Date / Revision / Access:** v1 2025-09-04; NTP/MATP objective, algorithms, benchmarks, 3B/1T-token ablations, timing/roofline analysis and appendices read. `Full Source Review Complete`.
- **Problem / Previous Design:** Exact NTP decoding is sequential; speculative decoding depends on draft acceptance; diffusion-style parallelism often sacrifices exact KV reuse.
- **Changed Constraint / Mechanism:** Fine-tune one model to jointly predict the next token and a set of masked future tokens, solve/refine the set in parallel, and retain exact cached prefix state.
- **State / Flow / Implementation:** KV cache owns committed prefix; set solver owns provisional future tokens; masked positions are mutable until correction/commit; training reuses an intermediate NTP checkpoint and adds MATP/NTP losses.
- **Evaluation Contract:** Llama-3.1-8B, Qwen3-8B and 3B pretraining ablations; reported 3～5× forward-pass reduction; NTP baseline, loss-term, training-duration, and roofline comparisons.
- **Hardware / precision / serving contract:** Paper timing setup is bounded; broad production batch, multi-tenant concurrency, scheduler interaction and SLO remain Not Disclosed.
- **Proves / Does Not Prove:** Proves reduced sequential model invocations with comparable disclosed benchmark quality; does not prove 3～5× wall-clock or fleet-level speedup.
- **Trade-offs / Failure Modes / Coexistence:** Parallel proposals add masked compute, solver/correction scheduling, mutable-token identity and commit complexity. Plain NTP remains simplest for low-latency single-token or unsupported models.
- **Evolution / Owner:** `Alternative Branch`; `INFER-SPECULATIVE-DECODING` Ch48 (legacy Ch44), handoff to `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 and `INFER-KV-CACHE` Ch45. Adjacent Ch47/49 reviewed.
- **Integration / Open:** `Books Pending`; add set-valued proposal/commit branch. Open: how does continuous batching interact with different refinement depths?

### On Robustness and Reliability of Benchmark-Based Evaluation of LLMs

- **Candidate / Week / Score:** Benchmark Robustness / 2025-W36 / 24/30.
- **Source Family / Type:** `BENCH-ROBUSTNESS-2509.04013`; evaluation paper.
- **Event Date / Revision / Access:** v1 2025-09-04; paraphrase construction, model evaluation, statistical analyses, rank comparison and conclusion read. `Full Source Review Complete`.
- **Problem / Previous Design:** Canonical benchmark prompts are reproducible but can measure prompt familiarity rather than stable capability.
- **Changed Constraint / Mechanism:** Semantically equivalent paraphrases perturb surface form while preserving intended task, testing invariance of score and ranking.
- **State / Flow / Implementation:** Original item owns semantic target; paraphraser owns variant; evaluator owns exact-match/task score; analysis separates absolute degradation from rank stability.
- **Evaluation Contract:** Multiple LLMs on original/paraphrased benchmark items; effectiveness drops while rankings are more stable. Hardware/precision/SLO are not the relevant contract and are Not Disclosed.
- **Proves / Does Not Prove:** Shows benchmark scores can overestimate robustness to wording; does not prove paraphrases are perfectly difficulty-equivalent or that all benchmarks fail similarly.
- **Trade-offs / Failure Modes / Coexistence:** Variant testing improves reliability but adds paraphrase validation cost and a new generator bias. Canonical items remain useful for longitudinal comparability.
- **Evolution / Owner:** `Direct Evolution`; `PLATFORM-EVALUATION-SYSTEM` Ch66, adjacent Ch65/67 reviewed.
- **Integration / Open:** `Books Pending`; refine sensitivity/equivalence-set contract. Open: how many validated variants are required for a stable confidence interval?

### Loong

- **Candidate / Week / Score:** Loong / 2025-W36 / 24/30.
- **Source Family / Type:** `LOONG-2509.03059`; synthetic reasoning-data/verifier paper + dataset/code.
- **Event Date / Revision / Access:** v1 2025-09-03; synthesis agents, domain pipeline, verifier strategy, evaluation, implementation and appendices read. `Full Source Review Complete`.
- **Problem / Previous Design:** Human long-CoT data are expensive; unconstrained self-generation scales but accumulates invalid questions and unverifiable chains.
- **Changed Constraint / Mechanism:** Domain-specific question/code generation is paired with programmatic/LLM verifiers, allowing scalable synthesis while retaining an explicit acceptance contract.
- **State / Flow / Implementation:** Synthesis agent owns candidate problem; code agent owns executable artifact; verifier/judge owns acceptance; dataset pipeline owns provenance. GPT-4.1-mini generates questions/code and DeepSeek-R1 judges in the disclosed experiments.
- **Evaluation Contract:** One hundred synthetic questions per domain/strategy with fixed seed sampling, downstream reasoning evaluation and strategy comparisons; verifier dependence is explicit.
- **Proves / Does Not Prove:** Shows the pipeline can generate useful author-evaluated long-CoT data; does not prove verifier correctness, contamination absence, or that longer chains are inherently better.
- **Trade-offs / Failure Modes / Coexistence:** Verification improves filtering but costs model/tool calls and can accept shared generator-verifier errors. Human-curated data remains preferable for ambiguous domains.
- **Evolution / Owner:** `Layering / Dependency`; `TRAIN-DATA` Ch27 (legacy Ch23), handoff to `PLATFORM-EVALUATION-SYSTEM` Ch66. Adjacent Ch26/28 reviewed.
- **Integration / Open:** `Books Pending`; refine executable verifier/provenance chain. Open: how is judge-model drift handled when regenerating the dataset?

### Emergent Hierarchical Reasoning through RL (HICRA)

- **Candidate / Week / Score:** HICRA / 2025-W36 / 25/30.
- **Source Family / Type:** `HICRA-2509.03646`; RL reasoning-mechanism paper + project artifact.
- **Event Date / Revision / Access:** arXiv v1 2025-09-03; later v3 2025-09-27 remains the same family. Abstract, Introduction, Strategic-Gram construction, HICRA objective, experiments, baseline comparisons, semantic-entropy analyses, sensitivity/full-dynamics appendices, implementation setup, and conclusion were read. `Full Source Review Complete` using the accessible revision while preserving v1 as owner date.
- **Original Problem / Previous Design:** Outcome-level GRPO applies a trajectory advantage broadly across generated tokens. This was reasonable when the verifier could judge only the final answer and no reliable step labels existed, but it treats procedural execution and high-level strategic choice as if they had equal learning leverage.
- **Changed Constraint / Mechanism:** Across the paper's math and vision-language runs, procedural-token uncertainty often falls early while later gains correlate with more diverse strategic patterns. HICRA constructs frequent cross-solution Strategic Grams as a functional proxy for planning spans and amplifies their group-normalized advantage by a fixed factor, concentrating policy pressure on an hypothesized strategic bottleneck.
- **State Ownership / Control Flow / Data Flow:** The policy owns rollout tokens and probabilities; the outcome verifier owns trajectory reward; the Strategic-Gram catalog and contextual matcher own the planning-token mask; GRPO owns group-normalized advantage; HICRA transforms masked-token credit before the optimizer update. Error categories are additionally classified by GPT-4o, so that diagnostic is judge-dependent evidence.
- **Implementation Details:** Strategic n-grams of length 3～5 are embedded, semantically clustered, ranked by cross-document frequency, and filtered to form a high-precision proxy. The reported HICRA runs use `alpha=0.2`; context grows from 16K to 32K when clipping exceeds 20%; training uses two to four groups of eight A100 80GB GPUs. Some Llama runs add dynamic filtering because of vanishing group advantages.
- **Evaluation Contract:** Qwen2.5-7B, Qwen3-4B, Llama-3.1-8B, Qwen2.5-VL-7B, and MiMO-VL-7B variants are trained on DAPO, DeepScaleR, or ViRL39K and evaluated on disclosed mathematical/VLM reasoning suites. Comparisons include base, GRPO, HICRA, entropy regularization, planning-token versus high-entropy-token targeting, Strategic-Gram removal sensitivity, and extended training dynamics.
- **What the Evidence Proves / Does Not Prove:** It supports a two-phase empirical description and shows targeted credit can beat the disclosed GRPO baselines on many, but not every, model/benchmark cell. It does not establish that surface Strategic Grams are latent plans, that the hierarchy transfers to arbitrary domains, or that semantic-entropy correlation proves causality.
- **Trade-offs / New Failure Modes / Coexistence:** Targeted credit can reduce wasted updates, but it adds a mined lexicon, clustering thresholds, language/style bias, mask errors, and another hyperparameter; it can under-credit silent or nonverbal planning. Uniform token credit remains preferable when the planning proxy is unreliable or reasoning is not expressed in reusable phrases.
- **Evolution Relationship / Owner:** `Alternative Branch`; `TRAIN-GRPO` Ch33 (legacy Ch29), with handoff to `PLATFORM-EVALUATION-SYSTEM` Ch66 for diagnostic validity. Adjacent Ch32/34 and Ch65/67 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Books already distinguish reward ownership and credit assignment but not hierarchy-conditioned token masks. `Books Pending` behind Historical Books Gate. Open: can causal intervention on identified spans separate planning leverage from linguistic marker leakage?

### Hunyuan-MT Technical Report

- **Candidate / Week / Score:** Hunyuan-MT / 2025-W36 / 24/30.
- **Source Family / Type:** `HUNYUAN-MT-2509.05209`; technical report + open model weights + official repository.
- **Event Date / Revision / Access:** arXiv v1 2025-09-05; later v2 2025-09-09 remains the same family. Pre-training data, two-stage SFT, RL, weak-to-strong fusion, prompts, evaluation metrics, ablations, case studies, human evaluation, conclusion, model cards, and repository were reviewed. `Full Source Review Complete` using the accessible revision while preserving v1 as owner date.
- **Original Problem / Previous Design:** One-pass translation is cheap and operationally simple, but a single decoding path cannot exploit complementary hypotheses; free-form CoT was a plausible slow-thinking alternative yet final-answer-only reward produced boilerplate reasoning with no measured benefit in this workload.
- **Changed Constraint / Mechanism:** Quality-critical multilingual and low-resource translation can spend more test-time compute. A base 7B model generates six candidates under varied settings; a specialized Chimera model consumes the source plus candidate portfolio and synthesizes one answer. Its weak-to-strong GRPO reward combines XCOMET-XXL, DeepSeek-V3-0324 judgment, and a repetition penalty.
- **State Ownership / Control Flow / Data Flow:** The base translator owns candidate hypotheses; inference orchestration owns diversity parameters and the six-candidate bundle; the Chimera model owns synthesis; automatic metrics and human raters own evaluation. Candidate identity, order, source text, target language, and model/reward versions therefore become explicit inference state.
- **Implementation Details:** General pre-training includes a 1.3T-token, 112-language/dialect component governed by a proprietary three-axis quality assessor; MT pre-training is followed by two-stage SFT over roughly three million parallel pairs plus general/MT instruction data, then RL and weak-to-strong RL. Exact training hardware, precision, batch, runtime concurrency, and production SLO are `Not Disclosed`.
- **Evaluation Contract:** Flores-200 across 1,056 selected directions, 29 WMT24pp pairs overlapping WMT25, Mandarin↔minority sets, general capability suites, XCOMET-XXL/CometKiwi, targeted human evaluation, training-stage ablations, and CoT reward comparisons are reported. The paper reports a 2.3% average XCOMET-XXL gain for Chimera over its base across Flores directions, but this remains author evidence under its metric/candidate budget.
- **What the Evidence Proves / Does Not Prove:** It demonstrates that learned multi-candidate synthesis can improve the disclosed translation evaluations and that outcome-only CoT did not help their setup. It does not prove universal superiority over single-pass decoding, unbiased neural metrics, robust low-resource coverage outside sampled languages, or favorable latency/cost under an external SLO.
- **Trade-offs / New Failure Modes / Coexistence:** Candidate generation multiplies decode compute and tail latency; synthesis can erase a correct minority hypothesis, inherit correlated errors, or optimize to reward-model bias. Single-pass translation remains appropriate for latency- or cost-bound traffic; reranking may be preferable when synthesis risk exceeds complementarity gain.
- **Evolution Relationship / Owner:** `Alternative Branch`; `INFER-SPECULATIVE-DECODING` Ch48 for proposal/selection/commit semantics, with handoffs to `TRAIN-RLHF` Ch31 and `PLATFORM-EVALUATION-SYSTEM` Ch66. Adjacent Ch47/49 and Ch30/32 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Books cover speculative candidates and verifier boundaries but not generative fusion as a quality-first branch. `Books Pending` behind Historical Books Gate. Open: at what candidate diversity and SLO does synthesis dominate best-of-N reranking after accounting for correlated metric error?

### Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs

- **Candidate / Week / Score:** Flaw or Artifact? / 2025-W36 / 24/30.
- **Source Family / Type:** `PROMPT-SENSITIVITY-EVAL-2509.01790`; evaluation-method research paper.
- **Event Date / Revision / Access:** arXiv v1 2025-09-01; Abstract through Conclusion, prompt construction, judging protocol, human study, sensitivity/ranking analyses, appendices and limitations read. `Full Source Review Complete`.
- **Original Problem / Previous Design:** Exact-match and format heuristics are cheap, deterministic, and easy to reproduce, so they were reasonable when tasks prescribed a narrow answer schema. They can nevertheless classify semantically correct variants as failures and make surface-form changes look like capability instability.
- **Changed Constraint / Mechanism:** Once outputs contain explanations, paraphrases, or formatting variation, evaluation must separate semantic correctness from serialization compliance. The paper creates twelve prompt templates and compares heuristics with an LLM judge that receives the question, reference answer, and candidate response.
- **State Ownership / Control Flow / Data Flow:** The benchmark item owns the intended task and reference; the prompt generator owns surface variants; the model owns its response; the parser and LLM judge own distinct acceptance decisions; the analysis layer owns variance and rank-correlation estimates. Those identities cannot be collapsed into one scalar score without losing the source of variation.
- **Implementation Details:** GPT-4o paraphrases templates; four open and three closed models are decoded across six multiple-choice/open-ended benchmarks. Benchmark-specific judge instructions are used where explanations must be ignored, and a human study checks judge agreement.
- **Evaluation Contract / Hardware / SLO:** Twelve prompts per benchmark, heuristic and judge scoring, within-model score variance, cross-model Spearman ranking, and human agreement are reported. Inference hardware, precision, batch, concurrency, latency, and production SLO are `Not Disclosed` and are not established by the paper.
- **What the Evidence Proves / Does Not Prove:** It shows that heuristic parsing can materially exaggerate prompt sensitivity in the disclosed suite and that judge-based rankings align better with the study's human labels. It does not prove that LLM judges are unbiased, that all prompt variants preserve equal difficulty, or that model sensitivity disappears.
- **Trade-offs / New Failure Modes / Coexistence:** Semantic judging reduces parser artifacts but adds judge-model bias, cost, nondeterminism, and prompt dependence. Exact match remains preferable for executable or uniquely serialized answers; robust evaluations should report both task behavior and evaluator behavior.
- **Evolution Relationship / Owner:** `Direct Evolution`; `PLATFORM-EVALUATION-SYSTEM` Ch66, with handoff to `AGENT-PROMPT` Ch74. Adjacent Ch65/67 and Ch73/75 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Existing Books distinguish model and harness but do not explicitly assign prompt-variant and parser identity. `Books Pending`. Open: what human-audited operating point is sufficient before an LLM judge can replace deterministic scoring?

### Manipulation as in Simulation

- **Candidate / Week / Score:** Manipulation as in Simulation / 2025-W36 / 24/30.
- **Source Family / Type:** `MANIPULATION-SIM-GEOMETRY-2509.02530`; embodied-perception and robot-data research paper + project artifact.
- **Event Date / Revision / Access:** arXiv v1 2025-09-02; sensor-noise modeling, Camera Depth Models, WBCMimicGen, robot pipeline, simulation/real experiments, depth comparisons, failure cases and appendices read. `Full Source Review Complete`.
- **Original Problem / Previous Design:** Training manipulation policies directly on simulated geometry is attractive because states and labels are exact, while using raw commodity depth at deployment is simple. The boundary appears when systematic holes, reflections, and camera-specific noise shift the observation distribution and destabilize the control loop.
- **Changed Constraint / Mechanism:** Instead of asking one policy to absorb the full sim-to-real gap, the work learns camera-specific depth correction from RGB plus noisy depth and makes synthetic demonstrations obey whole-body kinematic constraints. Perception is therefore adapted toward simulation-quality geometry before low-level action learning consumes it.
- **State Ownership / Control Flow / Data Flow:** The physical camera owns raw RGB/depth; the correction model owns a revised metric-depth estimate; the simulator owns clean geometry and degradation pairs; WBCMimicGen owns feasible demonstration trajectories; the policy owns action chunks; the controller and environment own execution and feedback. A corrected observation remains an estimate, not authoritative world state.
- **Implementation Details:** Camera degradation is learned and supplemented with handcrafted high-frequency noise; corrected depth feeds an imitation-learning stack. The disclosed system uses UR5/Robotiq-class manipulation and RealSense-family depth sensors, while velocity regularization and joint limits reduce acceleration/jerk at action-chunk boundaries.
- **Evaluation Contract / Hardware / SLO:** Depth quality, camera transfer, trajectory smoothness, simulation success, and real kitchen/canteen manipulation are compared with source-camera and MimicGen baselines. Training precision, batch, broad concurrency, and deployment SLO are `Not Disclosed`; success rates are author evidence for the disclosed tasks and embodiments.
- **What the Evidence Proves / Does Not Prove:** It supports factoring geometry correction from policy learning and shows smoother generated demonstrations can improve the reported tasks. It does not prove universal camera transfer, policy robustness to arbitrary geometry errors, or that corrected depth is safe enough for unbounded physical autonomy.
- **Trade-offs / New Failure Modes / Coexistence:** The extra perception stage improves geometry but adds calibration/version state, latency, domain-specific training, and a new correlated-error path. The paper documents failures when a large erroneous depth region is not recoverable from RGB semantics. Raw depth or end-to-end policies remain appropriate when sensors are reliable or latency/calibration costs dominate.
- **Evolution Relationship / Owner:** `Layering / Dependency`; `MULTIMODAL-EMBODIED-VLA` Ch26, with handoff to `MULTIMODAL-WORLD-MODELS` Ch25 and `PLATFORM-EVALUATION-SYSTEM` Ch66. Adjacent Ch25 and Ch27 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Books describe perception-action feedback but not camera-specific observation correction as an owned pre-policy state. `Books Pending`. Open: what runtime monitor can distinguish correctable sensor noise from a hazardous model hallucination?

### Inverse IFEval

- **Candidate / Week / Score:** Inverse IFEval / 2025-W36 / 23/30.
- **Source Family / Type:** `INVERSE-IFEVAL-2509.04292`; bilingual instruction-following benchmark and evaluation paper.
- **Event Date / Revision / Access:** event-time arXiv v1 2025-09-04; v1 PDF read across construction, taxonomy, human-in-the-loop filtering, judge optimization/calibration, model experiments, cases, appendices and limitations. `Full Source Review Complete`; later revisions remain this family.
- **Original Problem / Previous Design:** SFT standardizes desirable response forms, which improves ordinary instruction following and safety. The same regularity can become cognitive inertia when a legitimate instruction asks the model to violate a learned convention, such as preserve an intentional flaw or avoid a habitual explanation.
- **Changed Constraint / Mechanism:** The benchmark reverses familiar instruction-following expectations through eight counter-intuitive categories and evaluates whether a model follows the actual request instead of the dominant training convention. Human review and judge calibration make the evaluator contract explicit rather than treating an uncalibrated model score as truth.
- **State Ownership / Control Flow / Data Flow:** Dataset authors own the intended inverse constraint and reference; human reviewers own item validity; the candidate model owns its response; the judge owns classification under a versioned prompt; calibration examples and audits own the judge operating point. A model's habitual answer and the task's requested answer are deliberately distinct states.
- **Implementation Details:** The released set contains 1,012 Chinese/English questions across 23 domains. The pipeline combines generation, filtering, human inspection, and an optimized LLM-as-a-Judge protocol; the paper reports improving judge agreement from 88% to 98% during calibration.
- **Evaluation Contract / Hardware / SLO:** Leading disclosed LLMs are compared across the eight categories and two languages, with human-calibrated judging and category analyses. Model-serving hardware, precision, batch, concurrency, latency, and SLO are `Not Disclosed`; benchmark results do not establish deployment reliability.
- **What the Evidence Proves / Does Not Prove:** It demonstrates a measurable failure mode where learned response conventions can override explicit instructions in this dataset. It does not prove the cause is only SFT, that every unusual instruction should be obeyed, or that the calibrated judge generalizes to unseen constraint families.
- **Trade-offs / New Failure Modes / Coexistence:** Greater adaptability can reduce convention bias but may weaken safety defaults or invite adversarial requests. Stable conventions remain valuable when user intent is ambiguous or conflicts with policy; evaluation must separate task obedience from policy compliance.
- **Evolution Relationship / Owner:** `Alternative Branch`; `PLATFORM-EVALUATION-SYSTEM` Ch66, with handoff to `TRAIN-SFT` Ch29 and `PLATFORM-SECURITY` Ch72. Adjacent Ch65/67, Ch28/30, and Ch71/73 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Books cover instruction-following and evaluation but not convention-conflict tests as a separate axis. `Books Pending`. Open: how should a production evaluator label deliberate noncompliance when the inverse instruction conflicts with policy?

### Transition Models

- **Candidate / Week / Score:** Transition Models / 2025-W36 / 25/30.
- **Source Family / Type:** `TRANSITION-MODELS-2509.04394`; generative-learning objective paper + official code.
- **Event Date / Revision / Access:** arXiv v1 2025-09-04; PF-ODE derivation, arbitrary-interval identity, DDE approximation, architecture, training/sampling algorithms, experiments, ablations, connections, implementation appendices and limitations read. `Full Source Review Complete`.
- **Original Problem / Previous Design:** Diffusion objectives learn local dynamics and rely on many numerical steps for fidelity; endpoint/consistency objectives make few-step generation cheap but can impose a quality ceiling. Each was reasonable for its own fixed sampling budget.
- **Changed Constraint / Mechanism:** A single generator must support both short and long transitions and improve monotonically when more compute is available. TiM conditions on start and target times and learns a finite-interval state transition; a forward-pass finite-difference Differential Derivation Equation replaces a JVP that conflicts with FlashAttention/FSDP-style scaling.
- **State Ownership / Control Flow / Data Flow:** The noisy latent and two time coordinates define the mutable generation state; the transition network owns the proposed next state; the sampler owns interval decomposition; classifier-free guidance and autoencoder own conditioning/representation boundaries. Intermediate states remain provisional until the sampling schedule terminates.
- **Implementation Details:** Decoupled time embeddings and interval-aware attention expose absolute position and interval length; short-transition weighting stabilizes high-variance long jumps. The main text reports an 865M DiT-family model trained on 33M public images and includes from-scratch/native-resolution strategies.
- **Evaluation Contract / Hardware / SLO:** ImageNet-256 FID ablations and GenEval, MJHQ30K, and DPGBench text-to-image comparisons span one to many NFEs. The DDE-vs-JVP systems microbenchmark uses TiM-B/4, batch 256, BF16 on one NVIDIA A100; that setup reports roughly 2× operator latency improvement and FSDP compatibility, not an end-to-end fleet SLO.
- **What the Evidence Proves / Does Not Prove:** Author experiments support arbitrary-step training, monotonic disclosed quality across sampling budgets, and the scalability benefit of forward-only DDE in the measured setup. They do not prove generality beyond the image workloads, superiority under matched data/compute for every baseline, or production latency/cost.
- **Trade-offs / New Failure Modes / Coexistence:** Interval conditioning and derivative approximation add objective complexity, weighting sensitivity, and long-jump instability. The paper reports text/hand fidelity failures and high-resolution artifacts tied partly to the autoencoder. Standard diffusion remains valid when maximum quality and mature solvers matter; distilled endpoint models remain useful for fixed tiny budgets.
- **Evolution Relationship / Owner:** `Alternative Branch`; `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24, with execution-plan handoff to `INFER-TENSORRT-LLM` Ch49. Adjacent Ch23/25 and Ch48/50 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Books compare AR, diffusion, masked, and hybrid correction but do not yet express finite-interval learning as its own compute-quality branch. `Books Pending`. Open: can the monotonic quality property survive video duration, autoregressive conditioning, and serving-time adaptive budgets?

### Delta Activations

- **Candidate / Week / Score:** Delta Activations / 2025-W36 / 23/30.
- **Source Family / Type:** `DELTA-ACTIVATIONS-2509.04442`; model-representation/reuse research paper.
- **Event Date / Revision / Access:** arXiv v1 2025-09-04; formulation, model-pool construction, clustering and sensitivity experiments, task/model-selection extensions, full-finetuning appendix and limitations read. `Full Source Review Complete`.
- **Original Problem / Previous Design:** Model registries reasonably rely on names, cards, training metadata, and benchmark profiles, but community fine-tunes often have incomplete metadata and expensive, non-comparable evaluations. Raw weight distance is also a poor semantic index.
- **Changed Constraint / Mechanism:** A registry needs a cheap behavioral representation derivable from the artifact itself. Delta Activations runs a fixed generic probe through a base and its fine-tune, subtracts internal hidden states, and averages the shifts into a vector used for clustering, retrieval, and bounded reuse experiments.
- **State Ownership / Control Flow / Data Flow:** The base model and fine-tuned artifact jointly own the delta identity; the probe set and selected layer/token own the measurement protocol; the registry owns the stored vector and lineage; a downstream selector may query it but must not treat similarity as task correctness.
- **Implementation Details:** Three pools based on Llama-3.1-8B, Gemma-2-9B, and Qwen2.5-7B contain fifteen models each across five domains. Default LoRA runs use 3,000 examples, three epochs, learning rate `1e-4`, batch 4; prompt-count/content, layer/token, learning-rate, data-size, epoch, DPO, full-finetuning, and cross-base variants are ablated.
- **Evaluation Contract / Hardware / SLO:** Silhouette score compares delta vectors with flattened weights, saliency masks, and output embeddings; few-shot task retrieval, additive mixtures, and model-selection/merging cases are exploratory. Training uses disclosed H100-class hardware in the appendix, but registry throughput, proprietary-model access, concurrency, and SLO are `Not Disclosed`.
- **What the Evidence Proves / Does Not Prove:** It shows strong domain clustering for the constructed pools and robustness to several finetuning settings; it does not prove that vector proximity predicts quality, that additivity is causal, or that incompatible/proprietary architectures can share an activation space.
- **Trade-offs / New Failure Modes / Coexistence:** The vector is cheap after loading both artifacts but requires internal-state access, a known base, a versioned probe, and layer compatibility. Probe leakage, lineage mistakes, and false similarity can misroute models; model cards and task-specific evaluation remain authoritative for release decisions.
- **Evolution Relationship / Owner:** `Layering / Dependency`; `PLATFORM-MODEL-REGISTRY` Ch59, with handoff to `PLATFORM-EVALUATION-SYSTEM` Ch66 and `TRAIN-LORA` Ch30. Adjacent Ch58/60, Ch65/67, and Ch29/31 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Books cover lineage and evaluation profiles but not activation-delta indexing as a conditional discovery aid. `Books Pending`. Open: how should a registry invalidate embeddings when tokenizer, probe set, base checkpoint, or precision changes?

### False Sense of Security: Why Probing-based Malicious Input Detection Fails to Generalize

- **Candidate / Week / Score:** False Sense of Security / 2025-W36 / 26/30.
- **Source Family / Type:** `WHY-PROBE-FAILS-2509.03888`; safety-detection/evaluation research paper + official repository.
- **Event Date / Revision / Access:** arXiv v1 2025-09-04; problem formulation, OOD setup, three controlled studies, layer/classifier analyses, dataset and prompt appendices, discussion, conclusion, and repository identity read. `Full Source Review Complete`.
- **Original Problem / Previous Design:** A lightweight classifier over frozen hidden states is cheap and reports near-perfect in-distribution malicious/benign separation, so it was a plausible runtime safety detector. That contract silently assumed representation separability meant stable harmful semantics.
- **Changed Constraint / Mechanism:** Safety traffic shifts across phrasing, datasets, and attack styles. The paper tests probes out of distribution, compares them with n-gram Naive Bayes, removes harmful semantics while preserving structure, paraphrases structure, and injects trigger words into benign prompts to identify what the classifier actually uses.
- **State Ownership / Control Flow / Data Flow:** The base LLM owns frozen hidden states; dataset construction owns labels and spurious correlations; the probe owns a binary decision; policy enforcement owns the final allow/block action. Because the detector observes representation patterns rather than verified intent, its score cannot own the safety decision alone.
- **Implementation Details:** Last-token/last-layer SVM probes are evaluated across Gemma-3, Llama-3.1, and Qwen2.5 instruction models and multiple benign/malicious datasets; first/middle/last layers, logistic regression, and a small MLP are also tested. GPT-4o creates controlled sanitizations/paraphrases, which is itself an acknowledged generator dependency.
- **Evaluation Contract / Hardware / SLO:** ID/OOD accuracy, cleaned/paraphrased controls, XSTest trigger-word false positives, layer and classifier ablations form the contract. ID accuracy exceeds 98% in the disclosed cells while OOD drops by 15～99 percentage points; training/serving hardware, precision, batch, concurrency, latency, and SLO are `Not Disclosed`.
- **What the Evidence Proves / Does Not Prove:** It demonstrates severe spurious-cue dependence for the tested probing recipes and datasets and falsifies the inference that high ID accuracy alone establishes semantic safety detection. It does not prove all representation probes fail, that the underlying LLM lacks harmfulness information, or that the controlled transformations are perfect.
- **Trade-offs / New Failure Modes / Coexistence:** Probes remain cheap signals but require shift-aware validation, policy-layer redundancy, calibrated thresholds, and monitoring for false positives/negatives. More semantic or tool-backed verification costs latency and can still share model bias; simple probes remain useful as one ensemble feature, not a sole gate.
- **Evolution Relationship / Owner:** `Direct Evolution`; `PLATFORM-SECURITY` Ch72, with handoff to `PLATFORM-EVALUATION-SYSTEM` Ch66 and `PLATFORM-MONITORING` Ch67. Adjacent Ch71/73 and Ch65/68 reviewed.
- **Existing Coverage / Integration Decision / Open Questions:** Books already require threat models and operating points but do not explicitly treat OOD semantic controls as a release condition for activation probes. `Books Pending`. Open: which shift families and false-negative budgets should gate deployment of a probe-based detector?

### Kubernetes DRA GA design details

- **Candidate / Week / Score:** Kubernetes DRA GA design details / 2025-W36 / 26/30.
- **Source Family / Type:** `K8S-DRA-1.34`; official design follow-up + API docs/KEP.
- **Event Date / Revision / Access:** official post 2025-09-01; v1.34 core GA remains owned by W35. Blog, DRA docs, API kinds, allocation flow and KEP maturity read. `Full Source Review Complete`.
- **Problem / Previous Design:** A release headline collapses core GA, beta options, and alpha capacity/health/binding features into one misleading status.
- **Changed Constraint / Mechanism:** DeviceClass/ResourceClaim/ResourceSlice core is stable while admin access/prioritized alternatives and capacity/health/binding features retain different maturity and gates.
- **State / Flow / Implementation:** API server owns desired/allocation state; scheduler selects; driver/kubelet prepare devices and report driver-owned state; admission/RBAC/feature gates remain operator-owned.
- **Evaluation Contract:** Kubernetes API graduation/conformance evidence; no AI workload performance benchmark. Hardware/model/precision/length/batch/concurrency/SLO are Not Applicable/driver-specific.
- **Proves / Does Not Prove:** Proves stability must be tracked per feature, not per release headline; does not prove every vendor driver implements v1 or automatic recovery.
- **Trade-offs / Failure Modes / Coexistence:** Extensibility removes scheduler hard-coding but adds driver correctness, control-plane skew, admission, portability, and upgrade ordering. Extended resources remain adequate for simple non-shareable devices.
- **Evolution / Owner:** `Layering / Dependency`; W35 core GA → W36 maturity map. `PLATFORM-GPU-SCHEDULER` Ch63 (legacy Ch59), adjacent Ch62/64 reviewed.
- **Integration / Open:** `Refine — Existing Argument`, but Historical Books Gate is closed. Open: how should a platform test driver/API/feature-gate skew before rollout?

## Low-Score Source / Date / Rejection Closure

All entries below have a verified primary identity and first-public date. None is `Review Pending`.

| Source Family | Primary Identifier | Date Closure | Evidence Closure / Rejection Reason |
| --- | --- | --- | --- |
| `AGENTIC-RL-SURVEY` | arXiv:2509.02547 | v1 2025-09-02 | Survey taxonomy is useful discovery but cannot be counted as a new primary mechanism. |
| `REASONING-VECTORS` | arXiv:2509.01363 | v1 2025-09-01 | Task-arithmetic transfer is author evidence with limited scale/robustness coverage; Experimental. |
| `POINTS-READER` | arXiv:2509.01215 | v1 2025-09-01 | Distillation-free VLM adaptation is bounded to document conversion; no general system conclusion. |
| `GATED-ASSOCIATIVE-MEMORY` | arXiv:2509.00605 | v1 2025-09-01 | Parallel O(N) sequence architecture is promising but lacks evidence sufficient to alter the Transformer/long-context baseline. |
| `KEYE-VL-1.5` | arXiv:2509.01563 | v1 2025-09-01 | Model-report benchmark gains are not generalized beyond disclosed data/model settings. |
| `IMPLICIT-AC-RLVR` | arXiv:2509.02522 | v1 2025-09-02 | Supervised actor-critic coupling remains a bounded algorithmic branch. |
| `GENCOMPOSITOR` | arXiv:2509.02460 | v1 2025-09-02 | Narrow video compositing mechanism; low project relevance. |
| `DIVERSITY-QUALITY-RL` | arXiv:2509.02534 | v1 2025-09-02 | Diversity/quality reward coupling lacks long-horizon and cross-domain evidence. |
| `OPTIMIZER-BENCH-2509` | arXiv:2509.01440 | v1 2025-09-01 | Useful bounded comparison; not a universal optimizer ranking without matched scale/hardware budgets. |
| `MOONSHINE-FLAVORS` | arXiv:2509.02523 | v1 2025-09-02 | Edge ASR specialization retained as workload evidence only. |
| `DCPO` | arXiv:2509.02333 | v1 2025-09-02 | Dynamic clipping is an Experimental PPO branch; sensitivity/generalization remain insufficient. |
| `FLASHADVENTURE` | arXiv:2509.01052 | v1 2025-09-01 | Full-story game harness is a useful GUI-agent case but cannot isolate model from environment opportunity. |
| `FANTASTIC-OPTIMIZERS` | arXiv:2509.02046 | v1 2025-09-02 | Author comparison is retained; no deployment-independent optimizer conclusion. |
| `M3RET` | arXiv:2509.01360 | v1 2025-09-01 | Medical multimodal retrieval evidence is domain-bound and scored below core. |
| `VISTA-SLAM` | arXiv:2509.01584 | v1 2025-09-01 | Robotics perception specialization; no new AI-system owner. |
| `ROBIX` | arXiv:2509.01106 | v1 2025-09-01 | Identity/abstract verified; arXiv HTML returned an internal error and event-time full PDF was not recoverable in this run. `Unverified / Blocked`. |
| `LUXDIT` | arXiv:2509.03680 | v1 2025-09-03 | Lighting-estimation diffusion specialization; no durable cross-workload conclusion. |
| `WILDSCORE` | arXiv:2509.04744 | v1 2025-09-05 | Symbolic-music benchmark is retained as a domain evaluation fact. |
| `LATTICEWORLD` | arXiv:2509.05263 | v1 2025-09-05 | LLM+UE5 world generation remains Experimental and is not equivalent to a predictive causal world model. |
| `WINT3R` | arXiv:2509.05296 | v1 2025-09-05 | Streaming 3D reconstruction is a perception subsystem, not a general world-state solution. |
| `EXIT-TASK-SPACE` | arXiv:2509.04575 | v1 2025-09-04 | Autocurriculum self-improvement is promising but bounded to disclosed tasks and evaluator. |
| `U-ARM` | arXiv:2509.02437 | v1 2025-09-02 | Low-cost teleoperation improves data collection economics but does not establish policy learning quality. |
| `BEHAVIOR-FINGERPRINT` | arXiv:2509.04504 | v1 2025-09-02 | Eighteen-model diagnostic suite depends on LLM-as-judge and persona constructs; Emerging only. |
| `MEDVISTA3D` | arXiv:2509.03800 | v1 2025-09-04 | Medical 3D VLM evidence remains domain/model-bound. |
| `SYMBOLIC-GRAPHICS-RL` | arXiv:2509.05208 | v1 2025-09-05 | SVG programming with verifiable rewards is an Experimental artifact-producing workflow case. |
| `TEXTUAL-GENES-2509.02040` | arXiv:2509.02040 | v1 2025-09-02 | LLM-simulated genetic search for conditional data synthesis is an interesting generator/selection loop, but evidence is bounded to disclosed synthetic-image conditions and does not establish general data-quality control. |
| `DISCRETE-NOISE-INVERSION-2509.01984` | arXiv:2509.01984 | v1 2025-09-02 | Inversion adapted to next-scale autoregressive image editing is a narrow generation mechanism without cross-workload runtime or controllability evidence. |
| `AMBEDKAR-2509.02133` | arXiv:2509.02133 | v1 2025-09-02 | Knowledge-augmented speculative decoding for constitutional bias mitigation remains an experimental safety branch; external threat-model, latency, and generalization contracts are missing. |
| `PANEL-OF-PEERS-2509.01610` | arXiv:2509.01610 | v1 2025-09-01 | Iterative LVLM peer evaluation reduces human-label demand in the author benchmarks, but correlated peer errors and self-generated preference validity remain unresolved. |
| `MEDDINOV3-2509.02379` | arXiv:2509.02379 | v1 2025-09-02 | Foundation-vision adaptation is evaluated for medical segmentation only; useful domain evidence, not a new general multimodal owner. |
| `POINT-CROSS-RECON-2509.01250` | arXiv:2509.01250 | v1 2025-09-01 | Decoupled-view cross reconstruction is specific to point-cloud pretraining and lacks evidence that changes the general representation/data pipeline. |
| `MOSAIC-2509.01977` | arXiv:2509.01977 | v1 2025-09-02 | Correspondence-aware multi-subject personalization is a bounded image-generation technique; identity fidelity results do not establish a durable AI-system mechanism. |
| `DRIVELOLOGY-2509.03867` | arXiv:2509.03867 | v1 2025-09-04 | Nonsense-interpretation tasks expose a diagnostic corner of LLM reasoning, but the benchmark does not isolate a reusable mechanism or deployment contract. |
| `EDITOR-TO-GEOMETRY-2509.04338` | arXiv:2509.04338 | v1 2025-09-04 | Repurposing a diffusion editor for dense geometry is promising transfer evidence, but remains an experimental perception specialization with no broad systems result. |
| `NER-RETRIEVER-2509.04011` | arXiv:2509.04011 | v1 2025-09-04 | Type-aware embeddings improve the disclosed zero-shot named-entity retrieval task; the typed-index idea is retained without generalizing its benchmark to RAG retrieval. |
| `FEW-STEP-3D-FLOW-2509.04406` | arXiv:2509.04406 | v1 2025-09-04 | Marginal-data transport distillation is a bounded few-step 3D-generation branch; compute/quality claims are not portable outside the disclosed generator and datasets. |
| `DURIAN-2509.04434` | arXiv:2509.04434 | v1 2025-09-04 | Dual-reference portrait animation targets a narrow media workload and does not alter the general multimodal generation contract. |
| `RAY-2.49.1` | PyPI/GitHub Ray 2.49.1 | 2025-09-03 | Patch artifact verified; no durable mechanism disclosed separately from 2.49.0. |
| `TRTLLM-1.1.0RC3` | PyPI/GitHub prerelease | 2025-09-04 | Prerelease identity verified; production stability and final contract not established. |
| `OPENAI-SENSITIVE-ROUTING-PLAN` | OpenAI official post | 2025-09-02 | Official planned product behavior only; router/model mechanism and evaluation contract not disclosed. |
| `ANTHROPIC-REGIONAL-RESTRICTIONS` | Anthropic official policy | 2025-09-04 | Governance policy fact; no model/runtime mechanism. |

## Exact Materials Request

| Priority | Week | Source Family | Known Identity | Missing Material | Why Current Evidence Is Insufficient | Acceptable Substitute | Suggested Filename | Audit After Recovery |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 Full Text | 2025-W36 | `ROBIX` | arXiv:2509.01106, v1 2025-09-01 | Event-time v1 PDF or lossless HTML/TXT/Markdown, plus artifact revision if available | Title, authors, abstract, and date are verified, but Method, implementation, evaluation contract, ablations, limitations, and appendices could not be read; the current 19/30 is provisional evidence closure, not a final mechanism judgment | Author manuscript, institutional mirror, or a user-downloaded arXiv v1 PDF with checksum/source URL | `2509.01106v1-robix.pdf` | Re-read full paper/artifact, recompute six-dimensional score, upgrade to Full Source Review if `20+`, and reconcile owner/adjacent chapters |

## Evidence Level

| Evidence Class | Count | Meaning |
| --- | ---: | --- |
| A — Primary mechanism + implementation/evaluation reviewed | 24 | All `20+` candidates; official paper/report/docs were read beyond abstract and received Full Source Review. |
| B — Primary identity/date and bounded result/release reviewed | 36 | Below-threshold candidates with enough primary evidence for a specific Weekly-only, Emerging, or rejection disposition. |
| C — Official policy/version fact; mechanism not disclosed | 4 | Ray, TensorRT-LLM prerelease, OpenAI routing plan, and Anthropic restrictions remain narrow facts, not inferred mechanisms. |
| D — Identity/abstract verified; full mechanism blocked | 1 | Robix only; exact material request above. |

Evidence accounting: `24 + 36 + 4 + 1 = 65`. `Review Pending = 0`; `Unverified / Blocked = 1` under the approved blocked-skip rule.

## Cross-Week Deduplication and Spillback

### W35 owners discovered during W36 replay

The following eleven source families are not W36 events because their first-public dates fall in W35. The first seven were recovered during the reopened W35 review. The final four were exposed only after the complete W36 feed reconciliation and still require W35 reclosure. None is counted or scored in this Weekly.

| Primary Identifier | Candidate | v1 / First Public | W35 Ledger Check | Routing Decision |
| --- | --- | --- | --- | --- |
| arXiv:2509.00676 | LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model | 2025-08-31 | Recovered | Resolved in reopened W35; not a W36 score |
| arXiv:2509.00404 | Metis: Training LLMs with FP4 Quantization | 2025-08-30 | Recovered | Resolved in reopened W35; not a W36 score |
| arXiv:2509.00375 | Open Data Synthesis For Deep Research | 2025-08-30 | Recovered | Resolved in reopened W35; not a W36 score |
| arXiv:2509.00425 | The Gold Medals in an Empty Room: Diagnosing Metalinguistic Reasoning in LLMs with Camlang | 2025-08-30 | Recovered | Resolved in reopened W35; not a W36 score |
| arXiv:2509.00581 | SQL-of-Thought: Multi-agentic Text-to-SQL with Guided Error Correction | 2025-08-30 | Recovered | Resolved in reopened W35; not a W36 score |
| arXiv:2509.00930 | SATQuest: A Verifier for Logical Reasoning Evaluation and Reinforcement Fine-Tuning of LLMs | 2025-08-31 | Recovered | Resolved in reopened W35; not a W36 score |
| arXiv:2508.21496 | ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Long Video Understanding | 2025-08-29 | Recovered | Resolved in reopened W35; not a W36 score |
| arXiv:2509.00244 | Universal Deep Research | 2025-08-29 | Recovered | Resolved in second W35 reclosure; removed from W36 scoring |
| arXiv:2509.00428 | Mixture of Global and Local Experts with Diffusion Transformer | 2025-08-30 | Recovered | Resolved in second W35 reclosure; not a W36 score |
| arXiv:2509.00531 | MobiAgent | 2025-08-30 | Recovered | Resolved in second W35 reclosure; not a W36 score |
| arXiv:2509.00578 | C-DiffDet+ | 2025-08-30 | Recovered | Resolved in second W35 reclosure; not a W36 score |

### W37 discovery/revision spillback reconciled to W36

- Later feeds/revisions for arXiv:2509.03646, 2509.04013, 2509.04185, 2509.04504, 2509.04575, 2509.04664, 2509.05209, 2509.05263, and 2509.05296 resolve to W36 by v1 date. All nine now have exactly one W36 ledger row; W37 must treat later revisions as same-family evolution, not new events.
- Kubernetes DRA core GA remains a W35 event. The Sep 1 W36 item is a design/maturity clarification in the same `K8S-DRA-1.34` family and is explicitly marked `Layering / Dependency`, not scored as another GA announcement.
- Ray 2.49.1 is a patch descendant of the W35 2.49.0 family; the W36 row records the dated patch fact but does not claim a new durable mechanism.
- No duplicate primary identifier or Source Family remains inside the 65-row W36 canonical ledger.

## Knowledge Tree Position

| Mechanism Line | Canonical Owner | Adjacent Handoff |
| --- | --- | --- |
| Stateful agent rollout, environment lease, recovery, trajectory identity | `AGENT-WORKFLOW` Ch81 | `TRAIN-PPO` Ch32; `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| Tool-integrated reasoning and executable verifier loops | `AGENT-TOOL-CALLING` Ch78 / `AGENT-WORKFLOW` Ch81 | `TRAIN-GRPO` Ch33; Ch66 |
| Online/offline post-training gradients, process/outcome rewards, hierarchical credit | `TRAIN-RLHF` Ch31 / `TRAIN-GRPO` Ch33 | `TRAIN-DPO` Ch34; Ch66 |
| Hallucination incentives, benchmark invariance, harness/evaluator contract | `PLATFORM-EVALUATION-SYSTEM` Ch66 | `WORLDVIEW-WHY-MODELS-LEARN` Ch4; `AGENT-RAG` Ch76 |
| Prompt variants, inverse instruction generation, parser/judge/human-calibration pipeline | `PLATFORM-EVALUATION-SYSTEM` Ch66 | `PLATFORM-MONITORING` Ch67; `AGENT-PROMPT` Ch74 |
| Set-valued or multi-candidate proposal, correction, synthesis, commit | `INFER-SPECULATIVE-DECODING` Ch48 | `INFER-KV-CACHE` Ch45; `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 |
| Arbitrary-interval state transition and iterative generative correction | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 | `MULTIMODAL-WORLD-MODELS` Ch25; `INFER-SPECULATIVE-DECODING` Ch48 |
| Camera-conditioned observation correction before physical action | `MULTIMODAL-EMBODIED-VLA` Ch26 | `MULTIMODAL-WORLD-MODELS` Ch25; `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| Activation-delta identity for model discovery and registry comparison | `PLATFORM-MODEL-REGISTRY` Ch59 | `TRAIN-LORA` Ch30; `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| Distribution-shift robustness of safety probes | `PLATFORM-SECURITY` Ch72 | `PLATFORM-EVALUATION-SYSTEM` Ch66; `PLATFORM-MONITORING` Ch67 |
| Verified synthetic data and provenance | `TRAIN-DATA` Ch27 | `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| Device API maturity and driver/control-plane ownership | `PLATFORM-GPU-SCHEDULER` Ch63 | Adjacent Ch62/64 platform contracts |

The Weekly records owner candidates only. Historical Books Gate remains closed, so these mappings are routing decisions rather than claims of completed integration.

## Recommended Action

1. Preserve all 24 Full Source Reviews as Books candidates, but do not write them into Books until the historical family-level gate opens.
2. Keep the seven recovered W35 spillbacks resolved there; reopen W35 for the four newly exposed Aug 29～30 owners. Do not duplicate any of the eleven in W36.
3. Carry Robix in the blocked-material ledger and recompute its score only after full text is recovered.
4. When Books work resumes, integrate by mechanism owner: stateful Agent rollout; reward/credit assignment; typed evaluation and robustness; proposal/synthesis/commit; arbitrary-interval generation; embodied observation correction; model-registry evidence; data provenance; device-resource contracts. Do not append paper-by-paper summaries.
5. Keep policy announcements and prereleases Weekly-only unless later primary technical material discloses a durable mechanism.

## Event-Date Daily Decision

Historical Backfill does not create synthetic Daily records. All 65 canonical events and their actual dates are recorded directly in this Weekly. The eleven Aug 29～31 spillbacks belong to W35: seven are already recovered there and four remain a W35 repair item. No Daily is backfilled for them.

## Books Integration Decision

`Historical Books Gate: Closed.`

- `Books Pending`: the 24 `20+` reviews have sufficient W36 evidence packets but have not been integrated by this task.
- Below-threshold `Weekly Only`, `Emerging / Experimental`, rejection, policy fact, and blocked items do not modify Books.
- This Weekly reconstruction changes no Books file and makes no claim that archive completion or Books integration is complete.

## Independent Review and Weekly Gate

### Discovery Gate

- **Coverage replay:** Pass — institution, academic, and engineering lanes were replayed in fixed order through the full Sep 1～7 window, with Sep 8～9 feeds used only to recover earlier-v1 spillbacks.
- **Canonical denominator:** Pass — 65 W36 rows, 60 arXiv/research owners plus 5 official engineering/policy events.
- **Date/revision ownership:** Pass — all rows use v1/official first-public date; eleven W35 spillbacks and nine W37-discovered W36 revisions are explicitly routed.
- **Deduplication:** Pass — primary identifier and Source Family uniqueness checked; zero duplicate W36 rows.

### Evidence Gate

- **20+ Full Source Review:** Pass — 24/24.
- **Below-20 closure:** Pass — 41/41 have source, date, arithmetic, and non-template disposition/rejection evidence.
- **Ordinary Review Pending:** Pass — 0.
- **Blocked-skip:** Pass with disclosure — Robix is the sole blocked family and has an exact P1 material request; it is not described as full-read.
- **Fact boundary:** Pass — author benchmarks remain bounded; product/policy behavior is not used to infer undisclosed model or runtime mechanisms.

### Weekly Gate Result

`2025-W36 Weekly Evidence Gate: Pass with one explicit blocked-skip item.`

This result closes the ordinary W36 replay checkpoint. It does not close the annual Archive Completion Gate, the four newly exposed W35 spillback repairs, the Robix recovery item, or the Historical Books Gate.

## Ignored Noise

- Financing, hiring, education, regional availability, and product commentary without a public mechanism contract.
- Later arXiv revisions treated as new weekly events.
- Hugging Face popularity/ranking as evidence of technical importance.
- Benchmark headlines lacking matched model, data, evaluator, decoding, hardware, or serving conditions.
- Framework patch notes or prereleases that do not expose a durable design change.

## Repository Changes

- Rebuilt `papers/2025/weekly/2025-W36/README.md` from a one-event legacy archive into a 65-row canonical evidence ledger.
- Added 24 non-template Full Source Reviews, 41 below-threshold closures, one exact blocked-material request, cross-week routing, Stable Node ownership, and independent Gate results.
- No Daily, annual index, Books, ROADMAP, Learning State, or other Weekly file was modified by this W36 task.

## Open Questions

1. Can the event-time Robix v1 full text and artifact revision be recovered so its provisional 19/30 evidence status can be finalized?
2. How should asynchronous agent training bound off-policy drift when partial rollout pools contain multiple policy versions?
3. Can planning-span credit assignment be validated by causal intervention rather than mined linguistic proxies and judge-labeled errors?
4. Under what candidate diversity, correlation, and SLO does generative fusion beat reranking or a stronger single-pass model after fleet cost is included?
5. How should abstention/retrieval policies aggregate correlated atomic-claim evidence without multiplying nominal independent confidences?
6. Which conformance tests can detect Kubernetes DRA driver/API/feature-gate skew before production rollout?

## Sources

Accessed 2026-08-24. Primary identity links below are the canonical source-family anchors; later revisions do not change weekly ownership.

### Model, institution, and high-score research sources

- UI-TARS-2: https://arxiv.org/abs/2509.02544
- SimpleTIR: https://arxiv.org/abs/2509.02479
- VerlTool: https://arxiv.org/abs/2509.01055
- Baichuan-M2: https://arxiv.org/abs/2509.02208
- OpenVision 2: https://arxiv.org/abs/2509.01644
- DynaGuard: https://arxiv.org/abs/2509.02563
- LMEnt: https://arxiv.org/abs/2509.03405
- Planning with Reasoning using Vision Language World Model: https://arxiv.org/abs/2509.02722
- Beyond Correctness: https://arxiv.org/abs/2509.03403
- Towards a Unified View of LLM Post-Training: https://arxiv.org/abs/2509.04419
- DeepResearch Arena: https://arxiv.org/abs/2509.01396
- Why Language Models Hallucinate: https://arxiv.org/abs/2509.04664
- Set Block Decoding: https://arxiv.org/abs/2509.04185
- Benchmark Robustness and Reliability: https://arxiv.org/abs/2509.04013
- Loong: https://arxiv.org/abs/2509.03059
- Emergent Hierarchical Reasoning / HICRA: https://arxiv.org/abs/2509.03646
- Hunyuan-MT: https://arxiv.org/abs/2509.05209
- Flaw or Artifact?: https://arxiv.org/abs/2509.01790
- Manipulation as in Simulation: https://arxiv.org/abs/2509.02530
- Inverse IFEval: https://arxiv.org/abs/2509.04292
- Transition Models: https://arxiv.org/abs/2509.04394
- Delta Activations: https://arxiv.org/abs/2509.04442
- False Sense of Security: https://arxiv.org/abs/2509.03888
- Kubernetes DRA v1.34 update: https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/
- Kubernetes DRA documentation: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/

### Below-threshold research sources

- https://arxiv.org/abs/2509.02547
- https://arxiv.org/abs/2509.01363
- https://arxiv.org/abs/2509.01215
- https://arxiv.org/abs/2509.00605
- https://arxiv.org/abs/2509.01563
- https://arxiv.org/abs/2509.02522
- https://arxiv.org/abs/2509.02460
- https://arxiv.org/abs/2509.02534
- https://arxiv.org/abs/2509.01440
- https://arxiv.org/abs/2509.02523
- https://arxiv.org/abs/2509.02333
- https://arxiv.org/abs/2509.01052
- https://arxiv.org/abs/2509.02046
- https://arxiv.org/abs/2509.01360
- https://arxiv.org/abs/2509.01584
- Robix identity/abstract: https://arxiv.org/abs/2509.01106
- https://arxiv.org/abs/2509.03680
- https://arxiv.org/abs/2509.04744
- https://arxiv.org/abs/2509.05263
- https://arxiv.org/abs/2509.05296
- https://arxiv.org/abs/2509.04575
- https://arxiv.org/abs/2509.02437
- https://arxiv.org/abs/2509.04504
- https://arxiv.org/abs/2509.03800
- https://arxiv.org/abs/2509.05208
- https://arxiv.org/abs/2509.02040
- https://arxiv.org/abs/2509.01984
- https://arxiv.org/abs/2509.02133
- https://arxiv.org/abs/2509.01610
- https://arxiv.org/abs/2509.02379
- https://arxiv.org/abs/2509.01250
- https://arxiv.org/abs/2509.01977
- https://arxiv.org/abs/2509.03867
- https://arxiv.org/abs/2509.04338
- https://arxiv.org/abs/2509.04011
- https://arxiv.org/abs/2509.04406
- https://arxiv.org/abs/2509.04434

### Engineering and policy sources

- Ray 2.49.1: https://pypi.org/project/ray/2.49.1/
- TensorRT-LLM 1.1.0rc3: https://pypi.org/project/tensorrt-llm/1.1.0rc3/
- OpenAI sensitive-conversation routing plan: https://openai.com/index/building-more-helpful-chatgpt-experiences-for-everyone/
- Anthropic regional sales restrictions: https://www.anthropic.com/news/updating-restrictions-of-sales-to-unsupported-regions

### Routed W35 source identities

- https://arxiv.org/abs/2509.00676
- https://arxiv.org/abs/2509.00404
- https://arxiv.org/abs/2509.00375
- https://arxiv.org/abs/2509.00425
- https://arxiv.org/abs/2509.00581
- https://arxiv.org/abs/2509.00930
- https://arxiv.org/abs/2508.21496
- https://arxiv.org/abs/2509.00244
- https://arxiv.org/abs/2509.00428
- https://arxiv.org/abs/2509.00531
- https://arxiv.org/abs/2509.00578
