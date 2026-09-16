# 2026-05-22 Fresh Non-author Denominator Repair

## Scope

- Review role: fresh non-author post-write reviewer.
- Frozen owner window: `[2026-05-21T09:00:00+08:00, 2026-05-22T09:00:00+08:00)`.
- Frozen corpus: 667 identities. No source, date or identity expansion was performed.
- Review posture: disprove the frozen denominator and the five newest Books bindings before approval.
- Cross-model review: skipped because this is a delegated non-interactive checkpoint.

## Prior Books bindings

The five newest root bindings all passed direct post-write semantic inspection:

| Source family | Owner | Result |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-21573` | `TRAIN-PRETRAINING` | paired marker occurs once; body states the adopted proposition, boundary, trade-off and fallback before Review notes |
| `SF-2026-ARXIV-2605-21648` | `TRAIN-PRETRAINING` | pass |
| `SF-2026-ARXIV-2605-21776` | `PLATFORM-EVALUATION-SYSTEM` | pass |
| `SF-2026-ARXIV-2605-21847` | `PLATFORM-COST` | pass |
| `SF-2026-ARXIV-2605-22014` | `TRAIN-DISTRIBUTED-TRAINING` | pass after the adopted proposition was restated as a durable source-world / target-world / commit / fallback contract |

These findings do not close the day because the same fresh review found two denominator false negatives.

## Confirmed false negatives and bounded repair

### `2605.21692` — Representation Gap

The prior `survey_or_taxonomy_context` closure was false. Exact-v1 defines a representation-gap metric, derives asymptotic scaling governed by task intrinsic dimension, and identifies equivariance as virtual augmentation that changes effective dimension under explicit assumptions. This is a durable model/generalization mechanism.

- Evidence: deep complete from official exact-v1 HTML.
- Score: `3+2+3=8`.
- Owner: `WORLDVIEW-REPRESENTATION`, Ch5.
- Books: `Integrate — pending root serialized writeback`.
- Boundary: the result is asymptotic and assumption-bound; it is not a universal generalization-error formula and does not replace held-out or distribution-shift evaluation.

### `2605.22158` — ST-SimDiff

The prior `local_model_or_task_quality_delta` closure was false because the same report already retained a closely related long-video token-compression branch. Exact-v1 provides a reusable fixed-budget separation between representative stable-content tokens and temporal-change tokens, with explicit compute/memory and threshold-failure evidence.

- Evidence: standard complete from official exact-v1 HTML.
- Score: `2+2+2=6`.
- Owner: `MULTIMODAL-REPRESENTATION`, Ch23.
- Books: `No Change — current main body carries the proposition`.
- Boundary: similarity/difference thresholds are routing proposals, not event truth; the measured runtime does not transfer without matching the disclosed execution contract.

## New canonical projection

```text
667 raw identities
= 254 retained
+ 413 pre-denominator closures
+ 0 withdrawn

254 retained
= 196 deep evidence complete
+ 58 standard evidence complete
+ 0 pending
+ 0 blocked

254 Books dispositions
= 52 Integrate
   = 51 Applied
   + 1 pending root writeback
+ 146 No Change
+ 56 Report Only
```

The prior closure audit projection changes from `89 restored + 412 continued` to `91 restored + 410 continued`. The repair is limited to these two identified families.
The canonical ledger's legacy `integration_disposition` projection was also synchronized mechanically with each retained family's final `books_disposition`; this changed no semantic decision and removed contradictory retained/rejected states.

## Remaining Gate

The report must remain **Ongoing**. Root must serialize `SF-2026-ARXIV-2605-21692` into Ch5 before `## Review notes` with one paired marker and preserve old baseline, changed constraint, evidence boundary, trade-off and fallback. Because this reviewer performed the bounded repair, a different fresh non-author reviewer must inspect the final Books binding and the updated canonical projection before marking the day Complete.
