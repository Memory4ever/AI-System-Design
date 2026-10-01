# 2026-09-19 Screening Ledger

## Window

- Asia/Shanghai: `[2026-09-18T09:00:00+08:00, 2026-09-19T09:00:00+08:00)`
- arXiv official list: `Showing new listings for Friday, 18 September 2026`; it became visible at the regular Asia/Shanghai `2026-09-19T08:00:00+08:00` boundary.
- Categories: `cs.CL`, `cs.LG`, `cs.DC`, `cs.AI`, `cs.CV`, `cs.RO`, `cs.AR`, `cs.PL`, `cs.OS`, `cs.PF`, `cs.IR`, `cs.MA`.

## Coverage and denominator

The twelve official category pages contained 917 unique identities across new, cross-list and replacement sections. The current-window new/cross set contained 633 unique identities after cross-category de-duplication. One old cross-list identity (`2609.18122`) was reconciled to its earlier owner window instead of being counted again.

All 633 current-window titles were inspected. Ambiguous or potentially in-scope titles received full abstract reading. The first targeted repair restored 29 families. A second independent review then locked a narrower marker-title subset; after correcting its arithmetic, 87 identities required author re-review (the 88-row marker set minus confirmed `2609.19705`; separately checked `2609.19792` was not in that set). All 87 abstracts were read in full, 29 families were restored and reviewed against exact-current primary material, and 58 were closed with family-specific reasons. A fresh false-negative audit then identified 15 additional generic-close mistakes; only those 15 were reopened, all were retained after exact-v1 review. A bounded 12-item stratified sample from the same reason clusters found no further miss. The final arXiv candidate denominator is 142 unique Source Families. The retain rate is `142 / 633 = 22.4%`; this is a consequence of semantic contribution screening, not a quota. Every identity and its final decision is recorded below and in [denominator closure](denominator-closure.md).

The remaining 491 identities were closed before the denominator for one of four concrete reasons:

1. the work applies established AI methods to medicine, biology, materials, remote sensing, business, education or another domain without changing a foundation-model/system mechanism, and AI for Science is currently out of scope;
2. it studies generic vision, robotics, control, recommendation, networking or machine learning without a direct foundation-model/AI-system design delta;
3. it reports a local architecture, prompting, dataset or benchmark improvement but does not change a durable mechanism, operating boundary or evaluation contract;
4. it is a survey, position paper or comparison whose primary evidence does not resolve a current project design question.

The 142 retained arXiv families are:

```text
2609.19149 2609.19164 2609.19169 2609.19183 2609.19207 2609.19242
2609.19291 2609.19315 2609.19325 2609.19363 2609.19425 2609.19499
2609.19504 2609.19587 2609.19596 2609.19606 2609.19636 2609.19657
2609.19669 2609.19674 2609.19743 2609.19758 2609.19759 2609.19799
2609.19868 2609.19877 2609.19880 2609.19892 2609.19934 2609.19942
2609.19947 2609.19969 2609.19991 2609.20004 2609.20045 2609.20050
2609.20129 2609.20152 2609.20166 2609.20211 2609.20261 2609.20269
2609.20301 2609.20412 2609.20457 2609.20474 2609.20497 2609.20511
2609.20538 2609.20539 2609.20541 2609.20581 2609.20612 2609.20614
2609.20625 2609.20648 2609.20715 2609.20723 2609.20734 2609.20744
2609.20751 2609.20758 2609.20776 2609.20784 2609.20804 2609.20807
2609.20812 2609.20819 2609.20820
2609.19334 2609.19366 2609.19465 2609.19472 2609.19475 2609.19482
2609.19515 2609.19607 2609.19640 2609.19659 2609.19671 2609.19683
2609.19702 2609.19717 2609.19754 2609.19796 2609.19827 2609.19830
2609.19878 2609.19883 2609.19897 2609.19909 2609.20082 2609.20089
2609.20186 2609.20519 2609.20530 2609.20754 2609.20822
2609.19213 2609.19244 2609.19376 2609.19391 2609.19456 2609.19545
2609.19551 2609.19600 2609.19610 2609.19616 2609.19630 2609.19664
2609.19680 2609.19722 2609.19801 2609.19843 2609.19866 2609.19923
2609.20034 2609.20051 2609.20252 2609.20278 2609.20449 2609.20563
2609.20584 2609.20620 2609.20633 2609.20659 2609.20722
2609.19199 2609.19441 2609.19502 2609.19512 2609.19579 2609.19844
2609.20016 2609.20277 2609.20543 2609.20582 2609.20709 2609.20779
2609.20791 2609.20800 2609.20821
```

## Second bounded marker-subset adjudication

The following table is the final author-side decision for all 87 reopened identities. “Retain” means the abstract established a project-level mechanism and exact-current evidence review was completed; “Close” gives the specific reason it remains outside the denominator.

| ID | Decision | Family-specific reason |
| --- | --- | --- |
| `2609.19148` | Close | Hesitancy/ambivalence recognition classifier; no foundation-model state, runtime or evaluation-contract delta. |
| `2609.19150` | Close | Discovers prompt-conditional style axes in activations, but only as a local probing method without a system owner or release decision change. |
| `2609.19152` | Close | Misinformation detector application; model strategy-agnostic classification does not change AI-system mechanisms. |
| `2609.19155` | Close | Dialogue-conflict detection task and benchmark; it does not add durable context, memory or authority semantics. |
| `2609.19182` | Close | Benchmark-design mapping study; secondary taxonomy without new primary mechanism evidence. |
| `2609.19213` | Retain | Layer-wise curriculum changes compression recovery dynamics and training control. |
| `2609.19244` | Retain | Separates search decision, query, result consumption and grounding in conversational agents. |
| `2609.19357` | Close | Random-dot-product graph submanifold theory; not a foundation-model or AI-infrastructure mechanism. |
| `2609.19376` | Retain | Independent functional/scientific critics and verify-repair alter agent workflow evidence ownership. |
| `2609.19391` | Retain | Human-audited spec, typed IR, Dafny verifier and deterministic compiler create a formal commit path. |
| `2609.19417` | Close | Multisignal late-fusion RAG recipe; local retrieval-quality improvement without new state/provenance contract. |
| `2609.19456` | Retain | Traversal-safe deletion and alive-before-ranking change retrieval privacy/deletion semantics. |
| `2609.19513` | Close | Synthetic STEM corpus release; data asset quality does not introduce a new data-system control mechanism. |
| `2609.19529` | Close | Next-token functional-estimation theory; no disclosed training/runtime design consequence. |
| `2609.19530` | Close | Résumé-screening access/recurrence benchmark; domain application without a general multi-agent mechanism. |
| `2609.19531` | Close | LLM-tuned instruction duplication for conventional parallel software; the LLM is an offline tuning aid, not system state owner. |
| `2609.19539` | Close | Compressed active-subspace method for Bayesian inference; outside foundation-model systems. |
| `2609.19545` | Retain | LLM formulation is separated from deterministic typed compilation and executable emission. |
| `2609.19551` | Retain | Persistent enterprise rules are discovered, revised and retired as dynamic world state. |
| `2609.19569` | Close | Genetic-disease severity classification application; no general agent/evaluation contract delta. |
| `2609.19585` | Close | EHR journey construction pipeline; domain workflow packaging without new system ownership. |
| `2609.19600` | Retain | Contact-centric latent dynamics changes what a robot world model predicts and pays for. |
| `2609.19601` | Close | Visual-analytics UI for literature RAG; human interface contribution without new retrieval mechanism. |
| `2609.19610` | Retain | Long-horizon direct/counterfactual/noisy/inverse probes expose memory/adaptation failure. |
| `2609.19615` | Close | Telemetry semantic-layer induction application; hierarchical LLM/RAG composition does not add a durable mechanism. |
| `2609.19616` | Retain | Prompt-side complexity is evaluated as a reliability sensor with explicit confounds. |
| `2609.19622` | Close | Zero-token geometric graph is a local multi-hop RAG representation improvement; provenance and control contracts are unchanged. |
| `2609.19630` | Retain | Separates language safety from execution authorization for vehicle commands. |
| `2609.19664` | Retain | Tool solving/evolving and executable validation define a bounded self-improvement lifecycle. |
| `2609.19666` | Close | Dexterous-manipulation VLA post-training combines established recipe components; no new controller, safety or state contract. |
| `2609.19680` | Retain | Failure-driven skill admission, regression, replacement and retirement alter platform lifecycle control. |
| `2609.19716` | Close | Point-cloud prompt module for 3D vision; local representation improvement. |
| `2609.19722` | Retain | Read-only binary cover stories expose a new untrusted-artifact attack surface for LLM analyzers. |
| `2609.19747` | Close | Diffusion light-field reconstruction adaptation; imaging-task method without a generative-system contract delta. |
| `2609.19789` | Close | Adversarial-signal contagion in trading agents is domain simulation without a general authority or communication mechanism. |
| `2609.19801` | Retain | Persistent resources, simulator-event rewards and adaptive curriculum change embodied-agent evaluation state. |
| `2609.19805` | Close | Grapheme-to-phoneme data method for unsegmented languages; language-resource application. |
| `2609.19843` | Retain | Controlled GUI experiments show reasoning and social-nudge susceptibility are non-monotonic. |
| `2609.19866` | Retain | Directly distinguishes measurement reproducibility from construct validity. |
| `2609.19887` | Close | Lexical-abstraction mechanistic study; it does not change a current model/system design decision. |
| `2609.19913` | Close | Social-network opinion-dynamics digital twin; simulation application without a general world-model contract. |
| `2609.19916` | Close | Korean-neologism evaluation dataset; coverage expansion only. |
| `2609.19923` | Retain | ADMM consensus unifies full-model and adapter federated VLA updates. |
| `2609.19924` | Close | Pedagogical token-to-wire lifecycle overview; no new primary mechanism or measured delta. |
| `2609.19944` | Close | Multi-agent causal-graph candidate generation method; local task pipeline without new agent authority. |
| `2609.19964` | Close | Detection-transformer knowledge-distillation refinement; conventional vision-model improvement. |
| `2609.19989` | Close | China AIGC compliance benchmark; regulatory coverage artifact without a new evaluation mechanism. |
| `2609.19990` | Close | Query-conditioned visual-token pruning; local efficiency method without new runtime ownership or SLO contract. |
| `2609.20009` | Close | Multiview detection on distributed edge devices; conventional perception workload study. |
| `2609.20034` | Retain | Action-conditioned block-causal world generation and cross-block KV define persistent realtime state. |
| `2609.20051` | Retain | Distillation-aware coordinate transport changes adapter compatibility across denoising schedules. |
| `2609.20068` | Close | Information-economic framing for sovereign geo-mining inference; application analysis without validated new mechanism. |
| `2609.20081` | Close | Speech-LLM emotion-recognition adaptation; downstream classification task. |
| `2609.20086` | Close | Sparse-encoder transformer for time-series forecasting; domain architecture improvement. |
| `2609.20100` | Close | ViT-in-ViT token-selection/pruning module; local vision efficiency improvement, not a medical/biological application. |
| `2609.20143` | Close | Metacognitive anti-deskilling feedback study; HCI outcome without a durable AI-system mechanism. |
| `2609.20147` | Close | MRI-to-PET diffusion translation; medical imaging application. |
| `2609.20194` | Close | Adaptive fuzzy-inference membership function; outside foundation-model systems. |
| `2609.20214` | Close | Transformer-fault diagnosis with a quantum classifier; industrial diagnostic application. |
| `2609.20218` | Close | Classical-vs-LLM tabular crossover benchmark; comparison result without a new system contract. |
| `2609.20227` | Close | Resource-constrained navigation transformer; local planner for a specific environment. |
| `2609.20250` | Close | Sub-3B essay-scoring benchmark on consumer GPU; workload result without a mechanism delta. |
| `2609.20252` | Retain | Task-directed readout changes the usable semantics of frozen multimodal representations. |
| `2609.20267` | Close | Text-to-video concept-erasure algorithm; local method does not add deletion certification or lifecycle semantics. |
| `2609.20278` | Retain | Role/slot/instance operators preserve structured identity across text and graphs. |
| `2609.20297` | Close | Surface-EMG gesture transfer and calibration; biomedical application. |
| `2609.20318` | Close | LLM-guided driving-scenario augmentation; domain data generation without a new safety/evaluation contract. |
| `2609.20330` | Close | Personalized object-search system for accessibility; application integration. |
| `2609.20347` | Close | LLM agent for satellite QoS routing; networking application without a general agent-runtime delta. |
| `2609.20358` | Close | Geological microstructure generation; AI-for-domain application. |
| `2609.20388` | Close | Monocular navigation stack; local robotics method without a new embodiment/control boundary. |
| `2609.20404` | Close | Learned principal-agent contracts for carbon farming; economics application, not AI-agent architecture. |
| `2609.20449` | Retain | Controlled coding experiment separates task information, planning, execution and capacity. |
| `2609.20465` | Close | Neural Bayes estimator for emitter localization; signal-processing application. |
| `2609.20535` | Close | Predictive-maintenance time-series foundation model; domain forecasting architecture. |
| `2609.20563` | Retain | Embedding post-training jointly constrains retrieval representation and reasoning quality. |
| `2609.20584` | Retain | Industrial hazard benchmark decomposes regulated reasoning stages and shows CoT non-monotonicity. |
| `2609.20586` | Close | Cooperative Gaussian-splat scene understanding; local 3D perception method. |
| `2609.20604` | Close | Semantic SLAM for precision agriculture; domain robotics application. |
| `2609.20620` | Retain | Deterministic controller and LLM anomaly diagnosis have separate outcome contracts. |
| `2609.20624` | Close | Olfactory scene-graph quadruped navigation; specialized control method. |
| `2609.20633` | Retain | Iterative refinement can revise prior image state, unlike committed AR tokens. |
| `2609.20659` | Retain | Policy-guided human data collection and OOD-triggered VLA post-training define a deployment loop. |
| `2609.20669` | Close | Foresight training for 3D diffusion policies; local policy objective without a new controller/state contract. |
| `2609.20670` | Close | Multipath transmitter pose inference; wireless localization application. |
| `2609.20722` | Retain | Automatic representation steering increases prompt-injection surface as intervention grows. |
| `2609.20768` | Close | Shared action graph for sports-highlight interpretation; domain representation application. |

## Third bounded generic-close repair

The fresh reviewer identified 15 cases whose generic closure contradicted the title and complete abstract. The author reopened only these identities, read exact-v1 Method/Evaluation/Limitations, and retained all 15:

| ID | Decision | Family-specific reason |
| --- | --- | --- |
| `2609.19199` | Retain | Executable regulation-to-code and counterfactual self-checking change compliance proposal/decision ownership. |
| `2609.19441` | Retain | Offline action-deviation calibration adds accept/reject/defer semantics before quantized WAM deployment. |
| `2609.19502` | Retain | Canonical identity, evidence-backed ratings and adversarial aggregation define shared reputation state. |
| `2609.19512` | Retain | Provenance/conflict-aware belief gating owns proceed, re-observe, abstain and escalate decisions. |
| `2609.19579` | Retain | Cached offline hidden-state matching changes how aggressively pruned VLA artifacts are recovered and released. |
| `2609.19844` | Retain | Schema/provider acceptance is falsified as a sufficient validity test for an AI-generated measurement instrument. |
| `2609.20016` | Retain | Governance requirements become machine-checkable evidence and release criteria. |
| `2609.20277` | Retain | Generated visual instructions and frozen JEPA goal tokens form a distinct WAM-conditioning branch. |
| `2609.20543` | Retain | Homogeneous model-group consensus can be stronger yet less correct than human-group outcomes. |
| `2609.20582` | Retain | Generated video is converted into typed phase/object/geometry state before trajectory optimization. |
| `2609.20709` | Retain | Explicit future motion replaces inference-time future-video generation and is selected by a progress verifier. |
| `2609.20779` | Retain | Surface-toxicity improvement can conceal transformed representational harm, invalidating a one-axis safety metric. |
| `2609.20791` | Retain | Stage-transition authority is distilled into a lightweight controller above the low-level policy. |
| `2609.20800` | Retain | Orthogonal predictive factors and a shared predictive core define a cross-world factorization branch. |
| `2609.20821` | Retain | String overlap dominates physical-quantity embedding similarity, exposing a measurement-validity boundary. |

### Bounded stratified false-negative sample

To test whether the same generic reasons concealed another systematic miss, twelve already-closed families were sampled across the four closure types and their complete abstracts were reread. All stayed closed:

| Cluster | Sampled families | Result |
| --- | --- | --- |
| Domain application | `2609.19230` ultrasound segmentation, `2609.19385` mammography MACE prediction, `2609.20592` crystal refinement, `2609.20684` women's-health communication | All are domain-specific models/evaluations; none changes a general foundation-model or AI-system contract. |
| Local model/task method | `2609.19209` query suggestion, `2609.19483` person retrieval, `2609.19990` visual-token pruning, `2609.20267` video concept erasure | Each improves a bounded task/pipeline; no new state owner, control boundary or general release contract is established. |
| Evidence/position or generic ML | `2609.19151` app-review analysis, `2609.19180` biophysics benchmark, `2609.19414` offline goal-conditioned RL, `2609.20658` authorship/ownership survey | The abstracts provide domain evidence, benchmark coverage, generic RL or HCI findings rather than a durable project-level mechanism. |

This sample closes the known generic-reason cluster but does not turn sampling into proof that every excluded abstract is error-free. A new fresh reviewer must still challenge the repaired denominator before the report can become Complete.

## Replacement handling

- `2608.21363v2` (AIREP) is an important revision: the paper now separates Decision, Control, Execution and Effect evidence; defines deterministic wire integrity and bounded assurance semantics; and makes absence/indeterminacy explicit. It is reviewed as a revision event without another score.
- `2608.22808v4` (CatchBench) materially revises analyses and presentation around where an agent failure can be intercepted. It is reviewed as a revision event without another score.
- `2604.25323` and `2606.01670` carry explicit withdrawal notices and are excluded from the positive chain.
- `2606.05017` carries a correction/erratum that withdraws an earlier fabricated-die claim; no positive Books dependency was found, so the correction is retained only as a negative provenance event.
- `2609.14092` is a duplicate whose canonical family is `2511.05215`; it is not re-counted.

## Official engineering events

- ByteDance Seed VeOmni commit [`77cf73e`](https://github.com/ByteDance-Seed/VeOmni/commit/77cf73e69756eaff19c3f32df6f7415b0240e791), `2026-09-18T10:55:32+08:00`: extracts model-bound behavior into `VeOmniModelRuntime`; retained as a runtime ownership-boundary event.
- Tencent Hunyuan UniRL commit [`8fc283e`](https://github.com/Tencent-Hunyuan/UniRL/commit/8fc283e0eaee9de9f5a7de085872f7a046760ce6), `2026-09-18T16:26:16+08:00`: adds SGLang checkpoint-engine IPC weight synchronization with begin/end update sessions and fail-closed transfer behavior; retained.
- Xiaomi MiMo Code commits [`2bda179`](https://github.com/XiaomiMiMo/MiMo-Code/commit/2bda17944b346ab85c8ee3cf0a0d4ab24819d37c) and [`50cd713`](https://github.com/XiaomiMiMo/MiMo-Code/commit/50cd713989f47225cfc717868b245e1de32b35b7), published at `2026-09-18T12:43:18+08:00` and `2026-09-19T04:21:03+08:00`: one Source Family covering session-wide cancellation, durable terminal notification and explicit subagent recovery; retained.
- Qwen Omnilingua-Bench initial commit [`719bcb3`](https://github.com/QwenLM/Omnilingua-Bench/commit/719bcb395a44351fabd209d9094b2b3d1dfc5a5d) was read and closed before the denominator: it expands multilingual/audio benchmark coverage but does not by itself expose a new system mechanism or invalidate an existing evaluation contract.

## Evidence access

Exact-v1 arXiv HTML was opened for 139 of the 142 retained arXiv families and read to the method/evaluation/limitations depth required by the score. `2609.19866v1`, `2609.20497v1` and `2609.20543v1` used exact-v1 PDFs because the required HTML path was unavailable or unsuitable; they were reviewed at the same depth. The exact locators for all 142 arXiv families, both revisions and three official artifacts are recorded in [evidence locators](evidence-locators.md). The repair also corrected wrong domain labels for `2609.19213`, `2609.20100` and the 15 third-round identities; `2609.19705` is a finance-domain Agent security survey and `2609.19792` is generic queueing/scheduling theory.

The screening and evidence result is author-side only until an independent reviewer checks admission false positives/false negatives, adopted claims and Books routing.
