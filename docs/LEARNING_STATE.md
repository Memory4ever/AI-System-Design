# Current Learning State

Last Updated: 2026-08

## Current Phase

Reset to the repository-backed roadmap.

The previous Part II / Tokenizer / Embedding learning progress came from
chat-only discussions and should not be treated as repository learning
state. That gap has now been replaced by the repository-backed Part II Draft
recorded below.

Current priority:

Parts I～VII are repository-backed Drafts. The knowledge tree now contains 84
chapters and uses Stable Knowledge Node IDs. Part III owns the continuous route
from multimodal representation through generative paradigms and World Models to
Embodied/VLA action; former Training, Inference, Infrastructure and Agent chapters
have moved to Parts IV～VII without changing their durable content.

Historical note: dated entries below that precede the 2026-08-13 architecture
migration use legacy chapter numbers. Legacy Ch23～37 map to current Ch27～41,
Ch38～52 to Ch42～56, Ch53～69 to Ch57～73, and Ch70～80 to Ch74～84. New or
updated research records must use Stable Node ID plus current/legacy chapter.

## 2026-08-13 Seven-Part Architecture and Source-Family Integration

Status: Structure migration complete; selected Source-Family Books Integration
complete; W01～W32 Archive Completion Gate remains Open

Stable understanding:

- The former six-Part/80-chapter layout could absorb most Model, Training,
  Inference, Platform and Agent research, but it could not coherently own the
  `representation -> generation -> environment transition -> physical action`
  chain. Part III now owns that chain in Ch23～26.
- All 84 chapters have unique Stable Knowledge Node IDs. Current chapter number is
  reading order; the ID is durable ownership. `ROADMAP.md` is the authoritative
  current/legacy mapping.
- ADR-007 separates per-Source-Family Books eligibility from archive-wide recall
  completion. Twenty-two reviewed families support the new Part; blocked, disputed
  and version-only evidence remains outside long-term mechanism prose.
- Ch10 is again a worldview/future scenario owner, not a World Model or VLA
  mechanism container. Compiler/kernel/hardware and AI for Science remain explicit
  cross-chapter routes rather than new Parts.
- Existing Training, Inference, Platform and Agent arguments were reviewed before
  adding text. Their async/staleness, KV identity and rollback, typed resource,
  evidence, privacy, derived memory and Multi-Agent failure mechanisms were already
  present; the migration updates owner identity and handoffs instead of duplicating
  paper summaries.
- W01 is the first post-migration Weekly to pass the explicit per-week Books Gate:
  11/11 retained Source Families have final dispositions; ten integrate/refine
  Ch22, Ch27, Ch28, Ch33, Ch48, Ch55, Ch66 and Ch77, while DiT-HC is a documented
  `No Change` against Ch36. The weekly reverse review corrected OrchestrRL's owner
  to `TRAIN-GRPO`; W01 archive recall remains open and is not represented as complete.
- W02 has independently passed the same Books Gate for 5/5 retained families.
  Routing by Analogy refines `MODEL-MOE`, Crystal-KV refines `INFER-KV-CACHE`,
  MoEBlaze adds materialization-free indexed execution to `INFER-TENSORRT-LLM`,
  and AIConfigurator adds calibrated configuration search to `INFER-SCHEDULING`.
  The NVIDIA portfolio remains Weekly Only because it discloses no unified mechanism.
  The weekly reverse review corrected the provisional owners for MoEBlaze and
  AIConfigurator and kept all author benchmarks inside their disclosed contracts.
  W02 discovery recall remains open and is not represented as archive completion.
- W03 has independently passed its Books Gate for 7/7 scored candidates. KVzap
  refines learned KV eviction in `INFER-KV-CACHE`; the constrained MoE design study
  refines `MODEL-MOE`; TableCache adds dependency-aware reusable blocks to
  `INFER-SGLANG`; RAPID adds power/role closed-loop control to
  `INFER-PD-DISAGGREGATION`. Economic primitives are a concrete `No Change`, while
  MedGemma and NeuralGCM remain Weekly Only. The reverse review found that RAPID's
  recorded arXiv identifier pointed to an unrelated paper and corrected it from
  `2601.12727` to `2601.12241` before integration. W03 discovery recall remains open.
- W04 has independently passed its source-family Books Gate for 23/23 scored
  candidates after an item-by-item integration and reverse review. Sixteen candidates
  integrate or refine `TRAIN-SFT`, `TRAIN-GRPO`, `TRAIN-CHECKPOINT`,
  `TRAIN-DISTRIBUTED-TRAINING`, `TRAIN-MEGATRON`, `INFER-KV-CACHE`,
  `INFER-CONTINUOUS-BATCHING`, `INFER-SCHEDULING`, `PLATFORM-MONITORING`,
  `PLATFORM-SECURITY`, `AGENT-CONTEXT`, `AGENT-WORKFLOW` and
  `AGENT-MULTI-AGENT`; four are concrete No Change decisions, two remain Weekly
  Only and one cross-year CPU-only paper is rejected. Faramesh and Universal Load
  Balancing remain Emerging, and W04 discovery recall remains open.

Archive boundary:

- W01～W32 still has 41 requested material items, including identity, full text,
  revision and Scholar/OpenAlex recall export. `Review Pending = 0` for accessible
  material, but Archive Completion Gate remains Open.
- Tuna-2 and other `Disputed` evidence, GameWorld/blocked families and mechanism-not-
  disclosed version facts were not integrated.

## Completed Repository-Backed Work

### Chapter 1: Why Learn AI System

Status: Draft

Repository path:

`books/part-01-worldview/01-why-learn-ai-system.md`

Core understanding:

AI System is not model deployment. It is the system discipline of turning
model capability into stable, efficient, controllable, observable, and
iterable production value.

The chapter establishes the first mental model of the book:

Model capability must be understood together with data, training, inference,
serving, GPU scheduling, evaluation, observability, feedback, and governance.

### Chapter 2: AI 的发展历史

Status: Draft

Repository path:

`books/part-01-worldview/02-ai-history.md`

Core understanding:

AI 的发展史不是线性技术年表，而是瓶颈不断迁移的历史。

The chapter organizes the route from rule systems to machine learning, deep
learning, Transformer, LLM, post-training, and Agent around one system idea:
each paradigm solves an older bottleneck while pushing a new bottleneck into
the AI System boundary.

The current Draft establishes:

- rule systems expose the knowledge-coverage and maintenance bottleneck;
- machine learning shifts capability from handwritten rules to data-driven
  generalization;
- deep learning shifts the bottleneck from feature engineering to data,
  compute, optimization, and GPU infrastructure;
- Transformer aligns sequence modeling with parallel hardware but creates
  attention, memory, and long-context bottlenecks;
- LLMs move part of task definition into runtime prompt and context, making
  inference, evaluation, post-training, and governance central system
  concerns;
- Agents expand the system boundary from token generation to tool use,
  memory, state, permissions, trace, and workflow governance.

### Part I Worldview: Chapters 3-10

Status: Draft completed

Repository paths:

`books/part-01-worldview/03-global-knowledge-tree.md`

`books/part-01-worldview/04-why-models-learn.md`

`books/part-01-worldview/05-what-neural-networks-learn.md`

`books/part-01-worldview/06-why-transformer-changed-the-world.md`

`books/part-01-worldview/07-scaling-law.md`

`books/part-01-worldview/08-why-llms-show-intelligence.md`

`books/part-01-worldview/09-ai-system-evolution.md`

`books/part-01-worldview/10-future-of-ai.md`

Core understanding:

- Chapter 3 organizes AI System around capability production, capability
  delivery, control and governance, and the Agent runtime loop. The knowledge
  tree is a map of stable responsibilities, not a product architecture.
- Chapters 4-5 separate representation capacity, optimization, and
  generalization. Parameter updates minimize empirical risk; the resulting
  distributed representations remain dependent on data, objective, inductive
  bias, and deployment distribution.
- Chapters 6-8 form one capability chain: Transformer provides
  content-dependent routing and scalable training structure; Scaling Laws
  describe empirical loss regularities; broad LLM capabilities arise through
  data, scale, context, and post-training but do not imply reliability or
  consciousness.
- Chapter 9 separates system-form evolution from the capability-paradigm
  history in Chapter 2. It traces the route from local experiments through
  reproducible pipelines, distributed training, online Serving, LLM runtime,
  platform governance, and Agent runtime.
- Chapter 10 treats the future as constraint-driven scenario analysis across
  Agent, personalization, world models, edge intelligence, and AI
  platformization. It does not make vendor or timeline predictions.

Part I cross-chapter boundaries were checked in this pass:

- Chapter 2 owns capability-paradigm history; Chapter 9 owns system-form
  evolution.
- Chapter 4 owns the optimization mechanism; Chapter 5 owns representation and
  generalization boundaries.
- Chapter 6 owns the high-level Transformer design argument; Chapter 14 owns
  Q/K/V and Self Attention mathematics.
- Chapter 7 owns empirical scaling regularities; Chapter 8 owns capability,
  emergence, and reliability distinctions.

All ten Part I chapters remain `Draft`. They have distinct theses, natural
section structures, self-check questions, `Review notes`, and primary-source
entry points. Promotion to `Review` or `Final` is intentionally deferred.

### Part II Model: Chapters 11-22

Status: Draft completed

Repository paths:

`books/part-02-model/11-tokenizer.md`

`books/part-02-model/12-embedding.md`

`books/part-02-model/13-position-encoding.md`

`books/part-02-model/14-self-attention.md`

`books/part-02-model/15-multi-head-attention.md`

`books/part-02-model/16-feed-forward-mlp.md`

`books/part-02-model/17-transformer-layer.md`

`books/part-02-model/18-decoder-only.md`

`books/part-02-model/19-kv-cache.md`

`books/part-02-model/20-sampling.md`

`books/part-02-model/21-moe.md`

`books/part-02-model/22-long-context.md`

Core understanding:

- Tokenizer defines the discrete text interface and trades vocabulary size
  against sequence length, multilingual coverage, and downstream system cost.
- In long-running Agent sessions, Tokenizer can also become version-bound
  runtime state. Safe incremental reuse requires reference-equivalent token
  ids, a tokenizer-specific stable boundary, explicit fallback, and a lifetime
  contract separate from KV Cache; stateless full tokenization remains the
  valid branch when these conditions do not hold.
- Embedding and Position Encoding transform `[B,T]` token ids into positioned
  `[B,T,d_model]` states without treating ids or positions as semantic scalar
  values.
- Self Attention provides content-dependent routing; Multi-Head Attention
  extends it across learned subspaces and separates Query heads from KV heads
  through MHA, GQA, and MQA.
- MLP provides high-capacity position-wise nonlinear transformation. Residual
  and Normalization combine MHA and MLP into shape-stable Transformer Layers.
- Decoder-only architecture uses causal language modeling to produce
  `[B,T,V]` logits. KV Cache reuses invariant historical K/V during
  autoregressive Decode, and Sampling turns each conditional distribution into
  an actual token trajectory.
- MoE conditionally activates expert MLPs, separating total capacity from
  active parameters while introducing routing, capacity, load balance, and
  All-to-All communication.
- Long Context is a joint constraint across position generalization, Attention
  compute, KV Cache capacity, effective information use, and production SLOs.

The Part II Draft uses one consistent notation:

```text
B       batch size
T       sequence length
V       vocabulary size
d_model hidden dimension
H       query head count
H_kv    key/value head count
d_h     head dimension
L       layer count
```

The end-to-end model path is now repository-backed:

```text
Text
-> Tokenizer
-> Embedding + Position
-> Self Attention + MLP
-> Transformer Layer
-> Decoder Only
-> KV Cache
-> Logits / Sampling
-> MoE / Long Context extensions
```

Part II cross-chapter boundaries were checked in this pass:

- Chapter 11 ends at token ids; Chapter 12 owns continuous lookup.
- Chapter 13 owns position mechanisms; Chapter 22 owns length extension and
  long-context system constraints.
- Chapter 14 owns single-head Attention; Chapter 15 owns multi-head structure
  and GQA/MQA.
- Chapter 16 owns Dense MLP; Chapter 21 owns conditional expert routing.
- Chapter 18 owns causal model architecture; Chapter 20 owns token selection.
- Chapter 19 owns the model origin, shape, and capacity of KV Cache; Chapter 45
  owns runtime memory management, reuse, offload, and scheduling.

All Part I and Part II chapters remain `Draft`. No chapter is promoted to
`Review` or `Final` in this pass.

### Part II Cross-Chapter Review Pass 2

Status: Completed; chapter maturity remains Draft

Scope:

`books/part-02-model/11-tokenizer.md`

through:

`books/part-02-model/22-long-context.md`

Completed in this pass:

- Reviewed all twelve chapters both as independent arguments and as one model
  lifecycle, rather than treating chapter-level completeness as sufficient.
- Added the Part II dependency map at the entry chapter. Chapters 11-20 form
  the sequential generation trunk; Chapters 21-22 are capacity extensions,
  not additional operators after Sampling.
- Confirmed the continuous tensor path from `[B,T]` token ids through
  `[B,T,d_model]` hidden states, Attention/MLP, `[B,T,V]` logits, per-layer KV
  state, and next-token selection.
- Aligned causal probability factorization, tensor positions, shifted targets,
  and the autoregressive loop in Chapter 18. Chapter 19 now reads as the state
  branch of a Decode step, while Chapter 20 is the token-decision branch.
- Clarified that Chapter 21 returns to Chapter 16 and replaces the Dense MLP
  capacity organization without changing the Transformer Layer's external
  shape contract. Also distinguished token states from top-k expert
  assignments in the capacity derivation.
- Positioned Chapter 21 and Chapter 22 as two orthogonal scaling questions:
  parameter capacity through conditional computation, and sequence capacity
  through Position, Attention, KV Cache, effective utilization, and system
  constraints.
- Strengthened the Part I to Part II transition from system worldview to token
  mechanics. ADR-008 now routes Part II first into Part III's multimodal
  representation/generation contract, then into Part IV capability production.
- Rechecked chapter boundaries against later Parts: tokenizer data governance
  remains in current Chapter 27; training mechanisms remain in Part IV; KV Cache
  allocation, paging, and scheduling remain in Part V; RAG and Memory remain
  in Part VII.

Review conclusion:

Part II now has a coherent dependency structure rather than merely twelve
complete chapter files. Each chapter retains one central thesis, while chapter
transitions expose which tensor contract, unresolved problem, or scaling
constraint the next node receives. This pass does not promote the chapters to
`Review`; primary-source refresh and a later cross-Part verification are still
required before maturity changes.

### Part IV Training System: Chapters 27-41

Status: Draft completed; cross-chapter Review completed

Repository paths:

`books/part-04-training-system/27-data.md`

`books/part-04-training-system/28-pretraining.md`

`books/part-04-training-system/29-sft.md`

`books/part-04-training-system/30-lora.md`

`books/part-04-training-system/31-rlhf.md`

`books/part-04-training-system/32-ppo.md`

`books/part-04-training-system/33-grpo.md`

`books/part-04-training-system/34-dpo.md`

`books/part-04-training-system/35-checkpoint.md`

`books/part-04-training-system/36-distributed-training.md`

`books/part-04-training-system/37-tensor-parallel.md`

`books/part-04-training-system/38-pipeline-parallel.md`

`books/part-04-training-system/39-zero.md`

`books/part-04-training-system/40-megatron.md`

`books/part-04-training-system/41-deepspeed.md`

Core understanding:

- Training data is the executable specification of the empirical distribution.
  Filtering, deduplication, decontamination, mixture weights, packing,
  provenance, and data cursors all change which gradients reach the model.
- Pretraining repeatedly minimizes causal next-token negative log-likelihood.
  Token loss, perplexity, optimizer state, global batch, precision, activation
  memory, and scaling constraints are separated from claims about factual or
  behavioral reliability.
- SFT uses demonstrations and token-level loss masks to make target interaction
  patterns more probable. LoRA changes the parameterization and model-state
  cost of an update, not the supervision objective itself.
- RLHF is a feedback pipeline: preference pairs train a reward proxy, then a
  policy is optimized under a reference constraint. PPO uses a learned value
  baseline and clipped on-policy updates; GRPO uses same-prompt group-relative
  rewards without a learned critic; DPO directly optimizes offline preference
  pairs through policy/reference log-ratios.
- Verifiable reward still includes a measurement system. When execution time
  or another noisy continuous signal enters GRPO, sandbox identity,
  calibration, reward density, drift, and all-equal groups become part of the
  training specification rather than evaluation-only details.
- A training checkpoint is a consistent transaction over model, optimizer,
  scheduler, RNG, data cursor, parallel layout, and identity metadata. A
  weights-only artifact, resumable checkpoint, and deployment artifact have
  different contracts.
- Distributed training is a constraint-mapping problem. DP splits samples, TP
  splits operators, PP splits layer depth, CP splits context work, EP splits
  experts, and ZeRO/FSDP shards data-parallel model states. Every mechanism
  introduces a specific communication and lifecycle cost.
- Megatron organizes Transformer computation across multi-dimensional process
  groups and schedules. DeepSpeed organizes ZeRO, offload, precision,
  optimizer, and checkpoint behavior as training-runtime policy. Framework
  names do not replace the underlying mechanism boundaries.

The Part IV capability-production path is now repository-backed:

```text
Data distribution
-> Pretraining
-> SFT / LoRA
-> Preference data and reward
-> PPO / GRPO / DPO
-> Consistent Checkpoint
-> Distributed Training
-> TP / PP / ZeRO
-> Megatron / DeepSpeed
-> Validated model artifact
```

Important shared equations and state contracts were checked across chapters:

```text
B_global = micro_batch * accumulation * data_parallel_degree

training state
= parameters + gradients + optimizer state
 + scheduler + RNG + data cursor + parallel metadata
```

Part IV cross-chapter boundaries:

- Chapter 27 owns data distribution and lineage; Chapter 28 owns the
  next-token objective and base training loop.
- Chapter 29 owns demonstration supervision; Chapter 30 owns low-rank update
  parameterization and adapter assets.
- Chapter 31 owns the RLHF feedback and Reward Model pipeline; Chapters 32-34
  separately own PPO, GRPO, and DPO optimization mechanics.
- Chapter 35 owns consistent persistence, resume, resharding, and artifact
  conversion; Chapter 39 owns data-parallel model-state sharding.
- Chapter 36 owns the distributed-training decision framework and Data
  Parallel baseline; Chapters 37-39 own TP, PP, and ZeRO mechanisms.
- Chapter 40 owns multi-dimensional Transformer parallelism composition;
  Chapter 41 owns DeepSpeed training-state lifecycle policy and the transition
  to a validated inference artifact.
- Part IV stops at model-artifact production. Prefill, Decode, KV Cache,
  batching, serving engines, and online scheduling remain in Part V.

All fifteen chapters have one central thesis, defined mathematical symbols,
shape or state-flow examples, engineering trade-offs, self-check questions,
`Review notes`, and primary-source or official-documentation entry points.
They remain `Draft`; no chapter is promoted to `Review` or `Final` in this
pass.

### LLM Acceleration Materials Migration

Status: Draft migration completed; raw materials removed

Repository paths:

`books/part-02-model/12-embedding.md`

`books/part-02-model/14-self-attention.md`

`books/part-02-model/21-moe.md`

`books/part-02-model/22-long-context.md`

`books/part-04-training-system/30-lora.md`

`books/part-04-training-system/36-distributed-training.md`

`books/part-04-training-system/37-tensor-parallel.md`

`books/part-04-training-system/38-pipeline-parallel.md`

`books/part-04-training-system/39-zero.md`

`books/part-04-training-system/40-megatron.md`

`books/part-04-training-system/41-deepspeed.md`

`books/part-05-inference-system/42-what-happens-during-inference.md`

`books/part-05-inference-system/43-prefill.md`

`books/part-05-inference-system/44-decode.md`

`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`

`books/part-05-inference-system/46-continuous-batching.md`

`books/part-05-inference-system/47-pagedattention.md`

`books/part-05-inference-system/48-speculative-decoding.md`

`books/part-05-inference-system/49-tensorrt-llm.md`

`books/part-05-inference-system/50-vllm.md`

`books/part-05-inference-system/51-sglang.md`

`books/part-05-inference-system/54-gpu-memory.md`

`books/part-05-inference-system/55-pd-disaggregation.md`

`books/part-05-inference-system/56-inference-scheduling.md`

Core understanding:

The LLM Acceleration source materials have been migrated into the roadmap as
Draft chapter content, rather than preserved only as source notes.

The migrated knowledge spans:

- vectorization, cosine similarity, matrix computation, and embeddings;
- Self Attention as both a model mechanism and a memory-IO engineering problem;
- MoE sparse activation and expert routing;
- LoRA / QLoRA / distillation as low-cost fine-tuning paths;
- distributed training through DP / TP / PP / ZeRO / Megatron / DeepSpeed;
- inference through Prefill / Decode / KV Cache / batching / PagedAttention /
  Speculative Decoding / vLLM / SGLang / TensorRT-LLM;
- GPU memory, long context, Ring Attention, ShadowKV, PD disaggregation, and
  inference scheduling.

The organizing constraint is full-stack acceleration: matrix computation,
memory hierarchy, communication, runtime scheduling, and software/hardware
co-design.

The original source files and the temporary material-review document have been
removed from the repository after migration. The chapter Drafts are now the
working source of truth for this learning cluster.

### Part V Inference System: Chapters 42-56

Status: Draft completed; cross-chapter Review completed

Repository paths:

`books/part-05-inference-system/42-what-happens-during-inference.md`

`books/part-05-inference-system/43-prefill.md`

`books/part-05-inference-system/44-decode.md`

`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`

`books/part-05-inference-system/46-continuous-batching.md`

`books/part-05-inference-system/47-pagedattention.md`

`books/part-05-inference-system/48-speculative-decoding.md`

`books/part-05-inference-system/49-tensorrt-llm.md`

`books/part-05-inference-system/50-vllm.md`

`books/part-05-inference-system/51-sglang.md`

`books/part-05-inference-system/52-dynamo.md`

`books/part-05-inference-system/53-kserve-llm.md`

`books/part-05-inference-system/54-gpu-memory.md`

`books/part-05-inference-system/55-pd-disaggregation.md`

`books/part-05-inference-system/56-inference-scheduling.md`

Core understanding:

- LLM inference is a stateful token-generation process. A request moves from
  validation and admission through Prefill, Decode, streaming, completion, and
  state release; TTFT, TPOT, throughput, and goodput measure different parts
  of this lifecycle.
- Prefill converts prompt tokens into first-token logits and initial per-layer
  KV state. Decode advances the same request under an autoregressive
  dependency, making iteration cadence and memory movement first-class system
  concerns.
- The nano-vLLM implementation case now traces that boundary end to end:
  scheduler selection, cached/scheduled token progress, model-runner metadata,
  KV block ownership, sampling commit, repeated Decode, completion, and
  release. Its Prefill-first, phase-exclusive batching and
  release-and-recompute preemption remain versioned policy examples rather
  than definitions of vLLM or Continuous Batching.
- KV Cache exchanges memory for historical-computation reuse. Its logical
  capacity depends on layer count, KV heads, head dimension, dtype, sequence
  length, and concurrency; its physical lifecycle additionally requires
  allocation, sharing, paging, transfer, eviction, and release.
- Continuous Batching, PagedAttention, and Speculative Decoding are orthogonal
  mechanisms. They respectively change batch membership, physical KV
  placement, and target-model progress per serial step.
- Lossless speculative verification is a distribution contract: exact
  acceptance and residual sampling change execution while preserving the
  target distribution. Relaxing verification changes the decoding policy, so
  speed claims require a matched sampling-policy baseline and an explicit
  quality boundary.
- TensorRT-LLM, vLLM, and SGLang organize these mechanisms around different
  historical abstractions: NVIDIA GPU execution optimization, scheduler/KV
  ownership, and prefix/program structure. Current features remain
  version-dependent and overlap.
- Dynamo lifts inference into distributed request, control, and KV-state
  paths. KServe LLM expresses topology, Gateway/InferencePool/EPP routing,
  worker groups, and lifecycle as Kubernetes desired state.
- GPU memory is a joint budget for weights, KV, workspace, communication,
  fragmentation, and reserve. PD disaggregation and inference scheduling can
  improve SLO-aware goodput only when state movement, queueing, and control
  costs are included.

The Part V capability-delivery path is now repository-backed:

```text
validated model artifact
-> request state machine
-> Prefill
-> Decode + KV state
-> batching / paging / speculation
-> TensorRT-LLM / vLLM / SGLang
-> Dynamo / KServe LLM
-> GPU memory / PD / scheduling
-> SLO-constrained online capability
```

Shared state and capacity contracts:

```text
KV_bytes_per_token = 2 * L * H_kv * d_h * bytes_per_element

M_HBM
>= M_weights + M_KV + M_workspace
 + M_communication + M_fragmentation + M_reserve
```

Part V cross-chapter boundaries:

- Chapter 19 owns the model-level KV shape and reuse invariant; Chapter 45
  owns runtime capacity, lifecycle, sharing, eviction, and transfer readiness.
- Chapter 46 owns iteration-level dynamic batching; Chapter 56 owns admission,
  iteration, routing/placement, and autoscaling.
- Chapters 42-44 use nano-vLLM only to ground the minimal Prefill/Decode
  lifecycle; Chapter 46 owns the distinction between scheduling mechanism,
  phase policy, and preemption state disposition; Chapter 50 remains the owner
  of current production vLLM architecture.
- Chapter 47 owns logical-to-physical KV block mapping; Chapter 50 owns the
  complete vLLM V1 serving-engine architecture.
- Chapter 51 owns prefix/program structure as inference-runtime state; Part VII
  owns Agent planning, tools, memory semantics, and workflow governance.
- Chapter 52 owns Dynamo's distributed request/control/state architecture;
  Chapter 55 owns the mechanism and break-even reasoning for PD separation.
- Chapter 53 owns the LLMInferenceService serving topology and request path;
  Chapter 61 owns KServe as a general AI-platform capability.
- Chapter 56 schedules token-generation state; Part VI GPU schedulers place and
  govern Pods, gangs, queues, and cluster resources.

All fifteen chapters remain `Draft`. Framework behavior and API details are
treated as time-sensitive, with current official documentation and primary
papers retained as verification entry points.

### Part IV-V Cross-Part Review

Status: Completed; all chapters remain Draft

Review scope:

- Deep Review of current Chapters 27-56 (legacy Ch23-52), including each chapter's central thesis,
  internal reasoning, input/output contract, adjacent transition, and
  knowledge-tree ownership.
- Contract backtracking into the relevant Part I-II chapters for Tokenizer,
  Decoder-only generation, Sampling, KV Cache, MoE, and Long Context.
- Surgical upstream corrections only; no roadmap or chapter-structure change.

The reviewed capability path is:

```text
Part I   system problem and knowledge tree
-> Part II  model structure and generation semantics
-> Part III multimodal representation, generation, world state and action contract
-> Part IV data, objective, training state and deployment artifact
-> Part V request state, runtime execution, memory and SLO delivery
```

Resolved cross-Part contracts:

- `B_global` now consistently means
  `B_micro * gradient_accumulation_steps * data_parallel_degree`; local tensor
  batch dimension `B` remains a separate shape symbol.
- PPO-style RLHF and DPO both use `beta` around a reference-policy trade-off,
  but their estimators, reductions, adaptation and configuration values are
  not treated as interchangeable.
- A checkpoint is handed to inference only after architecture, tokenizer,
  chat template, adapter state, quantization, runtime format, lineage and
  conversion validation form a deployment-artifact identity.
- Training `DP/TP/PP/CP/EP` layout and inference `TP/PP/EP` layout are separate
  mappings. Serving may reshard global tensors and must validate the result.
- Chapter 19 owns model-level KV shape; Chapter 45 owns runtime lifecycle;
  Chapter 47 owns paging; Chapters 54-56 own capacity, PD and scheduling.
- MoE flows from router/expert semantics through training Expert Parallel to
  inference dispatch and runtime communication. Long Context flows from model
  semantics through training data/Context Parallel to Prefill, KV capacity
  and SLO constraints.
- LoRA flows from adapter parameterization through checkpoint lineage to
  merge or dynamic multi-adapter Serving; adapter identity participates in
  batching and prefix-cache correctness.
- Continuous Batching, PagedAttention and Speculative Decoding remain
  orthogonal scheduling, memory-placement and serial-execution mechanisms.
- KServe LLM and inference scheduling stop at the LLM data/control path;
  organization-wide platform governance and GPU-cluster scheduling remain in
  Part VI.

Current framework claims were refreshed against official documentation for
Megatron Core, TensorRT-LLM, vLLM V1, SGLang, NVIDIA Dynamo and KServe
LLMInferenceService. Version-dependent behavior is labeled as such; paper
results are not automatically projected onto current implementations.

No chapter was promoted beyond `Draft`. At the time of that legacy review, the
next position was legacy Part V, Chapter 53; after ADR-008 this owner is Part VI,
Chapter 57: 什么是 AI Platform.

### Daily Research Integration: Quantized Artifact and GPU Capacity

Status: Completed; affected chapters remain Draft

Source record:

`papers/2026/07/27/README.md`

Updated repository chapters:

`books/part-04-training-system/35-checkpoint.md`

`books/part-05-inference-system/49-tensorrt-llm.md`

`books/part-05-inference-system/54-gpu-memory.md`

`books/part-05-inference-system/56-inference-scheduling.md`

Stable understanding integrated in this pass:

- A deployment artifact must carry more than quantized tensors and scales.
  Numerical semantics, module/parameter mapping, structural graph rewrites,
  kernel and hardware capabilities, and quality evidence jointly define the
  executable artifact contract.
- Low-bit storage does not by itself prove lower end-to-end latency.
  Quantize/dequantize work, kernel launches, unfused memory traffic, and
  non-quantized operators remain in the execution path.
- Generic module replacement lowers model-integration cost and preserves
  framework composability. Architecture-specific graph rewrites and kernel
  fusion can reduce execution overhead, but increase build, validation, and
  support-matrix cost.
- Scheduler-visible KV capacity is derived from HBM only after fixed weights,
  peak workspace and communication, fragmentation, and reserve are removed.
  Therefore total-HBM ratios do not directly equal KV-capacity, concurrency,
  throughput, or goodput ratios.
- Admission consumes the remaining usable KV budget after resident requests
  and safety margin. It cannot infer a capacity gain from an artifact label
  unless the corresponding quantization and kernel path is actually active.
- The Nunchaku Lite and AMD MI455X reports are retained as bounded mechanism
  cases. Their version-, hardware-, and workload-specific results are not
  promoted to general performance claims.

Cross-chapter contract after this pass:

```text
Chapter 35
  validated numerical + graph + execution artifact identity
-> Chapter 49
  runtime build, quantization, graph rewrite and kernel execution plan
-> Chapter 54
  weights, KV, workspace and reserve compete within usable HBM
-> Chapter 56
  admission and scheduling operate on the resulting capacity
```

This integration did not change chapter maturity or course position. At that
legacy checkpoint, the next position was Part V, Chapter 53; after ADR-008 it
maps to Part VI, Chapter 57.

### Part VI AI Infrastructure: Chapters 57-73

Status: Draft completed and cross-chapter reviewed

Repository scope:

`books/part-06-ai-infrastructure/57-what-is-ai-platform.md`

through:

`books/part-06-ai-infrastructure/73-production-best-practice.md`

Core understanding:

- An AI Platform is a set of stable identity, state, policy, and feedback
  contracts around AI artifacts and expensive compute. It is not a portal,
  a Kubernetes passthrough, or a collection of unrelated tools.
- Kubeflow provides composable Kubernetes-native lifecycle subprojects.
  Model Registry, Training Operator, KServe, and Gateway respectively own
  artifact identity, training-workload reconciliation, serving desired state,
  and external traffic policy.
- GPU scheduling is a topology-, gang-, queue-, and fairness-constrained
  placement problem. Volcano and KAI Scheduler are reviewed as two mechanism
  mappings rather than as feature lists.
- Evaluation System maps intended use into versioned subjects,
  datasets/environments, scorers, per-example evidence, slices, uncertainty,
  and release decisions. MLflow remains one metadata/evidence implementation;
  it does not define quality semantics or replace workload, serving, tenancy,
  or resource control planes.
- Metrics, Logs, and Traces remain distinct evidence signals: aggregate
  health, event records, and per-operation causal paths. Shared identities
  connect them without collapsing their retention, cardinality, or privacy
  contracts.
- Cost is attributed resource-time under quality and SLO constraints.
  Multi-tenancy propagates identity and isolation across control, data,
  resource, and evidence planes. Security adds lifecycle provenance,
  least-privilege execution, validation, audit, and threat-driven controls.
- Production readiness is a continuous evidence and control loop across
  immutable artifacts, release gates, SLOs, rollback, cost, tenancy,
  security, and feedback. It is not a one-time launch checklist.

The Part VI platform path is now repository-backed:

```text
Part IV deployment artifact
-> Part V runtime state and SLO
-> platform identity and lifecycle contracts
-> Kubeflow / Registry / Operator / KServe / Gateway
-> GPU scheduling and queue governance
-> Evaluation evidence and release decisions
-> Metrics / Logs / Traces
-> cost / tenancy / security
-> production feedback and recovery
```

Part VI cross-chapter and cross-Part boundaries:

- Chapter 56 schedules request/token/KV state at inference-runtime time;
  Chapters 63-65 place Pods, gangs, and GPU resources at cluster time.
- Chapter 35 owns checkpoint and deployment-artifact formation; Chapter 59
  owns immutable model identity, lineage, evidence, aliases, and promotion
  metadata.
- Chapter 53 owns `LLMInferenceService` topology and EPP request paths;
  Chapter 61 owns the general KServe service lifecycle and Runtime abstraction.
- Chapter 60 maps Part IV training topology into Kubernetes workloads but
  does not change TP/PP/DP/CP/EP mathematics or replace gang scheduling.
- Chapter 66 owns the common Evaluation contract and keeps MLflow as an
  implementation mapping. Chapters 67-69 separately own aggregate metrics,
  event evidence, and causal traces; observed state and quality judgment share
  identity without becoming the same system.
- Chapter 72 freezes the platform security boundary for Prompt and Tool
  execution without pre-empting Part VII's Agent mechanisms.
- Chapter 73 hands Part VII immutable identity, policy, trace, budget,
  security, audit, and recovery contracts. Agent execution extends these
  contracts instead of creating a parallel governance system.

Current framework claims were checked against the July 2026 official
documentation for Kubeflow, Kubeflow Trainer, KServe 0.18, Gateway API and its
Inference Extension, Kubernetes DRA, Volcano, KAI Scheduler, MLflow, and
OpenTelemetry. The Evaluation structure was additionally checked against
primary research for holistic evaluation, LLM-as-a-Judge, AgentBench, and
SWE-bench, plus the NIST AI RMF MEASURE function. Version-dependent APIs are
labeled as such.

All seventeen chapters remain `Draft`. At the time of that pass, the next
legacy repository-backed learning position was Part VI, Chapter 70: Prompt;
after ADR-008 this is Part VII, Chapter 74.

### Part VII Agent: Chapters 74-84

Status: Draft completed and cross-chapter reviewed

Repository scope:

`books/part-07-agent/74-prompt.md`

through:

`books/part-07-agent/84-agent-platform.md`

Core understanding:

- Prompt is a versioned runtime input to a conditional model distribution,
  not a deterministic program or a security boundary.
- Context is the authorized, selected, ordered working set for one model call.
  RAG supplies external evidence; Memory persists state across calls through
  governed write, read, consolidation, correction, and forgetting policies.
- Memory security is a lifecycle from persistence through recall, adoption,
  external consequence, and selective repair. Recovery must remove malicious
  semantics while preserving required benign state and propagating the change
  through derived views.
- Context production can reuse heterogeneous derived views, but lexical,
  dense, structural, and history views keep operation-specific freshness and
  validity boundaries. In agentic retrieval, relevance can guide interaction
  order and observation selection without becoming evidence or authorization.
- Tool Calling converts model output into a typed proposal. A trusted executor
  still owns schema and semantic validation, authorization, approval,
  idempotency, execution, result filtering, and audit.
- Planning represents future state transitions with dependencies,
  preconditions, budgets, and completion evidence. Reflection is a bounded
  inference-time feedback loop, not RLHF or a parameter update.
- Workflow is the durable deterministic spine for Agent execution. It owns
  state transitions, retries, replay, approval, cancellation, compensation,
  and terminal evidence while model-driven nodes retain bounded flexibility.
- Multi-Agent creates value only when tasks, evidence, models, tools, or
  authority can be meaningfully decomposed. Multiple personas do not create
  independent evidence by themselves.
- MCP standardizes lifecycle, capability negotiation, messaging, and the
  connection of resources, prompts, and tools. It does not establish server
  trust, business authorization, workflow reliability, or Agent coordination.
- Agent Platform extends the Part VI platform with goal, plan, context, memory,
  action, delegation, approval, and long-running workflow state. It reuses the
  same identity, resource, evidence, cost, tenancy, security, and recovery
  substrate rather than creating a parallel platform.

The Part VII runtime path is now repository-backed:

```text
Prompt
-> Context assembly
-> RAG / Memory reads
-> Model proposal
-> Tool authorization and execution
-> Observation
-> Planning / Reflection
-> durable Workflow
-> Multi-Agent delegation
-> MCP connectivity
-> governed Agent Platform
```

Part VII cross-chapter and cross-Part boundaries:

- Chapter 74 owns runtime prompting; Chapter 29 owns SFT and parameter-level
  behavior adaptation.
- Chapter 22 owns long-context model/system limits; Chapter 75 owns runtime
  selection, ordering, compression, trust, and token-budget assembly.
- Chapter 76 owns external evidence retrieval; Chapter 77 owns persisted
  cross-call state and its write/forget lifecycle.
- Chapter 78 owns typed tool intent and execution boundaries; Chapter 83 owns
  MCP connectivity and capability negotiation.
- Chapter 79 owns a revisable plan; Chapter 81 owns durable authoritative
  workflow state. Chapter 80 owns inference-time feedback and does not modify
  the Part IV optimization objectives.
- Chapter 82 assigns bounded responsibility among Agents but relies on
  Chapter 81 for shared fact state and recovery.
- Chapter 84 extends Part VI governance to the action loop. Part V continues
  to own token/KV scheduling and Part VI continues to own GPU and tenant
  resource governance.

Current claims were checked against primary papers for in-context learning,
RAG, Memory, Tool use, planning, reflection, Multi-Agent, and Agent
evaluation. MCP is explicitly pinned to the published `2025-11-25`
specification; the 2026-07-28 release candidate is not treated as an already
released stable contract. Agent identity and authorization are described as
an evolving standards area using current NIST material.

All eleven chapters remain `Draft`. All seven roadmap Parts and Chapters 1-84
are now repository-backed Drafts.

### Evaluation System Structural Integration

Status: Structural decision and cross-chapter integration completed; affected
chapters remain Draft

Primary owner:

`books/part-06-ai-infrastructure/66-evaluation-system.md`

Decision record:

`docs/DECISIONS.md` ADR-004

Stable understanding integrated in this pass:

- Evaluation is a first-class control-loop system, not a benchmark list,
  metrics dashboard, or synonym for MLflow.
- Every evaluation claim is conditional on a versioned subject, an input
  distribution or environment, an execution path, and one or more scorers.
- Finite evaluation results estimate deployment behavior only under explicit
  assumptions about contamination, distribution relevance, scorer validity,
  sampling, slices, and uncertainty.
- Model, end-to-end system, runtime/service, and Agent/trajectory evaluation
  share evidence contracts while retaining different local failure modes.
- Offline, replay, shadow, canary, and continuous online evaluation provide
  complementary evidence and cannot be collapsed into one universal stage.
- Evaluation Run is immutable evidence; promotion, rollback, hold, and
  investigation are separate policy decisions with owners and expiring
  exceptions.
- Observability records what happened. Evaluation judges whether the observed
  behavior satisfies a specified objective. They share identity and evidence
  but remain different system responsibilities.
- Production feedback becomes training data, prompt, retrieval, model, or
  policy change only after provenance, attribution, privacy, quality, and
  version controls.
- MLflow maps experiments, runs, datasets, models, metrics, artifacts, and
  traces to part of the evidence plane. It does not define intended use,
  scorer validity, risk thresholds, or release authority.

Cross-chapter contract after this pass:

```text
Part IV data / training / checkpoint
-> Part VI Registry identity
-> Chapter 66 EvalSpec / Evaluation Run / Decision
<-> Chapters 67-69 observed Metrics / Logs / Traces
-> Chapter 73 gated release and production feedback
-> Part VII component and trajectory evaluation
```

This change resolved the repository-wide Review finding that Evaluation was
promised by the Part I knowledge tree but had no chapter owner. The legacy
Chapter 62 was refactored instead of inserting an Evaluation chapter; ADR-008
later moved that same owner to current Chapter 66.

### Repository-wide Draft Review Pass 1

Status: Completed

Scope:

- 26 chapters with repository status `Draft`.
- Part I: Chapters 1-2.
- Part II: Chapters 12, 14, 21, and 22.
- Legacy Part III: Chapters 26 and 32-37 (current Part IV, Chapters 30 and 36-41).
- Legacy Part IV: Chapters 38-47 and 50-52 (current Part V, Chapters 42-51 and 54-56).

At the time of that earlier pass, the 54 `Placeholder` chapters were
intentionally left unchanged.

Completed in this pass:

- Ensured every existing Draft has a distinct thesis, knowledge-tree role,
  self-check questions, and `Review notes`.
- Removed all remaining references to the deleted internal PPT, HTML, DOCX,
  and source-material files from chapter prose.
- Rebuilt the Part II Drafts around model mechanisms and mathematical
  boundaries rather than material summaries.
- Separated the Part III overview, mechanism, and runtime layers to reduce
  repetition across distributed training, TP, PP, ZeRO, Megatron, and
  DeepSpeed.
- Strengthened Part IV with explicit workload assumptions, memory formulas,
  runtime state, scheduling layers, and framework-version boundaries.
- Kept every reviewed chapter at `Draft`: this pass improves the working
  manuscripts but does not claim Final-level completeness.

## Current Course Position

Current position:

Parts I-VII complete as repository-backed Drafts

The repository-backed course now has a continuous worldview, model-mechanism,
capability-production, online capability-delivery, evaluation, and
platform-governance spine, extended through the complete Agent action loop. A
task can be traced from model capability and a governed artifact through
inference, EvalSpec and release evidence, platform policy, Context, Memory,
tools, Workflow, external effects, observation, evaluation, and feedback.

Next learning phase:

Papers-driven cross-Part refinement and verification. No new linear chapter
position remains in the current roadmap.

## Next Focus

- Refine existing chapters only when papers, official specifications, source
  materials, or real system evidence add durable knowledge or correct an
  existing contract.
- Use Part I as the worldview, Part II as the model contract, Part III as the
  multimodal representation/generation/world/action contract, Part IV as the
  capability-production contract, and Part V as the online inference-runtime
  and SLO contract. Use Part VI as the platform identity, resource, evidence,
  tenancy, security, and production-governance contract. Use Part VII as the
  governed Context-to-action runtime contract.
- Keep Parts I-VII at `Draft`; promotion to `Review` or `Final` remains a
  separate maturity decision after papers-driven refinement and a later
  repository-wide primary-source review.
- Use `ROADMAP.md` as the single source of truth for chapter order.
- Update the existing knowledge-tree node instead of appending disconnected
  paper notes to a chapter.
- Do not modify books merely to produce a diff; preserve the current argument
  when new material does not change durable understanding.
- Before finalizing any chapter that uses recent systems or research claims,
  verify against primary sources and avoid treating internal slides as
  authoritative evidence.

## Dual-Axis Knowledge Tree Structural Integration

Status: Structural decision and cross-Part integration completed; all affected
chapters remain Draft

Decision record:

`docs/DECISIONS.md` ADR-005

Stable understanding integrated in this pass:

- ADR-005 originally established six Parts and five horizontal lenses. ADR-008
  supersedes only the vertical structure: seven Parts now form the top-level
  reading and ownership tree, while the Compute, Memory, Communication,
  Scheduling and State lenses remain unchanged.
- Compute, Memory, Communication, Scheduling, and State are now explicit
  horizontal reading lenses. They connect constraints across Parts without
  creating duplicate chapter ownership.
- Horizontal chapter sequences are thematic routes rather than implicit
  direct-evolution arrows. Cross-Part handoffs now label layering, principle
  reuse, or semantic change where the relationship is easy to overread.
- Memory asks about placement, capacity, movement, retention, and eviction;
  State asks about identity, ownership, version, validity, commit, and
  recovery. A chapter may participate in both without merging the questions.
- Historical links distinguish direct evolution, layering/dependency,
  principle reuse, and explanatory analogy. Similarity alone is not evidence
  of implementation lineage.
- Current Chapter 36 (`TRAIN-DISTRIBUTED-TRAINING`; legacy Ch32) is the primary communication-foundations owner. It separates
  communication semantics, collective algorithms, runtime/library,
  transport/protocol, and physical topology.
- The communication path now connects local IPC and MPI concepts to training
  collectives, parallel strategies, and inference state transfer without
  presenting MPI, NCCL, UCC, and NIXL as a product-replacement sequence.
- Current Chapters 37-40 consume the common communication model for TP, PP, state
  sharding, and multidimensional training. Current Chapters 52 and 55 extend it to
  request-scoped KV state movement. Current Chapter 63 owns topology-aware placement
  at the platform control plane.
- The State route now includes Chapter 19 as the origin of KV runtime state
  and current Chapter 75 as per-invocation working state before Chapter 77 persisted
  Memory and Chapter 81 authoritative Workflow state.
- Compute, Memory, Scheduling, and State cross-Part anchor chapters now include
  short handoffs that name the previous constraint, the next owner, and the
  relationship between them.
- Framework case-study chapters now name the stable system problem before the
  current implementation example. Stable Node IDs now preserve that ownership
  even though ADR-008 changed the reading order and paths.

Updated reading model:

```text
formal reading / ownership axis:
  Part I: Worldview and coordinate system
  Part II-VII: Model -> Multimodal/World/Action -> Training
               -> Inference -> Infrastructure -> Agent

horizontal lenses:
  Compute | Memory | Communication | Scheduling | State
```

This change improves navigation and cross-Part reasoning but does not promote
chapter maturity or claim that every horizontal path is final. Future
papers-driven work should refine the existing owner chapter and update the
cross-Part path only when a durable system contract changes.

## 2026-07 Historical Research Refinement

Status: 2026-07-01 through 2026-07-26 backfill integrated; chapters remain Draft

Stable understanding integrated in this pass:

- Interpretability evidence now follows an explicit ladder from behavioral
  correlation and decodability to localized intervention, downstream change,
  and cross-context or cross-model replication. Jacobian-adjusted readout is
  retained as an experimental example, not a final map of model knowledge.
- Speculative verification depth is a scheduler-visible capacity decision.
  Expected accepted progress must be compared with draft, verification, and
  target-batch opportunity cost; a fixed maximum draft length is not a
  workload-independent optimum.
- Distributed inference routing may depend on conditional compute locality in
  addition to queue, KV reuse, transfer, and topology. MoE expert signatures
  are one experimental signal, not a universal routing contract.
- Once routing depends on shared distributed state, selection becomes a
  control plane with independent scaling, sharding, consistency, failure,
  backpressure, and observability requirements.

Repository-backed refinements:

- Chapter 5: interpretability evidence ladder.
- Chapters 44 and 52: capacity-aware speculative verification.
- Chapter 48: conditional service cost and selection/state-index boundaries.

No chapter was added or renumbered, no existing design conclusion was
reversed, and no chapter was promoted beyond Draft. The later full-source audit
did promote the durable mechanism in GRAM and Kimi K3 into existing owner
chapters; Harness Handbook, AgentCompass, Ring-Zero, HiKV, Ground Truth First,
and later live-run candidates remain bounded Daily/Weekly evidence or were
already covered without duplicate prose.

## 2026 Historical and Live Weekly Coverage

Status: W01 through W32 material recheck completed at the candidate-ledger level; Review Pending is zero; 41 unique
material requests remain (36 source families, one StreamMA revision/artifact sub-gap, three W32 identity gaps,
and one deduplicated Google Scholar/OpenAlex discovery export);
Archive Completion Gate remains Open; eligible Source-Family Books Gates may pass independently; prior broad Books decisions remain provisional;
W31/W32 Live Weekly coverage is 7/7 Daily

Repository index:

`papers/2026/weekly/README.md`

Coverage and archive decisions:

- The prior 93/93 Source Review and Books Gates established completeness only
  for candidates already admitted to the historical score tables. They did not
  establish discovery recall. W01 through W30 are therefore being re-opened at
  the Weekly evidence layer with a 20/30 retention threshold; existing Book
  prose and candidate reviews remain provisional inputs and are not rolled back.
- The annual `Historical Decision Chronicle` is intentionally non-additive: its early rows preserve the legacy
  93-row baseline while later rows contain recovered per-week checkpoints. Current arithmetic belongs only to the
  `Current Provisional Recovered Ledger`; the legacy `93/93` statement is not a current discovery census.
- The 2026-08-13 material recovery pass restored ViPO, Qwen-Image-2.0, the four W21 blockers, all twenty-seven
  W22 primary-text blockers, Continual Experience Internalization, VIA-SD, AgenticSTS, ElastiCo, OasisKV, TAOT,
  and KServe v0.20.0. The current provisional archive contains 1,143 scored rows: 707 high, 383 mid, and 53 low.
  Remaining source and identity gaps are deduplicated in the annual `Remaining Primary-Source Material Ledger`;
  they are not counted as ordinary review pending and do not authorize Books edits.
- Each historical week must now reconcile screened primary-source hits,
  below-threshold/out-of-scope aggregates, cross-week and revision duplicates,
  existing and newly recovered candidates, Source Reviews, and unresolved
  evidence. A Source Family enters Books only after its own identity, full-read,
  evidence-boundary, artifact and owner checks pass; this does not close the
  archive-wide discovery Gate.

- W05 has been expanded from 3 to 43 candidates. PaperBanana and Sweet Spot
  Learning were the final two source blockers; their paper methods, implementation,
  evaluation, ablations, limitations, appendices, and official artifacts are now
  recovered and bounded without treating product pages or aggregate benchmark
  claims as mechanism evidence. W05 therefore has 43/43 non-template Full Source
  Reviews and its Candidate Evidence Gate has passed. On 2026-08-13, all 43
  candidates also received chapter-level Books dispositions and an independent
  weekly reverse review: 28 Integrate/Refine, 11 No Change, 3 Weekly Only, and
  1 Reject, refining 17 owner chapters. The W05 Source-Family Books Gate is
  complete; its reproducible discovery census and Archive Gate remain open.
- W06 has 38/39 Full Source Reviews. The Claude Opus 4.6 official system
  card identity, table of contents, and indexed section taxonomy are verified, but
  the approximately 14 MB PDF cannot be fully read through the primary-source
  reader and direct browser access was rejected by user-side website permission.
  No bypass or snippet-based reconstruction was used. Claude remains `Unverified /
  Blocked / No Books Change`. Under the approved blocked-skip rule, all 41 scored
  rows now have final dispositions: 21 Integrate/Refine, 15 No Change, 4 Weekly
  Only, and 1 Unverified. Fifteen Stable Node owners have been integrated and
  independently reverse-reviewed. W06 Source-Family Books Gate is complete; only
  the blocked source and weekend/cross-index discovery gaps keep its Archive Gate open.
- W07 has 49/49 accessible non-template Full Source Reviews. InternAgent-1.5 remains the only
  candidate blocker because its 22.8 MB official PDF exceeds the direct reader.
  Search-indexed primary-text passages, the table-of-contents and appendix scope,
  the official Shanghai AI Lab release, repository, and February solution-refinement
  artifact now support a detailed partial packet covering mechanism, evaluation,
  memory ablation, limitations, and Chapters 72-78 deduplication. They do not prove
  page-complete coverage, so the review did not turn snippets into a false Full Source
  Review. The blocked-skip Candidate Review Gate therefore passes with one explicit
  `Unverified / Blocked / No Books Change` family. All 52 scored rows now have final
  Books dispositions: 39 Integrate/Refine, 7 No Change, 3 Emerging/Experimental,
  2 Weekly Only, and 1 Unverified. Sixteen Stable Node owners were integrated and
  independently reverse-reviewed. W07 Source-Family Books Gate is complete; the
  release/RFC, Scholar/OpenAlex recall gaps and blocked full text keep only the
  Archive Completion Gate open.
- W09 has been expanded from 2 to 62 in-window candidates through same-week
  scanning, post-week curation-lag checks, DBLP cross-index recovery, and
  source-family first-public deduplication. Fifty-eight candidates now have
  non-template Full Source Reviews, and four low-score candidates have completed
  source/date/score/rejection checks. Qwen3-Coder-Next and SkillNet were the last
  two open packets; both now include paper, appendix, official artifact, evidence
  boundary, evolution, and target/adjacent-chapter review. The W09 Candidate
  Evidence Gate is therefore 62/62 passed. Google Scholar/OpenAlex historical
  access remains a documented discovery limitation rather than an unresolved
  candidate packet. On 2026-08-13, all 62 candidates received final dispositions after target and adjacent-
  chapter review: 52 Refine, 6 No Change, and 4 Weekly Only. Twenty-four Stable Node owners were refined without
  adding isolated chapters or copying release/benchmark summaries; each owner group and the unified ledger passed
  independent review. W09 Source-Family Books Gate is complete. Google Scholar/OpenAlex historical discovery
  coverage remains a documented limitation, so the Archive Completion Gate stays open.
- W10's first 2026-08-09 checkpoint expanded the baseline 3-item report to 23
  candidates, completed 23/23 Source Reviews and 18/18 Books dispositions, and
  integrated durable mechanisms into Chapters 20, 23-25, 29, 39, 45, 62, 68,
  and 72-73. A later W11 discovery pass found 11 additional papers whose primary
  v1 dates fall in W10. W10's Discovery and Evidence Gates were therefore reopened;
  the earlier reviews and Book prose remain valid for their candidate set
  but no longer establish week-level recall completeness. MLRA, DistriVoting,
  ProRes, BandPO, Sparse-BitNet, ATLAS, Terminal Coding Agents, AutoResearch-RL,
  HCAPO, Scaling Data Difficulty, and MicroCoder-GRPO have now completed non-template
  Full Source Review. AutoResearch-RL was downgraded to `Withdrawn / Disputed /
  Weekly Only` after its arXiv admin withdrawal. The W12 curation-lag audit then recovered
  one additional 2026-03-07 spillback, and Nemotron 3 Super moved back from W16 because its
  base checkpoint first shipped on 2026-03-04. On 2026-08-12, Recursive Language Models Meet
  Uncertainty completed a full 31-page, experiment/appendix, and Ch22/72/76/62 adjacency review.
  W10 now has 36/36 scored reviews and zero pending candidates. Its recorded-candidate Evidence
  queue is complete, while broader historical discovery coverage remains an Archive limitation.
  On 2026-08-13, W10 completed 36/36 final Books dispositions: 27 Refine, 4 No Change, and 5 Weekly
  Only/Disputed. Fifteen Stable Node owners were refined and independently reviewed. SRLM now refines
  `MODEL-LONG-CONTEXT` / Ch22 by separating context capacity, programmatic traversal, candidate coverage,
  trajectory selection, and external acceptance, while recording that K=8 parallel wall-clock is not
  resource-matched. W10 Source-Family Books Gate is complete; Archive Completion Gate remains open.
  Nemotron's 51-page report, base/post-trained model cards, public artifact surface, and
  Ch20-22/24/29/41/45 adjacency are audited. Its provisional Ch21 refinement separates latent-
  coordinate expert dispatch, hybrid KV/recurrent state, native MTP draft verification, per-operator
  precision, and mixed-policy-age RL; vendor throughput ratios are excluded from general conclusions.
- W11 has been expanded from 2 to 55 scored in-window candidate families and records 11
  W10 spillbacks separately. RAGEN-2 moved back from W15 because the official repository records a
  2026-03-12 release; its sole later arXiv v1, all appendices, project/repository, current artifact, and
  Ch27-29/62 adjacency have a complete Source Review. Fifty-two of fifty-three `20+` candidates now have complete
  current-schema Source Reviews; Neural Thickets and the SFT-versus-RL survey have completed low-score source,
  date, experiment-boundary, and rejection check. EvoScientist's sole v1, full method/evaluation/appendices,
  later artifact boundary, and Ch73/77/76/62 adjacency are audited; its derived-memory mechanism is already
  covered with stronger provenance and workflow-authority boundaries, so it is `No Change — Already Covered /
  Experimental Case`. MEMO's current 38-page v2, v1/v2 history, algorithms, all experiments/ablations/appendices,
  five-commit official repository surface, and Ch73/62/77/78 adjacency are also audited. It is provisionally a
  Ch73 Experimental refinement: persistent derived memory, conservative population selection, and seed-preserving
  rare-state replay must be governed as one context-optimization loop, while all-memory and heavy replay ablations
  preserve the need for fresh exploration. The five text games, three runs, unmatched RL resource contract, missing
  hardware/total cost, and absent memory provenance/rollback prevent generalization. Reasoning as Compression's v1,
  revision history, CIB derivation, experiments/appendices and Ch28～30/20/62 adjacency are audited; it is provisionally
  a Ch29 Experimental refinement because it turns uniform token cost into a versioned prior-dependent reward contract,
  while prior surprisal is not semantic truth or production latency evidence. Deep Tabular Research's 23-page paper,
  revision, path-selection/memory algorithms, benchmark construction, ablations, cases and Ch73～77/62 adjacency are
  audited; it is provisionally a Ch75 Experimental refinement because planner-owned path statistics and execution
  feedback make replanning state explicit, while artifact, hardware, governance and independent-evaluation evidence are
  missing. FinToolBench's v1/current revision, full paper/appendices, official partial benchmark artifact and
  Ch62/68/74 adjacency are audited. It is `No Change — Already Covered / Experimental Evaluation Case`: existing
  chapters already separate selection, authorization, execution, observation, final outcome and policy-bound sensors,
  while the paper's real-API finance trace is retained as a dated case rather than a compliance guarantee. FineRMoE's
  primary chronology starts at its 2025-09-11 OpenReview submission, so it is rerouted to the 2025 backlog rather than
  scored in W11. Groundsource remains an unresolved blocked-backlog item: preprint metadata, the Google Research technical article, and the dataset
  record are verified, but EarthArXiv full-paper access is blocked by site verification
  and user-side browser permission. It remains `Unverified / Blocked` and is skipped for forward progress under
  the user-approved rule; this preserves an Archive source gap without blocking the later W11 Source-Family Books Gate. The W12 curation-lag
  audit recovered 28 additional events whose first-public dates fall in W11; after EvoScientist, MEMO, Reasoning as
  Compression, Deep Tabular Research, FinToolBench, LookaheadKV, UCIP, One-Eval, LMEB and Video Streaming Thinking,
  with FineRMoE rerouted and Safe Web Agent Learning marked `Unverified / Blocked Identity`, daVinci-Env / OpenSWE,
  MM-CondChain, ReBalance, Expert Threshold Routing, BAVT, EnterpriseOps-Gym and EvoClaw / SWE-Milestone have also completed full paper,
  artifact/evaluation-contract,
  and adjacent-chapter review. OpenSWE and MM-CondChain
  provisionally refine Ch23 and Ch62 respectively: executable environment plus verifier becomes part of training-sample
  identity, while conditional evaluation must balance true/false paths and expose continue bias. ReBalance and Expert
  Threshold provisionally refine Ch20 and Ch21: the former treats model-state feedback as a bidirectional reasoning-
  control artifact, while the latter causalizes Expert Choice with versioned population cutoff state and accepts
  per-batch load variance. BAVT provisionally refines Ch75 by making remaining token/tool budget part of search state
  while separating critic-threshold termination from answer correctness. EnterpriseOps-Gym is `No Change / Ch62
  Experimental Evaluation Case`: executable final-state, integrity, policy, side-effect and infeasible-refusal contracts
  are already covered, while its oracle-tool and plan/decomposition ablations remain useful dated evidence.
  EvoClaw / SWE-Milestone is likewise `No Change / Ch62 Experimental Evaluation Case`: Ch62 already preserves
  snapshot-to-persistent-state evolution, F2P/P2P-style feature/regression separation, state/action/test evidence,
  technical debt, rollback and harness revision. TERMINATOR has verified metadata, project and model artifacts, but
  no readable full-paper text; it remains unscored `Unverified / Blocked Full Text` and is skipped for forward progress.
  GradMem's sole-v1, all appendices, official implementation, WRITE/READ state, second-order training, break-even
  analysis and Ch22/39/73 adjacency are audited; it is provisionally a Ch22 Experimental refinement. The SFT-versus-RL
  survey is retained at 19/30 as Weekly-only secondary synthesis and cannot substitute for the primary papers it cites.
  HomeSafe-Bench and Think While Watching have verified identities but no arXiv HTML; their
  official PDFs are blocked by the saved browser permission, so both remain unscored `Unverified / Blocked Full Text`.
  AI Can Learn Scientific Taste, AgentProcessBench, V-JEPA 2.1, and KServe v0.17.0 subsequently completed
  v1/revision, full-paper or versioned official-docs, artifact, and adjacent-chapter review. Their dispositions are,
  respectively, No Change for Ch27, provisional Ch62 Experimental refinement, provisional Ch5 Experimental
  refinement, and No Change for Ch49/57 as a versioned evolution case. These provisional labels record the
  pre-integration audit snapshot and are superseded by the final W11 ledger. Ordinary pending is now zero. Five blocked
  items remain explicit backlog under the user-approved blocked-skip rule.
  LookaheadKV's
  sole-v1, official implementation surface, bounded H100/batch-1 TTFT contract and Ch39/41/50 adjacency support a
  provisional Ch41 Experimental refinement: learned future-utility eviction introduces a versioned selector artifact,
  runtime budget and kept-index lineage, rather than replacing heuristic, draft, FullKV or offload branches. UCIP's
  v1/current-v4, public result artifacts and Ch62/68 adjacency are also audited; its synthetic gridworld separation is
  retained only as `No Change / Experimental Evaluation Case` because the current protocol fails its mimicry and
  high-entropy operating points, does not transfer zero-shot, and does not scale beyond small exact density matrices.
  One-Eval's sole-v1, official repository, planning evaluation contract and Ch61-63/76-78 adjacency are audited;
  it is `No Change / Experimental System Case` because 99% planning executability is neither evaluation validity nor
  model quality, and Ch62 already owns a stricter EvalSpec/evidence/decision contract. LMEB's v1/current-v6,
  22-dataset/193-task suite, official benchmark artifacts and Ch71-73/61-62 adjacency support a provisional Ch73
  Experimental refinement: temporal anchor, retrieval granularity and admissible candidate scope belong in the
  Memory evaluation identity, while the 15-model correlation does not prove capability orthogonality. Video Streaming
  Thinking's v1/current-v2, SFT/RL/data/latency contract, official artifacts and Ch71-73/62/Part-IV adjacency support a
  provisional Ch71 Experimental integration: pre-query Context production can exchange total compute and derived-state
  risk for lower post-query latency, without proving lower end-to-end resource cost.
  RAGEN-2 ultimately refines `TRAIN-GRPO`, but its batch/scorer-dependent MI proxy, biased filtered objective,
  prompt-coverage loss, and undisclosed hardware/uncertainty prevent a benchmark headline or generic claim.
  On 2026-08-13, W11 completed the per-week Books Gate after all 55 scored candidates were rechecked against target
  and adjacent chapters: 31 Integrate/Refine, 20 No Change, 1 Emerging, 2 Weekly Only, and 1 scored blocker across
  17 Stable Node owners; four additional unscored blockers remain outside Books. The owner prose was reviewed for
  evolution, coexistence, state ownership, experiment boundaries and failure modes, then reverse-checked against the
  W11 ledger. W11 Source-Family Books Gate is complete; the broader Historical Archive Gate remains open.
- W12 discovery has been reopened and expanded from the 3-item baseline to 49
  in-window candidate families. Forty-eight score `20+`; Astrolabe is the single
  verified low-score item at 19/30. The date audit separates Hugging Face
  recommendation dates from arXiv v1 first-public dates and records delayed W10/W11
  papers as spillbacks rather than W12 events. The following detailed candidate labels
  preserve the Source Review stage snapshot; every `provisional` label in this W12 block
  is superseded by the final 2026-08-14 weekly Gate paragraph at the end of the block.
  Attention Residuals is the first
  recovered candidate to complete a current-schema Full Source Review: its 21-page
  paper, appendix, official repository, and Ch16-Ch18 context were checked, its owner
  was corrected from Ch15 to Ch17, and the missing public implementation plus
  hardware/precision/distributed evaluation conditions were recorded explicitly.
  Mixture-of-Depths Attention has also completed full-paper, official Triton artifact,
  and Ch14-Ch19 review. It reuses the token query and a unified softmax across sequence
  KV and per-layer depth KV, whereas Attention Residuals changes depth aggregation via
  learned pseudo-queries and optional block summaries; they are parallel depth-retrieval
  branches rather than a replacement sequence. The A100 evidence also shows that MoDA's
  overhead grows with depth, and the full reproducible training recipe remains open. OpenSeeker,
  POLCA, PokeAgent Challenge, and Code-A1 have now also completed full-paper, relevant-appendix,
  official-artifact, and chapter-adjacency review. OpenSeeker's owner moved from Ch74 to Ch72;
  POLCA moved from Ch29 to Ch77; PokeAgent remains Ch62; Code-A1 converged on Ch29. The first
  and last are provisional integration candidates, while POLCA and PokeAgent are chapter-level
  `No Change` candidates. HorizonMath, MiroThinker-1.7/H1, Online Experiential Learning, and
  TRUST-SQL have also completed the same full-source and chapter-adjacency review. Their owners
  converge on Ch62, Ch76, Ch73, and Ch29 respectively; OEL and TRUST-SQL are provisional integration
  candidates, while HorizonMath and MiroThinker are concrete chapter-level `No Change` decisions.
  Efficient Reasoning on the Edge, SWE-Skills-Bench, FlashSampling, and MetaClaw have now completed
  full-paper, revision-history, accessible official-artifact, and chapter-adjacency review. Their owners
  converge on Ch26, Ch80, Ch20, and Ch80 respectively. Efficient Reasoning's reusable base-only prompt
  KV requires masked prompt-side adapter training; SWE-Skills-Bench turns skill value into a paired
  counterfactual and compatibility question; FlashSampling moves exact categorical sampling into the
  LM-head materialization boundary; MetaClaw separates external-skill and parameter-update timescales
  with generation-tagged support/query data. All four are provisional integration candidates, not Books
  changes. Complementary RL, BenchPreS, AdaMem, and VTC-Bench have now completed full-paper,
  appendix, accessible-artifact, and chapter-adjacency review. Their owners converge on Ch29, Ch73,
  Ch73, and Ch62. The first two are provisional new-mechanism candidates, AdaMem is an existing-
  argument refinement candidate, and VTC-Bench is a chapter-level `No Change` decision because its
  durable claims are already covered by Ch62/Ch74; the unresolved 32/35-tool metadata conflict remains
  explicit. Efficient Exploration at Scale, training-free MTP, RAMP, and PRISM now also have full-paper,
  relevant-appendix, artifact-status, and chapter-adjacency reviews. Their owners converge on Ch27,
  Ch44, Ch45, and Ch24. Efficient Exploration and PRISM are provisional new-mechanism candidates;
  training-free MTP refines the existing speculative-decoding proposal taxonomy; RAMP remains
  `Emerging / Experimental` because no executable artifact connects its allocation policy to direct
  runtime evidence and the public contract is internally inconsistent. AI Scientist via Synthetic Task Scaling,
  Nemotron-Cascade 2,
  Memento-Skills, and AndroTMem now also have full-paper, relevant-appendix, artifact, and chapter-adjacency
  reviews. Their owners converge on Ch25, Ch29, Ch80, and Ch73: executable synthetic environments and MOPD
  are provisional new-mechanism candidates, while skill lifecycle and causal state anchors refine existing
  arguments. ProRL Agent, Reasoning over Mathematical Objects, Hyperagents, and lambda-RLM now also have
  full-paper, relevant-appendix, public-artifact, and chapter-adjacency reviews. Their owners converge on Ch29,
  Ch27, Ch77, and Ch77: phase-decoupled rollout service and policy-conditioned reward-model training are
  provisional new mechanisms, while editable improvement-policy search and typed recursive control refine
  existing workflow arguments. Subgoal-driven Agents, LoopRPT, BEAVER, and Reintroducing Markov States
  now also have full-paper, relevant-appendix, evaluation-contract, and chapter-adjacency reviews. Their owners
  converge on Ch75, Ch24, Ch71, and Ch29: milestone progress joins online replanning to training credit;
  latent-step objectives make recurrent compute a learned allocation problem; structure-aware page selection
  refines the context-compression branch; explicit Markov state changes post-training credit and coverage.
  AgentDS, OpenResearcher, BubbleRAG, and HopChain now also have full-paper,
  revision, evaluation-contract, and chapter-adjacency reviews. Their owners converge
  on Ch62, Ch23, Ch72, and Ch23: AgentDS is a chapter-level `No Change`, while
  offline evidence-supported trajectory synthesis, black-box-KG evidence subgraphs,
  and dependency-constrained visual data are provisional integration/refinement candidates.
  Official/Infra recall also recovered Vera Rubin, DSX Air, Dynamo v1.0.1/v1.1.0-dev.1,
  Kubeflow Distribution 26.03, Trainer v2.2, and SDK v0.4.0. The fixed official source
  list, all forty-eight `20+` Full Source Reviews, and the one low-score verification
  are complete. W12 Discovery and Evidence Gates pass; Vera Rubin and Trainer v2.2 are
  provisional refinement candidates; vLLM incremental MoE expert offloading is also a
  Ch50 Experimental refinement candidate, owned by the 2026-03-16 open PR rather than
  the 2026-03-26 architecture RFC. DSX Air remains a product fact, and Dynamo plus
  the Kubeflow distribution/SDK entries are chapter-level `No Change`.
  On 2026-08-14, W12 then completed its independent weekly Books Gate: 23 Integrate,
  11 Refine, 11 No Change, 3 Weekly Only including the low-score boundary, and
  1 Emerging across 17 Stable Node owners. The owner prose was reverse-checked by
  mechanism rather than paper title, and preserves previous-design coexistence,
  evidence limits, state ownership and new failure modes. W12 Source-Family Books
  Gate is complete; the broader Historical Archive Gate remains open, and the active
  Books cursor advances to W13.
- W13 has completed its item-by-item Source-Family Books Gate. All 45 scored
  candidates now have final dispositions: 10 Integrate, 23 Refine, 6 No Change,
  2 Disputed and 4 low-score/cross-week Weekly Only; all 41 scored `20+` families
  retain non-template Full Source Reviews. Eighteen Stable Node owners were changed
  or revalidated, including parameter-vs-execution depth, mixture-dependent SFT
  stopping, typed RL credit, differentiable collective semantics, verified kernel
  admission, participant-local collective failure snapshots, workflow object identity,
  derived Memory/Skill compilation and Multi-Agent risk/commitment contracts.
  ClawKeeper remains one explicit unscored `Unverified / Blocked / No Books Change`
  source; it keeps the Archive Completion Gate open but does not reopen W13 Books.
  The active Books cursor advances to W14.

  **W13 supersession boundary (2026-08-14):** the detailed W13 paragraphs below are
  retained as chronological Source Review checkpoints. Their older candidate counts,
  `Books pending`, `Evidence Gate Open`, and `Historical Books Gate closed` statements
  do not describe the current W13 Books state and are superseded by the 45/45 disposition
  above. They still document why the broader Archive Completion Gate remains open.

- W14 has completed its independent Source-Family Books Gate. All 27 scored families
  have final dispositions: 5 Integrate, 18 Refine, 3 No Change and 1 low-score Weekly
  Only; all 26 scored `20+` families retain complete Source Reviews. Fifteen Stable Node
  owners were changed, including multimodal plan/generate/validate/retry, hierarchical
  Prefill indexing, population-based kernel admission, evaluator sampling and evidence
  planes, cumulative Agent harm, interface granularity, reversible/derived Memory,
  learned Reflection policy, RL scaffold/credit lifecycle, model-defined KV sharing,
  CPU-authoritative training state and target-profiled Skill compilation. Medical AI
  Scientist, GEMS and HippoCamp remain chapter-specific No Change decisions. Backdoor
  Attacks and Cactus remain two unscored `Unverified / Blocked / No Books Change`
  identities; they keep the Archive Completion Gate open without reopening W14 Books.
  The active Books cursor advances to W15.

  **W14 supersession boundary (2026-08-14):** the detailed W14 paragraphs below remain
  chronological Source Review checkpoints. Their older `pending`, `provisional`,
  `Blocked — Not Started`, and `Historical Books Gate closed` statements are superseded
  by the 27/27 final disposition above.

- W15 has completed its independent Source-Family Books Gate. All 31 scored families
  have final dispositions: 21 Refine, 3 No Change, 1 Emerging, 1 scored Unverified/
  Blocked and 5 low-score or pre-release Weekly Only. The 25 accessible scored `20+`
  families retain complete Source Reviews. Thirteen Stable Node owners were changed,
  covering conditional attention/context anchors, semantic KV policy, typed data lineage,
  PPO/GRPO baseline and precision boundaries, mutable generation, multi-token proposal,
  runtime ownership, trajectory cost, Skill/proactivity evaluation, residual-risk and
  instruction provenance, and Memory/Skill retrieval. GameWorld remains `Unverified /
  Blocked / No Books Change`; Seeduplex remains Emerging and does not enter mechanism
  prose. The Archive Completion Gate remains open; the active Books cursor advances to W16.

  **W15 supersession boundary (2026-08-14):** older W15 `pending`, `provisional`,
  `Blocked — Not Started`, and `Historical Books Gate closed` paragraphs are retained as
  chronological Source Review checkpoints and superseded by the 31/31 final disposition.

- W13 has been reopened from three baseline rows to thirty-five scored candidate
  families. All thirty-one candidates scoring at least twenty now have non-template Full
  Source Reviews. DSPA covers the dual-SAE conditional map, token-active intervention,
  theory, evaluation, and limitations; DRTriton covers v1/v2, CSP-DAG, verifier, curriculum
  DRPO, compositional search, hardware/overhead, and revision boundaries. The vLLM
  `TRITON_MLA_SPARSE` packet traces portability through build/link guards, capability-aware
  dispatch, Triton indexer and attention kernels, and graph metadata, while preserving its
  open-PR and narrow A100 benchmark boundary. Cross-Context
  Verification remains a low-score boundary because its public claim is tied to nine
  SWE-bench problems and one model; the Astrolabe code release remains a cross-week
  artifact follow-up to the W12 paper. W13 remains `Evidence Gate Open` only because
  discovery recall is not closed; the Historical Books Gate remains closed. W14 discovery has been
  reopened without waiting for a separate per-week instruction.
  A 2026-08-12 reconciliation of W14's curation-lag ledger then recovered twenty additional
  W13 in-window candidates. `Lie to Me` is now a 25/30 Full Source Review and chapter-level
  `No Change`: its classifier-dependent faithfulness evidence is already owned by Ch62's scorer
  contract and Ch68's policy-bound sensor boundary. MedOpenClaw is now a 29/30 provisional
  Ch62 refinement: its full-study workflow separates answer, spatial evidence, persistent viewer
  state and derived artifacts, while the publicly linked code repository currently exposes the
  static project site rather than a verified runtime implementation. Composer 2 is now a 29/30 provisional
  Ch29 refinement based on versioned vendor evidence: the packet treats token-span weight revision,
  MoE router path, logprob, sandbox snapshot and verifier version as parts of asynchronous trajectory
  identity, while keeping private CursorBench scores outside the general systems argument. ClawKeeper is
  an unscored `Unverified / Blocked Backlog` after abstract, HTML, search, export API and visual browser
  access all failed; no mechanism or chapter owner is inferred from its name. Hybrid Memory / HyDRA is a
  26/30 provisional Ch10 refinement: it separates static-view reconstruction from dynamic subject-state
  continuation and uses compressed spatiotemporal tokens plus query-conditioned top-k retrieval, while its
  synthetic dataset, author-owned DSC pipeline and partial training artifact keep it Experimental. Trace2Skill is now a
  27/30 provisional Ch80 refinement after full v1, experiment/ablation/limitations, later revision, official spreadsheet
  artifact and Ch73/76/77/80 adjacency review. Its frozen-base patch proposal and hierarchical consolidation make
  trajectory-derived Skill a versionable compilation artifact, but do not replace sequential edits, retrieval memory or
  human authoring. Work-in-progress status, partial artifact, same-model correlated errors, validation selection and missing
  patch/section attribution remain explicit. Natural-Language Agent Harnesses is now a 28/30 provisional Ch77
  refinement after full v1, RQ1-RQ3, module/migration ablations, limitations, appendices, v2 revision, post-window
  LinguaClaw artifact and Ch77/78/80/62 adjacency review. It externalizes only the harness pattern layer; deterministic
  code keeps enforcement ownership. Single-seed subsets, runtime contamination, prompt confounds and substrate drift
  prevent the OSWorld score from becoming a natural-language-over-code claim. Density-aware Soft Context Compression is
  now a 26/30 provisional Ch22 refinement after the sole v1, formulas, training/evaluation contract, official code/data/
  LoRA artifacts and Ch22/71/41 adjacency were reviewed. It separates a continuous density estimate from finite executable
  ratio buckets; summary-length proxy, short inputs, substring scoring, missing hardware/SLO/variance and correlation-only
  evidence keep it Experimental, while artifact availability is not independent reproduction. Learning to Commit is now a
  25/30 provisional Ch73 refinement after the sole v1, dataset construction, all four
  experiment settings, metrics/analysis/future work and Ch73/80/62 adjacency were reviewed. It separates repository
  snapshot, blind attempt, accepted oracle diff and derived procedural Skill, but the internal single-repository 24/7-
  commit pilot, synthetic issues, unavailable artifact/variance/cost and judge/maintainer gap keep it Experimental.
  TAPS is now a 29/30 provisional Ch44 refinement after the sole-v1 21-page PDF, all five RQs, formulas/setup/
  results, merged-tree lossless proof, depth/entropy appendices, official code/weights/datasets and Ch44/42/41/
  45/55 adjacency were reviewed. It extends draft identity with training distribution and runtime specialist
  composition; acceptance length is not end-to-end speedup, and dual-draft plus larger-tree costs keep it
  Experimental. DataFlex is now a 28/30 provisional Ch23 refinement after the sole-v1 paper,
  three dynamic data-action abstractions, distributed implementation, all experiments/efficiency
  appendices, official code/docs/datasets and Ch22-24/35/56/62 adjacency were reviewed. It turns
  selection, mixture and sample weighting into stateful control-plane actions, but its multi-GPU
  headline is not a matched-resource scale-up result; the 2025-12-23 project origin, 2026-03-17
  ZeRO-3 support and 2026-03-27 paper node remain separate Source Family events. Ask or Assume is now a
  28/30 provisional Ch77 refinement after its v1/v2 papers,
  five settings, question/difficulty/cost appendices, official code/evaluation paths and Ch75/77/78/62
  adjacency were audited. It makes clarification a per-turn workflow gate, while the v2 Kimi over-query
  result shows that calibration depends on backbone and tool semantics; simulated-user resolve rate is not
  treated as real-human collaboration evidence. XpertBench is now a 25/30 `No Change` Ch62 case after its
  v1/v4 papers, expert task/rubric pipeline, ShotJudge, Gold-subset results, appendices, platform/empty-
  dataset boundary and Ch61-63 adjacency were audited. Its April-prefixed arXiv ID does not override the
  2026-03-27 submission timestamp, and 52% CDR is not human-equivalent judge evidence. EpochX is now a
  23/30 `No Change` Ch80 case after its sole-v1 architecture, equations, three cases, official product/live-
  platform boundary and Ch77-80/55 adjacency were audited. Its task/delegation/asset/settlement model is
  already covered at the platform-contract level, while implementation, transaction traces, longitudinal
  incentive evidence, fraud/dispute handling and programmable verification are not public. The remaining six are explicit
  `Audit Pending` rows. The earlier
  26 scored / 22 reviewed numbers therefore describe only the
  previous recorded set, not the complete ISO week. Three
  other names in that ledger—Sommelier, SEAR, and FIPO—carry provisional 2026-03-20 dates and
  are routed to W12 backlog rather than counted in W13. W13 now has 40 scored, 5 unscored pending and
  1 blocked candidate; all 36 scored `20+` rows have Full Source Reviews, while its Discovery and Evidence
  Gates remain open and Historical Books Gate closed.
  `Emergent Social Intelligence Risks` subsequently adds a 27/30 provisional Ch78 refinement after its v1
  formal lifecycle, all fifteen risk scenarios, experiments/appendices, v2 revision boundary and Ch78/62/68
  adjacency were reviewed. It turns local utility, information partition, communication topology, aggregation,
  resource rules and adaptive governance into one collective-risk contract, but heterogeneous backbones/trial
  counts/judges, missing unified sampling/variance, no deployment control, no standalone limitations section and
  no public artifact keep it Experimental. W13 therefore advances to 41 scored, 4 unscored pending and 1 blocked;
  all 37 scored `20+` rows have Full Source Reviews. Historical Books Gate remains closed.
  PRBench then adds a 27/30 `No Change` Ch62 case after its sole-v1 paper, thirty-task curation/evaluation
  contract, experiments/failure analysis, all appendices, official project, partial public harness and Ch62/61/63
  adjacency were reviewed. It demonstrates the gap from paper understanding to executable numerical reproduction,
  but Ch62 already owns artifact/environment/trace, hidden verifier, rubric and hard-gate boundaries. Only one full
  benchmark sample is public and the complete judge/sampling/cost/run contract is not, so it remains Experimental /
  Artifact Partially Available. W13 is now 42 scored, 3 unscored pending and 1 blocked, with 38/38 scored `20+`
  Full Source Reviews. Historical Books Gate remains closed.
  MuSEAgent then adds a 28/30 provisional Ch73 refinement after its sole-v1 paper, transition/hindsight/multi-view
  retrieval mechanism, all experiments and ablations, tool/prompt appendices, official repository and Ch73/76/72/74/62
  adjacency were reviewed. It refines whole-trajectory retrieval into state-level derived procedural memory without
  replacing raw trajectory provenance, replay or cross-step causal context. Four multiple-choice VQA tasks, a fixed
  1:1 split, undisclosed hardware/latency/cost/multi-seed variance and a GPT-4o hindsight model that owns both admission
  and guidance keep it Experimental / Artifact Available. W13 is now 43 scored, 2 unscored pending and 1 blocked,
  with 39/39 scored `20+` Full Source Reviews. Historical Books Gate remains closed.
  KAT-Coder-V2 then adds a 29/30 provisional Ch29 new-mechanism candidate after its sole-v1 report, KwaiEnv,
  five-domain data/SFT/RL pipeline, turn-level objective, MCLA, KRL/Tree Training, on-policy distillation, all
  evaluation tables and Ch28-30/36/56/77/62 adjacency were reviewed. It makes environment/tool/scaffold/task/verifier
  the Agent-RL workload identity and separates specialization, student-on-policy fusion, credit granularity, MoE
  estimator control and tree-trajectory compute. Undisclosed model architecture, training hardware/precision,
  critical ablations, seeds/variance and KwaiEnv/KRL implementation keep it Experimental / Implementation Not
  Disclosed. W13 is now 44 scored, 1 unscored pending and 1 blocked, with 40/40 scored `20+` Full Source Reviews.
  Historical Books Gate remains closed.
  LongCat-Next then adds a 29/30 provisional Ch11 new-mechanism candidate after its sole-v1 paper, DiNA/dNaViT,
  vision/audio hierarchical RVQ, unified autoregressive MoE backbone, training stages, all main evaluations and
  methodology analyses, multimodal RL, VHalf/mismatch/quantization appendices, official repository/model card and
  Ch11/12/21/29/34 adjacency were reviewed. It makes tokenizer/codebook a versioned multimodal input/output protocol
  while keeping continuous feature projection and specialized modality systems as valid alternatives. Undisclosed
  training hardware/topology/cost/variance, an incomplete VHalf workload contract and unavailable full pretraining
  pipeline keep it Experimental / Artifact Partially Reproducible. W13 is now 45 scored, 0 current-review pending
  and 1 blocked, with 41/41 scored `20+` Full Source Reviews. Its Forward Candidate Evidence Gate has passed and
  the forward cursor moves to W14; the broader Historical Evidence Gate and Historical Books Gate remain closed.

- W14 through W16 have now been reopened as continuous checkpoints. W14 has expanded
  from two baseline rows to twenty-three independently scored families: twenty-one recovered
  candidates are assigned by arXiv v1 / first-public date, including later curation-feed
  recovery, while twenty-three discovery-feed spillbacks are explicitly moved to earlier
  owner weeks. The two baseline reviews plus HISA and Kernel-Smith make four of twenty-three
  Full Source Reviews; nineteen remain `Audit Pending`. HISA's v1/v3 method, formulas,
  experiments, appendix, artifact, adjacent chapters, and revision drift have been audited;
  it is provisionally a Ch39 refinement with a short Ch22 handoff. Kernel-Smith's full method,
  training/evaluation contract, repository boundary and merged SGLang/LMDeploy pull requests
  have also been audited; it is provisionally a Ch45 refinement with Ch52/77 handoffs, and
  its isolated-kernel results are explicitly separated from end-to-end serving evidence.
  Marco DeepResearch now makes five of twenty-three Full Source Reviews, leaving eighteen
  pending. Its paper, public inference artifact and Ch72/74-78/62 neighborhood were audited;
  verification is separated across QA construction, trajectory synthesis and test-time search,
  while same-model judging, the 600-call budget and mixed-source baselines remain explicit
  evidence limits. It is provisionally a Ch76 refinement with Ch72/77 handoffs. No Books edit
  is authorized while the Gate is closed. Combee then raises W14 to six of twenty-three Full
  Source Reviews, with seventeen pending. Its full paper, appendices, ACE/GEPA artifact boundary
  and Ch72-74/77-78 neighborhood were audited; bounded fan-in, redundant exposure and synchronous
  context-version ownership are separated from the paper's non-equivalent gradient-aggregation
  analogy. It is provisionally a Ch73 refinement with Ch77/78 handoffs. Stochastic KV Routing then
  raises W14 to seven of twenty-three Full Source Reviews, with sixteen pending. Its nineteen-page
  paper, appendices, Apple Research entry and Ch18-22/39-41 neighborhood were audited; depth-wise
  cache sharing is recorded as a checkpoint-semantics, deployment-mapping and runtime-layout
  co-design, not as post-hoc eviction for arbitrary models. It is provisionally a Ch19 refinement
  with Ch40/41 handoffs, while the missing artifact, GPU/backend, variance and SLO contract remain
  explicit evidence limits. MiroEval then raises W14 to eight of twenty-three Full Source Reviews,
  with fifteen pending. Its full paper, robustness/human-study appendices, public evaluator repository
  and Ch62/63 neighborhood were audited; report synthesis, claim factuality, process intrinsic quality
  and process-to-report provenance are recorded as separate evidence planes. It is provisionally a
  Ch62 refinement with a Ch63 handoff, while trace availability, judge calibration, live-web drift and
  unmatched tool budgets remain explicit evidence limits. AgentHazard then raises W14 to nine of
  twenty-three Full Source Reviews, with fourteen pending. Its full paper, taxonomy/results/prompt
  appendices, public dataset/code/trajectories and Ch62/68/69/77 neighborhood were audited;
  locally plausible action accumulation, framework-as-subject and trajectory-level harm are provisionally
  a Ch68 refinement with Ch62/77 handoffs. The single judge, absent benign calibration, absent executable
  side-effect verifier and untagged artifact remain explicit evidence limits. LightThinker++ then raises W14
  to ten of twenty-three Full Source Reviews, with thirteen pending. Its full paper, formulas, general/agentic
  experiments, appendices, public implementation guides and Ch22/41/71-74/77 neighborhood were audited;
  fixed irreversible compression evolves into a reversible raw/summary visibility-state projection. It is
  provisionally a Ch73 refinement with Ch71/22/41/77 handoffs, while synthetic trajectories, model judging,
  unmatched proprietary baselines, the untagged artifact and undisclosed inference hardware/SLO remain
  explicit evidence limits. SKILL0 then raises W14 to eleven of twenty-three Full Source Reviews, with
  twelve pending. Its v1 paper, theoretical and experimental appendices, v2 revision boundary, author
  repository, ALFWorld/Search-QA recipes and Ch28-30/71/80 neighborhood were audited. Runtime Skills are
  treated as training scaffolds that can be filtered, ranked and annealed to zero for stable procedural
  priors—not as obsolete registries. The coupled GRPO, visual rendering, compression reward and curriculum,
  noisy helpfulness estimate, non-causal internalization claim and untagged evolving repository remain
  explicit limits. It is provisionally a Ch29 refinement with Ch80/71 handoffs; the Historical Books Gate
  remains closed. GrandCode then raises W14 to twelve of twenty-three Full Source Reviews, with eleven
  pending. Its v1 report, formulas and appendices, v2/v3 revision boundary, official project/report/
  contest-submission artifacts and Ch28-30/75-78 neighborhood were audited. Stage-immediate reward,
  final-difference correction, token-level behavior-policy identity and staleness are recorded as one
  training-state lifecycle; independent normalization, dropped stale corrections, absent algorithm ablation,
  absent training code and incomplete compute contract prevent causal attribution. It is provisionally a
  Ch29 Experimental refinement with Ch77/78 handoffs; no Books edit or contest-headline claim is authorized.
  Self-Distilled RLVR then raises W14 to thirteen of twenty-three Full Source Reviews, leaving ten pending.
  Its v1 paper, all theoretical appendices, v2 revision, current author implementation/configs and Ch28-30
  neighborhood were audited. The durable mechanism is a separation between verifier-owned sign and
  privileged-teacher magnitude; the paper's zero-leakage result does not establish zero effect on parameter
  trajectory, and its Bayesian interpretation is assumption-bound. Missing component ablations, unmatched
  extra-forward cost, the lambda/objective specification ambiguity and the lack of an event-bound release
  remain explicit limits. It is provisionally a Ch29 Experimental refinement with a Ch28 handoff; no Books
  edit is authorized while the Historical Books Gate is closed.
  Towards a Medical AI Scientist then raises W14 to fourteen of twenty-three Full Source Reviews, leaving
  nine pending. Its thirty-page paper, sole v1, official project/case pages and Ch62/69/77/78 neighborhood
  were audited. The domain evidence-to-code-to-run-to-manuscript workflow and graded autonomy are retained,
  but the public code/data links remain coming-soon/404; random data subsampling, unmatched GPT-5 workflow
  budgets, judge calibration and a single-task manuscript study bound the claims. Ch62/69/77/78 already
  cover claim provenance, executable-not-ground-truth, approval, durable state and correlated roles, so the
  provisional decision is `No Change — Already Covered`; no benchmark headline or Books edit is authorized.
  GEMS then raises W14 to fifteen of twenty-three Full Source Reviews, leaving eight pending. Its sole v1,
  full experiments and appendices, project page, current core implementation and Ch73/76/77/78/80
  neighborhood were audited. Criterion-wise refinement, raw attempts plus compressed experiences and
  manifest-to-on-demand Skills are retained as a case, but same-family MLLM roles, string-parsed yes/no
  verdicts, equal-weight best selection, in-process memory and ungoverned prompt Skills bound the claims.
  Ch73/76/80 already own the durable contracts, so the provisional decision is `No Change — Already
  Covered`; no model-ranking claim or Books edit is authorized while the Historical Books Gate is closed.
  Terminal Agents then raises W14 to sixteen of twenty-three Full Source Reviews, leaving seven pending.
  Its v1/v2, August v3 additions on granularity, open-weight models, limitations, reproducibility and safety,
  all appendices, and the Ch68/74/77/79/80 neighborhood were audited. The later generic API-call control
  locates most of the gap in narrow-catalog versus flexible-request granularity rather than the terminal or MCP
  protocol itself; filesystem/shell, typed domain tools and browser retain distinct scratch/batch/protocol,
  governance and UI-only-state branches. It is provisionally a Ch74 Experimental refinement with Ch68/79/80
  handoffs; model/cost headlines and Books edits remain unauthorized while the Historical Books Gate is closed.
  MemRerank then raises W14 to seventeen of twenty-three Full Source Reviews, leaving six pending. Its v1/v3
  papers, substantive revision drift, public dataset schema and Ch29/62/68/72-74 neighborhood were audited.
  Query-independent preference memory is recorded as a downstream-utility-trained derived materialized view,
  while same-reranker reward/evaluation, synthetic purchase/query labels, missing code/checkpoint/compute and
  absent consent/correction/delete lifecycle remain explicit limits. It is provisionally a Ch73 Experimental
  refinement with Ch29/62/68/72 handoffs; no headline metric or Books edit is authorized while the Gate is closed.
  ASI-Evolve then raises W14 to eighteen of twenty-three Full Source Reviews, leaving five pending. Its sole v1,
  circle-packing appendix, current public pipeline/database/cognition implementation, artifact/release coverage
  and Ch23/29/62/73/77 neighborhood were audited. Cognition cold-start priors and Analyzer-produced run-derived
  lessons are separated as two memory planes. Only circle packing provides three-run component ablations; the
  three expensive main tasks lack causal isolation, hardware/total-compute disclosure and replayable artifacts.
  It is provisionally a Ch77 Experimental refinement with Ch73/62 handoffs; SOTA counts, benchmark headlines and
  the repository's fully-open-sourced claim are not treated as main-experiment reproducibility evidence.
  Simple Self-Distillation then raises W14 to nineteen of twenty-three Full Source Reviews, leaving four pending,
  and its evidence-based score is corrected from 24 to 26. The v1 five-model paper, all theory and experiment
  appendices, v2 revision boundary, official generation/evaluation code, checkpoint cards and the Ch20/24-29/62
  neighborhood were audited. Non-unit-temperature plus truncated self targets are separated from plain on-policy
  self-training, then compiled into parameters by SFT before a separately chosen serving decode policy. GPT-OSS
  remains a v2 addition; the current repository's bottom-10-percent length filter and 1.5 example temperature do
  not reproduce the paper's minimal filter and every main configuration, and no Megatron training recipe,
  repeated-run confidence interval or independent tuning split is public. The provisional owner is Ch25, with
  Ch20/62 handoffs; wrong-code and pass-at-k headlines do not become general self-improvement claims.
  HippoCamp has then received a detailed official-artifact review without being counted as a Full Source Review.
  Its sole v1 has no arXiv HTML and the 24.5 MB primary PDF cannot be read through the current reader; the saved
  arXiv site-security preference also blocks the in-app-browser route and was not bypassed. The project page,
  author repository/history, official dataset schema and evaluation entrypoints establish the benchmark's raw
  snapshot, hidden hierarchical evidence, capability labels and QA/profile claim planes, but cannot verify the
  paper's complete Method, baseline parity, ablations, Limitations or appendix. It remains `Unverified / Blocked`,
  likely owned by Ch62 with Ch72/73/68 handoffs. W14 therefore remains nineteen of twenty-three Full Source
  Reviews, with one detailed blocked review and three pending candidates.
  Omni-SimpleMem then raises W14 to twenty of twenty-three Full Source Reviews, leaving one detailed blocked
  review and two pending candidates. Its v1/v2 paper, equations, five-backbone results, component ablations,
  efficiency contract, all appendices and prompt catalog, author repository, and v0.2.0 release were audited.
  Hot MAU metadata versus cold raw evidence, dense/sparse/graph candidate preservation, and token-budgeted
  progressive expansion are provisionally owned by Ch73 with Ch72/62/68/77 handoffs. Novelty filtering remains
  a destructive write gate, and current-main CLIP/relation-schema/MCP behavior is recorded as version drift.
  Because the largest measured gains came from response-format, timestamp, tokenization, and data-completeness
  repairs, the durable conclusion is to validate the harness and data pipeline before attributing the remaining
  delta to architecture. Naive-baseline headlines, hardware-free eight-worker throughput, and benchmark-specific
  prompts are excluded from Books. S0 Tuning then raises W14 to twenty-one of twenty-three Full Source Reviews,
  leaving one detailed blocked review and one pending candidate. Its v1/v2 paper, every appendix, repository and
  package, trained-state card, and dataset card were audited. Recurrent launch state is provisionally classified as
  a non-weight, non-prompt adaptation surface owned by Ch26 with Ch22/31/46 handoffs. Paper/model-card conflicts
  over the 24+8 versus 21+6 layer layout, A10G versus A100 training hardware, and exact base identity lower Source
  Reliability and the score from 24 to 23; checkpoint/layout and general performance claims remain excluded.
  Meta-TTL then raises W14 to twenty-two of twenty-three Full Source Reviews, leaving only HippoCamp's detailed
  blocked review. Its complete v1/v2 paper and appendices, v3 revision boundary, repository entrypoints, and
  Ch62/73/75-77 adjacency were audited. Fixed reflection rule evolves into an offline learned meta-policy plus a
  runtime-mutable actor prompt, provisionally owned by Ch76. Because v1 omits seeds, variance, hardware, token/API
  cost and current code has drifted in episode/model/selection surfaces, Source Reliability and the score fall from
  24 to 23; the Web OOD gain is also concentrated in a structurally related domain, so no general self-improvement
  claim or headline enters Books.
  MegaTrain then returns from W15 to W14 because the author release page publicly announced the framework on
  2026-04-05, one day before arXiv v1. Its sole v1, complete evaluation and appendices, author release, current
  repository, and Ch31-36 adjacency were audited, raising W14 to twenty-three of twenty-four Full Source Reviews;
  HippoCamp remains the only detailed blocked review. CPU-owned authoritative parameters/gradients/Adam state plus
  a per-layer transient GPU execution cache is provisionally a Ch35 offload refinement, with Ch32/34/31 handoffs.
  Conflicting checkpoint-ablation and 1K-context numbers, absent production SLO/recovery/cost contracts, and later
  repository drift prevent benchmark headlines or current RL/multi-GPU features from entering historical evidence.
  No Books edit is authorized while the Historical Gate remains closed.
  HippoCamp's official arXiv primary text became readable on 2026-08-11 and was then reviewed across complete
  construction, trajectory/evidence schema, Atomic Units, annotation/QC, experiments, evaluation regimes, metrics,
  analysis and appendices. This resolves W14's final source-access blocker and raises the recorded queue to 24/24
  Full Source Reviews with no pending or blocked candidate. Its disposition is `No Change — Already Covered /
  Experimental Evaluation Case`: Ch62, Ch72, Ch73 and Ch68 already own the durable evaluation, retrieval,
  memory-lifecycle and privacy boundaries. W14 fixed-source Discovery Gate remains Open and the all-history Books
  Gate remains Closed; no Books edit is authorized by this checkpoint.
  A later cross-week attribution check re-opened only the W14 discovery ledger, not the completed 24 source packets.
  W16 had named `Backdoor Attacks on Decentralised Post-Training` (March 31) and `Cactus` (April 5) as W14
  spillbacks without primary identifiers; neither metadata, authors, artifacts nor readable text could be located, so
  both are explicit unscored `Unverified / Blocked Backlog` entries and do not block the forward cursor. The W18
  GLM-5V-Turbo family also exposed an April 2 official product node. W14 records it as an 18/30 `Weekly Only —
  Version/Product Fact / Mechanism Not Disclosed` boundary, while the April 29 technical report and Ch34 mechanism
  remain owned by W18. W14 now has 25 scored rows (13 high, 11 medium, 1 low), 24/24 scored `20+` Full Source
  Reviews, one low-score boundary, two blocked identities and zero current-review pending. Its Forward Candidate
  Evidence Gate has passed and the cursor moves to W15; its fixed-source Discovery Gate and the all-history Books
  Gate remain closed.
  The 2026-08-12 fixed-source checkpoint then replayed accessible first-line model/research indexes and major
  AI-infrastructure release/repository pages. It recovered Amazon Science's April 1 LLM-based TTS engineering node,
  scored 24/30 and reviewed against Ch38-40 and Ch62/68. The durable candidate is a plan/validate/retry state machine:
  phoneme and duration plan, autoregressive acoustic generation, post-generation checks, and bounded regeneration or
  fallback. Because the official article exposes no paper, model/data card, code, immutable artifact, hardware,
  uncertainty, concurrency or tail-SLO contract, it remains `Refine — Existing Argument (Experimental; Official
  Engineering Evidence; Artifact Not Available)` under Ch38 and no vendor benchmark enters Books. Microsoft ADeLe,
  inference-energy and relevance-labeling April publication/communication nodes were deduplicated to 2025 or earlier
  primary source families rather than counted again. W14 now has 26 scored rows (13 high, 12 medium, 1 low), 25/25
  scored `20+` reviews, one low-score boundary, two blocked identities and zero ordinary pending. The official-Research
  checkpoint is reviewed; academic cross-index and remaining historical Infra release coverage keep Discovery open,
  and the all-history Books Gate remains closed.
  W15 has expanded from four baseline families to eighteen scored families;
  fourteen recovered candidates are assigned by first-public date and nine curation-lag
  entries return to W11/W13/W14. SPPO was surfaced by W16 curation but returned to W15 by its
  2026-04-10 v1 date. Seeduplex, TriAttention, Memory Intelligence Agent, SkillX, and Beyond Accuracy / PTE
  initially make five of sixteen retained Full Source Reviews. PTE's v1 paper, all appendices,
  v2/ACL publication boundary, current artifact, and Ch39-41/62-63/77 adjacency are audited. It provisionally
  refines Ch62 by replacing flat output-token counts with turn-aware Prefill/Decode state cost, but its
  single-node 8xH200 validation measures only model generation and excludes tool/network time. The cross-GPU
  analysis re-prices the same trajectories with datasheet peak FLOPS rather than rerunning them, while partial
  KV reuse, batching, scheduler behavior, actual utilization, and SLO remain outside the model; PTE therefore
  cannot replace observed trace-level SLIs. TriAttention's full method, formulas,
  experiments, appendices, artifact, and Ch19/22/40/41 adjacency have been audited; it
  is provisionally a Ch41 refinement with Ch22 handoff. W16 has expanded from three
  baseline families to forty-two scored families after moving Nemotron 3 Super to W10. W17 curation exposed six additional
  candidates whose arXiv v1 dates belong to W16: BEHEMOTH, AgentSPEX, OpenMobile,
  Scaling Test-Time Compute, SkillFlow, and EvoMaster. CodeTracer, BEHEMOTH, and the three baseline
  packets plus Sema Code, OccuBench, Agentic Aggregation, ClawGUI, Rethinking On-Policy Distillation, AiScientist,
  AgentSPEX, Exploration/Exploitation Errors, Dive into Claude Code, Memory Transfer Learning, DR3-Eval and
  Corpus2Skill, OpenMobile, Scaling Test-Time Compute, SkillFlow and EvoMaster, the second-pass academic set,
  Gemini Robotics-ER 1.6, SGLang Q2 roadmap, Megatron Core 0.17.0, NVIDIA Dynamo agentic inference,
  NemoClaw/OpenShell, and PEFT 0.19.0 make forty-two of forty-two Full Source Reviews. Three named
  below-threshold engineering items also have verified rejection records. OpenReview/TMLR/formal proceedings,
  weekend discovery, fixed institutional archives, and release/RFC/PR lists are closed under first-public-date
  and source-family deduplication; W16 Evidence Gate is Passed. Dynamo is provisionally a Ch48 refinement,
  PEFT 0.19.0 a Ch26 refinement, while roadmap/version/tutorial evidence remains Weekly-only, Emerging, or
  No Change as appropriate. The Historical Books Gate remains closed until all weeks pass. SkillFlow's sole v1, all appendices,
  project/repository/data artifacts and Ch62/73/77/80 adjacency were audited. Its family-local fixed-order protocol
  provides conditional evidence about skill repair and negative transfer, but does not test cross-family retrieval or
  forgetting; the primary report also conflicts internally between 47.41% and 51.04% for its history-context control.
  It is therefore corrected from 25 to 24 and provisionally classified `No Change — Already Covered` rather than
  promoted into Books. EvoMaster's v1 four-benchmark OpenClaw comparison, v4 ten-benchmark revision, all
  benchmark-specific setup/appendices, repository/tags and post-W16 run-level evolution guide were separately
  audited. Specialized-workflow confounding, absent component ablation/matched compute/seeds/CI and missing
  event-bound run artifacts reduce it from 25 to 23 and make it a Ch77/78/80 `No Change` case. AiScientist's repository release record corrects its
  event date from arXiv v1 04-14 to 04-13. Its full paper, PaperBench/MLE-Bench contracts, File-as-Bus ablation,
  current artifact and Ch76-78/80 adjacency were audited. The provisional Ch77 refinement treats a compact workspace
  map as a derived navigation view over authoritative state; files alone do not supply versioned transitions,
  conflict handling, provenance, replay or rollback. Practical Value and Longevity are rebalanced without changing
  the 26-point total, and no benchmark headline or generic production claim enters Books.
  AgentSPEX's sole v1, full eighteen-page paper, all appendices, seven-benchmark evaluation,
  twenty-three-person user study, formal-verification example, current six-commit repository and Ch76-80 adjacency
  were audited. Ch77 already owns the deterministic-spine and durable-state mechanism, so the disposition is
  `No Change`. Missing component ablations, repeated runs, workload/cost/SLO disclosure, exactly-once side-effect
  semantics and real verification evidence reduce the score from 26 to 23; YAML syntax is not a durable runtime.
  Exploration and Exploitation Errors' sole v1, full thirty-six-page paper, all appendices, formulas and edge cases,
  prompt/harness/semantic experiments, additional results, current eleven-commit artifact and Ch62/73-75/77
  adjacency were audited. It provisionally refines Ch62: the process metric avoids reading model policy but requires
  evaluator-owned full map/DAG state, productive targets and distances, so policy-agnostic is not environment-agnostic.
  Its trajectory-conditioned opportunity denominator makes it complementary to final outcome rather than a general
  model ranking; three seeds, symbolic grids and a bundled harness ablation block broad extrapolation.
  Dive into Claude Code's v1 forty-six-page paper, v2 revision drift, companion repository, current official
  documentation, and Ch68/73/74/77-80 adjacency were audited. It is an independent reverse-engineering snapshot
  of the public v2.1.88 package, not an Anthropic architecture statement or production-path measurement. The
  reactive loop, graduated compaction, deny-first authorization, append-oriented persistence, isolated delegation
  and extension boundaries are already owned by the adjacent chapters; without benchmarks, ablations, failure
  injection, cost/SLO or user-study evidence, the disposition is Ch80 `No Change` and no Books text is duplicated.
  Memory Transfer Learning's sole v1, all tables and appendices, negative-transfer cases, formal abstraction
  assumptions, project page, seven-commit placeholder repository and Ch72-74/77/80 adjacency were audited. It
  provisionally refines Ch73: cross-domain procedural memory must trade specificity benefit against mismatch risk,
  with source/target model, language/tool/environment and evaluator compatibility checked at adoption. The public
  code remains `Coming Soon`, and seeds/uncertainty, cost/SLO and contamination audit are undisclosed; its score is
  therefore corrected from 25 to 24, and no historical Books text is written while the gate is closed.
  DR3-Eval's sole v1, appendices, DR3-Agent control flow, corpus/retrieval/framework ablations, live-web comparison,
  judge validation, current code/data and Ch61-63/72/77 adjacency were also audited. It provisionally refines Ch62:
  a Deep Research evaluation environment must identify user files, frozen source snapshots, support/noise taxonomy
  and corpus budget, while static/live calibration must compare components and slices rather than an aggregate whose
  opposing changes can cancel. The public dataset card does not explicitly expose the paper's static sandbox corpus,
  and the main text's fifty-report/four-expert human check conflicts with Appendix D's thirty-report/two-expert
  protocol. Source Reliability is therefore corrected from 4 to 3 and the total from 25 to 24; reproducibility and
  human-alignment claims remain bounded rather than promoted to Books.
  Don't Retrieve, Navigate / Corpus2Skill's v1 full paper, Appendices A-I, navigation traces, v2/v3 scope and
  metric/cost revisions, current seven-commit WIP artifact, and Ch71-73/80 adjacency were audited. It provisionally
  refines Ch72: an Agent-visible hierarchy is a versioned derived index over authoritative sources, and its value
  depends on a recoverable topical taxonomy rather than replacing retrieval. The later HAGRID/TatQA/CUAD losses
  preserve flat retrieval for open-domain, homogeneous-table and extractive corpora. Hard versus multi-parent routing,
  map/source identity, ACL/delete propagation, incremental rebuild and route traces become explicit state. The
  event-time single-corpus study, correlated judge, missing uncertainty/production SLO and WIP artifact reduce
  Technical Novelty from 5 to 4, Source Reliability from 4 to 3, and the total from 26 to 24.
  OpenMobile's sole v1, appendices, environment-memory/task-synthesis/policy-switching flow, current code/data/model
  artifacts and Ch23/25/62/77/80 adjacency were audited. It provisionally refines Ch25 by treating
  learner-reachable error and recovery states as part of the demonstration contract rather than assuming successful
  expert paths cover deployment states. Annotation, filtering, monitoring, expert continuation and reasoning rewrite
  share one Gemini family, while event-time model identity, hardware, cost/SLO, full contamination, real-device and
  safe-reset evidence are undisclosed. Source Reliability and Longevity each fall by one point, correcting 25 to 24;
  AndroidWorld-suite evidence is not promoted to generic mobile-Agent capability.
  Scaling Test-Time Compute for Agentic Coding's sole v1, Appendices A-H, RTV/PDR formulas, full 500-task
  SWE-Bench Verified and 88-task Terminal-Bench v2.0 contracts, five-model results, ablations and
  Ch62/75/77/78/80 adjacency were audited. It provisionally refines Ch78: a bounded trajectory representation is
  the shared interface for parallel selection and sequential reuse, but generator, summarizer and judge share model
  lineage. The main study lacks a total-compute-matched baseline, public artifact, cost/latency/SLO and seed evidence;
  higher average pass@1 coexists with lower pass@16 and more 0/16 tasks after refinement, exposing bad-context
  amplification. TN/PV/SR fall and Longevity rises, correcting the total from 27 to 25.
  OccuBench's two paper revisions, public dataset/reimplementation, simulator/fault/verifier paths, and
  Ch61-63/68/77 adjacency are audited. It provisionally refines Ch62 by making simulator fidelity and
  cross-simulator disagreement part of the evaluation contract; the proprietary event-time harness,
  missing domain-expert/real-environment calibration, and ranking sensitivity prevent synthetic
  occupational scores from being treated as professional fitness or production reliability. Agentic
  Aggregation's 33-page paper, all appendices, public rollouts/code, and Ch62/76-79 adjacency are audited.
  It provisionally refines Ch78 by externalizing immutable trajectories as a read-only evidence environment
  and separating synthesis from selection. Its score is corrected from 26 to 25: uncompressed storage is
  not full evidence coverage under keyword retrieval and a finite context, while modified model-judge prompts,
  K<=8, and absent adversarial/side-effect/runtime tests block generic scaling or production claims.
  ClawGUI's sole v1, RL/Eval/Agent modules, current repository, and Ch27-30/62/68/73-80 adjacency are audited.
  Its score is corrected from 26 to 24. It provisionally refines Ch29 by treating environment generation,
  reset, health, lease, spare-server failover, and verifier semantics as rollout-state contracts. The
  GiGPO+dense comparison changes both algorithm and reward, the reproduction metric is an asymmetric
  tolerance hit rate, and seeds/variance, PRM calibration, large-scale real-device evidence, security,
  privacy, and hybrid CLI/GUI ablations are absent; production-ready and generic reproducibility claims
  are therefore excluded. Rethinking On-Policy Distillation's sole v1, all appendices, OPD/verl/LLaMA-Factory
  artifacts, and Ch24-26/29 adjacency are audited. Its score is corrected from 27 to 25 and it provisionally
  refines Ch25 by separating global teacher quality from local exploitability on student-visited states:
  support compatibility, genuinely new teacher capability, trajectory-depth drift, and cold-start entropy/
  coverage are training-contract gates. All evidence is confined to small math/model-family pairs, the
  gradient-anisotropy explanation is explicitly unverified, and no seeds/CI, matched compute, tokenizer/
  architecture sweep, non-math domain, or production evidence exists; the reported overlap mass, length
  sweet spot, and sampled-token sufficiency are therefore not generalized. Sema Code's
  full paper, two client artifacts, current package/API surface, and Ch74/77-80 adjacency are audited.
  Its score is corrected from 26 to 23 because functional deployment cases do not provide stress,
  ablation, security, crash-recovery, or horizontal-scale evidence, and no event-bound immutable code
  release is available. Ch80 already owns the durable engine/platform boundary, so this candidate is
  `No Change`; production-ready, strict-isolation, and zero-residue claims are not adopted. CodeTracer's complete
  paper, appendices, evaluation and ablation contract, artifact entry point, and
  Ch62/64/65/77/80 adjacency have been audited. It is provisionally a Ch80 refinement,
  while its separate diagnosis-pass cost prevents replay gains from being treated as
  total-compute-matched production evidence. BEHEMOTH's sole v1, all appendices, CluE
  repository, and Ch72-74 adjacency are also audited. It provisionally refines Ch73 by
  treating the extraction policy itself as a versioned derived artifact: cluster-local
  analysis reduces heterogeneous-feedback dilution but does not establish an end-to-end
  memory lifecycle, independent evaluator evidence, long-term drift safety, or production
  SLO. W16 recall remains open. The former claims
  that no other paper or stable release existed have been
  downgraded to coverage limitations until the fixed official, academic, and Infra
  source lists are rescanned. All three weeks remain `Evidence Gate Open`, and the
  historical sequence continues without per-week prompting.
  MIA's v1-v3 in-window paper, v4 revision boundary, all appendices, repository/model/dataset
  artifacts, and Ch29/31/62/72-77 adjacency are now audited. It is provisionally owned by
  Ch73: the durable mechanism is a dual plane of versioned external procedural memory and
  mutable Planner parameters, while the paper does not establish reversible conversion,
  per-memory deletion from weights, atomic model-version swaps, rollback, independent judge
  evidence, or production SLO. Its Source Reliability and score therefore fall from 25 to 24;
  no Books edit is authorized while the Historical Gate remains closed.
  SkillX's v1 full paper and appendices, v2 revision boundary, current repository/SkillKB, and
  Ch73-75/77/80 adjacency are audited. The durable mechanism is multi-granularity procedural
  representation plus query-to-pseudo-plan-to-step retrieval, not a universal fixed three-level
  taxonomy. The paper itself reports per-model skill-composition regressions and third-iteration
  overfitting, while hardware, full cost, uncertainty, provenance, versioning, rollback, and delete
  semantics are missing; Source Reliability and total score fall from 25 to 24. It is provisionally
  a Ch73 refinement with Ch74/75/80 handoffs, and Historical Books Gate remains closed.
  Agentic Skills in the Wild leaves W15 at six of fifteen retained Full Source Reviews, with nine pending.
  Its sole v1, all appendices, author code/data, one-commit/no-release boundary, and Ch62/73-75/77/80 adjacency
  are audited. The durable contribution is a progressive Skill evaluation ladder that separately exposes
  selection, retrieval, adaptation, and task-local refinement failures. Three repeats, pair-level model/harness
  confounding, unequal benchmark timeouts, undisclosed local-serving hardware and total cost, and observed
  refinement regressions prevent model rankings or a universal “skills help” claim. It is provisionally a Ch62
  refinement; Historical Books Gate remains closed.
  MARS then raises W15 to seven of fifteen retained Full Source Reviews, with eight pending. Its sole v1, all
  appendices, author repository, benchmark entrypoints, and Ch40/41/44/48/52 adjacency are audited. It is
  provisionally a Ch44 refinement: a same-backbone masked-proposal branch keeps causal attention, right-shifted
  logits and left-to-right commit, while clean AR loss protects one-token competence. It is not exact speculative
  sampling: confidence-gated commits change the output policy, training roughly doubles H200-hours, and block-level
  KV caching introduces batch-barrier idle. The reported peak wall-clock speedup lacks a complete inference
  hardware/runtime/SLO contract and therefore does not enter Books; Historical Books Gate remains closed.
  FP4 Explore, BF16 Train / Sol-RL then raises W15 to eight of fifteen retained Full Source Reviews, with seven
  pending. Its sole v1, theory and appendices, NVIDIA project, current Sana recipes/docs, and Ch28-32/35 adjacency
  are audited. The durable mechanism is precision-separated state: NVFP4 deterministic previews rank seeds, while
  selected seeds are regenerated by the BF16 policy before they become objective-bearing training artifacts. The
  reported peak convergence speedup is not iteration throughput; the measured iteration gain is bounded to the
  authors' single-node B200 setup. Bounded-error, Lipschitz, i.i.d.-Gaussian assumptions, missing uncertainty and
  immutable artifact identity, and the lack of deterministic replay in LLM/Agent trajectories keep this an
  Experimental Ch29 refinement with Ch31/32/35 handoffs. Historical Books Gate remains closed.
  Flux Attention then raises W15 to nine of fifteen retained Full Source Reviews, with six pending. Its sole v1,
  all appendices, author repository and training paths, sparse-kernel dependency, nano-vLLM integration tree, and
  Ch22/39-42/52 adjacency are audited. The durable mechanism is a context-conditioned layer hard route that trades
  head-level budget flexibility for regular execution and whole-layer KV-traffic bypass. The authors' 256K Prefill
  result is end-to-end, while Decode is only single-A800, BF16, batch-one kernel latency; neither establishes
  continuous-batching goodput, TTFT/TPOT tails, TP scaling, route/KV identity, or safe cache sharing. It is
  provisionally an Experimental Ch22 refinement with Ch39-41/52 handoffs. Historical Books Gate remains closed.
  SkillClaw then raises W15 to ten of fifteen retained Full Source Reviews, leaving five pending. Its sole v1,
  complete twenty-four-page paper and appendices, current client/evolve/validation repository paths, no-release
  boundary, later-feature drift, and Ch62/68/73-75/77/79-80 adjacency are audited. The durable evolution is
  user-local/manual Skill to session evidence aggregation, candidate synthesis, same-environment validation and
  controlled shared release. Four-of-six displayed task categories, one Qwen3-Max serving as executor/evolver/
  validator, and missing independent judge, held-out isolation, uncertainty, privacy/consent, tenant/poisoning,
  revoke/rollback and immutable event-time artifact reduce Source Reliability and score from 25 to 24. Ch80 already
  owns Skill identity, provenance, evaluation/policy/revocation, canary, in-flight pinning, rollback and the boundary
  against direct global-memory writes, so the provisional disposition is `No Change — Already Covered`; no Books
  edit is manufactured while the Historical Gate remains closed.
  DMax then raises W15 to eleven of fifteen retained Full Source Reviews, leaving four pending. Its v1 full text,
  equations, Algorithm 1, experiments and ablations, v2/v3 revision boundary, author repository, Math/Coder
  model and data artifacts, no-release state, and Ch29/40-44/48/52 adjacency are audited. The durable mechanism
  evolves one-way mask-to-token commit into on-policy correction of self-generated errors, confidence-carrying
  hybrid embeddings and explicit block convergence/commit; applying soft decoding to the untrained base model
  collapses, so this is not a runtime-only optimization. Evidence is limited to LLaDA-2.0-mini, math/code
  self-distillation, 8xH200 training, 2xH200 TP, batch one and 2048-token generation, with no uncertainty,
  continuous batching, KV/cache, TTFT/TPOT tails, energy or general-domain contract. Source Reliability falls
  from 4 to 3 and score from 26 to 25. It is provisionally an Experimental Ch40 refinement with Ch29/44/52
  handoffs; Ch48 is not the owner. Historical Books Gate remains closed.
  Externalization in LLM Agents then raises W15 to twelve of fifteen retained Full Source Reviews, leaving
  KnowU-Bench, MolmoWeb, and SPPO pending. Its sole v1 and all fifty-four pages were read across memory, Skill,
  protocol, harness, component interaction, parametric/externalized trade-offs, failure taxonomy, and future work.
  It is a narrative systems synthesis rather than an empirical or systematic review: no original implementation,
  benchmark, ablation, hardware/SLO contract, or uncertainty exists. The durable contribution is an ownership
  vocabulary for weights/context/memory/Skill/protocol/harness, while Ch71/73/74/77/79/80 already contain the
  corresponding context budget, provenance, authority, workflow, lifecycle, policy, observability, and rollback
  boundaries. The score remains 23 and the provisional disposition is `No Change — Already Covered` with Ch80 as
  owner. Historical Books Gate remains closed.
  KnowU-Bench then raises W15 to thirteen of fifteen retained Full Source Reviews, leaving MolmoWeb and SPPO.
  Its sole v1, all main sections and appendices, project page, and current Android/container/task/profile/log/agent/
  evaluator code boundaries were audited. Its durable mechanism expands proactive-Agent evaluation from static
  intent into an `act / ask / silent / stop-after-rejection` feedback-conditioned policy and separates initiative
  from restraint through Act, Silent, and Stop metrics, combining rule-based side-effect evidence with semantic
  rubric judgment. Four synthetic personas, LLM-generated logs, a gpt-4o simulator, judge calibration on only
  twenty-six trajectories with four human raters, and missing simulator-human fidelity, uncertainty, hardware,
  cost, and SLO prevent real-user or production extrapolation. Score 24 remains; the provisional disposition is
  `Refine — Existing Argument (Experimental)` in Ch62 with Ch68/73/75/77/80 handoffs. Historical Books Gate
  remains closed.

  MolmoWeb's full paper, official announcement, model/data collection, and repository then correct its source-family
  owner from W15 to W13: Ai2 first published the model, data, and evaluation tools on 2026-03-24, before the
  2026-04-09 arXiv v1 and 2026-04-10 full-code update. At that checkpoint W13 recorded twenty-five scored families
  and twenty-one of twenty-one `20+` reviews; a later vLLM fixed-source replay raises the current ledger to
  twenty-six scored families and twenty-two of twenty-two `20+` reviews. W15 records seventeen families and
  thirteen of fourteen retained reviews, with only
  SPPO pending. The provisional owner is Ch23, because the durable gap is trajectory lineage across teacher/student
  observation modality, action abstraction, browser revision, verifier and judge. `pass@k` is candidate coverage,
  not deployable selector reliability; synthetic AxTree and human demonstrations remain alternative branches.
  Historical Books Gate remains closed.

  SPPO then completes W15's recorded retained queue at fourteen of fourteen. Its sole v1, all appendices, math and
  classic-control evaluations, official verl fork and run scripts, `sequence_level_adv` code path, and Ch28-30
  adjacency were audited. It retains a learned Critic but reduces its input/target from per-prefix return to
  policy-conditioned prompt solvability, broadcasting `R-V(prompt)` across response tokens. This trades Critic
  state, calibration, refresh and version coupling for single-rollout updates; it bypasses noisy temporal value
  estimation but does not identify causal reasoning steps. The evidence is limited to 1.5B/7B math RLVR and five
  deterministic binary-outcome control tasks on four A100/H100 GPUs, with zero reference KL, no multi-seed
  uncertainty and no complete calibration audit. Score 26 remains; the provisional owner is Ch28 with a Ch29
  handoff and `Refine — Existing Argument (Experimental)` disposition. W15 discovery coverage and its Evidence
  Gate remain open; Historical Books Gate remains closed.

  A later W16-to-W15 attribution reconciliation adds seven date-only identities—SkVM, GameWorld, Process Reward
  Agents, BERT-as-a-Judge, Many-Tier Instruction Hierarchy, SCOPE (OPD), and Tracing the Roots—but no author,
  stable identifier, artifact, or readable primary text is available from the saved source chain. They are therefore
  explicit unscored `Unverified / Blocked Spillbacks`, not inferred mechanisms or Books candidates. The current W15
  ledger is seventeen scored families (eight high, six medium, three low), fourteen of fourteen scored `20+` Full
  Source Reviews, seven blocked identities, and zero current-review pending. Its Forward Candidate Evidence Gate
  has passed and the cursor advances to W16; fixed-source Discovery and the all-history Books Gate remain open.

  The 2026-08-12 W15 fixed-source replay then expands that checkpoint to twenty-four scored families. Meta's
  Advanced AI Scaling Framework v2 and Muse preparedness report are jointly audited as version-grounded governance
  evidence; SGLang v0.5.10 is audited across piecewise CUDA Graph, Elastic NIXL-EP and PD staging-buffer mechanisms;
  Think in Strokes, FinTrace, SinkTrack and CodeComp receive complete paper/revision/evaluation/adjacent-chapter
  reviews. Microsoft New Future of Work remains a nineteen-point research-synthesis boundary rather than a new
  system mechanism. vLLM v0.19.0 stays in W14 by its official 2026-04-03 release date. W15 now records thirteen
  high, seven medium and four low-score families; all twenty `20+` candidates and all four low-score boundaries have
  non-template reviews, while seven identity-only spillbacks remain explicitly blocked and skipped. The forward
  candidate checkpoint passes with zero ordinary pending, but the 2026-04-12 academic cross-index, remaining
  immutable Infra history, the all-history Evidence Gate and Books Gate remain open.

  The 2026-08-12 W14/W15 attribution-and-closure checkpoint then resolves all seven identities. SkVM is
  arXiv:2604.03088 and returns to W14 by its 2026-04-03 v1; its complete paper and author runtime/repository
  review adds the target-profile -> AOT variant -> runtime selection -> trace-driven JIT proposal -> reviewed
  solidification chain, while explicitly preserving raw Skills and deterministic workflows for stable or
  high-risk targets. W14 is now 27 scored families (14 high, 12 medium, 1 low), 26/26 `20+` Full Source
  Reviews, one of one low-score boundary, two blocked identity backlogs and zero ordinary pending. A
  2026-08-13 ledger review confirmed that neither attribution-only blocker appears in scoring, Full Source Review,
  ROADMAP ownership, or Books disposition. The same external access restriction already confirmed at W13 was not
  bypassed or retried through an alternate browser. W14's Candidate Gate therefore remains passed under
  blocked-skip, its broader Discovery/Historical Gate remains open, and the backlog cursor advances to W15.
  For W15, Process Reward Agents,
  BERT-as-a-Judge, Many-Tier Instruction Hierarchy, SCOPE and Tracing the Roots now have complete reviews.
  GameWorld's arXiv identity, abstract, project and repository are verified, but the 23-page primary PDF is
  not stably readable under the current access path; the earlier full-read claim is withdrawn and the item is
  now explicit `Unverified / Blocked Backlog`, with no Books eligibility. TensorRT-LLM v1.3.0rc11 is retained
  only as an 18-point pre-release boundary. W15 is now 31 scored families (19 high, 7 medium, 5 low), 25/25
  accessible `20+` Full Source Reviews, one blocked source, five of five low-score boundaries and zero
  ordinary pending. Its academic and accessible fixed-Infra forward checkpoint passes under the user's
  blocked-skip rule; the all-history Evidence Gate and Books Gate remain closed.
  A 2026-08-13 ledger review confirmed that GameWorld remains outside the accessible-review denominator and has
  no final Books disposition; the metadata/project/repository boundary packet is not treated as a full-paper read.
  The cursor therefore advances through W15 without bypassing the saved arXiv restriction.

- W17 through W30 have also been reopened and reviewed for ledger integrity. The
  recorded Full Source Reviews remain useful, but they no longer imply weekly recall.
  Combined score rows in W17, W23, W25, and W26 hide multiple Source Families; W18's
  zero-high-score conclusion needs a complete discovery replay; and W27's nine score
  rows represent eight unique candidates. The Seed2.0 packet was present but its
  heading suffix prevented machine counting; after normalization W27 has eight of
  eight unique review packets, while its expanded discovery replay remains open.
  W28 through W30 have now been replayed against the expanded discovery list and contain
  twenty-one, twenty-six, and twenty-five scored source families. This closes candidate-structure
  recovery only: forty-nine Full Source Reviews remain pending across the three weeks. All prior
  Books decisions remain provisional and the Historical Books Gate stays closed.

- W17 has now passed its Discovery and Candidate Evidence Gates. Five baseline families were
  expanded to twenty-two scored families; nineteen score at least twenty and all nineteen have
  non-template Full Source Reviews. Thirty-one named topical hits reconcile to twenty-two scored
  families, eight cross-week attributions, and one below-retention patch. The academic cross-index,
  official-institution list, and Infra fixed list are closed; KServe v0.18.0 RC is retained only as
  a pre-release/version fact and Ray 2.55.1 remains below threshold. Stochastic KV Routing was
  returned to W14 by its 2026-04-03 v1 date, while TCOD belongs to W18 by its 2026-04-27 v1 date.
  The forward cursor is now W18 and the Historical Books Gate remains closed.
  A 2026-08-13 machine recheck confirmed W16 at 42 scored / 42 retained reviews plus three named low-score
  rejection checks, and W17 at 22 scored / 19 retained reviews plus three low-score boundaries. Both weeks have
  zero pending and retain their passed Gate status; no Books files were changed.

- W18 recall has been corrected again after replaying the full Hugging Face weekly index and reopening the
  official/infra source lists. The current scored set contains seventy-three families: fifty-one high,
  sixteen medium, and six below twenty; all sixty-seven `20+` families have non-template Full Source Reviews.
  A title/date reconciliation recovered nine additional in-window families before the later fixed-source pass.
  World-R1 has now been scored 26/30 and fully reviewed across v1/v4, official code/dataset, camera-noise state,
  heterogeneous reward services, periodic objective/data switching, its evaluation contract, and Ch28-30/
  Ch61-63 adjacency; it is a provisional Ch29 Experimental refinement. Tuna-2 has now been scored 24/30 and
  reviewed across v1/v2, the project page, current official code, pixel-space architecture, masking/data-mixture/
  evaluation contracts, and Ch4-6/Ch23-24 adjacency. Its v1/v2 data-ratio conflict, anomalous v1 HTML date and
  later evaluator references, unavailable paper-run weights, and non-frozen current recipe keep it
  `Disputed Revision Integrity / Experimental`; Ch5 is only a provisional owner and no Books change is allowed.
  Conversational User Simulation has now been scored 23/30 and reviewed across the complete v1 survey, its
  Who/What/How taxonomy, evaluation, limitations, ethical boundary, and Ch61-63/Ch71-74/Ch77 adjacency. It is
  `No Change — Already Covered`: Ch62 already owns population, subject, simulator/scorer and calibration identity,
  while Ch71/73 own history, memory, drift and provenance. Perceval has now been scored 26/30 and fully reviewed
  across the CVPR/arXiv paper, official repository/checkpoints, token-span advantage, truncate/regenerate inference,
  evaluation/sensitivity, and Ch28-30/Ch62 adjacency. It is a provisional Ch29 Experimental refinement, but the
  PRM lacks independent span calibration and its self-reported hallucination plateau cannot prove absence of reward
  hacking. Turning TIDE has now been scored 26/30 and reviewed across its sole v1, all method equations and
  appendices, official code/model/data artifacts, TIDAL/CompDemo/Reverse CALM mechanisms, training/evaluation
  contracts, and Ch24-26/Ch30/Ch40 adjacency. It is a provisional Ch25 Experimental refinement: the paper
  supports cross-architecture/tokenizer distillation viability for two teacher pipelines and a 0.6B block-diffusion
  student, not a general dLLM advantage; its controlled single-H100 table actually leaves the same-size AR baseline
  faster. Step-level optimization for computer-use agents has now been scored 28/30 and reviewed across its
  sole v1 HTML/PDF, all prompts and appendices, StepWise detector weights, event-driven route/verification,
  evaluation, and Ch57-59/Ch61-63/Ch76-80 adjacency. It is a provisional Ch77 Experimental refinement. The
  paper's claimed hysteresis/bounded recovery policy is not specified in the Method or public artifact, and the
  overlapping-window 80/20 split is not disclosed as trajectory-grouped; benchmark cost/latency is therefore not
  a production economic claim. InteractWeb-Bench has now been scored 25/30 and reviewed across its sole v1
  HTML/PDF, all prompts, project/repository/data surface, synthetic persona/user/judge contracts, and Ch61-63/
  Ch73-77 adjacency. It is `No Change — Already Covered` / Ch62: the benchmark adds a domain-specific instance,
  while Ch62 already owns feedback-conditioned policy, hidden-answer judge, turn budget, artifact/trace evidence,
  and human/executable calibration. Its ground-truth-aware synthetic user, model-judged TCR/IAS/CHR, and exclusion
  of anti-hallucination from TCR prevent claims about real users or production website quality. FlashRT has now
  been scored 28/30 and reviewed across its sole v1, all appendices, current author repository, white/black-box
  threat contracts, selective recomputation, context-subsampled gradients, sensitivity, and Ch22/Ch49-51/
  Ch67-69 adjacency. It is a provisional Ch68 Experimental refinement: red-team feasibility and approximation
  policy belong to evidence identity, but four-H100/BF16/white-box target-output results do not establish generic
  Serving KV efficiency or deployment incident probability. ReVSI has now been scored 28/30 and reviewed across
  v1/v2 metadata, the complete paper and relevant appendices through the author-public full-text copy, ICML/OpenReview
  metadata, official repository/project/dataset, and Ch61-63 adjacency. Its durable contribution is to bind
  answerability and ground truth to the actual sampled observation, then use evidence-removal counterfactuals to
  expose prior reliance. Expert-owned annotation/verification, a heuristic visibility cue, mixed frame/FPS contracts,
  the proprietary tiny subset, missing independent audit and uncertainty prevent general ranking or 3D-reasoning
  claims. It is a provisional Ch62 Experimental refinement. Continued full-page Hugging Face reconciliation then
  recovered ten additional in-window families: the Visual Generation survey, verifier-based image-editing RL,
  Meta-CoT, FAMA, terminal-task synthesis via skill graphs, reasoning controllability, Zero-to-CAD, step-level
  advantage selection, onchain-agent operating controls, and Semi-DPO. Their title, arXiv identity, first-public date,
  and initial owner are verified. Step-Level Advantage Selection is now scored 28/30 and fully reviewed across
  v1, all appendices, the current official VeRL artifact, short-context truncation, confidence-conditioned asymmetric
  advantage masking, evaluation/ablation/overhead contracts, and Ch28-30 adjacency. It is a provisional Ch29
  Experimental refinement: truncation makes the context window part of reward identity, and zero-masking avoids
  false negative credit without treating a failed prefix as successful. AIME24 also selects the checkpoint; the
  single model/hardware contract, lack of independent step-gold calibration, and absent training-seed intervals
  prevent broader claims. Semi-DPO is now scored 27/30 and reviewed across the ICLR conference full text,
  Appendices 6.1-6.11, the official project page, current missing-code surface, its five-scorer consensus,
  timestep-conditioned pseudo-label lifecycle, SD1.5 training/cost contract, all ablations, and Ch29-31 adjacency.
  It is a provisional Ch30 Experimental refinement with a Ch31 handoff. Its 3,992-pair controller is not a pure
  held-out test; committee/evaluation scorers overlap, and no human audit, seeds, complete SDXL recipe or usable
  artifact is public. Operating-Layer Controls for Onchain Language-Model Agents is now scored 28/30 and reviewed
  across its sole v1, all figures/tables, Limitations/Ethics, Appendix prompt compiler/template, official AgentVault and
  Core Contracts documentation, whitepaper/Terms, and Ch79-80 adjacency. It provisionally refines Ch80, with Ch68/77
  handoffs: mandate, compiled context, typed proposal, deterministic guard, settlement, and trace have distinct owners
  but one evidence identity. Its 99.9% settlement rate is conditional on policy-valid submitted transactions and does
  not establish rejection-inclusive mandate success, profitability, or safety; raw traces, replay data, runtime code,
  randomized production comparisons, SLOs, and independent reproduction are absent. Visual Generation in the New
  Era is now scored 24/30 and reviewed across the complete v1 roadmap, v2 revision metadata, all qualitative stress
  tests, the official living-roadmap repository, and Ch61-63/Ch9-10/Ch38 adjacency. It is `No Change — Already
  Covered` / Ch62: perceptual, structural, executable and causal evidence are already separated in Ch62, while Ch10
  already requires intervention and action faithfulness for world models. The paper's closed-source architecture and
  silent-verifier explanations are explicitly speculative, and selected qualitative cases without frozen prompts,
  raw runs, seeds, calibrated scorers or uncertainty cannot establish rankings or causal mechanisms. Edit-R1 has
  also received a complete arXiv mechanism review plus OpenReview source-family/date reconciliation. Its same nine
  authors and same principle-decomposition, GCPO and RRM-guided GRPO mechanism were first public on 2025-09-03;
  it is therefore a 2025 backlog item rather than a W18 event, regardless of the 2026-04-30 arXiv v1 and later CVPR
  publication. Meta-CoT has now been scored 26/30 and reviewed across its sole v1 main paper, formulas and
  algorithms, training/evaluation contract, public project/repository/model/dataset surfaces, and Ch25/Ch27-30/
  Ch62 adjacency. Its durable contribution is to bind a typed task/meta-task/target plan, image action and
  consistency reward into one training identity, then freeze the understanding side during early-timestep
  Flow-GRPO to trade joint adaptation for stability. The five-primitive basis and entropy claim remains an
  empirical taxonomy whose supplement could not be independently reopened; closed model judges dominate data,
  reward and evaluation, and the public artifact surface does not prove a complete paper-run release. It is a
  provisional Ch29 Experimental refinement with Ch25/62 handoffs, not a Books change while the historical gate
  is closed. Compliance versus Sensibility is now scored 26/30 after a full author-manuscript review covering
  reasoning-conflict construction, hidden-state probes, CAA intervention, judge validation, implementation and
  Ch16-18/Ch27-28/Ch62 adjacency. It provisionally refines Ch17, but linear decodability and narrow steering gains
  do not establish deliberate choice, a sufficient causal feature, or production instruction-hierarchy control.
  Zero-to-CAD is now scored 28/30 after full paper, OpenReview and official dataset review across distributed
  synthesis, tool-driven repair, execution/geometric/export validation, downstream bootstrapping, complete training
  configuration and Ch22-24/Ch61-63/Ch76-78 adjacency. It provisionally refines Ch23: repair trajectory,
  validator identity and accepted program must share lineage. The evidence does not establish DFM, human design
  intent, matched superiority to real-history datasets or unbiased synthetic provenance. The other two academic
  families, FAMA and Terminal Task Synthesis, have since completed full primary-source review. FAMA is scored
  27/30 and maps to `No Change — Already Covered` in Ch78 because the durable failure-conditioned coordination
  mechanism and its judge/side-effect boundary are already explicit. Terminal Task Synthesis is scored 28/30
  and provisionally refines Ch23 through scenario-skill support coverage and graph-conditioned executable task
  synthesis; the graph counting ambiguity and absent public artifact keep it Experimental. Fixed-source reconciliation
  also recovered the EuroSys 2026 Concord formal-publication node. Its full 18-page mechanism/evaluation review is
  complete, but a 2025 acceptance announcement and Microsoft `2025/10` PDF path leave first-public timing unresolved
  against the 2026-04-27 proceedings date. It is therefore a disputed 2025 backlog reconciliation item rather than a
  new W18 score; any future Books owner would be Ch69, with learned best-effort guards explicitly layered below
  semantic verification and release authority. Broader title/date and fixed-source reconciliation remain open. The
  prior twenty-one academic reviews remain valid. System-integrated
  speculative rollout adds a complete paper, NeMo RL v0.6 artifact, measured/simulated evaluation-boundary,
  and Ch29/44 adjacency audit; it is a provisional Ch44 Experimental refinement. KServe v0.18.0 stable
  adds another completed review through its official release, release blog, CRD/control-plane docs,
  W17 RC packet, and Ch56-58 adjacency audit; it is a stable version node, not a new mechanism or Books diff.
  Kubernetes v1.36 controller staleness mitigation adds a complete official design, client-go v0.36.0 cache-API,
  and Ch53/54/63 adjacency review. It is scored 27/30 and provisionally refines Ch53: controller-local write
  watermarks and informer cache progress become an actuation precondition, while Ch54 owns the custom-controller
  implementation handoff and Ch63 owns freshness/skip observability. The evidence establishes this guard for four
  built-in controllers, not global linearizability or automatic protection for all custom controllers. Suspended
  Job mutable resources adds a second complete official review across the feature blog, Jobs concept, feature-gate/
  API reference, and Ch56/59/60 adjacency. It is scored 28/30 and provisionally refines Ch56: resource intent can
  be negotiated while suspended, but must freeze before Pods execute; Job identity preservation does not prove that
  a smaller GPU/CPU shape preserves training topology, convergence, cost, or fairness. Tiered Memory QoS adds a
  third official review across its feature Blog, Kubernetes QoS/resource/cgroup-v2 docs, kernel memory-controller
  semantics, and Ch59/63/67 adjacency. It is scored 27/30 and provisionally refines Ch67: requests can map to
  hard or soft reclaim protection while throttling remains a separate boundary, but the alpha version facts and
  absent workload benchmark do not establish lower OOM rate, higher utilization, or better latency. In-place
  Pod-level vertical scaling adds a fourth review across its feature Blog, resize/status task docs, and Ch53/56/59
  adjacency. It is scored 28/30 and provisionally refines Ch53: spec intent, node-admitted allocation and applied
  cgroup state must be separated by condition and generation; the version evidence does not establish correct
  recommendations, zero disruption, or superiority to recreation. Pod-Level Resource Managers adds a fifth
  Kubernetes review across its feature Blog, Resource Managers concept, feature-gate/task docs and Ch53/56/59
  adjacency. It is scored 28/30 and provisionally refines Ch59: the Pod budget is partitioned into exclusive
  slices and a shared remainder under scope-specific NUMA/quota semantics, while persistent reservation and
  incompatible checkpoint downgrade become new failure surfaces. The alpha, Linux/static-policy contract and
  absent workload benchmark do not establish higher ML throughput, utilization or lower tail latency. The four
  explicitly recovered resource-management families are now reviewed. Seven adjacent Kubernetes index entries
  have also been date/source-family reconciled rather than copied into W18: manifest admission, sharded list/watch
  and DRA belong to W19; PSI and workload-aware scheduling belong to W20; Agent Sandbox belongs to W12; Gateway
  API v1.5 is a W09 release with a W17 publication node. Other fixed official/infra sources still require
  event-date/source-family/relevance reconciliation.
  Microsoft Research's 2026-04-30 multi-agent network red-team has also completed an official-report,
  experiment/evidence-boundary, and Ch68/78/80 adjacency review. It is scored 28/30 and provisionally refines
  Ch78: the communication graph is also an attack-propagation graph, and evidence independence must be tied to
  verifiable identity, ownership, and delegation provenance. The internal 100+ Agent platform and four case
  studies establish existence under that setup, not general attack prevalence, model ranking, or evaluated
  mitigation effectiveness; raw traces, denominators, controlled ablations, and external reproduction are absent.
  NVIDIA's 2026-04-30 TileGym cross-DSL kernel-translation post has also completed an official engineering,
  semantic-mapping, validator/test-contract, and Ch45/77 adjacency review. It is scored 24/30 and is `No Change —
  Already Covered` / Ch77 because the chapter already owns typed problem compilation, deterministic checks,
  artifact/version lineage, and human deployment authority. Repository access remains blocked, and the single
  reported GEMM run does not establish general productivity, correctness, or unseen-kernel transfer.
  xAI Custom Voices adds a complete 2026-04-30 announcement/current-docs review across two-stage enrollment,
  team-scoped `voice_id`, reference-audio CRUD, consent/identity evidence boundaries, and Ch67-69 adjacency.
  It is scored 24/30 and provisionally refines Ch68 as a Version-Grounded case: phrase/STT matching and speaker-
  embedding comparison are policy sensors, not proof of liveness or authorization; public sources omit thresholds,
  spoof/deepfake evaluation, human escalation, audit retention, and derived-artifact deletion proof. Baidu's
  ERNIE-5.1-Preview LMArena announcement is separately scored 15/30 and remains `Weekly Only — Product/
  Leaderboard Fact; Mechanism Not Disclosed`; the 2026-05-09 formal release cannot be used to backfill a W18
  training mechanism. Mistral Workflows adds a complete 2026-04-27 announcement/current-docs review across
  deterministic workflow replay, activity retry/idempotency, event/wait semantics, worker/deployment ownership,
  OBO connector identity, current limits and Ch76-80 adjacency. It is scored 28/30 and is `No Change — Already
  Covered` / Ch77: Ch77 already owns the same durable control-plane mechanism and Ch80 owns the platform/identity
  handoff. Current documentation is not treated as a frozen launch-day snapshot, customer narratives are not
  reliability benchmarks, and no Books edit is authorized while the Historical Gate is closed. Z.ai Scaling Pain
  adds a complete 2026-04-30 incident review across PD abort/RDMA completion/KV address reuse, HiCache
  read-before-ready, speculative-acceptance anomaly telemetry, LayerSplit, its incomplete workload contract and
  Ch19/44/50-52/63 adjacency. It is scored 29/30 and provisionally refines Ch51 as a Version-Grounded incident:
  timeout cancellation cannot authorize reuse until all old-generation writers are fenced. The author report does
  not disclose frozen commits, complete denominator, hardware/precision/concurrency/SLO or independent reproduction.
  Agent-Native Research Artifacts adds a complete protocol/compiler/manager/seal review, three evaluation
  contracts, limitations/appendices, current-repository drift boundary, and Ch77/80 adjacency audit; it is a
  provisional Ch80 Experimental refinement with a Ch77 handoff. Tabular-retrieval representational stability
  adds a complete v1, v2 revision-boundary, current-artifact, evaluation-contract and Ch71-73 adjacency audit;
  it makes serialization/retriever/adapter/index revisions part of derived-view identity, while its dense-only
  gains and sparse/dataset/format regressions block a universal adapter claim. It is a provisional Ch72
  Experimental refinement with a Ch71 handoff. DataPRM adds a complete v1/v2-boundary, current-artifact,
  tool-augmented ReAct verifier, ternary-reward, GRPO-integration, evaluation/cost/limitations and
  Ch29/61-63/77 adjacency audit. It is a provisional Ch62 Experimental refinement: active verification adds
  grounding evidence but also tool authority, state, contamination and cost, and its author results remain
  data-analysis-contract evidence. GLM-5V-Turbo adds a complete v1/v3-boundary, official API/GLM-V/
  ImageMining/Skills-artifact and Ch33-39/44/62/71/73 adjacency audit. Its durable mechanism is the way
  visual-token shape changes PP/CP/TP boundaries, RL stage overlap, bin packing and context state; ownership
  moves from Ch21/38 to Ch34, with an Experimental provisional refinement. Synthetic Computers adds a
  complete v1/PDF and retrospective-Appendix review, Microsoft Research publication, current official
  dataset/schema/artifact boundary, and Ch23/62/71/73/76-78/80 adjacency audit. It turns task-only synthesis
  into environment/state synthesis with an evolving file graph, cross-day event history and scoped derived
  skills, but its 1,000-run paper set differs from the current 98-computer public artifact and shares a model
  ecosystem across setup, work, rubric and judge. It is therefore only a provisional Ch77 Experimental
  refinement. Step-Audio-R1.5 adds a complete v1/v2, official-repository, three-benchmark schema/prompt/scorer
  and Ch27-30/38/62 adjacency audit. Its text-only architecture and exclusively S2T evaluation cannot measure
  the claimed prosody, naturalness or spoken-response quality, and the report provides neither a controlled
  RLVR/RLHF ablation nor a direct human study or training contract. Ownership therefore moves from Ch38 to
  Ch27 and the disposition is `No Change — Claim–Evidence Mismatch`.
  World-R1's durable contribution is not its PSNR headline but the way high-dimensional grouped rollouts make
  3D reconstruction, VLM/aesthetic scorers, asynchronous reward joins, and phase scheduling part of the GRPO
  training contract. Its training and primary evaluation share reconstruction/semantic components, and its
  user studies are small, so it does not prove a general physical simulator or deployment economics.
  Amazon's 2026-04-29 privacy-training-data reproduction adds a 24/30 complete review across membership
  inference, local-gradient inversion, malicious-participant global-gradient reconstruction, DP/MPC layering,
  the related primary-source entry points, incomplete experiment contract and Ch63/67-69 adjacency. It is
  `No Change — Already Covered` / Ch68: the Book already owns privacy-unit, clipping/noise/accounting,
  composition, distributed-equivalence, utility and secure-aggregation boundaries. Amazon's 2026-04-27
  C3LLM explanation was also reviewed with the full 20-page v3 paper and revision history; arXiv v1 is
  2025-10-04, so it is a 2025 source-family backlog / W18 publication node and is not rescored in W18.
  PyTorch's fixed-source pass adds two complete reviews. AutoSP is scored 28/30 after reading the full
  arXiv v1, compiler rewrite, sequence-aware rematerialization, evaluation/ablation, and Ch22/24/32-36
  adjacency; it provisionally refines Ch33 as Experimental. LightSeek-SMG is scored 27/30 after reviewing
  the full engineering report, CPU/GPU ownership split, gRPC/tokenizer-cache/routing path, benchmark
  contract, and Ch38/46/49/52/58/67/80 adjacency; it provisionally refines Ch38 as Experimental. Neither
  source's repository surface was treated as verified while access is blocked, and no Books edit is made.
  IBM Research's 2026-04-29 Granite 4.1 release has also been recovered, but is not represented as one scored
  bundle: the five product classes are partitioned into seven mechanism-level source families because Speech AR,
  Plus, and NAR have different state machines, output schemas, and latency contracts. The Language family now has
  a complete official technical-article, 3B/8B/30B card,
  8B config/history, training/evaluation, and chapter-adjacency review. It scores 24/30 and provisionally refines
  Ch24 as Version-Grounded evidence. Its 512K training exposure is explicitly separated from the current released
  artifact's 131,072-position contract. Vision now also has a complete current card/config/history, ChartNet v1/
  dataset, architecture, evaluation, and chapter-adjacency review. It scores 24/30 and provisionally refines Ch17
  as Experimental evidence; the current 4.2M-row dataset and May/June subsets are not back-written as the launch
  training manifest. Speech NAR now also has a complete sole-v1 NLE paper/current-card review across the frozen
  CTC draft, interleaved insertion slots, bidirectional editor, CTC collapse, matched AR/CTC experiment, all
  ablations, sensitivity, error analysis, runtime constraints, and Ch38-41/44/62 adjacency. It scores 27/30 and
  provisionally refines Ch40 as Experimental. The NLE, NLE++, and current-artifact data/projector/LoRA/batch
  contracts remain explicitly separate. Speech AR also has a complete current-card, 2025 predecessor architecture,
  and W11 Self-Speculative review across dual-head/importance pooling, Q-Former modality alignment, the 174K-hour
  data/task schema, relaxed verification, evaluation, safety, and Ch5/17/38-40/44/62 adjacency. It scores 26/30
  and provisionally refines Ch5 as Experimental; the 4.1 artifact and earlier experiments are not conflated.
  Speech Plus now also has a complete current-card and two related-paper review across structured speaker/time
  tokens, conversation-local speaker identity, prefix-conditioned incremental state, SAA/timestamp data lineage,
  evaluation and Ch5/38/40/62 adjacency. It scores 26/30 and provisionally refines Ch38 as Experimental. The
  current 2B artifact, the SAA 8B paper, and the In-Sync 8B paper retain separate architecture, length, output-
  encoding and evaluation contracts; incremental decode is not treated as bounded-compute streaming. Guardian
  now also has a complete current-card/docs and predecessor-paper review across the policy/risk prompt grammar,
  score formula, human/synthetic data lineage, OOD/BYOC/function/RAG/JETTS evaluation, limitations and
  Ch62/68/69/77 adjacency. It scores 26/30 and provisionally refines Ch68 as Version-Grounded evidence; the
  4.1 claims are not conflated with the 2024 training run, and neither a thinking trace nor a vendor score is treated
  as a calibrated safety guarantee. Embedding now also has a complete current-artifact and later-public-paper review
  across layer/vocabulary reduction, language-routed two-teacher distillation, 512-to-4K retrieval training,
  long-context evaluation, per-language regressions, runtime-dependent unpadding throughput, and Ch22/45/62/72
  adjacency. It scores 27/30 and provisionally refines Ch72 as Version-Grounded evidence. The 2026-04-29 artifact
  release and the paper first published in W20 remain separate event nodes; accepting 32K input is not treated as
  evidence of 32K training or uniformly effective retrieval, and unchanged weights do not imply an unchanged
  serving contract when the tokenizer/runtime path changes.
  Initial official-index boundaries for OpenAI, Apple, Ai2, Mistral, DeepSeek, NVIDIA, Amazon, PyTorch,
  Cohere, Qwen Code, Kimi and MiniMax are now recorded. The Hugging Face Blog pass also retained DeepInfra's
  provider integration at 19/30 and NVIDIA/Siemens Raw2Insights-US at 17/30; both have source/date/rejection
  checks and neither changes the `20+` review denominator. The
  framework release pass has additionally completed mechanism-level reviews of vLLM v0.20.0 and Transformers
  v5.7.0. The vLLM family is 29/30 and provisionally refines Ch46 through request-slot generation, tenant cache
  namespaces, external KV ownership, transfer-topology identity, and IR/kernel-dispatch boundaries; unavailable
  individual PR pages remain release-level verified only. The Transformers family is 26/30 and provisionally
  refines Ch42 through actual-free-memory and two-peak admission sizing, write-only Prefill, CPU offload, and
  recompute fallback; incomplete benchmark contracts are not generalized. That checkpoint left W18 at 75 scored
  families, 69 at `20+`, and 69/69 non-template Full Source Reviews. A subsequent replay of the 2026-04-27
  through 2026-05-01 Hugging Face daily paper pages invalidated the earlier claim that no known in-window academic
  review was pending. Diffusion Templates has now been fully read across its sole v1, framework design, template
  cache/model/pipeline/training, eleven model-zoo cases, evidence boundary, future work, and Ch54-56 adjacency.
  It scores 28/30 and provisionally refines Ch55, with Ch26/45 handoffs; its hardware-free `1.8x` editing claim is
  not generalized. Refinement via Regeneration has now also been read across its sole v1, current official
  repository/inferencer/model card, experiments, ablations, and Ch22-24 adjacency. It scores 27/30 and provisionally
  refines Ch23, with Ch25/62 handoffs; the author benchmark is not generalized to identity/locality preservation,
  multi-round convergence, or production cost. Mutual Forcing is also complete across its sole v1, full methods,
  experiments and appendices, official project page, demo-only current repository, and Ch24-26 adjacency. It scores
  28/30 and provisionally refines Ch25, with Ch38/40 handoffs; 4/8-NFE, 25-second and FPS claims remain author-
  workload evidence, and the online fake model prevents “teacher-free” from being read as stateless training.
  Co-Director is also complete across its sole v1, methods, evaluations, all appendices/prompts, current official
  code and Ch62/76-78 adjacency. It scores 27/30 and is `No Change — Already Covered` / Ch77: T=4 MAB is an
  author workflow result, while the judge-generated factored reward and forced strategic/execution correlation do
  not establish causal credit. MAIC-UI is now also complete across its sole v1, formative study, method, lab and
  classroom evaluations, all implementation/limitation appendices, current official implementation and Ch62/76-78
  adjacency. It scores 28/30 and is `No Change — Already Covered` / Ch77: the paper and code make a human-selected
  element scope plus diff-first patch workflow concrete, but the full-system lab comparison does not isolate its
  components, the event-time artifact is not frozen, and the single-school observational deployment cannot prove
  causal learning gains. GoClick is now also complete across its sole v1, full methods/evaluations/limitations,
  current official repository, model/data/evaluation surfaces, and Ch10/23/62/74-78 adjacency. It scores 28/30
  and provisionally refines Ch10, with Ch23/62/75/78 handoffs: it makes the cloud-planner / device-grounder split
  and narrow encoder-decoder/data-refinement branch concrete, but L20 batch-1 BF16 latency and frozen-trajectory
  Step SR do not establish real-device SLO, energy, privacy, recovery, or online task success. AutoGUI-v2 is now
  also complete across its sole v1, all fifty-one PDF pages including implementation/task-generation/prompts/
  limitations appendices, the current official repository, public dataset surfaces, and Ch61-63/75/77 adjacency.
  It scores 27/30 and is `No Change — Already Covered` / Ch62: its hierarchical functionality and hard-negative
  suite strengthens static capability decomposition, but it neither executes actions nor measures multi-step
  planning, environment transitions, recovery, or task success. W18 then had 82 scored families, 76 at `20+`, and
  76/76 Full Source Reviews for the current scored set. X-WAM is now also complete across its sole event-time v1,
  appendices, project page, later-release artifact boundary, evaluation contract and Ch9-10/20/38/62 adjacency.
  It scores 28/30 and provisionally refines Ch10: modality-specific completion deadlines and coupled noise schedules
  are durable mechanism candidates, while predicted RGB-D is not causal world state and June artifacts cannot be
  backdated to W18. ExoActor is complete across its sole v1, cases, failures, ablations, latency, prompts, project
  page, 404 code boundary and Ch9-10/38/62/75/77 adjacency. It scores 24/30 and is `No Change — Already Covered`
  / Ch10: modular video-to-motion-to-controller handoffs expose error amplification, but no trial denominator,
  success rate, uncertainty or reproducible artifact supports a general zero-shot-control claim. Representation
  Fréchet Loss is now complete across its sole v1, all appendices, current repository surface, Queue/EMA population
  estimator, evaluation contract and Ch23-25/62 adjacency. It scores 29/30 and provisionally refines Ch62, with
  Ch23/24 handoffs: decoupling population-estimation and gradient windows is a durable state mechanism, while using
  the scorer as loss creates stale-state and Goodhart surfaces; absent hardware/cost evidence prevents generalizing
  FD-SIM or one-step generation. W18 now has 85 scored families, 79 at `20+`, and 79/79 Full Source Reviews for
  the current scored set. ElementsClaw was then date-reconciled through the official
  arXiv submission history: v1 is 2026-04-26 in W17, v2 is 2026-04-29 in W18, and v3 is 2026-05-04. It is therefore
  a W17 source family with a W18 revision node, not a new W18 score row; the forward cursor remains at W18 and the
  W17 full review is deferred to the post-W30 spillback sweep. The denominator is explicitly open: ViPO and Safety Drift are
  date-confirmed in-window but `Unverified / Blocked Backlog`, because current browser permissions deny both the
  arXiv primary text and the attempted author-artifact discovery path. They remain unscored and are not counted as
  Full Reviews. EmbodiedMidtrain, DiagramBank, IndustryAssetEQA, and other page hits still await primary-date
  reconciliation. SGLang v0.5.10 was returned to W15 by its April 6 release date. How Much Is One Recurrence Worth
  belongs to W17 by its April 22 v1; its April 27 v2 is only a W18 revision node. The remaining HF title queue and
  other named institution/framework/RFC/PR indexes still need first-public-date and source-family reconciliation.
  The user explicitly authorized temporarily marking the two inaccessible sources and continuing on 2026-08-11;
  therefore the forward cursor advances to W19 without claiming W18 Historical Evidence Gate completion. Both
  blocked papers and the remaining W18 discovery surfaces stay in the post-forward backlog, and Historical Books
  Gate remains closed.
  Earlier-week spillbacks such as
  Sapiens2, DIVERT, Memanto, and AgentSearchBench are recorded in backlog rather than pulling the forward cursor
  back from W18. Discovery Recall and W18 Evidence Gate remain open; Historical Books Gate stays closed.

- W19 has advanced from three baseline families to thirty-five scored families. ARIS,
  HeavySkill, T2PO, PhysicianBench, OpenSeeker-v2, Reasoning-Intensive Retrieval,
  Workspace-Bench, AI co-mathematician, Auto Research with Specialist Agents, A2TGPO,
  STALE, UniPrefill, LLMs Improving LLMs, HyperEyes, Soohak, MCP-Cosmos, MemPrivacy,
  Geometry Conflict, GPT-5.5 Instant, EMO, ERNIE 5.1, four Kubernetes 1.36 mechanisms,
  NCCL Inspector, vLLM 0.20.1-0.20.2, and the three baseline packets make thirty of thirty
  accessible `20+` Full Source Reviews; NSF OMAI has a low-score source/boundary review, and the
  current scored set has no pending review. MolmoAct2 has accessible official code,
  datasets and deployment documentation, but its paper full text is currently inaccessible;
  it is therefore an explicit `Unverified / Blocked Backlog`, not a Full Review, and does not
  stop the user-authorized forward sweep. ARIS has been read across its three-layer architecture, cross-model review,
  evidence-to-claim audit cascade, skill/wiki/workflow implementation, meta-optimization,
  observational deployment evidence, limitations, and Appendices A-E. Its one overnight
  trajectory proves executability, not a causal advantage for cross-family review; the
  compute-matched benchmark remains future work. Eight W20-feed papers were returned to
  W19 by their May 7-10 v1 dates. OpenSearch-VL, Skill1, and StraTA also moved to
  `Unverified / Blocked Backlog` because their primary text was unavailable through the
  currently permitted access paths; they do not count as Full Source Reviews and do not
  block the forward sweep. The fixed official/Infra checkpoint has passed; cross-index discovery
  remains in post-forward backlog, so W19 Historical Evidence Gate is still open even though the
  forward cursor has advanced beyond W20. AI co-mathematician separates stateful human-steered research
  workflow from static problem solving and records reviewer false consensus/non-termination;
  Auto Research with Specialist Agents supplies evaluator-owned append-only trial lineage and
  a matched no-lineage control; A2TGPO aligns comparison cohort, credit accumulation, and
  policy-update granularity at the turn level while retaining ground-truth and small-group limits.
  STALE separates updated-evidence retrieval from current-state adjudication and adds an explicit
  unknown-current safety state; UniPrefill extends sparse Prefill from one attention kernel into
  hybrid-block token propagation and per-layer runtime metadata, while its inconsistent asymptotic
  FLOPs claim is explicitly excluded; AutoTTS separates controller search from expensive generation
  through fixed replay and execution traces, without treating replay cost as online inference cost.
  Geometry Conflict distinguishes state-relative/global update geometry from weak isolated pairwise
  conflict, retains replay/regularization/plain merge as coexisting branches, and records the paper's
  inconsistent 1.7B gain as unusable evidence. MemPrivacy separates edge detection, policy-bound typed
  aliasing, cloud memory, and local restoration, while treating its plaintext unscoped reference
  mapping as an artifact-level security gap rather than an end-to-end privacy guarantee.
  ARIS, HeavySkill, T2PO, PhysicianBench, Reasoning-Intensive Retrieval, Workspace-Bench,
  AI co-mathematician, Auto Research with Specialist Agents, A2TGPO, STALE, UniPrefill, and
  LLMs Improving LLMs are provisionally Ch77, Ch78, Ch29, Ch62, Ch72, Ch62, Ch77, Ch77,
  Ch29, Ch73, Ch39, and Ch77 refinements respectively; OpenSeeker-v2 is a concrete Ch23
  no-change case. HyperEyes, MemPrivacy, and Geometry Conflict are provisional Ch29, Ch68,
  and Ch25 refinements; Soohak and MCP-Cosmos are concrete Ch62 and Ch75 no-change cases.
  EMO provisionally refines Ch21 by making objective-shaped modularity and versioned expert-subset
  selection one contract; the Kubernetes mechanisms restore bootstrap policy, validation takeover,
  controller partitioning, and device-readiness evolution. NCCL Inspector provisionally refines Ch63.
  GPT-5.5 Instant, the vLLM patch series, and NSF OMAI remain source-family, version, and availability
  boundaries rather than new universal mechanisms.
  There is no Books edit while the Historical Gate is closed.

- W20 has advanced from two baseline items to thirty-one scored families. Thirty score at
  least twenty; twenty-nine accessible Full Source Reviews are complete, Qwen-Image-2.0 is an explicit
  `Unverified / Blocked Backlog`, and no current-review candidate remains pending. The forward
  cursor has advanced to W21. MinT was read across its thirty-page
  report, appendices, public SDK/runtime/cookbook,
  policy-record and adapter-revision state model, distributed export, cache/readiness path,
  full Scale Up/Down/Out evaluation contract, native-vLLM compatibility caveat, and negative
  adaptive-activation result. The durable insight is that training state, immutable behavior,
  durable addressability, local residency, and readiness evolve at different time scales.
  δ-mem separates a fixed-size online associative state from its frozen full-attention backbone;
  SDAR uses a bounded, detached token-level self-teacher gap as an auxiliary signal rather than
  replacing RL. Long-Context VLM Beyond 128K makes evidence localization, length distribution,
  task mixture and visual-token preprocessing one auditable data curriculum; its synthetic
  256K/512K padding tests are not generalized to arbitrary real documents. RubricEM aligns
  workflow stage, judge rubric and reflection-memory schemas, while retaining judge alignment,
  shared-backbone negative transfer, staleness and provenance as explicit conditions.
  BetaPRM preserves Monte Carlo continuation counts instead of collapsing them into point labels,
  then separates reward mean from learned evidence concentration for uncertainty-aware Best-of-N;
  its concentration is not generalized into a correctness guarantee or statistical confidence bound.
  RTPurbo separates offline head-role calibration, low-dimensional candidate routing and exact sparse
  attention, while keeping retrieval-head prefill and full KV dense. Its two approximately 600-step
  training stages contradict a literal hundred-total-step reading of the title, and its H20 attention-
  operator speedups are not generalized to end-to-end serving.
  WildClawBench has been reviewed across its sole v1, all evaluation/limitations appendices, current
  repository, container/grader contract, and Ch62/61/63/68/77/80 adjacency. It confirms that model,
  harness, tools, budget, environment and scorer jointly define an Agent-evaluation subject; its five-
  task human-judge case study does not establish GPT judge as ground truth. It is `No Change — Already
  Covered` / Ch62 because that chapter already owns complete subject identity, trajectory/side-effect
  evidence, hybrid verification, judge audit, uncertainty and cost/SLO boundaries.
  ToolCUA has also completed its sole v1, all implementation/limitations appendices, project/repository/
  model/evaluation surface, and Ch74/29/62/68/77 adjacency review. It identifies hybrid action-space
  expansion as a trajectory-level branch-policy problem; synthetic next-state grounding is not real API
  execution, and a success-gated path reward does not establish a globally optimal or safe shortest path.
  It provisionally refines Ch74 as Experimental, with reward/evidence/permission/recovery handoffs.
  EVA-Bench has been read across v2, Appendices A-R, official code/data, and Ch62/61/63/65 adjacency.
  It treats the generative user simulator as a separately validation-gated evaluation participant and
  separates average, peak, and all-trial reliability through pass@1, pass@k, and pass^k. Bot-to-bot
  simulation, mock tools, commercial simulator drift, and log-timestamp reconciliation remain explicit
  sim-to-real boundaries. It provisionally refines Ch62 as Experimental rather than replacing its existing
  subject-identity, trajectory evidence, judge-audit, and uncertainty contracts.
  EvolveMem has also been read across its sole v1, complete appendices, current implementation
  surface, and Ch73/72/74/62/77 adjacency. It makes retrieval configuration a separately versioned
  derived policy and guards offline proposals with best-so-far, revert, and stagnation exploration.
  The paper does not clearly separate evolution and final-test splits; its extraction-quality ablation
  is much larger than removing self-evolution itself. It therefore provisionally refines Ch73 as
  Experimental and does not support autonomous online self-modification or universal retrieval claims.
  MemLens has now been read across its sole 63-page v1, all A-I appendices, current evaluation code,
  memory-agent reproduction notes, dataset/schema surface, and Ch62/72/73/17/22/23 adjacency. It
  separates original multimodal evidence, write-time representation, retrieval, answer-time representation,
  and judge state, and uses image removal plus oracle retrieval to distinguish fidelity, retrieval, and
  comprehension failures. Its direct-LVLM/full-789 and agent/195-subset protocols use heterogeneous
  input adapters and proxy image-token accounting; synthetic conversations, partial judge audit, unmatched
  compute, and the absence of an evaluated hybrid architecture keep the result Experimental. It provisionally
  refines Ch62 rather than establishing a general ranking of long Context versus external memory.
  MemEye has now been read across its sole v1 HTML, all appendices, official benchmark/code/data
  surface, and Ch62/72/73 adjacency. Its orthogonal visual-granularity and reasoning-depth axes,
  oracle controls, and evolving-state probes expose a durable distinction between semantic relevance
  and temporal authority. The stronger-caption ablation closes most of the reported raw-image gap,
  so the conclusion is representation-rate and evidence-provenance dependent rather than a universal
  raw-pixel advantage. It provisionally refines Ch62 as Experimental; Ch73 receives only a state-validity
  handoff when the Historical Books Gate later opens.
  Anti-Self-Distillation has now been read across its sole v1, all proofs/ablations/limitations,
  current veRL fork/recipes, and Ch25/28-30 adjacency. Its conditional-PMI derivation exposes how
  privileged context can reverse the desired token-credit polarity for search, while bounded JSD shaping
  and an entropy hysteresis gate provide a model-conditional controller. The reported step speedup is not
  wall-clock or GPU-cost speedup, and nonlinear AntiSD shaping does not automatically inherit the linear
  PMI telescoping argument. It provisionally refines Ch29 as Experimental; no Books edit occurs before Gate.
  Video2GUI has now been read across its thirty-page v1, all appendices, project repository,
  post-event WildGUI release/schema, and Ch23/22/24/74/75/77 adjacency. It makes observation-derived
  trajectory generation a staged compiler with timestamp, frame, action and state-change lineage. The
  current repository does not expose the full extraction pipeline; the later personally reprocessed
  dataset's roughly 94.2M rows cannot be equated with the paper's 12.7M task trajectories, and source
  rights, privacy, contamination and takedown remain open. It provisionally refines Ch23 as Experimental.
  π-Bench has now been read across its v1/v3 paper, all appendices, official benchmark artifact,
  project page, and Ch62/61/63/73/75/77 adjacency. It separates who drives latent-requirement discovery
  from whether the final workflow is completed, while exposing the simulator as an information channel
  and scorer-owned state machine. Because the user simulator eventually reveals every intent and Proc
  does not penalize false-positive inference, overreach or unwanted intervention, its score cannot be
  generalized into user value or deployment safety. It provisionally refines Ch62 as Experimental.
  HarnessAudit has now been read across v1/v2, every implementation appendix, its official runner,
  dataset surface, and Ch62/68/74/77/78/80 adjacency. Its durable mechanism treats the harness as
  a policy-constrained execution subject and separates hidden post-hoc boundary evidence, execution
  fidelity, and perturbation stability over normalized append-only traces and final state snapshots.
  The paper/project contain conflicting best-overall values, 91-versus-94 tool counts, and different
  S@T thresholds; single-run results and unnormalized event counts also confound trajectory length with
  exposure. It therefore provisionally refines Ch62 as `Experimental / Disputed Accounting`, without
  carrying the leaderboard claims into Books. W20 Candidate Evidence Gate passes for the forward sweep;
  blocked and cross-index discovery backlogs keep the global Historical Evidence Gate open.
  Fixed official and infrastructure replay additionally covers Kubernetes PSI, Workload-Aware Scheduling
  v1alpha2, Service `externalIPs` deprecation, Mixed Version Proxy Beta, the CCM route-sync counter,
  OpenAI's TanStack incident and cross-conversation safety summaries, NVIDIA Fleet Intelligence and its
  public host agent, the NVIDIA serving-pipeline checklist, and Transformers v5.8.1. The durable candidate
  owners are Ch63, Ch60, Ch68, Ch53, Ch68/73, and Ch63/68 respectively; the route counter and serving
  checklist are chapter-level no-change evidence, while the Transformers patch is a version fact. Official
  incident or product claims are not treated as independent forensics or universal benchmark evidence.
  Six curation-lag papers exposed by the W21 feed were returned to W20 by their May 12-17
  v1 dates. MinT, δ-mem, SDAR, Long-Context VLM Beyond 128K, RubricEM, BetaPRM and RTPurbo are provisionally
  Ch55, Ch22, Ch29, Ch23, Ch29, Ch62 and Ch22 refinements. Qwen-Image-2.0 does not block the forward
  cursor, but remains in the post-forward retry ledger. No Books edit is allowed before the
  Historical Gate.

- W21 has advanced from three baseline items to thirty-one scored families. Thirty score at least twenty
  and one has a completed low-score boundary. SkillsVote and LongLive-2.0 are `Unverified / Blocked Backlog` because their primary texts
  are unavailable through the currently permitted paths. WorldKV's official project page and two-commit repository
  are accessible, but its 15 MB full paper cannot be read through the current primary-source paths; it therefore joins
  the same backlog without performance or mechanism extrapolation. Twenty-six of thirty `20+` Full Source
  Reviews are complete, no current-review candidate remains pending, the W21 fixed official/Infra checkpoint has passed, and
  the forward cursor has advanced to W22.
  OpenComputer has been read across its full paper, experiments, self-evolving-verifier
  ablation, limitations, appendix case studies, public repository, and Ch62/77/80 adjacency.
  Its stable mechanism is verification-first environment and task synthesis with fixed-
  trajectory, bounded checker repair; checkability bias, schema drift, checker regression,
  and visual criteria remain explicit boundaries. It is provisionally a Ch62 refinement.
  HRM-Text has been read across its sole v1, appendices, dual-timescale recurrence, MagicNorm,
  truncated-credit warmup, task-formatted data, matched-compute and objective ablations,
  contamination analysis, public implementation surface, and Ch16-18/23-25 adjacency. It
  provisionally refines Ch17 as Experimental: parameter-shared recurrence, PrefixLM, response-only
  loss, and the data distribution form one training contract; the heterogeneous external baseline
  headlines do not establish general superiority over standard Transformers.
  Code as Agent Harness has also been reviewed across its full 1,208-line HTML, interface/mechanism/
  multi-agent taxonomy, PEV control, adaptive-harness and transactional-state agenda, and companion
  bibliography. It is `No Change — Already Covered` / Ch80 because Ch62/74/75/77/78/80 already own
  the concrete contracts; absent a systematic-review protocol, unified experiment, or executable artifact,
  the survey taxonomy is not treated as new mechanism evidence.
  DelTA has now been read across its sole v1, all A-L appendices, local-gradient derivation,
  centroid/refinement algorithm, training and evaluation contract, baselines, ablations, sensitivity,
  computational overhead, supplementary backbone/code/OOD evidence, current veRL-based repository
  surface, and Ch28-30 adjacency. It provisionally refines Ch29 as Experimental: reward-side
  gradient-proxy weighting is a distinct token-credit branch, while extra actor passes, batch
  composition, proxy bias, checkpoint-selection reuse, and absent multi-seed training evidence remain
  explicit limits.
  Neither of the two initial blocked candidates counts as reviewed or receives a Books owner or mechanism inference;
  both move to the post-forward retry ledger without blocking the W21 cursor.
  OSCAR has now been read across its 35-page v1, all theoretical/system/evaluation appendices, official
  SGLang-based repository and project surface, and Ch40-43/45/50 adjacency. It provisionally refines Ch41
  as Experimental: attention-induced calibration targets, protected BF16 boundary windows, uniform INT2
  history pages, and a fused decode path form one system contract. Conflicting calibration defaults,
  frozen-error theory, H100-specific evidence, prefix identity, and artifact lifecycle remain explicit limits.
  EnvFactory has now been read across its sole v1, all appendices, official environment/data/model/training
  surface, and Ch62/74/77/79/80 adjacency. It provisionally refines Ch77 as Experimental: source-grounded
  executable state, dependency-aware trajectory synthesis, SFT cold start, and composite-reward RL form a
  versioned training-data workflow. Internal generated tests do not establish real-API behavioral conformance;
  failed-call filtering, correlated simulator/judge models, isolated-session throughput, the partial MCP-Atlas
  contract, paper/repository data-unit drift, and ambiguous sampling pseudocode remain explicit limits.
  Mix-Quant has now been read across its sole v1, complete method and phase ablation, two-commit official
  repository, pinned vLLM/NIXL launch path, and Ch39-41/45/50-52 adjacency. It provisionally refines Ch51 as
  Experimental: phase-specific precision and model artifacts require a shared tokenizer/position/KV contract,
  while initial-Prefill versus Decode-added KV provenance becomes part of cache identity. The approximately
  three-times result is isolated RTX 5090 Prefill-stage latency, not end-to-end TTFT, TPOT, NIXL transfer,
  goodput, total-budget, failure-recovery, or production-SLO evidence; the public artifact also exposes only a
  subset of the paper evaluation matrix.
  ACC has now been reviewed across v1/v2, all A-F appendices, official dataset/checkpoint cards, and
  Ch22-25/62/77 adjacency. It provisionally refines Ch23 as Experimental: an answer-verified interactive
  trajectory is transformed into a derived direct-answer long-context dataset, so the stable contribution is
  governed data lineage and a distinct evidence-integration objective, not replacement of the original tool
  policy. Success-only selection, shuffled temporal structure, privileged-patch SWE rationales, incomplete
  evidence/answer contamination testing, undisclosed training hardware, and post-hoc selected attention/router
  plots remain explicit limits. Ch22/25/62/77 are only handoffs, and no Books edit is authorized while the
  Historical Gate is closed.
  GoLongRL has now been read across its sole 39-page v1, all relevant appendices, official training and evaluation
  repositories, dataset/checkpoint cards, and Ch22/23/28-30/62 adjacency. It provisionally refines Ch29 as
  Experimental: heterogeneous long-context RL must treat reward scale, within-task difficulty, and task sampling
  mass as separate controls. Task-level variance normalization does not balance a sample-skewed capability mixture;
  model-solvability filtering, benchmark-guided dataset revision, query-only 13-gram overlap, single-run evidence,
  absent 30B algorithm ablation, evaluation-alignment deltas, and YaRN-confounded 1M results remain explicit limits.
  Ch22/23/62 are only handoffs, and no Books edit is authorized while the Historical Gate is closed.
  WorldKV has only an official-artifact-level verification: camera-pose retrieval, GPU/CPU KV-bank placement,
  `sink + retrieved + recent` windows, optional RoPE correction, and anchor/novelty compression flags are visible in
  the project/repository surface. The paper's evaluation, ablations, limitations, transfer costs, and roughly two-times
  headline are not Full Source Review evidence. It is `Unverified / Blocked Backlog`, receives no Books owner, and does
  not stop the forward cursor.
  PlanningBench has now been read across v1/v2 metadata, the complete 27-page v2 and appendices, official one-commit
  repository, 467-row evaluation dataset/license, and Ch23/24/61-63/76-78 adjacency. It is `No Change — Already
  Covered` / Ch62, with Ch23 only a data-pipeline handoff: the existing chapters already own constraint-derived data,
  shared generator/verifier blind spots, rubric formation, criterion execution, judge calibration, and the distinction
  between local criterion satisfaction and global validity. The unreleased 300-row training set, single critic, default
  inference parameters, undisclosed hardware/seeds/statistical method, and reuse of the measurement channel for reward
  remain explicit evidence limits. No Books edit is authorized while the Historical Gate is closed.
  Gated DeltaNet-2 has now been read across its sole v1, all A-E appendices, official seven-commit implementation
  surface, and Ch14-15/17/22/39-40/45 adjacency. It provisionally refines Ch22 as Experimental: channel-wise decay,
  key-side erase/read, and value-side write are distinct controls over a fixed recurrent state, while compact-WY chunk
  training, gate-aware backward, fp32 state/solve policy, and recurrent decoding show that model freedom must be carried
  into the execution contract. The 1.3B/100B-token, 4K-training, 2K-SWA, single-H100 and single-run evidence does not
  establish universal superiority over dense Attention, KDA or Mamba, and no Decode SLO, state-lifecycle or multi-GPU
  evidence is public. Ch17/39/40/45 are handoffs only; no Books edit is authorized while the Historical Gate is closed.
  Post-Trained MoE/ZEDA has now been read across v1/v2, all A-D appendices, the official sixteen-commit
  training/evaluation surface, two checkpoint cards, and Ch21/25/40/45/52 adjacency. It provisionally refines Ch21 as
  Experimental: parameter-free zero-output routes, frozen-teacher SFT followed by on-policy distillation, group-level
  routing preservation, and no renormalization form a post-trained static-to-dynamic MoE migration contract. Roughly
  half the expert FLOPs cannot be read as half the service cost: the reported throughput is bound to one H200, sequence
  length 8192, concurrency 32, 256 examples sampled from training prompts, and undisclosed serving precision, without
  TTFT/TPOT/goodput, EP-topology, multi-seed or rollback evidence. Ch25/40/45/52 are handoffs only; no Books edit is
  authorized while the Historical Gate is closed.
  SkillOpt has now been read across v1/v2, Limitations, the executable optimizer algorithm and prompt contracts,
  the official repository, versioned documentation, release history, and Ch62/73/76/77/80 adjacency. It provisionally
  refines Ch80 as Experimental: a Skill is external optimization state governed by bounded patches, a validation-gated
  best artifact, rejected-step evidence and separate slow/meta state, rather than a prompt that silently rewrites itself
  in production. A single split seed, repeated selection queries, the same benchmark scorer behind gate and final
  evidence, limited positive transfer cases, and undisclosed hardware/API snapshots/multi-run variance keep the 52/52
  headline inside the authors' contract. Ch77/76/73/62 are handoffs only; no Books edit is authorized while the
  Historical Gate is closed.
  Foundation Protocol has now been read across its sole v1, complete architecture/scenario, Appendix reference stack,
  both official protocol/application repositories, and Ch68/69/77-80 adjacency. Its entity/session/activity/envelope/
  event/receipt/provenance vocabulary, four planes, checkpoint pipeline and evidence spine form an early architecture
  proposal, not a validated interoperability standard. With no benchmark, formal threat model, conformance matrix,
  fault/partition evaluation, scale/SLO evidence or independent deployment, the stable claims are already concretely
  owned by Ch77-80 and Ch68/69. Its disposition is `No Change — Already Covered` / Ch80; no Books edit is authorized.
  SciAtlas has now been read across its sole v1, KG schema/index/prompt appendices, current official client/CLI/API
  surface, and Ch72/23/62 adjacency. It provisionally refines Ch72 as Experimental: lexical, semantic and title recall
  create seed state, typed graph expansion and RWR add topological support, and raw OpenAlex facts must remain distinct
  from LLM-derived keywords, embeddings, `RELATED_TO` edges and ranking traces. The paper provides qualitative examples
  but no quantitative retrieval benchmark, baseline/ablation, hardware/cost/load/freshness SLO or event-time repository
  tag; the 12-versus-11 edge schema conflict, author non-deduplication, undirected citations, manual updates and
  popularity/language/PDF selection bias remain explicit evidence limits. Ch23 and Ch62 are handoffs only, and no Books
  edit is authorized while the Historical Gate is closed.
  QUEST's metadata, official project page, repository, model and data collection are accessible, but the sole v1 has no
  arXiv HTML and its 28.7 MB PDF cannot be completely read through the currently permitted primary-source paths. Public
  rubric-tree, context-management and training-code surfaces do not substitute for the paper's full method, evaluation,
  limitations and appendices. QUEST is therefore `Unverified / Blocked Backlog`, does not count as a Full Source Review,
  receives no Books owner, and does not stop the W21 forward cursor.
  ThriftAttention has now been read across its sole v1, complete derivation and mixed-precision method, fused CUDA
  kernel, LongBench/RULER/HELMET/PG19 evaluation, sparse and selector ablations, Limitations, current official artifact
  surface, and Ch39-41/45/50 adjacency. It provisionally refines Ch45 as Experimental: a per-query-block selector
  promotes a small key-block budget to FP16 while retaining all remaining support in NVFP4, and the two paths merge
  through one online-softmax state. This is a precision-allocation branch, not evidence that uniform FP4, sparse
  attention, or exact FP16 should disappear. The single RTX PRO 6000, batch-one latency contract, undisclosed output
  length/concurrency/queue/SLO, absent downstream multi-seed/confidence intervals, matched-FLOPs sparse comparison,
  and 28% dual-cache footprint remain explicit limits. Ch39-41/50 are handoffs only, and no Books edit is authorized
  while the Historical Gate is closed.
  SkillEvolBench has now been read across its sole v1, full protocol and result tables, Raw-Trajectory comparison,
  Tier-3 capacity diagnostic, environment/cost analysis, family catalog, current runnable repository/dataset surface,
  and Ch62/73/76/80 adjacency. It provisionally refines Ch73 as Experimental: acquisition, frozen replay, and frozen
  deployment must be separated, while context shift, shortcut resistance, and composition expose different failure
  modes. Raw episodes can preserve cues lost by a derived Skill, and forced library growth can create procedural clutter;
  therefore capacity is not selective abstraction. Co-designed task families, curated seeds and verifiers, absent
  multi-seed/uncertainty, undisclosed hardware/token/runtime, model-provider/harness confounding, and no long-horizon
  cross-environment drift keep the aggregate point changes inside the authors' contract. Ch62/76/80 are handoffs only,
  and no Books edit is authorized while the Historical Gate is closed.
  NITP has now been read across v1-v3, the complete method and local curvature analysis, Dense/MoE/MTEB evaluations,
  all ablations, training and overhead appendices, the current official repository, and Ch23-25/17 adjacency. It
  provisionally refines Ch24 as `Experimental / Revision-sensitive`: standard token likelihood remains the base
  objective, while a temporally shifted, stop-gradient shallow state supplies a separate latent prediction target.
  The theoretical result depends on fixed-target, local alignment, GGN and well-conditioned-projector assumptions;
  training hardware, precision, data manifest, seeds and confidence intervals are undisclosed; implementation code is
  still announced as forthcoming. The 45B MoE appendix present in v1 was removed from v2/v3, so it is treated as
  withdrawn evidence rather than a current scaling result. Ch17 is a representation handoff only, and no Books edit
  is authorized while the Historical Gate is closed.
  The W22 curation feed returned six additional May 20-22 papers to W21, and the W23 feed returned
  NITP to its May 24 v1 date. The Historical Books
  Gate remains closed.
  The fixed-source replay additionally audits layered C2PA/SynthID/public verification as a provisional Ch68
  refinement, NVIDIA-verified Agent Skills as a provisional Ch80 lifecycle refinement with Ch68 supply-chain
  enforcement, and NVL72 Slurm segment-policy simulation as provisional Ch59 official engineering evidence.
  The content verifier's negative result is not negative origin proof; a signed/scanned Skill is not therefore safe;
  and the scheduling occupancy claim remains bound to the vendor's 5,000-node, 20,000-GPU, 15,000-job, seven-day,
  2.5%-nodes-down simulation. NVIDIA's Agent evaluation guide is already covered by Ch62, Transformers v5.9.0
  is a version fact, and token-metered services remain a low-score reference-architecture boundary. Historical Books
  Gate remains closed and no Books chapter is changed by this checkpoint.

- W22 has advanced from three baseline items to forty-three scored families. Forty-two score at
  least twenty; fifteen Full Source Reviews are complete, AgentDoG 1.5,
  How LoRA Remembers?, MemTrace, CUA-Gym, LaRA, FluxMem, Skill0.5, SkillGrad, Claw-Anything, Crafter, Domino,
  COLLEAGUE.SKILL, GrepSeek, TASTE, Trust-Region Behavior Blending, Trust Region On-Policy Distillation, LongTraceRL, dMoE, SkillAdaptor, Draft-OPD, SCOPE, Harness Updating, SAAS, RAMP, Masking Stale Observations, ResearchClawBench, and Smaller Models Are Natural Explorers are
  `Unverified / Blocked Backlog`, no current-review item remains, and one low-score
  governance fact is verified. ScientistOne v1 is now correctly owned by W22, while the July 30
  Google Research explanation remains a W31 publication node. The paper, appendices, audit
  procedure, failure taxonomy, limitations, and Ch62/77 adjacency had already been fully read
  for the W31 source family and are now recorded at the first-public week without duplicating
  Books prose. Gamma-World has been read across its sole v1, full paper and appendices, NVIDIA project,
  later official artifact, and Ch10/13/14/40 adjacency. It provisionally refines Ch10 as Experimental:
  exchangeable agent identity, hub-owned shared state, and bidirectional-teacher to causal cached-student
  evolution are durable mechanisms, while two-player-only training, qualitative multi-agent/robot evidence,
  undisclosed data, and an incomplete 24-FPS contract prevent generalization. Sixteen May 26-31 papers
  surfaced by the W23 display feed and ResearchClawBench from
  the W24 display feed were returned to W22 by arXiv v1 date.
  AgentDoG 1.5 metadata, abstract, sole-v1 date and forty-four-page primary-text surface are verified,
  but the full paper is inaccessible through the permitted paths. The W08 OpenClaw audit's AgentDoG judge
  is not substitute evidence for this paper. It therefore does not count as a Full Source Review, receives
  no Books owner or mechanism inference, moves to the post-forward blocked ledger, and does not stop W22.
  DVAO has been read across its sole v1, full HTML/PDF, three proof appendices, dual-objective math/tool-use
  evaluation, implementation, limitations, and Ch28-30 adjacency. It provisionally refines Ch29 as
  Experimental: group-wise reward variance becomes explicit adaptive-combination state, but base weights
  remain, empirical evidence uses only two rewards with G=16, and small-group/noisy-reward behavior,
  three-or-more objectives, seeds/confidence intervals, code, and compute overhead remain unresolved.
  OmniRetrieval has been read across its sole v1, method/evaluation, current official repository/code path,
  and Ch71/72/74 adjacency. It provisionally refines Ch72 as Experimental: heterogeneous search, SQL,
  SPARQL, and Cypher sources retain native operators behind top-k routing, native execution, and late evidence
  selection. Its single-gold-source questions and single-best-candidate selector do not demonstrate cross-source
  joins, while freshness, ACL, schema drift, query safety, partial failure, provenance, and production latency/SLO
  remain outside the evidence contract.
  MobileGym has been reviewed across v1/v2, the full paper and appendices, official project/repository, and
  Ch61-63/29/80 handoffs. It provisionally refines Ch62 as Experimental: one authoritative structured environment
  state supports configure/reset/fork, deterministic judging, side-effect diff, and grouped-rollout reward. The
  browser surrogate omits real backends, stochastic services, and full feature surfaces; its outcome-stratified
  59-task real-device subset is a transfer existence proof rather than a comprehensive Sim-to-Real contract.
  Bidirectional Evolutionary Search has been read across its sole v1, all appendices, theory assumptions,
  three evaluation settings, ablation/cost evidence, official project/repository, and Ch19-21/29/75/77
  adjacency. It provisionally refines Ch20 as Experimental: evolution operators widen proposal support beyond
  independent rollouts and prefix-only expansion, while a backward goal tree supplies denser selection state.
  Entropy-shell escape does not establish semantic validity or correctness; the exponential claim assumes
  independent subgoals plus reliable decomposition, verification, and recombination. Post-training stops at 8B,
  program search uses three seeds, and end-to-end compute accounting remains incomplete.
  ResearchMath-14K has been read across its sole v1, all appendices, current official dataset/schema/files/history,
  and Ch22-25/62 adjacency. It provisionally refines Ch23 as Experimental by separating source quote,
  self-contained rewrite, mutable open-status evidence, teacher attempt, and filter verdict. The current public
  artifact does not expose the claimed 220K trajectories, 5K filtered subset, training code or adapters; filter
  definition, split/card semantics, source license/status supersession, benchmark decontamination and the full
  LoRA workload contract remain unresolved. Incorrect attempts are therefore not generalized as trusted supervision.
  How LoRA Remembers? could not be read because the saved access policy explicitly denied its arXiv HTML/PDF and no
  auditable local primary text or author artifact exists in the repository. It therefore does not count as a Full Source
  Review, receives no Books owner or mechanism inference, moves to the post-forward blocked ledger, and does not stop W22.
  MemTrace is subject to the same evidence boundary: both its arXiv primary text and Hugging Face paper surface are denied,
  and no local primary text or author artifact was found. Its taxonomy, trace-attribution, overhead, and intervention focus
  remain unverified; it receives no Books owner, enters the blocked ledger, and does not stop the forward cursor.
  CUA-Gym is also blocked: the arXiv domain and the direct QwenLM/CUA-Gym official-artifact surface are denied, while no
  local primary material exists. Environment synthesis, verifier/reward, leakage, and RL mechanisms therefore remain
  unverified; the candidate receives no Books owner and does not stop W22.
  LaRA has only the same denied arXiv surface in the ledger and no local paper or author artifact. Its layer-wise geometry,
  contamination protocol, RL-vs-SFT controls, and false-positive behavior remain unverified; it receives no Books owner,
  enters the blocked ledger, and does not stop the forward cursor.
  FluxMem likewise has only the denied arXiv surface plus a `planned code` placeholder without an auditable release or
  commit identity, and no local primary material was found. Connectivity, feedback, pruning, consolidation, and rollback
  mechanisms remain unverified; it receives no Books owner and does not stop W22.
  Skill0.5 has the denied arXiv surface and an unresolvable `+ code` label without a repository, release, or commit identity;
  no local artifact exists. Internalization/externalization routing, difficulty/OOD tiers, and conflict behavior remain
  unverified; it receives no Books owner, enters the blocked ledger, and does not stop the forward cursor.
  SkillGrad has the same denied paper surface and an unresolvable `+ code` label, with no local artifact. Textual-gradient,
  momentum, patch-safety, and held-out-regression mechanisms remain unverified; it receives no Books owner, enters the
  blocked ledger, and does not stop W22.
  Claw-Anything has only the denied arXiv surface and no local primary material. Always-on execution, authority/privacy,
  proactivity metrics, and environment realism remain unverified; it receives no Books owner, enters the blocked ledger,
  and does not stop the forward cursor.
  Crafter has only the denied arXiv surface plus an unresolvable `+ code/benchmark` label, with no local artifact. Agent roles,
  editable-SVG representation, verifier/human criteria, component ablations, and visual limits remain unverified; it receives
  no Books owner, enters the blocked ledger, and does not stop W22.
  Domino has only the denied arXiv surface plus an unresolvable `+ code` label, with no local artifact. Parallel-backbone,
  refinement-head, curriculum, acceptance/latency, and backend-integration mechanisms remain unverified; it receives no
  Books owner, enters the blocked ledger, and does not stop the forward cursor.
  COLLEAGUE.SKILL has only the denied paper surface and an unresolvable `open-source artifact` label, with no local material.
  Trace-to-skill distillation, capability/behavior separation, correction/rollback, and measured claims remain unverified;
  it receives no Books owner, enters the blocked ledger, and does not stop W22.
  GrepSeek has only the denied paper surface and an unresolvable `+ code` label, with no local artifact. Tutor/Planner
  causality, GRPO, sandbox, sharding, and byte-equivalence mechanisms remain unverified; it receives no Books owner,
  enters the blocked ledger, and does not stop the forward cursor.
  TASTE has only the denied paper surface and an unresolvable `+ benchmark` label, with no local artifact. Tool-sequence
  generation, judge validity, coverage/difficulty coupling, contamination, and grader independence remain unverified;
  it receives no Books owner, enters the blocked ledger, and does not stop W22.
  Trust-Region Behavior Blending has only the denied arXiv surface and no local primary material. KL direction/bound,
  annealing, prefix distribution, two-setting generality, and stability remain unverified; it receives no Books owner,
  enters the blocked ledger, and does not stop the forward cursor.
  Trust Region On-Policy Distillation has the same denied paper surface and no local primary material. Reliable/outlier
  regions, reverse/forward-KL estimators, mask/clip sensitivity, and off-policy guidance remain unverified; it receives
  no Books owner, enters the blocked ledger, and does not stop W22.
  LongTraceRL has only the denied paper surface and an unresolvable `+ code/data/models` label, with no local artifact.
  Trajectory distractors, positive-only rubric reward, reward hacking, and contamination remain unverified; it receives
  no Books owner, enters the blocked ledger, and does not stop the forward cursor.
  dMoE has only the denied paper surface and an unresolvable `+ code` label, with no local artifact. Block/expert
  distribution, state ownership, dispatch, memory traffic, runtime implementation, quality/latency contract, and
  revision boundary remain unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  SkillAdaptor has only the denied paper surface and a `planned code` placeholder, with no immutable or local artifact.
  Fault attribution, skill responsibility, acceptance checks, rollback, benchmark realism, and reported gains remain
  unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  Draft-OPD has only the denied arXiv surface and no supporting or local artifact. Target-assisted rollout,
  verification-error replay, on-policy signal construction, acceptance/throughput conditions, and failure recovery
  remain unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  SCOPE has only the denied arXiv surface and no judge, experiment, or local artifact. Challenger/solver ownership,
  co-evolution, self-judge validity, open-ended rewards, compute-matched controls, and failure modes remain unverified;
  it receives no Books owner, enters the blocked ledger, and does not stop W22.
  Harness Updating has only the denied paper surface and an unresolvable `+ code` label, with no local artifact.
  Updater/consumer separation, activation/following failures, model-tier controls, harness identity, and rollback remain
  unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  SAAS has only the denied paper surface and an unresolvable `+ code` label, with no local artifact. Self-awareness
  reward, search-depth shaping, curriculum, accuracy/cost Pareto, live-search validity, and evidence-loss failures remain
  unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  RAMP has only the denied paper surface and an unresolvable `platform artifact` label, with no local material.
  Workflow identity, staged recovery, utility/resource accounting, failure injection, and production transfer remain
  unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  Masking Stale Observations has only the denied paper surface and an unresolvable `trajectories` label, with no local
  artifact. Its inverted-U regime, retriever/model interaction, token-for-turn trade-off, and evidence-loss failures remain
  unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  ResearchClawBench has a verified W24-to-W22 v1-date spillback, but its paper is denied and its `benchmark/code` label
  has no immutable or local artifact. Research-chain provenance, grader validity, contamination, and benchmark governance
  remain unverified; it receives no Books owner, enters the blocked ledger, and does not stop W22.
  Smaller Models Are Natural Explorers has a verified W25-to-W22 v1-date spillback, but its paper is denied and no
  immutable or local artifact exists. Scale-to-exploration causality, policy ownership, annealing, off/on-policy boundaries,
  and rollout compute remain unverified; it receives no Books owner and enters the blocked ledger. W22's forward Candidate
  Evidence Gate is passed and the cursor advances to W23, while broader discovery and Historical Evidence Gates stay open.
  The fixed official/Infra replay adds six complete source packets. Dynamo Snapshot is a provisional Ch46/53
  Experimental refinement: host/device execution snapshots can cut reconstruction latency, but privileged restore,
  compatibility, external-state freshness, and multi-GPU boundaries remain open. DynoSim is a provisional Ch62
  refinement: the stable pattern is a calibrated simulate-first inner loop with a real-cluster validation outer loop,
  not the reported workload-specific Pareto points. DOCA's isolated DPU sensor/enforcement plane provisionally refines
  Ch68 without treating vendor throughput claims or hardware isolation as universal safety. Vera CPU, DSX OS, and
  STAC-AI respectively provide bounded Ch50 workload co-design, Ch53/63 IT/OT control-plane, and Ch62 workload-contract
  evidence. W22 fixed official/Infra checkpoint passes; Historical Books Gate remains closed and no Books edit occurs.

- W23 has advanced from five baseline source families to thirty-three scored families. All thirty-three
  score at least twenty; twenty-one current-version Full Source Reviews are complete, current-review pending is zero,
  and twelve families are `Unverified / Blocked Backlog`. Under the user-approved blocked-skip rule, the forward
  Candidate Gate passes and the cursor advances to W24; W23 discovery and Historical Evidence Gates stay open.
  StreamMA's v1 event snapshot and runnable artifact are recorded in the blocked backlog and do not stop the
  forward queue. On the
  Scaling of PEFT was read across its forty-three-page PDF, algorithmic and systems sections,
  figures/tables, evaluation, limitations, and Ch25-27/54-56/73 adjacency. It separates policy
  identity, mutable training state, immutable serving/evaluation revision, catalog addressability,
  CPU residency, GPU batch slots, and readiness. Its controlled benchmarks and simulations do not
  prove a million-user deployment. Code2LoRA has now been read through its complete HTML, method,
  benchmark construction, static/evolution/OOD experiments, limitations, compute and deployment
  appendices, with Ch25/26/55/71-73 adjacency. Its repository-conditioned adapters remain evidence
  only for the disclosed Python assertion-completion, Qwen2.5-Coder-1.5B and single-H100 contract.
  Harness-1 has now been read across its 63-page PDF, state-transition algorithms, two-tier memory,
  SFT/RL recipe, eight-benchmark protocol, same-model/different-harness control, component ablations,
  limitations and Ch71-74/77 adjacency. It supports the policy/harness ownership split under that
  retrieval contract, not a universal model ranking or open-ended/adversarial-web claim. DRIFT/TELBench has
  now been read through its complete HTML, annotation pipeline, claim-ledger/support/dependency-tracing method,
  five-model-family and four-harness evaluation, ablations, token-cost appendix, and Ch62/63/76/77 adjacency.
  It supports outcome/process separation and first-harmful-commitment diagnosis only inside the disclosed
  benchmark and annotation contract, not universal production incident rates or an authoritative root cause.
  KVarN has now been read through its sole v1, magnitude/direction decomposition, pseudo-decode feedback path,
  dual-axis variance normalization, four-model 2-bit evaluation, runtime measurements, limitations, all
  appendices, and Ch40/41/42/45/46 adjacency. It supports autoregressive-state-aware KV quantization evaluation
  only for the disclosed layout, models, sampling, lengths and abstract GPU contract; it does not establish
  general serving overhead, MLA compatibility or independent reproduction. Cosmos 3 has now been read through
  its 139-page technical report, architecture, token/action representations, data and training system, Serving,
  reasoner/generator/action evaluation, ablations, relevant appendices, and Ch9/10, Ch13/14/17/18, Ch23/24,
  Ch62/75 adjacency. It supports a shared omnimodal interface with separate parameter towers, masks/objectives,
  modality clocks and runtime loops under its disclosed contracts; it does not establish causal world simulation
  or deployment-safe control. The May 31 official release belongs to W22, while W23 records only the June 1
  technical-report node. AdaPlanBench has now been read through its complete v2, construction and judge pipeline,
  interaction/state protocol, main evaluation, constraint/memory/feedback/temperature/threshold ablations, human
  validation, limitations, current repository/dataset boundary, and Ch62/71/73-77 adjacency. It provisionally refines
  Ch75 with a cumulative constraint ledger and revision-wide regression gate, but remains Experimental because its
  synthetic household, oracle-like judge, text-only plan and threshold-sensitive rubric do not establish embodied
  execution or real preference adaptation. CHERRL has now been read through its sole v1, all appendices, dual-judge
  reward construction, threshold-derived onset, discoverability/exploitability analysis, RHDA detector/control flow,
  six-run evaluation, budget/case-study evidence, compute contract, repository/data gaps, and Ch27-30/62-65/68
  adjacency. It provisionally refines Ch27 by separating privileged reward-side decomposition from judge-blind
  policy-side temporal audit, but remains Experimental: the intended judge is not ground truth, the onset is an
  operational label, full rollouts/workspaces are absent, and no online mitigation or rollback is evaluated. All eight
  recovered mechanism candidates remain provisional refinements. AutoLab has now been read through its sole v1,
  all task, experiment and analysis appendices, official project, current repository/task contract, commit history,
  and Ch62/66/76/77/80 adjacency. Its evidence is limited to thirty-six executable tasks, a fixed terminus-2 harness,
  three rollouts per model-task, and two-to-twelve-hour budgets; persistence is observational rather than an isolated
  causal intervention, and the twenty-five-task harness ablation does not establish a universal model/runtime ranking.
  Current main includes post-W23 v1.1 commits and public reference/solution paths, so it is not an immutable event-time
  artifact and future training contamination remains a live-benchmark governance issue. Ch62 and its adjacent chapters
  already own these evaluation, budget, stopping, lineage, and contamination boundaries, so the disposition is
  `No Change — Already Covered` rather than a Books edit. StreamMA has now been read across the complete
  twenty-nine-page v2 paper, protocol algorithms, three theorems and proofs, benchmark/role/tool/scaling/cost
  experiments, limitations, prompts, risk statement, current project/repository surface, and Ch77-79/71/65/66/32
  adjacency. It provisionally refines Ch78 with communication granularity, partial-progress visibility,
  arrival-order semantics and a production failure contract, but remains Experimental and Revision-sensitive:
  the v1 text is unavailable, the public repository lacks the referenced implementation, the scaling speedup
  is not a matched Serial wall-clock metric, and backpressure/completion/cancellation are not disclosed.
  Self-Distilled Policy Gradient has now been read through its sole v1, fixed-prefix gradient proof, normalized
  and unnormalized KL derivations, one-step off-policy and omitted score-function analysis, both model-scale
  experiments, alpha/beta ablations, current implementation README, and Ch25/27-30 adjacency. It supports a
  layered design in which the verifier selects successful trajectories, privileged full-vocabulary reverse KL
  shapes local token distributions, and a fixed reference anchors drift; it does not establish independent-seed,
  compute-matched, cross-domain or erroneous-context robustness, nor isolate positive gating from the beta
  schedule. The provisional disposition is `Refine — Existing Argument / Experimental`, owner Ch29, with no
  Books edit while the Historical Books Gate remains closed.
  M3Eval has now been read through its sole v1, four cognitively inspired task constructions, dataset/question
  pipeline, model and human evaluation, all appendices, current official project/repository/dataset surfaces,
  and Ch14/22/62/73 adjacency. It gives a useful taxonomy for divided attention, interference, interleaving,
  source binding and N-Back load, but does not causally isolate a memory mechanism: visual density, frame
  sampling, position/recency, hard cuts, option calibration and source binding all change with the tasks, while
  human protocol, annotator agreement and an immutable sample/scorer revision are not disclosed or auditable.
  Ch62 and Ch22 already own the evaluation-object, slice/confound and effective-utilization principles, and Ch73
  explicitly owns cross-call persistent Agent Memory rather than model-forward working state. Its disposition is
  therefore `No Change — Already Covered / Experimental Case` / Ch62, with no Books edit.
  Continual Experience Internalization and the other eleven unreviewed families could not be read through the
  saved-access policy for their arXiv primary-paper domain; the GitHub artifact domain required by several families
  is likewise blocked. They are `Unverified / Blocked Backlog`: provisional discovery scores are retained, but
  title- or pending-focus-derived mechanisms are excluded from evidence and Books. They do not block the forward
  queue under the user-approved skip rule.
  The fixed official/Infra replay is now complete. SGLang issue #27462 was read as a current, revision-sensitive
  design roadmap rather than an event-time implementation claim. It establishes a provisional Ch44 gap around
  verifier-owned commit, versioned future buffers, safe one-token fallback, and drafter transport/liveness state;
  missing implementation, tests, PP/multi-node support, fairness, and workload/SLO evidence remain explicit.
  vLLM v0.22.1 and PR #43864 were read as a Ch46/53 stabilization case: Ray actors serialized endpoint addresses
  before bind, so the Ray path restores driver-side port allocation while the multiprocessing path retains
  bind-time allocation. Transformers GHSA-fgcw-684q-jj6r and its fix commit were read as Ch68 corrective evidence:
  untrusted LightGlue nested config could not own the caller's remote-code trust decision, and the fix combines
  registered-only config resolution with a native-integration lint rule whose dynamic coverage remains bounded.
  Datasets 5.0.0 was read as a Ch23/62 breaking version fact: Agent traces enter a common messages surface and
  streaming shuffle changes to multiple input shards, but release evidence does not establish lossless cross-runtime
  trace provenance, training benefit, or exactly-once resume. The latter three are `No Change / Weekly Only` because
  their durable contracts are already owned by Ch46/53, Ch68, and Ch23/62; the SGLang refinement remains provisional.
  The Historical Books Gate stays closed. Language Models Need Sleep is a 2025 first-public family and is
  not counted as a new W23 event. Eleven later-feed papers, including SkillHarness from the W26 display
  feed, were returned to their June 2-5 v1 dates in W23. The Historical Books Gate remains closed.

- W24 has advanced from two baseline items to thirty-eight scored families. Thirty-seven score at least
  twenty; thirty-five Full Source Reviews are complete, current-review pending is zero, and VIA-SD plus the
  Agentic Environment Engineering survey remain `Unverified / Blocked Backlog`. FastContext is kept as
  a seventeen-point withdrawn provenance record rather than mechanism evidence. MiniMax Sparse
  Attention has been read across its thirty-page paper, architecture and training equations, kernel
  design, matched 109B experiments, related work, all appendices and ablations, public repository,
  and Ch21-24/Ch39 adjacency. Its durable contribution is the joint contract among selector-gradient
  ownership, GQA-group block granularity, KV-outer execution, hot-block load balancing, and staged
  dense-to-sparse migration. The paper's H800 measurements and the current repository's SM100
  contract remain distinct evidence. Eight W23 spillbacks, one W22 spillback, one 2025 cross-year node,
  and twelve W25/W26-feed spillbacks were date-corrected. A 2026-08-13 exact-identity retry recovered full HTML
  text for twenty-nine formerly blocked families; each now records actual mechanism/evaluation boundaries rather
  than title-derived inference. The two remaining blocked identities receive no Books owner or mechanism claim.
  Under the user-approved blocked-skip rule the forward Candidate Gate passes
  and the cursor advances to W25; W24 discovery and Historical Evidence Gates stay open. The Historical Books
  Gate remains closed. The fixed official/Infra replay adds three complete reviews. KServe v0.19.0 provisionally
  refines Ch57 with a closed loop among desired spec, applied configuration, observed routing/workload state,
  LocalModel and static-LoRA reconciliation, readiness, migration, and termination; release evidence does not
  prove cross-runtime reliability or performance. AA-AgentPerf provisionally refines Ch62/66 by evolving a
  fixed-shape request benchmark into workflow-trajectory replay with tool delays, per-request SLOs, steady-state
  concurrency search, and measured accelerator power; its private test set, live revisions, vendor-tuned configs,
  and excluded CPU/network/cooling power remain explicit. NVIDIA's FP8 checkpoint-to-ONNX-Q/DQ-to-TensorRT path
  is a bounded Ch45 `No Change` case because the chapter already owns precision, graph rewrite, kernel, hardware,
  quality, and artifact-revision coupling. vLLM v0.23.0 is routed to W25 by its official June 15 release date.

- W25 has advanced from four baseline source families to thirty-five scored families. Thirty-four score at
  least twenty; thirty-two Full Source Reviews are complete, current-review pending is zero, and only
  LLM-Designed Training Environment plus MemGUI-Agent remain `Unverified / Blocked Backlog`. TokenPilot was read
  across arXiv v1, equations, both control layers, evaluation setup, baselines, ablations, limitations,
  all appendices, the current LightMem2 artifact, and Ch70-73/Ch66/cache adjacency. Its durable systems
  contribution is the joint optimization of context reduction, byte-identical prefix identity,
  recoverable full-fidelity artifacts, and delayed lifecycle eviction. Commercial token-price results
  remain bound to the disclosed model, provider metadata, benchmark, task ordering, and pricing rather
  than being generalized to GPU latency or goodput. The W26 display feed returned fourteen additional
  candidates to their W25 v1 dates. A 2026-08-13 retry recovered twenty-five complete HTML texts; each now has
  a source-grounded mechanism, evidence boundary, trade-off, owner, adjacent-chapter review, and provisional
  disposition. The old JetSpec ledger label was corrected to the paper's JetFlow title. The two blocked families
  receive no mechanism inference or Books owner. Under the user-approved blocked-skip rule the Candidate Gate
  passes and the cursor advances to
  W26. The fixed-source replay is now complete for vLLM v0.23.0, NVIDIA sync-free MoE fused kernels, and MLPerf
  Training v6.0, and the fixed-source cursor also advances to W26. vLLM's full release was reviewed as a Ch46
  version-sensitive runtime-state evolution joining pluggable KV
  specifications, multi-tier per-request offload policy, PP-aware connector handshake, scheduler accounting,
  speculative/prefix correctness, frontend/parser identity, and input hardening. The 408 commits and isolated
  vendor microbenchmarks are not treated as one architecture claim or a universal performance result. The MoE
  kernel family provisionally refines Ch21, with Ch36/45 handoffs, by joining epilogue fusion, host-sync removal,
  graphability, and configurable SM headroom for communication; its GB200 and internal end-to-end percentages
  remain bounded vendor claims. MLPerf Training v6.0 provisionally refines Ch62 by binding MoE training evidence
  to model, dataset, target quality, division, framework/system identity, and repeated-run aggregation; submitter
  statements remain separate from MLCommons rules and suite ownership. W25
  discovery and Historical Evidence Gates stay open. The Historical Books Gate remains closed.

- W26 has advanced from four baseline source families to forty scored families. Thirty-nine score
  at least twenty; thirty-seven Full Source Reviews are complete, ordinary pending is zero, and only AOHP
  plus Self-Compacting Agents remain `Unverified / Blocked Backlog`. The Agent-Native
  Memory / MemoryData paper was read across its complete HTML, four-module taxonomy, five end-to-end RQs,
  component ablations, cost analysis, conclusion, public testbed, and Ch72-74/80 adjacency. Its durable
  contribution is module-level attribution across representation/storage, extraction, retrieval/routing,
  and maintenance under workload-specific bottlenecks, not a universal winning memory architecture.
  The fixed-source replay adds two fully reviewed engineering nodes. DFlash's June 23 deployment post is
  deduplicated against the W06 algorithm paper and W16 DDTree branch: it demonstrates a training/export and
  TensorRT-LLM/vLLM/SGLang integration surface plus workload-bound latency-throughput curves, not a new algorithm
  or universal 15x claim; Ch44 is `No Change`. TensorRT 11 multi-device inference provisionally refines Ch45 by
  making distributed collectives, rank-local engine/context ownership, communicator lifetime, all-rank progress,
  support matrices, and hang semantics part of the execution-plan contract. The fixed checkpoint passes and the
  cursor advances to W27; broader discovery and Historical Evidence Gates remain open and Books stays closed.
  Seventeen display-feed spillbacks were returned to W23-W25 by arXiv v1 date, and ten W27-feed candidates
  were returned to W26 by their June 25-28 v1 dates. A 2026-08-13 exact-identity retry recovered thirty-one
  previously blocked HTML papers; each now has a non-template review covering mechanism, state ownership,
  evaluation contract, evidence boundary, limitations, adjacent chapters and provisional disposition. Among
  the durable candidates, Wan-Streamer and Multi-Block DLM provisionally add Ch38 mechanisms; Qwen-AgentWorld,
  Verification Horizon, EDV, InfoKV, Agentic Abstention, OSWorld 2.0, DiscoBench and GBC refine their respective
  Ch10/62/73/22/75/78 arguments. No Books edits are authorized before the global Historical Evidence Gate.
  The two remaining blocked families require arXiv primary-paper access; their provisional scores remain
  discovery priorities, while title-derived mechanisms are excluded from evidence.
  Under the user-approved blocked-skip rule the forward Candidate Gate passes and the cursor advances to W27;
  W26 discovery and Historical Evidence Gates stay open. The Historical Books Gate remains closed.

- W27 has advanced from nine score rows to thirty-three score rows representing thirty-two unique source
  families. Twenty-three score 25-30 and ten score 20-24. Eleven unique Full Source Reviews are complete and
  current-review pending is zero; twenty-one families are `Unverified / Blocked Backlog`. Program-as-Weights was read across the complete HTML, compiler/interpreter
  mechanism, Text-to-LoRA and prefix branches, objective/training contract, baselines, ablations,
  quantization/local execution, case studies, limitations, public SDK artifacts, and Ch25-27/55/74
  adjacency. Its durable signal is specification-to-versioned-neural-artifact compilation; single-step
  synthetic evaluation, opaque weights, compiler/interpreter coupling, and incomplete production SLOs
  prevent generalization. The fixed official/Infra replay also completes Secure Agent Workspace Reference
  Design and TensorRT Edge-LLM v0.9.0. The former provisionally refines Ch80's workspace/run lifecycle with a
  Ch68 enforcement handoff, but remains a target reference architecture and does not turn current OpenShell
  alpha/experimental state into an event-date production claim. The latter is a Ch45 version fact whose support
  matrix does not disclose a general mechanism. The blocked families require arXiv primary-paper access and, for several, GitHub
  artifact access; both domains are denied by the current saved-access policy. Their provisional scores remain
  discovery priorities, while title-derived mechanisms are excluded from evidence. Under the user-approved
  blocked-skip rule the forward Candidate Gate and fixed-source checkpoint pass and the cursor advances to W28; W27 discovery and
  Historical Evidence Gates stay open. The Historical Books Gate remains closed.

- W28 has advanced from six baseline candidates to twenty-one scored source families: ten high,
  ten medium, and one low. Seven Full Source Reviews are complete, current-review pending is zero,
  and fourteen families are `Unverified / Blocked Backlog`.
  LLM-as-a-Verifier was reviewed across the full paper, verifier decomposition, training and evaluation
  contract, ablations, limitations, and Ch62/64/65 adjacency. Its durable contribution is to separate
  criterion coverage, evidence grounding, and aggregation rather than treating a scalar reward as
  correctness. Metadata, v1 dates, scores, and owners are recorded for the remaining candidates, but their
  arXiv primary-paper domain and several required GitHub artifact surfaces are denied by the current saved-access
  policy. Those records are not full-read evidence. Under the user-approved blocked-skip rule the forward
  Candidate Gate passes and the cursor advances to W29; W28 discovery and Historical Evidence Gates stay open.
  The Historical Books Gate remains closed.

- W29 has advanced from six baseline candidates to thirty-eight scored source families: twenty-one high and
  seventeen medium. Thirty-four Full Source Reviews are complete, current-review pending is zero, and four
  families remain `Unverified / Blocked Backlog`: Multi-Agent Exploration, AI Scientist Capability,
  Generative Compilation, and LongStraw. SearchOS was
  reviewed across the full paper, SOCM shared state, schema-bound evidence extraction, continuous
  dispatch, skills and middleware, evaluation, ablations, appendices, and Ch62/72/73/76-78/80 adjacency.
  Its durable signal is explicit ownership of frontier, evidence, coverage, and failure state; its
  reported gains remain bound to the disclosed model, budget, and benchmark contracts. The other recovered
  families now have primary-text evidence and provisional dispositions rather than
  title-derived mechanisms. Under the user-approved blocked-skip rule the forward Candidate Gate passes and
  the cursor advances to W30; W29 discovery and Historical Evidence Gates stay open. The Historical Books
  Gate remains closed.

- W29 first recovered eleven unscored cross-week identities: `Training Variable Long Sequences with Data-Centric
  Parallel` (arXiv:2608.07524), whose v1 was date-deduplicated to 2026-07-14 by the 2026-08-11 Daily and whose
  metadata/full text were recovered on 2026-08-13. Eleven additional W30 attribution identities now have stable arXiv
  IDs and v1 dates from 2026-07-16 through 2026-07-19. They were written back without scores because only
  identity/date/abstract verification was initially complete. OPD² has since completed its sole-v1 paper, formulation,
  three-domain evaluation, training dynamics, ablations, H100 compute contract, appendix, official code/recipes,
  and Ch27-30/23 adjacency review. Recursive Harness Self-Improvement has also completed its sole-v1 paper,
  objective/algorithm, synthetic repository benchmark, judge/resource contract, component ablations,
  information-theoretic hypothesis, appendices, and Ch76-78/62 adjacency review. Muon Agentic RL has since completed
  its event-time v1 paper and appendices plus post-window v4 and official-repository verification, with the single-seed
  v1 claims kept separate from the later multi-seed, scale, transfer, RMS-control, and FSDP implementation evidence.
  Xiaomi-Robotics-1 has also completed its v1 model/data/training and evaluation review, with its July 22 revision and
  August 3 code/checkpoints treated as post-window verification. DSWorld has now completed its sole-v1 architecture,
  state/transition ownership, data construction, training, evaluation, limitations and appendix review; the listed
  anonymous artifact is unavailable, and the claimed `~14x` speedup versus Compiler is disputed because Table 2 reports
  335 versus 277 minutes while the approximately 14x ratio matches DeepSeek-3.2 versus DSWorld. Beyond Success Rate
  has also completed event-time v1 plus post-window v3 revision verification, including cost/refusal
  accounting, contamination controls, scaling, limitations, all appendices, and Ch62/66/68 adjacency. SeerGuard has
  completed its sole-v1 dual-stage guard, SAWM data/training, MobileSafetyBench/MobileRisk/Next-State-QA contracts,
  ablations, latency, appendices, current official artifacts and Ch68/74/77/62/10 adjacency. Environment-free API data
  has completed its 82-page event-time v1, including task synthesis, per-task/per-app simulated state,
  schema/semantic checks, judge calibration, AppWorld/OfficeBench experiments, all relevant appendices and
  Ch23/74/77/62/10 adjacency. Exact HTML recovery on 2026-08-13 additionally completed LightMem-Ego,
  AdvancedMathBench, Proxy-Guided Update Signals, Function-Aware FIM, SpectraReward, KnowAct, Oat,
  ShortOPD, PalmClaw, SEED, BadWAM, Pixels-to-States, Demystifying OPD, Byte-Exact KV Grafting,
  Harness Evolution Evaluation, Distilled RL, JoyNexus, DataFlow-Harness, and Data-Centric Parallel.
  W29 therefore has thirty-eight scored families, thirty-four Full Source Reviews, and four explicit blockers.
  OPD² scores 28/30 and provisionally refines Ch29 with teacher/base lineage delta plus an original-OPD direction
  gate; RHI scores 27/30 and provisionally refines Ch77 with trajectory-local harness search and contract/hop
  evolution; Muon Agentic RL scores 26/30 and provisionally refines Ch29 with optimizer transformation, parameter
  routing, effective update scale, regularization, and sharding as one policy-recipe identity, with Ch35/31 handoffs.
  Xiaomi-Robotics-1 scores 27/30 and provisionally refines Ch23 with an embodiment-free UMI trajectory breadth stage
  followed by embodiment/action-schema/instruction alignment, with Ch24/25/10/62 handoffs.
  DSWorld scores 27/30 and provisionally refines Ch77 with exact-execution versus learned-simulation routing,
  predicted/authoritative state separation and timeout reconciliation; Ch75/76/62/10 receive handoffs, while the
  performance headline remains disputed and no Books file changes before the Historical Evidence Gate closes.
  Cost-Aware Security Agents scores 28/30, but its workload-specific operating point, budget/tool/environment identity,
  refusal semantics, cost per valid outcome and public-benchmark contamination controls are already owned by Ch62/66/68;
  its disposition is `No Change — Already Covered / Experimental Evaluation Case`.
  SeerGuard scores 27/30 and provisionally refines Ch68 by inserting pre-execution semantic consequence prediction
  between instruction filtering and deterministic authorization, while preserving actual-environment state ownership,
  uncertainty/approval and prediction reconciliation; current artifacts are post-window verification only.
  Environment-free API data scores 29/30 and provisionally refines Ch23 with a spec-only stateful-simulation branch;
  per-app derived history, structurally accepted write responses and model judges do not replace real side-effect state,
  sampled executable calibration or final environment evaluation.
  A 2026-08-12 access recheck of Distilled RL, JoyNexus, and DataFlow-Harness could not retrieve the required
  primary full text or artifacts because the saved access policy denied those surfaces. That process checkpoint
  is superseded by the 2026-08-13 exact HTML recovery, which completed
  all three Full Source Reviews in W29. The four blockers named above still keep the broader Historical Evidence
  Gate open under the approved blocked-skip rule.
  No abstract-derived mechanism is treated as a Full Source Review.

- The historical forward sweep has now been reconciled through W32, the latest completed ISO week at the
  2026-08-12 checkpoint. W31 and W32 both have seven Daily records. The 2026-08-12 W32 process snapshot had
  24 reviews, 16 blocked families and two unscored discovery gaps; the later exact-source recovery supersedes it:
  W32 now has 44 scored families, 36 Full Source Reviews, three identity gaps and zero ordinary pending items.
  This closes only the forward cursor, not the Historical Evidence Gate. The post-forward
  backlog sweep has restarted at the earliest open week: W13 ClawKeeper and W14's two attribution-only identities
  were retried and remain unscored `Unverified / Blocked`, so the backlog cursor advances to W15. Historical Books
  Gate remains closed. The same sweep then retried W15 GameWorld and W18 ViPO / Safety Drift through their exact
  arXiv, project, repository, and title/ID discovery surfaces; the required primary paper text still did not resolve.
  W16 and W17 have no ordinary pending items, so the post-forward cursor advances to W19 without upgrading any
  blocker or opening Books Integration. W19 MolmoAct2, OpenSearch-VL, Skill1, and StraTA were then retried through
  exact arXiv and title/ID surfaces; none returned readable primary paper text. Their discovery scores remain, but
  they are still excluded from Full Source Review and Books eligibility. W20 Qwen-Image-2.0 was then retried via
  its arXiv PDF, official repository, title, and ID; the 46 MB report still has no readable primary-text surface.
  It remains 24/30 blocked, and the post-forward cursor advances to W21.
  W21 SkillsVote, LongLive-2.0, WorldKV, and QUEST were then retried through their exact HTML/PDF and title/ID
  surfaces. No complete primary paper text resolved; WorldKV and QUEST artifact surfaces remain artifact-only
  evidence. All four stay blocked and the post-forward cursor advances to W22 without opening Books Integration.
  W22's twenty-seven blocked candidates were then retried in three ordered batches through the exact arXiv HTML
  identities already recorded in the Weekly. None returned verifiable primary paper text. Their discovery scores,
  review denominator, owners, and dispositions remain unchanged; W22 stays 15/42 reviewed plus 27 blocked, and the
  post-forward cursor advances to W23 while both global gate states remain Open/Closed respectively.
  W23's twelve blocked families and the separate StreamMA v1 PDF were then retried through their exact primary
  identities; none returned readable text. Current-v2 evidence still cannot overwrite the W23 event snapshot or
  substitute for missing runnable code. W23 remains 21/33 current-version reviews plus 12 blocked and one sub-family
  gap; the post-forward cursor advances to W24 and Historical Books Integration remains closed.
  W24's thirty-one blocked identities were then retried individually. Twenty-nine exact arXiv HTML sources
  recovered and now have non-template Full Source Reviews covering mechanism, ownership, evaluation contract,
  evidence boundary, trade-offs, adjacent chapters, and provisional disposition. VIA-SD still returns no paper
  body and the Agentic Environment Engineering survey still has no verifiable primary text, so W24 is now
  35/37 reviewed plus two blocked and zero ordinary pending. The post-forward cursor advances to W25; Historical
  Evidence remains open and Historical Books Integration remains closed.
  The W25 retry then recovered twenty-five of twenty-seven exact arXiv HTML sources and completed their Full
  Source Reviews. LLM-Designed Training Environment and MemGUI-Agent remain unverified. W25 is therefore
  32/34 completed, zero ordinary pending, and two blocked; the post-forward cursor advances to W26 while the
  Historical Evidence Gate remains open and the Books Gate stays closed.
  W26 then recovered thirty-one of thirty-three exact arXiv HTML sources. AOHP and Self-Compacting Agents still
  have no verifiable primary text. All recovered papers completed non-template Full Source Reviews; W26 is now
  37/39 completed, zero ordinary pending and two blocked. The post-forward cursor advances to W27 while the
  broader Historical Evidence Gate remains open and the Books Gate stays closed.
  W27 then retried twenty-one scored blocked families plus the unscored RESOURCE2SKILL identity. Twenty scored
  papers and RESOURCE2SKILL now have readable HTML and form an explicit Full Source Review queue; AgenticSTS is
  the only scored identity still blocked. W27 remains 11/32 scored unique reviews, twenty scored plus one unscored
  recovered pending, and one scored blocked. The post-forward cursor is held at W27 and Books remains closed.
  That recovered queue has now completed non-template Full Source Review across mechanism, state/data flow,
  evaluation contract, limitations or disclosure gaps, adjacent chapters, and disposition. RESOURCE2SKILL is no
  longer unscored: its complete v1/v4 review supports 28/30 while preserving W27 ownership by v1 date. W27 is now
  34 score rows / 33 unique families, 24 high / 10 mid, 32/33 unique `20+` reviews complete, zero ordinary pending,
  and one explicit blocked family (AgenticSTS). The W27 Forward Candidate Evidence Gate passes and the cursor
  advances to W28; broader discovery/Historical Evidence Gates remain open and Historical Books stays closed.
  W28 then retried fourteen scored blocked families and seven unscored spillback identities. Eighteen primary
  texts recovered; all seven spillbacks were date-verified, scored, and fully reviewed. W28 is now thirty scored
  families (nineteen high, ten medium, one low), 27/30 Full Source Reviews, zero ordinary pending, and three
  explicit blocked families: AgentLens, UP, and Ideas Have Genomes. The Forward Candidate Evidence Gate passes
  with this backlog and the cursor remains W29. Broader Historical Evidence remains open and Books remains closed.

- W30's pre-window attribution ledger exposed fourteen declared-but-not-ingested spillbacks. Identity attribution
  is now closed: RESOURCE2SKILL is an unscored W27 identity; ReflectWorld-MM and ReOPD belong to W28;
  eleven July 16-19 papers began as unscored W29 identities. ReOPD, ReflectWorld-MM, OPD², Recursive Harness
  Self-Improvement, Muon Agentic RL, Xiaomi-Robotics-1, DSWorld, Cost-Aware Security Agents, SeerGuard, and
  Environment-free API data, Distilled RL, JoyNexus, DataFlow-Harness, and Data-Centric Parallel have since completed
  full-paper, disclosed implementation/artifact-boundary, evaluation-boundary, scoring, and adjacent-chapter reviews.
  Attribution and review evidence remain separately traceable in their owner weeks.

- W30 has advanced from eight baseline candidates to twenty-five scored source families: eleven high,
  thirteen medium, and one low. All twenty-five Full Source Reviews are complete; current-review pending and
  blocked counts are both zero.
  OpenForgeRL was reviewed across the full paper, harness/proxy/sandbox/orchestrator/policy-server
  ownership, rollout reconstruction, task synthesis, Claw and GUI contracts, cross-harness evaluation,
  limitations, and Ch28-30/62/77/78/80 adjacency. Its durable signal is that training runtime must preserve
  deployment-harness identity; coupling among synthesis, teacher, harness, RL, and evaluator prevents
  universalizing the authors' results. Exact arXiv HTML recovery on 2026-08-13 completed the remaining sixteen
  candidates across mechanism, ownership, evaluation, limitations, evolution, adjacent chapters, and disposition.
  These remain provisional Books inputs until the all-history Gate. Under the user-approved
  blocked-skip rule the forward Candidate Gate passes and the cursor advances to W31; W30 discovery and
  Historical Evidence Gates stay open. The Historical Books Gate remains closed.

- W30's fixed official/Infra checkpoint now passes after reviewing the existing Dynamo v1.3, SGLang v0.5.16,
  and Nunchaku Lite source packets and correcting an overstrong spillback claim. All fourteen pre-window titles
  now have stable owner-week attribution. At that checkpoint ReOPD and ReflectWorld-MM were reviewed and scored,
  while twelve remained unscored. Subsequent W29 reviews completed OPD², Recursive Harness Self-Improvement,
  Muon Agentic RL, Xiaomi-Robotics-1, DSWorld, Cost-Aware Security Agents, SeerGuard, Environment-free API data,
  Distilled RL, JoyNexus, DataFlow-Harness, and Data-Centric Parallel. The earlier four-item owner-week gap and
  W30's sixteen blocked reviews were closed by the 2026-08-13 exact-source checkpoint.
  W30 stays at twenty-five scored families, twenty-five reviews complete, zero blocked, and zero current-review
  pending. Its broader
  Historical Evidence Gate remains open and the Books Gate remains closed.

- Superseded W28 process snapshot: nine source identities that W29/W30 had already routed back
  to W28 were previously absent from the owner week. ABot-AgentOS, GRASP, Weak-to-Strong Direct OPD,
  What LLM Forecasters Know, PolicyShiftGuard, Root Causes, DeepSearch-World, ReflectWorld-MM, and ReOPD are
  now explicit spillbacks. Owner-week evidence and primary IDs are stable; ReOPD and ReflectWorld-MM also have
  full primary-source evidence, while incomplete reviews are not replaced with title-derived mechanisms or scores.
  At that intermediate checkpoint W28 had twenty-three scored rows and thirty unique families: nine scored reviews complete,
  fourteen scored blocked, seven unscored blocked, and zero current-review pending. ReOPD contributes a
  provisional Ch29 Experimental refinement: online OPD and teacher-prefix replay occupy different points in the
  student-occupancy / teacher-reliability trade-off, and neither universally replaces the other. ReflectWorld-MM
  provisionally refines Ch73 with perception/entity-resolver/consolidator/retrieval/rule-resolver ownership and
  identity-critical commit boundaries, without universalizing its six-benchmark headline. The Historical
  Evidence and Books Gates remained open/closed respectively. The current W28 state is the later exact-source result
  recorded above: thirty scored families, 27/30 Full Source Reviews, three explicit blockers, and zero ordinary pending.

- W31 remains a completed Live Weekly rather than a historical backfill checkpoint.
  Its seven Daily records, twenty-four score totals, links, coverage limitations,
  cross-week deduplication, Books decisions, Markdown, and focused diff check were
  revalidated on 2026-08-09. This validation does not close the W13 through W30
  historical discovery gaps.

- W32 has been rebuilt as a complete ISO-window archive with seven of seven Daily records and received a
  coverage repair on 2026-08-12. The 2026-08-09 Daily now contains ten scored source families rather than
  only Beyond Routing. Forty-eight Daily score rows normalize to forty-four unique source families. After the
  2026-08-13 exact-source recovery and owner-week correction, the current Weekly ledger contains twenty-three
  high, nineteen medium, and two low families. Thirty-six paper Full Source Reviews are complete; ElastiCo,
  OasisKV, TAOT and KServe v0.20.0 have been recovered, while PrefixPlace, xPress and Resource-Fair Scheduling
  remain three unscored identity gaps. Current Full Source Review pending is zero. Tangent
  refines Ch62 with the Benchmark / Evaluation / Testing boundary; subjective RLVR and Beyond Routing do not
  change their owner chapters. W32 Evidence Gate stays open, and the Historical Books Gate remains closed.
  Under the user-approved blocked-skip rule, the remaining identity gaps stay explicit material requests rather
  than stopping the forward cursor. With zero ordinary Full Source Review pending, the Forward Archive Checkpoint
  has reached the latest completed ISO week.
  This is not an all-history Evidence Gate or Books Gate pass; blocked sources must still be retried when access
  changes, and future Live Sunday Weekly continues independently.

- Source-family normalization has now split compressed baseline rows in W13, W15,
  W17, W23, W25, and W26 into twenty-six, four, five, five, four, and four independently scored and
  reviewed families. This separates product facts, observational studies, domain
  experiments, telemetry methodology, and research mechanisms instead of averaging
  their evidence strength. Project Fetch is now an 18-point three-trial domain fact,
  while the GPT-5.6 preview is a separate 19-point model-state fact. These ledger
  repairs improve auditability but do not close any week-level discovery gate. W13
  now has one review or boundary record for each of its forty-five scored rows and no recorded
  Full Source Review pending; its discovery-recall gate remains separate and open.
  The 2026-08-13 external retry did not change that denominator: ClawKeeper's exact arXiv HTML is blocked by
  the saved user access policy, and the OpenAlex week-window request was denied. No alternate browser or indirect
  bypass was used, and no empty result was treated as negative discovery evidence. W13 therefore remains
  45 scored, 41/41 retained reviews, four low/cross-week boundaries, one explicit blocker, and zero ordinary
  pending; its Candidate Gate passes under blocked-skip while broader Historical Evidence stays open.

- The current machine-recomputed provisional ledger contains 1073 scored rows in the
  historical W01-W30 window: 671 at 25-30, 354 at 20-24, and 48 below 20. W01-W12
  account for 407 rows; W13-W30 currently account for 666. The recount includes every
  six-dimensional scoring table in the current Weekly files, including incremental candidate tables in W27-W30;
  it corrects the stale annual subtotal rather than treating later recovered rows as prose-only additions. These
  counts replace neither
  the frozen 93-row baseline nor a completed Evidence Gate: candidate recovery and full-source
  completion are separate ledgers. Live W31 contributes 26 current score rows after ResKV and SLIM were
  returned to their 2026-07-31 owner week; W32 contributes 44 unique
  scored families with 7/7 Daily coverage. The arithmetic archive total was 1140 rows
  in the superseded pre-recovery snapshot. The current archive total is 1143 rows
  (707 high, 383 medium, 53 low), which is not a completed Evidence Gate.
  W07 has 52 score rows because SPEED-Bench was returned to its explicit 2026-02-10 v1 timestamp despite the
  anomalous `2604.*` identifier prefix. Its v1/v2 full text, measurement framework, experiments, Appendices,
  NVIDIA dataset, and Ch43-45/62 adjacency are now audited. It is `No Change — Already Covered / Experimental
  Evaluation Case`: Ch44 already owns acceptance versus end-to-end speedup, draft/verification cost, workload,
  concurrency, hardware, and capacity-aware verify length. W07 therefore has 49/49 accessible Full Source Reviews,
  one InternAgent blocked packet, and zero ordinary pending; its blocked-skip Candidate Review Checkpoint passes.
  The subsequent 2026-08-13 pass completed 52/52 Books dispositions and 16 owner-chapter integrations, so the
  W07 Source-Family Books Gate is complete while the broader Discovery/Historical Archive Gate remains open.
  W08 now has one explicit packet for each of its 23 candidates. A 2026-08-13 independent
  Books review completed 23/23 final dispositions: 18 Integrate/Refine, four No Change and one
  Weekly Only across 12 Stable Node owners. Its Source-Family Books Gate is complete while its
  Archive Completion Gate stays open for historical engineering/discovery coverage. W09's three extra
  review packets are cross-week removals, while W27's thirty-four rows intentionally map to
  thirty-three source families because Seed2.0 is duplicated across source groups.
  A 2026-08-13 continuation checkpoint then revalidated W18 through W23 directly from their current score tables.
  Later exact-source recovery supersedes the intermediate blocked counts: W18 is 86 scored with 80/80 retained
  reviews plus Safety Drift as one unscored blocker; W19 is 35 scored with 33/34 retained reviews plus StraTA as
  one blocker and one low boundary; W20 is 31 scored with 30/30 retained reviews and one low boundary; W21 is
  31 scored with 30/30 retained reviews and one low boundary; W22 is 43 scored with 42/42 retained reviews and
  one low boundary; W23 is 33 scored with 22 current-version reviews, eleven blocked families and a separate
  StreamMA v1/artifact sub-gap. All six weeks have zero ordinary pending and no score-total mismatch. W24 through W30 already carry exact-source
  recovery checkpoints dated 2026-08-13, while Live W31 and W32 retain 7/7 Daily coverage. The forward archive
  cursor therefore remains at W32; blocked sources and cross-index discovery keep Historical Evidence open and
  Historical Books closed.
  `CODEX_HISTORICAL_RESEARCH_PROMPT.md` has now been restored as the repository contract for historical discovery,
  source-family deduplication, blocked recovery, materials requests and Evidence/Books Gates.

- Historical research now has continuous Weekly coverage from 2026-W01
  through W30. W01 correctly includes 2025-12-29 through 2026-01-04 because
  ISO week-year boundaries take precedence over calendar-year truncation.
- Retrospective backfill stores evidence directly in complete Monday-Sunday
  Weekly reports and does not create historical Daily records unless a task
  explicitly requests daily reconstruction.
- The legacy high-score event Dailies for 2026-07-01, 07-06, 07-08, 07-16,
  and 07-22 were removed only after a field-by-field coverage audit confirmed
  that their candidates, mechanisms, evidence boundaries, sources, open
  questions, and Books decisions were retained in W27-W30.
- The archive contains 93 scored rows: 20 at 25-30, 60 at 20-24, and 13 below
  20 retained to make rejection boundaries explicit. The 80 retained rows
  represent 79 unique events because W27 listed the same Seed2.0 Model Card in
  two source groups.
- The 2026-07-31 Addenda and prior Books decisions were treated as provisional
  inputs rather than reading evidence. The prior admitted-candidate audit has 92 non-template
  Source Review packets covering all 93 scored rows: 20/20 high-score and
  60/60 medium-score candidates received complete primary-source review,
  13/13 low-score candidates received source/date/score/rejection checks, and
  the duplicated Seed2.0 row points to one shared source family. Those earlier
  Evidence and Books Gates passed only for the 93 candidates already present;
  they do not close the current Discovery Recall Gate for the frozen window
  ending 2026-07-26.
- Stable understanding added to Books:
  - Model/training/hardware: controlled Post-LN, router-to-dispatch coupling,
    pluggable communication contracts, asynchronous pipeline staleness, and
    workload-specific accelerator co-design.
  - Inference/runtime: adaptive speculative verification, heterogeneous cache
    identity, expert/KV locality, and distributed selection-state ownership.
  - Evaluation/governance: executable artifacts, deployment autonomy
    telemetry, privacy-preserving aggregation, policy-bound privacy sensing,
    and experimental training-state capability isolation.
  - Agent/workflow: derived memory with provenance, deterministic domain
    tools, physical experiment authority, workflow-visible serving, and
    task-topology matching for Multi-Agent systems.
- Sequential Attention and overthinking were corrected as publication-state
  events rather than new first-public mechanisms. TurboQuant is marked
  `Disputed` pending reconciliation with reproduction evidence.
- Final candidate dispositions and source families are summarized in the 2026
  Weekly index and remain traceable to candidate-level review packets. The
  audit retained validated material, refined only owner chapters with a durable
  mechanism gap, and did not convert version facts or product capability into
  undisclosed model/runtime mechanisms.
- Final cross-owner contracts now state that typed inference payload remains
  engine-owned even when distributed selection indexes it; privacy sensing,
  aggregate observability, and evidence judgment have separate owners; and
  derived Agent memory remains advisory until Workflow revalidates it against
  current tool, permission, budget, and side-effect semantics.
- No Part or chapter was added, renumbered, or promoted. The audit refined
  existing owner chapters and preserved older techniques as valid branches
  under their original constraints.
- Live W31 covers the complete Monday-Sunday window 2026-07-27 through
  2026-08-02 and links all seven retained Daily records. Cross-day review
  preserved exact-prefix and tiered KV as valid branches while adding semantic
  composition as a separate compatibility contract; it also refined Chapter
  62 from run-level evidence retention to typed claim-to-artifact provenance.
  ScientistOne remains an experimental source: its paper first appeared in
  W22, its 2026-07-30 Google Research article is the W31 publication node, and
  its systems-optimization benchmark is not generalized to autonomous science.
  Anthropic's 2026-07-28 cryptanalysis result remains Weekly-only until the
  associated domain papers receive full technical verification.
- W32 covers the full ISO window 2026-08-03 through 2026-08-09 with seven retained Daily records; the
  2026-08-09 record is explicitly marked as a retrospective recovery and 2026-08-12 coverage repair. Cross-day review preserves
  co-location and P/D as valid serving branches while adding conditional A/F cuts and full-provisioning
  accounting; it also separates tokenizer session state, recurrent context state, and durable typed memory.
  Agent workflow refinements connect typed problem compilation, causal repair, audited skill artifacts, and
  workflow-visible resource demand. Tangent adds a Benchmark / Evaluation / Testing boundary and layered
  Agent test adequacy to Ch62; the Weekly adds no duplicate Books prose. Beyond Routing adds an Experimental
  selection / execution / commitment split for Ch21 without changing Books. The other six August 9 candidates
  now have Full Source Reviews: Business Arena and PIRL are deferred cross-source refinement candidates;
  pre-pretraining, activation steering, carbon-aware fine-tuning, and AquiLLM are No Change or Emerging.
  Sixteen blocked source families and two unscored discovery-only gaps keep the W32 Evidence Gate open.

## 2025 Historical Weekly Coverage and Books Integration

Status: 2025-W01 through 2025-W52 archive completed; Books Integration complete with 1 user-approved unverified exclusion

Repository index:

`papers/2025/weekly/README.md`

Coverage and archive decisions:

- Historical research uses 52 complete ISO weeks from 2024-12-30 through
  2025-12-28. The remaining 2025 calendar days belong to ISO 2026-W01 and are
  not duplicated.
- The archive contains 75 scored evidence rows: 32 at 25-30, 41 at 20-24,
  and 2 below 20 retained only to make evidence boundaries explicit.
- Candidate-level review progress is 75/75. Full primary-source verification is
  74/75: 32/32 high-score, 40/41 medium-score, and 2/2 low-score candidates.
  This count is derived from non-template `Full Source Review` packets, not from
  prior Weekly summaries.
- The official Claude Opus 4.5 system-card PDF is locatable, but the current
  primary-source channel rejects the 11.5 MB document before full-text
  extraction. The user explicitly approved skipping it on 2026-08-01. It is
  recorded as `User-approved exclusion / Unverified`, is absent from Books, and
  does not count as full-primary-source verified.
- All 75 candidates now have a final disposition: 38 `Refine`, 13 `No Change`,
  23 `Weekly Only`, and 1 `Excluded / Unverified`.
- Historical Daily records were not fabricated. Each Weekly preserves event
  date, first-public date, source role, evidence boundary, disposition, and
  unresolved questions.
- Full-source review corrected the chronology of test-time memory: Titans v1
  belongs to W01, MIRAS v1 to W16, and the W49 Google Research article is a
  later institutional synthesis rather than the first-public event.

Stable understanding integrated after primary-source re-audit:

- Chapter 22 now preserves the long-context design branches from dense
  attention through linear/recurrent hybrids, hardware-aligned native sparse
  attention, staged DSA migration, and test-time neural memory. Each branch
  retains the older solution's valid conditions and names the new selector,
  kernel, online-state, isolation, or recovery cost.
- Chapter 29 distinguishes pure outcome-reward emergence from the cold-start,
  filtering/SFT, later-RL, and distillation stages needed for readable and
  deployable reasoning behavior.
- Chapter 44 treats speculative decoding as a target-coupled artifact
  lifecycle spanning drafter architecture, MTP integration, training/data
  production, compatibility, provenance, canarying, and rollback.
- Chapter 59 separates stable DRA core resource semantics from alpha health
  and consumable-capacity extensions, with explicit driver, scheduler,
  admission, and recovery ownership.
- Chapter 68 maps differential privacy by privacy unit and lifecycle layer:
  inference-time synthetic data, user-level fine-tuning, distributed DP
  runtime, and privacy-preserving production telemetry.
- Chapter 72 separates retrieval relevance, context sufficiency, answer
  faithfulness, confidence, and abstention as different control signals.
- Chapters 22 and 73 distinguish model-internal test-time neural memory from
  durable Agent Memory with cross-run identity and governance.
- Chapter 77 adds evaluator-driven search as a governed Workflow: candidate
  lineage, evaluation cascade, quality/diversity selection, held-out checks,
  and human deployment authority. It is not described as autonomous model
  self-improvement.
- Chapter 5 now treats a sparse feature/attribution graph as a replacement model
  with its own reconstruction, pruning, attention-path, and labeling gaps;
  readability is not identical to mechanistic completeness.
- Chapters 20 and 52 make reasoning effort/stopping policy part of the runtime
  and evaluation identity. More test-time tokens are a capacity choice, not a
  universal quality guarantee.
- Chapter 24 defines elastic training recovery as trajectory preservation across
  checkpoint, data cursor, RNG, topology, and replay, not merely process restart.
- Chapter 25 records cascade distillation as one response to teacher/student
  capacity gaps while preserving from-scratch training as a valid branch.
- Chapter 29 adds partial-rollout trajectory ownership and the resulting policy
  staleness, segment credit, masking, and recovery risks.
- Chapter 32 adds one-sided symmetric memory as a kernel-specialized layer above
  registration/order/lifetime contracts, not as a replacement for collective
  libraries.
- Chapters 38 and 45 preserve two portability trade-offs: cascade versus
  end-to-end streaming pipelines, and shared serving semantics versus
  hardware-specific compilers/kernels.
- Chapter 46 restores the V0-to-V1 vLLM control/state evolution while retaining
  V0 and PD-specialized paths under their original compatibility constraints.
- Chapter 48 distinguishes the 2025 Dynamo launch contract from later
  request/control/state-path documentation so newer interfaces are not
  back-projected into the initial release.
- Chapter 68 additionally records open-weight operator responsibility and
  policy-as-data safeguards; model verdicts remain sensors, not authorization.

The archive structure, ISO-week coverage, 75 candidate-level Source Reviews,
32 high-score primary-source audits, and 75 candidate dispositions are now
evidenced in the Weekly records. Books Integration is complete for the 74
verified candidates; Claude Opus 4.5 remains the sole explicit exclusion and
cannot support any Book claim. No Part or chapter was added, renumbered, or
promoted; later technologies were integrated as evolution branches without
silently replacing the conditions under which older designs remain valid.

## 2026-08-01 Daily Research Integration

Status: Daily primary-source review completed; three existing chapters refined

Stable understanding integrated in this pass:

- Chapter 46 now distinguishes exact prefix reuse from position-independent KV
  composition. RoPE re-rotation repairs position, not causal-context information;
  reusable KV therefore needs a semantic compatibility contract in addition to
  cache identity and transport correctness. Online repair and offline semantic
  compilation remain coexisting branches with different TTFT, training, rebuild,
  and domain-shift costs.
- Chapter 62 now separates an Agent's narrative, typed actions, observed environment
  transition, and task-specific completion evidence. Model judges and scripted
  verifiers are both fallible; success recall and failure recall must be inspected
  separately so false successes do not silently become reward or training labels.
- Chapter 78 now treats runtime topology repair as a bounded Workflow transition,
  not autonomous graph growth. Trace-triggered rewiring, verifier insertion, branch
  expansion, or serialization require topology versioning, mutation budgets,
  deterministic validation, authority transfer, and replay semantics.

SemPIC, OSReward, the accompanying benchmark audit, and MANTA remain experimental
evidence. Their author-reported benchmark values were not promoted into general
production claims. No Part or chapter was added, renumbered, or promoted.

## 2026-08-04 GEMM Kernel Refinement

Status: Official-documentation and source-code refinement completed; affected chapters remain Draft

Stable understanding integrated in this pass:

- Chapter 16 now maps Transformer Linear/MLP semantics to a verifiable GEMM
  contract by flattening `M=B*T`, defining `N` and `K`, and separating model
  shape from the library or kernel that executes it. It also explains why the
  same weights have different utilization boundaries in Training/Prefill and
  small-`M` Decode.
- Chapter 21 now treats grouped GEMM as the execution form of router-produced
  per-expert batches. It can reduce launches and padding but does not remove
  imbalance, empty experts, tail tiles, metadata or All-to-All.
- Chapter 45 now derives GEMM tiling, operand reuse, cuBLAS/cuBLASLt heuristic
  selection, Tensor Core instruction layers, TMA asynchronous movement and
  multi-stage producer-consumer pipelines before using DeepGEMM as a
  specialized implementation case.
- The instruction terminology was corrected: DeepGEMM documents `FFMA`
  interleaving, not a stable `FMMA` family. Scalar `FFMA`, PTX `mma.sync`,
  Hopper `wgmma.mma_async`, Blackwell `tcgen05.mma`, and architecture-specific
  SASS names now have separate semantic boundaries.
- DeepGEMM and cuBLAS are recorded as coexisting branches. The current
  DeepGEMM source tree includes both specialized SM90/SM100 JIT/TMA paths and a
  cuBLASLt invocation path; its historical manual post-SASS interleaving was
  removed after the project moved to compiler-provided FFMA scheduling.

No Roadmap node was added because the durable knowledge belongs to the existing
Compute horizontal path: Chapter 16 owns model-to-GEMM shape, Chapter 21 owns
router-created grouped workload, and Chapter 45 owns hardware-specific execution.
Chapter 50 remains responsible for HBM capacity rather than instruction-level
data movement. No chapter was renumbered or promoted.

## 2026-08-05 Daily Research Integration

Status: Daily primary-source review completed; two existing chapters refined

Stable understanding integrated in this pass:

- Chapter 22 now distinguishes historical access from state continuity under
  context turnover. Bounded KV provides exact active addressing, external
  retrieval preserves auditable evidence, and a fixed recurrent state can carry
  lossy computation across working-context eviction. These are layered branches,
  not replacements. Serving must separately own recurrent-state allocation,
  isolation, reset, migration and release; fixed capacity does not imply exact
  recall, unlimited positions or cross-session governance.
- Chapter 77 now separates problem compilation from candidate search. A natural-
  language infrastructure goal should first become a typed task contract covering
  decision variables, objectives, hard constraints, evaluator, budget and workload
  identity. Generated candidates remain inside that feasible region; simulation
  success still requires held-out replay, shadow/canary checks, human authority and
  rollback before production use.
- LiveMem and AtumAI remain experimental single-paper evidence. AFlex remains
  Daily-only pending source release and cross-hardware validation; its A/F
  disaggregation and DVFS results were not generalized beyond the disclosed A800,
  model, trace and SLO contract.

No Roadmap node, Part or chapter was added or renumbered.

## 2026-08-06 Daily Research Integration

Status: Daily primary-source review completed; three existing chapters refined

Stable understanding integrated in this pass:

- Chapter 13 now separates a position mechanism's real-number definition from its
  finite-precision execution contract. ALiBi's linear bias can create an implicit
  effective window when softmax terms underflow; the boundary depends on slope,
  dtype, content logits and kernel behavior. Default ALiBi remains a valid branch
  inside a tested contract, and the 2026 evidence is retained as Experimental.
- Chapter 51 now treats P/D, A/F and P/D/A/F as alternative cuts of an execution
  graph rather than a monotonic version ladder. Finer pools are justified only
  when resource-specialization, interference and control gains exceed new state or
  activation movement, queueing, synchronization and recovery costs. AFlex and
  HeteroPanacea provide complementary implementation/simulation evidence, not a
  cross-hardware default topology.
- Chapter 73 now treats Memory Write as a typed, evidence-bearing state transition
  rather than a binary Write/Hold decision. Accepted, pending and historical state
  need explicit transition and provenance semantics; a semantic memory transaction
  does not itself provide database ACID, concurrency, durability or authorization.

TAOT, Oilbird and formal verification over operational Agent data remain Daily-only
pending full Source Packets. No Roadmap node, Part or chapter was added or renumbered.

## 2026-08-07 Daily Research Integration

Status: Daily primary-source review completed; two existing chapters refined

Stable understanding integrated in this pass:

- Chapter 24 now treats optimizer choice as part of the parameterization contract.
  Functionally equivalent factorizations can follow different trajectories under
  coordinate-wise preconditioning because the optimizer state depends on the
  chosen basis. Gauge equivariance is a necessary condition for transferring some
  implicit-bias arguments, not a universal proof of better generalization or a
  reason to replace Adam in LLM training. Symmetry-twin tests are retained as a
  bounded engineering diagnostic.
- Chapter 51 now requires local Attention/FFN acceleration to pass a complete,
  same-contract deployment ledger. A pure FFN pool removes devices from resident
  request/KV capacity, creating a request-bearing-capacity tax that local kernel,
  MFU or batch gains must repay. Architecture decisions compare independently
  optimized feasible plans under the same workload, SLO, budget, catalog and
  runtime capabilities; prediction near-ties require replay, canary and telemetry.
- Argus was reviewed against Chapters 76–78 and did not change the Book. Its
  durable workspace, bounded missions, review gate, event log, rollback and
  operator escalation are already owned by Chapter 77's Workflow control-plane
  argument. KServe v0.20.0 and Dynamo v1.3.1 remain version/source-family evidence
  pending Weekly integration or are already covered by existing failure semantics.

AFD-Ledger and the optimizer-basis paper remain Experimental single-preprint
evidence. No Roadmap node, Part or chapter was added or renumbered.

## 2026-08-08 Daily Research Integration

Status: Daily primary-source review completed; two existing chapters refined

Stable understanding integrated in this pass:

- Chapter 76 now separates outcome scoring from failure localization. Long-horizon
  repair needs an evidence-backed earliest critical step, bounded root-cause
  attribution, a repair directive, and an explicit resume/replay gate. Frozen-trace
  audit cannot recover unrecorded environment state, and a single-cause schema can
  hide co-causal failures; human review and online state reconciliation therefore
  remain part of the production boundary.
- Chapter 80 now treats reusable Agent Skills as mixed-modality, versioned assets.
  Expression, Implementation and Operational traces provide complementary
  provenance evidence, but same-function similarity and LLM-extracted operational
  graphs only create review queues, not automatic legal or security verdicts.
- Chapter 80 also makes workflow shape part of Agent resource scheduling. LLM,
  orchestration, tool and waiting phases create bursty CPU-GPU demand; harvesting,
  model-residency consolidation and role-aware core affinity are conditional
  branches whose safety depends on headroom, prefetch/swap cost, locality and tail
  SLO. They do not replace Chapter 59's slower Pod/gang/device placement.

SearchAuditor, SkillTrace and the Agent-workflow architecture study remain
Experimental single-preprint evidence. Their reported audit accuracy, similarity
scores, throughput and utilization results were not promoted to general production
claims. No Roadmap node, Part or chapter was added or renumbered.

## 2026-08-13 Daily Research Integration

Status: Daily primary-source review completed; three existing chapters refined

Stable understanding integrated in this pass:

- Chapter 70 now treats long-lived Prompt and procedural Skill maintenance as a
  reversibility problem. An instruction needs scope, rationale, observed outcome and
  falsification evidence before later maintainers can safely delete it. Typed contract
  consolidation may remove repeated expression while retaining rare guards, but a
  structural coverage guarantee does not prove behavioral equivalence across models,
  tasks or decoding settings; regression and canary remain authoritative.
- Chapter 73 now makes provenance an online control signal rather than only post-hoc
  audit metadata. Hard authorization, graded path trust and action-risk evidence gates
  are separate decisions. Once a faulty memory propagates, persistent-state disposition
  and execution-trace disposition must also be separated so independently supported
  work can be preserved while affected, answer-relevant computation is selectively
  replayed. This cannot undo irreversible external side effects.
- Chapter 77 now distinguishes branch-local hypotheses from environment-wide execution
  constraints in evaluator-driven search. A shared constraint registry accepts only
  observable, reproducible, environment-versioned failures or fixes; search budget is
  phase-aware, and uncertainty-guided selection is one conditional branch rather than a
  universal search policy.

Catastrophic Remembering, SkillZip, MAP-Graph, Dependency-Guided Rollback Repair and
Recovering Wasted Compute in Autoresearch Agents remain Experimental arXiv v1 evidence.
Their repository, compression, memory-safety, recovery and tabular-search results were
not promoted to universal production claims. No Roadmap node, Part or chapter was added
or renumbered.

## 2026-08-14 Daily Research Integration

Status: Daily primary-source review completed; four existing chapters refined

Stable understanding integrated in this pass:

- Chapter 26 now distinguishes explicit-future, joint-generation and direct-policy
  World Action Models. A latent predictive interface can move future reasoning out of
  the deployment pixel-rollout path, but Future-KV and dynamics registers remain
  observation/version-bound derived state; training supervision does not prove causal
  or control-sufficient dynamics.
- Chapter 75 now treats Context compression as a per-information-type preservation
  contract. Temporal anchors, exceptions, identifiers and provenance can fail
  independently of aggregate answer quality, so protected fields, source links and
  slice tests must be explicit rather than delegated to a generic gist prompt.
- Chapter 81 now separates retained candidate objects from authoritative Workflow
  activation. Only a commit against an exact predecessor, pre-state authority,
  freshness and unique effect identity may advance the run head; bounded protocol
  verification does not replace physical storage and external-side-effect evidence.
- Chapter 84 now evaluates Skill marginal utility from paired execution evidence and
  separates artifact mismatch, environment mutation, induced procedure and repeated
  Context cost. Reusable guidance remains advisory until compatibility, budget and
  canary Gates grant scoped authority.

ForeWAM, The Sleeping Agent, Beyond Memory and Agent Skills Can Be Harmful remain
Experimental arXiv v1 evidence. Their LIBERO, LoCoMo, bounded-state and Skill benchmark
results were not promoted to general production claims. No Roadmap node, Part or
chapter was added or renumbered.

## 2026-08-14 W16 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Archive Completion Gate open; cursor advances to W17

W16 now has 42/42 final dispositions: 23 Refine, 14 No Change, three Weekly Only,
one Emerging roadmap and one Disputed paper. The 23 refinements were consolidated into
12 Stable Node owners rather than appended as paper summaries. The durable routes added
or strengthened are: heterogeneous-feedback memory extraction and target-gated memory
transfer; simulator-as-measurement-subject and exploration/exploitation diagnosis;
read-only trajectory aggregation and bounded test-time scaling; on-policy distillation
state coverage, privileged trajectory projection and outcome-gated reward shaping;
dynamic update-subspace and expanded adapter artifact contracts; corpus-to-navigation;
durable engineering artifacts and derived trace trees; document-level KV packets; and
workflow hints as non-authoritative routing/cache inputs.

DDTree's existing Ch24 integration was independently revalidated. Lightning OPD remains
Disputed and was not written to Books. Gemini Robotics-ER, GPT-Rosalind and Megatron
remain product/release facts; the SGLang roadmap remains Emerging. No Part, chapter or
Stable Node was added or renumbered. The active weekly Books cursor is W17.

## 2026-08-14 W17 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Archive Completion Gate open; cursor advances to W18

W17 now has 22/22 final dispositions: 13 Refine, four No Change, four Weekly Only and
one Emerging conceptual paper. Eight Stable Node owners were changed. Evaluation now
connects generated executable environments, repeated-run reliability, active evidence-
acquiring judges, living-world mutation identity and epistemic claim-evidence-test-update
graphs without treating any model judge or simulator as truth. Training preserves a
frozen held-out boundary while allowing environment-policy curriculum co-evolution.
Inference records early-exit KV completeness before FLOPs claims. Agent chapters add
governed scaffold/fix artifacts, budget-aware recovery, typed Skill admission, capability-
substrate identity separation and query-conditioned emphasis without deletion.

KServe RC remains a pre-release fact; Last Harness remains conceptual; River-LLM remains
Experimental and contributes no benchmark constant. ReasoningBank, Privacy Filter,
Chat2Workflow and Agentic World Modeling were chapter-level No Change decisions. No Part,
chapter or Stable Node was added or renumbered. The active weekly Books cursor is W18.

## 2026-08-14 W18 Books Integration Checkpoint

Status: scored Source-Family Books Gate complete; Historical Archive/Discovery Gate open; cursor advances to W19

W18 now has final dispositions for all 86 scored families: 56 Refine, 21 No Change,
seven Weekly Only and two Disputed. The 56 refinements were revalidated against 30 Stable
Node owners. They are already represented in the current Books as mechanism-level routes,
including latent communication, data/environment curricula, policy-relative distillation,
multimodal generation and world-action boundaries, PP/SP execution contracts, target/draft
versioning, routing and output-length state, Kubernetes desired/observed/applied generations,
policy-as-data, retrieval representation identity, and workflow/artifact authority. This
checkpoint therefore avoids duplicating paper summaries and records the exact owner matrix
in W18 instead.

Safety Drift After Fine-Tuning remains an unscored `Unverified / Blocked / No Books Change`
family. DV-World and Tuna-2 remain Disputed. The archive/discovery Gate stays open for that
blocker and cross-index reconciliation, but it no longer blocks completed source families
from Books review. No Part, chapter or Stable Node was added or renumbered. The active
weekly Books cursor is W19.

## 2026-08-14 W19 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Historical Archive/Discovery Gate open; cursor advances to W20

W19 now has 35/35 final dispositions: 25 Refine, six No Change, three Weekly Only and one
Unverified / Blocked family. Nineteen Stable Node owners were changed or revalidated. The
durable additions are objective-shaped MoE modularity and versioned expert subsets; hybrid-
block Prefill token-state propagation; fresh versus cross-round claim assurance; explicit
unknown-current Memory adjudication; Kubernetes bootstrap validation and server-acknowledged
state partitioning; and collective telemetry that moves from periodic aggregates to bounded
verbose drill-down. MolmoAct2's earlier Ch26 Gate is included in this weekly result.

ARIS, UniPrefill, EMO, STALE and the Kubernetes/NCCL families retain their primary-source
proof boundaries. Product/release facts were not promoted into hidden mechanisms, disputed
Geometry Conflict numbers were excluded, and author benchmarks were not generalized.
StraTA remains `Unverified / Blocked / No Books Change`; cross-index discovery remains an
archive backlog. No Part, chapter or Stable Node was added or renumbered. The active weekly
Books cursor is W20.

## 2026-08-14 W20 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Historical Archive/Discovery Gate open; cursor advances to W21

W20 now has 31/31 final dispositions: 25 Refine, four No Change and two Weekly Only.
Fifteen Stable Node owners were changed or revalidated; thirteen own Refine decisions. The
durable additions are adapter policy-revision lifecycle; PSI pressure evidence separated
from utilization; telemetry, health and attestation separated as evidence layers; workload-
snapshot and atomic group scheduling; end-to-end supply-chain response; and purpose-limited
cross-session safety state. Qwen-Image-2.0's prior Ch23 Gate is included in this result.

Experimental model, reward, memory and harness papers retain their workload, artifact and
evaluator boundaries. HarnessAudit accounting conflicts, AntiSD optimizer-step ratios and
NVIDIA performance/economic claims were not generalized. Cross-index discovery remains an
archive backlog, but there are no blocked or pending W20 Source Families. No Part, chapter
or Stable Node was added or renumbered. The active weekly Books cursor is W21.

## 2026-08-14 W21 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Historical Archive/Discovery Gate open; cursor advances to W22

W21 now has 31/31 final dispositions: 22 Refine, six No Change and three Weekly Only
or Record Only. Seventeen Stable Node owners were changed or revalidated. Durable additions
include two-timescale recurrence; zero-route post-trained MoE compute control; attention-
distortion-aware and selectively promoted KV precision; phase-aware Prefill/Decode precision;
verifier-first task synthesis; layered content provenance; Skill pre-admission; and topology-
segment scheduling. WorldKV's earlier Ch25 Gate is included in the weekly result.

Exploit evaluation, PlanningBench, Foundation Protocol and the NVIDIA evaluation guide were
concrete chapter-level No Change decisions. Scientific milestones and patch/reference facts
remain Weekly Only. All author results retain hardware, model, precision, artifact and SLO
boundaries; simulation and revision-sensitive claims were not generalized. Cross-index
discovery remains an archive backlog, but W21 has no blocked or pending Source Family. No Part,
chapter or Stable Node was added or renumbered. The active weekly Books cursor is W22.

## 2026-08-14 W22 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Historical Archive/Discovery Gate open; cursor advances to W23

W22 now has 43/43 final dispositions: 38 Refine, three No Change and two Weekly Only. All 42 retained
families have current-version Full Source Reviews; the 27 old access blockers were recovered and no longer
remain blocked. Seventeen Stable Node owners were changed or revalidated. Durable refinements cover
multi-agent world-state ownership, stubborn-token parametric recall, heterogeneous native retrieval,
counterfactual Memory diagnosis, separate architecture and training-distribution branches for parallel
drafting, compatibility-gated execution snapshots, an independent DPU security plane, Skill updater versus
consumer-benefit measurement, and digital-twin promotion through real-cluster evidence.

Zero-trust aggregation, ScientistOne and STAC-AI are concrete No Change decisions. Social-science usage and
Rosalind access policy remain Weekly Only. Vendor performance claims and author experiments retain their
workload contracts. No Part, chapter or Stable Node was added or renumbered. The active weekly Books cursor
is W23.

## 2026-08-14 W23 Books Integration Checkpoint

Status: Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; cursor advances to W24

W23 now has 33/33 final dispositions: ten Refine, seven No Change, four Weekly Only, one Emerging /
Revision-sensitive and eleven Unverified / Blocked. The reviewed source families add or revalidate a shared-interface
but separate-owner world/action model, repository-derived adapters, recoverable harness bookkeeping, autoregressive
KV-quantization feedback, cumulative planning constraints, reward-hacking onset evidence and a decoupled speculative
commit protocol. StreamMA v2 was not used to overwrite its missing v1 event snapshot or runnable artifact.

The eleven blocked families receive no Books owner or mechanism inference. PEFT/MinT, Dreaming, Agentic RAG,
AutoLab, M3Eval, the vLLM patch and LightGlue are concrete No Change decisions; product/domain and breaking-version
facts remain Weekly Only. No Part, chapter or Stable Node was added or renumbered. The active Books cursor is W24.

## 2026-08-14 W24 Books Integration Checkpoint

Status: Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; cursor advances to W25

W24 completed 38/38 dispositions: 25 Refine, nine No Change, one Weekly Only, one Emerging, one Withdrawn and
one Unverified / Blocked. The stable knowledge tree gained no new node; six existing owners were materially
refined: `MODEL-LONG-CONTEXT`, `TRAIN-GRPO`, `INFER-SPECULATIVE-DECODING`, `PLATFORM-KSERVE`,
`PLATFORM-EVALUATION-SYSTEM` and `AGENT-PLATFORM`.

The retained lesson is an evolution chain rather than a version list: selection semantics require explicit gradient
and execution ownership; speculation can add an intermediate verifier only with transactional rollback; RL constraints
and counterfactual branching solve different credit problems; declarative serving needs desired/applied/observed state;
Agent capacity is trajectory- and SLO-shaped; and note-to-Skill compilation must preserve evidence status and execution
authority. Archive closure remains open for one blocked family and cross-index recall. The active Books cursor is W25.

## 2026-08-14 W25 Books Integration Checkpoint

Status: Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; cursor advances to W26

W25 completed 35/35 dispositions: 24 Refine, seven No Change, one Weekly Only, one Emerging and two Unverified /
Blocked. The stable knowledge tree did not change. Six owners were materially refined: `AGENT-CONTEXT`,
`INFER-VLLM`, `MODEL-MOE`, `PLATFORM-EVALUATION-SYSTEM`, `PLATFORM-SECURITY` and `AGENT-PLATFORM`;
the prior W25 World Model Source-Family integration remains valid.

The durable evolution is from token-count-only Context control to cache-aware lifecycle; from a monolithic runtime
release to typed request-state owners; from grouped expert execution to fusion with communication headroom; from
step-time benchmarks to convergence contracts; from utility-only Memory to ACL/forgetting; and from transcript-only
runs to typed Sessions. Two blocked families remain archive backlog and were not inferred into Books. Cursor: W26.

## 2026-08-14 W26 Books Integration Checkpoint

Status: Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; cursor advances to W27

W26 completed 40/40 dispositions: 30 Refine, seven No Change, one Weekly Only and two Unverified / Blocked.
The stable tree did not change. Material refinements landed in `AGENT-MEMORY`, `INFER-TENSORRT-LLM`,
`MULTIMODAL-GENERATIVE-PARADIGMS` and `PLATFORM-EVALUATION-SYSTEM`; earlier Qwen-AgentWorld and
Multi-Block Diffusion Source-Family integration remains valid.

The durable chain is module-attributed Memory rather than monolithic scores; graph-native collective execution with
explicit group progress rather than “multi-GPU” as a flag; state-preserving multimodal overlap rather than unowned
pipeline latency; and dynamic checkpoint evidence rather than final pass/fail alone. Two inaccessible papers remain
archive backlog and were not inferred into Books. Cursor: W27.

## 2026-08-14 W27 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Historical Archive/Discovery Gate open; cursor advances to W28

W27 completed 34/34 score-row and 33/33 unique-family dispositions: 21 Refine, seven No Change and five Weekly
Only, with one duplicate Seed2.0 row explicitly linked to its owner family. All unique `20+` families have current-
version Full Source Reviews; none remains blocked, pending or Disputed.

Durable refinements landed in `TRAIN-LORA`, `PLATFORM-EVALUATION-SYSTEM`, `AGENT-MEMORY` and
`AGENT-PLATFORM`: specification-compiled neural program artifacts; bounded typed Memory visibility; resource/trace-
to-Skill admission; long-lived secure workspace lifecycle; reference-artifact replay; and dense proxy/return alignment.
The existing asynchronous Pipeline Parallel and ELDR arguments were revalidated without duplicating paper summaries.
No Part, chapter or Stable Node was added or renumbered. Cursor: W28.

## 2026-08-14 W28 Books Integration Checkpoint

Status: Source-Family Books Gate complete under blocked-skip; Historical Archive/Discovery Gate open; cursor advances to W29

W28 completed 30/30 dispositions: 18 Refine, six No Change, two Weekly Only, one Emerging and three Unverified /
Blocked. All 27 accessible families have current-version Full Source Reviews; the three blocked identities receive no
mechanism inference or Books owner.

Durable refinements landed in `TRAIN-SFT`, `AGENT-MEMORY`, `PLATFORM-TRACE` and `AGENT-WORKFLOW`: replayed-
prefix distillation and relative-policy-shift transfer; entity-resolved longitudinal memory; immutable-trace-derived
root-cause graphs; and offline-world-to-live-promotion boundaries. Existing J-space, DSpark, PyTorch, GRAM, KV and
Attention arguments were revalidated without duplicating source summaries. No Part, chapter or Stable Node changed.
Cursor: W29.

## 2026-08-14 W29 Books Integration Checkpoint

Status: Source-Family Books Gate complete under blocked-skip; Historical Archive/Discovery Gate open; cursor advances to W30

W29 completed 38/38 dispositions: 22 Refine, nine No Change, two Weekly Only, one Disputed and four Unverified /
Blocked. All 34 accessible families have current-version Full Source Reviews; blocked identities receive no mechanism
inference or owner.

Durable refinements landed in `TRAIN-GRPO`, `TRAIN-DISTRIBUTED-TRAINING`, `PLATFORM-SECURITY` and
`AGENT-WORKFLOW`: matched-base policy-delta and optimizer/sharding recipe identity; adjacent-revision Harness search;
semantic-consequence sensor versus deterministic authority and actual-state reconciliation; and batch-driven parallel-plan
selection under training invariants. K3 and Xiaomi-Robotics-1 integration was revalidated. No structural node changed.
Cursor: W30.

## 2026-08-14 W30 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Historical Archive/Discovery Gate open; historical cursor advances to W31

W30 completed 25/25 dispositions: 17 Refine, three No Change, three Weekly Only, one Emerging and one Disputed.
All 25 families have current-version Full Source Reviews; none remains blocked or pending.

Durable additions landed in `PLATFORM-SECURITY` and `AGENT-RAG`: layered protection/detection/recovery for Agent
self-state, and set-level evidence utility over coverage, redundancy, conflict and complementarity. Existing Dynamo,
SGLang, HiKV and Native Multimodal integration was revalidated without copying release or benchmark claims. No
structural node changed. Historical W01-W30 weekly Books cursor is complete; next review starts at W31.

## 2026-08-14 W31 Books Integration Checkpoint

Status: Source-Family Books Gate complete; Archive/Discovery Gate open; cursor advances to W32

W31 completed 26/26 final dispositions: 14 Refine, seven No Change and five Weekly Only, with no blocked,
pending or Disputed family. `INFER-KV-CACHE` now distinguishes exact main state from approximate residual state
under a fixed budget; `INFER-SCHEDULING` now connects saturation-aware analytical capacity modeling to versioned
calibration, online observation and silicon canary validation. Existing ScientistOne, Kimi K3, MCP, vLLM and Agent
integrations were revalidated without duplicating source summaries. No Part, chapter or Stable Node changed. Cursor: W32.

## 2026-08-14 W32 Books Integration Checkpoint

Status: Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; W19-W32 Books cursor complete

W32 completed 44/44 final dispositions: 24 Refine, seven No Change, five Emerging, three Unverified / Blocked
Identity, three Weekly Only Version Facts and two low-score / pre-release boundaries; Review Pending is zero. The
three identity gaps receive no mechanism inference or owner.

Material refinements landed in `MODEL-MOE`, `TRAIN-GRPO`, `INFER-SPECULATIVE-DECODING`, `INFER-VLLM`,
`PLATFORM-GPU-SCHEDULER`, `PLATFORM-EVALUATION-SYSTEM`, `PLATFORM-SECURITY`, `AGENT-MEMORY` and
`AGENT-PLANNING`. They preserve the old branches while adding topology-aware replica placement, semantic draft
retrieval, state-matched distillation and prompt-robust reward, sparse off-HBM KV prefetch, elastic job portfolios,
stateful counterfactual evaluation, bounded formal verification/safe commit, dependency-localized Memory updates,
search-derived Skill gates and project-to-task compilation. No Part, chapter or Stable Node changed.

## 2026-08-14 Books Coherence Review — Navigation and Part I

Status: Navigation baseline complete; Part I Gate passed; Part II is next

The Books tree now has a reader-facing root index and one Part guide per Part. The guides define each Part's
question, entry assumptions, evolution spine, chapter ownership and exit contract without creating new knowledge
nodes. Four byte-identical Part VII copy files were removed after hash and reference verification; the canonical 84
chapters and 84 unique Stable Knowledge Node IDs remain unchanged.

Part I was read sequentially together with the Ch10→Ch11 boundary. Its ten chapter dispositions are:

| Chapter | Disposition | Review result |
| --- | --- | --- |
| Ch1 | Refine — Local Flow | Restored the missing Part III step in the full-book route. |
| Ch2 | No Change — Explicitly Verified | Owns capability-paradigm history, not platform/runtime history. |
| Ch3 | No Change — Explicitly Verified | Owns the global responsibility tree and horizontal primitives. |
| Ch4 | No Change — Explicitly Verified | Cleanly hands optimization to representation. |
| Ch5 | No Change — Explicitly Verified | Connects learned representation to scalable architecture. |
| Ch6 | No Change — Explicitly Verified | Preserves Transformer gains and the bottlenecks created by success. |
| Ch7 | No Change — Explicitly Verified | Treats Scaling Law as conditional evidence, not a capability guarantee. |
| Ch8 | No Change — Explicitly Verified | Separates operational capability from reliability and full Agent systems. |
| Ch9 | Refine — Local Flow | Corrected the post-ADR Part mapping to Part IV→V→VI→VII. |
| Ch10 | No Change — Explicitly Verified | Remains constraint-driven scenario analysis with a direct Part II handoff. |

The Structure Gate rejected merging Ch2, Ch9 and Ch10: they separately own capability history, engineering-system
history and future constraint analysis, and their input/output contracts remain independent. Part I has no mechanism
headings after Review notes, no heading jumps or unclosed fences, and its transition into Part II is explicit.

## 2026-08-14 Books Coherence Review — Part II

Status: Part II Gate passed; Part III is next

Part II was read as a generation spine followed by two orthogonal capacity branches. Its twelve chapter dispositions
are:

| Chapter | Disposition | Review result |
| --- | --- | --- |
| Ch11 | No Change — Explicitly Verified | Establishes the text-to-token protocol and separates incremental tokenization from KV reuse. |
| Ch12 | No Change — Explicitly Verified | Owns trainable token coordinates; hashed lexical capacity remains a bounded branch. |
| Ch13 | No Change — Explicitly Verified | Preserves the absolute→relative→RoPE route and numeric execution boundary. |
| Ch14 | No Change — Explicitly Verified | Derives Q/K/V before placing FlashAttention in the execution layer. |
| Ch15 | No Change — Explicitly Verified | Connects multi-head representation to MQA/GQA state capacity and sharding. |
| Ch16 | No Change — Explicitly Verified | Owns dense per-token transformation and hands conditional compute to Ch21. |
| Ch17 | No Change — Explicitly Verified | Preserves Post-Norm, Pre-Norm and controlled/depth-routed alternatives without declaring a universal replacement. |
| Ch18 | No Change — Explicitly Verified | Owns causal Decoder semantics and keeps latent reasoning state distinct from visible CoT. |
| Ch19 | Refine — Local Flow | Moved the general limits of KV Cache before the depth-wise-sharing special case. |
| Ch20 | No Change — Explicitly Verified | Keeps decoding distribution, budget policy and selection evidence in one output-control route. |
| Ch21 | No Change — Explicitly Verified | Owns the parameter-capacity branch; router, placement and communication remain layered rather than conflated. |
| Ch22 | Refine — Local Flow | Repaired a displaced recurrent-state sentence and restored the exact-state→compressed-state→governed-state progression. |

The Structure Gate kept all twelve nodes. Ch21 and Ch22 are long, but they own distinct parameter- and sequence-
capacity questions and each still has a single exit contract; splitting would duplicate the joint constraint tables and
state boundaries. Ch19 remains model-state semantics while Ch45 owns runtime lifecycle. Part II has no mechanism
headings after Review notes, no heading jumps or unclosed fences, and Ch22 explicitly hands representation identity
to Part III before Training begins.

## 2026-08-14 Books Coherence Review — Part III

Status: Part III Gate passed; Part IV is next

Part III was read as one continuous expansion of state responsibility: representation identity becomes mutable
generation state, then action-conditioned world state, and finally physical control with irreversible effects. Its four
chapter dispositions are:

| Chapter | Disposition | Review result |
| --- | --- | --- |
| Ch23 | No Change — Explicitly Verified | Owns modality, coordinate and artifact identity before any generative or control semantics. |
| Ch24 | Refine — Local Flow | Restored the Plan→Generate→Validate→Retry mechanism to the main argument before failure modes; Review notes now remain evidence-only. |
| Ch25 | No Change — Explicitly Verified | Separates video generation, predictive dynamics and controllable persistent world state. |
| Ch26 | No Change — Explicitly Verified | Owns action authority, freshness, controller boundaries, sim-to-real evidence and physical safety. |

The Structure Gate kept all four nodes: each expands a distinct state contract and hands a concrete unresolved
constraint to the next. Adding or merging a chapter would either duplicate representation/generation semantics or
collapse reversible model state with irreversible environment action. Part III has no mechanism headings after Review
notes, no heading jumps or unclosed fences, and Ch26 explicitly hands capability semantics to Ch27 Data as the first
Training System input.

## 2026-08-14 Books Coherence Review — Part IV

Status: Part IV Gate passed; Part V is next

Part IV was read as two connected halves: Ch27–34 decide what behavior is optimized, while Ch35–41 make the
resulting state recoverable and executable across devices. Its fifteen chapter dispositions are:

| Chapter | Disposition | Review result |
| --- | --- | --- |
| Ch27 | No Change — Explicitly Verified | Owns governed acquisition, mixture, lineage and contamination before any objective consumes data. |
| Ch28 | No Change — Explicitly Verified | Owns the base objective, optimizer trajectory, precision and training-budget contract. |
| Ch29 | No Change — Explicitly Verified | Narrows the learned distribution to demonstrations and preserves distillation/scaffold boundaries. |
| Ch30 | Refine — Local Flow | Corrected the dynamic-adapter handoff: execution belongs to Part V and governance to Part VI. |
| Ch31 | No Change — Explicitly Verified | Defines preference/reward production and hands distinct optimization branches to PPO, GRPO and DPO. |
| Ch32 | No Change — Explicitly Verified | Owns value-based on-policy advantage and clipped update mechanics. |
| Ch33 | Refine — Rebuild Spine | Rebuilt the 1100-line chapter into estimator/reward, objective artifact, stateful rollout service and typed-trajectory layers; restored three mechanism sections from Review notes and expanded the title/intent to match its actual owner. |
| Ch34 | No Change — Explicitly Verified | Owns offline pairwise policy/reference margins and cleanly closes preference optimization. |
| Ch35 | No Change — Explicitly Verified | Converts parameter change into a transactional, reshardable and deployable state artifact. |
| Ch36 | No Change — Explicitly Verified | Owns communication semantics and the common cost/invariant model for distributed training. |
| Ch37 | No Change — Explicitly Verified | Owns intra-layer operator partition and its collective boundary. |
| Ch38 | No Change — Explicitly Verified | Owns depth partition, micro-batch scheduling, bubble and parameter-version trade-offs. |
| Ch39 | Refine — Local Flow | Moved CPU-authoritative layer streaming from the evidence appendix into the Offload evolution where its old/new coexistence boundary is readable. |
| Ch40 | No Change — Explicitly Verified | Uses Megatron as a bounded case for multi-dimensional process-group and schedule composition, not as a product feature list. |
| Ch41 | No Change — Explicitly Verified | Uses DeepSpeed as a bounded case for executable state/offload policy and closes on a validated deployment artifact. |

The Structure Gate rejected splitting Ch33 after its spine rebuild: every retained branch changes the identity,
admission, credit or update compatibility of a GRPO trajectory, so a second owner would duplicate the same correctness
contract. It also rejected merging Ch40 and Ch41: process-group composition and state/offload lifecycle have distinct
inputs and failure modes despite framework overlap. Part IV has no mechanism headings after Review notes, no heading
jumps or unclosed fences, and Ch41 hands a validated artifact—not a training shard layout—to Ch42 request execution.

## 2026-08-14 Books Coherence Review — Part V

Status: Part V Gate passed; Part VI is next

Part V was read as one request-state expansion: a validated artifact enters Prefill/Decode, acquires KV and iteration
state, then crosses engine, worker and declarative-topology boundaries before SLO scheduling closes the loop. Its
fifteen chapter dispositions are:

| Chapter | Disposition | Review result |
| --- | --- | --- |
| Ch42 | No Change — Explicitly Verified | Owns the end-to-end request state machine and metric time boundaries. |
| Ch43 | Refine — Local Flow | Moved hierarchical sparse indexing from Review notes into the discovery→flat index→hierarchical index evolution, with its visible error budget. |
| Ch44 | No Change — Explicitly Verified | Owns autoregressive iteration semantics, cadence and the transition to persistent KV state. |
| Ch45 | No Change — Explicitly Verified | Owns KV capacity, identity, lifecycle, approximation and recovery rather than model-side cache semantics. |
| Ch46 | No Change — Explicitly Verified | Evolves static batches into token-budgeted iterations with explicit preemption and verify work. |
| Ch47 | No Change — Explicitly Verified | Owns logical-to-physical KV block mapping and copy-on-write, not the whole serving engine. |
| Ch48 | No Change — Explicitly Verified | Preserves exact verification, governed draft artifacts, rollback and workload-dependent proposal branches. |
| Ch49 | Refine — Local Flow | Restored population-based kernel search to learned-kernel admission before portability/build-time, keeping the archive as auditable experiment state. |
| Ch50 | No Change — Explicitly Verified | Uses vLLM as a bounded single-engine lifecycle case after batching and paging are already derived. |
| Ch51 | No Change — Explicitly Verified | Owns structured-prefix and reusable-program state, with SGLang only as the implementation case. |
| Ch52 | No Change — Explicitly Verified | Expands request/control/state paths across workers and separates transfer substrate from routing policy. |
| Ch53 | No Change — Explicitly Verified | Owns declarative LLM topology and reconciliation, not GPU execution or general platform governance. |
| Ch54 | No Change — Explicitly Verified | Reconciles fixed, dynamic and transient HBM consumers before any placement decision. |
| Ch55 | No Change — Explicitly Verified | Treats P/D and further specialization as conditional split branches with transfer, failure and fleet-accounting costs. |
| Ch56 | No Change — Explicitly Verified | Closes admission, iteration, placement and autoscaling across distinct time scales and hands contracts to Part VI. |

The Structure Gate kept all fifteen nodes. Ch49 is long but owns one execution-plan question from operator semantics
through kernel admission and hardware mapping; splitting by library would recreate a product catalogue. Ch50–53 each
change a different state boundary—engine, structured runtime, distributed runtime and declarative topology—so their
framework names remain bounded cases rather than chapter taxonomy. Part V has no mechanism headings after Review
notes, no heading jumps or unclosed fences, and Ch56 explicitly hands identity, resource and evidence contracts to
Ch57 instead of treating cluster scheduling as a slower token scheduler.

## 2026-08-14 Books Coherence Review — Part VI

Status: Part VI Gate passed; Part VII is next

Part VI was read as the conversion of inference contracts into an operable platform: artifact and workload identity
enter deployment and resource control, become observable evidence, and finally support cost, tenancy, security and
production decisions. Its seventeen chapter dispositions are:

| Chapter | Disposition | Review result |
| --- | --- | --- |
| Ch57 | No Change — Explicitly Verified | Owns the platform control loop and separates desired state, observed state and reconciled state. |
| Ch58 | No Change — Explicitly Verified | Uses Kubeflow as a bounded workflow/control-plane case rather than a product inventory. |
| Ch59 | Refine — Local Flow | Corrected stale chapter handoffs so checkpoint and KServe references resolve to their current owners. |
| Ch60 | No Change — Explicitly Verified | Owns artifact packaging, dependency and promotion boundaries. |
| Ch61 | No Change — Explicitly Verified | Uses KServe as the bounded serving control-plane case after deployment contracts are derived. |
| Ch62 | No Change — Explicitly Verified | Owns workload identity and lifecycle across interactive, batch and asynchronous execution. |
| Ch63 | Refine — Local Flow | Corrected stale inference- and GPU-scheduler chapter references. |
| Ch64 | No Change — Explicitly Verified | Uses Volcano as a bounded queue, gang and batch-scheduling case. |
| Ch65 | No Change — Explicitly Verified | Uses KAI Scheduler as a bounded topology, fairness and GPU-sharing case. |
| Ch66 | Refine — Rebuild Spine | Rebuilt evaluation into Claim Contract → Evidence Production → Measurement Inference → Decision/Feedback and moved reliability mechanisms out of Review notes. |
| Ch67 | No Change — Explicitly Verified | Owns telemetry semantics and causal observability rather than duplicating evaluation decisions. |
| Ch68 | No Change — Explicitly Verified | Owns capacity, utilization and cost attribution under workload contracts. |
| Ch69 | No Change — Explicitly Verified | Owns tenant isolation, quota, noisy-neighbor and fairness boundaries. |
| Ch70 | No Change — Explicitly Verified | Owns release policy, progressive exposure and rollback evidence. |
| Ch71 | No Change — Explicitly Verified | Owns governance as authority, evidence and accountability rather than policy prose. |
| Ch72 | Refine — Local Flow | Restored trajectory-level accumulated-harm mechanics to the security argument after effect-time authorization. |
| Ch73 | No Change — Explicitly Verified | Closes the platform loop through production readiness, incident response and continuous verification. |

The Structure Gate kept all seventeen nodes. Ch66 is long, but every retained section transforms the same EvalSpec
into admissible evidence and a release decision; splitting metrics from decision would duplicate claim identity,
sampling and uncertainty contracts. Ch58, Ch61, Ch64 and Ch65 remain distinct bounded cases because they expose
different workflow, serving, batch and accelerator scheduling control boundaries. Part VI has no mechanism headings
after Review notes, no heading jumps or unclosed fences, and Ch73 hands governed platform capabilities—not raw tools
or credentials—to Part VII.

## 2026-08-14 Books Coherence Review — Part VII

Status: Part VII Gate passed; cross-axis review is next

Part VII was read as a controlled expansion from information state to external action: Prompt and Context assemble a
working set, RAG and Memory add evidence over different lifetimes, Tool/Planning/Reflection propose bounded changes,
Workflow commits durable transitions, Multi-Agent delegates roles, MCP standardizes connectivity, and Agent Platform
closes identity, policy and evidence. Its eleven chapter dispositions are:

| Chapter | Disposition | Review result |
| --- | --- | --- |
| Ch74 | No Change — Explicitly Verified | Owns the probabilistic soft interface and hands assembled runtime state to Context. |
| Ch75 | No Change — Explicitly Verified | Owns the authorized per-call working set and keeps it distinct from persisted Memory. |
| Ch76 | No Change — Explicitly Verified | Owns external evidence acquisition, ranking, packing, freshness and provenance. |
| Ch77 | Refine — Rebuild Spine | Moved the raw-episode→derived-memory evolution before implementation branches, added a four-layer navigation, and separated derived-state organization/validation from construction. |
| Ch78 | No Change — Explicitly Verified | Owns typed action proposal, execution authority, side-effect classes and idempotency boundaries. |
| Ch79 | No Change — Explicitly Verified | Owns plans as revisable state-transition hypotheses with dependencies and completion evidence. |
| Ch80 | No Change — Explicitly Verified | Owns evidence-backed diagnosis and bounded correction, not durable run state. |
| Ch81 | No Change — Explicitly Verified | Owns authoritative workflow transitions, durable replay, compensation and human checkpoints. |
| Ch82 | No Change — Explicitly Verified | Preserves the single-Agent baseline before bounded delegation, communication and aggregation. |
| Ch83 | No Change — Explicitly Verified | Owns connectivity and lifecycle contracts without absorbing authorization or workflow semantics. |
| Ch84 | Refine — Local Flow | Added identity-first chapter navigation and restored target-profiled Skill compilation from Review notes to the capability-admission body. |

The Structure Gate kept all eleven nodes. Ch77 remains one owner because fact, episode and procedural views all share
the same persisted-state write/read/consolidation/deletion contract; its problem was ordering, not a second independent
responsibility. Ch81 and Ch84 are also long but respectively own durable execution and platform-wide coordination, so
splitting them by framework or feature would duplicate identity, evidence and recovery contracts. Four hash-identical
Part VII copies were removed. The Part now has no duplicate chapter files, mechanism headings after Review notes,
heading jumps, unclosed fences, broken local links or filename/title mismatches; Ch73→Ch74 and Ch84→whole-book
transitions are explicit.

## 2026-08-14 Books Coherence Review — Cross-Axis and Final Gate

Status: Seven-Part / 84-chapter coherence review complete

The five horizontal rereads passed after two navigation corrections. The Memory route now includes Ch75 Context
before Ch77 persisted Memory; the Communication route now continues from collective and KV transfer through Ch82
delegation and Ch83 protocol connectivity. `books/README.md` exposes clickable paths for Compute, Memory,
Communication, Scheduling and State, plus five representative evolution chains:

- Dense MLP → conditional MoE → distributed communication/placement → executable kernel and fleet constraints;
- Pretraining → SFT → RLHF → PPO / GRPO / DPO conditional branches;
- request/decode → Continuous Batching → paged state → speculative commit → distributed scheduling;
- claim contract → metrics/logs/traces → evaluation decision → production release gate;
- Context → RAG → Memory → Tool → Workflow → bounded Multi-Agent delegation.

These routes are marked as layering, dependency or alternative branches where appropriate; none is presented as a
single successor erasing its predecessor. The final Structure Gate keeps seven Parts and 84 chapters. No merge, split,
new chapter or Part is justified after the spine repairs: the long chapters Ch33, Ch49, Ch66, Ch77, Ch81 and Ch84 each
retain one canonical system responsibility and a distinct exit contract. `ROADMAP.md` was updated only for horizontal
navigation. `docs/DECISIONS.md` was not changed because no new structural decision supersedes ADR-008.

Final repository checks passed: 84 canonical chapters, 84 unique Stable Knowledge Node IDs, 84 chapter-level audit
dispositions, seven Part guides, 84 Review-notes boundaries, zero duplicate content hashes, zero `* 2.md` copies, zero
mechanism headings after Review notes, no heading jumps or unclosed fences, valid local navigation links, consistent
ROADMAP current/legacy mappings, URL syntax, `git diff --check`, and `git diff --cached --check`. No files were staged,
committed or pushed.
