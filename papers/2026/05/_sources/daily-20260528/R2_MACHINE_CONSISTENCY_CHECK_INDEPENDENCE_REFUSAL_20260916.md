# 2026-05-28 R2 Machine Consistency Check — Independence Refusal

- Check time: `2026-09-16T13:51:12+08:00`
- Checker role: machine-consistency reviewer only
- Independence boundary: this checker performed the first Gamma-World bounded repair and therefore is not a fresh semantic reviewer for the R2 artifact
- Result: `Machine consistency passed; final semantic sign-off refused`

## Checks that passed

- Screening conservation: `835 = 118 retained + 717 pre-denominator closure + 0 withdrawn`.
- Owner routes: `670 official_arxiv_oai_direct + 165 initial-registration recovery = 835`.
- Candidate identity sets are equal across screening, Evidence and Books: `118`.
- Evidence: `118 deep complete + 0 standard + 0 blocked`; score distribution is `{7: 6, 8: 92, 9: 20}`.
- Books: `18 Applied + 100 No Change`; root writeback queue has `18` applied projections and `0` pending.
- README candidate table and Source Review headings both contain `118` identities.
- All `18` Applied source-family markers are unique and occur before the owner chapter's canonical `## Review notes` boundary.
- Gamma-World has exactly one paired semantic binding and one source-family marker before Ch25 `## Review notes`.
- Gamma-World's README, screening, Evidence, exact-v1 packet, Books comparison and Ch25 body consistently separate virtual quantitative results from the qualitative dual-arm example.
- `validate_research.py`, all current V3 JSON parses and scoped `git diff --check` pass.

## Metadata finding

The R2 Markdown and JSON record `2026-09-16T15:45:00+08:00`, while their filesystem modification time is approximately `2026-09-16T13:38:22+08:00` and this check ran at `13:51:12+08:00`. This future timestamp is not a credible audit time and must be corrected by the next fresh reviewer when issuing the final receipt.

## Why this is not a final receipt

Machine consistency does not establish semantic correctness, and this checker participated in the R1 repair. The report must remain Ongoing. A reviewer who participated in neither the owner repair nor Gamma R1/R2 must challenge the R2 evidence boundary and then issue a correctly timestamped final receipt before marking the Daily Complete.
