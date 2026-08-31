# 2026-06-24 canonical presentation fresh audit v1

## Scope

This presentation-only audit compares the canonical report with the frozen date-local receipts after the post-write Books audit. It does not reopen the Candidate Denominator, Source Reviews, Books Decisions or shared Books writeback.

## Results

- Canonical top fields: `5/5` present and exact.
- Canonical H2 order: `14/14` exact (`Executive Summary` plus numbered sections `1`–`13`).
- Candidate / Review / Benchmark / Selection / Books rows: `43 / 43 / 43 / 43 / 43`.
- Selection: `3 selected / 40 not selected`; Books: `43 Integrate / 0 No Change`.
- Frozen Source Review bodies: `43/43` unchanged; aggregate SHA-256 `018b822f125ea6618200f9cff9187818a8a35adf4c398f3fd31b89139e3f6b0f`.
- Review Provenance IDs: `43/43` unchanged; aggregate SHA-256 `0d5b3c5ade7d4357c10f5d061747aa04f6a7f2c32653188b769cbf88fcaa3451`.
- Sources: `43/43` exact-v1 arXiv identities plus the source registry.
- Existing semantics remain `541 raw = 43 retained + 498 closures`, with `Coverage=Closed / Evidence=Passed / Books=Passed / Completion=Complete`.
- Shared Books, `docs/LEARNING_STATE.md` and the monthly index remain outside this renderer's write set.
- Unresolved presentation findings: `0`.

## Boundary

This receipt proves that the presentation migration preserved frozen evidence identity after the independent 43/43 post-write audit. It does not replace the report's Coverage, Evidence, Selection or Books semantic audits; machine validation does not establish the underlying research claims.
