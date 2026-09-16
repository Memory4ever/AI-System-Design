# Fresh post-write semantic review — four Data/RLHF items

- Reviewer: fresh non-author for these four root Books edits; also the date-local corpus repair author
- Reviewed at: 2026-09-15T23:05:00+08:00
- Root writeback: observed directly in root-owned Ch27/Ch31 files
- Result: PASS for these four Books bindings only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

All four source markers are unique paired `:start`/`:end` bindings and occur before their target chapter's main `## Review notes`. Each bounded body and its adjacent paragraphs was read in sequence.

| Source | Owner/body result | Semantic result |
| --- | --- | --- |
| `2605.22651` | `TRAIN-DATA` / Ch27 | PASS: keeps coarse global alignment as the baseline, adds controlled phrase-level substitution sensitivity without promoting it to grounding/localization/causal proof, separates scorer proposal from admission, records parser/scorer/tokenizer/nonce and interaction failure, and falls back to coarse alignment, randomized coverage controls and human or region-grounded evidence. |
| `2605.21654` | `TRAIN-RLHF` / Ch31 | PASS: preserves score-function/advantage credit as the safe baseline, bounds empirical-costate interpretation to continuous differentiable additive-noise assumptions, states the missing discrete sampling path and entropy gap, separates outcome/autodiff/optimizer ownership, records hidden-gradient and matched-rollout cost, and falls back to standard advantage, process reward, an explicit critic or held-out sweep. |
| `2605.21822` | `TRAIN-RLHF` / Ch31 | PASS: explains why crowd-average reward entangles shared safety with user-specific goals, adds a conditional skill-basis/controller decomposition, separates preference, skill, task-controller and hard-safety ownership, bounds the branch to the shared-safety and skill-support assumptions, records offline-data/coverage/basis cost, and falls back to grouped reporting, explicit safety cost/gates, task baselines and human adjudication. |
| `2605.22156` | `TRAIN-RLHF` / Ch31 | PASS: retains symmetric KL as the baseline, routes signed direction to the verifier and magnitude to reference log-ratio, versions reference refresh as rollback state, bounds evidence to disclosed Qwen/math binary-verifier settings, records false-positive lock-in and state cost, and falls back to a frozen reference, symmetric KL/plain GRPO and independent held-out/safety gates. |

## Adjacent-flow and Gate boundary

The Ch27 insertion advances from coarse filtering to phrase sensitivity and then to compute/data-aware thresholds. The Ch31 insertions advance from pluralistic aggregation to multi-objective reward, from output-distribution change to reverse-KL coverage, and from delayed sequence reward to the harm-horizon discussion without changing the neighboring claims.

This closes only the write-after semantic Gate for these four root-owned edits. It does not sign the repaired daily corpus Complete: 22 accessible exact-v1 deep reviews remain after the current SFT batch, three new Ch29 Integrate items remain in the serialized root queue, and a different fresh non-author must execute the final daily Gate after all repair and Books work freezes.
