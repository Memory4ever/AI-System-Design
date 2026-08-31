#!/usr/bin/env python3
"""Build the deterministic 2026-05-03 Daily discovery and screening packet.

The script deliberately separates full registered-category recall from the
human-reviewed Candidate Denominator.  Retained identities are an explicit
allow-list; every other registered hit receives a concrete pre-denominator
closure and is never assigned Score V2.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE = ROOT / "papers/2026/05/_sources/datacite-arxiv-202605-v2"
OUT = Path(__file__).resolve().parent
START = "2026-05-02T01:00:00Z"
END = "2026-05-03T01:00:00Z"

CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
KEYWORD = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}
REGISTERED = CORE | KEYWORD

# Admission was decided after a complete title+abstract pass over all 274
# registered identities.  These papers change a durable mechanism, state /
# control owner, evaluation contract, or design boundary.
RETAIN = {
    "2605.01188": ("SF-COMPUTE-OPTIMAL-TOKENIZATION", "MODEL-TOKENIZER", 3, 3, 3),
    "2605.01194": ("SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE", "MULTIMODAL-EMBODIED-VLA", 3, 3, 2),
    "2605.01195": ("SF-TAIL-SAFE-RUNTIME-MONITOR", "MULTIMODAL-EMBODIED-VLA", 3, 3, 2),
    "2605.01203": ("SF-GRBEN-PROCESS-REWARD-EVAL", "PLATFORM-EVALUATION-SYSTEM", 2, 3, 2),
    "2605.01255": ("SF-ACTIVATION-GRADIENT-COMPRESSION", "TRAIN-DISTRIBUTED-TRAINING", 3, 3, 3),
    "2605.01311": ("SF-CONFOUNDED-LOG-EVALUATION", "PLATFORM-EVALUATION-SYSTEM", 3, 3, 3),
    "2605.01342": ("SF-ACCESS-AWARE-VECTOR-INDEX", "AGENT-RAG", 3, 3, 3),
    "2605.01352": ("SF-VUDA-CUDA-VULKAN-SHARING", "PLATFORM-GPU-SCHEDULER", 3, 3, 2),
    "2605.01357": ("SF-LONG-FORM-LENGTH-VOLATILITY", "INFER-DECODE", 2, 3, 3),
    "2605.01394": ("SF-LIVEFMBENCH-SPECIFICATION-EVAL", "PLATFORM-EVALUATION-SYSTEM", 2, 3, 2),
    "2605.01425": ("SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER", "AGENT-RAG", 3, 3, 3),
    "2605.01477": ("SF-ACTION-AGENT-VIDEO-CONTROL", "MULTIMODAL-EMBODIED-VLA", 3, 3, 2),
    "2605.01640": ("SF-DATA-CONSTRAINED-SCALING-LAW", "TRAIN-PRETRAINING", 3, 3, 3),
    "2605.01644": ("SF-AGENT-SAFETY-SEARCH-MEASUREMENT", "PLATFORM-EVALUATION-SYSTEM", 3, 3, 3),
    "2605.02953": ("SF-DITRON-DISTRIBUTED-TILING", "INFER-TENSORRT-LLM", 3, 3, 2),
    "2605.02958": ("SF-REFUSAL-TRAJECTORY-MONITOR", "PLATFORM-SECURITY", 2, 3, 2),
    "2605.06690": ("SF-RECURSIVE-STATE-TERMINATION", "AGENT-REFLECTION", 3, 3, 3),
    "2605.08137": ("SF-PRUNING-BEHAVIORAL-REGRESSION", "PLATFORM-EVALUATION-SYSTEM", 2, 3, 3),
    "2605.12535": ("SF-POLICY-CARRIAGE-INTEGRITY", "AGENT-CONTEXT", 3, 3, 3),
    "2605.15208": ("SF-QUANTIZATION-BEHAVIORAL-REGRESSION", "PLATFORM-EVALUATION-SYSTEM", 2, 3, 3),
}


def first(items, key):
    return next((x.get(key, "") for x in items if x.get(key)), "")


def categories(attrs):
    out = []
    for item in attrs.get("subjects", []):
        match = re.search(r"\(([^()]+)\)$", item.get("subject", ""))
        if match:
            out.append(match.group(1))
    return sorted(set(out))


def submitted(attrs):
    return next((
        d.get("date") for d in attrs.get("dates", [])
        if d.get("dateType") == "Submitted" and d.get("dateInformation") == "v1"
    ), None)


def closure_reason(title: str, abstract: str, cats: list[str]) -> str:
    text = f"{title} {abstract}".lower()
    if any(k in text for k in ("survey", "perspective", "position:", "grand challenges", "framework for understanding")):
        kind = "综述、立场或概念框架未给出会改变现有系统 contract 的新 primary mechanism"
    elif any(k in text for k in ("medical", "clinical", "protein", "mri", "health", "agric", "dental", "farming")):
        kind = "单领域应用的表示或任务指标改进，未改变通用 AI System 的 state/data/control ownership"
    elif any(k in text for k in ("dataset", "benchmark")):
        kind = "局部任务数据集或 benchmark，没有形成可迁移的 evaluation/release contract 增量"
    elif any(k in text for k in ("accuracy", "segmentation", "classification", "forecast", "detection", "reconstruction")):
        kind = "局部模型/任务性能改进，证据不足以改变长期 Training、Inference 或 Platform 设计判断"
    elif any(k in text for k in ("agent", "llm", "language model", "retrieval", "lora", "reasoning")):
        kind = "虽与 Agent/LLM 相关，但属于单方法或单 workload 增益，未建立新的持久机制或 ownership 边界"
    elif set(cats) & {"cs.AR", "cs.DC", "cs.OS", "cs.PL", "cs.NI", "cs.PF"}:
        kind = "一般 systems/architecture 工作，未出现足以改变本书 AI workload contract 的机制增量"
    else:
        kind = "研究问题与 AI System 长期机制没有直接设计增量"
    return f"《{title}》：{kind}；保留 identity/date 以便未来重要 revision 重开。"


def main():
    snapshot_files = sorted(SOURCE.glob("*.json.gz"))
    raw_records = []
    snapshots = []
    for path in snapshot_files:
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            payload = json.load(handle)
        data = payload.get("data", [])
        raw_records.extend(data)
        snapshots.append({
            "path": str(path.relative_to(ROOT)),
            "records": len(data),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })

    raw_window = {}
    registered = {}
    for record in raw_records:
        attrs = record.get("attributes", {})
        v1 = submitted(attrs)
        if not v1 or not START <= v1 < END:
            continue
        doi = attrs.get("doi", "")
        aid = doi.lower().split("arxiv.", 1)[1] if "arxiv." in doi.lower() else ""
        if not aid:
            continue
        cats = categories(attrs)
        row = {
            "arxiv_id": aid,
            "submitted_v1_utc": v1,
            "first_public_date_beijing": "2026-05-02" if v1 < "2026-05-02T16:00:00Z" else "2026-05-03",
            "title": first(attrs.get("titles", []), "title"),
            "abstract": first([x for x in attrs.get("descriptions", []) if x.get("descriptionType") == "Abstract"], "description"),
            "categories": cats,
            "doi": doi,
        }
        raw_window[aid] = row
        if REGISTERED.intersection(cats):
            registered[aid] = row

    rows = []
    for aid in sorted(registered, key=lambda x: int(x.split(".")[1])):
        row = dict(registered[aid])
        is_core = bool(CORE.intersection(row["categories"]))
        if aid in RETAIN:
            family, owner, dd, sr, du = RETAIN[aid]
            row.update({
                "screening_route": "core_daily_full_semantic" if is_core else "keyword_category_full_semantic",
                "screening_decision": "retain",
                "source_family_id": family,
                "stable_node_id": owner,
                "score_v2": {"design_delta": dd, "system_reach": sr, "durability": du, "total": dd + sr + du},
                "closure_reason": "—",
            })
        else:
            row.update({
                "screening_route": "core_daily_full_semantic" if is_core else "keyword_category_semantic_or_false_negative_audit",
                "screening_decision": "pre_denominator_closure",
                "source_family_id": "—",
                "stable_node_id": "—",
                "score_v2": None,
                "closure_reason": closure_reason(row["title"], row["abstract"], row["categories"]),
            })
        rows.append(row)

    result = {
        "schema": "daily-v2.1-full-semantic-screening-v1",
        "report_date": "2026-05-03",
        "window_beijing": "[2026-05-02T09:00:00+08:00,2026-05-03T09:00:00+08:00)",
        "window_utc": f"[{START},{END})",
        "monthly_snapshot_unique_records": len(raw_records),
        "raw_window_identities_all_categories": len(raw_window),
        "registered_window_identities": len(rows),
        "core_daily_semantic_screened": sum(bool(CORE.intersection(r["categories"])) for r in rows),
        "keyword_category_screened": sum(not bool(CORE.intersection(r["categories"])) for r in rows),
        "retained_candidates": sum(r["screening_decision"] == "retain" for r in rows),
        "pre_denominator_closures": sum(r["screening_decision"] != "retain" for r in rows),
        "snapshots": snapshots,
        "rows": rows,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "screening-ledger-v2.1.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    header = ["arxiv_id", "submitted_v1_utc", "categories", "title", "screening_route", "screening_decision", "source_family_id", "stable_node_id", "score_v2_total", "closure_reason"]
    lines = ["\t".join(header)]
    for row in rows:
        score = row["score_v2"]["total"] if row["score_v2"] else "—"
        values = [row["arxiv_id"], row["submitted_v1_utc"], ",".join(row["categories"]), row["title"], row["screening_route"], row["screening_decision"], row["source_family_id"], row["stable_node_id"], str(score), row["closure_reason"]]
        lines.append("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in values))
    (OUT / "screening-ledger-v2.1.tsv").write_text("\n".join(lines) + "\n")
    (OUT / "identity-date-provenance.json").write_text(json.dumps({"window": result["window_beijing"], "raw": list(raw_window.values()), "registered": list(registered.values())}, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("monthly_snapshot_unique_records", "raw_window_identities_all_categories", "registered_window_identities", "core_daily_semantic_screened", "keyword_category_screened", "retained_candidates", "pre_denominator_closures")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
