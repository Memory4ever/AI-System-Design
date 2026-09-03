# Daily Latest-Contract Audit Ledger

- Audit version: `daily-latest-contract-readiness-v1`
- Generated at: `2026-09-03T03:04:07+00:00`
- Formal Daily reports: **218**
- Semantic rule: readiness is not acceptance; every row remains `fresh_context_reaudit=pending` until a new independent review closes it.

## Month Summary

| Month | Reports | Candidates | Integrate | Machine-ready | Reopen required | Pending / Conditional Families |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2025-05 | 4 | 74 | 11 | 0 | 4 | 1 |
| 2026-02 | 28 | 284 | 51 | 0 | 28 | 0 |
| 2026-03 | 31 | 507 | 48 | 6 | 25 | 1 |
| 2026-04 | 30 | 1004 | 38 | 0 | 30 | 0 |
| 2026-05 | 31 | 1975 | 536 | 0 | 31 | 0 |
| 2026-06 | 30 | 1507 | 728 | 0 | 30 | 0 |
| 2026-07 | 31 | 454 | 175 | 0 | 31 | 0 |
| 2026-08 | 31 | 275 | 80 | 1 | 30 | 0 |
| 2026-09 | 2 | 35 | 8 | 1 | 1 | 0 |

## Reopen Reasons

| Reason | Reports | Meaning |
| --- | ---: | --- |
| `arxiv_owner_date_receipt_missing` | 198 | 缺少冻结的官方 announcement/listing 收据；Submitted:v1 或 registry timestamp 不足以证明 Daily owner。 |
| `raw_inventory_missing` | 82 | 缺少可复算的原始枚举或 snapshot。 |
| `per_identity_closure_missing` | 80 | 没有为分母外 identity 保存逐项、family-specific closure。 |
| `screening_ledger_missing` | 48 | 缺少全量 title+abstract screening ledger。 |
| `source_packet_missing` | 20 | 对应来源包不存在，或只剩 0 字节空壳。 |
| `historical_daily_weekly_dependency` | 4 | Historical Daily 仍显式依赖旧 Weekly discovery/review。 |
| `embedded_semantic_audit_not_passed` | 1 | 报告内至少一个 Semantic Audit scope 未通过。 |

## Next Executable Checkpoint

| Action | Reports |
| --- | ---: |
| `recover_official_listing_owner_receipt` | 121 |
| `restore_or_replay_raw_inventory` | 82 |
| `fresh_context_semantic_reaudit` | 8 |
| `replay_full_semantic_screening` | 4 |
| `independent_historical_discovery_replay` | 3 |

## Report Ledger

| Date | Candidates / Reviews | Integrate | Packet Files (non-empty / empty) | Inventory | Screening | Closures | Interface | Readiness | Next Action | Semantic Reaudit | Issues |
| --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-05-01 | 19 / 19 | 3 | 181 / 1 | yes | yes | yes | pass | reopen_required | independent_historical_discovery_replay | pending | arxiv_owner_date_receipt_missing, historical_daily_weekly_dependency |
| 2025-05-02 | 17 / 17 | 5 | 170 / 1 | yes | yes | yes | pass | reopen_required | independent_historical_discovery_replay | pending | arxiv_owner_date_receipt_missing, historical_daily_weekly_dependency |
| 2025-05-03 | 24 / 24 | 3 | 196 / 1 | yes | yes | yes | pass | reopen_required | independent_historical_discovery_replay | pending | arxiv_owner_date_receipt_missing, historical_daily_weekly_dependency |
| 2025-05-04 | 14 / 14 | 0 | 173 / 1 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-01 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-02 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-03 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-04 | 36 / 36 | 6 | 908 / 66 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-05 | 23 / 23 | 1 | 851 / 58 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-06 | 9 / 9 | 0 | 816 / 58 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-07 | 15 / 15 | 2 | 823 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-08 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-09 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-10 | 12 / 12 | 4 | 815 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-11 | 27 / 27 | 3 | 873 / 64 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-12 | 13 / 13 | 2 | 817 / 60 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-13 | 11 / 11 | 1 | 817 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-14 | 25 / 25 | 2 | 859 / 60 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-15 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-16 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-17 | 9 / 9 | 5 | 813 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-18 | 16 / 16 | 2 | 845 / 66 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-19 | 6 / 6 | 0 | 807 / 66 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-20 | 9 / 9 | 2 | 811 / 62 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-21 | 6 / 6 | 1 | 807 / 60 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-22 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-23 | 0 / 0 | 0 | 791 / 56 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-24 | 4 / 4 | 2 | 811 / 62 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-25 | 18 / 18 | 4 | 838 / 68 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-26 | 12 / 12 | 4 | 819 / 68 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-27 | 13 / 13 | 2 | 831 / 62 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-02-28 | 20 / 20 | 8 | 849 / 72 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-01 | 0 / 0 | 0 | 17 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-02 | 0 / 0 | 0 | 23 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-03 | 0 / 0 | 0 | 30 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-04 | 33 / 33 | 3 | 171 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |
| 2026-03-05 | 23 / 23 | 4 | 126 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |
| 2026-03-06 | 20 / 20 | 1 | 122 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |
| 2026-03-07 | 31 / 31 | 2 | 161 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |
| 2026-03-08 | 0 / 0 | 0 | 22 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-09 | 22 / 22 | 3 | 131 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-10 | 33 / 33 | 2 | 170 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |
| 2026-03-11 | 41 / 41 | 3 | 191 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-12 | 33 / 33 | 3 | 133 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-13 | 31 / 31 | 2 | 133 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-14 | 0 / 0 | 0 | 124 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-15 | 0 / 0 | 0 | 68 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |
| 2026-03-16 | 30 / 30 | 3 | 147 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-03-17 | 30 / 30 | 0 | 116 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-03-18 | 13 / 13 | 0 | 94 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-03-19 | 13 / 13 | 1 | 95 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-03-20 | 19 / 19 | 0 | 120 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-03-21 | 0 / 0 | 0 | 52 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-03-22 | 0 / 0 | 0 | 32 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-03-23 | 15 / 15 | 1 | 89 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-03-24 | 34 / 34 | 1 | 155 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-03-25 | 21 / 21 | 6 | 168 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-03-26 | 12 / 12 | 1 | 130 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-03-27 | 14 / 14 | 3 | 122 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-03-28 | 0 / 0 | 0 | 20 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-03-29 | 0 / 0 | 0 | 20 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-03-30 | 11 / 11 | 1 | 88 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-03-31 | 28 / 28 | 8 | 194 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing |
| 2026-04-01 | 29 / 29 | 0 | 136 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-02 | 32 / 32 | 3 | 118 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-03 | 39 / 39 | 0 | 101 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-04 | 51 / 51 | 0 | 130 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-05 | 17 / 17 | 1 | 34 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-06 | 31 / 31 | 4 | 71 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-07 | 66 / 66 | 3 | 169 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-08 | 18 / 18 | 0 | 128 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-09 | 22 / 22 | 0 | 154 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-10 | 27 / 27 | 0 | 182 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-11 | 18 / 18 | 0 | 128 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-12 | 12 / 12 | 0 | 92 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-13 | 16 / 16 | 0 | 116 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-14 | 33 / 33 | 1 | 219 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-15 | 22 / 22 | 1 | 153 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-16 | 40 / 40 | 0 | 178 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-17 | 34 / 34 | 0 | 158 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-18 | 28 / 28 | 0 | 138 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-19 | 20 / 20 | 1 | 103 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-20 | 29 / 29 | 0 | 140 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-21 | 39 / 39 | 2 | 179 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-22 | 29 / 29 | 0 | 142 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-23 | 43 / 43 | 2 | 191 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-04-24 | 41 / 41 | 5 | 562 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-25 | 56 / 56 | 7 | 505 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-26 | 27 / 27 | 2 | 2855 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-27 | 20 / 20 | 1 | 2847 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-28 | 61 / 61 | 3 | 2915 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-29 | 50 / 50 | 0 | 111 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-04-30 | 54 / 54 | 2 | 2909 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-01 | 56 / 56 | 24 | 14 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-02 | 43 / 43 | 11 | 19 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-03 | 36 / 36 | 19 | 119 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-04 | 27 / 27 | 7 | 14 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-05 | 91 / 91 | 6 | 18 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-06 | 63 / 63 | 27 | 17 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-07 | 54 / 54 | 35 | 23 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-08 | 58 / 58 | 6 | 13 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-09 | 83 / 83 | 4 | 31 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-10 | 57 / 57 | 29 | 16 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-11 | 53 / 53 | 6 | 13 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-12 | 76 / 76 | 8 | 36 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-13 | 75 / 75 | 13 | 20 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-14 | 61 / 61 | 31 | 10 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-15 | 56 / 56 | 13 | 18 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-16 | 47 / 47 | 13 | 72 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-17 | 31 / 31 | 22 | 42 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-18 | 52 / 52 | 14 | 37 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-05-19 | 60 / 60 | 18 | 17 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-20 | 59 / 59 | 47 | 18 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-21 | 66 / 66 | 15 | 21 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-22 | 75 / 75 | 19 | 20 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-23 | 61 / 61 | 13 | 15 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-24 | 40 / 40 | 24 | 16 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-25 | 41 / 41 | 16 | 16 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-26 | 81 / 81 | 41 | 19 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-27 | 70 / 70 | 14 | 18 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-28 | 112 / 112 | 10 | 14 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-29 | 114 / 114 | 13 | 299 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-30 | 121 / 121 | 13 | 308 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-05-31 | 56 / 56 | 5 | 146 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-01 | 40 / 40 | 4 | 2 / 700 | no | yes | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-02 | 28 / 28 | 19 | 0 / 172 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-03 | 55 / 55 | 16 | 0 / 785 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-04 | 42 / 42 | 2 | 0 / 547 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing, historical_daily_weekly_dependency |
| 2026-06-05 | 64 / 64 | 8 | 0 / 700 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-06 | 51 / 51 | 23 | 0 / 25 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-07 | 23 / 23 | 6 | 23 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-08 | 42 / 42 | 9 | 0 / 20 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-09 | 15 / 15 | 14 | 0 / 19 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-10 | 44 / 44 | 9 | 0 / 99 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-11 | 31 / 31 | 26 | 0 / 91 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-12 | 36 / 36 | 32 | 0 / 30 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-13 | 38 / 38 | 14 | 0 / 15 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-14 | 41 / 41 | 37 | 0 / 12 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-15 | 39 / 39 | 36 | 0 / 11 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-16 | 63 / 63 | 61 | 0 / 13 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-17 | 43 / 43 | 41 | 0 / 11 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-18 | 37 / 37 | 16 | 0 / 14 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-19 | 68 / 68 | 56 | 0 / 16 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-20 | 65 / 65 | 44 | 0 / 16 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-06-21 | 37 / 37 | 20 | 15 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-22 | 39 / 39 | 29 | 15 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-23 | 92 / 92 | 58 | 18 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-24 | 43 / 43 | 43 | 17 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-25 | 68 / 68 | 63 | 17 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-26 | 84 / 84 | 7 | 187 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-27 | 64 / 64 | 14 | 147 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-28 | 65 / 65 | 6 | 151 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-29 | 86 / 86 | 13 | 18 / 0 | no | yes | yes | pass | reopen_required | restore_or_replay_raw_inventory | pending | raw_inventory_missing, arxiv_owner_date_receipt_missing |
| 2026-06-30 | 64 / 64 | 2 | 146 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-07-01 | 28 / 28 | 6 | 562 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-02 | 19 / 19 | 4 | 305 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-03 | 26 / 26 | 5 | 305 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-04 | 9 / 9 | 2 | 305 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-05 | 6 / 6 | 1 | 305 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-06 | 7 / 7 | 2 | 305 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-07 | 21 / 21 | 4 | 305 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-08 | 21 / 21 | 13 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-09 | 14 / 14 | 9 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-10 | 15 / 15 | 5 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-11 | 4 / 4 | 1 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-12 | 7 / 7 | 3 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-13 | 4 / 4 | 3 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-14 | 15 / 15 | 8 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-15 | 21 / 21 | 7 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-16 | 18 / 18 | 7 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-17 | 16 / 16 | 10 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-18 | 15 / 15 | 10 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-19 | 10 / 10 | 7 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-20 | 10 / 10 | 5 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-21 | 19 / 19 | 1 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-22 | 8 / 8 | 5 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-23 | 14 / 14 | 10 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-24 | 13 / 13 | 3 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-25 | 8 / 8 | 4 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-26 | 2 / 2 | 1 | 329 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-27 | 10 / 10 | 4 | 145 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-28 | 12 / 12 | 7 | 89 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-29 | 12 / 12 | 7 | 89 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-30 | 55 / 55 | 7 | 89 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-07-31 | 15 / 15 | 14 | 105 / 0 | yes | yes | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-01 | 9 / 9 | 3 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-02 | 2 / 2 | 0 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-03 | 4 / 4 | 3 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-04 | 7 / 7 | 0 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-05 | 11 / 11 | 3 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-06 | 15 / 15 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-07 | 4 / 4 | 2 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-08 | 4 / 4 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-09 | 6 / 6 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-10 | 14 / 14 | 2 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-11 | 4 / 4 | 2 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-12 | 6 / 6 | 2 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-13 | 7 / 7 | 0 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing, embedded_semantic_audit_not_passed |
| 2026-08-14 | 17 / 17 | 2 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-15 | 8 / 8 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-16 | 4 / 4 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-17 | 4 / 4 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-18 | 10 / 10 | 3 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-19 | 4 / 4 | 2 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-20 | 4 / 4 | 0 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-21 | 11 / 11 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-22 | 4 / 4 | 0 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-23 | 4 / 4 | 4 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-24 | 3 / 3 | 1 | 8 / 0 | yes | no | no | pass | reopen_required | recover_official_listing_owner_receipt | pending | screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-25 | 21 / 21 | 3 | 25 / 0 | yes | no | no | pass | reopen_required | replay_full_semantic_screening | pending | screening_ledger_missing, per_identity_closure_missing |
| 2026-08-26 | 21 / 21 | 11 | 44 / 0 | yes | no | no | pass | reopen_required | replay_full_semantic_screening | pending | screening_ledger_missing, per_identity_closure_missing |
| 2026-08-27 | 34 / 34 | 18 | 19 / 0 | yes | no | no | pass | reopen_required | replay_full_semantic_screening | pending | screening_ledger_missing, per_identity_closure_missing |
| 2026-08-28 | 29 / 29 | 12 | 8 / 33 | yes | no | no | pass | reopen_required | replay_full_semantic_screening | pending | screening_ledger_missing, per_identity_closure_missing |
| 2026-08-29 | 4 / 4 | 0 | 0 / 56 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-30 | 0 / 0 | 0 | 0 / 0 | no | no | no | pass | reopen_required | restore_or_replay_raw_inventory | pending | source_packet_missing, raw_inventory_missing, screening_ledger_missing, per_identity_closure_missing, arxiv_owner_date_receipt_missing |
| 2026-08-31 | 0 / 0 | 0 | 53 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |
| 2026-09-01 | 23 / 23 | 4 | 93 / 0 | yes | yes | yes | pass | reopen_required | recover_official_listing_owner_receipt | pending | arxiv_owner_date_receipt_missing |
| 2026-09-02 | 12 / 12 | 4 | 85 / 0 | yes | yes | yes | pass | ready_for_fresh_context_reaudit | fresh_context_semantic_reaudit | pending | — |

## Interpretation

- `ready_for_fresh_context_reaudit` 只表示现有报告和证据包足以进入新的独立语义复核，不表示语义已再次验收。
- `reopen_required` 表示至少一个 Coverage / denominator / report interface 机械前置条件缺失。
- 文件路径存在但大小为 0 时不构成 Receipt、Ledger 或 Primary Material；它只说明曾有恢复目标。
- 详细 validator findings、证据包路径和逐日报表位于同目录 `ledger.json`。
