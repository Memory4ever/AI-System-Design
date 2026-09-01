#!/usr/bin/env python3
"""Freeze the author-reviewed Candidate Denominator for 2026-04-01..07.

The explicit retain set is the result of title+abstract semantic review.  The
rules below only encode closure explanations; they do not decide admission.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Explicit semantic-admission decisions.  Inclusion means the abstract claims
# a potentially durable change to AI-system mechanism, state/control ownership,
# evaluation contract, or a current Books conclusion.  It does not mean that
# the claim has survived exact-v1 review or should enter Books.
RETAINED = {
    # 2026-04-01
    "2603.29231", "2603.29235", "2603.29247", "2603.29357", "2603.29399",
    "2603.29403", "2603.29493", "2603.29494", "2604.16400", "2603.29559",
    "2603.29640", "2604.00073", "2603.29844", "2603.29919", "2604.02372",
    "2604.00131", "2604.00136", "2604.00200", "2604.02375",
    # 2026-04-02
    "2604.00368", "2604.00392", "2604.00414", "2604.00499", "2604.00529",
    "2604.00726", "2604.00830", "2604.00835", "2604.01007", "2604.01020",
    "2604.01039", "2604.01128", "2604.01168", "2604.01193", "2604.01221",
    "2604.01499",
    # 2026-04-03
    "2604.01560", "2604.01563", "2604.01597", "2604.01607", "2604.01618",
    "2604.01621", "2604.01723", "2604.01904", "2604.02007", "2604.02268",
    "2604.02288", "2604.02478", "2604.02556",
    # 2026-04-04
    "2604.02715", "2604.02721", "2604.02766", "2604.02947", "2604.02965",
    "2604.02985", "2604.02986", "2604.03070", "2604.22782", "2604.03081",
    "2604.03088", "2604.03128", "2604.03143", "2604.03144", "2604.03179",
    "2604.03191", "2604.03395", "2604.03420",
    # 2026-04-05
    "2604.03588", "2604.03679",
    # 2026-04-06
    "2604.03956", "2604.03964", "2604.04013", "2604.04142", "2604.04161",
    "2604.04247", "2604.04258", "2604.04261",
    # 2026-04-07
    "2604.04399", "2604.04410", "2604.04503", "2604.04561", "2604.04654",
    "2604.04701", "2604.04722", "2604.04743", "2604.04750", "2604.04783",
    "2604.04804", "2604.05012", "2604.04834", "2604.04855", "2604.04894",
    "2604.04895", "2604.05014", "2604.05091", "2604.05117", "2604.05119",
    "2604.05134", "2604.05248", "2604.05250", "2604.05267",
}

DOMAIN = re.compile(
    r"\b(?:medical|clinical|health|cancer|disease|finance|financial|trading|"
    r"wireless|satellite|chemistry|molecular|material|agriculture|education|"
    r"student|legal|law|music|traffic|weather|remote sensing|radiology)\b", re.I
)
BENCHMARK = re.compile(r"\b(?:benchmark|dataset|survey|taxonomy|evaluation of|empirical study)\b", re.I)
LOCAL_MODEL = re.compile(
    r"\b(?:classification|segmentation|detection|forecast|prediction|retrieval|"
    r"image restoration|speech recognition|question answering)\b", re.I
)


def closure(item: dict) -> tuple[str, str]:
    text = f"{item['title']} {item['abstract']}"
    if DOMAIN.search(text):
        return (
            "domain_application_without_system_delta",
            "关闭：该工作主要把既有模型/Agent 方法用于特定领域，title+abstract 未改变通用 AI System 的状态、数据或控制权。",
        )
    if BENCHMARK.search(item["title"]):
        return (
            "benchmark_without_evaluation_contract_delta",
            "关闭：该 benchmark/dataset 面向局部任务或模型能力，title+abstract 未提出可迁移的 evaluation/release contract 变化。",
        )
    if LOCAL_MODEL.search(text):
        return (
            "localized_model_quality_delta",
            "关闭：该方法报告局部模型或任务质量改进，但未改变长期架构、训练/推理运行时或平台责任边界。",
        )
    return (
        "no_durable_ai_system_delta",
        "关闭：title+abstract 未给出足以改变长期 AI System 设计判断、owner contract 或既有 Books 结论的机制。",
    )


def retention_reason(item: dict) -> str:
    title = item["title"]
    return (
        f"保留：`{title}` 的 title+abstract 指向可迁移的 AI System 机制、状态/控制权或 evaluation contract；"
        "是否成立及是否进入 Books 必须由 exact-v1 全文与相邻章节比较决定。"
    )


def main() -> None:
    seen: set[str] = set()
    for day in range(1, 8):
        packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
        inventory = json.loads((packet / "inventory.json").read_text(encoding="utf-8"))
        rows = []
        for item in inventory["identities"]:
            aid = item["arxiv_id"]
            if aid in RETAINED:
                decision = "retained"
                reason_code = "durable_system_delta_requires_fulltext"
                reason = retention_reason(item)
                seen.add(aid)
            else:
                decision = "pre_denominator_closure"
                reason_code, reason = closure(item)
            rows.append({
                "arxiv_id": aid,
                "identity": item["identity"],
                "published_v1_utc": item["published_v1_utc"],
                "published_v1_beijing": item["published_v1_beijing"],
                "primary_category": item["primary_category"],
                "route": item["route"],
                "title": item["title"],
                "abstract": item["abstract"],
                "screening_decision": decision,
                "reason_code": reason_code,
                "reason": reason,
            })
        retained = [row for row in rows if row["screening_decision"] == "retained"]
        closure_rows = [row for row in rows if row["screening_decision"] != "retained"]
        payload = {
            "schema": "daily-v2.1-semantic-screening-ledger-v1",
            "report_date": f"2026-04-{day:02d}",
            "screening_scope": "all registered identities; Core full title+abstract semantic review; filtered categories bounded semantic review",
            "raw_registered_identities": len(rows),
            "retained_candidates": len(retained),
            "pre_denominator_closures": len(closure_rows),
            "denominator_id": "sha256:" + hashlib.sha256(
                "\n".join(sorted(row["identity"] for row in retained)).encode()
            ).hexdigest(),
            "rows": rows,
        }
        (packet / "screening-ledger.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        fields = tuple(rows[0]) if rows else ()
        with (packet / "screening-ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)
        print(json.dumps({
            "date": payload["report_date"],
            "raw": len(rows),
            "retained": len(retained),
            "closures": len(closure_rows),
            "denominator_id": payload["denominator_id"],
        }, ensure_ascii=False))
    missing = RETAINED - seen
    if missing:
        raise RuntimeError(f"retained identities did not resolve into 04-01..07 windows: {sorted(missing)}")


if __name__ == "__main__":
    main()
