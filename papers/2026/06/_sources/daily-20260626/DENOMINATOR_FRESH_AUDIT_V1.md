# 2026-06-26 Candidate Denominator Fresh Audit

- Window: `[2026-06-25 09:00, 2026-06-26 09:00)` Asia/Shanghai.
- Denominator: `daily-v2.1:2026-06-26:48b4ead4054910a5`.
- Frozen arithmetic: `470 raw identities = 84 retained + 386 family-specific pre-denominator closures`.
- Retain rate: `17.87%`.
- Routes: Core `303`, keyword `60`, route-negative `107`; all `107/107` route-negative rows were re-read and `2` durable false negatives were recovered.
- False-positive audit: `89` proposed durable rows were re-read against explicit ownership/evaluation criteria; `5` model-local or benchmark-local rows were closed before freezing.
- False-negative audit: `470/470` title+abstract rows have an identity-specific decision and reason.
- Coverage Gate: **Closed**.
- Evidence, Selection, Books Gates: **Open**; denominator admission is permission to inspect exact v1, not proof.
