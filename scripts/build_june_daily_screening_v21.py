#!/usr/bin/env python3
"""Build a deterministic arXiv identity-screening ledger for a June Daily.

This helper does not decide the Candidate Denominator, Evidence Gate, or Books
Gate. It converts frozen DataCite arXiv DOI snapshots into a complete
strict-window receipt, then marks which identities require human title/abstract
semantic screening. A positive route is a recall obligation, not admission to
the Candidate Denominator; `not_routed` is likewise an auditable pre-screening
decision, not a claim that the manuscript was read.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from pathlib import Path


CORE_DAILY_CATEGORIES = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
KEYWORD_DAILY_CATEGORIES = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}
REGISTERED_CATEGORIES = CORE_DAILY_CATEGORIES | KEYWORD_DAILY_CATEGORIES

# This is deliberately recall-oriented. Every routed identity still needs a
# family-specific pre-denominator decision. Only work that changes a durable AI
# System mechanism, state/data/control ownership, evaluation contract, platform
# or training/inference design judgment, or corrects existing Books knowledge
# may be retained and scored. Score V2 never performs candidate admission.
ROUTE_TERMS = {
    "accelerator", "activation steering", "agent", "agentic", "alignment",
    "allreduce", "attention", "autoregressive", "benchmark for evaluating llm",
    "benchmarking llm", "cache", "checkpoint", "collective", "compiler",
    "computer use", "computer-using", "context optimization", "context window",
    "data attribution", "data poisoning", "decode", "deep research",
    "diffusion language", "diffusion llm", "distributed training", "distillation",
    "edge inference", "evidence tracing", "execution provenance", "fine-tun",
    "finetun", "foundation model", "gpu", "gradient", "grpo", "guardrail",
    "hallucination", "in-context", "inference", "jailbreak", "judge", "kernel",
    "knowledge distillation", "language model", "llm", "long context",
    "long-context", "lora", "machine unlearning", "memory", "mcp", "mixture of experts",
    "mixture-of-experts", "mlops", "model compression", "model context protocol",
    "model deployment", "model editing", "model evaluation", "model merging",
    "model registry", "model safety", "moe", "multi-agent", "multi-modal",
    "multiagent", "multimodal", "npu", "observability", "on-device", "optimizer",
    "parallel decoding", "parameter-efficient", "peft", "pipeline parallel",
    "positional bias", "post-training", "preference optimization", "prefill",
    "privacy-preserving model", "process reward", "prompt ambiguity", "prompt injection",
    "quantization", "rag", "reasoning distillation", "reasoning trace", "red teaming",
    "retrieval-augmented", "reward hacking", "rlhf", "rlvr", "runtime", "safety evaluation",
    "scaling laws", "security", "serving", "silent delivery", "silent error", "sparse",
    "speculative", "synthetic data", "tensor parallel", "test-time compute",
    "test-time training", "token", "tool aware", "tool-aware", "training data",
    "training dynamics", "uncertainty in llm", "vision-language-action", "vla",
    "watermarking", "workflow", "world model",
}
ROUTE_RE = re.compile(
    "|".join(re.escape(term) for term in sorted(ROUTE_TERMS, key=len, reverse=True)),
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-date", required=True, help="YYYY-MM-DD in Asia/Shanghai")
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def submitted_v1(attributes: dict) -> str | None:
    for item in attributes.get("dates", []):
        if item.get("dateType") == "Submitted" and item.get("dateInformation") == "v1":
            return item.get("date")
    return None


def arxiv_categories(attributes: dict) -> list[str]:
    categories: list[str] = []
    for item in attributes.get("subjects", []):
        match = re.search(r"\(([^()]+)\)$", item.get("subject", ""))
        if match:
            categories.append(match.group(1))
    return sorted(set(categories))


def first_text(items: list[dict], key: str) -> str:
    return next((item.get(key, "") for item in items if item.get(key)), "")


def main() -> None:
    args = parse_args()
    report_day = datetime.fromisoformat(args.report_date).date()
    cst = timezone(timedelta(hours=8))
    window_end = datetime.combine(report_day, datetime.min.time(), cst) + timedelta(hours=9)
    window_start = window_end - timedelta(days=1)
    start_utc = window_start.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    end_utc = window_end.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")

    snapshot_paths = sorted((args.source_dir / "datacite").glob("*.json.gz"))
    if not snapshot_paths:
        raise SystemExit("no DataCite snapshots found")

    raw_records: list[dict] = []
    snapshots: list[dict] = []
    for path in snapshot_paths:
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            payload = json.load(handle)
        data = payload.get("data", [])
        expected = payload.get("meta", {}).get("total")
        if expected != len(data):
            raise SystemExit(f"incomplete snapshot {path}: {len(data)} != {expected}")
        raw_records.extend(data)
        snapshots.append({
            "path": str(path),
            "records": len(data),
            "sha256": sha256(path.read_bytes()).hexdigest(),
        })

    identities: dict[str, dict] = {}
    for record in raw_records:
        attributes = record.get("attributes", {})
        submitted = submitted_v1(attributes)
        if not submitted or not (start_utc <= submitted < end_utc):
            continue
        categories = arxiv_categories(attributes)
        if not REGISTERED_CATEGORIES.intersection(categories):
            continue
        doi = attributes.get("doi", "")
        identifier = doi.split("arxiv.", 1)[1] if "arxiv." in doi.lower() else ""
        title = first_text(attributes.get("titles", []), "title")
        abstract = first_text(
            [item for item in attributes.get("descriptions", []) if item.get("descriptionType") == "Abstract"],
            "description",
        )
        if not identifier or identifier in identities:
            raise SystemExit(f"missing or duplicate identity: {identifier}")
        core_daily = bool(CORE_DAILY_CATEGORIES.intersection(categories))
        keyword_match = bool(ROUTE_RE.search(title))
        routed = core_daily or keyword_match
        identities[identifier] = {
            "arxiv_id": identifier,
            "source_family_key": f"arxiv:{identifier}",
            "submitted_v1_utc": submitted,
            "title": title,
            "categories": categories,
            "abstract": abstract,
            "screening_route": (
                "core_daily_semantic_review_required"
                if core_daily
                else "keyword_daily_semantic_review_required"
                if keyword_match
                else "not_routed_by_keyword_contract"
            ),
            "screening_status": "pending_pre_denominator_semantic_screen",
            "screening_reason": (
                "Core Daily category hit; title/abstract semantic screening is mandatory, but the hit is not yet a candidate and receives Score V2 only after durable-system admission"
                if core_daily
                else "Daily keyword-filtered category matched the recall-oriented title route; semantic screening is mandatory, but the hit is not yet a candidate and receives Score V2 only after durable-system admission"
                if keyword_match
                else "Daily keyword-filtered category did not match the registered route; independent false-negative audit is still required before denominator freeze"
            ),
        }

    ordered = [identities[key] for key in sorted(identities, key=lambda value: int(value.split(".")[1]))]
    result = {
        "schema": "daily-v2.1-screening-ledger-v1",
        "report_date": args.report_date,
        "window": f"[{window_start.isoformat()},{window_end.isoformat()})",
        "utc_window": f"[{start_utc},{end_utc})",
        "registered_categories": sorted(REGISTERED_CATEGORIES),
        "snapshots": snapshots,
        "raw_snapshot_records": len(raw_records),
        "registered_window_identities": len(ordered),
        "core_daily_semantic_review_required": sum(
            row["screening_route"] == "core_daily_semantic_review_required" for row in ordered
        ),
        "keyword_daily_semantic_review_required": sum(
            row["screening_route"] == "keyword_daily_semantic_review_required" for row in ordered
        ),
        "semantic_review_required": sum(
            row["screening_route"].endswith("semantic_review_required") for row in ordered
        ),
        "title_route_negative_pending_false_negative_audit": sum(
            row["screening_route"] == "not_routed_by_keyword_contract" for row in ordered
        ),
        "gate_status": "open_pending_manual_screening_and_false_negative_audit",
        "identities": ordered,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "report_date", "registered_window_identities", "core_daily_semantic_review_required",
        "keyword_daily_semantic_review_required", "semantic_review_required",
        "title_route_negative_pending_false_negative_audit", "gate_status",
    )}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
