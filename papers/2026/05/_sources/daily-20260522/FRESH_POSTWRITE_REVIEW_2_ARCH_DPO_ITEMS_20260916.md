# Fresh post-write semantic review — architecture and DPO items

- Reviewer: fresh non-author for these two root Books edits; also the date-local corpus repair author
- Reviewed at: 2026-09-16T10:05:00+08:00
- Root writeback: observed directly in root-owned Ch17 and Ch34
- Result: PASS for these two Books bindings only; the daily report remains Ongoing

## Scope and checks

Both source markers are unique paired `:start`/`:end` bindings before the target chapter's main `## Review notes`. Each bounded body and the preceding old-path/constraint paragraph were read in sequence.

| Source | Result |
| --- | --- |
| `2605.21724` | PASS: starts from single-stream/finite-Sinkhorn feasibility, introduces the exact/full-interior transportation chart only when repeated mixing needs exact double stochasticity and full expressivity, separates checkpoint and runtime ownership, records sequential/nonlinear/kernel/optimizer costs, denies that matrix feasibility proves model quality, bounds the evidence to small mostly single-seed LM runs, and falls back to single stream or validated Sinkhorn/permutation/structured mixers. |
| `2605.21883` | PASS: starts from vanilla equal token sums and names token weighting as an objective change, versions pair/reference/reduction/weight policy, limits pairwise-judge attention to a token-credit proposal, preserves label/objective/optimizer ownership, records two forward passes, layer/head/order/sink/judge costs, bounds evidence to the disclosed instruction-following setting, and falls back to vanilla DPO or verified token/process labels. |

## Gate boundary

This closes only the write-after semantic Gate for these two root-owned edits. It does not sign the repaired daily corpus Complete; remaining exact-v1 review and any resulting root queue must freeze before a different fresh non-author executes the final daily Gate.
