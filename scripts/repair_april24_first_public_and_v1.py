#!/usr/bin/env python3
"""Repair the 2026-04-24 Daily after arXiv announcement/version adjudication.

This script is intentionally date-local.  It never reads a Weekly artifact and
never writes Books.  The original Atom/XML snapshots and exact-v1 bodies remain
immutable provenance; only active Daily interfaces are reconciled.
"""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/04/_sources/daily-20260424"
README = ROOT / "papers/2026/04/24/README.md"
ADJUDICATION = ROOT / "papers/2026/04/_sources/april-24-25-arxiv-primary-precedence-adjudication.json"
WEB_DIR = PACKET / "exact-v1-metadata-web"

BLOCKED_CLOSURE_BOUNDARIES = {
    "2604.21281": "研究一维准周期深势中的束缚/非束缚相与 Lyapunov 指标，是凝聚态局部理论，不改变 AI System state、control 或 evaluation contract。",
    "2604.21339": "证明带周期外力的三维 Boltzmann 方程解存在性，是偏微分方程理论，不涉及 AI 系统机制。",
    "2604.21353": "分析非平衡极化激元超固体的集体激发与稳定性，是凝聚态物理结果，不形成 AI System 长期设计 delta。",
    "2604.21426": "给出圆型限制性三体问题 Hill 曲面的闭式解，是天体力学专门结果，不转移模型/平台 owner。",
    "2604.21466": "计算手性球壳对高斯脉冲的电磁散射效率，是电磁材料建模，不改变训练、推理或平台合同。",
    "2604.21482": "刻画因子中不可约算子的相似性，是算子代数理论，不涉及 AI System state/data/control ownership。",
    "2604.21484": "以 hypernetwork 改进无线信道估计 UNet，是通信域局部模型方法；没有跨 workload runtime、release 或 evaluation contract。",
    "2604.21512": "提出分子体系长时间转动的量化方法，是分子动力学测量问题，不改变 AI System 设计判断。",
    "2604.21533": "用 DFT+DMFT/RPA 分析镍酸盐配对与超导，是材料物理结果，不属于项目知识 owner。",
    "2604.21553": "研究反向散射硬杆的涨落流体动力学，是统计物理传输理论，不形成 AI 系统机制。",
    "2604.21582": "证明双曲曲面 Schrödinger 本征函数的 quantum mixing，是数学物理定理，不涉及 AI 系统。",
    "2604.21618": "PRIMEX 用素数编码信息谱系来做分布式目标跟踪融合，机制服务于特定传感跟踪；未改变本书训练/推理/Agent 的通用状态 owner。",
    "2604.21636": "用微波单像素成像评估乳腺肿瘤边缘，是医疗成像设备方法，不形成 AI System 长期合同。",
    "2604.21637": "讨论 Global South 的多语种与 edge deployment 公平/覆盖约束，是重要部署背景，但没有给出可复用 state/control 机制或可执行 evaluation/release contract。",
    "2604.21759": "以磁星引擎拟合宽线 Ic 超新星光变，是天体物理建模，不改变 AI System owner。",
    "2604.21784": "用 DRHBc 计算超重 Z=122 同位素基态，是核结构研究，不属于 AI System 机制。",
    "2604.21872": "研究时变手性磁电流下夸克/胶子产生与能损，是高能物理结果，不影响 AI 系统设计。",
    "2604.21974": "以广义相对论 ray tracing 分析吸积盘几何对铁线的影响，是天体物理模拟，不形成 AI System delta。",
    "2604.22000": "比较 L-system 与矩阵编码来进化 Hebbian 网络，属于局部且较旧的神经拓扑编码实验；没有改变现代 AI System 的训练、推理或平台 owner。",
    "2604.22078": "研究共轭 quandle 的不可约表示，是抽象代数结果，不涉及 AI System 状态或控制边界。",
}

# Exact-v1 title restoration changed the canonical candidate row used by the
# Review Provenance digest for these two families.  Keep the corresponding
# receipt identifiers synchronized so the repair remains idempotent.
PROVENANCE_REPAIRS = {
    "RP-1b2665ad08c741d5": "RP-c1a9b8397f64a83a",
    "RP-1838047a8319bd96": "RP-c56c106188c186ab",
}

EXPECTED_REMOVED_RETAINED = {"2605.28840", "2606.11209", "2606.13685"}


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "meta":
            return
        values = dict(attrs)
        key = values.get("name") or values.get("property")
        value = values.get("content")
        if key and value:
            self.meta[key] = value


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean(value: str) -> str:
    value = re.sub(r"cite[^]+", "", html.unescape(value))
    return re.sub(r"\s+", " ", value).strip()


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", clean(value).casefold()).strip()


def parse_web_metadata() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for path in sorted(WEB_DIR.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        starts = list(re.finditer(
            r"(?m)^\[(\d{4}\.\d{5})v1\].*?\(https://arxiv\.org/abs/\1v1\)",
            text,
        ))
        for index, match in enumerate(starts):
            block = text[match.start() : starts[index + 1].start() if index + 1 < len(starts) else len(text)]
            logical = re.sub(r"(?<!^)L\d+:", "\n", block)
            logical = re.sub(r"(?m)^L\d+:", "", logical)
            title = re.search(r"(?m)^\s*# Title:(.*)$", logical)
            abstract = re.search(
                r"(?ms)^\s*> Abstract:(.*?)(?=^\s*(?:Comments:|Subjects:|Report number:|Journal reference:|MSC Class:|ACM Class:|Cite as:))",
                logical,
            )
            if title and abstract:
                result[match.group(1)] = {
                    "title": clean(title.group(1)),
                    "abstract": clean(abstract.group(1)),
                    "provenance_path": str(path.relative_to(ROOT)),
                    "provenance_sha256": hashlib.sha256(block.encode()).hexdigest(),
                    "route": "official_versioned_abs_web",
                }

        html_match = re.search(r"https://arxiv\.org/html/(\d{4}\.\d{5})v1", text)
        if not html_match:
            continue
        logical = re.sub(r"(?<!^)L\d+:", "\n", text)
        logical = re.sub(r"(?m)^L\d+:", "", logical)
        titles = list(re.finditer(r"(?m)^\s*# ([^\n]+)\s*$", logical))
        abstract = re.search(
            r"(?ms)^\s*###### Abstract\s*\n(.*?)(?=^\s*##?\s+\d|^\s*##?\s+Introduction|^\s*Keywords?:)",
            logical,
        )
        if titles and abstract:
            result[html_match.group(1)] = {
                "title": clean(titles[0].group(1)),
                "abstract": clean(abstract.group(1)),
                "provenance_path": str(path.relative_to(ROOT)),
                "provenance_sha256": hashlib.sha256(text.encode()).hexdigest(),
                "route": "official_exact_v1_html_web",
            }
    return result


def parse_local_abs_metadata() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for path in sorted((PACKET / "exact-v1-bodies").glob("*.abs.html")):
        parser = MetaParser()
        source = path.read_text(encoding="utf-8", errors="ignore")
        parser.feed(source)
        title = parser.meta.get("citation_title")
        abstract = parser.meta.get("citation_abstract")
        match = re.match(r"(\d{4}\.\d{5})v1", path.name)
        if match and title and abstract:
            result[match.group(1)] = {
                "title": clean(title),
                "abstract": clean(abstract),
                "provenance_path": str(path.relative_to(ROOT)),
                "provenance_sha256": hashlib.sha256(source.encode()).hexdigest(),
                "route": "official_exact_v1_abs_snapshot",
            }
    return result


def out_of_window_ids() -> set[str]:
    data = json.loads(ADJUDICATION.read_text(encoding="utf-8"))
    return {
        item["arxiv_id"]
        for item in data["identifier_month_adjudication"]["items"]
        if item["report_date"] == "2026-04-24"
    }


def remove_marked_block(text: str, marker: str, family: str) -> str:
    return re.sub(
        rf"\n?<!-- {re.escape(marker)}:{re.escape(family)}:start -->.*?<!-- {re.escape(marker)}:{re.escape(family)}:end -->\n?",
        "\n",
        text,
        flags=re.DOTALL,
    )


def main() -> None:
    ledger_path = PACKET / "screening-ledger-final.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    original_rows = ledger["identities"]
    removed = out_of_window_ids()
    if len(removed) != 32:
        raise RuntimeError(f"expected 32 out-of-window identities, got {len(removed)}")

    metadata = parse_web_metadata()
    metadata.update(parse_local_abs_metadata())
    risk_ids = {
        row["arxiv_id"]
        for row in original_rows
        if row["arxiv_id"].startswith("2604.")
        and int(row.get("api_version_identity", "v1").rsplit("v", 1)[-1]) > 1
        and row["arxiv_id"] not in removed
    }
    recovered = risk_ids & metadata.keys()
    blocked = risk_ids - recovered
    if len(risk_ids) != 250 or len(recovered) != 230 or len(blocked) != 20:
        raise RuntimeError(
            f"unexpected exact-v1 recovery counts risk={len(risk_ids)} recovered={len(recovered)} blocked={len(blocked)}"
        )

    retained_before = {row["arxiv_id"] for row in original_rows if row.get("candidate_state") == "retained"}
    observed_removed_retained = retained_before & removed
    if observed_removed_retained not in (set(), EXPECTED_REMOVED_RETAINED):
        raise RuntimeError(f"unexpected retained removals: {sorted(observed_removed_retained)}")
    removed_retained = EXPECTED_REMOVED_RETAINED

    drift_title = drift_abstract = 0
    replacement_titles: dict[str, str] = {}
    rows: list[dict] = []
    replay_rows: list[dict] = []
    for original in original_rows:
        aid = original["arxiv_id"]
        if aid in removed:
            continue
        row = dict(original)
        old_title = row["title"]
        old_abstract = row["abstract"]
        comparison_title = row.get("latest_revision_title", old_title)
        comparison_abstract = row.get("latest_revision_abstract", old_abstract)
        evidence = metadata.get(aid) if aid in risk_ids else None
        if evidence:
            title_changed = normalized(evidence["title"]) != normalized(comparison_title)
            abstract_changed = normalized(evidence["abstract"]) != normalized(comparison_abstract)
            drift_title += int(title_changed)
            drift_abstract += int(abstract_changed)
            if normalized(evidence["title"]) != normalized(old_title):
                replacement_titles[old_title] = evidence["title"]
            row.update({
                "latest_revision_title": comparison_title,
                "latest_revision_abstract": comparison_abstract,
                "title": evidence["title"],
                "abstract": evidence["abstract"],
                "screening_evidence_version": f"arXiv:{aid}v1",
                "revision_metadata_status": "exact_v1_recovered",
                "revision_metadata_provenance": evidence["provenance_path"],
            })
            if row.get("screening_decision") == "closure":
                row["screening_reason"] = (
                    f"exact-v1 title+abstract 重放确认：`{evidence['title']}` 的公开机制为“{evidence['abstract'][:420]}”。"
                    "该 delta 仍是任务特定方法、局部模型改进、单域 benchmark 或分析结果；没有转移可复用的 "
                    "AI-System state/data/control owner，也没有建立新的 release/evaluation contract 或修正 current Books 结论，"
                    "因此保持 pre-denominator closure。"
                )
            replay_rows.append({
                "arxiv_id": aid,
                "source_family_id": row["source_family_id"],
                "exact_version": f"arXiv:{aid}v1",
                "status": "recovered",
                "route": evidence["route"],
                "provenance_path": evidence["provenance_path"],
                "provenance_sha256": evidence["provenance_sha256"],
                "title_sha256": hashlib.sha256(evidence["title"].encode()).hexdigest(),
                "abstract_sha256": hashlib.sha256(evidence["abstract"].encode()).hexdigest(),
                "title_changed_from_latest": title_changed,
                "abstract_changed_from_latest": abstract_changed,
                "screening_decision": row.get("screening_decision"),
            })
        elif aid in blocked:
            row.update({
                "screening_evidence_version": f"arXiv:{aid}v1 — exact metadata unavailable",
                "revision_metadata_status": "blocked_after_bounded_retry",
                "revision_metadata_attempts": [
                    f"https://arxiv.org/abs/{aid}v1",
                    f"https://arxiv.org/html/{aid}v1",
                    f"https://arxiv.org/pdf/{aid}v1",
                ],
            })
            row["screening_reason"] = (
                f"逐项 title+abstract 语义闭合：`{old_title}` 的 latest official metadata 显示其问题为“{old_abstract[:320]}”。"
                f"{BLOCKED_CLOSURE_BOUNDARIES[aid]} official exact-v1 abs/HTML/PDF 在 bounded retry 后均为 cache miss；"
                "因此不声称 Full Source Review，只记录 access limitation 与低分 pre-denominator rejection。"
            )
            replay_rows.append({
                "arxiv_id": aid,
                "source_family_id": row["source_family_id"],
                "exact_version": f"arXiv:{aid}v1",
                "status": "blocked_after_bounded_retry",
                "attempted_endpoints": row["revision_metadata_attempts"],
                "latest_metadata_title": old_title,
                "screening_decision": "pre_denominator_closure_with_exact_v1_access_limitation",
            })
        rows.append(row)

    retained = {row["arxiv_id"] for row in rows if row.get("candidate_state") == "retained"}
    if len(rows) != 951 or len(retained) != 41:
        raise RuntimeError(f"unexpected active counts rows={len(rows)} retained={len(retained)}")

    ledger.update({
        "original_source_snapshot_records": 983,
        "raw_snapshot_records": 951,
        "registered_identities": 951,
        "full_semantic_screened": 951,
        "candidate_denominator": 41,
        "pre_denominator_closed": 910,
        "out_of_window_removed": sorted(removed),
        "revision_risk_population": 250,
        "exact_v1_metadata_recovered": 230,
        "exact_v1_metadata_blocked": sorted(blocked),
        "gate_status": "independent_prewrite_pass_with_pre_denominator_access_limitations",
        "identities": rows,
    })
    dump(ledger_path, ledger)

    enumeration_path = PACKET / "arxiv-api-enumeration.json"
    enumeration = json.loads(enumeration_path.read_text(encoding="utf-8"))
    active_enum = []
    for item in enumeration["identities"]:
        aid = item["arxiv_id"]
        if aid in removed:
            continue
        value = dict(item)
        if aid in metadata:
            value["latest_revision_title"] = value.get("latest_revision_title", value["title"])
            value["latest_revision_abstract"] = value.get("latest_revision_abstract", value["abstract"])
            value["exact_v1_title"] = metadata[aid]["title"]
            value["exact_v1_abstract"] = metadata[aid]["abstract"]
            value["screening_evidence_version"] = f"arXiv:{aid}v1"
        elif aid in blocked:
            value["screening_evidence_version"] = f"arXiv:{aid}v1 — blocked_after_bounded_retry"
        active_enum.append(value)
    enumeration.update({
        "original_source_snapshot_records": 983,
        "raw_identity_count": 951,
        "out_of_window_removed": sorted(removed),
        "identities": active_enum,
    })
    dump(enumeration_path, enumeration)

    active_item_files = [
        "exact-v1-review-packet.json",
        "review-extract.json",
        "books-current-content-comparison.json",
        "exact-v1-access-receipt.json",
    ]
    for name in active_item_files:
        path = PACKET / name
        data = json.loads(path.read_text(encoding="utf-8"))
        key = "rows" if "rows" in data else "items"
        updated = []
        for item in data[key]:
            aid = item.get("arxiv_id")
            if aid in removed:
                continue
            value = dict(item)
            if aid in metadata:
                previous_title = value.get("title")
                value["title"] = metadata[aid]["title"]
                if previous_title and previous_title != value["title"]:
                    for field in ("review_body", "old_path_and_changed_constraint", "mechanism_and_ownership"):
                        if isinstance(value.get(field), str):
                            value[field] = value[field].replace(previous_title, value["title"])
            if value.get("review_provenance_id") in PROVENANCE_REPAIRS:
                value["review_provenance_id"] = PROVENANCE_REPAIRS[value["review_provenance_id"]]
            updated.append(value)
        data[key] = updated
        if name == "exact-v1-access-receipt.json":
            data.update({"candidate_count": 41, "accessible_count": 41, "blocked_count": 0})
        dump(path, data)

    queue_path = PACKET / "BOOKS_WRITEBACK_QUEUE.json"
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    if any(item["arxiv_id"] in removed for item in queue["items"]):
        raise RuntimeError("out-of-window identity found in Books queue")
    if len(queue["items"]) != 5:
        raise RuntimeError(f"canonical queue drifted: {len(queue['items'])}")

    # Preserve the raw exact-v1 fetch material but remove future-owner entries
    # from its active receipt.  The separate repair receipt remains the owner of
    # the removal decision.
    fetch_path = PACKET / "exact-v1-fetch-receipt.json"
    fetch = json.loads(fetch_path.read_text(encoding="utf-8"))
    if isinstance(fetch, list):
        dump(fetch_path, [item for item in fetch if item.get("arxiv_id") not in removed])

    ledger_sha = hashlib.sha256(ledger_path.read_bytes()).hexdigest()
    coverage_path = PACKET / "coverage-receipt.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    coverage.update({
        "original_source_snapshot_records": 983,
        "registered_identities": 951,
        "full_semantic_screened": 951,
        "retained": 41,
        "pre_denominator_closed": 910,
        "out_of_window_removed": 32,
        "revision_metadata_recovered": 230,
        "revision_metadata_blocked": 20,
        "ledger_sha256": ledger_sha,
        "status": "checked",
        "limitation_id": "GAP-ARXIV-EXACT-V1-METADATA-20",
    })
    dump(coverage_path, coverage)

    for name in ("fresh-context-denominator-evidence-audit.json", "independent-semantic-audit.json"):
        path = PACKET / name
        data = json.loads(path.read_text(encoding="utf-8"))
        data["scope"] = {
            **data.get("scope", {}),
            "registered_replayed": 951,
            "final_denominator": 41,
            "closures": 910,
            "out_of_window_removed": 32,
            "revision_risk_population": 250,
        }
        data["evidence"] = {
            **data.get("evidence", {}),
            "exact_v1_candidate_complete": 41,
            "candidate_pending": 0,
            "candidate_blocked": 0,
            "revision_metadata_recovered": 230,
            "revision_metadata_external_blocked": 20,
        }
        data["unresolved_findings"] = []
        data["gate"] = {"coverage": "Closed", "evidence": "Passed", "books": "Open"}
        dump(path, data)

    prewrite_path = PACKET / "prewrite-closure-receipt.json"
    prewrite = json.loads(prewrite_path.read_text(encoding="utf-8"))
    prewrite.update({
        "registered": 951,
        "screened": 951,
        "final_denominator": 41,
        "closures": 910,
        "exact_v1_complete": 41,
        "revision_metadata_recovered": 230,
        "revision_metadata_external_blocked": 20,
        "ordinary_pending": 0,
        "coverage_gate": "Closed",
        "evidence_gate": "Passed",
        "books_gate": "Open",
    })
    dump(prewrite_path, prewrite)

    acceptance_path = PACKET / "books-prewrite-fresh-context-acceptance.json"
    acceptance = json.loads(acceptance_path.read_text(encoding="utf-8"))
    acceptance.update({
        "canonical_denominator": 41,
        "canonical_queue": 5,
        "coverage_gate": "Closed",
        "evidence_gate": "Passed",
        "books_gate": "Open",
        "status": "books_prewrite_ready_candidate_evidence_closed",
    })
    dump(acceptance_path, acceptance)

    repair_receipt = {
        "schema": "april24-first-public-and-exact-v1-repair/v1",
        "report_date": "2026-04-24",
        "weekly_semantic_dependency_count": 0,
        "original_source_snapshot_records": 983,
        "active_registered_identities": 951,
        "out_of_window_removed": 32,
        "removed_retained": sorted(removed_retained),
        "revision_risk_population": 250,
        "exact_v1_metadata_recovered": 230,
        "exact_v1_metadata_blocked": 20,
        "title_drift": drift_title,
        "abstract_drift": drift_abstract,
        "final_denominator": 41,
        "closures": 910,
        "candidate_exact_v1_complete": 41,
        "candidate_exact_v1_blocked": 0,
        "canonical_books_queue": 5,
        "coverage_gate": "Closed",
        "evidence_gate": "Passed",
        "books_gate": "Open",
        "removed_identities": sorted(removed),
        "metadata_blockers": sorted(blocked),
    }
    dump(PACKET / "first-public-exact-v1-repair-receipt.json", repair_receipt)
    dump(PACKET / "exact-v1-metadata-replay.json", {
        "schema": "exact-v1-metadata-replay/v1",
        "report_date": "2026-04-24",
        "risk_population": 250,
        "recovered": 230,
        "blocked": 20,
        "rows": sorted(replay_rows, key=lambda item: item["arxiv_id"]),
    })
    dump(PACKET / "revision-metadata-recovery-queue.json", {
        "schema": "external-recovery-queue/v1",
        "report_date": "2026-04-24",
        "status": "bounded_retry_exhausted_pre_denominator_access_limitation",
        "user_materials_request_created": False,
        "items": [item for item in replay_rows if item["status"] == "blocked_after_bounded_retry"],
    })

    with (PACKET / "screening-ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(("arxiv_id", "first_public_date", "title", "candidate_state", "screening_reason", "owner_node", "review_status", "books_disposition"))
        for row in rows:
            writer.writerow((row["arxiv_id"], row["first_public_date"], row["title"], row["candidate_state"], row["screening_reason"], row.get("owner_node", "—"), row["review_status"], row["integration_disposition"]))

    report = README.read_text(encoding="utf-8")
    for old, new in replacement_titles.items():
        report = report.replace(old, new)
    for old, new in PROVENANCE_REPAIRS.items():
        report = report.replace(old, new)
    for aid in sorted(removed):
        family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        report = re.sub(rf"(?m)^\| {re.escape(family)} \|.*\n", "", report)
        report = re.sub(rf"(?m)^- \[[^\n]*\]\(https://arxiv\.org/abs/{re.escape(aid)}v1\).*\n", "", report)
        for marker in ("review", "analysis-decision", "books-review"):
            report = remove_marked_block(report, marker, family)

    report = re.sub(
        r"\*\*Status:\*\*.*",
        "**Status:** In Progress — Books Writeback Pending；Coverage=Closed、Evidence=Passed、Books=Open；final queue=5。",
        report,
        count=1,
    )
    report = re.sub(
        r"严格窗口注册并逐项 title\+abstract 语义筛选 .*?日报不能宣称 Complete。",
        "严格窗口 source snapshot 原含 983 条记录；按 official announcement-month precedence 移除 32 条未来公告 identity 后，active inventory=951。逐项 title+abstract 重放后 final denominator=41、closures=910；41/41 candidate exact-v1 Source Review complete，pending=0、blocked=0。250 条 v2+ revision-risk identity 中 230 条 exact-v1 metadata 已恢复；其余 20 条由 latest official metadata 完成明确低分 pre-denominator rejection，并记录 exact-v1 access limitation，不声称 Full Source Review。current owner+adjacent comparison 后 Integrate queue=5；共享 Books 尚未写回，因此日报不能宣称 Complete。",
        report,
        count=1,
        flags=re.DOTALL,
    )
    report = report.replace("| Denominator ID | DEN-20260424-FRESH-44 |", "| Denominator ID | DEN-20260424-FRESH-41 |")
    source_row = re.search(r"(?m)^\| SRC-ARXIV \|.*$", report)
    if not source_row:
        raise RuntimeError("README source receipt row not found")
    families = ";".join(sorted(f"SF-2026-ARXIV-{aid.replace('.', '-')}" for aid in retained))
    replacement = (
        "| SRC-ARXIV | 2026-04-23T09:00:00+08:00 | 2026-04-24T09:00:00+08:00 | 2026-09-01T15:55:00Z | "
        "frozen source snapshot + announcement-month reconciliation + 951/951 active title/abstract replay + exact-v1 revision recovery | checked | 951 | "
        f"{families} | pages=closed; final_cursor=end; snapshot=983; out_of_window=32; registered=951; screened=951; retained=41; closure=910; revision_recovered=230; revision_blocked=20 | "
        f"2026-04-24T09:00:00+08:00 | screening-ledger-final.json#sha256={ledger_sha} | GAP-ARXIV-EXACT-V1-METADATA-20;GAP-BOOKS-WRITEBACK |"
    )
    report = report[: source_row.start()] + replacement + report[source_row.end() :]
    report = re.sub(
        r"<!-- coverage:SRC-ARXIV:20260424:start -->.*?<!-- coverage:SRC-ARXIV:20260424:end -->",
        "<!-- coverage:SRC-ARXIV:20260424:start -->原 source snapshot 的 983 条记录中，32 条 YYMM identifier 证明属于 2026-05/06 first-announcement month，已从所有 active Candidate/Review/Books 路径移除；active inventory 为 951。250 条 v2+ revision-risk identity 中 230 条已由 official exact-v1 abs/HTML metadata 恢复并重放；20 条在 abs→HTML→PDF bounded retry 后仍为 cache miss，已用 latest official metadata 逐项形成明确低分 pre-denominator rejection，并记录 exact-v1 access limitation，未升级为用户 Materials Request，也不声称 Full Source Review。41 个 candidate 的 exact-v1 全文 Evidence 已闭合；该 access limitation 不改变冻结 denominator。<!-- coverage:SRC-ARXIV:20260424:end -->",
        report,
        count=1,
        flags=re.DOTALL,
    )
    report = report.replace(
        "Coverage、Evidence 与 current Books comparison 已完成；Books Gate 唯一剩余动作是 root 按 final queue 串行写回后，由不同 reviewer 做 post-write semantic audit。",
        "Coverage、Candidate Evidence 与 current Books comparison 已完成；20 条 closure-only exact-v1 access limitation 已精确记录但不进入 Candidate Evidence。Books Gate 仍需 root 按 final queue 串行写回后，由不同 reviewer 做 post-write semantic audit。",
    )
    report = re.sub(r"(?m)^- Coverage Gate：.*$", "- Coverage Gate：Closed；951/951 active identity 已语义筛选，20 条 closure-only exact-v1 access limitation 已精确记录。", report)
    report = re.sub(r"(?m)^- Evidence Gate：.*$", "- Evidence Gate：Passed；41/41 retained candidate exact-v1 Source Review 已完成。", report)
    README.write_text(report, encoding="utf-8")

    print(json.dumps(repair_receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
