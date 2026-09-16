# 2026-05-25 Fresh Non-author Final Review — Owner-day Isolation Fail

- Reviewer role: fresh non-author; not involved in the 05-25 author repair or root Books writeback.
- Review time: `2026-09-16T13:15:26+08:00`.
- Scope: only the frozen `499` identities, PrefBench recovery, terminal blocked slices, Books projection, five new bindings and current physical placement.
- Verdict: **Fail — keep Ongoing.**

## Checks that passed

- Frozen arithmetic is mechanically consistent: `499 = 281 retained + 218 pre-denominator closure + 0 withdrawn`.
- `2605.22855 PrefBench` has official arXiv OAI owner-day membership, exact `arXiv:2605.22855v1` HTML, `2+2+3=7`, a bounded adopted proposition, and a valid `No Change — Existing Coverage` comparison to Ch66.
- Evidence arithmetic is mechanically consistent: `281 = 278 complete + 3 blocked`; the three blocked families are exactly `2605.22834`, `2605.23491`, and `2605.23857`, and all three are `Deferred` with explicit materials requests.
- Books arithmetic is mechanically consistent: `281 = 52 Applied + 3 Deferred + 210 No Change — Existing Coverage + 9 Report Only + 7 Structural Candidate`.
- The five newly written bindings contain an adopted proposition, evidence boundary, trade-off, failure mode and fallback at the intended chapter location. `2605.23562` is outside and before the `daily-20260621` trace. Marker pairs are balanced.
- Queue counters are mechanically consistent and `pending_integration_count=0`; JSON parsing, report validator, marker inspection and scoped `git diff --check` pass.

## Blocking finding

The 97 DataCite-recovered arXiv identities have identity/version provenance only; official announcement membership was not independently recovered. Current Report contract requires such date-uncertain material to remain a terminal isolated item that does **not** support a positive candidate, Evidence, Books or coverage assertion.

The current projection does not satisfy that isolation:

- 97 ambiguous identities = 56 `retained` + 41 `pre_denominator_closure`.
- The 56 retained identities enter Evidence as 54 complete + 2 blocked.
- Their Books projection is 8 Applied + 2 Deferred + 44 No Change + 1 Report Only + 1 Structural Candidate.
- The eight Applied identities are `2605.22863`, `2605.22873`, `2605.22949`, `2605.22967`, `2605.23080`, `2605.23128`, `2605.23668`, and `2605.23826`.
- `2605.23128` is one of the five new bindings. Its prose and physical placement are sound, but this Daily cannot own or positively integrate it until official owner-day evidence is recovered or it is reassigned to a verified owner report.

Writing `owner-day 边界未证实` beside a candidate does not turn its positive Evidence/Books use into isolation. Therefore the current `281` candidate and `52 Applied` projections cannot be the final 05-25 Gate state.

## Exact bounded repair

Do not rerun or expand the 499-identity corpus.

1. Keep `499 = 402 official-day-owned + 97 owner-day-ambiguous` as the raw identity partition.
2. Move all 97 ambiguous identities to one terminal owner-day isolation state outside the Candidate Denominator. Preserve their title/abstract/exact-v1 work as reusable recovery evidence, but do not count it as this Daily's Evidence or Books decision.
3. Recompute the owned-day projection from the current files: `402 = 225 candidate + 177 pre-denominator closure`; Evidence becomes `225 = 224 complete + 1 blocked`; Books becomes `225 = 44 Applied + 1 Deferred + 166 No Change + 8 Report Only + 6 Structural Candidate`.
4. Quarantine the eight ambiguous Applied dependencies from this Daily. A binding may remain only after another report proves its official owner day and adopts it, or after official announcement membership for this window is recovered. Until then the semantic root queue is not zero, even though the mechanical queue says `pending_integration_count=0`.
5. For the five-new-binding slice, keep `2605.23482`, `2605.23562`, `2605.23565`, and `2605.23883` as passed. Reclassify only `2605.23128` as owner-day blocked; do not rewrite its mechanism text before provenance is resolved.
6. Update README candidate rows, conclusion, gaps, review statement and canonical JSON projections. Then obtain a different fresh non-author pass over only this owner-day repair.

The report remains `Ongoing`; this receipt does not authorize Books edits, staging, commit or push.
