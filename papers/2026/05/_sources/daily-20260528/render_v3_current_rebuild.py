#!/usr/bin/env python3
"""Superseded 2026-05-28 all-ambiguous rebuild.

Do not run this historical author script. Its blanket rejection of the 165
initial-registration recovery identities conflicts with the project authority
``ARXIV_ANNOUNCEMENT_PROVENANCE.md``. The current idempotent author repair is
``rebuild_owner_receipt_v3.py``.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


raise SystemExit(
    "superseded: run rebuild_owner_receipt_v3.py; the all-ambiguous owner model is invalid"
)


ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/28/README.md"
OWNER_RECEIPT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260528/arxiv-owner-receipt.json"

DATE = "2026-05-28"
WINDOW = "[2026-05-27T09:00:00+08:00,2026-05-28T09:00:00+08:00)"
CHECKED_AT = "2026-09-16T10:00:52+08:00"
MINIMAX_URL = "https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953"
MINIMAX_HASH = "baca8d9868acd714bb1644f2fd61eebb8484b08cc6cae6d8fcb4dad4c6c51823"
MINIMAX_ID = "SF-2026-MINIMAX-AGENT-TEAM"


def load(path: Path):
    return json.loads(path.read_text())


def dump(name: str, value) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


receipt = load(OWNER_RECEIPT)
ambiguous = sorted(receipt["identities"], key=lambda item: item["arxiv_id"])
assert len(ambiguous) == 835
assert len({item["arxiv_id"] for item in ambiguous}) == 835

ambiguous_items = []
for item in ambiguous:
    ambiguous_items.append(
        {
            "arxiv_id": item["arxiv_id"],
            "source_family_id": item["source_family_id"],
            "title": item["title"],
            "abstract": item["abstract"],
            "categories": item.get("categories", []),
            "owner_status": "owner_ambiguous_excluded_from_confirmed_raw",
            "screening_status": "not_adjudicated_owner_gate_precedes_contribution_gate",
            "prior_status": item.get("screening_status"),
            "prior_status_authority": "invalidated_not_reused",
            "forbidden_owner_fields_present": [
                key
                for key in (
                    "datacite_initial_created_timestamp",
                    "datacite_current_updated_timestamp_revision_only",
                    "v1_submission_timestamp_provenance_only",
                    "oai_current_datestamps",
                )
                if item.get(key) is not None
            ],
            "reviewed_fields": ["identity", "title", "full_abstract", "categories"],
            "terminal_reason": (
                "The saved identity/title/full abstract is usable as a retrieval lead, but no replayable official "
                "announcement/listing membership proves this family belongs to the strict 2026-05-28 window. "
                "It is outside confirmed raw and cannot support a candidate, closure, withdrawal-completeness, "
                "score, Evidence Review, Books Decision or no-omission claim."
            ),
            "reopen_condition": (
                "Provide an official arXiv announcement/category-list membership record for the 2026-05-27 "
                "20:00 ET batch, then run title+full-abstract contribution screening and, only if retained, "
                "withdrawal/exact-v1/score/Evidence/Books review. DataCite/OAI/submitted time or ID continuity "
                "is not an acceptable substitute."
            ),
        }
    )

minimax_event = {
    "source_family_id": MINIMAX_ID,
    "source_id": "SRC-MINIMAX",
    "event_identity": "official-web-release:minimax-agent-team:2026-05-27",
    "title": "MiniMax Agent Team: Built for Long-Running Tasks and Continuous Evolution",
    "source_url": MINIMAX_URL,
    "public_owner_time": "2026-05-27T00:00:00Z",
    "public_owner_time_asia_shanghai": "2026-05-27T08:00:00+08:00",
    "owner_evidence": (
        "Official page JSON-LD datePublished=2026-05-27T00:00:00.000Z, which converts to "
        "2026-05-27T08:00:00+08:00 and precedes this window by one hour."
    ),
    "screening_status": "out_of_window_previous_daily_reopen_clue",
    "terminal_reason": (
        "The official timestamp is outside the 2026-05-28 strict window. The numeric URL suffix is not an "
        "official owner field and cannot override JSON-LD. This event is not scored or reviewed for 05-28."
    ),
    "reopen_condition": "Reopen only the 2026-05-27 Daily for contribution/Evidence/Books review; do not expand the 05-28 window.",
    "reviewed_fields": ["title", "full_official_body", "official_json_ld", "linked product boundary"],
}

owner_evidence = {
    "schema": "daily-official-owner-batch-evidence-v3",
    "report_date": DATE,
    "window": WINDOW,
    "checked_at": CHECKED_AT,
    "official_schedule": "https://info.arxiv.org/help/availability.html",
    "scheduled_announcement": {
        "eastern": "2026-05-27T20:00:00-04:00",
        "utc": "2026-05-28T00:00:00Z",
        "asia_shanghai": "2026-05-28T08:00:00+08:00",
        "proof_scope": "cadence/time only; does not prove item membership",
    },
    "membership_status": "blocked_official_membership_not_replayable",
    "confirmed_arxiv_raw_count": 0,
    "owner_ambiguous_inventory_count": 835,
    "owner_ambiguous_inventory_ref": "screening-outcomes-v3.json#owner_ambiguous_items",
    "invalidated_receipt_ref": str(OWNER_RECEIPT.relative_to(ROOT)),
    "invalidated_receipt_routes": {
        "official_arxiv_oai_direct": 670,
        "datacite_initial_created_owner_proxy": 165,
        "authority": "metadata-only; neither route proves official announcement membership",
    },
    "forbidden_positive_owner_proxies": [
        "DataCite created/updated timestamp",
        "OAI current datestamp",
        "v1 submitted/updated timestamp",
        "contiguous or neighboring arXiv identifiers",
    ],
    "attempts": [
        {
            "url": "https://arxiv.org/list/cs/2605?skip=0&show=2000",
            "result": "official endpoint returned 404 on 2026-09-16",
        },
        {
            "url": "https://arxiv.org/list/cs/2605?skip=6000&show=2000",
            "result": "official endpoint returned Rate exceeded on 2026-09-16",
        },
        {
            "url": "https://export.arxiv.org/list/cs/2605?skip=0&show=2000",
            "result": "official export endpoint returned 404 on 2026-09-16",
        },
    ],
    "terminal_disposition": (
        "The 835 identities are preserved as owner-ambiguous materials and excluded from confirmed raw. "
        "This is a contract-permitted terminal isolation, not a zero-hit or no-omission assertion."
    ),
    "materials_request_ref": "materials-request-v3.json#MR-20260528-ARXIV-OFFICIAL-BATCH",
}

sources = [
    {
        "source_id": "SRC-OPENAI",
        "basis": "official Research index/RSS; bounded dated-index check",
        "result": "checked_no_window_event",
        "hits": 0,
        "limitation": "no assertion beyond visible dated research entries",
    },
    {
        "source_id": "SRC-ANTHROPIC",
        "basis": "official Research index; nearest visible research date 2026-05-22",
        "result": "checked_no_window_event",
        "hits": 0,
        "limitation": "date-only pages are not promoted across the 09:00 boundary",
    },
    {
        "source_id": "SRC-GOOGLE-AI",
        "basis": "official DeepMind publication pages",
        "result": "date_ambiguous_isolated",
        "hits": 0,
        "ambiguous_events": [
            {
                "title": "Realistic honeypot evaluations for scheming propensity",
                "url": "https://deepmind.google/research/publications/253391/",
                "displayed_date": "2026-05-28",
            },
            {
                "title": "Gram: Assessing sabotage propensities via automated alignment auditing",
                "url": "https://deepmind.google/research/publications/252981/",
                "displayed_date": "2026-05-28",
            },
        ],
        "limitation": "official pages disclose only the calendar date; 00:00-09:00 Asia/Shanghai membership is unproved",
    },
    {
        "source_id": "SRC-META-AI",
        "basis": "official Publications entry",
        "result": "limited",
        "hits": 0,
        "limitation": "stable dated listing unavailable; not used for positive no-hit",
    },
    {"source_id": "SRC-QWEN", "basis": "official article index; adjacent explicit date 2026-05-29", "result": "checked_no_window_event", "hits": 0, "limitation": "none"},
    {"source_id": "SRC-DEEPSEEK", "basis": "official Research/News; adjacent visible dates outside window", "result": "checked_no_window_event", "hits": 0, "limitation": "none"},
    {"source_id": "SRC-MOONSHOT", "basis": "official Kimi Platform Blog; research/release/RFC slice", "result": "checked_no_window_event", "hits": 0, "limitation": "none"},
    {"source_id": "SRC-TENCENT-HUNYUAN", "basis": "official Research publicList and linked primary artifacts", "result": "checked_no_window_event", "hits": 0, "limitation": "visible dated records outside window"},
    {"source_id": "SRC-ZAI", "basis": "official Research/release index; adjacent explicit dates outside window", "result": "checked_no_window_event", "hits": 0, "limitation": "none"},
    {"source_id": "SRC-BYTEDANCE-SEED", "basis": "official Research/Public Papers; adjacent explicit date 2026-05-29", "result": "checked_no_window_event", "hits": 0, "limitation": "none"},
    {"source_id": "SRC-BAIDU-ERNIE", "basis": "official technical Blog; latest visible pre-window date 2026-05-09", "result": "checked_no_window_event", "hits": 0, "limitation": "none"},
    {"source_id": "SRC-XIAOMI-MIMO", "basis": "official paper/blog cards", "result": "limited", "hits": 0, "limitation": "undated cards cannot support a day-level no-hit"},
    {
        "source_id": "SRC-MINIMAX",
        "basis": "official Research/Blog page and JSON-LD datePublished",
        "result": "checked_no_window_event",
        "hits": 0,
        "out_of_window_event_source_family_ids": [MINIMAX_ID],
        "limitation": "official 2026-05-27T08:00:00+08:00 event belongs to the previous Daily and is only a 05-27 reopen clue",
    },
    {
        "source_id": "SRC-ARXIV",
        "basis": "official schedule proven; official announcement/list membership unavailable",
        "result": "owner_membership_blocked",
        "hits": 0,
        "limitation": "835 owner-ambiguous identities isolated; not a positive no-hit",
    },
]

source_coverage = {
    "schema": "daily-source-coverage-v3",
    "report_date": DATE,
    "window": WINDOW,
    "checked_at": CHECKED_AT,
    "source_count": 14,
    "institution_source_count": 13,
    "confirmed_institutional_event_count": 0,
    "date_ambiguous_institutional_event_count": 2,
    "out_of_window_previous_daily_event_count": 1,
    "sources": sources,
    "ordinary_commits_or_prs_expanded": False,
    "zero_omission_claim": False,
}

screening = {
    "schema": "daily-screening-outcomes-v3-author-rebuild",
    "report_date": DATE,
    "window": WINDOW,
    "checked_at": CHECKED_AT,
    "confirmed_raw_count": 0,
    "retained_count": 0,
    "pre_denominator_closure_count": 0,
    "withdrawn_count": 0,
    "confirmed_raw_conservation": "0 = 0 retained + 0 pre-denominator closure + 0 withdrawn",
    "surfaced_record_conservation": "838 = 0 confirmed raw + 835 arXiv owner-ambiguous + 2 Google date-ambiguous + 1 MiniMax previous-Daily clue",
    "retained_items": [],
    "date_ambiguous_items": [
        {
            "source_family_id": "SF-2026-GOOGLE-REALISTIC-HONEYPOT-EVALS",
            "title": "Realistic honeypot evaluations for scheming propensity",
            "source_url": "https://deepmind.google/research/publications/253391/",
            "displayed_date": "2026-05-28",
            "terminal_reason": "The official page exposes a calendar date but no timezone-bearing time; the date crosses the 09:00 Asia/Shanghai cutoff.",
            "reopen_condition": "Provide an official timezone-bearing publication timestamp; reopen this event only if its full interval lies inside the 05-28 window.",
        },
        {
            "source_family_id": "SF-2026-GOOGLE-GRAM-SABOTAGE-AUDIT",
            "title": "Gram: Assessing sabotage propensities via automated alignment auditing",
            "source_url": "https://deepmind.google/research/publications/252981/",
            "displayed_date": "2026-05-28",
            "terminal_reason": "The official page exposes a calendar date but no timezone-bearing time; the date crosses the 09:00 Asia/Shanghai cutoff.",
            "reopen_condition": "Provide an official timezone-bearing publication timestamp; reopen this event only if its full interval lies inside the 05-28 window.",
        },
    ],
    "out_of_window_previous_daily_items": [minimax_event],
    "owner_ambiguous_count": 835,
    "owner_ambiguous_items": ambiguous_items,
    "false_positive_negative_challenge": {
        "stale_positive_rows_invalidated": 91,
        "stale_negative_rows_invalidated": 744,
        "reason": (
            "The owner Gate precedes contribution screening. None of the 835 stale arXiv labels is copied as a candidate or closure; "
            "each is reopened only after official batch membership is proved. There is no confirmed 05-28 item to score."
        ),
        "confirmed_false_positive_count": 0,
        "confirmed_false_negative_count": 0,
    },
    "withdrawal_boundary": (
        "There is no confirmed raw item. No complete official withdrawal assertion is made for the 835 arXiv identities: "
        "owner ambiguity keeps them outside the denominator, and withdrawal "
        "must be checked after official batch membership is supplied."
    ),
}

evidence = {
    "schema": "daily-evidence-review-v3-author-rebuild",
    "report_date": DATE,
    "count": 0,
    "deep_complete_count": 0,
    "standard_complete_count": 0,
    "blocked_count": 0,
    "score_distribution": {},
    "items": [],
}

books = {
    "schema": "daily-books-comparison-v3-author-rebuild",
    "report_date": DATE,
    "count": 0,
    "no_change_count": 0,
    "pending_integrate_count": 0,
    "items": [],
}

queue = {
    "schema": "daily-root-books-writeback-queue-v3",
    "report_date": DATE,
    "status": "empty_no_confirmed_integrate",
    "pending_count": 0,
    "items": [],
    "note": "The author did not edit shared Books. There is no confirmed candidate; 835 owner-ambiguous arXiv identities and two Google date-ambiguous events cannot produce Books work.",
}

materials = {
    "schema": "daily-materials-request-v3",
    "report_date": DATE,
    "items": [
        {
            "request_id": "MR-20260528-ARXIV-OFFICIAL-BATCH",
            "priority": "blocking_only_for_ambiguous_slice",
            "source_id": "SRC-ARXIV",
            "affected_count": 835,
            "missing_material": (
                "Official arXiv category-list/announcement membership for the 2026-05-27 20:00 ET batch across "
                "cs.CL, cs.LG, cs.DC, cs.AI, cs.CV, cs.RO, cs.AR, cs.PL, cs.OS, cs.PF, cs.IR and cs.MA, including pagination."
            ),
            "why_existing_is_insufficient": "Saved DataCite/OAI/submitted metadata and numeric ID adjacency prove neither public announcement membership nor the strict 09:00 owner.",
            "acceptable_substitute": "Replayable official arXiv list HTML/snapshot or other official announcement record that enumerates membership; not a metadata-derived date proxy.",
            "reopen_scope": "Only the 835 owner-ambiguous identities, followed by current contribution/withdrawal/exact-v1/Books gates.",
        },
        {
            "request_id": "MR-20260528-GOOGLE-PUBLICATION-TIMES",
            "priority": "isolated_nonblocking",
            "source_id": "SRC-GOOGLE-AI",
            "affected_count": 2,
            "missing_material": "Official publication timestamps (with timezone) for DeepMind publications 253391 and 252981.",
            "why_existing_is_insufficient": "The pages expose only 2026-05-28; the strict window ends at 09:00 Asia/Shanghai.",
            "acceptable_substitute": "Official timestamped feed, changelog or page metadata.",
            "reopen_scope": "These two institution events only.",
        },
        {
            "request_id": "MR-20260528-META-DATED-LIST",
            "priority": "isolated_nonblocking",
            "source_id": "SRC-META-AI",
            "affected_count": None,
            "missing_material": "Stable official dated publications/release listing for the strict window.",
            "why_existing_is_insufficient": "The official entry was unavailable/unstable and cannot support a positive no-hit.",
            "acceptable_substitute": "Official dated index or release feed snapshot.",
            "reopen_scope": "Meta source only.",
        },
        {
            "request_id": "MR-20260528-MIMO-DAY-TIMES",
            "priority": "isolated_nonblocking",
            "source_id": "SRC-XIAOMI-MIMO",
            "affected_count": None,
            "missing_material": "Official day-level timestamps for undated MiMo cards visible near the window.",
            "why_existing_is_insufficient": "Undated cards cannot prove inclusion or absence within the strict Daily window.",
            "acceptable_substitute": "Official timestamped blog/paper page or release feed.",
            "reopen_scope": "MiMo undated cards only.",
        },
    ],
}

audit = {
    "schema": "daily-author-adversarial-audit-v3",
    "report_date": DATE,
    "status": "author_safe_terminal_pending_fresh_non_author",
    "challenges": {
        "owner": "835 stale identities were not admitted because official announcement membership is unavailable; forbidden proxies remain metadata only.",
        "arithmetic": "0 confirmed raw = 0 retained + 0 closure + 0 withdrawn; 838 surfaced = 835 arXiv ambiguous + 2 Google ambiguous + 1 MiniMax previous-Daily clue.",
        "false_positive": "All 91 stale positive labels were invalidated; none survives without owner proof. MiniMax was removed after UTC-to-Asia/Shanghai conversion placed it one hour before the window.",
        "false_negative": "All 744 stale negative labels were invalidated rather than treated as closure evidence; each shares an exact owner-proof reopen condition.",
        "evidence": "No confirmed candidate exists; Evidence count is zero. Ambiguous and out-of-window material is not promoted into review.",
        "books": "No confirmed candidate exists; Books comparison and root queue are empty.",
    },
    "gates": {
        "coverage": "AUTHOR_SAFE_TERMINAL_WITH_EXPLICIT_SOURCE_ISOLATION",
        "candidate_denominator": "AUTHOR_PASS_FOR_CONFIRMED_RAW",
        "evidence": "AUTHOR_PASS_ZERO_CANDIDATES",
        "books": "AUTHOR_PASS_ZERO_CANDIDATES_ZERO_INTEGRATE",
        "fresh_non_author": "PENDING",
    },
    "author_did_not_edit_shared_books": True,
    "cross_model_review": "not available in delegated non-interactive author lane; independent fresh non-author Gate remains mandatory",
}

dump("official-owner-batch-evidence-v3.json", owner_evidence)
dump("source-coverage-v3.json", source_coverage)
dump("screening-outcomes-v3.json", screening)
dump("evidence-review-v3.json", evidence)
dump("exact-v1-review-packet-v3.json", evidence)
dump("books-comparison-v3.json", books)
dump("root-books-writeback-queue-v3.json", queue)
dump("materials-request-v3.json", materials)
dump("author-adversarial-audit-v3.json", audit)

source_rows = []
for item in sources:
    if item["result"] == "checked":
        result = "已检查"
    elif item["result"] == "checked_no_window_event":
        result = "已检查"
    elif item["result"] == "date_ambiguous_isolated":
        result = "受阻"
    elif item["result"] == "owner_membership_blocked":
        result = "受阻"
    else:
        result = "受阻"
    source_rows.append(f"| {item['source_id']} | {item['basis']} | {result} | {item['limitation']} |")

report = f"""# Daily Research — 2026-05-28

**规范：** V3

**窗口：** 2026-05-27T09:00:00+08:00 ～ 2026-05-28T09:00:00+08:00

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** {CHECKED_AT}

> **Superseding notice（2026-09-16）：** 旧 V2.1 的 `835 raw / 117 candidate / Complete` 及 DataCite-created、OAI datestamp、submitted time owner 口径全部失效；旧评分、Evidence 与 Books disposition 均不继承。本页以下内容是当前 V3 author rebuild；仍需另一位 fresh non-author reviewer 才能 Complete。

## 1. 结论

当前可证明的 confirmed raw 为 **0 = 0 retained + 0 pre-denominator closure + 0 withdrawn**；因此 Evidence、score、Books comparison 与 root queue 均为 0，作者未编辑共享 Books。旧 835 个 arXiv identity 与两条 Google publication 只作为隔离材料存在，不能支撑候选或 no-hit。

旧 835 个 arXiv identity 只保留为 **owner-ambiguous terminal inventory**，不计入 raw、closure、withdrawn、candidate、score、Evidence 或 Books。官方 announcement/list membership 无法重放；schedule 只能证明 05-27 20:00 ET 存在公告时点，不能证明成员。DataCite/OAI/submitted time 与连续 ID 均未被用作替代 owner。旧 91 个正面标签和 744 个负面标签全部失效；每项只有在取得官方 membership 后才按当前贡献门槛重开。

MiniMax Agent Team 页面的官方 JSON-LD 为 `2026-05-27T00:00:00Z = 2026-05-27T08:00:00+08:00`，比本窗起点早一小时，因此只登记为 **2026-05-27 Daily 的定点 reopen clue**，不计入 05-28。URL 尾部数字不作为 owner 时间，不能覆盖官方日期字段。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{chr(10).join(source_rows)}

结构化记录见 [`source-coverage-v3.json`](../_sources/daily-20260528/source-coverage-v3.json)、[`official-owner-batch-evidence-v3.json`](../_sources/daily-20260528/official-owner-batch-evidence-v3.json) 与 [`screening-outcomes-v3.json`](../_sources/daily-20260528/screening-outcomes-v3.json)。Google 两条仅有 `2026-05-28` 日级日期，无法判断是否早于北京时间 09:00，故不作正面候选或 no-hit；Meta 与 MiMo 缺口同样隔离。普通 commit/PR 未扩入 denominator。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无。所有当前可见材料都因 owner/date 边界未进入本窗候选。

## 4. 证据与知识整合

无 confirmed candidate，因此没有合法的 exact-version Evidence、score 或 Books Decision。空集合见 [`evidence-review-v3.json`](../_sources/daily-20260528/evidence-review-v3.json)、[`books-comparison-v3.json`](../_sources/daily-20260528/books-comparison-v3.json) 与 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260528/root-books-writeback-queue-v3.json)。835+2 隔离项不得借用旧 exact-v1 locator 或 Books disposition；仅在 owner/date 证据到达后定点重开。

## 5. 缺口与下一步

- **arXiv 835 项：** 需要 2026-05-27 20:00 ET 官方 announcement/category-list 的逐项 membership 与 pagination；取得后仅重开这 835 项，再做贡献、withdrawal、exact-v1、score、Evidence 与 Books。DataCite/OAI/submitted time/连续 ID 均不可替代。
- **Google 2 项：** 需要 publication 253391、252981 的官方带时区时间戳；日级日期不支持跨 09:00 边界归属。
- **MiniMax Agent Team：** 官方时间属于 05-27 Daily；只重开 2026-05-27，不扩张 05-28。
- **Meta / MiMo：** 分别需要稳定的官方日级列表、未标日期卡片的官方时间；当前不用于正面 no-hit。

精确清单见 [`materials-request-v3.json`](../_sources/daily-20260528/materials-request-v3.json)。这些隔离项不阻塞 confirmed set 的 author-side safe terminal，但禁止“全来源无遗漏”断言。

## 6. 复核

- **复核者：** 待不同 fresh non-author reviewer。
- **结论：** 未通过（author-side 已到安全终态，fresh semantic Gate pending）。
- **作者检查范围：** Coverage=`AUTHOR_SAFE_TERMINAL_WITH_EXPLICIT_SOURCE_ISOLATION`；confirmed raw `0=0+0+0`；835 arXiv + 2 Google 隔离项不入分母；Evidence=`0`；Books/root queue=`0`，共享 Books 未修改。
- **机器检查：** JSON、集合算术、marker uniqueness、validator 与 scoped diff-check 的最终结果记录在 author checkpoint；机器通过不替代独立语义复核。
- **独立性边界：** 本轮作者不自签 Complete；fresh reviewer 必须挑战 MiniMax 前一日归属与 arXiv/Google/Meta/MiMo 隔离边界。
"""
REPORT.write_text(report)

checkpoint = f"""# 2026-05-28 V3 author rebuild checkpoint

## 冻结状态

- 日报：`Ongoing`；author-side safe terminal 已完成，fresh non-author Gate pending。
- 窗口：`{WINDOW}`。
- confirmed raw：`0 = 0 retained + 0 closure + 0 withdrawn`。
- owner-ambiguous：`835`，全部在 raw/candidate/closure/score/Evidence/Books 之外；旧 `91 positive + 744 negative` 标签全部失效。
- date-ambiguous：Google `2`，日级日期跨 09:00 cutoff，不支持 positive/no-hit。
- Evidence：`0 deep + 0 standard + 0 blocked`；score 为空。
- Books：`0 No Change + 0 Integrate`；root queue=`0`；作者未修改共享 Books。

## 前一日重开线索

- `{MINIMAX_ID}`：官方 `datePublished=2026-05-27T00:00:00Z = 2026-05-27T08:00:00+08:00`，比本窗起点早一小时；只重开 2026-05-27，不计 05-28。

## 隔离与重开

- `MR-20260528-ARXIV-OFFICIAL-BATCH`：需要官方 announcement/category-list membership；禁止 DataCite/OAI/submitted/连续 ID 代理。
- `MR-20260528-GOOGLE-PUBLICATION-TIMES`：需要两条 05-28 页面带时区时间。
- Meta/MiMo 入口缺口不支持正面 no-hit。

## 待办

由不同 fresh non-author reviewer 挑战 source boundary、MiniMax 前一日归属，以及 835+2 隔离是否完备。只有 fresh Gate 通过后才可 Complete。

## 作者侧校验

- `scripts/validate_research.py --report papers/2026/05/28/README.md`：通过，识别 1 份 V3 report。
- JSON parse、集合/算术/identity uniqueness：通过；`0=0+0+0`、835 arXiv unique、2 Google ambiguous、1 previous-Daily clue、Evidence/Books/queue 均为 0。
- marker uniqueness：Books 中 `{MINIMAX_ID}` marker 为 0，符合空 root queue；未编辑共享 Books。
- `git diff --check`（05-28 README + date-local sources）：通过。
- scoped status：只有 05-28 README 与 `daily-20260528` 新工件；仓库内其余并行改动未触碰。
"""
(HERE / "AUTHOR_V3_REBUILD_CHECKPOINT_20260916.md").write_text(checkpoint)

print(
    json.dumps(
        {
            "confirmed_raw": 0,
            "retained": 0,
            "closure": 0,
            "withdrawn": 0,
            "owner_ambiguous": 835,
            "date_ambiguous": 2,
            "previous_daily_reopen_clue": 1,
            "evidence": {"deep": 0, "standard": 0, "blocked": 0},
            "books": {"No Change — Existing Coverage": 0, "Integrate": 0},
            "root_queue": 0,
        },
        ensure_ascii=False,
    )
)
