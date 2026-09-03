#!/usr/bin/env python3
"""Build author-side V2.1 Historical Daily packets for 2026-08-01..15.

The script is deliberately downstream of the frozen official-owner replay.  It
does not discover, keyword-screen, score, or infer semantic decisions.  A day
is rendered only when every raw identity already has a human/agent-authored
title+abstract decision in ``semantic-screening-author.json``.  Empty owner
days are the sole exception because their 0/0 decision set is mechanically
closed without a semantic classification.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
MONTH = ROOT / "papers/2026/08"
REPLAY = MONTH / "_sources/arxiv-owner-replay-20260903"
EXECUTED_AT = "2026-09-03T06:22:39Z"


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def digest_json(payload: object) -> str:
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(canonical.encode()).hexdigest()


def strict_window(report_date: str) -> tuple[str, str]:
    day = datetime.strptime(report_date, "%Y-%m-%d")
    start = day - timedelta(days=1)
    return start.strftime("%Y-%m-%dT09:00:00+08:00"), day.strftime("%Y-%m-%dT09:00:00+08:00")


def zero_day(report_date: str) -> None:
    key = report_date.replace("-", "")
    packet = REPLAY / key
    inventory_path = packet / "raw-inventory-reconciliation.json"
    owner_path = packet / "official-arxiv-first-announcement-reconciliation.json"
    inventory = json.loads(inventory_path.read_text())
    owner = json.loads(owner_path.read_text())
    if inventory["raw_identity_count"] != 0 or inventory["identities"]:
        raise ValueError(f"{report_date} is not an empty owner day")

    start, end = strict_window(report_date)
    denominator_id = digest_json({"report_date": report_date, "candidate_family_ids": []})
    screening = {
        "schema": "semantic-screening-ledger-v2.1-author",
        "report_date": report_date,
        "window": {"start": start, "end": end, "semantics": "left_closed_right_open"},
        "decision_policy": "complete title+abstract semantic review; no keyword closure, sampling, or template reasons",
        "raw_identity_count": 0,
        "screened_identity_count": 0,
        "candidate_denominator": 0,
        "pre_denominator_closures": 0,
        "withdrawn_primary_sources": [],
        "denominator_id": denominator_id,
        "weekly_dependency_count": 0,
        "author_status": "complete",
        "fresh_context_false_positive_false_negative_audit": "pending",
        "identities": [],
    }
    dump(packet / "semantic-screening-author.json", screening)
    dump(packet / "coverage-receipt.json", {
        "schema": "coverage-receipt-v2.1-author",
        "report_date": report_date,
        "source_id": "SRC-ARXIV",
        "window_start": start,
        "window_end": end,
        "registered_identities": 0,
        "full_semantic_screened": 0,
        "retained": 0,
        "pre_denominator_closed": 0,
        "withdrawn": 0,
        "blocked": 0,
        "pagination_closed": True,
        "author_status": "closed",
        "semantic_audit_status": "pending",
        "executed_at": EXECUTED_AT,
    })
    dump(packet / "exact-v1-review-packet.json", {
        "schema": "exact-v1-review-packet-v2.1-author",
        "report_date": report_date,
        "author_status": "complete",
        "semantic_audit_status": "pending",
        "candidate_count": 0,
        "complete_count": 0,
        "blocked_count": 0,
        "withdrawn_pre_denominator": [],
        "items": [],
    })
    dump(packet / "books-current-content-comparison.json", {
        "schema": "books-current-content-comparison-v2.1-author",
        "report_date": report_date,
        "status": "not_required_empty_denominator",
        "items": [],
    })
    dump(packet / "BOOKS_WRITEBACK_QUEUE.json", {
        "schema": "books-writeback-queue-v2.1",
        "report_date": report_date,
        "status": "empty_pending_books_gate",
        "items": [],
    })
    dump(packet / "materials-request.json", {
        "schema": "materials-request-v2.1",
        "report_date": report_date,
        "items": [],
        "status": "not_required",
    })
    dump(packet / "weekly-dependency-audit.json", {
        "schema": "weekly-dependency-audit-v1",
        "report_date": report_date,
        "dependency_count": 0,
        "status": "passed",
        "note": "Historical Daily discovery, denominator, evidence, and Books queue did not use Weekly.",
    })

    owner["semantic_screening_complete"] = True
    owner["author_evidence_status"] = "complete"
    owner["fresh_context_semantic_audit"] = "pending"
    dump(owner_path, owner)
    inventory["semantic_status"] = "author_complete"
    inventory["screening_ledger"] = "semantic-screening-author.json"
    inventory["screened_identity_count"] = 0
    inventory["candidate_denominator"] = 0
    inventory["pre_denominator_closures"] = 0
    inventory["denominator_id"] = denominator_id
    dump(inventory_path, inventory)

    readme = f"""# Daily Research — {report_date}

**Research Date:** {report_date}

**Timezone:** Asia/Shanghai

**Strict Window:** {start[:10]} 09:00:00 ～ {end[:10]} 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；Weekly dependency=0

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；作者侧 0/0 Evidence 已闭合，等待 fresh-context Semantic Audit，Books 未执行写回

## Executive Summary

本窗口 official owner raw identities=0，title+abstract semantic screening=0/0；Candidate Denominator=0，pre-denominator closures=0，exact-v1 Review=0/0。官方 owner receipt 的 pagination 已闭合，因此这是显式 `no_hit`，不是缺失日报或空泛“无更新”。

作者侧没有发现可进入候选分母的 Source Family，也没有生成 Score V2、Source Review、Deep Analysis 或 Books 写回。四域 fresh-context Semantic Audit 尚未执行，三个 Gate 依合同保持 `Open`。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | {report_date} |
| Window End | {report_date} |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {denominator_id} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | {start} | {end} | {EXECUTED_AT} | DataCite 10.48550 initial created-day inventory reconciled to official arXiv first-announcement owner; registered arXiv categories | no_hit | 0 | — | pages=165 monthly content snapshots; final_cursor=end; owner_rows=0; screened=0 | {end} | papers/2026/08/_sources/arxiv-owner-replay-20260903/{key}/official-arxiv-first-announcement-reconciliation.json; papers/2026/08/_sources/arxiv-owner-replay-20260903/{key}/raw-inventory-reconciliation.json; papers/2026/08/_sources/arxiv-owner-replay-20260903/{key}/semantic-screening-author.json; coverage:SRC-ARXIV:{key} | — |

<!-- coverage:SRC-ARXIV:{key}:start -->Official first-announcement owner replay returned zero registered identities and a closed pagination receipt. The 0/0 semantic ledger is complete without classification; no Weekly content supplied discovery, filtering, scoring, Review, or Books evidence.<!-- coverage:SRC-ARXIV:{key}:end -->

### Coverage Limitations

- `SRC-ARXIV` 的 official owner replay 是本窗口唯一确定性分母；DataCite timestamp 仅用于 identity recovery，不代替 first-public owner proof。
- `docs/RESEARCH_SOURCES.md` 当前固定来源在 2026-08-25 生效，不反推为本历史日的 Required Daily。
- fresh-context coverage audit 尚未执行，所以作者侧收据闭合不等于 `Coverage Gate=Closed`。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

None — zero owner identities in this strict window.

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Source Reviews

None — denominator is empty.

## 4. Benchmark Contracts

None — no retained family and no benchmark claim.

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |

None — eligibility pool is empty.

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None — empty denominator. `BOOKS_WRITEBACK_QUEUE.json` is empty and Books Gate remains Open pending independent audit.

## 7. Semantic Audit

<!-- author-evidence:{key}:start -->Author-side 0/0 coverage, screening, exact-v1, selection, and empty Books queue receipts are complete. Independent semantic review has not started.<!-- author-evidence:{key}:end -->

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-{key}-COVERAGE | fresh-context:pending-independent-reviewer | coverage | coverage:SRC-ARXIV:{key}; author-evidence:{key} | PENDING-SA-{key}-COVERAGE | Pending — independent reviewer must verify the zero-owner receipt and Effective Date boundary | open |
| SA-{key}-EVIDENCE | fresh-context:pending-independent-reviewer | evidence | validator:review-completion-v1; author-evidence:{key} | PENDING-SA-{key}-EVIDENCE | Pending — independent reviewer must verify that the empty denominator requires no Review | open |
| SA-{key}-SELECTION | fresh-context:pending-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | PENDING-SA-{key}-SELECTION | Pending — independent reviewer must verify the empty eligibility pool | open |
| SA-{key}-BOOKS | fresh-context:pending-independent-reviewer | books | validator:books-comparison-v1; author-evidence:{key} | PENDING-SA-{key}-BOOKS | Pending — Books writeback is intentionally queued and not authorized in this Evidence rebuild | open |

## 8. Ignored Noise

None — raw owner identity count is zero.

## 9. Recommended Action

Fresh-context reviewer should verify the no-hit owner receipt and empty downstream ledgers. No Books writeback is queued for this date.

## 10. Repository Changes

- Rebuilt this Daily and its owner/evidence receipts from the official owner replay.
- Did not read or reuse Weekly evidence; did not modify Books, stage, commit, or push.

## 11. Open Questions

- Only the four fresh-context Semantic Audit scopes remain open; there is no candidate-level material blocker.

## 12. Sources

- [arXiv announcement schedule](https://info.arxiv.org/help/availability.html#announcement-schedule) — first-announcement owner semantics; accessed 2026-09-03.
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — version/effective date 2026-08-25.

## 13. Final Status

Completion=`In Progress`；Coverage=`Open`；Evidence=`Open`；Books=`Open`；Unresolved Findings=4。作者侧 raw=0、screened=0、retained=0、closures=0、exact-v1 reviews=0、blocked=0；等待 fresh-context Semantic Audit，不执行 Books 写回。
"""
    (MONTH / report_date[-2:] / "README.md").write_text(readme)


def pending_day(report_date: str) -> None:
    """Replace the invalid legacy-complete report with a truthful checkpoint."""
    key = report_date.replace("-", "")
    packet = REPLAY / key
    inventory_path = packet / "raw-inventory-reconciliation.json"
    owner_path = packet / "official-arxiv-first-announcement-reconciliation.json"
    inventory = json.loads(inventory_path.read_text())
    owner = json.loads(owner_path.read_text())
    rows = inventory["identities"]
    if not rows:
        raise ValueError(f"{report_date} is empty; use zero_day")
    start, end = strict_window(report_date)
    checkpoint_id = digest_json({"report_date": report_date, "pending_raw_family_ids": [row["source_family_id"] for row in rows]})
    authored: dict[str, dict] = {}
    for batch_path in sorted(packet.glob("semantic-decisions-batch-*.json")):
        batch = json.loads(batch_path.read_text())
        for decision in batch["rows"]:
            aid = decision["arxiv_id"]
            if aid in authored:
                raise ValueError(f"duplicate semantic decision for {aid}")
            authored[aid] = decision
    raw_ids = {row["arxiv_id"] for row in rows}
    unknown_ids = sorted(set(authored) - raw_ids)
    if unknown_ids:
        raise ValueError(f"semantic decisions not present in {report_date} raw inventory: {unknown_ids}")
    screened_count = len(authored)
    retained_count = sum(item["decision"] == "retain" for item in authored.values())
    closure_count = sum(item["decision"] == "pre_denominator_closure" for item in authored.values())
    decisions = []
    for raw in rows:
        authored_decision = authored.get(raw["arxiv_id"])
        if authored_decision:
            decisions.append({
                **raw,
                "semantic_decision": authored_decision["decision"],
                "semantic_reason": authored_decision["reason"],
                "proposed_stable_node_id": authored_decision.get("stable_node_id", "—"),
                "withdrawn_audit": "pending",
                "candidate_admission": "proposed_retained" if authored_decision["decision"] == "retain" else "proposed_pre_denominator_closure",
            })
        else:
            decisions.append({
                **raw,
                "semantic_decision": "pending",
                "semantic_reason": "Pending — full title+abstract semantic judgment has not yet been authored",
                "withdrawn_audit": "pending",
                "candidate_admission": "pending",
            })
    dump(packet / "semantic-screening-author.json", {
        "schema": "semantic-screening-ledger-v2.1-author",
        "report_date": report_date,
        "window": {"start": start, "end": end, "semantics": "left_closed_right_open"},
        "decision_policy": "complete title+abstract semantic review; no keyword closure, sampling, or template reasons",
        "raw_identity_count": len(rows),
        "screened_identity_count": screened_count,
        "proposed_retained_count": retained_count,
        "proposed_pre_denominator_closures": closure_count,
        "candidate_denominator": None,
        "pre_denominator_closures": None,
        "weekly_dependency_count": 0,
        "author_status": "in_progress",
        "fresh_context_false_positive_false_negative_audit": "not_started",
        "identities": decisions,
    })
    dump(packet / "coverage-receipt.json", {
        "schema": "coverage-receipt-v2.1-author",
        "report_date": report_date,
        "source_id": "SRC-ARXIV",
        "window_start": start,
        "window_end": end,
        "registered_identities": len(rows),
        "full_semantic_screened": screened_count,
        "retained": retained_count,
        "pre_denominator_closed": closure_count,
        "withdrawn": None,
        "blocked": 0,
        "pagination_closed": True,
        "author_status": "in_progress",
        "semantic_audit_status": "not_started",
        "executed_at": EXECUTED_AT,
    })
    dump(packet / "exact-v1-review-packet.json", {
        "schema": "exact-v1-review-packet-v2.1-author",
        "report_date": report_date,
        "author_status": "not_started_pending_denominator",
        "semantic_audit_status": "not_started",
        "candidate_count": None,
        "complete_count": 0,
        "blocked_count": 0,
        "withdrawn_pre_denominator": [],
        "items": [],
    })
    dump(packet / "BOOKS_WRITEBACK_QUEUE.json", {
        "schema": "books-writeback-queue-v2.1",
        "report_date": report_date,
        "status": "blocked_pending_evidence",
        "items": [],
    })
    dump(packet / "weekly-dependency-audit.json", {
        "schema": "weekly-dependency-audit-v1",
        "report_date": report_date,
        "dependency_count": 0,
        "status": "passed",
        "note": "Historical Daily discovery, denominator, evidence, and Books queue did not use Weekly.",
    })
    owner["semantic_screening_complete"] = False
    owner["author_evidence_status"] = "in_progress"
    owner["fresh_context_semantic_audit"] = "not_started"
    dump(owner_path, owner)
    inventory["semantic_status"] = "review_pending"
    inventory["screening_ledger"] = "semantic-screening-author.json"
    inventory["screened_identity_count"] = screened_count
    dump(inventory_path, inventory)

    readme = f"""# Daily Research — {report_date}

**Research Date:** {report_date}

**Timezone:** Asia/Shanghai

**Strict Window:** {start[:10]} 09:00:00 ～ {end[:10]} 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；Weekly dependency=0

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；official owner raw inventory 已闭合，逐行 title+abstract semantic screening={screened_count}/{len(rows)}，exact-v1 Review 尚未完成

## Executive Summary

本窗口 official owner raw identities={len(rows)}。owner identity 与 pagination 已由月级 replay 冻结，当前 title+abstract semantic screening={screened_count}/{len(rows)}，proposed retained={retained_count}、proposed closures={closure_count}；Candidate Denominator 尚未冻结。旧日报使用不同日期分桶与关键词路由得出的候选、分数、Review 和 Books disposition 均不再构成当前证据。

本 checkpoint 的作用是让每条 raw identity 显式进入待审 ledger，并把三个 Gate 恢复为真实 `Open`；它不把 pending 行伪装为 pre-denominator closure，也不执行 Score V2、Source Review 或 Books 写回。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | {report_date} |
| Window End | {report_date} |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {checkpoint_id} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | {start} | {end} | {EXECUTED_AT} | DataCite 10.48550 initial created-day inventory reconciled to official arXiv first-announcement owner; registered arXiv categories | incomplete | {len(rows)} | — | pages=165 monthly content snapshots; final_cursor=end; Pending — semantic_screened={screened_count}/{len(rows)} and candidate denominator not frozen | {end} | — | GAP-{key}-SEMANTIC-SCREEN |

<!-- coverage:SRC-ARXIV:{key}:start -->Official owner replay froze {len(rows)} unique identities and pagination is closed. Candidate-family closure remains incomplete because {len(rows) - screened_count} title+abstract judgments plus primary-status and FP/FN review are still pending in semantic-screening-author.json. Weekly dependency count is zero.<!-- coverage:SRC-ARXIV:{key}:end -->

### Coverage Limitations

- 当前缺口是 ordinary semantic-screening work，不是 external failure；因此 Result=`incomplete`、Coverage Gate=`Open`，不生成 Materials Request。
- `docs/RESEARCH_SOURCES.md` 当前固定来源在 2026-08-25 生效，不反推为本历史日的 Required Daily。
- 未读取或复用 Weekly；旧 Daily 的候选也不会作为当前 denominator seed。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

None yet — denominator cannot freeze before all {len(rows)} title+abstract decisions and withdrawn checks finish.

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Source Reviews

None yet — exact-v1 review is downstream of the frozen denominator.

## 4. Benchmark Contracts

None yet — denominator pending.

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |

None yet — evidence routing pending.

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None yet — Books queue is blocked on Evidence and Books Gate remains Open.

## 7. Semantic Audit

<!-- author-evidence:{key}:start -->Owner inventory is frozen, but semantic decisions, exact-v1 evidence, Selection, and Books comparison are incomplete.<!-- author-evidence:{key}:end -->

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-{key}-COVERAGE | fresh-context:pending-independent-reviewer | coverage | coverage:SRC-ARXIV:{key}; author-evidence:{key} | PENDING-SA-{key}-SCREENING | Pending — {len(rows) - screened_count} title+abstract decisions plus primary-status and FP/FN audit remain | open |
| SA-{key}-EVIDENCE | fresh-context:pending-independent-reviewer | evidence | validator:review-completion-v1; author-evidence:{key} | PENDING-SA-{key}-EVIDENCE | Pending — denominator, exact-v1 access, Score V2, and route-matched Reviews remain | open |
| SA-{key}-SELECTION | fresh-context:pending-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1; author-evidence:{key} | PENDING-SA-{key}-SELECTION | Pending — eligibility pool is not frozen | open |
| SA-{key}-BOOKS | fresh-context:pending-independent-reviewer | books | validator:books-comparison-v1; author-evidence:{key} | PENDING-SA-{key}-BOOKS | Pending — Books comparison and ordered queue are downstream of Evidence | open |

## 8. Ignored Noise

None declared yet. Pending rows are not noise closures.

## 9. Recommended Action

Continue the non-sampled, full-row semantic screen, then freeze the denominator and retrieve exact-v1 HTML/PDF for every retained family.

## 10. Repository Changes

- Replaced the stale complete claim with the current official-owner checkpoint and explicit per-identity pending ledger.
- Did not use Weekly evidence, modify Books, stage, commit, or push.

## 11. Open Questions

- {len(rows) - screened_count} title+abstract semantic decisions remain; all {len(rows)} primary-status checks and the final FP/FN audit remain ordinary work.

## 12. Sources

- [arXiv announcement schedule](https://info.arxiv.org/help/availability.html#announcement-schedule) — first-announcement owner semantics; accessed 2026-09-03.
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — version/effective date 2026-08-25.

## 13. Final Status

Completion=`In Progress`；Coverage=`Open`；Evidence=`Open`；Books=`Open`；Unresolved Findings=4。作者侧 raw={len(rows)}、screened={screened_count}、proposed retained={retained_count}、proposed closures={closure_count}、denominator=pending、exact-v1 reviews=0；不存在 external blocker，继续逐行重建。
"""
    (MONTH / report_date[-2:] / "README.md").write_text(readme)


def main() -> None:
    for day in (1, 2, 8, 9, 15):
        zero_day(f"2026-08-{day:02d}")
    for day in (3, 4, 5, 6, 7, 10, 11, 12, 13, 14):
        pending_day(f"2026-08-{day:02d}")


if __name__ == "__main__":
    main()
