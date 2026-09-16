# 2026-05-27 Fresh Non-Author Post-Write Review — Bounded Repair

- Review time: `2026-09-16T13:56:31+08:00`
- Reviewer role at start: fresh non-author; not involved in the 05-27 denominator/Evidence repair or root Ch22 writeback
- Result: `FAIL → bounded repair applied; another fresh reviewer required`

## Checks that passed

- Owner-day conservation: `692 = 92 retained + 600 closure + 0 withdrawn`.
- Screening, Evidence and Books candidate identity sets are equal at `92`.
- Evidence: `92 deep + 0 standard + 0 blocked`; scores reconcile to `22×7 + 60×8 + 10×9`.
- Root writeback queue has `18 applied_pending_fresh_review` items and `0` pending writebacks.
- Exact-v1 supports bounded offline recurrence before KV eviction, fast-weight updates, single-pass wake-time prediction, and controlled evidence on cellular automata, Depo and GSM-Infinite. It also discloses the sequential/offline compute and training-stability costs.

## Findings and bounded repairs

1. Exact-v1 title is `Language Models Need Sleep`; the current Daily projections used an earlier/incorrect expanded title. Current README, screening and Evidence projections now use the exact-v1 title.
2. Root writeback had completed, but Books comparison and Evidence still projected `Integrate`. They now project `Applied`; Books arithmetic is `59 Applied + 33 No Change + 0 pending`.
3. Ch22 placed the paired binding start marker after the mechanism paragraph, so the binding only enclosed the trade-off paragraph. The start marker now precedes the complete adopted mechanism.
4. Ch22 did not clearly distinguish the paper's tested mechanism from the project's transactional runtime inference. The paragraph now states that recurrent passes and KV eviction are paper-supported, while versioning, quality gate, atomic commit and recovery are system-design deductions required to make that state mutation operationally safe.

## Independence boundary

This reviewer modified the reviewed artifacts and therefore cannot issue a final PASS. Another reviewer who participated in neither the earlier repair nor this bounded repair must verify the exact-v1 title, Evidence boundary, full Ch22 binding, `59+33` projection and queue state before marking the Daily Complete.
