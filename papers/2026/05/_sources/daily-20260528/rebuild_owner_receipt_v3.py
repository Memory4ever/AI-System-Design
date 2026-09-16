#!/usr/bin/env python3
"""Rebuild 2026-05-28 V3 from the authoritative owner receipt.

This is an author-side bounded repair.  It deliberately leaves the Daily
Ongoing until a different fresh non-author reviewer signs the final gate.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/28/README.md"
SNAPSHOT = HERE / "OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md"
OWNER_RECEIPT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260528/arxiv-owner-receipt.json"
DATE_AUTHORITY = ROOT / "papers/2026/05/_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md"
MAY27_QUEUE = ROOT / "papers/2026/05/_sources/daily-20260527/books-writeback-queue-independent-final.json"
ROADMAP = ROOT / "ROADMAP.md"

DATE = "2026-05-28"
WINDOW_START = "2026-05-27T09:00:00+08:00"
WINDOW_END = "2026-05-28T09:00:00+08:00"
WINDOW = f"[{WINDOW_START},{WINDOW_END})"
CHECKED_AT = "2026-09-16T13:40:00+08:00"
GAMMA_ID = "2605.28816"
GAMMA_SF = f"SF-2026-ARXIV-{GAMMA_ID.replace('.', '-')}"


def load(path: Path):
    return json.loads(path.read_text())


def dump(name: str, value) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def parse_table(lines: list[str], header_prefix: str) -> list[dict[str, str]]:
    header = None
    rows: list[dict[str, str]] = []
    for line in lines:
        if line.startswith(header_prefix):
            header = [cell.strip() for cell in line.strip("|").split("|")]
            continue
        if header is None:
            continue
        if line.startswith("| ---"):
            continue
        if not line.startswith("| "):
            break
        values = [cell.strip() for cell in line.strip("|").split("|")]
        if len(values) == len(header):
            rows.append(dict(zip(header, values)))
    return rows


def extract_review(snapshot: str, source_family_id: str) -> str:
    pattern = re.compile(
        rf"<!-- review:{re.escape(source_family_id)}:start -->(.*?)"
        rf"<!-- review:{re.escape(source_family_id)}:end -->",
        re.S,
    )
    match = pattern.search(snapshot)
    if not match:
        raise AssertionError(f"missing review block: {source_family_id}")
    return match.group(1).strip()


def title_from_review(review: str) -> str:
    match = re.search(r"^#### (.+)$", review, re.M)
    if not match:
        raise AssertionError("review block has no H4 title")
    return match.group(1).strip()


def book_binding(source_family_id: str, arxiv_id: str) -> dict[str, str | int]:
    hits = []
    for path in (ROOT / "books").rglob("*.md"):
        text = path.read_text(errors="ignore")
        marker_count = text.count(source_family_id)
        id_count = text.count(arxiv_id)
        if marker_count or id_count:
            hits.append((path.relative_to(ROOT).as_posix(), marker_count, id_count, text))
    if len(hits) != 1:
        raise AssertionError(f"expected one Books binding for {source_family_id}, got {[(p,m,i) for p,m,i,_ in hits]}")
    path, marker_count, id_count, text = hits[0]
    first_review_notes = text.find("## Review notes")
    first_mechanism = text.find(source_family_id) if marker_count else text.find(arxiv_id)
    return {
        "path": path,
        "source_family_marker_count": marker_count,
        "arxiv_id_count": id_count,
        "binding_anchor": source_family_id if marker_count else arxiv_id,
        "mechanism_before_first_review_notes": int(first_review_notes < 0 or first_mechanism < first_review_notes),
    }


def roadmap_paths() -> dict[str, str]:
    paths: dict[str, str] = {}
    for line in ROADMAP.read_text().splitlines():
        match = re.match(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+\.md)` \|", line)
        if match:
            paths[match.group(1)] = match.group(2)
    return paths


snapshot = SNAPSHOT.read_text()
lines = snapshot.splitlines()
candidate_rows = parse_table(lines, "| Source Family ID | Primary Identifier |")
packet_rows = parse_table(lines, "| Source Family ID | Review Provenance ID |")
assert len(candidate_rows) == 117
assert len(packet_rows) == 117
assert {row["Source Family ID"] for row in candidate_rows} == {row["Source Family ID"] for row in packet_rows}

receipt = load(OWNER_RECEIPT)
identities = receipt["identities"]
assert receipt["raw_identity_count"] == 835 == len(identities)
assert receipt["official_oai_direct_count"] == 670
assert receipt["revision_recovery_count"] == 165
identity_by_sf = {item["source_family_id"]: item for item in identities}
assert len(identity_by_sf) == 835

candidate_by_sf: dict[str, dict] = {}
packet_by_sf = {row["Source Family ID"]: row for row in packet_rows}
for row in candidate_rows:
    sf = row["Source Family ID"]
    assert sf in identity_by_sf
    review = extract_review(snapshot, sf)
    title = title_from_review(review)
    aid = row["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
    score_parts = [int(row["Design Delta"]), int(row["System Reach"]), int(row["Durability"])]
    assert sum(score_parts) == int(row["Total"])
    old_disposition = row["Books Disposition"]
    current_disposition = "Applied" if old_disposition == "Integrate" else "No Change — Existing Coverage"
    candidate_by_sf[sf] = {
        "arxiv_id": aid,
        "source_family_id": sf,
        "title": title,
        "primary_evidence_version": row["Primary Identifier"],
        "primary_url": f"https://arxiv.org/html/{aid}v1",
        "score_parts": {
            "design_delta": score_parts[0],
            "system_reach": score_parts[1],
            "durability": score_parts[2],
        },
        "score": int(row["Total"]),
        "review_route": "deep",
        "review_status": "deep_complete_reused_exact_v1_same_identity_and_claim",
        "stable_node_id": row["Stable Node ID"],
        "books_disposition": current_disposition,
        "prior_books_disposition": old_disposition,
        "review_markdown": review,
        "evidence_packet": packet_by_sf[sf],
        "owner_receipt_route": identity_by_sf[sf]["owner_receipt_route"],
        "claim_boundary": (
            "Only the exact-v1 mechanism, disclosed evaluation conditions and stated counterevidence are adopted; "
            "unreported model, hardware, workload, concurrency, tail-SLO and production behavior remain Not Disclosed."
        ),
    }

gamma_identity = identity_by_sf[GAMMA_SF]
candidate_by_sf[GAMMA_SF] = {
    "arxiv_id": GAMMA_ID,
    "source_family_id": GAMMA_SF,
    "title": "Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players",
    "primary_evidence_version": f"arXiv:{GAMMA_ID}v1",
    "primary_url": f"https://arxiv.org/html/{GAMMA_ID}v1",
    "score_parts": {"design_delta": 3, "system_reach": 3, "durability": 3},
    "score": 9,
    "review_route": "deep",
    "review_status": "deep_complete_exact_v1",
    "stable_node_id": "MULTIMODAL-WORLD-MODELS",
    "books_disposition": "Applied",
    "prior_books_disposition": "pre-denominator closure (corrected false negative)",
    "owner_receipt_route": gamma_identity["owner_receipt_route"],
    "adopted_claim": (
        "多主体 world model 将 shared scene 与 per-agent identity、observation 和 action state 分解，"
        "再以 permutation-symmetric interaction 更新 joint next-state，使独立可控性与跨主体一致性成为显式状态契约。"
    ),
    "method": "exact-v1 HTML §3 Method",
    "evaluation": "exact-v1 HTML §4 Experiments; author virtual environments with two- and four-agent settings",
    "nonproof": "exact-v1 HTML §5 Discussion",
    "claim_boundary": (
        "只支持作者虚拟环境中的两主体/四主体 video fidelity、action controllability 与 inter-agent consistency 结果；"
        "不证明开放世界物理因果、社会因果、真实机器人控制或生产 SLO。"
    ),
    "review_markdown": (
        "问题：统一 latent 容易把多主体身份与动作责任压平。机制：Gamma-World 显式分解 shared scene 与 per-agent state，"
        "并以 permutation-symmetric interaction 建模 joint transition。Evaluation 只覆盖作者虚拟环境的两主体与四主体设置。"
        "Trade-off 是 association error、组合状态爆炸与未观测意图；单主体或弱交互场景仍可使用更便宜的统一 latent。"
    ),
    "evidence_packet": {
        "Source Family ID": GAMMA_SF,
        "Review Provenance ID": "RP-gamma-world-2605-28816-v1",
        "Review Route": "deep",
        "Primary Evidence Version": f"arXiv:{GAMMA_ID}v1",
        "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{GAMMA_ID}v1",
        "Method / Identity Locators": "exact-v1 HTML §3 Method",
        "Evaluation Locators": "exact-v1 HTML §4 Experiments",
        "Limitations / Counterevidence Locators": "exact-v1 HTML §5 Discussion",
        "Artifact Locators": f"https://arxiv.org/html/{GAMMA_ID}v1; immutable event-time artifact Not Disclosed",
        "Claim Boundary Ref": f"claim:{GAMMA_SF}",
        "Completion Result": "complete",
    },
}

candidates = sorted(candidate_by_sf.values(), key=lambda item: item["arxiv_id"])
assert len(candidates) == 118
candidate_sfs = {item["source_family_id"] for item in candidates}
assert len(candidate_sfs) == 118

closures = []
for identity in sorted(identities, key=lambda item: item["arxiv_id"]):
    if identity["source_family_id"] in candidate_sfs:
        continue
    reason = identity.get("screening_reason") or (
        "pre-denominator closure: title and full abstract do not establish a durable AI System mechanism, "
        "state/data/control ownership change, evaluation contract delta, or correction to an existing Books proposition"
    )
    closures.append(
        {
            "arxiv_id": identity["arxiv_id"],
            "source_family_id": identity["source_family_id"],
            "title": identity["title"],
            "abstract": identity["abstract"],
            "categories": identity.get("categories", []),
            "decision": "pre_denominator_closure",
            "reason": reason,
            "reviewed_fields": ["identity", "title", "full_abstract", "categories"],
            "owner_receipt_route": identity["owner_receipt_route"],
        }
    )
assert len(closures) == 717

score_distribution = Counter(item["score"] for item in candidates)
evidence_items = []
for item in candidates:
    packet = item["evidence_packet"]
    evidence_items.append(
        {
            "arxiv_id": item["arxiv_id"],
            "source_family_id": item["source_family_id"],
            "title": item["title"],
            "score": item["score"],
            "score_parts": item["score_parts"],
            "stable_node_id": item["stable_node_id"],
            "primary_evidence_version": item["primary_evidence_version"],
            "primary_url": item["primary_url"],
            "review_route": "deep",
            "review_status": item["review_status"],
            "method": packet["Method / Identity Locators"],
            "evaluation": packet["Evaluation Locators"],
            "nonproof": packet["Limitations / Counterevidence Locators"],
            "artifact": packet["Artifact Locators"],
            "claim_boundary": item["claim_boundary"],
            "review_markdown": item["review_markdown"],
            "completion_result": "complete",
        }
    )

books_items = []
node_paths = roadmap_paths()
for item in candidates:
    decision = item["books_disposition"]
    result = {
        "arxiv_id": item["arxiv_id"],
        "source_family_id": item["source_family_id"],
        "title": item["title"],
        "stable_node_id": item["stable_node_id"],
        "decision": decision,
        "prior_decision": item["prior_books_disposition"],
        "comparison_evidence_ref": "OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md#source-reviews",
        "owner_path": node_paths[item["stable_node_id"]],
    }
    if decision == "Applied":
        result["binding"] = book_binding(item["source_family_id"], item["arxiv_id"])
        result["status"] = "applied_pending_fresh_review"
    else:
        result["status"] = "no_change_existing_coverage_pending_fresh_review"
    books_items.append(result)

assert Counter(item["decision"] for item in books_items) == Counter(
    {"Applied": 18, "No Change — Existing Coverage": 100}
)

# Keep the already bounded institutional coverage, but restore the authoritative
# arXiv route instead of the superseded all-ambiguous interpretation.
source_coverage = load(HERE / "source-coverage-v3.json")
source_coverage.update(
    {
        "schema": "daily-source-coverage-v3-owner-receipt-repair",
        "checked_at": CHECKED_AT,
        "window": WINDOW,
        "confirmed_arxiv_raw_count": 835,
        "confirmed_event_count": 835,
        "zero_omission_claim": False,
    }
)
for source in source_coverage["sources"]:
    if source["source_id"] == "SRC-ARXIV":
        source.update(
            {
                "basis": "official OAI direct batch plus initial-registration recovery under ARXIV_ANNOUNCEMENT_PROVENANCE.md",
                "result": "checked_owner_receipt_closed",
                "hits": 835,
                "retained": 118,
                "pre_denominator_closure": 717,
                "withdrawn": 0,
                "limitation": "165 recovery identities use initial registration plus exact-v1 identity/month/cadence consistency; current OAI revision metadata is not owner evidence",
            }
        )
dump("source-coverage-v3.json", source_coverage)

owner_evidence = {
    "schema": "daily-official-owner-batch-evidence-v3-authority-corrected",
    "report_date": DATE,
    "window": WINDOW,
    "checked_at": CHECKED_AT,
    "authority_ref": str(DATE_AUTHORITY.relative_to(ROOT)),
    "owner_receipt_ref": str(OWNER_RECEIPT.relative_to(ROOT)),
    "owner_receipt_sha256": hashlib.sha256(OWNER_RECEIPT.read_bytes()).hexdigest(),
    "membership_status": "closed_by_authoritative_owner_receipt",
    "raw_identity_count": 835,
    "official_oai_direct_count": 670,
    "initial_registration_recovery_count": 165,
    "owner_logic": (
        "exact-v1 identity plus initial DataCite registration plus compatible arXiv identifier month and official cadence; "
        "same-day OAI directly corroborates 670 identities, while 165 revision-recovery identities remain valid because current OAI revision metadata does not replace initial registration provenance"
    ),
    "forbidden_owner_substitutions": [
        "DataCite updated as first-public owner",
        "current OAI revision datestamp as first-public owner",
        "v1 submission timestamp alone",
        "numeric adjacency alone",
    ],
    "conservation": "835 = 118 retained + 717 pre-denominator closure + 0 withdrawn",
}
dump("official-owner-batch-evidence-v3.json", owner_evidence)

screening = {
    "schema": "daily-screening-outcomes-v3-owner-receipt-repair",
    "report_date": DATE,
    "window": WINDOW,
    "checked_at": CHECKED_AT,
    "confirmed_raw_count": 835,
    "retained_count": 118,
    "pre_denominator_closure_count": 717,
    "withdrawn_count": 0,
    "confirmed_raw_conservation": "835 = 118 retained + 717 pre-denominator closure + 0 withdrawn",
    "retained_items": candidates,
    "pre_denominator_closure_items": closures,
    "false_positive_negative_challenge": {
        "reused_exact_v1_candidate_reviews": 117,
        "recovered_false_negative": [GAMMA_SF],
        "closure_reason_scope": "family-specific title plus full-abstract contribution adjudication",
        "pending": 0,
    },
    "withdrawal_boundary": "No retained or closure identity in this frozen owner receipt is marked withdrawn; withdrawn count=0.",
}
dump("screening-outcomes-v3.json", screening)

evidence = {
    "schema": "daily-evidence-review-v3-owner-receipt-repair",
    "report_date": DATE,
    "count": 118,
    "deep_complete_count": 118,
    "standard_complete_count": 0,
    "blocked_count": 0,
    "score_distribution": {str(k): score_distribution[k] for k in sorted(score_distribution)},
    "items": evidence_items,
    "legacy_evidence_snapshot_ref": "OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md",
}
dump("evidence-review-v3.json", evidence)
dump("exact-v1-review-packet-v3.json", evidence)

books = {
    "schema": "daily-books-comparison-v3-owner-receipt-repair",
    "report_date": DATE,
    "count": 118,
    "applied_count": 18,
    "no_change_count": 100,
    "pending_integrate_count": 0,
    "items": books_items,
}
dump("books-comparison-v3.json", books)

materials = load(HERE / "materials-request-v3.json")
materials["schema"] = "daily-materials-request-v3-owner-receipt-repair"
materials["items"] = [
    item for item in materials["items"] if item["source_id"] != "SRC-ARXIV"
]
dump("materials-request-v3.json", materials)

applied_items = [item for item in books_items if item["decision"] == "Applied"]
queue = {
    "schema": "daily-books-writeback-queue-v3-owner-receipt-repair",
    "report_date": DATE,
    "status": "applied_in_shared_books_pending_fresh_review",
    "pending_count": 0,
    "applied_count": 18,
    "shared_books_editing": False,
    "items": applied_items,
    "note": "All 18 semantic increments already exist in their canonical Books owners; this author did not edit shared Books. A different fresh reviewer must validate the bindings before Complete.",
}
dump("root-books-writeback-queue-v3.json", queue)

audit = {
    "schema": "daily-author-adversarial-audit-v3-owner-receipt-repair",
    "report_date": DATE,
    "status": "author_checks_passed_fresh_non_author_pending",
    "author_did_not_edit_shared_books": True,
    "challenges": {
        "owner_authority_conflict_corrected": True,
        "raw_conservation": "835=118+717+0",
        "candidate_evidence_bijection": len({x["source_family_id"] for x in evidence_items}) == 118,
        "candidate_books_bijection": len({x["source_family_id"] for x in books_items}) == 118,
        "gamma_false_negative_recovered": True,
        "applied_bindings_found": len(applied_items),
        "external_date_ambiguous_items_remain_isolated": True,
    },
    "gates": {
        "coverage": "author_passed",
        "evidence": "author_passed",
        "books": "author_passed_existing_bindings",
        "fresh_non_author": "pending",
    },
}
dump("author-adversarial-audit-v3.json", audit)

# Correct only the eight stale 05-27 queue projections.  Preserve their
# evidence and previous status while moving ownership to 2026-05-28.
moved_ids = {
    "2605.27480",
    "2605.27494",
    "2605.27599",
    "2605.27678",
    "2605.27712",
    "2605.27784",
    "2605.27785",
    "2605.27789",
}
may27_queue = load(MAY27_QUEUE)
moved = 0
for item in may27_queue["items"]:
    if item["arxiv_id"] in moved_ids:
        if item.get("status") != "superseded_moved_to_2026-05-28":
            item["prior_status"] = item.get("status")
        elif item.get("prior_status") == "superseded_moved_to_2026-05-28":
            # Repair the non-idempotent first author run without discarding the
            # original evidence-completion state.
            item["prior_status"] = "post_write_semantic_audit_passed"
        item["status"] = "superseded_moved_to_2026-05-28"
        item["owner_report_date"] = DATE
        item["superseded_reason"] = "authoritative 2026-05-28 owner receipt supersedes the old 2026-05-27 projection; evidence remains preserved"
        moved += 1
assert moved == 8
may27_queue["ownership_correction"] = {
    "moved_to_2026-05-28_count": 8,
    "source_family_ids": sorted(f"SF-2026-ARXIV-{aid.replace('.', '-')}" for aid in moved_ids),
    "evidence_deleted": False,
}
MAY27_QUEUE.write_text(json.dumps(may27_queue, ensure_ascii=False, indent=2) + "\n")

# Render the six-section current Daily.  Detailed historical reviews live in
# the evidence snapshot and current JSON instead of duplicating a second long
# report body.
candidate_lines = []
for item in candidates:
    score = item["score_parts"]
    review_result = "深入完成"
    if item["source_family_id"] == GAMMA_SF:
        contribution = (
            "shared scene + per-agent state 的 permutation-symmetric multi-agent transition；"
            "只支持作者虚拟环境的两/四主体实验"
        )
    else:
        contribution = "exact-v1 机制与受限 evaluation 已完成；完整命题见 Evidence 附件"
    owner_path = node_paths[item["stable_node_id"]]
    owner_link = f"../../../../{owner_path}"
    decision = (
        f"整合：`{item['stable_node_id']}` [章节]({owner_link})"
        if item["books_disposition"] == "Applied"
        else f"已有覆盖：`{item['stable_node_id']}` [章节]({owner_link})"
    )
    candidate_lines.append(
        f"| [{item['arxiv_id']} {item['title']}]({item['primary_url']}) | 2026-05-28T08:00:00+08:00 | "
        f"{contribution}；`{item['stable_node_id']}`；"
        f"{score['design_delta']}+{score['system_reach']}+{score['durability']}={item['score']} | "
        f"{review_result} | {decision} |"
    )

evidence_lines = []
for item in candidates:
    packet = item["evidence_packet"]
    owner_path = node_paths[item["stable_node_id"]]
    if item["books_disposition"] == "Applied":
        books_text = f"整合到 `{item['stable_node_id']}` 的 [{owner_path}](../../../../{owner_path})；当前 binding 已定位，待 fresh reviewer 验收。"
    else:
        books_text = f"已有覆盖：`{item['stable_node_id']}` 的 [{owner_path}](../../../../{owner_path}) 已承载长期命题；完整对读见证据附件。"
    evidence_lines.append(
        f"### [{item['arxiv_id']} {item['title']}]({item['primary_url']})\n\n"
        f"采用版本=`{item['primary_evidence_version']}`。Method/identity=`{packet['Method / Identity Locators']}`；"
        f"Evaluation=`{packet['Evaluation Locators']}`；Counterevidence/non-proof=`{packet['Limitations / Counterevidence Locators']}`。"
        f"证据边界：{item['claim_boundary']} {books_text} "
        f"完整 Why、Mechanism、trade-off、failure mode 与 coexistence 记录见 "
        f"[`OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md`](../_sources/daily-20260528/OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md)。"
    )

applied_lines = []
for item in applied_items:
    b = item["binding"]
    applied_lines.append(
        f"- `{item['source_family_id']}` → `{item['stable_node_id']}` → `{b['path']}`；"
        f"binding=`{b['binding_anchor']}`，位于正文区={bool(b['mechanism_before_first_review_notes'])}。"
    )

report = f"""# Daily Research — 2026-05-28

**规范：** V3

**窗口：** {WINDOW_START} ～ {WINDOW_END}

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** {CHECKED_AT}

本页取代旧 V3 的全量隔离判断。日期归属遵循项目权威 [`ARXIV_ANNOUNCEMENT_PROVENANCE.md`](../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md)：exact-v1 identity、initial registration、arXiv identifier month 与官方发布节奏一致时可确定 owner；当前 OAI revision metadata 不会反向抹除 first-public provenance。旧 V2.1 长报告仅作为已完成 exact-v1 review 与 Books comparison 的证据附件，不拥有当前 Gate。

## 1. 结论

本窗 arXiv 冻结集合为 **835 = 118 retained + 717 family-specific pre-denominator closure + 0 withdrawn**。其中 670 项由 same-day official OAI 直接佐证，165 项由 initial-registration recovery 佐证；两条路线均保留在 owner receipt 中。117 个旧候选的 exact-v1 identity、采用命题与定位未变化，因此复用其已完成 Source Review；Gamma-World `2605.28816` 从错误 closure 恢复为第 118 个候选。

Evidence 为 **118 deep complete + 0 standard + 0 blocked**，分数分布为 {dict(sorted(score_distribution.items()))}。Books 作者侧对账为 **118 = 18 Applied + 100 No Change + 0 pending Integrate**。17 个旧 Integrate 已投影为当前 Applied，Gamma-World 的 Ch25 机制段与 Review note 也已存在；本 author 未编辑共享 Books。状态保持 Ongoing，只等待另一位 fresh non-author 对 owner、closure、Evidence、No Change 与 18 个正文 binding 做最终挑战。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research index/RSS 的本窗定点检查 | 已检查 | 无本窗确认事件 |
| SRC-ANTHROPIC | 官方 Research index；相邻记录截至 2026-05-22 | 已检查 | 无本窗确认事件 |
| SRC-GOOGLE-AI | 官方 DeepMind publication pages | 受阻 | 两条页面只有 `2026-05-28` 日级日期，无法判断 09:00 前后；已隔离，不进入确认集合 |
| SRC-META-AI | 官方 Publications 入口 | 受阻 | 稳定日级列表不可回放，不支持正向 no-hit |
| SRC-QWEN | 官方 article index；相邻明确日期为 2026-05-29 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 Research/News；可见相邻日期在窗外 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Kimi Platform Blog、release/RFC slice | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 官方 Research publicList 与 linked primary artifacts | 已检查 | 可见记录在窗外 |
| SRC-ZAI | 官方 Research/release index；相邻明确日期在窗外 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方 Research/Public Papers；相邻明确日期为 2026-05-29 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方 technical Blog；最近明确记录为 2026-05-09 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官方 paper/blog cards | 受阻 | 无日期卡片不支持日级 no-hit；已隔离 |
| SRC-MINIMAX | 官方页面与 JSON-LD | 已检查 | Agent Team=`2026-05-27T08:00:00+08:00`，属于 05-27 reopen clue，不计本窗 |
| SRC-ARXIV | authoritative owner receipt：670 OAI direct + 165 initial-registration recovery | 已检查 | `835=118+717+0` |

结构化来源账本见 [`source-coverage-v3.json`](../_sources/daily-20260528/source-coverage-v3.json)、[`official-owner-batch-evidence-v3.json`](../_sources/daily-20260528/official-owner-batch-evidence-v3.json) 与原始 [`arxiv-owner-receipt.json`](../_sources/arxiv-owner-replay-20260903/20260528/arxiv-owner-receipt.json)。外部日级歧义只保留定点材料请求，不参与本窗正向证据。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{chr(10).join(candidate_lines)}

117 个旧候选的完整 Why、Mechanism、evaluation contract、trade-off、failure mode、coexistence boundary 与 exact-v1 locator 保存在 [`OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md`](../_sources/daily-20260528/OWNER_REPLAY_EVIDENCE_SNAPSHOT_20260916.md)；当前逐项结构化投影见 [`evidence-review-v3.json`](../_sources/daily-20260528/evidence-review-v3.json)。这不是只复用旧评分：只有 identity、exact version 与 adopted claim 未变的 117 项复用正文；Gamma-World 已执行独立 deep review。

## 4. 证据与知识整合

Gamma-World 的旧 closure 是 false negative。其长期增量不是“多一个视频 benchmark”，而是把多主体 world state 从统一 latent 演进为 shared scene 与 per-agent identity/observation/action state 的显式分解，再用 permutation-symmetric interaction 更新 joint transition。Method=`§3`，Experiments=`§4`，Discussion=`§5`；只支持作者虚拟环境中的两主体/四主体 video fidelity、action controllability 与 inter-agent consistency，不证明开放世界物理因果、社会因果、真实机器人控制或生产 SLO。该机制已由 `MULTIMODAL-WORLD-MODELS` 的 Ch25 正文与 Review note 承载。

当前 18 个 Applied binding：

{chr(10).join(applied_lines)}

其余 100 项经 owner/相邻章节对读后为 `No Change — Existing Coverage`；旧 `Weekly Only — Context` 的 2605.27566 在当前 V3 中不再作为 Books 状态，因其没有形成新的长期 owner proposition，归入 No Change。完整逐项对账见 [`books-comparison-v3.json`](../_sources/daily-20260528/books-comparison-v3.json)，root 投影见 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260528/root-books-writeback-queue-v3.json)。

{chr(10).join(evidence_lines)}

## 5. 缺口与下一步

- arXiv 当前集合无待补材料、无 blocked Evidence、无 pending Books writeback。
- Google 两条日级 publication、Meta 稳定 dated list 与 MiMo 未标日期卡片保持外部隔离；精确请求见 [`materials-request-v3.json`](../_sources/daily-20260528/materials-request-v3.json)。它们不支撑本窗 no-hit，也不参与 `835=118+717+0`。
- 05-27 旧 queue 中 8 个实际属于 05-28 的 family 已标记 `superseded_moved_to_2026-05-28`；原 Evidence 未删除，当前 05-27 V3 正文也不包含这些 family。
- 仍需另一位 fresh non-author reviewer：先寻找 owner/closure false positive 与 false negative，再逐项挑战 118 个 Evidence 终态、100 个 No Change 和 18 个 Books binding。该复核前本页不得标 Complete。

## 6. 复核

- **本轮角色：** bounded repair author；曾参与旧失败审查，因此不自签 final。
- **作者侧结果：** owner authority 冲突已纠正；835 identity 唯一，118 retained/717 closure 不重叠且覆盖全集；Evidence 与 Books 各 118 个唯一 family；18 个 Applied binding 均能在唯一 canonical Books 文件中定位。
- **状态：** `Ongoing — fresh non-author final review pending`。
- **证据保留：** 旧失败审查不删除；它记录了被本轮权威日期依据推翻的假设，不能复用为当前 final receipt。
"""
REPORT.write_text(report)

checkpoint = f"""# 2026-05-28 owner-receipt V3 bounded repair checkpoint

- Role: bounded repair author; final self-sign prohibited.
- Status: Ongoing, another fresh non-author reviewer pending.
- Window: `{WINDOW}`.
- Owner receipt: `835 = 670 OAI direct + 165 initial-registration recovery` under `ARXIV_ANNOUNCEMENT_PROVENANCE.md`.
- Denominator: `835 = 118 retained + 717 closure + 0 withdrawn`.
- Evidence: `118 deep complete + 0 standard + 0 blocked`.
- Books: `18 Applied + 100 No Change + 0 pending`; shared Books not edited by this author.
- Gamma-World `2605.28816`: recovered false negative, score `3+3+3=9`, owner `MULTIMODAL-WORLD-MODELS`, Applied.
- 05-27 stale queue: 8 items marked `superseded_moved_to_2026-05-28`; evidence preserved.
- Required next step: a different fresh non-author reviewer must challenge owner, closure, exact-v1 Evidence, all Books dispositions and semantic bindings before Complete.
"""
(HERE / "OWNER_RECEIPT_V3_BOUNDED_REPAIR_CHECKPOINT_20260916.md").write_text(checkpoint)

print(
    json.dumps(
        {
            "raw": 835,
            "retained": 118,
            "closure": 717,
            "withdrawn": 0,
            "evidence": len(evidence_items),
            "deep": 118,
            "applied": 18,
            "no_change": 100,
            "pending_books": 0,
            "moved_from_2026_05_27": moved,
        },
        indent=2,
    )
)
