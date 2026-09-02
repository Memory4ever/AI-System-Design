#!/usr/bin/env python3
"""Freeze author-side denominators for March lane B after full abstract replay."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Explicit results of the lane's title+abstract semantic replay.  Admission is
# intentionally narrow: a paper must plausibly change a durable AI-system
# mechanism, ownership boundary, or evaluation/release contract.
RETAINED = {
    9: {
        "2603.07416", "2603.07427", "2603.07433", "2603.07466", "2603.07557",
        "2603.07607", "2603.07670", "2603.07685", "2603.07770", "2603.07777",
        "2603.07799", "2603.08761", "2603.10044", "2603.15658",
    },
    10: {
        "2603.07915", "2603.07917", "2603.07972", "2603.08088", "2603.08163",
        "2603.08221", "2603.08429", "2603.08519", "2603.08640", "2603.08797",
        "2603.08806", "2603.08835", "2603.08960", "2603.09023", "2603.09046",
        "2603.10057", "2603.10062", "2603.15661", "2603.19289",
    },
    11: {
        "2603.09079", "2603.09086", "2603.09121", "2603.09157", "2603.09180",
        "2603.09192", "2603.09216", "2603.09221", "2603.09241", "2603.09290",
        "2603.09297", "2603.09435", "2603.09453", "2603.09488", "2603.09513",
        "2603.09555", "2603.09619", "2603.09657", "2603.09692", "2603.09716",
        "2603.09756", "2603.09821", "2603.09877", "2603.09891", "2603.09892",
        "2603.10085", "2603.10087", "2603.10088", "2603.10143", "2603.10165",
        "2603.10291",
    },
    12: {
        "2603.10353", "2603.10422", "2603.10469", "2603.10577", "2603.10600",
        "2603.10712", "2603.10749", "2603.10765", "2603.10899", "2603.11101",
        "2603.11132", "2603.11273", "2603.11287", "2603.11337",
    },
    13: {
        "2603.11438", "2603.11445", "2603.11504", "2603.11560", "2603.11564",
        "2603.11768", "2603.11853", "2603.11873", "2603.11896", "2603.11935",
        "2603.12031", "2603.12056", "2603.12118", "2603.12255", "2603.12396",
        "2603.12465", "2603.13404", "2603.13417", "2603.13420",
    },
    14: {
        "2603.12553", "2603.12614", "2603.12621", "2603.12631", "2603.12639",
        "2603.12646", "2603.12655", "2603.12671", "2603.12707", "2603.12831",
        "2603.12933", "2603.13017", "2603.13019", "2603.13099", "2603.13110",
        "2603.13176", "2603.13189", "2603.13215", "2603.13424", "2603.13428",
        "2603.13443", "2603.13591", "2603.13594", "2603.13605", "2603.13606",
        "2603.13644", "2603.15676",
    },
    15: {
        "2603.13686", "2603.13724", "2603.13835", "2603.13875", "2603.13893",
        "2603.13906", "2603.13950", "2603.13966", "2603.13972", "2603.14011",
        "2603.14057", "2603.14110",
    },
    16: {
        "2603.14212", "2603.14224", "2603.14229", "2603.14251", "2603.14303",
        "2603.14332", "2603.14371", "2603.14417", "2603.14468", "2603.14486",
        "2603.14517", "2603.14523", "2603.14597", "2603.14602", "2603.14633",
        "2603.14635", "2603.14688",
    },
}

DOMAIN = re.compile(r"\b(?:medical|clinical|patient|molecular|protein|finance|wireless|traffic|education|agriculture|remote sensing|satellite)\b", re.I)
EVAL = re.compile(r"\b(?:benchmark|dataset|evaluation|survey|taxonomy)\b", re.I)
LOCAL = re.compile(r"\b(?:classification|segmentation|detection|forecast|recommendation|recognition|estimation)\b", re.I)
WITHDRAWN = re.compile(r"\b(?:this paper has been withdrawn|this submission has been withdrawn|withdrawn by)\b", re.I)


def sentence(text: str) -> str:
    values = re.split(r"(?<=[.!?])\s+", " ".join(text.split()))
    return next((x for x in values if re.search(r"\b(?:propose|present|introduce|develop|design|show|study|build)\b", x, re.I)), values[0] if values else "")[:480]


def closure(row: dict) -> tuple[str, str]:
    text = row["title"] + " " + row["abstract"]
    if WITHDRAWN.search(text):
        return "withdrawn_primary_source", "权威 metadata 已标示撤回；只保留 identity/status，不进入候选、Review 或 Books。"
    if DOMAIN.search(text):
        return "domain_application_without_system_delta", "领域数据、标签或工作流增量未迁移为通用 AI System 的长期状态、控制或发布责任。"
    if EVAL.search(row["title"]):
        return "local_benchmark_without_contract_delta", "局部 benchmark/dataset 未改变 evaluator identity、可复算证据对象或 release gate。"
    if LOCAL.search(text):
        return "localized_model_quality_delta", "单任务质量改进未重新分配训练、推理或平台的 state/data/control owner。"
    return "no_durable_ai_system_delta", "摘要未显示足以改变长期 AI System 机制、owner contract、evaluation contract 或既有 Books 判断的设计增量。"


def main() -> None:
    found: set[str] = set()
    for day, selected in RETAINED.items():
        packet = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
        inventory = json.loads((packet / "inventory.json").read_text())
        rows = []
        for item in inventory["identities"]:
            aid = item["arxiv_id"]
            row = dict(item)
            if aid in selected:
                found.add(aid)
                row.update({
                    "screening_decision": "retained",
                    "screening_status": "candidate_denominator",
                    "reason_code": "durable_system_delta_requires_fulltext",
                    "screening_reason": f"保留：`{item['title']}` 的摘要机制（{sentence(item['abstract'])}）可能改变长期 AI System 的机制、状态/控制权或 evaluation/release contract；exact-v1 全文决定结论与 Books 处置。",
                })
            else:
                code, reason = closure(item)
                row.update({
                    "screening_decision": "closure",
                    "screening_status": "pre_denominator_closure",
                    "reason_code": code,
                    "screening_reason": f"`{item['title']}`：{reason}",
                })
            rows.append(row)
        actual = {row["arxiv_id"] for row in rows if row["screening_decision"] == "retained"}
        missing = selected - actual
        if missing:
            raise RuntimeError(f"03-{day:02d} selected identities missing from inventory: {sorted(missing)}")
        digest = hashlib.sha256("\n".join(sorted(actual)).encode()).hexdigest()
        payload = {
            "schema": "screening-ledger-v2.1-independent-author",
            "report_date": f"2026-03-{day:02d}",
            "registered_identities": len(rows),
            "full_semantic_screened": len(rows),
            "candidate_denominator": len(actual),
            "pre_denominator_closed": len(rows) - len(actual),
            "denominator_id": f"sha256:{digest}",
            "fresh_context_false_positive_false_negative_audit": "pending_independent_reviewer",
            "identities": rows,
        }
        (packet / "screening-ledger-author.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"date": payload["report_date"], "raw": len(rows), "retained": len(actual), "closures": len(rows)-len(actual), "denominator": payload["denominator_id"]}))


if __name__ == "__main__":
    main()
