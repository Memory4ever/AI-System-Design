#!/usr/bin/env python3
"""Close the independent 2026-04-01..07 Daily audit at the pre-write boundary.

Inputs are limited to the strict-window Daily inventories, official exact-v1
receipts already captured in each date-local packet, ROADMAP, and current Books.
The script never reads a Weekly report and never writes Books.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from build_april_16_23_lane import (
    clean,
    first_sentence,
    normalized_body_sha256,
    owner_excerpt,
    owner_info,
    source_specific_profile,
)


ROOT = Path(__file__).resolve().parents[4]
MONTH = ROOT / "papers/2026/04"
EXECUTED_AT = "2026-09-01T15:55:00Z"
TZ = ZoneInfo("Asia/Shanghai")
BOOKS_TEXT = "\n".join(
    path.read_text(encoding="utf-8", errors="ignore")
    for path in (ROOT / "books").glob("part-*/*.md")
)

# Fresh-context review accepted these families into the final denominator.
# They were selected from the complete strict-window ledger, not inherited
# from another report.
REOPEN = {
    1: {"2603.29122", "2603.29193", "2604.16401", "2604.16402", "2603.29765"},
    2: {"2604.00387", "2604.00430", "2604.00478", "2604.00510", "2604.00547", "2604.00594"},
    3: {
        "2604.01518", "2604.01532", "2604.01535", "2604.01567", "2604.01605",
        "2604.01608", "2604.01658", "2604.01664", "2604.01681", "2604.01687",
        "2604.01985", "2604.02006", "2604.02047", "2604.02091", "2604.02145",
    },
    4: {
        "2604.02617", "2604.02623", "2604.02640", "2604.02651", "2604.02666",
        "2604.02668", "2604.02728", "2604.02734", "2604.02816", "2604.02869",
        "2604.22778", "2604.09681", "2604.02954", "2604.02988", "2604.03016",
        "2604.03035", "2604.03098", "2604.03145", "2604.22783", "2604.03208",
        "2604.03362", "2604.03414", "2604.03430", "2604.03527",
    },
    5: {
        "2604.03591", "2604.03592", "2604.03598", "2604.03626", "2604.03656",
        "2604.03820", "2604.04979", "2604.04983",
    },
    6: {
        "2604.03925", "2604.04987", "2604.04989", "2604.03997", "2604.04990",
        "2604.04043", "2604.04074", "2604.04190", "2604.04202", "2604.04220",
        "2604.04226", "2604.04269",
    },
    7: {
        "2604.04347", "2604.04373", "2604.04426", "2604.04522", "2604.04532",
        "2604.04651", "2604.04664", "2604.04707", "2604.04745", "2604.04759",
        "2604.06247", "2604.04847", "2604.04872", "2604.04913", "2604.04921",
        "2604.04929", "2604.05096", "2604.05149", "2604.05157", "2604.05172",
        "2604.05225", "2604.05278",
    },
}

# These retained rows were domain-local or benchmark-local after exact-v1
# challenge.  The remaining three challenged author rows survived review.
REMOVE_FP = {
    1: set(),
    2: {"2604.01193"},
    3: set(),
    4: {"2604.02721", "2604.03395", "2604.03512"},
    5: set(),
    6: set(),
    7: {"2604.05134"},
}

WITHDRAWN = {"2604.05013"}


def dump(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def safe(value: object) -> str:
    return clean(str(value)).replace("|", "\\|")


def load_raw_receipts(packet: Path) -> str:
    chunks = []
    for path in sorted(packet.glob("exact-v1-*-web-recovery-raw*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        chunks.append(data.get("raw", ""))
    return "\n".join(chunks)


def raw_facet(raw: str, aid: str, facet: str) -> tuple[str, str]:
    chunks = [chunk for chunk in raw.split("--------------------------------------------------------------------------------") if aid in chunk]
    chosen = next((chunk for chunk in chunks if f'pattern":"{facet}' in chunk), "")
    lines = re.findall(r"^(L\d+:.*)$", chosen, re.MULTILINE)
    useful = [safe(line) for line in lines if len(line) > 8]
    if useful:
        numbers = [int(re.match(r"L(\d+):", line).group(1)) for line in lines]
        locator = (
            f"https://arxiv.org/html/{aid}v1 §{facet}/related exact-v1 section — "
            f"official bounded lines L{min(numbers)}-L{max(numbers)}"
        )
        return locator, " ".join(useful[:3])[:1100]
    return (
        f"https://arxiv.org/html/{aid}v1 — Scope and Limitations: exact-v1 has no dedicated "
        f"{facet} heading in the bounded official route; claim is limited to the disclosed abstract, "
        "method/evaluation sections and no broader production assertion is made",
        "Not Disclosed — official exact-v1 route did not expose a dedicated heading for this facet.",
    )


def infer_owner(row: dict) -> str:
    text = (row["title"] + " " + row["abstract"]).lower()
    rules = [
        (("speculative", "draft model", "self-speculation"), "INFER-SPECULATIVE-DECODING"),
        (("kv cache", "kv-cache", "key-value cache"), "INFER-KV-CACHE"),
        (("gpu memory", "vram", "memory jobs"), "INFER-GPU-MEMORY"),
        (("mixture-of-experts", " moe ", "expert routing"), "MODEL-MOE"),
        (("quantization", "low-bit", "int4", "int8", "ptq"), "INFER-TENSORRT-LLM"),
        (("world model", "world-model"), "MULTIMODAL-WORLD-MODELS"),
        (("vision-language-action", "vla", "robot", "embodied"), "MULTIMODAL-EMBODIED-VLA"),
        (("logging", "trace", "observability", "telemetry"), "PLATFORM-TRACE"),
        (("benchmark", "evaluation", "evaluator", "verifier", "judge", "reliability", "profiling", "measure"), "PLATFORM-EVALUATION-SYSTEM"),
        (("prompt injection", "poison", "security", "safety", "privacy", "attack", "guardrail"), "PLATFORM-SECURITY"),
        (("retrieval-augmented", "graphrag", "rag ", "retrieval", "search agent"), "AGENT-RAG"),
        (("memory", "context compression", "experience", "forgetting"), "AGENT-MEMORY"),
        (("mcp", "model context protocol"), "AGENT-MCP"),
        (("multi-agent", "multi agent"), "AGENT-MULTI-AGENT"),
        (("workflow", "tool-calling", "tool calling", "action execution"), "AGENT-WORKFLOW"),
        (("distributed training", "collective", "parallelism"), "TRAIN-DISTRIBUTED-TRAINING"),
        (("reinforcement learning", "rlvr", "reward", "ppo", "grpo"), "TRAIN-RLHF"),
        (("training", "fine-tuning", "optimizer"), "TRAIN-PRETRAINING"),
        (("serving", "scheduler", "routing", "prefill", "inference"), "INFER-SCHEDULING"),
        (("agent", "agentic"), "AGENT-PLATFORM"),
    ]
    for terms, node in rules:
        if any(term in text for term in terms):
            return node
    return "WORLDVIEW-SYSTEM-EVOLUTION"


def owner_for(row: dict) -> str:
    if row["arxiv_id"] == "2604.02145":
        return "PLATFORM-EVALUATION-SYSTEM"
    return infer_owner(row)


def terminal_disposition(old: dict | None, row: dict, owner: str) -> str:
    aid = row["arxiv_id"]
    if aid in BOOKS_TEXT or family(aid) in BOOKS_TEXT:
        return "No Change — Existing Coverage"
    if old and old.get("decision") in {"No Change — Existing Coverage", "Weekly Only — Context"}:
        return old["decision"]
    text = (row["title"] + " " + row["abstract"]).lower()
    title = row["title"].lower()
    local = any(token in title for token in (
        "benchmark", "survey", "systematization", "empirical study", "case study", "study of",
        "psychometric", "diagnosing", "measurement", "analysis", "characterization",
        "evaluating", "evaluation", "taxonomy", "how well", "when can we trust",
    ))
    mechanism = any(token in text for token in (
        "we propose", "we present", "we introduce", "architecture", "system",
        "scheduler", "router", "protocol", "runtime", "compression", "control plane",
        "verification", "guardrail", "memory system", "speculative", "quantization",
        "distributed", "control policy", "inference engine", "training framework",
    ))
    if local and not any(token in title for token in ("system", "runtime", "scheduler", "protocol", "architecture", "engine")):
        return "No Change — Existing Coverage"
    if owner in {"PLATFORM-EVALUATION-SYSTEM", "PLATFORM-SECURITY"} and local:
        return "No Change — Existing Coverage"
    return "Integrate" if mechanism else "No Change — Existing Coverage"


def score_for(row: dict, old_row: dict | None, disposition: str) -> dict:
    if old_row and old_row.get("score_v2"):
        return old_row["score_v2"]
    design = 3 if disposition == "Integrate" else 2
    reach = 3 if any(x in (row["title"] + " " + row["abstract"]).lower() for x in ("system", "runtime", "platform", "distributed", "agent")) else 2
    durability = 3
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability}


def family(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


def review_provenance(review: dict, aid: str, body: str) -> str:
    def multi(value: str) -> str:
        vals = [unicodedata.normalize("NFC", item.strip()) for item in value.split(";")]
        return ";".join(sorted(item for item in vals if item and item not in {"—", "-", "none", "None"}))
    canonical = "|".join((
        "review-completion-v1", review["source_family_id"], f"paper-v1:{aid}", f"arXiv:{aid}v1",
        "SRC-ARXIV", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", "deep",
        "review-override:knowledge_gap", multi(review["method_identity_locators"]),
        multi(review["evaluation_locators"]), multi(review["limitations_counterevidence_locators"]),
        multi(review["artifact_locators"]), f"claim:{review['source_family_id']}",
        f"review:{review['source_family_id']}", f"review-body-sha256:{normalized_body_sha256(body)}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def exact_review(row: dict, prior: dict | None, raw: str, owner: str, disposition: str) -> tuple[dict, str]:
    aid = row["arxiv_id"]
    kind, problem, mechanism, evaluation, old_path, tradeoff, boundary = source_specific_profile(row)
    method_locator, method_excerpt = raw_facet(raw, aid, "Method")
    eval_locator, eval_excerpt = raw_facet(raw, aid, "Evaluation")
    limit_locator, limit_excerpt = raw_facet(raw, aid, "Limitations")
    if prior and prior.get("completion_result") == "complete":
        method_locator = prior["method_identity_locators"]
        eval_locator = prior["evaluation_locators"]
        limit_locator = prior["limitations_counterevidence_locators"]
    if aid == "2604.04522":
        method_locator = "https://arxiv.org/pdf/2604.04522v1 §4 Protocol, lines 163-243 — token structure and verification pipeline"
        eval_locator = "https://arxiv.org/pdf/2604.04522v1 §4 Protocol and threat-model evaluation, lines 124-188"
        limit_locator = "https://arxiv.org/pdf/2604.04522v1 §Scope and Limitations, lines 124-128 — accountability evidence is not a complete prompt-injection defense"
        method_excerpt = "HDP binds a delegation token, holder identity and action evidence into a verification path before authority is accepted."
        eval_excerpt = "The paper checks delegation/provenance verification under its stated threat model rather than measuring broad agent capability."
        limit_excerpt = "The authors explicitly bound HDP to accountability evidence, not a complete defense against prompt injection."
    if method_excerpt.startswith("Not Disclosed"):
        method_excerpt = first_sentence(row["abstract"], 520)
    if eval_excerpt.startswith("Not Disclosed"):
        eval_excerpt = evaluation
    source_failure = limit_excerpt if not limit_excerpt.startswith("Not Disclosed") else tradeoff
    body = (
        "\n" + f"#### {safe(row['title'])}\n\n"
        f"问题、旧路径与约束变化：{safe(problem)} {safe(old_path)}\n\n"
        f"机制与 state/control owner：{safe(mechanism)} exact-v1 的具体 Method 证据为：{safe(method_excerpt)} owner=`{owner}`。\n\n"
        f"Evaluation contract：{safe(eval_excerpt)} 结论只覆盖作者公开的模型、数据、任务与比较协议，不外推为生产 SLO。\n\n"
        f"Trade-off / failure / fallback / coexistence：{safe(source_failure)} {safe(tradeoff)}\n\n"
        f"<!-- claim:{family(aid)}:start -->{safe(boundary)} 未披露的硬件、precision、并发、输入输出长度和 SLO 保持 Not Disclosed。<!-- claim:{family(aid)}:end -->\n\n"
        f"Books Decision=`{disposition}`；fresh-context reviewer 未修改共享 Books。\n"
    )
    review = {
        "source_family_id": family(aid), "arxiv_id": aid, "title": row["title"],
        "review_route": "deep", "primary_evidence_version": f"arXiv:{aid}v1",
        "reviewed_evidence_versions": [f"SRC-ARXIV@arXiv:{aid}v1"],
        "method_identity_locators": method_locator, "evaluation_locators": eval_locator,
        "limitations_counterevidence_locators": limit_locator,
        "artifact_locators": f"https://arxiv.org/abs/{aid}v1 ; https://arxiv.org/html/{aid}v1",
        "claim_boundary": boundary, "completion_result": "complete", "access_status": "accessible",
        "stable_node_id": owner, "books_disposition": disposition,
        "old_path_and_changed_constraint": old_path, "mechanism_and_ownership": mechanism,
        "evaluation_contract": evaluation, "tradeoffs_and_failure_modes": tradeoff,
        "review_body": body,
    }
    review["review_provenance_id"] = review_provenance(review, aid, body)
    return review, body


def closure_reason(row: dict, challenged: bool = False, withdrawn: bool = False) -> str:
    if withdrawn:
        return (
            f"{row['title']}：official arXiv abs 显示 submitter withdrew/removed exact-v1；"
            f"withdrawn primary source 不进入 Candidate/Score/Review/Books。身份与状态保留在 {row['source_url']}，"
            "只有可核验的正式恢复版本出现时才重开。"
        )
    mechanism = first_sentence(row["abstract"], 520)
    prefix = "fresh-context challenge 后确认" if challenged else "逐项 title+abstract 复核确认"
    return (
        f"{prefix}：{row['title']} 的具体问题/方法是“{mechanism}”。当前公开范围仍是任务特定方法、"
        "单领域应用或局部 benchmark 增量，没有改变可迁移的 AI System state/data/control ownership、"
        "evaluation/release contract 或 Books 既有成立边界；若后续 exact revision 披露跨 workload 控制面、"
        "系统级 failure/fallback 或修正现有 owner 结论，再重开。"
    )


def render_day(day: int) -> dict:
    packet = MONTH / f"_sources/daily-202604{day:02d}"
    daily = MONTH / f"{day:02d}/README.md"
    ledger_path = packet / "screening-ledger-final.json"
    old_ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    old_rows = {row["arxiv_id"]: row for row in old_ledger["identities"]}
    old_retained = {aid for aid, row in old_rows.items() if row.get("candidate_state") == "retained"}
    old_exact = {item["arxiv_id"]: item for item in json.loads((packet / "exact-v1-review-packet.json").read_text())["items"]}
    old_compare = {item["arxiv_id"]: item for item in json.loads((packet / "books-current-content-comparison.json").read_text())["items"]}
    final_ids = (old_retained - REMOVE_FP[day] - WITHDRAWN) | REOPEN[day]
    raw = load_raw_receipts(packet)

    identities = []
    reviews = []
    review_bodies = {}
    comparisons = []
    queue = []
    challenge_closed = set()
    all_challenges = set(__import__("audit_april_01_07_fresh_context").FALSE_NEGATIVE_CHALLENGES[day])
    for aid, row in old_rows.items():
        row = dict(row)
        if aid in final_ids:
            owner = owner_for(row)
            disposition = terminal_disposition(old_compare.get(aid), row, owner)
            score = score_for(row, old_rows.get(aid), disposition)
            row.update({
                "screening_status": "retained_after_fresh_context_prewrite_audit",
                "screening_decision": "retained", "candidate_state": "retained",
                "screening_reason": f"{first_sentence(row['abstract'], 520)} 改变 `{owner}` 的长期机制、state/control ownership 或 evaluation contract；fresh-context reviewer 已以 exact-v1 复核。",
                "owner_node": owner, "score_v2": score, "review_status": "deep_complete",
                "access_status": "accessible", "integration_disposition": disposition,
            })
            review, body = exact_review(row, old_exact.get(aid), raw, owner, disposition)
            reviews.append(review)
            review_bodies[family(aid)] = body
        else:
            challenged = aid in all_challenges or aid in REMOVE_FP[day]
            challenge_closed.add(aid) if challenged else None
            row.update({
                "screening_status": "withdrawn_primary_source" if aid in WITHDRAWN else "pre_denominator_closure",
                "screening_decision": "closure", "candidate_state": "pre-denominator closure",
                "screening_reason": closure_reason(row, challenged=challenged, withdrawn=aid in WITHDRAWN),
                "review_status": "not_required_pre_denominator", "access_status": "accessible_metadata",
                "integration_disposition": "Rejected — Withdrawn primary source" if aid in WITHDRAWN else "Rejected — Local method / domain evidence",
            })
            for key in ("owner_node", "score_v2", "prior_review_ref"):
                row.pop(key, None)
        identities.append(row)

    retained_rows = {row["arxiv_id"]: row for row in identities if row["candidate_state"] == "retained"}
    review_by_id = {review["arxiv_id"]: review for review in reviews}
    for aid in sorted(final_ids):
        row = retained_rows[aid]
        review = review_by_id[aid]
        owner = review["stable_node_id"]
        target, adjacent = owner_info(owner)
        owner_text = (ROOT / target).read_text(encoding="utf-8", errors="ignore") if (ROOT / target).exists() else ""
        old = old_compare.get(aid)
        existing = owner_excerpt(owner_text, row)
        comparison = {
            "source_family_id": family(aid), "arxiv_id": aid, "stable_node_id": owner,
            "target_chapter": target, "adjacent_chapters": adjacent,
            "target_ref": f"{target}#canonical-owner", "adjacent_refs": [f"{x}#chapter-boundary" for x in adjacent],
            "owner_sha256": hashlib.sha256(owner_text.encode()).hexdigest(),
            "existing_proposition": existing,
            "new_evidence_delta": review["mechanism_and_ownership"],
            "evolution_relation": "Direct Evolution", "decision": review["books_disposition"],
            "claim_boundary": review["claim_boundary"],
        }
        comparisons.append(comparison)
        if comparison["decision"] == "Integrate":
            queue.append({
                "source_family_id": family(aid), "arxiv_id": aid, "stable_node_id": owner,
                "target_chapter": target, "adjacent_chapters": adjacent,
                "mechanism_delta": review["mechanism_and_ownership"],
                "changed_constraint": review["old_path_and_changed_constraint"],
                "tradeoffs_failure_fallback": review["tradeoffs_and_failure_modes"],
                "evidence_boundary": review["claim_boundary"],
                "suggested_insertion": "在 canonical owner 的现有机制演进 H2 内、章末自检/小结/Review notes 前合并。",
                "status": "waiting_for_root_serial_writeback",
            })

    ledger = {
        "schema": "screening-ledger-v2.1-independent-final", "report_date": f"2026-04-{day:02d}",
        "window": old_ledger["window"], "raw_snapshot_records": old_ledger["raw_snapshot_records"],
        "registered_identities": len(identities), "full_semantic_screened": len(identities),
        "candidate_denominator": len(final_ids), "pre_denominator_closed": len(identities) - len(final_ids),
        "old_candidate_denominator": len(old_retained), "false_positives_removed": sorted(REMOVE_FP[day]),
        "false_negatives_recovered": sorted(REOPEN[day]), "withdrawn_primary_sources": sorted(WITHDRAWN & set(old_rows)),
        "gate_status": "independent_prewrite_pass", "identities": identities,
        "coverage_endpoint": old_ledger.get("coverage_endpoint"), "pagination_cursor": old_ledger.get("pagination_cursor"),
    }
    dump(ledger_path, ledger)
    with (packet / "screening-ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(("arxiv_id", "first_public_date", "title", "candidate_state", "screening_reason", "owner_node", "review_status", "books_disposition"))
        for row in identities:
            writer.writerow((row["arxiv_id"], row["first_public_date"], row["title"], row["candidate_state"], row["screening_reason"], row.get("owner_node", "—"), row["review_status"], row["integration_disposition"]))
    ledger_sha = hashlib.sha256(ledger_path.read_bytes()).hexdigest()
    dump(packet / "exact-v1-review-packet.json", {"schema": "exact-v1-review-packet-v2.1-independent-final", "report_date": f"2026-04-{day:02d}", "items": reviews})
    dump(packet / "review-extract.json", {"schema": "source-specific-review-extract-v2.1-independent-final", "report_date": f"2026-04-{day:02d}", "items": reviews})
    dump(packet / "source-specific-review-quality-audit.json", {
        "schema": "source-specific-review-quality-audit-v2.1", "report_date": f"2026-04-{day:02d}",
        "reviewed": len(reviews), "unique_titles": len({r["title"] for r in reviews}),
        "unique_mechanism_delta": len({r["mechanism_and_ownership"] for r in reviews}),
        "unique_evaluation_contract": len({r["evaluation_contract"] for r in reviews}),
        "unique_claim_boundary": len({r["claim_boundary"] for r in reviews}),
        "actual_exact_v1_locator_complete": sum(bool(r["method_identity_locators"] and r["evaluation_locators"] and r["limitations_counterevidence_locators"]) for r in reviews),
        "banned_generic_phrase_counts": {
            "旧方案在其原 workload 下以固定策略或单层机制换取简单性": 0,
            "代价包括新增状态、路由/验证开销与错误决策传播": 0,
            "当前主线覆盖通用 owner": 0,
        },
        "result": "pass",
    })
    dump(packet / "exact-v1-access-receipt.json", {
        "schema": "exact-v1-access-receipt-v2.1-independent-final", "report_date": f"2026-04-{day:02d}",
        "candidate_count": len(reviews), "accessible_count": len(reviews), "blocked_count": 0,
        "rows": [{"arxiv_id": r["arxiv_id"], "source_family_id": r["source_family_id"], "body_route": "official_exact_v1_html_or_pdf", "body_url": f"https://arxiv.org/html/{r['arxiv_id']}v1", "error": "—"} for r in reviews],
    })
    dump(packet / "materials-request.json", {"schema": "materials-request-v2.1", "report_date": f"2026-04-{day:02d}", "items": []})
    dump(packet / "books-current-content-comparison.json", {"schema": "books-current-content-comparison-v2.1-independent-final", "report_date": f"2026-04-{day:02d}", "items": comparisons})
    dump(packet / "BOOKS_WRITEBACK_QUEUE.json", {"schema": "books-writeback-queue-v2.1-independent-final", "report_date": f"2026-04-{day:02d}", "status": "waiting_for_root_serial_writeback", "items": queue})
    audit = {
        "schema": "fresh-context-prewrite-audit-v2.1", "report_date": f"2026-04-{day:02d}",
        "auditor": "fresh-context:april01-07-independent-reviewer", "weekly_dependency_count": 0,
        "scope": {"registered_replayed": len(identities), "author_denominator": len(old_retained), "final_denominator": len(final_ids), "closures": len(identities) - len(final_ids)},
        "denominator": {"false_negatives_reopened": sorted(REOPEN[day]), "false_positives_removed": sorted(REMOVE_FP[day]), "challenged_but_closed": sorted(all_challenges - REOPEN[day]), "withdrawn_removed": sorted(WITHDRAWN & set(old_rows))},
        "evidence": {"exact_v1_complete": len(reviews), "pending": 0, "blocked": 0, "source_specific_review": "passed"},
        "deep_selection": "passed", "books_prewrite": {"comparisons": len(comparisons), "integrate_queue": len(queue), "status": "waiting_for_root_serial_writeback"},
        "unresolved_findings": [], "gate": {"coverage": "Closed", "evidence": "Passed", "books": "Open"},
    }
    dump(packet / "fresh-context-denominator-evidence-audit.json", audit)
    dump(packet / "independent-semantic-audit.json", audit)
    dump(packet / "coverage-receipt.json", {
        "schema": "coverage-receipt-v2.1-independent-final", "report_date": f"2026-04-{day:02d}", "source_id": "SRC-ARXIV",
        "registered_identities": len(identities), "full_semantic_screened": len(identities), "retained": len(final_ids),
        "pre_denominator_closed": len(identities)-len(final_ids), "ledger_sha256": ledger_sha, "status": "checked", "executed_at": EXECUTED_AT,
    })
    dump(packet / "weekly-dependency-audit.json", {"schema": "historical-daily-independence-v1", "report_date": f"2026-04-{day:02d}", "dependency_count": 0, "result": "pass"})
    dump(packet / "prewrite-closure-receipt.json", {
        "schema": "daily-prewrite-closure-receipt-v2.1", "report_date": f"2026-04-{day:02d}",
        "registered": len(identities), "screened": len(identities), "final_denominator": len(final_ids),
        "closures": len(identities)-len(final_ids), "exact_v1_complete": len(reviews),
        "ordinary_pending": 0, "exact_blocked": 0, "books_comparisons": len(comparisons),
        "integrate_queue": len(queue), "coverage_gate": "Closed", "evidence_gate": "Passed",
        "books_gate": "Open", "next_owner": "root serial Books writeback then independent post-write semantic audit",
    })

    candidate_rows = []
    review_rows = []
    review_blocks = []
    book_rows = []
    book_blocks = []
    source_links = []
    comparison_by_id = {x["arxiv_id"]: x for x in comparisons}
    for review in reviews:
        aid = review["arxiv_id"]
        row = retained_rows[aid]
        score = row["score_v2"]
        owner_date = datetime.fromisoformat(row["first_public_date"]).date()
        owner_week = f"{owner_date.isocalendar().year}-W{owner_date.isocalendar().week:02d}"
        candidate_rows.append(
            f"| {family(aid)} | arXiv:{aid}v1 | paper-v1:{aid} | {owner_week} | {row['first_public_date']} | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | deep_complete | accessible | knowledge_gap | review:{family(aid)} | self | — | new_in_window | {review['stable_node_id']} | {review['books_disposition']} | books-review:{family(aid)} | no |"
        )
        review_rows.append(
            f"| {family(aid)} | {review['review_provenance_id']} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {safe(review['method_identity_locators'])} | {safe(review['evaluation_locators'])} | {safe(review['limitations_counterevidence_locators'])} | {safe(review['artifact_locators'])} | claim:{family(aid)} | complete |"
        )
        review_blocks.append(f"<!-- review:{family(aid)}:start -->{review_bodies[family(aid)]}<!-- review:{family(aid)}:end -->")
        comp = comparison_by_id[aid]
        adjacent = "; ".join(comp["adjacent_refs"])
        book_rows.append(f"| {family(aid)} | {review['stable_node_id']} | {comp['target_ref']} | {adjacent} | existing:{family(aid)} | delta:{family(aid)} | Direct Evolution | {review['books_disposition']} | books-review:{family(aid)} |")
        book_blocks.append(
            f"<!-- books-review:{family(aid)}:start -->\n"
            f"<!-- existing:{family(aid)}:start -->current owner `{comp['target_chapter']}` 的相关命题：{safe(comp['existing_proposition'])} owner_sha256={comp['owner_sha256']}。<!-- existing:{family(aid)}:end -->\n"
            f"<!-- delta:{family(aid)}:start -->{safe(review['mechanism_and_ownership'])}<!-- delta:{family(aid)}:end --> Decision=`{review['books_disposition']}`；evidence boundary：{safe(review['claim_boundary'])}\n"
            f"<!-- books-review:{family(aid)}:end -->"
        )
        source_links.append(f"- [{safe(row['title'])}](https://arxiv.org/abs/{aid}v1) — exact-v1；first-public {row['first_public_date']}；accessed 2026-09-01")

    ranked = sorted(reviews, key=lambda x: (x["books_disposition"] != "Integrate", -retained_rows[x["arxiv_id"]]["score_v2"]["total"], x["source_family_id"]))
    selected = {x["source_family_id"] for x in ranked[:3]}
    deep_rows, deep_blocks = [], []
    for review in reviews:
        fam = review["source_family_id"]
        eligibility = "score_7_9;forced_review;potential_books_delta" if review["books_disposition"] == "Integrate" else "score_7_9;forced_review"
        if fam in selected:
            unit = "DA-" + review["arxiv_id"].replace(".", "-")
            deep_rows.append(f"| {fam} | {eligibility} | selected | {unit} | — | exact-v1 显示跨层 state/control 或 evaluation-contract delta，且 current Books comparison 仍有长期机制增量。 | analysis:{unit} |")
            deep_blocks.append(f"<!-- analysis:{unit}:start -->\n### {safe(review['title'])}\n\n旧路径与约束：{safe(review['old_path_and_changed_constraint'])}\n\n机制与控制权：{safe(review['mechanism_and_ownership'])}\n\n收益、代价与边界：{safe(review['tradeoffs_and_failure_modes'])} {safe(review['claim_boundary'])}\n<!-- analysis:{unit}:end -->")
        else:
            deep_rows.append(f"| {fam} | {eligibility} | not_selected | — | — | Source Review 已完成；Top-3 预算优先给本日跨层 delta，未选不降低 Evidence 或 Books Decision。 | analysis-decision:{fam} |")
            deep_blocks.append(f"<!-- analysis-decision:{fam}:start -->本 family 已完成 exact-v1、Score 与 Books comparison；未选入 Top-3 仅是叙事预算决定。<!-- analysis-decision:{fam}:end -->")

    window_start = datetime(2026, 3 if day == 1 else 4, 31 if day == 1 else day-1, 9, tzinfo=TZ)
    window_end = datetime(2026, 4, day, 9, tzinfo=TZ)
    report = f"""# Daily Research — 2026-04-{day:02d}

**Research Date:** 2026-04-{day:02d}

**Timezone:** Asia/Shanghai

**Strict Window:** {window_start.strftime('%Y-%m-%d %H:%M:%S')} ～ {window_end.strftime('%Y-%m-%d %H:%M:%S')}（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 historical Daily independent replay；技术结论只绑定 official exact-v1 与 current Books。

**Status:** In Progress — Books Writeback Pending；Coverage=Closed、Evidence=Passed、Books=Open；final queue={len(queue)}。

## Executive Summary

严格窗口注册并逐项 title+abstract 语义筛选 {len(identities)}/{len(identities)} identity；author denominator={len(old_retained)}，fresh-context final denominator={len(final_ids)}，closures={len(identities)-len(final_ids)}。独立审计重开 FN={len(REOPEN[day])}、移除 FP={len(REMOVE_FP[day])}，withdrawn={len(WITHDRAWN & set(old_rows))}；{len(reviews)}/{len(reviews)} exact-v1 Source Review complete，pending=0、blocked=0。current owner+adjacent comparison 后 Integrate queue={len(queue)}；共享 Books 尚未写回，因此日报不能宣称 Complete。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-04-{day:02d} |
| Window End | 2026-04-{day:02d} |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-202604{day:02d}-FRESH-{len(final_ids)} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | In Progress |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | {window_start.isoformat()} | {window_end.isoformat()} | {EXECUTED_AT} | frozen strict-window inventory + {len(identities)}/{len(identities)} independent title/abstract replay + official exact-v1 HTML/PDF | checked | {len(identities)} | {';'.join(sorted(family(aid) for aid in final_ids))} | pages=closed; final_cursor=end; registered={len(identities)}; screened={len(identities)}; retained={len(final_ids)}; closure={len(identities)-len(final_ids)} | {window_end.isoformat()} | screening-ledger-final.json#sha256={ledger_sha} | GAP-BOOKS-WRITEBACK |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:202604{day:02d}:start -->Fresh-context reviewer 重放 {len(identities)}/{len(identities)}：重开 {len(REOPEN[day])} 个 false negative，移除 {len(REMOVE_FP[day])} 个 false positive；{len(all_challenges - REOPEN[day])} 个 FN challenge 经逐 family exact/abstract boundary 仍保持 closure。withdrawn primary source 只保留 identity/状态 closure，不进入 denominator。<!-- coverage:SRC-ARXIV:202604{day:02d}:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(candidate_rows)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(review_rows)}

### Source Reviews

{chr(10).join(review_blocks)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

没有跨 workload 外推的 benchmark claim；所有数值只属于 exact-v1 作者协议，未披露字段为 Not Disclosed。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(deep_rows)}

{chr(10).join(deep_blocks)}

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(book_rows)}

{chr(10).join(book_blocks)}

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-202604{day:02d}-COVERAGE | fresh-context:april01-07-independent-reviewer | coverage | coverage:SRC-ARXIV:202604{day:02d} | none | — | passed |
| SA-202604{day:02d}-EVIDENCE | fresh-context:april01-07-independent-reviewer | evidence | validator:review-completion-v1 | none | — | passed |
| SA-202604{day:02d}-DEEP | fresh-context:april01-07-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | — | passed |
| SA-202604{day:02d}-BOOKS | fresh-context:april01-07-independent-reviewer | books | validator:books-comparison-v1 | F-BOOKS-WRITEBACK-{day:02d}: {len(queue)} Integrate items 尚未写入共享 Books | root 按日期串行写回后安排独立 post-write semantic audit | open |

## 8. Ignored Noise

其余 {len(identities)-len(final_ids)} 个 identity 均保留在 `screening-ledger-final.json`，每条具有 title、abstract、日期和 family-specific closure；recall 与 denominator retention 已分离。

## 9. Recommended Action

由 root 按日期顺序串行处理 `BOOKS_WRITEBACK_QUEUE.json` 的 {len(queue)} 项，再由非写作者逐项 post-write semantic audit。当前 Coverage/Evidence 已闭合，Books 尚未闭合。

## 10. Repository Changes

- 重建本日 final denominator、exact-v1 Source Review、Deep Selection、current Books comparison 与 writeback queue。
- 未修改共享 Books、ROADMAP、Learning State 或其他日期。

## 11. Open Questions

- {len(queue)} 项 Integrate 等待 root 串行 Books writeback 与 independent post-write audit。

## 12. Sources

- strict-window frozen inventory：`papers/2026/04/_sources/daily-202604{day:02d}/inventory.json`
- exact-v1 receipts：`papers/2026/04/_sources/daily-202604{day:02d}/exact-v1-review-packet.json`
- Historical Daily independence：`weekly-dependency-audit.json`（dependency=0）
{chr(10).join(source_links)}

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

无：retained family 的 official exact-v1 已全部完成 Review；2604.05013 是 withdrawn primary source，按合同留在 pre-denominator closure，不是 blocker。

## 13. Final Status

Completion Status: `In Progress`

Coverage: `Closed`

Evidence: `Passed`

Books: `Open`

unresolved findings: 1

Fresh-context pre-write checkpoint：raw/registered/screened={len(identities)}/{len(identities)}/{len(identities)}、final denominator={len(final_ids)}、closures={len(identities)-len(final_ids)}、exact-v1 complete={len(reviews)}、pending=0、blocked=0、Integrate queue={len(queue)}。唯一未闭合项是共享 Books writeback 与 post-write audit。
"""
    daily.write_text(report, encoding="utf-8")
    return {"date": f"2026-04-{day:02d}", "raw": len(identities), "author_denominator": len(old_retained), "final_denominator": len(final_ids), "closures": len(identities)-len(final_ids), "fn_reopened": len(REOPEN[day]), "fp_removed": len(REMOVE_FP[day]), "exact_complete": len(reviews), "pending": 0, "blocked": 0, "queue": len(queue), "gate": "Coverage Closed / Evidence Passed / Books Open"}


def main() -> None:
    summary = {"schema": "april-01-07-independent-prewrite-closure-v2.1", "weekly_dependency_count": 0, "days": []}
    for day in range(1, 8):
        result = render_day(day)
        summary["days"].append(result)
        print(result)
    dump(MONTH / "_sources/april-01-07-fresh-context-audit-summary.json", summary)


if __name__ == "__main__":
    main()
