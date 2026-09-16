#!/usr/bin/env python3
"""Render the 2026-05-24 V3 author recertification from preserved legacy receipts."""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
LOCAL = ROOT / "papers/2026/05/_sources/daily-20260524"
REPORT = ROOT / "papers/2026/05/24/README.md"
OWNER_ROOT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903"
CHECKED_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")


def write_json(name: str, value: object) -> None:
    (LOCAL / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


legacy = json.loads((LOCAL / "screening-ledger-final.json").read_text(encoding="utf-8"))
legacy_packet = json.loads((LOCAL / "exact-v1-review-packet.json").read_text(encoding="utf-8"))

owner_by_id: dict[str, str] = {}
for owner_day in ("20260525", "20260526", "20260527", "20260528", "20260529"):
    receipt = json.loads(
        (OWNER_ROOT / owner_day / "arxiv-owner-receipt.json").read_text(encoding="utf-8")
    )
    for item in receipt["identities"]:
        owner_by_id[item["arxiv_id"]] = receipt["report_date"]

crosswalk = []
owner_counts: Counter[str] = Counter()
for item in legacy["identities"]:
    arxiv_id = item["arxiv_id"]
    owner = owner_by_id.get(arxiv_id)
    bucket = owner or "later_2026_06_owner_day_not_resolved_in_this_date_scope"
    owner_counts[bucket] += 1
    crosswalk.append(
        {
            "arxiv_id": arxiv_id,
            "title": item["title"],
            "legacy_submitted_v1_utc": item.get("submitted_v1_utc"),
            "legacy_screening_status": item.get("screening_status"),
            "public_owner_day": owner,
            "migration_status": (
                "mapped_to_adjacent_official_owner_receipt"
                if owner
                else "excluded_from_2026-05-24_pending_later_owner_day_only"
            ),
            "reason": (
                "The official arXiv announcement schedule has no batch in the "
                "2026-05-24 Daily window; a submitted_v1 timestamp cannot own a public day."
            ),
        }
    )

packet_counts: Counter[str] = Counter()
packet_crosswalk = []
for item in legacy_packet:
    arxiv_id = item["arxiv_id"]
    owner = owner_by_id.get(arxiv_id)
    bucket = owner or "later_2026_06_owner_day_not_resolved_in_this_date_scope"
    packet_counts[bucket] += 1
    packet_crosswalk.append(
        {
            "arxiv_id": arxiv_id,
            "legacy_primary_evidence_version": item["primary_evidence_version"],
            "public_owner_day": owner,
            "current_2026_05_24_use": "excluded_not_reused",
        }
    )

owner_evidence = {
    "schema": "daily-owner-window-evidence-v3",
    "report_date": "2026-05-24",
    "window": {
        "start": "2026-05-23T09:00:00+08:00",
        "end_exclusive": "2026-05-24T09:00:00+08:00",
    },
    "arxiv": {
        "official_schedule": "https://info.arxiv.org/help/availability.html",
        "previous_announcement": {
            "eastern": "2026-05-21T20:00:00-04:00",
            "asia_shanghai": "2026-05-22T08:00:00+08:00",
            "relation": "before_window",
        },
        "next_announcement": {
            "eastern": "2026-05-24T20:00:00-04:00",
            "asia_shanghai": "2026-05-25T08:00:00+08:00",
            "relation": "after_window",
        },
        "raw_identity_count": 0,
        "proof_boundary": (
            "Scheduled public announcement owns the public day. submitted_v1, DataCite "
            "created/updated, and current OAI datestamps do not prove publication inside "
            "the strict window."
        ),
    },
    "institutional_confirmed_public_events": [],
    "institutional_isolated_boundary_families": [
        {
            "source_family_id": "SF-2026-ANTHROPIC-MYTHOS-GLASSWING-UPDATE",
            "source_id": "SRC-ANTHROPIC",
            "official_pages": [
                "https://www.anthropic.com/research/exploit-evals",
                "https://www.anthropic.com/research/glasswing-initial-update",
            ],
            "page_date": "May 22, 2026",
            "related_snapshot": {
                "url": "https://red.anthropic.com/2026/cvd/snapshots/2026-05-22-1027/about/",
                "generated_local_source_time": "2026-05-22T10:27:00-07:00",
                "asia_shanghai": "2026-05-23T01:27:00+08:00",
                "relation": "before_window",
            },
            "date_boundary": (
                "The two article pages expose only a calendar date and no timestamp/timezone. "
                "The related snapshot time does not prove the articles' publication time."
            ),
            "potential_contribution": (
                "A reproducible exploit-capability evaluation ladder and coordinated disclosure "
                "artifact may change security evaluation/release contracts if first-public is in-window."
            ),
            "status": "isolated_not_in_confirmed_denominator",
        }
    ],
    "event_type_scope": {
        "rule": (
            "Daily institution coverage is limited to official Research/Blog and clearly important "
            "release, RFC, or research artifacts. Ordinary GitHub commits and PRs are not enumerated."
        ),
        "ordinary_github_commit_or_pr_itemization": False,
    },
}

sources = [
    {
        "source_id": "SRC-OPENAI",
        "entry": "https://openai.com/news/rss.xml",
        "result": "checked",
        "basis": "Official Research/News feed: adjacent dated entries are May 22 00:00Z (before the window) and May 25.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-ANTHROPIC",
        "entry": "https://www.anthropic.com/research/exploit-evals ; https://www.anthropic.com/research/glasswing-initial-update",
        "result": "checked_with_isolated_gap",
        "basis": "Two related official research pages expose May 22 only; the 10:27 PT snapshot converts to May 23 01:27 BJT and is before the window, but does not prove article publication time.",
        "raw_families": 0,
        "limitation": "One linked event family lacks an official article timestamp/timezone and is isolated from the confirmed denominator.",
    },
    {
        "source_id": "SRC-GOOGLE-AI",
        "entry": "https://deepmind.google/research/publications/ ; https://research.google/pubs/",
        "result": "checked_with_isolated_gap",
        "basis": "Dated DeepMind Research entries bracket the target with May 19 and May 28.",
        "raw_families": 0,
        "limitation": "Some Google Publications records expose only year/venue; those records cannot support a day-level no-event claim.",
    },
    {
        "source_id": "SRC-META-AI",
        "entry": "https://ai.meta.com/research/publications/",
        "result": "blocked",
        "basis": "Official Publications directory returned an empty/internal-error response during this recertification.",
        "raw_families": 0,
        "limitation": "The response is not treated as proof that no event existed.",
    },
    {
        "source_id": "SRC-QWEN",
        "entry": "https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US",
        "result": "checked",
        "basis": "Official article indices bracket the target with May 20 10:00 and May 29 17:00.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-DEEPSEEK",
        "entry": "https://www.deepseek.com/news/",
        "result": "checked",
        "basis": "Official News/Research adjacent records are April 24 and June 24.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-MOONSHOT",
        "entry": "https://platform.kimi.com/blog",
        "result": "checked",
        "basis": "Official Blog has no dated event in the strict window.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-TENCENT-HUNYUAN",
        "entry": "https://api.hunyuan.tencent.com/api/blog/publicList",
        "result": "checked",
        "basis": "Official Research/Blog publicList contains five entries outside the target interval.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-ZAI",
        "entry": "https://www.zhipuai.cn/zh/research",
        "result": "checked",
        "basis": "Official Research entries bracket the target with May 20 and June 16.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-BYTEDANCE-SEED",
        "entry": "https://seed.bytedance.com/en/research ; https://seed.bytedance.com/en/public_papers",
        "result": "checked",
        "basis": "Official Research/Public Papers dated entries bracket the target with May 16 and May 29.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-BAIDU-ERNIE",
        "entry": "https://ernie.baidu.com/blog/zh/",
        "result": "checked",
        "basis": "Official technical Blog's nearest earlier dated entry is May 9; no in-window important release/research artifact was identified.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-XIAOMI-MIMO",
        "entry": "https://mimo.xiaomi.com/",
        "result": "checked_with_isolated_gap",
        "basis": "Dated papers bracket the target with March 13 and June 29.",
        "raw_families": 0,
        "limitation": "Blog cards are undated and are not used to assert day-level absence.",
    },
    {
        "source_id": "SRC-MINIMAX",
        "entry": "https://www.minimax.io/blog ; https://www.minimaxi.com/blog",
        "result": "checked",
        "basis": "Official Blog/Agent Tech Blog dated entries bracket the target with March 18 and May 26/27.",
        "raw_families": 0,
        "limitation": None,
    },
    {
        "source_id": "SRC-ARXIV",
        "entry": "https://info.arxiv.org/help/availability.html",
        "result": "checked",
        "basis": "No Friday/Saturday announcement; previous batch is May 22 08:00 BJT and next batch is May 25 08:00 BJT.",
        "raw_families": 0,
        "limitation": None,
    },
]

source_coverage = {
    "schema": "daily-source-coverage-v3-author-recertification",
    "report_date": "2026-05-24",
    "window": "[2026-05-23T09:00:00+08:00,2026-05-24T09:00:00+08:00)",
    "checked_at": CHECKED_AT,
    "scope_rule": (
        "Official Research/Blog and clearly important release/RFC/research artifacts only; "
        "ordinary GitHub commits/PRs are not expanded into the daily pool."
    ),
    "sources": sources,
    "checked_count": sum(item["result"] == "checked" for item in sources),
    "checked_with_isolated_gap_count": sum(
        item["result"] == "checked_with_isolated_gap" for item in sources
    ),
    "blocked_count": sum(item["result"] == "blocked" for item in sources),
    "confirmed_raw_family_count": 0,
    "isolated_boundary_family_count": 1,
    "zero_omission_claim": False,
}

screening = {
    "schema": "daily-screening-ledger-v3-author-recertification",
    "report_date": "2026-05-24",
    "window": "[2026-05-23T09:00:00+08:00,2026-05-24T09:00:00+08:00)",
    "confirmed_raw_identity_count": 0,
    "retained_count": 0,
    "pre_denominator_closure_count": 0,
    "withdrawn_count": 0,
    "evidence_complete_count": 0,
    "evidence_blocked_count": 0,
    "deep_review_count": 0,
    "standard_review_count": 0,
    "books_integrate_count": 0,
    "books_no_change_count": 0,
    "books_other_terminal_count": 0,
    "books_writeback_pending_count": 0,
    "confirmed_identities": [],
    "isolated_boundary_families": [
        "SF-2026-ANTHROPIC-MYTHOS-GLASSWING-UPDATE"
    ],
    "conservation": "0 = 0 retained + 0 pre-denominator closure + 0 withdrawn",
    "status": "author_gate_frozen_pending_fresh_non_author_review",
}

evidence = {
    "schema": "daily-exact-version-evidence-v3",
    "report_date": "2026-05-24",
    "candidate_count": 0,
    "deep_count": 0,
    "standard_count": 0,
    "blocked_count": 0,
    "items": [],
    "boundary_note": (
        "No confirmed in-window candidate exists. Legacy exact-v1 packets remain migration "
        "evidence only and are not Evidence Reviews for this Daily."
    ),
}

books = {
    "schema": "daily-books-current-content-comparison-v3",
    "report_date": "2026-05-24",
    "candidate_count": 0,
    "integrate_count": 0,
    "no_change_count": 0,
    "other_terminal_count": 0,
    "pending_count": 0,
    "items": [],
    "shared_books_modified_by_author": False,
}

queue = {
    "schema": "daily-root-books-writeback-queue-v3",
    "report_date": "2026-05-24",
    "status": "empty",
    "pending_count": 0,
    "items": [],
    "note": "No confirmed candidate produced a Books gap; the author did not modify shared Books.",
}

materials = {
    "schema": "daily-materials-request-v3",
    "report_date": "2026-05-24",
    "requests": [
        {
            "request_id": "MR-20260524-ANTHROPIC-ARTICLE-PUBLICATION-TIME",
            "source_family_id": "SF-2026-ANTHROPIC-MYTHOS-GLASSWING-UPDATE",
            "source_id": "SRC-ANTHROPIC",
            "known": [
                "https://www.anthropic.com/research/exploit-evals displays May 22, 2026",
                "https://www.anthropic.com/research/glasswing-initial-update displays May 22, 2026",
                "related snapshot generated May 22 10:27 PT = May 23 01:27 Asia/Shanghai, before the window",
            ],
            "missing": "official article publication timestamp and timezone, or an official timestamped feed/archive item",
            "why": "calendar-day labels and a related artifact timestamp cannot prove whether the article event fell before or inside the strict window",
            "acceptable_substitute": "official RSS/Atom/JSON publication timestamp, response metadata preserved by Anthropic, or a timestamped official announcement",
            "potential_review_scope": "If in-window, review the linked Mythos/Glasswing family as one event for exploit-capability evaluation, randomized-harness controls, coordinated disclosure boundaries, failure modes and fallback.",
            "current_disposition": "isolated_not_in_confirmed_denominator",
            "reopen": "only SF-2026-ANTHROPIC-MYTHOS-GLASSWING-UPDATE",
        },
        {
            "request_id": "MR-20260524-META-DATED-DIRECTORY",
            "source_family_id": None,
            "source_id": "SRC-META-AI",
            "known": ["https://ai.meta.com/research/publications/"],
            "missing": "readable official date-indexed publication directory for the strict window",
            "why": "an empty/internal-error response cannot establish absence",
            "acceptable_substitute": "official archive/export or individual official event pages that bound the window",
            "current_disposition": "coverage_gap_isolated",
            "reopen": "only SRC-META-AI for the strict window",
        },
        {
            "request_id": "MR-20260524-DATE-METADATA-LIMITS",
            "source_family_id": None,
            "source_id": "SRC-GOOGLE-AI,SRC-XIAOMI-MIMO",
            "known": ["https://research.google/pubs/", "https://mimo.xiaomi.com/"],
            "missing": "official day-level dates for Google Publications records and undated MiMo Blog cards",
            "why": "year/venue or undated cards cannot support a Daily no-event assertion",
            "acceptable_substitute": "official timestamped archive/feed or individual timestamped item pages",
            "current_disposition": "retrieval_limit_not_used_for_no-omission_claim",
            "reopen": "only matching item(s) in the strict window",
        },
    ],
}

migration = {
    "schema": "daily-v21-to-v3-owner-migration",
    "report_date": "2026-05-24",
    "legacy_ledger": "screening-ledger-final.json",
    "legacy_exact_v1_packet": "exact-v1-review-packet.json",
    "legacy_contract": legacy["schema"],
    "legacy_submitted_window_identity_count": len(legacy["identities"]),
    "legacy_candidate_count": legacy["candidate_denominator"],
    "current_public_owner_result": (
        "None of the legacy 289 identities is proven to belong to the 2026-05-24 "
        "public-announcement window."
    ),
    "owner_crosswalk_counts": dict(sorted(owner_counts.items())),
    "owner_crosswalk_sum": sum(owner_counts.values()),
    "legacy_exact_v1_crosswalk_counts": dict(sorted(packet_counts.items())),
    "legacy_exact_v1_crosswalk_sum": sum(packet_counts.values()),
    "policy": (
        "Legacy title/abstract, exact-version and Books work may be reused only by the real "
        "owner report after identity/version/claim/locator verification. No legacy Complete, "
        "Evidence, score or Books status is inherited here."
    ),
    "identities": crosswalk,
    "legacy_exact_v1_items": packet_crosswalk,
}

audit = {
    "schema": "daily-author-adversarial-audit-v3",
    "report_date": "2026-05-24",
    "auditor": "same author; not an independent reviewer",
    "method": (
        "Degraded doubt-driven self-review because this delegated author task does not "
        "authorize creating a fresh reviewer."
    ),
    "checks": [
        {
            "check": "owner boundary",
            "challenge": "Could weekend submissions or legacy exact-v1 files be mistaken for publication?",
            "result": "No. Official announcement cadence bounds arXiv raw=0; all 289 legacy identities are migrated away from this Daily.",
        },
        {
            "check": "institution event scope",
            "challenge": "Were ordinary GitHub commits/PRs expanded into the pool?",
            "result": "No. Only official Research/Blog and clearly important release/RFC/research artifacts were checked.",
        },
        {
            "check": "false negative",
            "challenge": "Could the Anthropic May 22 research pair belong to this strict window?",
            "result": "Yes, because the article pages are date-only. The family is isolated in a precise Materials Request and is not counted as closure or raw=0 proof.",
        },
        {
            "check": "false positive",
            "challenge": "Could a related snapshot timestamp admit the Anthropic articles?",
            "result": "No. The snapshot is before the window and does not establish the articles' publication instant.",
        },
        {
            "check": "Evidence and Books",
            "challenge": "Could migrated packets or a boundary family receive scores/Books decisions?",
            "result": "No. Confirmed candidate count is zero; Evidence, score and Books sets are empty; shared Books are untouched.",
        },
    ],
    "outcome": "author_gate_frozen_pending_fresh_non_author_review",
}

checkpoint = f"""# 2026-05-24 Daily V3 author recertification checkpoint

- Author checkpoint: `{CHECKED_AT}`
- Strict window: `[2026-05-23T09:00:00+08:00, 2026-05-24T09:00:00+08:00)`
- Confirmed public-owner arithmetic: `0 = 0 retained + 0 pre-denominator closure + 0 withdrawn`
- Evidence: `0 = 0 deep + 0 standard`; blocked candidate evidence: `0`
- Books: `0 Integrate + 0 No Change + 0 other terminal`; root queue: `0`; author Books edits: `0`
- Legacy migration: `289` submitted-window identities and `40` exact-v1 packet items are excluded from this Daily. Crosswalk is `263 -> 2026-05-26 + 2 -> 2026-05-27 + 3 -> 2026-05-28 + 1 -> 2026-05-29 + 20 -> later June owner day`.
- Isolated material: one Anthropic Mythos/Glasswing research-event family has only the page date `May 22, 2026`; the related snapshot time is before this window but cannot prove article publication time. Meta directory retrieval and Google/MiMo day-level metadata limits are separately isolated and do not support a zero-omission claim.
- Source scope: official Research/Blog and clearly important release/RFC/research artifacts only; ordinary GitHub commit/PR itemization was not performed.
- Status: `Ongoing`. The author Gate is frozen; a different fresh non-author reviewer must validate window ownership, the legacy crosswalk, isolated gaps and all zero sets before any `Complete` signature.
- Adversarial check: performed by the author in degraded self-review mode; it is not an independent semantic review and cannot sign completion.
- Git: not staged, committed or pushed.
"""

report = f"""# Daily Research — 2026-05-24

**规范：** V3
**窗口：** 2026-05-23T09:00:00+08:00 ～ 2026-05-24T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** {CHECKED_AT}

## 1. 结论

本次按当前 V3 合同重认证，不继承旧 V2.1 的 zero-denominator `Complete`。arXiv 的 owner 由官方 public announcement 决定：[官方 availability schedule](https://info.arxiv.org/help/availability.html)规定周五、周六不公告；前一批 `2026-05-21 20:00 EDT` 换算为北京时间 `2026-05-22 08:00`，早于本窗；下一批 `2026-05-24 20:00 EDT` 换算为北京时间 `2026-05-25 08:00`，晚于本窗。因此本窗确认 arXiv raw 为 0，submitted timestamp、DataCite `created/updated` 与旧 exact-v1 packet 都不承担 first-public 时间语义。

十四个日级来源按“官方 Research/Blog + 明确重要 release/RFC/research artifact”检查，没有把普通 GitHub commit/PR 逐项扩池。当前确认 public-owner 算术为 `0 = 0 retained + 0 pre-denominator closure + 0 withdrawn`；Evidence 为 `0 = 0 deep + 0 standard`，Books 为 `0 Integrate + 0 No Change + 0 其他终态`，root queue 为 0，作者未修改共享 Books。

这不是“零遗漏”断言。[Anthropic 的 exploit evaluation](https://www.anthropic.com/research/exploit-evals)与[Project Glasswing update](https://www.anthropic.com/research/glasswing-initial-update)只显示 `May 22, 2026`，没有文章时刻和时区；[关联 CVD snapshot](https://red.anthropic.com/2026/cvd/snapshots/2026-05-22-1027/about/)的 `May 22 10:27 PT` 换算为北京时间 `May 23 01:27`，虽早于窗起，却不能证明两篇文章何时发布。两页作为同一 Mythos/Glasswing event family 隔离，取得官方 article timestamp 后只重开该 family。

旧 ledger 的 289 项全部来自 submitted-window 口径；迁移对账为 `263 -> 05-26 + 2 -> 05-27 + 3 -> 05-28 + 1 -> 05-29 + 20 -> later June owner day = 289`。旧 40 项 exact-v1 packet 为 `37 -> 05-26 + 1 -> 05-29 + 2 -> later June owner day`，均不在本日继承评分、Evidence 或 Books 状态。逐项 title、旧状态与 owner mapping 见 [`legacy-v21-migration-v3.json`](../_sources/daily-20260524/legacy-v21-migration-v3.json)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 官方 Research/News feed；相邻条目为 05-22 00:00Z（窗前）与 05-25。 | 已检查 | 无 |
| `SRC-ANTHROPIC` | 官方 Research 两页与关联 CVD snapshot；snapshot 为北京时间 05-23 01:27，文章仅有日期。 | 受阻 | 缺官方文章 publication timestamp/timezone；该 family 已定点隔离，不能据 snapshot 推断文章时刻。 |
| `SRC-GOOGLE-AI` | DeepMind Research/Blog 相邻日为 05-19 与 05-28；Google Publications 目录只用于可判读日期。 | 受阻 | 部分 Publications 记录仅有年/venue，已定点隔离且不支持日级零遗漏断言。 |
| `SRC-META-AI` | 官方 Research/Publications 入口。 | 受阻 | 空响应/内部错误不能证明本窗无事件；需可读官方 archive。 |
| `SRC-QWEN` | 官方 article index；相邻记录为 05-20 10:00 与 05-29 17:00。 | 已检查 | 无 |
| `SRC-DEEPSEEK` | 官方 News/Research；相邻记录为 04-24 与 06-24。 | 已检查 | 无 |
| `SRC-MOONSHOT` | 官方 Kimi Platform Blog。 | 已检查 | 无本窗日期事件。 |
| `SRC-TENCENT-HUNYUAN` | 官方 Research/Blog `publicList` 五项。 | 已检查 | 五项日期均不在本窗。 |
| `SRC-ZAI` | 官方 Research；相邻记录为 05-20 与 06-16。 | 已检查 | 无 |
| `SRC-BYTEDANCE-SEED` | 官方 Research/Public Papers；相邻记录为 05-16 与 05-29。 | 已检查 | 无 |
| `SRC-BAIDU-ERNIE` | 官方技术 Blog；最近更早日期为 05-09。 | 已检查 | 无本窗重要 release/research artifact。 |
| `SRC-XIAOMI-MIMO` | 官方 Paper/Blog；有日期论文为 03-13 与 06-29。 | 受阻 | Blog cards 未给日级时间，已定点隔离且不用于零遗漏断言。 |
| `SRC-MINIMAX` | 官方英文/中文 Blog 与 Agent Tech Blog；相邻技术条目为 03-18 与 05-26/27。 | 已检查 | 无 |
| `SRC-ARXIV` | 官方 availability schedule；前批北京时间 05-22 08:00，后批 05-25 08:00。 | 已检查 | 无；旧 submitted-window identities 仅作迁移。 |

结构化来源记录见 [`source-coverage-v3.json`](../_sources/daily-20260524/source-coverage-v3.json)，严格窗口与 Anthropic 边界见 [`official-owner-window-evidence-v3.json`](../_sources/daily-20260524/official-owner-window-evidence-v3.json)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无确认在窗候选。没有把 submitted-time 条目、旧 exact-v1 packet 或日期未决 family 冒充候选。

## 4. 证据与知识整合

确认候选分母为 0，因此没有可执行的 exact-version Evidence Review、评分或 Books comparison。空 Evidence 集合见 [`exact-v1-evidence-v3.json`](../_sources/daily-20260524/exact-v1-evidence-v3.json)，空 Books 对读与队列分别见 [`books-current-content-comparison-v3.json`](../_sources/daily-20260524/books-current-content-comparison-v3.json)和 [`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260524/BOOKS_WRITEBACK_QUEUE_V3.json)。

Anthropic 边界 family 若取得在窗时刻，不得直接套用空集合：应重开 title + full abstract 贡献准入；若 retained，再读 exact-version 正文，审查 ExploitBench 任务分层、程序化验证、随机化布局、相同 harness、试验重复与 disclosure/fallback 边界，随后重新评分和对读唯一 Stable Knowledge Node。当前不预判 Books 结果。

## 5. 缺口与下一步

- `MR-20260524-ANTHROPIC-ARTICLE-PUBLICATION-TIME`：需要两篇文章的官方 publication timestamp/timezone，或官方 timestamped feed/archive。只重开 `SF-2026-ANTHROPIC-MYTHOS-GLASSWING-UPDATE`。
- `MR-20260524-META-DATED-DIRECTORY`：需要可读的官方日期目录或本窗逐项官方页面；不能把空响应写成 no hit。
- `MR-20260524-DATE-METADATA-LIMITS`：Google Publications 的 year/venue 与 MiMo undated cards 只作检索限制；取得日级材料后只重开命中的 item。
- 旧 289 项逐项 crosswalk 已冻结；真实 owner report 仅在 identity/version/claim/locator 仍一致时复用旧正文，不继承旧 `Complete`、评分或 Books 状态。

精确材料清单见 [`materials-request-v3.json`](../_sources/daily-20260524/materials-request-v3.json)。作者侧没有其他可执行 Evidence/Books 动作；当前保持 Ongoing，等待另一位 fresh non-author 独立复核窗口、迁移、边界隔离与全部空集合。

## 6. 复核

复核者：待 fresh non-author（不得由本报告作者自签）

结论：待复核

作者已完成严格 owner-window、十四源有界检查、legacy migration、confirmed denominator、空 Evidence/Books 集合与 Materials Request。本轮 doubt-driven 检查因 delegated author scope 未授权另开 reviewer，降级为作者侧反证复核，仅挑战周末 owner、Anthropic false negative、snapshot false positive 与旧 packet 误复用，不替代独立语义 Gate。完整记录见 [`author-adversarial-audit-v3.json`](../_sources/daily-20260524/author-adversarial-audit-v3.json)与 [`AUTHOR_V3_RECERTIFICATION_CHECKPOINT_20260915.md`](../_sources/daily-20260524/AUTHOR_V3_RECERTIFICATION_CHECKPOINT_20260915.md)。
"""

write_json("official-owner-window-evidence-v3.json", owner_evidence)
write_json("source-coverage-v3.json", source_coverage)
write_json("screening-ledger-v3.json", screening)
write_json("exact-v1-evidence-v3.json", evidence)
write_json("books-current-content-comparison-v3.json", books)
write_json("BOOKS_WRITEBACK_QUEUE_V3.json", queue)
write_json("materials-request-v3.json", materials)
write_json("legacy-v21-migration-v3.json", migration)
write_json("author-adversarial-audit-v3.json", audit)
(LOCAL / "AUTHOR_V3_RECERTIFICATION_CHECKPOINT_20260915.md").write_text(
    checkpoint, encoding="utf-8"
)
REPORT.write_text(report, encoding="utf-8")

print(
    json.dumps(
        {
            "checked_at": CHECKED_AT,
            "legacy_owner_counts": dict(sorted(owner_counts.items())),
            "legacy_packet_counts": dict(sorted(packet_counts.items())),
            "source_count": len(sources),
        },
        ensure_ascii=False,
    )
)
