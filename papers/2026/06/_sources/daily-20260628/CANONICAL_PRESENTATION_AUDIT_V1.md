# 2026-06-28 Canonical Presentation Audit V1

- Scope: accepted-state reader-facing and renderer audit only; frozen denominator, Evidence, Selection and Books semantics were not re-evaluated.
- Canonical presentation: top five fields present; `Executive Summary` plus the exact numbered §§1–13 H2 sequence passed.
- Denominator and access: `211 = 65 retained + 146 closures`; `65/65` exact-v1 accessible; pending `0`.
- Protected report fragments: `346`; combined SHA256 `ce8dd1443098a741404d5da6b298cd4aabf7b40641b064c4b9d8491d2770a612`.
- Bounded Reviews: `65/65`; combined SHA256 `fa9647323ccaff08e6514b97c2ede4d6e07129c3d82c93edfe85b0eeb7fa61c8`.
- Review Provenance IDs: `65/65`; the protected Review Completion table remains byte-identical.
- Books table and bounded blocks: `145` fragments; combined SHA256 `62db95c88169bb5e83f2a06a721418d82cfde312441f86552d0c834a5d331ea6`.
- Books dispositions and fresh audit: `6 Integrate / 42 No Change / 17 Weekly Only`; post-write `65/65`; unresolved findings `0`.
- Semantic packet inputs: `84` files sealed; combined SHA256 `0d760b4887924bc0c1ce5eaa3352fb8841f281938a8577c08347d9c0b12107a9`.
- Reader-facing Daily SHA256: `26f2b002267dd45bf9d362ee850b67af728784105c378de9ba3abd17d6f4e227`.
- Final owner renderer: PASS — accepted state exits before Books access or semantic regeneration; protected-byte drift, packet drift, missing audits, wrong Gate state, duplicate markers or H2 drift fails closed.
- Semantic handoff: `FRESH_EVIDENCE_SELECTION_AUDIT_V1.md` and `POST_WRITE_FRESH_AUDIT_V1.md` remain the accepted fresh-context audits; validator success is not substituted for semantic truth.
- Cross-model skipped: non-interactive child-lane context; no independent second-model claim is made.
- Findings: none unresolved.
