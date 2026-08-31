# 2026-06-22 Candidate Denominator Fresh Audit

- Window: `[2026-06-21 09:00, 2026-06-22 09:00)` Asia/Shanghai.
- Denominator: `daily-v2.1:2026-06-22:7409eb001ec5b069`.
- Frozen arithmetic: `230 raw identities = 39 retained + 191 family-specific pre-denominator closures`.
- Retain rate: `16.96%`.
- Routes: Core `150`, keyword `22`, route-negative `58`; all `58/58` route-negative identities were independently checked and `5` were recovered.
- False-positive correction: late-index identity/title pairs were re-read against the frozen ledger before freezing; `2606.22734`, `2606.22738`, `2606.23741`, and `2606.23744` remain closed rather than being confused with adjacent retained identities.
- False-negative audit: `230/230` title+abstract rows and all route-negative rows have a decision and source-family-specific reason.
- Coverage Gate: **Closed**.
- Evidence, Selection, Books Gates: **Open**. Retention is permission to read exact-v1 evidence, not proof of a durable claim.
