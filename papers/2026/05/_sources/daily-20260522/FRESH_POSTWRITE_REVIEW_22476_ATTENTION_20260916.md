# Fresh post-write semantic review — exact-local/reduced-residual attention

- Reviewer: fresh non-author for this root Books edit; also the date-local corpus repair author
- Reviewed at: 2026-09-16T09:21:20+08:00
- Root body: `books/part-02-model/14-self-attention.md`, immediately after the sparse-Q/K layout branch
- Result: PASS for this Books binding only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

The `SF-2026-ARXIV-2605-22476` marker is a unique paired `:start`/`:end` binding before Ch14's main `## Review notes`. The review read the dense/sparse-QK baseline, bounded body and transition into budget-conditioned Attention rather than accepting marker presence alone.

## Semantic result

PASS: the body preserves fixed-window/sparse-support deletion as the simpler old path, identifies the changed constraint as exact block-local relations plus light cross-block propagation, and states the operator-specific exact-local/reduced-residual mechanism. It assigns block partition, causal mask, pool/lift and reduced-system semantics to the operator owner while limiting runtime to that frozen decomposition; it explicitly withholds equivalence to generic softmax sparsity and arbitrary pretrained checkpoints. It records tiling, two branches, block-size, adaptation and head-capacity costs, names diffuse routing/residual error/properties-over-heads/measured-latency failures, and falls back to dense resolvent, dense Attention or a validated fixed-window/sparse kernel. Placement between the existing feature-sparse kernel discussion and compute-budget routing is coherent.

## Gate boundary

This closes only the write-after semantic Gate for root-owned `2605.22476`. It does not sign the repaired daily corpus Complete: 0 accessible exact-v1 deep reviews and 0 current root queue items remain, and a different fresh non-author must execute the final daily Gate after all repairs freeze.
