# Current Learning State

Last Updated: 2026-07

## Current Phase

Reset to the repository-backed roadmap.

The previous Part II / Tokenizer / Embedding learning progress came from
chat-only discussions and should not be treated as repository learning
state.

Current priority:

Build the knowledge-tree backbone from `ROADMAP.md`, while selectively using
high-value source material to draft chapters at their correct knowledge-tree
positions.

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

### Part IV Inference System Review Pass 1

Status: Completed

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

`books/part-04-inference-system/50-gpu-memory.md`

`books/part-04-inference-system/51-pd-disaggregation.md`

`books/part-04-inference-system/52-inference-scheduling.md`

Completed in this pass:

- Removed references to deleted source-material files from Part IV chapters.
- Replaced source-material notes with `Review notes` and primary-source
  verification entry points.
- Standardized the core serving terms: Prefill, Decode, KV Cache, TTFT, TPOT,
  PD disaggregation, scheduler, and runtime.
- Added a Part IV internal map in Chapter 38: stage layer, mechanism layer, and
  engine layer.
- Clarified boundaries among PagedAttention, vLLM, SGLang, TensorRT-LLM, and
  inference scheduling.
- Added workload-dependent caveats to the Prefill compute-bound and Decode
  memory-bound heuristics.
- Added capacity models for KV Cache and GPU memory, plus SLO-aware goodput.
- Distinguished admission control, iteration scheduling, and placement.
- Verified the stable framework boundaries against current official vLLM,
  SGLang, TensorRT-LLM, Megatron Core, and DeepSpeed entry points.

### Repository-wide Draft Review Pass 1

Status: Completed

Scope:

- 26 chapters with repository status `Draft`.
- Part I: Chapters 1-2.
- Part II: Chapters 12, 14, 21, and 22.
- Part III: Chapters 26 and 32-37.
- Part IV: Chapters 38-47 and 50-52.

The 54 `Placeholder` chapters were intentionally left unchanged.

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

AI System worldview → AI history as bottleneck migration → global knowledge
tree → repository-wide refinement of the existing Part II / Part III / Part IV
Draft spine

The repository-backed course has completed the first two Part I worldview
chapters as Drafts and refined all 26 existing Draft chapters. The migrated
material is now expressed as independent chapter reasoning rather than source
material commentary.

Next chapter position:

Continue Part I with Chapter 3: AI System 全局知识树.

## Next Focus

- Stabilize Part I worldview and global AI System knowledge tree.
- Continue with Chapter 3: AI System 全局知识树 when following the book
  linearly.
- Use the reviewed Draft spine as context, but do not promote chapters to
  `Review` or `Final` until adjacent Placeholder dependencies are written.
- Use `ROADMAP.md` as the single source of truth for chapter order.
- Only mark chapter progress after the corresponding repo content is written
  or updated.
- Before finalizing any chapter that uses recent systems or research claims,
  verify against primary sources and avoid treating internal slides as
  authoritative evidence.
