#!/usr/bin/env python3
"""Build honest fresh-context review frontiers for June/July 2026.

The output is a routing queue, never a semantic acceptance result.  It makes
obvious false-negative pressure visible without promoting a title-pattern hit
into the Candidate denominator or demoting a completed Source Review.
"""

from __future__ import annotations

import gzip
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent

ROUTES = {
    "inference_state_runtime": re.compile(
        r"kv cache|paged attention|speculative decod|prefill[- /]decode|continuous batch|"
        r"llm inference (?:serving|runtime|engine|schedul)|llm serving|inference[- ]time control|"
        r"activation spars|weight dequant|sparse (?:weight|matrix)|long[- ]context inference|"
        r"edge (?:llm|vlm) inference|token (?:compression|selection)",
        re.I,
    ),
    "distributed_execution": re.compile(
        r"distributed (?:llm )?(?:training|inference)|tensor parallel|pipeline parallel|"
        r"expert parallel|zero[- ](?:redundancy|stage)|all[- ]reduce|nccl",
        re.I,
    ),
    "agent_state_action": re.compile(
        r"agent (?:memory|workflow|orchestrat|protocol|platform|runtime|security)|"
        r"multi[- ]agent (?:system|coordination|communication)|tool[- ](?:calling|use)|"
        r"mcp (?:server|protocol)|prompt injection|memory poisoning|agentic (?:workflow|system|testing|fuzzing)|"
        r"agent (?:planning|evaluation|benchmark|harness|context|skill)|coding agent|persistent memory",
        re.I,
    ),
    "world_model_embodied": re.compile(
        r"world model|vision[- ]language[- ]action|\bvla\b|sim[- ]to[- ]real|"
        r"embodied (?:agent|ai)|action[- ]conditioned|robot (?:policy|control|planning)|"
        r"perception[- ]action|video[- ]to[- ]robot|latent action|simulator|scene state",
        re.I,
    ),
    "compiler_kernel_precision_moe": re.compile(
        r"gpu (?:kernel|memory|cluster|schedul)|kernel generation|compiler[- ]driven|"
        r"llm quantiz|low[- ]bit (?:llm|language model)|moe (?:serving|routing|training)|"
        r"expert routing|sparse tensor core|fused attention|memory[- ]efficient inference|"
        r"hardware[- ]software co[- ]design|npu|hbm",
        re.I,
    ),
    "training_control": re.compile(
        r"checkpoint (?:system|storage|recovery)|training data (?:curation|dedup)|"
        r"post[- ]training (?:system|pipeline)|rlhf|\bdpo\b|\bgrpo\b|"
        r"reward model (?:runtime|serving|training)|preference optimization|distributed .*post[- ]training|"
        r"asynchronous .*training|training objective|policy optimization|safe reinforcement learning|"
        r"learning rate adaptation|initialization for language model pretraining",
        re.I,
    ),
    "evaluation_governance": re.compile(
        r"evaluation (?:framework|protocol|contract|system)|benchmark contamination|"
        r"release gate|observability|telemetry|model registry|artifact provenance|"
        r"evaluation (?:target|metric|harness)|benchmark(?:ing)? .*agent|confidence calibrat|"
        r"risk classification|auditable|verification|failure trajector|security evaluation",
        re.I,
    ),
}

TITLE_DEPRIORITIZE = re.compile(
    r"\bsurvey\b|position paper|tutorial|systematic review|literature review",
    re.I,
)


def load_packet(month: str, packet: Path) -> tuple[dict, dict]:
    with gzip.open(packet / "canonical-raw-identity-inventory-v2.1.json.gz", "rt", encoding="utf-8") as handle:
        raw = json.load(handle)
    with gzip.open(packet / "canonical-semantic-screening-checkpoint-v2.1.json.gz", "rt", encoding="utf-8") as handle:
        screen = json.load(handle)
    raw_by_id = {item["arxiv_id"]: item for item in raw["identities"]}
    return raw_by_id, screen


def main() -> None:
    false_negative = []
    retained = []
    per_day: dict[str, Counter] = defaultdict(Counter)

    for month in ("06", "07"):
        base = ROOT / f"papers/2026/{month}/_sources"
        for packet in sorted(base.glob("daily-2026????")):
            raw_by_id, screen = load_packet(month, packet)
            report_date = screen["report_date"]
            for item in screen["items"]:
                raw = raw_by_id[item["arxiv_id"]]
                title = raw["title"]
                # Denominator screening is explicitly title+abstract semantic
                # screening.  The old title-only frontier missed papers whose
                # durable system delta was stated only in the abstract (for
                # example, harness control, sparse GPU execution, persistent
                # agent state, or asynchronous post-training ownership).
                semantic_text = f"{title}\n{raw['abstract']}"
                routes = [name for name, pattern in ROUTES.items() if pattern.search(semantic_text)]
                record = {
                    "report_date": report_date,
                    "arxiv_id": item["arxiv_id"],
                    "source_family_id": item["source_family_id"],
                    "title": title,
                    "abstract": raw["abstract"],
                    "categories": raw["categories"],
                    "title_abstract_sha256": raw["title_abstract_sha256"],
                }
                if item["semantic_screen_status"].startswith("retained"):
                    retained.append({
                        **record,
                        "prior_candidate": item.get("prior_candidate"),
                        "audit_status": "fresh_context_false_positive_audit_pending",
                    })
                    per_day[report_date]["retained_pending"] += 1
                elif routes:
                    false_negative.append({
                        **record,
                        "risk_routes": routes,
                        "prior_closure_kind": item["semantic_decision_kind"],
                        "prior_closure_reason": item["semantic_screen_reason"],
                        "priority": "secondary" if TITLE_DEPRIORITIZE.search(title) else "primary",
                        "audit_status": "fresh_context_false_negative_audit_pending",
                    })
                    per_day[report_date]["false_negative_frontier"] += 1

    payload = {
        "schema": "fresh-context-semantic-frontiers-v1",
        "status": "review_pending",
        "boundary": (
            "Title+abstract patterns route an adversarial audit; they neither retain nor close a Source Family. "
            "Every routed item requires title+abstract semantic judgment, and every retained item requires "
            "false-positive review before a Daily can close."
        ),
        "retained_false_positive_audit_pending": len(retained),
        "closure_false_negative_frontier_pending": len(false_negative),
        "false_negative_route_counts": dict(Counter(
            route for item in false_negative for route in item["risk_routes"]
        )),
        "per_report": {day: dict(counts) for day, counts in sorted(per_day.items())},
        "retained_items": retained,
        "false_negative_frontier": false_negative,
    }
    path = OUT / "fresh-context-semantic-frontiers-v1.json.gz"
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    (OUT / "fresh-context-semantic-frontiers-summary.json").write_text(
        json.dumps({key: value for key, value in payload.items() if key not in {"retained_items", "false_negative_frontier"}}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
