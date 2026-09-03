#!/usr/bin/env python3
"""Build non-empty raw inventories and identity-level screening checkpoints.

This deliberately does not close the semantic gate.  It reconstructs the
official identity/abstract denominator from DataCite's arXiv DOI records,
reuses only prior explicit candidate decisions, and makes every remaining
identity auditable.  A later fresh-context pass must adjudicate the generated
pre-denominator closure proposal before a Daily can become Complete.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent
RAW = AUDIT / "raw-datacite"
OWNER_TSV = AUDIT / "owner-recovery/owner-reconciliation.tsv"
SHANGHAI = ZoneInfo("Asia/Shanghai")
WITHDRAWN = {"2606.24369"}
REGISTERED = {
    "cs.AI", "cs.AR", "cs.CL", "cs.CR", "cs.CV", "cs.DB", "cs.DC",
    "cs.IR", "cs.LG", "cs.MA", "cs.NI", "cs.OS", "cs.PF", "cs.PL",
    "cs.RO", "cs.SD", "cs.SE", "eess.AS", "stat.ML",
}


def text_field(attributes: dict, key: str, nested: str) -> str:
    values = attributes.get(key) or []
    for value in values:
        text = value.get(nested)
        if text:
            return re.sub(r"\s+", " ", text).strip()
    return ""


def categories(attributes: dict) -> list[str]:
    result = []
    for item in attributes.get("subjects") or []:
        if item.get("subjectScheme") != "arXiv":
            continue
        match = re.search(r"\(([a-z-]+\.[A-Z]+)\)$", item.get("subject", ""))
        if match:
            result.append(match.group(1))
    return sorted(set(result))


def arxiv_id(attributes: dict) -> str:
    doi = attributes.get("doi", "").lower()
    match = re.fullmatch(r"10\.48550/arxiv\.(\d{4}\.\d{4,5})", doi)
    return match.group(1) if match else ""


def current_candidates() -> tuple[dict[str, dict], dict[str, str]]:
    by_id: dict[str, dict] = {}
    source_report: dict[str, str] = {}
    for month in ("06", "07"):
        for report in sorted((ROOT / f"papers/2026/{month}").glob("[0-9][0-9]/README.md")):
            body = report.read_text(encoding="utf-8")
            try:
                section = body.split("<!-- validator:candidate-ledger-v2.1 -->", 1)[1].split("## 3.", 1)[0]
            except IndexError:
                continue
            for line in section.splitlines():
                if not line.startswith("| SF-"):
                    continue
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) != 22:
                    continue
                match = re.search(r"(\d{4}\.\d{4,5})", cells[1])
                if not match or match.group(1) in WITHDRAWN:
                    continue
                item = {
                    "source_family_id": cells[0],
                    "primary_identifier": cells[1],
                    "score": {"design_delta": cells[6], "system_reach": cells[7], "durability": cells[8], "total": cells[9]},
                    "review_status": cells[11],
                    "access_status": cells[12],
                    "stable_node_id": cells[18],
                    "books_disposition": cells[19],
                }
                # Duplicate ids are data-quality findings, never silently overwritten.
                if match.group(1) in by_id and by_id[match.group(1)]["source_family_id"] != cells[0]:
                    raise RuntimeError(f"candidate identity collision: {match.group(1)}")
                by_id[match.group(1)] = item
                source_report[match.group(1)] = report.parent.name
    return by_id, source_report


def owner_map() -> dict[str, str]:
    import csv

    owners = {}
    with OWNER_TSV.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["arxiv_id"] in WITHDRAWN:
                continue
            if row["reconciliation"] != "identifier_month_conflict_ambiguous":
                owners[row["arxiv_id"]] = row["resolved_owner_report_date"]
    return owners


def closure_kind(title: str, abstract: str, cats: list[str]) -> tuple[str, str]:
    text = f"{title} {abstract}".lower()
    first = re.split(r"(?<=[.!?])\s+", abstract, maxsplit=1)[0][:280]
    theory = ("we prove" in text or "theorem" in text) and not any(
        key in text for key in ("system", "runtime", "serving", "training", "inference", "agent")
    )
    vertical = any(key in text for key in (
        "medical", "clinical", "healthcare", "autonomous driving", "agriculture", "finance",
        "legal", "education", "protein", "molecule", "wireless", "remote sensing",
    )) and not any(key in text for key in ("platform", "serving", "distributed", "runtime"))
    benchmark = "benchmark" in title.lower() and not any(
        key in text for key in ("release gate", "evaluation contract", "deployment", "system-level")
    )
    robotics = bool({"cs.RO"} & set(cats)) and not any(
        key in text for key in ("vision-language-action", "vla", "world model", "control frequency", "sim-to-real")
    )
    if theory:
        kind = "theory_without_ai_system_contract"
        why = "贡献停留在理论性质或算法界限，没有改变 AI System 的长期 state/data/control owner 或工程 contract"
    elif vertical:
        kind = "vertical_application_without_system_delta"
        why = "贡献绑定单一领域应用，没有形成可迁移的训练、推理、平台、评测或 agent 系统机制"
    elif benchmark:
        kind = "local_benchmark_without_release_delta"
        why = "局部 benchmark 没有新增跨系统 evaluation/release contract，也未修正 Books 既有判断"
    elif robotics:
        kind = "embodied_task_local_method"
        why = "贡献停留在特定机器人、传感器或动作任务，未改变通用 VLA 状态/控制所有权"
    else:
        kind = "incremental_method_without_durable_system_delta"
        why = "标题与摘要未显示可持久的系统 owner、控制流、数据流、evaluation/release contract 或 Books 结论变化"
    reason = f"《{title}》：摘要证据“{first or 'Not Disclosed'}”；据此提出 pre-denominator closure，因为{why}。"
    return kind, reason


def main() -> None:
    candidates, source_report = current_candidates()
    owners = owner_map()
    records: dict[str, dict] = {}
    snapshots = []
    for path in sorted(RAW.glob("datacite-arxiv-26??-g?-page-*.json.gz")):
        raw = path.read_bytes()
        snapshots.append({"path": path.name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            payload = json.load(handle)
        for entry in payload.get("data", []):
            attributes = entry.get("attributes", {})
            aid = arxiv_id(attributes)
            if not aid or aid in WITHDRAWN:
                continue
            cats = categories(attributes)
            if not REGISTERED.intersection(cats):
                continue
            records[aid] = {
                "arxiv_id": aid,
                "title": text_field(attributes, "titles", "title"),
                "abstract": text_field(attributes, "descriptions", "description"),
                "categories": cats,
                "datacite_created_utc": attributes.get("created", ""),
                "datacite_registered_utc": attributes.get("registered", ""),
                "datacite_doi": attributes.get("doi", ""),
                "source_locator": attributes.get("url", f"https://arxiv.org/abs/{aid}"),
            }

    by_date: dict[str, list[dict]] = defaultdict(list)
    outside = Counter()
    for aid, item in sorted(records.items()):
        owner = owners.get(aid)
        if not owner:
            created = item.get("datacite_created_utc")
            if not created:
                outside["missing_created"] += 1
                continue
            owner = datetime.fromisoformat(created.replace("Z", "+00:00")).astimezone(SHANGHAI).date().isoformat()
        if not ("2026-06-01" <= owner <= "2026-07-31"):
            outside["outside_target_months"] += 1
            continue
        prior = candidates.get(aid)
        family = prior["source_family_id"] if prior else f"SF-2026-ARXIV-{aid}"
        base = {
            **item,
            "source_family_id": family,
            "resolved_owner_report_date": owner,
            "title_abstract_sha256": hashlib.sha256((item["title"] + "\n" + item["abstract"]).encode()).hexdigest(),
        }
        if prior:
            base.update({
                "semantic_screen_status": "retained_prior_decision_pending_owner_reaudit",
                "semantic_decision_kind": "prior_retained_candidate",
                "semantic_screen_reason": (
                    "旧报告已保留并完成 Source Review；本轮只恢复 canonical announcement owner，"
                    "仍须在新 owner Daily 中重新执行 false-positive、selection 与 Books comparison audit。"
                ),
                "prior_candidate": prior,
                "prior_source_report_day": source_report[aid],
            })
        else:
            kind, reason = closure_kind(item["title"], item["abstract"], item["categories"])
            base.update({
                "semantic_screen_status": "closure_proposed_pending_fresh_context_audit",
                "semantic_decision_kind": kind,
                "semantic_screen_reason": reason,
            })
        by_date[owner].append(base)

    summary = {
        "schema": "canonical-raw-inventory-recovery-summary-v1",
        "generated_at": datetime.now(SHANGHAI).isoformat(),
        "snapshot_count": len(snapshots),
        "snapshot_records_after_category_dedup": len(records),
        "in_scope_identities": sum(map(len, by_date.values())),
        "prior_retained_candidates": sum(
            item["semantic_screen_status"].startswith("retained")
            for items in by_date.values() for item in items
        ),
        "closure_proposals_pending_audit": sum(
            item["semantic_screen_status"].startswith("closure_proposed")
            for items in by_date.values() for item in items
        ),
        "outside": dict(outside),
        "snapshots": snapshots,
        "per_report": {},
    }

    for owner in [f"2026-06-{day:02d}" for day in range(1, 31)] + [f"2026-07-{day:02d}" for day in range(1, 32)]:
        items = sorted(by_date.get(owner, []), key=lambda item: item["arxiv_id"])
        month = owner[5:7]
        packet = ROOT / f"papers/2026/{month}/_sources/daily-{owner.replace('-', '')}"
        packet.mkdir(parents=True, exist_ok=True)
        raw_payload = {
            "schema": "canonical-raw-identity-inventory-v2.1",
            "report_date": owner,
            "date_semantics": "candidate owner reconciliation when available; otherwise DataCite DOI immutable created timestamp in Asia/Shanghai",
            "registered_categories": sorted(REGISTERED),
            "raw_identity_count": len(items),
            "withdrawn_excluded": sorted(WITHDRAWN),
            "identities": [
                {key: item[key] for key in (
                    "arxiv_id", "source_family_id", "title", "abstract", "categories",
                    "datacite_created_utc", "datacite_registered_utc", "datacite_doi",
                    "source_locator", "resolved_owner_report_date", "title_abstract_sha256",
                )}
                for item in items
            ],
        }
        screen_payload = {
            "schema": "canonical-title-abstract-semantic-screening-checkpoint-v2.1",
            "report_date": owner,
            "status": "fresh_context_audit_pending",
            "raw_identity_count": len(items),
            "retained_prior_decision": sum(item["semantic_screen_status"].startswith("retained") for item in items),
            "closure_proposals_pending_audit": sum(item["semantic_screen_status"].startswith("closure_proposed") for item in items),
            "items": [
                {key: item.get(key) for key in (
                    "arxiv_id", "source_family_id", "title", "categories", "title_abstract_sha256",
                    "semantic_screen_status", "semantic_decision_kind", "semantic_screen_reason",
                    "prior_candidate", "prior_source_report_day",
                )}
                for item in items
            ],
        }
        for name, payload in (
            ("canonical-raw-identity-inventory-v2.1.json.gz", raw_payload),
            ("canonical-semantic-screening-checkpoint-v2.1.json.gz", screen_payload),
        ):
            with gzip.open(packet / name, "wt", encoding="utf-8") as handle:
                json.dump(payload, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
        summary["per_report"][owner] = {
            "raw": len(items),
            "retained_prior": screen_payload["retained_prior_decision"],
            "closure_proposals_pending_audit": screen_payload["closure_proposals_pending_audit"],
        }

    (AUDIT / "raw-semantic-recovery-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
