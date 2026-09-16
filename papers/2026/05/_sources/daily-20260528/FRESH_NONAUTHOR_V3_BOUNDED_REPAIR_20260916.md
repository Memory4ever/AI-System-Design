# 2026-05-28 Fresh Non-Author Review — Bounded Repair

- Review time: `2026-09-16T13:29:10+08:00`
- Reviewer role: fresh non-author relative to the 05-28 owner repair
- Result: `Ongoing — bounded repair applied; a new fresh reviewer is required`

## Checks that passed

- The authoritative owner receipt contains 835 unique identities: `835 = 118 retained + 717 closure + 0 withdrawn`.
- Owner evidence routes reconcile to `670 official_arxiv_oai_direct + 165 datacite_initial_created_owner_proxy`.
- Candidate, Evidence and Books identity sets are internally consistent; Evidence has 118 deep-complete items, with score distribution `{7: 6, 8: 92, 9: 20}`.
- Books dispositions reconcile to `18 Applied + 100 No Change`; all 18 Applied owner paths exist and all 18 bindings occur before the canonical chapter-level `## Review notes` boundary.
- The 117 reused exact-v1 reviews remain represented in `OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md`.

## Finding and bounded repair

Gamma-World (`arXiv:2605.28816v1`) was retained correctly, but its prior Books summary described a shared-scene/per-agent-state factorization that the paper does not claim, and Ch25 had no paired source-family binding.

The exact-v1 paper instead supports this bounded mechanism chain:

1. fixed learned slot identity and dense cross-agent attention become brittle as the roster grows;
2. parameter-free simplex rotary agent encoding preserves distinct identities while remaining permutation-equivalent;
3. Sparse Hub Attention moves cross-agent communication through a small hub state;
4. the causal streaming student keeps per-agent and hub KV state separately.

The evidence only covers the authors' virtual multi-player settings, trained with two agents and evaluated with two/four players. It does not establish open-world physical causality, social causality, real-robot control, or production SLOs.

The repair directly updated Ch25, added paired semantic and source-family markers, and synchronized the Daily README plus canonical screening, Evidence, exact-v1 packet, Books comparison and writeback queue JSON projections.

## Why this is not a final pass receipt

This reviewer changed the reviewed artifact. Independence therefore no longer holds for the repaired Gamma binding. A different fresh non-author reviewer must verify only the repaired Gamma exact-v1 semantics, Ch25 body placement/markers, and README/JSON projection consistency. Until that pass, the Daily remains `Ongoing`.

