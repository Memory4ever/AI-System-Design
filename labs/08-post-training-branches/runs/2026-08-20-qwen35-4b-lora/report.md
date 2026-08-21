# Experiment Report — Qwen3.5-4B MLX LoRA

## Claim

- Hypothesis: Rank-16 LoRA improves six-section answer compliance on held-out AI System prompts.
- Expected mechanism: assistant-only SFT raises the likelihood of the demonstrated response structure while base weights remain immutable.
- Expected validity boundary: one post-trained Qwen3.5-4B checkpoint, one MLX backend, one seed, and this synthetic task distribution.

## Workload Contract

| Dimension | Value |
| --- | --- |
| Code / dependency revision | Unsloth Desktop `0.1.800-beta`; Transformers 5.5.0; local MLX runtime |
| Dataset | `dataset/train.jsonl` 100 rows; validation/test 20 each |
| Model | `/Users/apple/Downloads/Qwen3.5-4B`, Safetensors, post-trained |
| Hardware | Apple M1 Max, 64 GB unified memory |
| Runtime | Unsloth Desktop `0.1.800-beta`, MLX |
| Precision | 16-bit LoRA |
| Context | 1024 |
| Batch | micro 1, accumulation 8, effective 8 |
| Seed | 3407 |
| Generation | non-thinking; temperature 0.7; top-p 0.8; top-k 20 |

## Baseline and Change

- Baseline: base checkpoint with no adapter.
- Single changed variable: Rank-16 LoRA adapter trained for 30 steps.
- Base checkpoint, test prompts and decoding parameters remain fixed.

## Correctness Evidence

- Dataset validation: PASS; train/validation/test counts are 100/20/20, prompts are unique, and all demonstrations preserve heading order.
- Token length: train max 275, validation max 255 under the exact Qwen3.5 chat template; no truncation at context 1024.
- Adapter reload: PASS from the copied `adapter/` directory through `mlx_lm.load(..., adapter_path=...)`.
- Base checkpoint immutability: base shard mtimes remain 2026-07-10; digests are recorded in `adapter/MANIFEST.md`.
- Output structure and expected-concept scoring: Base completed on 20 held-out prompts.

## Results

| Variant | Structure Pass | Concept Recall | Training Loss | Wall Time | Peak Memory | Notes |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Base | 0.100 | 0.289 | N/A | mean 7.639 s/prompt | Not captured | Often uses `###` instead of the required `##` headings |
| Base + LoRA | 1.000 | 0.247 | final 1.3849; mean 2.0214 | training 379.1 s; inference mean 5.902 s/prompt | 11.042 GB | Best eval loss 2.1984 at step 27; final 2.2009 |

General regression, using a neutral system prompt that does not request the six-section format:

| Variant | Template Intrusion | Concept Recall | Notable Failure |
| --- | ---: | ---: | --- |
| Base | 0.000 | 0.889 | None in the deterministic checks |
| Base + LoRA | 0.000 | 0.833 | Returned `reversed(...)` rather than a concrete list-reversal slice |

## Interpretation

- What the evidence proves: 30-step Rank-16 LoRA changed the target behavior. Strict held-out structure compliance rose from 0.100 to 1.000, and the adapter can be loaded independently from the immutable base.
- What it does not prove: Expected-concept recall fell from 0.289 to 0.247. The run therefore does not prove new knowledge, better factuality or better system-design reasoning.
- New cost and failure modes: The 91 MiB adapter is coupled to the exact base identity. Eval loss reached its minimum at step 27 and rose slightly by step 30, which is an early overfitting signal. One general Python regression also appeared.
- Where the baseline still applies: Base performance remained slightly better on the simple general regression set. The adapter should only be selected when the six-section response contract is required.

## Handoff

- Reusable artifacts: dataset, config, base outputs, adapter outputs and LoRA adapter.
- Required identity/version: base digest, Unsloth/MLX version, seed and chat template.
- Open questions: A longer run is not justified yet. The next experiment should improve answer diversity and concept coverage, then compare step 20/27/30 checkpoints before increasing steps.
