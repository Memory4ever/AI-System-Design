# Current Learning State

Last Updated: 2026-07

## Current Phase

Reset to the repository-backed roadmap.

The previous Part II / Tokenizer / Embedding learning progress came from
chat-only discussions and should not be treated as repository learning
state. That gap has now been replaced by the repository-backed Part II Draft
recorded below.

Current priority:

Parts I, II, III, IV, V, and VI have been completed as repository-backed
Drafts. The complete Chapters 1-80 knowledge tree is now available for
papers-driven refinement, cross-Part verification, and later maturity review.

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

No chapter was promoted beyond `Draft`. At the time of that review, the next
learning position was Part V, Chapter 53: 什么是 AI Platform.

### Daily Research Integration: Quantized Artifact and GPU Capacity

Status: Completed; affected chapters remain Draft

Source record:

`papers/2026/07/27/README.md`

Updated repository chapters:

`books/part-03-training-system/31-checkpoint.md`

`books/part-04-inference-system/45-tensorrt-llm.md`

`books/part-04-inference-system/50-gpu-memory.md`

`books/part-04-inference-system/52-inference-scheduling.md`

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
Chapter 31
  validated numerical + graph + execution artifact identity
-> Chapter 45
  runtime build, quantization, graph rewrite and kernel execution plan
-> Chapter 50
  weights, KV, workspace and reserve compete within usable HBM
-> Chapter 52
  admission and scheduling operate on the resulting capacity
```

This integration did not change chapter maturity or course position. At that
time, the next position was Part V, Chapter 53: 什么是 AI Platform.

### Part V AI Infrastructure: Chapters 53-69

Status: Draft completed and cross-chapter reviewed

Repository scope:

`books/part-05-ai-infrastructure/53-what-is-ai-platform.md`

through:

`books/part-05-ai-infrastructure/69-production-best-practice.md`

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
- MLflow maps runs, artifacts, logged models, evaluation evidence, and
  registered versions into a metadata plane. It does not replace workload,
  serving, tenancy, or resource control planes.
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

The Part V platform path is now repository-backed:

```text
Part III deployment artifact
-> Part IV runtime state and SLO
-> platform identity and lifecycle contracts
-> Kubeflow / Registry / Operator / KServe / Gateway
-> GPU scheduling and queue governance
-> Metrics / Logs / Traces
-> cost / tenancy / security
-> production feedback and recovery
```

Part V cross-chapter and cross-Part boundaries:

- Chapter 52 schedules request/token/KV state at inference-runtime time;
  Chapters 59-61 place Pods, gangs, and GPU resources at cluster time.
- Chapter 31 owns checkpoint and deployment-artifact formation; Chapter 55
  owns immutable model identity, lineage, evidence, aliases, and promotion
  metadata.
- Chapter 49 owns `LLMInferenceService` topology and EPP request paths;
  Chapter 57 owns the general KServe service lifecycle and Runtime abstraction.
- Chapter 56 maps Part III training topology into Kubernetes workloads but
  does not change TP/PP/DP/CP/EP mathematics or replace gang scheduling.
- Chapters 63-65 separately own aggregate metrics, event evidence, and causal
  traces. Chapter 62 MLflow is one lifecycle-metadata implementation, not the
  entire production observability plane.
- Chapter 68 freezes the platform security boundary for Prompt and Tool
  execution without pre-empting Part VI's Agent mechanisms.
- Chapter 69 hands Part VI immutable identity, policy, trace, budget,
  security, audit, and recovery contracts. Agent execution extends these
  contracts instead of creating a parallel governance system.

Current framework claims were checked against the July 2026 official
documentation for Kubeflow, Kubeflow Trainer, KServe 0.18, Gateway API and its
Inference Extension, Kubernetes DRA, Volcano, KAI Scheduler, MLflow, and
OpenTelemetry. Version-dependent APIs are labeled as such.

All seventeen chapters remain `Draft`. At the time of that pass, the next
repository-backed learning position was Part VI, Chapter 70: Prompt.

### Part VI Agent: Chapters 70-80

Status: Draft completed and cross-chapter reviewed

Repository scope:

`books/part-06-agent/70-prompt.md`

through:

`books/part-06-agent/80-agent-platform.md`

Core understanding:

- Prompt is a versioned runtime input to a conditional model distribution,
  not a deterministic program or a security boundary.
- Context is the authorized, selected, ordered working set for one model call.
  RAG supplies external evidence; Memory persists state across calls through
  governed write, read, consolidation, correction, and forgetting policies.
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
- Agent Platform extends the Part V platform with goal, plan, context, memory,
  action, delegation, approval, and long-running workflow state. It reuses the
  same identity, resource, evidence, cost, tenancy, security, and recovery
  substrate rather than creating a parallel platform.

The Part VI runtime path is now repository-backed:

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

Part VI cross-chapter and cross-Part boundaries:

- Chapter 70 owns runtime prompting; Chapter 25 owns SFT and parameter-level
  behavior adaptation.
- Chapter 22 owns long-context model/system limits; Chapter 71 owns runtime
  selection, ordering, compression, trust, and token-budget assembly.
- Chapter 72 owns external evidence retrieval; Chapter 73 owns persisted
  cross-call state and its write/forget lifecycle.
- Chapter 74 owns typed tool intent and execution boundaries; Chapter 79 owns
  MCP connectivity and capability negotiation.
- Chapter 75 owns a revisable plan; Chapter 77 owns durable authoritative
  workflow state. Chapter 76 owns inference-time feedback and does not modify
  the Part III optimization objectives.
- Chapter 78 assigns bounded responsibility among Agents but relies on
  Chapter 77 for shared fact state and recovery.
- Chapter 80 extends Part V governance to the action loop. Part IV continues
  to own token/KV scheduling and Part V continues to own GPU and tenant
  resource governance.

Current claims were checked against primary papers for in-context learning,
RAG, Memory, Tool use, planning, reflection, Multi-Agent, and Agent
evaluation. MCP is explicitly pinned to the published `2025-11-25`
specification; the 2026-07-28 release candidate is not treated as an already
released stable contract. Agent identity and authorization are described as
an evolving standards area using current NIST material.

All eleven chapters remain `Draft`. All six roadmap Parts and Chapters 1-80
are now repository-backed Drafts.

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

Parts I-VI complete as repository-backed Drafts

The repository-backed course now has a continuous worldview, model-mechanism,
capability-production, online capability-delivery, and platform-governance
spine, extended through the complete Agent action loop. A task can be traced
from model capability and a governed artifact through inference, platform
policy, Context, Memory, tools, Workflow, external effects, evidence, and
feedback.

Next learning phase:

Papers-driven cross-Part refinement and verification. No new linear chapter
position remains in the current roadmap.

## Next Focus

- Refine existing chapters only when papers, official specifications, source
  materials, or real system evidence add durable knowledge or correct an
  existing contract.
- Use Part I as the worldview, Part II as the model contract, Part III as the
  capability-production contract, and Part IV as the online inference-runtime
  and SLO contract. Use Part V as the platform identity, resource, evidence,
  tenancy, security, and production-governance contract. Use Part VI as the
  governed Context-to-action runtime contract.
- Keep Parts I-VI at `Draft`; promotion to `Review` or `Final` remains a
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
