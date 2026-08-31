# 2026-06-29 canonical presentation fresh audit v1

## Scope

This presentation-only audit compares the canonical report with the frozen date-local receipts after the post-write Books audit. It does not reopen the Candidate Denominator, Source Reviews, Books Decisions or shared Books writeback.

## Results

- Canonical top fields: `5/5` present and exact.
- Canonical H2 order: `14/14` exact (`Executive Summary` plus numbered sections `1`–`13`).
- Candidate / Review / Benchmark / Selection / Books rows: `86 / 86 / 86 / 86 / 80`.
- Selection: `3 selected / 83 not selected`; Books: `13 Integrate / 67 No Change / 6 Weekly Only`.
- Recovered Source Review bodies: `86/86` re-frozen after candidate-ID, exact-v1 locator and body-hash reconciliation; aggregate SHA-256 `f9d976ae45912647be214fafdc33637ab2ea929c92f9b8fe45a6a82d7168ae0b`.
- Recovered Review Provenance IDs: `86/86` re-frozen after the same filesystem-loss recovery audit; aggregate SHA-256 `efd9a23ff89daf8cb0322d63662991c7cb105f0e4931e924895be3ee422ca83c`.
- Sources: `86/86` exact-v1 arXiv identities plus the source registry; five PDF fallback routes remain explicitly bounded in Review receipts.
- Existing semantics remain `262 raw = 86 retained + 176 closures`, with `Coverage=Closed / Evidence=Passed / Books=Passed / Completion=Complete`.
- Shared Books, `docs/LEARNING_STATE.md` and the monthly index remain outside this renderer's write set.
- Unresolved presentation findings: `0`.

## Boundary

The pre-loss byte seal could not be reconstructed from the zero-byte recovered files. This receipt therefore records an explicit recovery re-freeze: the candidate identity set, exact-v1 locator triples, receipt/body hashes and post-write Books ownership were independently reconciled before the new aggregate was accepted. It does not replace the report's Coverage, Evidence, Selection or Books semantic audits; machine validation does not establish the underlying research claims.
