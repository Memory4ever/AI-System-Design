# Current Learning State

Last Updated: 2026-07

## Current Phase

Reset to the repository-backed roadmap.

The previous Part II / Tokenizer / Embedding learning progress came from
chat-only discussions and should not be treated as repository learning
state. That gap has now been replaced by the repository-backed Part II Draft
recorded below.

Current priority:

Parts I, II, III, and IV have been completed as repository-backed Drafts.
Continue linearly into Part V while preserving the model, training-state,
inference-runtime, SLO, and distributed-control contracts established by
Chapters 1-52.

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
- Chapter 19 owns the model origin, shape, and capacity of KV Cache; Chapter 41
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
  mechanics, and the Part II to Part III transition from model structure to
  capability production through data, objectives, and optimization.
- Rechecked chapter boundaries against later Parts: tokenizer data governance
  remains in Chapter 23; training mechanisms remain in Part III; KV Cache
  allocation, paging, and scheduling remain in Part IV; RAG and Memory remain
  in Part VI.

Review conclusion:

Part II now has a coherent dependency structure rather than merely twelve
complete chapter files. Each chapter retains one central thesis, while chapter
transitions expose which tensor contract, unresolved problem, or scaling
constraint the next node receives. This pass does not promote the chapters to
`Review`; primary-source refresh and a later cross-Part verification are still
required before maturity changes.

### Part III Training System: Chapters 23-37

Status: Draft completed; cross-chapter Review completed

Repository paths:

`books/part-03-training-system/23-data.md`

`books/part-03-training-system/24-pretraining.md`

`books/part-03-training-system/25-sft.md`

`books/part-03-training-system/26-lora.md`

`books/part-03-training-system/27-rlhf.md`

`books/part-03-training-system/28-ppo.md`

`books/part-03-training-system/29-grpo.md`

`books/part-03-training-system/30-dpo.md`

`books/part-03-training-system/31-checkpoint.md`

`books/part-03-training-system/32-distributed-training.md`

`books/part-03-training-system/33-tensor-parallel.md`

`books/part-03-training-system/34-pipeline-parallel.md`

`books/part-03-training-system/35-zero.md`

`books/part-03-training-system/36-megatron.md`

`books/part-03-training-system/37-deepspeed.md`

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

The Part III capability-production path is now repository-backed:

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

Part III cross-chapter boundaries:

- Chapter 23 owns data distribution and lineage; Chapter 24 owns the
  next-token objective and base training loop.
- Chapter 25 owns demonstration supervision; Chapter 26 owns low-rank update
  parameterization and adapter assets.
- Chapter 27 owns the RLHF feedback and Reward Model pipeline; Chapters 28-30
  separately own PPO, GRPO, and DPO optimization mechanics.
- Chapter 31 owns consistent persistence, resume, resharding, and artifact
  conversion; Chapter 35 owns data-parallel model-state sharding.
- Chapter 32 owns the distributed-training decision framework and Data
  Parallel baseline; Chapters 33-35 own TP, PP, and ZeRO mechanisms.
- Chapter 36 owns multi-dimensional Transformer parallelism composition;
  Chapter 37 owns DeepSpeed training-state lifecycle policy and the transition
  to a validated inference artifact.
- Part III stops at model-artifact production. Prefill, Decode, KV Cache,
  batching, serving engines, and online scheduling remain in Part IV.

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

`books/part-03-training-system/26-lora.md`

`books/part-03-training-system/32-distributed-training.md`

`books/part-03-training-system/33-tensor-parallel.md`

`books/part-03-training-system/34-pipeline-parallel.md`

`books/part-03-training-system/35-zero.md`

`books/part-03-training-system/36-megatron.md`

`books/part-03-training-system/37-deepspeed.md`

`books/part-04-inference-system/38-what-happens-during-inference.md`

`books/part-04-inference-system/39-prefill.md`

`books/part-04-inference-system/40-decode.md`

`books/part-04-inference-system/41-why-kv-cache-speeds-up.md`

`books/part-04-inference-system/42-continuous-batching.md`

`books/part-04-inference-system/43-pagedattention.md`

`books/part-04-inference-system/44-speculative-decoding.md`

`books/part-04-inference-system/45-tensorrt-llm.md`

`books/part-04-inference-system/46-vllm.md`

`books/part-04-inference-system/47-sglang.md`

`books/part-04-inference-system/50-gpu-memory.md`

`books/part-04-inference-system/51-pd-disaggregation.md`

`books/part-04-inference-system/52-inference-scheduling.md`

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

### Part IV Inference System: Chapters 38-52

Status: Draft completed; cross-chapter Review completed

Repository paths:

`books/part-04-inference-system/38-what-happens-during-inference.md`

`books/part-04-inference-system/39-prefill.md`

`books/part-04-inference-system/40-decode.md`

`books/part-04-inference-system/41-why-kv-cache-speeds-up.md`

`books/part-04-inference-system/42-continuous-batching.md`

`books/part-04-inference-system/43-pagedattention.md`

`books/part-04-inference-system/44-speculative-decoding.md`

`books/part-04-inference-system/45-tensorrt-llm.md`

`books/part-04-inference-system/46-vllm.md`

`books/part-04-inference-system/47-sglang.md`

`books/part-04-inference-system/48-dynamo.md`

`books/part-04-inference-system/49-kserve-llm.md`

`books/part-04-inference-system/50-gpu-memory.md`

`books/part-04-inference-system/51-pd-disaggregation.md`

`books/part-04-inference-system/52-inference-scheduling.md`

Core understanding:

- LLM inference is a stateful token-generation process. A request moves from
  validation and admission through Prefill, Decode, streaming, completion, and
  state release; TTFT, TPOT, throughput, and goodput measure different parts
  of this lifecycle.
- Prefill converts prompt tokens into first-token logits and initial per-layer
  KV state. Decode advances the same request under an autoregressive
  dependency, making iteration cadence and memory movement first-class system
  concerns.
- KV Cache exchanges memory for historical-computation reuse. Its logical
  capacity depends on layer count, KV heads, head dimension, dtype, sequence
  length, and concurrency; its physical lifecycle additionally requires
  allocation, sharing, paging, transfer, eviction, and release.
- Continuous Batching, PagedAttention, and Speculative Decoding are orthogonal
  mechanisms. They respectively change batch membership, physical KV
  placement, and target-model progress per serial step.
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

The Part IV capability-delivery path is now repository-backed:

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

Part IV cross-chapter boundaries:

- Chapter 19 owns the model-level KV shape and reuse invariant; Chapter 41
  owns runtime capacity, lifecycle, sharing, eviction, and transfer readiness.
- Chapter 42 owns iteration-level dynamic batching; Chapter 52 owns admission,
  iteration, routing/placement, and autoscaling.
- Chapter 43 owns logical-to-physical KV block mapping; Chapter 46 owns the
  complete vLLM V1 serving-engine architecture.
- Chapter 47 owns prefix/program structure as inference-runtime state; Part VI
  owns Agent planning, tools, memory semantics, and workflow governance.
- Chapter 48 owns Dynamo's distributed request/control/state architecture;
  Chapter 51 owns the mechanism and break-even reasoning for PD separation.
- Chapter 49 owns the LLMInferenceService serving topology and request path;
  Chapter 57 owns KServe as a general AI-platform capability.
- Chapter 52 schedules token-generation state; Part V GPU schedulers place and
  govern Pods, gangs, queues, and cluster resources.

All fifteen chapters remain `Draft`. Framework behavior and API details are
treated as time-sensitive, with current official documentation and primary
papers retained as verification entry points.

### Part III-IV Cross-Part Review

Status: Completed; all chapters remain Draft

Review scope:

- Deep Review of Chapters 23-52, including each chapter's central thesis,
  internal reasoning, input/output contract, adjacent transition, and
  knowledge-tree ownership.
- Contract backtracking into the relevant Part I-II chapters for Tokenizer,
  Decoder-only generation, Sampling, KV Cache, MoE, and Long Context.
- Surgical upstream corrections only; no roadmap or chapter-structure change.

The reviewed capability path is:

```text
Part I   system problem and knowledge tree
-> Part II  model structure and generation semantics
-> Part III data, objective, training state and deployment artifact
-> Part IV  request state, runtime execution, memory and SLO delivery
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
- Chapter 19 owns model-level KV shape; Chapter 41 owns runtime lifecycle;
  Chapter 43 owns paging; Chapters 50-52 own capacity, PD and scheduling.
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
  Part V.

Current framework claims were refreshed against official documentation for
Megatron Core, TensorRT-LLM, vLLM V1, SGLang, NVIDIA Dynamo and KServe
LLMInferenceService. Version-dependent behavior is labeled as such; paper
results are not automatically projected onto current implementations.

No chapter was promoted beyond `Draft`. The next learning position remains
Part V, Chapter 53: 什么是 AI Platform.

### Repository-wide Draft Review Pass 1

Status: Completed

Scope:

- 26 chapters with repository status `Draft`.
- Part I: Chapters 1-2.
- Part II: Chapters 12, 14, 21, and 22.
- Part III: Chapters 26 and 32-37.
- Part IV: Chapters 38-47 and 50-52.

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

Parts I-IV complete as Draft → ready to enter Part V platform capability

The repository-backed course now has a continuous worldview, model-mechanism,
capability-production, and online capability-delivery spine. A request can be
traced from a validated model artifact through Prefill, Decode, KV state,
runtime mechanisms, serving engines, distributed control, and SLO-aware
scheduling.

Next chapter position:

Part V, Chapter 53: 什么是 AI Platform.

## Next Focus

- Continue linearly with Part V, Chapter 53: 什么是 AI Platform.
- Use Part I as the worldview, Part II as the model contract, Part III as the
  capability-production contract, and Part IV as the online inference-runtime
  and SLO contract.
- Keep Parts I-IV at `Draft`; promotion to `Review` or `Final` remains a
  separate maturity decision after adjacent platform chapters and a later
  cross-Part primary-source refresh are complete.
- Use `ROADMAP.md` as the single source of truth for chapter order.
- Only mark chapter progress after the corresponding repo content is written
  or updated.
- Before finalizing any chapter that uses recent systems or research claims,
  verify against primary sources and avoid treating internal slides as
  authoritative evidence.
