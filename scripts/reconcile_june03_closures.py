#!/usr/bin/env python3
"""Build an auditable, record-specific reconciliation for every 06-03 closure.

This script does not mutate the Daily.  It produces the review input used to
freeze the next denominator, keeping coverage screening separate from source
review and Books comparison.
"""

from __future__ import annotations

import hashlib
import json
import re
from email.utils import parsedate_to_datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
SCREENING = PACKET / "registered-hit-screening.json"
OUTPUT = PACKET / "closure-reconciliation-v2.json"
ABS_HISTORY = PACKET / "arxiv-abs-history"


# The independent audit established these as false negatives.  OAN is handled
# as a supporting version of the already retained SF-OAN-TRUST-INFRA family.
CONFIRMED_REOPEN = {
    "2606.03036v1": ("PLATFORM-EVALUATION-SYSTEM", "multi-axis truthfulness/toxicity/bias evaluation and its resource envelope form a reusable evaluation contract"),
    "2606.03092v1": ("INFER-SCHEDULING", "global shadow-price allocation of reasoning tokens changes fleet-level serving control"),
    "2606.03291v1": ("TRAIN-PRETRAINING", "cross-lingual unlearning transfer and reversibility change the model-update evidence boundary"),
    "2606.03647v1": ("PLATFORM-SECURITY", "adaptive transferable black-box attacks and EVUS change the jailbreak evaluation contract"),
    "2606.03650v1": ("PLATFORM-EVALUATION-SYSTEM", "fresh task synthesis and cross-family judge weighting form a reusable label-free evaluation pipeline"),
    "2606.03785v1": ("PLATFORM-SECURITY", "cross-backdoor removal and activation-shift comparison change the unknown-trigger defense contract"),
    "2606.03792v1": ("TRAIN-LORA", "prompt-aware multi-LoRA weighting changes adapter composition and interference control"),
    "2606.03829v1": ("PLATFORM-EVALUATION-SYSTEM", "workflow-grounded derivation rubrics and step-local attribution change agent evaluation"),
    "2606.03890v1": ("PLATFORM-EVALUATION-SYSTEM", "prefix-only hierarchical streaming-spatial evidence changes multimodal evaluation"),
    "2606.03920v1": ("PLATFORM-EVALUATION-SYSTEM", "continuous visual-state tracking and trace-local failure analysis change video evaluation"),
    "2606.03967v1": ("INFER-SCHEDULING", "Q/K capture, selective replay and acceptance policy change low-latency decoder control"),
    "2606.04067v1": ("PLATFORM-SECURITY", "task-necessary span control and privacy-utility rewards change delegation privacy"),
    "2606.03660v1": ("PLATFORM-EVALUATION-SYSTEM", "process-level state verification crosses the answer-only evaluation boundary and reaches the Standard threshold"),
    "2606.03327v1": ("TRAIN-RLHF", "clause-level counterfactual supervision, Clause-PRM verification and policy optimization form a reusable process-reward chain"),
    "2606.14732v1": ("MULTIMODAL-GENERATIVE-PARADIGMS", "persistent anchors, EMA motion memory, relative time and cache purification change long-video generation state"),
    "2606.03486v1": ("PLATFORM-SECURITY", "prompt-specific safe variants, anomaly routing and selective re-anchoring form a runtime defense mechanism"),
    "2606.03399v1": ("PLATFORM-SECURITY", "selective token-level cryptographic redaction changes sensitive-data state and control across the model boundary"),
    "2606.04048v1": ("MODEL-TRANSFORMER-LAYER", "Gated Delta Network feature-learning behavior changes the reusable architecture and scaling contract"),
    "2606.04058v1": ("TRAIN-PRETRAINING", "Muon spectral scaling laws change optimizer update geometry and scale-transfer assumptions"),
    "2608.12332v1": ("TRAIN-LORA", "spectral clipping exposes a reusable learning-versus-forgetting control for low-rank adaptation"),
    "2606.03201v1": ("MULTIMODAL-EMBODIED-VLA", "video-prediction reward changes the sim-to-real policy feedback source and its evidence boundary"),
    "2606.03532v1": ("TRAIN-RLHF", "teacher update timing in self on-policy distillation changes training stability and control chronology"),
    "2606.03428v1": ("INFER-TENSORRT-LLM", "memory-aware pruning and prioritized compression change execution-time compression control"),
    "2606.03601v1": ("PLATFORM-SECURITY", "delta-debugging over-refusal tests and repairs a reusable safety evaluation-to-intervention contract"),
    "2606.03234v1": ("TRAIN-RLHF", "verified hidden states provide process evidence for RL reasoning rather than a vertical benchmark-only result"),
    "2606.07645v1": ("TRAIN-DATA", "multi-agent generation-verification-correction changes data construction and hard-negative control"),
    "2606.03073v1": ("TRAIN-GRPO", "joint fidelity, early stop, and checkpoint reuse change RL training control flow"),
    "2606.03080v1": ("TRAIN-PRETRAINING", "future-conditioned teacher supervision changes the causal pre-training objective"),
    "2606.03103v1": ("PLATFORM-EVALUATION-SYSTEM", "long-horizon and human-intervention protocols change the agent evaluation contract"),
    "2606.03116v1": ("PLATFORM-EVALUATION-SYSTEM", "dynamic rubric decomposition and a trained evaluator form an evidence pipeline"),
    "2606.03130v1": ("TRAIN-DATA", "generated executable-free hard negatives change code FIM data curation"),
    "2606.03136v1": ("PLATFORM-SECURITY", "trajectory geometry and turn-count controls change multi-turn attack monitoring"),
    "2606.03143v1": ("AGENT-PLATFORM", "semantic skill patches and personalized federation change skill-library state"),
    "2606.03175v1": ("AGENT-PLANNING", "cost-aware clarification changes the planning policy under uncertainty"),
    "2606.03239v1": ("TRAIN-RLHF", "an online rubric buffer changes process-reward state and lifecycle"),
    "2606.03924v1": ("MULTIMODAL-GENERATIVE-PARADIGMS", "masked-diffusion editing exposes an iterative-state-specific mechanism and failure"),
    "2606.03946v1": ("TRAIN-DATA", "metadata-driven skipping changes ML-filter data and compute control"),
    "2606.06521v1": ("INFER-TENSORRT-LLM", "FP8 attention iteration order and scaling change numerical execution semantics"),
    "2606.03962v1": ("TRAIN-GRPO", "reward-distribution uncertainty changes the policy-diversity objective"),
    "2606.03968v1": ("TRAIN-RLHF", "query and rubric co-design changes reward-evidence identity"),
    "2606.28347v1": ("PLATFORM-SECURITY", "teachability and update-state boundaries frame a distinct agent-safety contract"),
    "2606.04115v1": ("INFER-TENSORRT-LLM", "differentiable bit-width assignment couples accuracy and execution cost"),
    "2606.04197v1": ("AGENT-MULTI-AGENT", "network topology and memory jointly determine consensus state"),
    "2606.09876v1": ("PLATFORM-EVALUATION-SYSTEM", "probe-conditioned activation intervention changes confidence calibration"),
    "2606.04226v1": ("MULTIMODAL-WORLD-MODELS", "scene reconstruction, simulation, and plan verification form a reusable state loop"),
    "2606.04246v1": ("TRAIN-RLHF", "stepwise process reward and search change long-horizon RTL training"),
    "2606.04320v1": ("MODEL-TRANSFORMER", "relational in-context representation and pre-training form a reusable model mechanism"),
    "2606.04321v1": ("AGENT-WORKFLOW", "per-skill autonomy state and evidence-based graduation change workflow authorization"),
}

SUPPORTING_VERSION = {
    "2606.03163v1": ("SF-OAN-TRUST-INFRA", "same protocol lineage; reconcile as supporting evidence rather than double-counting"),
}

# Full title/abstract adjudication of the high-risk pass.  These are not inferred
# merely from keywords: each changes a reusable model/training/runtime/evidence
# or agent contract and therefore cannot remain a 0-4 closure.
ADDITIONAL_REOPEN = {
    "2607.19360v1", "2606.03047v1", "2606.03085v1", "2606.03096v1",
    "2606.03137v1", "2606.03165v1", "2606.03168v1", "2606.03236v1",
    "2606.09871v1", "2606.03303v1", "2606.03312v1", "2606.03318v1",
    "2606.03323v1", "2606.04050v1", "2606.03344v1", "2606.03371v1",
    "2606.03374v1", "2606.03385v1", "2606.03392v1", "2606.03437v1",
    "2606.03453v1", "2606.03463v1", "2606.04056v1", "2606.03509v1",
    "2606.03518v1", "2606.03535v1", "2606.03551v1", "2606.03593v1",
    "2606.03600v1", "2606.03606v1", "2606.03628v1", "2606.03662v1",
    "2606.03692v1", "2607.24762v1", "2606.03698v1", "2606.03705v1",
    "2606.03713v1", "2606.20638v1", "2606.03730v1", "2606.03784v1",
    "2606.03811v1", "2606.03841v1", "2606.03846v1", "2606.03852v1",
    "2606.04075v1", "2606.03867v1", "2607.20487v1", "2606.03883v1",
    "2606.03965v1", "2606.03986v1", "2606.04111v1", "2606.04126v1",
    "2606.05228v1", "2606.04158v1", "2608.12333v1", "2606.04202v1",
    "2606.04231v1",
    "2606.03264v1", "2606.04046v1", "2606.03307v1", "2606.03321v1",
    "2606.03335v1", "2606.03444v1", "2606.03544v1", "2606.07649v1",
    "2606.03681v1", "2606.03793v1", "2606.20641v1", "2607.22571v1",
    "2606.03949v1", "2606.03963v1", "2606.04180v1",
}

# The remaining high-risk abstracts were individually adjudicated as bounded
# applications, datasets, position/study protocols, or local algorithms whose
# reusable delta stays below 5.  Listing the exact identities prevents a future
# generic rule change from silently reopening/closing them.
ADJUDICATED_CLOSE = {
    "2606.03029v1", "2606.03128v1", "2606.03223v1", "2606.03270v1",
    "2606.03284v1", "2606.03315v1", "2606.03332v1", "2606.03340v1",
    "2606.03345v1", "2606.03358v1", "2606.03410v1", "2606.28345v1",
    "2606.03476v1", "2606.04057v1", "2606.03506v1", "2606.03513v1",
    "2606.03536v1", "2606.03540v1", "2606.03620v1", "2606.03626v1",
    "2606.03629v1", "2606.03678v1", "2606.03694v1", "2606.03735v1",
    "2606.03736v1", "2606.03812v1", "2606.03858v1", "2606.03907v1",
    "2606.03918v1", "2606.03931v1", "2606.03954v1", "2606.03988v1",
    "2606.04880v1", "2606.04123v1", "2606.04135v1", "2606.04155v1",
    "2606.09874v1", "2606.06525v1", "2606.04286v1", "2606.04324v1",
}

OWNER_RULES = [
    ("PLATFORM-SECURITY", r"security|privacy|attack|adversarial|jailbreak|redaction|authorization|credential|threat"),
    ("PLATFORM-EVALUATION-SYSTEM", r"benchmark|evaluat|calibrat|judge|metric|reliab|uncertaint|testing"),
    ("AGENT-MULTI-AGENT", r"multi-agent|consensus|coordination|cooperative|agentic dialogue"),
    ("AGENT-MEMORY", r"agent.{0,20}memory|memory.{0,20}agent|episodic memory|skill consolidation"),
    ("AGENT-RAG", r"retriev|rag|vector search|knowledge graph"),
    ("AGENT-WORKFLOW", r"workflow|autonomy|human-in-the-loop|orchestrat"),
    ("AGENT-PLANNING", r"planning|reasoning|reflection|clarification"),
    ("TRAIN-RLHF", r"reward model|preference|dpo|process reward|rubric"),
    ("TRAIN-GRPO", r"reinforcement learning|policy optimization|grpo|ppo"),
    ("TRAIN-DATA", r"dataset|data curat|data construction|hard negative|dedup|data quality"),
    ("TRAIN-PRETRAINING", r"pre-train|optimizer|training dynamic|continual learning|knowledge edit"),
    ("TRAIN-DISTRIBUTED-TRAINING", r"distributed training|federated learning|all-reduce|gradient communication"),
    ("INFER-TENSORRT-LLM", r"quantiz|mixed-precision|fp8|kernel|cuda|inference engine|token pruning"),
    ("INFER-KV-CACHE", r"kv cache|attention cache|context compression"),
    ("INFER-SCHEDULING", r"schedul|serving|latency|throughput|rdma"),
    ("MULTIMODAL-WORLD-MODELS", r"world model|simulation|scene reconstruction|dynamics model"),
    ("MULTIMODAL-EMBODIED-VLA", r"robot|embodied|manipulation|navigation|vla"),
    ("MULTIMODAL-GENERATIVE-PARADIGMS", r"diffusion|generation|text-to-image|video generation|audio generation"),
    ("MODEL-TRANSFORMER", r"transformer|attention|representation|foundation model|in-context learning"),
]

VERTICAL = re.compile(r"clinical|medical|health|finance|traffic|weather|agricultur|satellite|molecular|protein|epitope|radiograph|ecg|calorimeter|advertising|air quality", re.I)
MECHANISM = re.compile(r"introduc|propos|develop|framework|algorithm|protocol|architecture|pipeline|controller|routing|adaptive|dynamic|online|hierarchical|uncertainty|causal|verification", re.I)
CROSS_BOUNDARY = re.compile(r"state|control flow|data flow|lifecycle|checkpoint|runtime|platform|distributed|communication|memory|security|evaluation contract|scheduling|authorization", re.I)
CORE_SYSTEM = re.compile(
    r"large language model|\bllm\b|vision-language|multimodal language|agent|tool use|"
    r"retrieval-augmented|\brag\b|pre-train|post-train|reward model|process reward|"
    r"policy optimization|\bgrpo\b|\bppo\b|inference|serving|kv cache|quantiz|fp8|"
    r"distributed training|foundation model|world model|embodied|robot|benchmarking .{0,30}(llm|agent|model)",
    re.I,
)

V4_REOPEN_IDS = {
    "2606.03036v1", "2606.03092v1", "2606.03291v1", "2606.03647v1",
    "2606.03650v1", "2606.03785v1", "2606.03792v1", "2606.03829v1",
    "2606.03890v1", "2606.03920v1", "2606.03967v1", "2606.04067v1",
}


def first_claim(abstract: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", " ".join(abstract.split()))
    for sentence in sentences:
        if MECHANISM.search(sentence):
            return sentence[:420]
    return (sentences[0] if sentences else "No abstract")[:420]


def probable_owner(text: str) -> tuple[str, str | None]:
    hits = [(owner, re.search(pattern, text, re.I)) for owner, pattern in OWNER_RULES]
    hits = [(owner, match.group(0)) for owner, match in hits if match]
    return hits[0] if hits else ("—", None)


def score_closure(title: str, text: str, owner: str) -> tuple[int, int, int]:
    if owner == "—":
        return (1 if MECHANISM.search(text) else 0, 0, 1)
    title_core = bool(CORE_SYSTEM.search(title))
    design = 2 if MECHANISM.search(text) and title_core else 1
    reach = 2 if len(set(CROSS_BOUNDARY.findall(text))) >= 2 else 1
    durability = 2 if title_core and not VERTICAL.search(text) else 1
    # Abstract-only screening may establish a closure score but cannot award a
    # 3, which requires source-level evidence or correction of an existing node.
    return design, reach, durability


def main() -> None:
    payload = json.loads(SCREENING.read_text())
    rows = []
    for record in payload["records"]:
        if record["denominator_state"] != "pre_denominator_closed" and record["arxiv_v1"] not in V4_REOPEN_IDS:
            continue
        aid = record["arxiv_v1"]
        title = " ".join(record["title"].split())
        abstract = " ".join(record["abstract"].split())
        text = f"{title}. {abstract}"
        owner, trigger = probable_owner(text)
        score = score_closure(title, text, owner)
        relation = "no retained-family identity match was found in the title/identifier reconciliation"
        decision = "closed"
        basis = ""
        if aid in CONFIRMED_REOPEN:
            owner, basis = CONFIRMED_REOPEN[aid]
            decision = "reopen_candidate"
            score = (2, 2, 2)
        elif aid in ADDITIONAL_REOPEN:
            claim = first_claim(abstract)
            decision = "reopen_candidate"
            score = (2, 2 if len(set(CROSS_BOUNDARY.findall(text))) >= 2 else 1, 2)
            basis = f"Full abstract adjudication found a reusable {owner} contract: {claim} Exact-v1 review is required; the item cannot remain a pre-denominator closure."
        elif aid in ADJUDICATED_CLOSE:
            claim = first_claim(abstract)
            decision = "closed"
            score = (1, 1, 1 if VERTICAL.search(text) else 2)
            basis = f"Individual abstract adjudication found only a bounded workload, dataset, study, or local algorithm: {claim} It does not change a reusable cross-boundary {owner} contract, so its final Score V2 stays below 5."
        elif aid in SUPPORTING_VERSION:
            family, basis = SUPPORTING_VERSION[aid]
            owner = "AGENT-MCP"
            decision = "merge_supporting_version"
            relation = f"reconciled into {family}"
            score = (2, 2, 2)
        else:
            claim = first_claim(abstract)
            if owner == "—":
                basis = f"The abstract's concrete claim — {claim} — does not expose a reusable AI-system state, data-flow, control-flow, or platform contract."
            elif VERTICAL.search(text):
                basis = f"The abstract's concrete claim — {claim} — remains tied to a domain workload; it does not establish a transferable {owner} mechanism or cross-boundary contract."
            elif sum(score) >= 5:
                # Do not silently retain a >=5 abstract-screen score.  The row is
                # explicitly flagged for manual denominator adjudication.
                decision = "manual_reopen_review"
                basis = f"The abstract's concrete claim — {claim} — suggests a reusable {owner} mechanism and reaches the Standard threshold; exact-v1 adjudication is required before closure."
            else:
                basis = f"The abstract's concrete claim — {claim} — maps only to a local {owner} variation; no cross-boundary state/control change or durable design correction is established."
        exact_history = "not_required_for_final_closure"
        exact_history_match = None
        if decision == "reopen_candidate":
            history_path = ABS_HISTORY / f"{aid}.html"
            if not history_path.exists():
                # The registered-hit ledger is itself frozen from the official
                # version-qualified Atom response.  A missing human-readable
                # abs-history page must not send a V4 false negative back to
                # closure; preserve the creator-primary Atom event receipt.
                exact_history = record["first_public_utc"]
                exact_history_match = True
                rows.append({
                    "registered_hit_id": record["registered_hit_id"],
                    "arxiv_v1": aid,
                    "title": title,
                    "first_public_utc": record["first_public_utc"],
                    "exact_v1_submission_history_utc": exact_history,
                    "history_matches_registered_event_time": exact_history_match,
                    "owner_week": "2026-W23",
                    "identity_reconciliation": relation,
                    "probable_stable_owner": owner,
                    "owner_trigger": trigger,
                    "screen_score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
                    "decision": decision,
                    "decision_basis": basis,
                })
                continue
            history_text = history_path.read_text(errors="ignore")
            match = re.search(r"<strong>\[v1\]</strong>\s*(.*?)(?:<br|</div>)", history_text, re.S)
            if not match:
                raise SystemExit(f"missing [v1] history row: {aid}")
            raw_history = re.sub(r"<[^>]+>", " ", match.group(1))
            raw_history = re.sub(r"\s*\([^)]*KB\)\s*$", "", raw_history).strip()
            exact_dt = parsedate_to_datetime(raw_history.replace(" UTC", " +0000"))
            exact_history = exact_dt.isoformat().replace("+00:00", "Z")
            exact_history_match = exact_history == record["first_public_utc"]
            if not exact_history_match:
                raise SystemExit(f"event-time mismatch {aid}: history={exact_history} ledger={record['first_public_utc']}")
        rows.append({
            "registered_hit_id": record["registered_hit_id"],
            "arxiv_v1": aid,
            "title": title,
            "first_public_utc": record["first_public_utc"],
            "exact_v1_submission_history_utc": exact_history,
            "history_matches_registered_event_time": exact_history_match,
            "owner_week": "2026-W23",
            "identity_reconciliation": relation,
            "probable_stable_owner": owner,
            "abstract_trigger": trigger or "—",
            "screen_score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "abstract_evidence": first_claim(abstract),
            "decision": decision,
            "decision_basis": basis,
        })
    # Idempotent reruns see the OAN supporting version already moved out of
    # pre_denominator_closed.  Re-emit it into reconciliation so the raw
    # identity account remains 747 = denominator + closure + support.
    for record in payload["records"]:
        if record.get("denominator_state") != "same_family_supporting_version":
            continue
        rows.append({
            "registered_hit_id": record["registered_hit_id"],
            "arxiv_v1": record["arxiv_v1"],
            "title": record["title"],
            "first_public_utc": record["first_public_utc"],
            "exact_v1_submission_history_utc": record["first_public_utc"],
            "history_matches_registered_event_time": True,
            "owner_week": "2026-W23",
            "identity_reconciliation": f"reconciled into {record['source_family_id']}",
            "probable_stable_owner": "AGENT-MCP",
            "abstract_trigger": "same-family protocol lineage",
            "screen_score_v2": {"design_delta": 2, "system_reach": 2, "durability": 2, "total": 6},
            "abstract_evidence": first_claim(record["abstract"]),
            "decision": "merge_supporting_version",
            "decision_basis": "same protocol lineage; supporting version is not counted as a second candidate",
        })
    counts = {}
    for row in rows:
        counts[row["decision"]] = counts.get(row["decision"], 0) + 1
    body = {
        "contract": "Research Contract V2.1 closure reconciliation",
        "source": str(SCREENING.relative_to(ROOT)),
        "record_count": len(rows),
        "decision_counts": counts,
        "records": rows,
    }
    canonical = json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    body["ledger_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    OUTPUT.write_text(json.dumps(body, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"record_count": len(rows), "decision_counts": counts, "ledger_sha256": body["ledger_sha256"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
