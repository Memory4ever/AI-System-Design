# Nov21 actual query input supplement

Dalton; 2026-10-04T20:07:45+08:00. Only Planck DAY20:02's missing-input record repair. No new search, no API refetch, no inference from result titles. Inputs recovered from this author's actual local task rollout, thread01a105a2-ee88-78c0-9a07-829ac4011d23. [Preserved call records](QUERY_CALL_INPUTS.json) retain source path/line, call ID, original complete input, turn ID, Unix creation time and recorded UTC time. Creation/record times bound the enclosing execution cell; they are not invented exact nested network-request times. All requested five groups were recovered; none remains missing.

## Binding and Actual Parameters

All five search batches called `tools.web__run`, `response_length:"long"`; each `search_query` entry supplied only `q`. No separate `domains`, `recency`, pagination/cursor or date filter was passed. Dates/domain restrictions below are literal query text, not structured public-event filters. Each batch stopped at the returned first result set; no search-result pagination was executed in these calls. Raw JSON files already hold their actual returns and are unchanged; they alone did not prove these inputs.

| group and bound raw return | source line / call ID | enclosing cell creation ～ recorded time, UTC |
| --- | --- | --- |
| Four initial date-discovery queries: [WEB_DATE_DISCOVERY_01](WEB_DATE_DISCOVERY_01.json) | 2809 / call_zc1gNmUGu0u7lbJIpFCuX05B; `store("21datedSearch",r)` | 2026-10-04T10:07:07.419237+00:00 ～ 10:07:47.028Z |
| Two CVE queries: [WEB_CVE_DATE_RECOVERY](WEB_CVE_DATE_RECOVERY.json) | 2891 / call_Z1i5TrV5hvwIoSWypDwVKkLL; `store("21cveDate",r)` | 2026-10-04T10:13:56.475214+00:00 ～ 10:14:10.099Z |
| Meta/Qwen two finite queries: [WEB_FINITE_RECOVERY_02](WEB_FINITE_RECOVERY_02.json) | 2980 / call_fBlUh7XzJZ4SnBcXkwEaf2CH; `store("21finiteRecovery2",r2)` | 2026-10-04T10:21:49.010523+00:00 ～ 10:22:06.953Z |
| Four specific arXiv/author-date recoveries, first batch: [WEB_DATE_RESTORE_ARXIV_01](WEB_DATE_RESTORE_ARXIV_01.json) | 3326 / call_LdBgF00NC5qw1fvDg8k2bufO; `store("21dateRestore1",s)` | 2026-10-04T10:46:41.283605+00:00 ～ 10:47:01.604Z |
| Four specific arXiv/author-date recoveries, second batch: [WEB_DATE_RESTORE_ARXIV_02](WEB_DATE_RESTORE_ARXIV_02.json) | 3416 / call_2rNM6vPaQ6CtCNimwSHh2pn9; `store("21dateRestore2",r)` | 2026-10-04T10:53:07.669621+00:00 ～ 10:53:28.516Z |

## Exact Runtime Query Strings

Initial date discovery,4:

```text
site:openai.com/index/ "November 20, 2025" research
site:anthropic.com "Nov 20, 2025" research
site:research.google "November 20, 2025"
site:blog.google "Nov 20, 2025" model
```

CVE,2:

```text
site:openai.com/policies/openai-cve-assignment-policy/ "2025-11-20" published
site:openai.com "CVE assignment policy" "November 20"
```

Meta/Qwen,2:

```text
site:ai.meta.com/research "November 20, 2025"
site:qwen.ai/blog "November 20" "2025"
```

The same Meta/Qwen cell also opened exactly `https://agent.minimax.io/docs/llms.txt`, `https://agent.minimax.io/docs/techblog.md`, and `https://research.google/blog/`; these three original opens are preserved in the full input rather than miscounted as queries. [WEB_FINITE_RECOVERY_01](WEB_FINITE_RECOVERY_01.json) is a different open-only recovery, not evidence for the two queries above.

Specific-date recovery first batch,4:

```text
"NorthPole" "November 20, 2025" site:research.ibm.com
"SkyRL-Agent" "Nov 20" 2025
"Tokenisation over Bounded Alphabets" November 2025
"Time dependent loss reweighting" November 2025
```

Specific-date recovery second batch,4:

```text
"SkyRL-Agent" site:skyrl.ai
"NorthPole" "2025" "November" site:research.ibm.com/blog
"Liars’ Bench" "2025" November
"EvoVLA" "2025-11"
```

The typographic apostrophe in Liars’ is present in the actual query, not silently normalized. The first recovery cell separately opened four specific abs pages before its search; the second separately opened two exact-v1 HTMLs after its search. Full originals remain in QUERY_CALL_INPUTS, but those opens do not add to the eight queries and do not prove public dates. All result/date/identity limitations and the32 potential-only dispositions remain unchanged. No schedule-generated09:00 or submitted→public inference is added.

## MiMo Narrow Stop Correction

Planck's [DAY_REVIEW](DAY_REVIEW.md)20:01:17 independently fetched and read [official native component](PLANCK_RAW_MIMO_NATIVE.js): More/Show less toggles existing `p.map` output through local `h`, with `u(e=>!e)`; it is not a pagination request and does not supply missing Blog dates. Therefore there is no executable More-fetch ordinary task. The precise external gap is the Blog target-date historical slice, not a More page. This independently checked interface fact is reused only for21; no other date's coverage is inferred.

Ready for Planck's narrow input/binding/stop and six-section recheck. Nano,32 complete abstracts/necessary reverse, withdrawals and other sources are not reopened. No Books/shared-state write, stage, commit or push.
