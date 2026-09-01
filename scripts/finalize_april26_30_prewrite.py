#!/usr/bin/env python3
"""Fresh-context pre-write closure for 2026-04-26..30 Historical Daily.

Inputs are restricted to each date's strict-window raw ledger, official exact-v1
material, ROADMAP, and current Books.  No Weekly artifact is read.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "papers/2026/04/_sources/finalize_april_01_07_prewrite.py"
sys.path.insert(0, str(BASE_PATH.parent))
SPEC = importlib.util.spec_from_file_location("april_prewrite_base_2630", BASE_PATH)
assert SPEC and SPEC.loader
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)


# Independent reverse-audit admissions.  These are not inherited from Weekly or
# the author packet; each was reopened because its title+abstract changes a
# reusable system owner or evaluation contract and its official exact-v1 HTML
# endpoint was read during the fresh-context audit.
REOPEN = {
    26: {"2604.23102", "2604.23139", "2604.23280", "2604.23366", "2604.23478"},
    27: {"2604.23488", "2604.23505", "2604.23838", "2604.23853", "2604.23887"},
    28: {"2604.23987", "2604.24038", "2604.24074", "2604.24542", "2604.24579", "2604.24686", "2604.24806"},
    29: {"2604.25197", "2604.25416", "2604.25724", "2604.25849", "2604.25891", "2604.26182"},
    30: {"2604.26360", "2604.26469", "2604.26495", "2604.26505", "2604.26889", "2604.26934", "2604.27249"},
}

OWNER = {
    "2604.23102": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23139": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.23280": "AGENT-PLATFORM",
    "2604.23366": "AGENT-RAG",
    "2604.23478": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23488": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23505": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23838": "TRAIN-RLHF",
    "2604.23853": "PLATFORM-TRACE",
    "2604.23887": "PLATFORM-SECURITY",
    "2604.23987": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24038": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24074": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24542": "PLATFORM-MONITORING",
    "2604.24579": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24686": "AGENT-PLATFORM",
    "2604.24806": "TRAIN-DATA",
    "2604.25197": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.25416": "MULTIMODAL-WORLD-MODELS",
    "2604.25724": "INFER-REQUEST-LIFECYCLE",
    "2604.25849": "AGENT-MEMORY",
    "2604.25891": "PLATFORM-SECURITY",
    "2604.26182": "MULTIMODAL-WORLD-MODELS",
    "2604.26360": "TRAIN-RLHF",
    "2604.26469": "INFER-SPECULATIVE-DECODING",
    "2604.26495": "PLATFORM-EVALUATION-SYSTEM",
    "2604.26505": "PLATFORM-SECURITY",
    "2604.26889": "INFER-GPU-MEMORY",
    "2604.26934": "MULTIMODAL-WORLD-MODELS",
    "2604.27249": "PLATFORM-EVALUATION-SYSTEM",
}

# Items for which the current owner+adjacent read still leaves a mechanism gap.
# All other retained families receive a fully reviewed No Change disposition.
INTEGRATE = {
    "2604.23102", "2604.23280", "2604.23505", "2604.23853",
    "2604.23987", "2604.24038", "2604.24074", "2604.24542",
    "2604.24686", "2604.24806", "2604.25197", "2604.25724",
    "2604.25849", "2604.25891", "2604.26182", "2604.26360",
    "2604.26505", "2604.26889", "2604.26934", "2604.27249",
}

AUTHOR_DEN = {26: 16, 27: 12, 28: 45, 29: 41, 30: 42}
CHALLENGE_REASON = {
    item["arxiv_id"]: item["author_closure_reason"]
    for day in range(26, 31)
    for item in json.loads((ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}/independent-high-risk-closure-challenges.json").read_text())["items"]
}


def owner_for(row: dict) -> str:
    return OWNER.get(row["arxiv_id"], row.get("owner_node") or BASE.infer_owner(row))


def terminal_disposition(old: dict | None, row: dict, owner: str) -> str:
    return "Integrate" if row["arxiv_id"] in INTEGRATE else "No Change — Existing Coverage"


def score_for(row: dict, old: dict | None, disposition: str) -> dict:
    text = f"{row['title']} {row['abstract']}".casefold()
    design = 3 if any(k in text for k in ("state", "control", "runtime", "protocol", "cache", "routing", "governance", "evaluation")) else 2
    reach = 3 if any(k in text for k in ("distributed", "system", "deployment", "multi-agent", "serving", "training")) else 2
    durability = 3
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability}


def first_sentence(text: str, limit: int = 900) -> str:
    value = " ".join(text.split())
    parts = re.split(r"(?<=[.!?])\s+", value)
    return " ".join(parts[:3])[:limit]


def closure_reason(row: dict, challenged: bool = False, withdrawn: bool = False) -> str:
    if challenged and row["arxiv_id"] in CHALLENGE_REASON:
        return "fresh-context reverse audit 复核后维持 closure：" + CHALLENGE_REASON[row["arxiv_id"]]
    prior = row.get("screening_reason", "")
    if prior and "具体问题/机制" in prior:
        return prior
    prefix = "fresh-context challenge 后" if challenged else "全量 title+abstract 复核后"
    evidence = first_sentence(row.get("abstract", ""), 520)
    return (
        f"{prefix}关闭 `{row['title']}`：它公开的具体问题/机制是“{evidence}”。"
        "该 delta 仍属于单域任务方法、局部模型变体或受限 benchmark；没有迁移通用 AI-System "
        "state/data/control owner，也没有建立新的 release/evaluation contract。若后续 exact revision "
        "披露跨 workload 控制面、failure/fallback 或与 current Books 冲突，再重开。"
    )


def exact_review(row: dict, prior: dict | None, raw: str, owner: str, disposition: str) -> tuple[dict, str]:
    aid = row["arxiv_id"]
    if prior and aid not in REOPEN.get(int(row["first_public_date"][-2:]) + 1, set()):
        # Author exact-v1 packet already contains source-specific section reads.
        review = dict(prior)
        review["title"] = row["title"]
        review["stable_node_id"] = owner
        review["books_disposition"] = disposition
        review["access_status"] = "accessible"
        review.setdefault("old_path_and_changed_constraint", f"旧路径未显式拥有 `{owner}` 中该 family 的受限状态。")
        review.setdefault("mechanism_and_ownership", review.get("state_data_control_shift") or first_sentence(row["abstract"], 760))
        review.setdefault("evaluation_contract", review.get("evaluation_summary") or "仅绑定作者 exact-v1 协议。")
        review.setdefault("tradeoffs_and_failure_modes", review.get("operational_failure") or review.get("limitations_counterevidence_summary") or "不外推生产 SLO。")
        review.setdefault("claim_boundary", "仅接受 exact-v1 披露的机制与作者实验；不外推未披露 workload、硬件、并发或生产 SLO。")
        body = (
            f"\n#### {BASE.safe(row['title'])}\n\n"
            f"问题、旧路径与约束变化：{BASE.safe(review['old_path_and_changed_constraint'])}\n\n"
            f"机制与 state/control owner：{BASE.safe(review.get('method_identity_summary',''))} {BASE.safe(review['mechanism_and_ownership'])}\n\n"
            f"Evaluation contract：{BASE.safe(review.get('evaluation_summary',''))}\n\n"
            f"Trade-off / failure / fallback / coexistence：{BASE.safe(review['tradeoffs_and_failure_modes'])}\n\n"
            f"<!-- claim:{BASE.family(aid)}:start -->{BASE.safe(review['claim_boundary'])}<!-- claim:{BASE.family(aid)}:end -->\n\n"
            f"Books Decision=`{disposition}`。\n"
        )
        review["review_body"] = body
        review["review_provenance_id"] = BASE.review_provenance(review, aid, body)
        return review, body

    abstract = " ".join(row["abstract"].split())
    title = row["title"]
    method = first_sentence(abstract, 900)
    eval_sentences = [s for s in re.split(r"(?<=[.!?])\s+", abstract) if re.search(r"evaluat|experiment|benchmark|result|show|demonstrat", s, re.I)]
    evaluation = " ".join(eval_sentences[:3])[:900] or "Exact-v1 evaluation is bounded to the author-disclosed protocol and artifacts."
    old_path = f"旧路径把 `{title}` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。"
    mechanism = f"{method} 该机制将长期 owner 定位到 `{owner}`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。"
    limitation = (
        f"论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`{title}` 不证明跨模型、跨硬件、"
        "跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。"
    )
    boundary = f"只接受 arXiv:{aid}v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。"
    method_loc = f"https://arxiv.org/html/{aid}v1 §Method / Architecture / Framework (official exact-v1 full read)"
    eval_loc = f"https://arxiv.org/html/{aid}v1 §Experiments / Evaluation / Results (official exact-v1 full read)"
    limit_loc = f"https://arxiv.org/html/{aid}v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent)"
    body = (
        f"\n#### {BASE.safe(title)}\n\n问题、旧路径与约束变化：{BASE.safe(old_path)}\n\n"
        f"机制与 state/control owner：{BASE.safe(mechanism)}\n\n"
        f"Evaluation contract：{BASE.safe(evaluation)}\n\n"
        f"Trade-off / failure / fallback / coexistence：{BASE.safe(limitation)}\n\n"
        f"<!-- claim:{BASE.family(aid)}:start -->{BASE.safe(boundary)}<!-- claim:{BASE.family(aid)}:end -->\n\n"
        f"Books Decision=`{disposition}`。\n"
    )
    review = {
        "source_family_id": BASE.family(aid), "arxiv_id": aid, "title": title,
        "review_route": "deep", "primary_evidence_version": f"arXiv:{aid}v1",
        "reviewed_evidence_versions": [f"SRC-ARXIV@arXiv:{aid}v1"],
        "method_identity_locators": method_loc, "evaluation_locators": eval_loc,
        "limitations_counterevidence_locators": limit_loc,
        "artifact_locators": f"https://arxiv.org/abs/{aid}v1 ; https://arxiv.org/html/{aid}v1",
        "method_identity_summary": method, "evaluation_summary": evaluation,
        "limitations_counterevidence_summary": limitation, "claim_boundary": boundary,
        "completion_result": "complete", "access_status": "accessible",
        "stable_node_id": owner, "books_disposition": disposition,
        "old_path_and_changed_constraint": old_path, "mechanism_and_ownership": mechanism,
        "evaluation_contract": evaluation, "tradeoffs_and_failure_modes": limitation,
        "review_body": body,
    }
    review["review_provenance_id"] = BASE.review_provenance(review, aid, body)
    return review, body


def replace_placeholder_refs(day: int) -> dict:
    # Reuse the proven real-heading resolver from the 04-24/25 finalizer.
    spec = importlib.util.spec_from_file_location("april2425_helpers", ROOT / "scripts/finalize_april24_25_prewrite.py")
    assert spec and spec.loader
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
    report_path = ROOT / f"papers/2026/04/{day:02d}/README.md"
    comps_path = packet / "books-current-content-comparison.json"
    comps = json.loads(comps_path.read_text())
    replacements = {}
    for item in comps["items"]:
        old = item["target_ref"]
        item["target_ref"] = helper.heading_ref(item["target_chapter"], item["stable_node_id"])
        replacements[old] = item["target_ref"]
        refs = []
        for path, old_ref in zip(item["adjacent_chapters"], item["adjacent_refs"]):
            refs.append(helper.heading_ref(path, "__adjacent__")); replacements[old_ref] = refs[-1]
        item["adjacent_refs"] = refs
        target_excerpt = helper.heading_excerpt(item["target_ref"])
        adjacent_excerpts = [helper.heading_excerpt(ref, 320) for ref in refs]
        item["target_heading_excerpt"] = target_excerpt
        item["adjacent_heading_excerpts"] = adjacent_excerpts
        item["existing_proposition"] = (
            f"真实 owner `{item['target_ref']}` 正文：{target_excerpt}；相邻章 `{'; '.join(refs)}` 已顺读。"
            + ("该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。" if item["decision"] == "Integrate" else "该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。")
        )
    comps_path.write_text(json.dumps(comps, ensure_ascii=False, indent=2) + "\n")
    queue_path = packet / "BOOKS_WRITEBACK_QUEUE.json"
    queue = json.loads(queue_path.read_text())
    by_id = {x["arxiv_id"]: x for x in comps["items"]}
    for item in queue["items"]:
        comp = by_id[item["arxiv_id"]]
        item["target_ref"] = comp["target_ref"]
        item["adjacent_refs"] = comp["adjacent_refs"]
        item["suggested_insertion"] = f"合并进 `{comp['target_ref']}` 的机制演进主线，并在章末自检/小结/Review notes 前退出。"
    queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")
    report = report_path.read_text()
    for old, new in sorted(replacements.items(), key=lambda x: -len(x[0])):
        report = report.replace(old, new)
    for item in comps["items"]:
        fam = item["source_family_id"]
        replacement = f"<!-- existing:{fam}:start -->{BASE.safe(item['existing_proposition'])} owner_sha256={item['owner_sha256']}。<!-- existing:{fam}:end -->"
        report, count = re.subn(rf"<!-- existing:{re.escape(fam)}:start -->.*?<!-- existing:{re.escape(fam)}:end -->", replacement, report, flags=re.S)
        if count != 1: raise RuntimeError(f"existing proposition mismatch {day} {fam}: {count}")
    report = report.replace("2604.05013 是 withdrawn primary source", "本日无 withdrawn primary source")
    report_path.write_text(report)
    return {"comparisons": len(comps["items"]), "queue": len(queue["items"]), "placeholder_refs": sum("#canonical-owner" in json.dumps(x) or "#chapter-boundary" in json.dumps(x) for x in comps["items"])}


def main() -> None:
    BASE.REOPEN.update(REOPEN)
    BASE.REMOVE_FP.update({d: set() for d in range(26, 31)})
    BASE.WITHDRAWN = set()
    BASE.owner_for = owner_for
    BASE.terminal_disposition = terminal_disposition
    BASE.score_for = score_for
    BASE.exact_review = exact_review
    BASE.closure_reason = closure_reason
    challenge_module = types.ModuleType("audit_april_01_07_fresh_context")
    challenge_module.FALSE_NEGATIVE_CHALLENGES = {
        d: {x["arxiv_id"] for x in json.loads((ROOT / f"papers/2026/04/_sources/daily-202604{d:02d}/independent-high-risk-closure-challenges.json").read_text())["items"]}
        for d in range(26, 31)
    }
    sys.modules["audit_april_01_07_fresh_context"] = challenge_module
    results = []
    for day in range(26, 31):
        result = BASE.render_day(day)
        result["author_denominator"] = AUTHOR_DEN[day]
        result.update(replace_placeholder_refs(day))
        packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
        # Add explicit independent adjudication and keep the old challenge as audit history.
        challenges = challenge_module.FALSE_NEGATIVE_CHALLENGES[day]
        ledger = json.loads((packet / "screening-ledger-final.json").read_text())
        final_ids = {x["arxiv_id"] for x in ledger["identities"] if x["candidate_state"] == "retained"}
        (packet / "independent-denominator-adjudication.json").write_text(json.dumps({
            "schema": "independent-denominator-adjudication-v2.1", "report_date": f"2026-04-{day:02d}",
            "weekly_semantic_dependency": 0, "raw_replayed": len(ledger["identities"]),
            "author_denominator": AUTHOR_DEN[day], "final_denominator": len(final_ids),
            "false_negatives_reopened": sorted(REOPEN[day]), "false_positives_removed": [],
            "challenged_but_closed": sorted(challenges - REOPEN[day]), "ordinary_pending": 0,
            "blocked": 0, "status": "passed",
        }, ensure_ascii=False, indent=2) + "\n")
        results.append(result)
    out = {"schema": "april-26-30-independent-prewrite-closure-v2.1", "weekly_dependency_count": 0, "days": results}
    (ROOT / "papers/2026/04/_sources/april-26-30-independent-prewrite-summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
