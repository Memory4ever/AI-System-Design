# 2026-06-29 Recovery Re-freeze Audit V1

## Recovery condition

The filesystem recovery exposed the prior Daily and packet paths as zero-byte placeholders. The pre-loss byte seal therefore cannot be treated as recovered evidence. This packet uses an explicit recovery re-freeze rather than silently replacing the historical seal.

## Reconciliation

- Raw registered identities: `262`.
- Frozen Candidate Denominator: `86` retained + `176` family-specific pre-denominator closures.
- Candidate-ID set: reconciled against the surviving historical command/audit trail; `86/86` identities match.
- Exact-version Evidence: `86/86` receipts bind `arXiv:<id>v1`, source-specific Method, Evaluation and limitations/counterevidence locators; ordinary pending and blocked are `0`.
- Books disposition: `13 Integrate / 67 No Change — Existing Coverage / 6 Weekly Only — Context`.
- Recovered Source Review body aggregate: `f9d976ae45912647be214fafdc33637ab2ea929c92f9b8fe45a6a82d7168ae0b`.
- Recovered Review Provenance aggregate: `efd9a23ff89daf8cb0322d63662991c7cb105f0e4931e924895be3ee422ca83c`.

## Boundary

This receipt does not claim byte-for-byte identity with the lost report. It records the new frozen identity after source-family, exact-v1 locator, review-body and provenance reconciliation. The Daily may become `Complete` only after the 13 Integrate families are written under the chronological Books lock and the independent 86/86 post-write audit passes with no unresolved finding.
