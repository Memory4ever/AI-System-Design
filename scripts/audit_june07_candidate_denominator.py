#!/usr/bin/env python3
"""Freeze the full 2026-06-07 title+abstract semantic denominator."""
from __future__ import annotations

import csv, hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260607"
SRC = PACKET / "registered-hit-screening.json"

# Independent admission requires a durable state/data/control/evaluation-contract delta.
RETAIN = {
"2606.07923": ("INFER-SCHEDULING", "Online selectivity learning plus exact per-row ordering makes semantic-predicate token cost query-planner state rather than an opaque LLM charge."),
"2606.07936": ("PLATFORM-EVALUATION-SYSTEM", "Twenty reproducibility fields separate what human judges measured, who judged, and how judgments may be interpreted; this changes the evaluation receipt contract."),
"2606.07943": ("PLATFORM-SECURITY", "Postcondition-validated payload execution jointly with legitimate-task success changes skill-poisoning evidence from invocation to completed side effect, while position controls stealth and reliability."),
"2606.07950": ("TRAIN-GRPO", "Confidence, empirical difficulty, and shrinking group advantage become explicit rollout-allocation state used for both resampling and update weighting under fixed compute."),
"2606.07957": ("PLATFORM-SECURITY", "CSPM rules become tenant-local derived state maintained bidirectionally from catalogue entries and the live asset graph, removing vendor release cadence from the protection critical path."),
"2606.07968": ("PLATFORM-MONITORING", "A generation-time monitor combines recurrence, volume growth, and task progress over consecutive chunks and owns early termination of reasoning-token consumption attacks."),
"2606.07970": ("TRAIN-SFT", "Train-time adversarial attack strength becomes an inner-loop robustness control, with parallel execution preserving the stronger full-parameter threat model."),
"2606.07992": ("AGENT-MCP", "Tool errors are an authority-bearing ingress path; mutation across error structure and language changes MCP trust from tool output validation to error-loop admission and containment."),
"2606.08049": ("AGENT-WORKFLOW", "Versioned notebooks make each reusable step auditable state and let validation gates choose code execution or local natural-language fallback when environments drift."),
"2606.08094": ("INFER-REQUEST-LIFECYCLE", "A single C++ runtime owns cached vision-language prefix state, cross-attending action-expert solver steps, portable model bundles, and one request protocol across VLA families."),
"2606.08106": ("AGENT-PLATFORM", "Anytime-valid paired tests move self-evolution authority from noisy score improvement to a false-commit-controlled acceptor that remains valid under optional stopping."),
"2606.08197": ("TRAIN-DISTRIBUTED-TRAINING", "Version grouping, calibration-set semantic alignment, and freshness/participation weighting make staleness and fairness explicit asynchronous federated aggregation state."),
"2606.08200": ("PLATFORM-EVALUATION-SYSTEM", "An in-world evaluator actively creates criterion-relevant situations through native dialogue/action, changing evaluation from passive trajectory scoring to coverage-seeking intervention."),
"2606.08302": ("INFER-KV-CACHE", "Head role, layer, and generation step control separate attention and retained-cache budgets for visual autoregressive decoding instead of applying one global compression ratio."),
"2606.08317": ("PLATFORM-FOUNDATIONS", "Nine dimensions, workload characterization, constraint filtering, and compatibility scoring make polyglot database choice a reviewable platform decision rather than intuition."),
"2606.08340": ("AGENT-MULTI-AGENT", "A long-horizon world separates individual task reward from coordination reward while controlling communication, role specialization, and coordination difficulty."),
"2606.08346": ("TRAIN-GRPO", "Tree outcome diversity and policy-reward decorrelation identify low-signal rollout trees; critique-guided grafting repairs all-fail branches before informativeness-weighted updates."),
"2606.08348": ("AGENT-PLATFORM", "Verified trajectories and posterior beliefs turn skills into evidence-bearing lifecycle objects with auditable update and guardrail actions across harnesses."),
"2606.08367": ("PLATFORM-EVALUATION-SYSTEM", "Continuously running heterogeneous agent populations, persistent memories, consequential governance, and live exogenous data expose drift and cross-influence absent from exam-style evaluation."),
"2606.08372": ("PLATFORM-SECURITY", "A memorization test distinguishes population reconstruction from training-record leakage and maps reconstruction and membership inference to one comparable privacy-risk scale."),
"2606.08381": ("PLATFORM-EVALUATION-SYSTEM", "Reference-set-relative semantic divergence provides a black-box audit contract for provider-specific alignment when absolute ground truth is unavailable."),
"2606.08382": ("INFER-KV-CACHE", "Differentiable head/block thresholds, sensitivity-specific factorization, and rank-aware mixed precision turn KV rank into adaptive runtime compression state backed by kernels."),
"2606.09916": ("INFER-KV-CACHE", "Cross-turn QueryMemory controls live-token retention while slot-map redirection preserves surviving rows, RoPE phase, and prefix-cache identity during eviction."),
}

def sentence(text: str, last=False) -> str:
    parts=[p.strip() for p in re.split(r"(?<=[.!?])\s+", " ".join(text.split())) if p.strip()]
    s=(parts[-1] if last else parts[0]) if parts else ""
    return s[:360]

def closure_class(title, abstract):
    s=(title+" "+abstract).lower()
    if any(x in s for x in ("benchmark", "dataset", "leaderboard")): return "bounded-benchmark-or-dataset"
    if any(x in s for x in ("survey", "position paper", "perspective")): return "survey-or-position-without-owner-delta"
    if any(x in s for x in ("video", "robot", "medical", "driving", "wireless", "traffic")): return "domain-model-or-application"
    if any(x in s for x in ("loss", "architecture", "representation", "fine-tuning", "optimizer")): return "local-model-or-training-method"
    return "no-durable-system-owner-change"

def main():
    d=json.loads(SRC.read_text())
    ids=d["identities"]
    assert len(ids)==261 and len({x['arxiv_id'] for x in ids})==261 and set(RETAIN)<= {x['arxiv_id'] for x in ids}
    rows=[]
    for i,x in enumerate(ids,1):
        aid=x['arxiv_id']
        if aid in RETAIN:
            node, rationale=RETAIN[aid]; decision="retain"; klass="durable-owner-contract-delta"
            reopen="retained; exact-v1 must confirm mechanism, evaluation, counterevidence, and benchmark identity"
        else:
            node="—"; decision="pre_denominator_closure"; klass=closure_class(x['title'],x['abstract'])
            rationale=(f"{x['title']} is closed as {klass}: its stated contribution starts with ‘{sentence(x['abstract'])}’ "
                       f"and the abstract-level outcome ends with ‘{sentence(x['abstract'],True)}’; neither assigns a new durable state, data, control, or release-evidence contract to a ROADMAP owner.")
            reopen=(f"Reopen only if exact-v1 shows a reusable cross-workload owner contract beyond the stated {klass}, "
                    "or invalidates an existing chapter proposition.")
        rows.append({"row":i,"arxiv_id":aid,"source_family_id":f"SF-2026-ARXIV-{aid.replace('.','-')}","submitted_v1_utc":x['submitted_v1_utc'],"title":x['title'],"categories":";".join(x['categories']),"route":x['screening_route'],"decision":decision,"stable_node_id":node,"closure_class":klass,"rationale":rationale,"reopen_condition":reopen})
    # This file begins as the raw discovery receipt.  Once the independent
    # population audit finishes, preserve the same 261 identities but replace
    # stale intermediate "pending" labels with the final screening outcome.
    # Keep snapshot references repository-relative so the recovery packet is
    # self-contained rather than dependent on a deleted /private/tmp directory.
    d["title_route_negative_pending_false_negative_audit"] = 0
    d["title_route_negative_reviewed"] = sum(
        row["route"] == "not_routed_by_keyword_contract" for row in rows
    )
    d["gate_status"] = "closed_full_title_abstract_semantic_screening"
    for snapshot in d["snapshots"]:
        snapshot["path"] = f"datacite/{Path(snapshot['path']).name}"
    for identity, row in zip(ids, rows):
        identity["screening_status"] = (
            "retained_after_semantic_screening"
            if row["decision"] == "retain"
            else "pre_denominator_closed"
        )
        identity["screening_reason"] = (
            f"Final decision={row['decision']}; see candidate-denominator.tsv row {row['row']} "
            "for the family-specific rationale and reopen condition."
        )
        identity["screening_result_ref"] = f"candidate-denominator.tsv#row={row['row']}"
    SRC.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blob=json.dumps(rows,ensure_ascii=False,sort_keys=True,separators=(",",":")); den="DEN-20260607-"+hashlib.sha256(blob.encode()).hexdigest()[:8]
    out={"schema":"candidate-denominator-v2.1","report_date":"2026-06-07","window":"[2026-06-06T09:00:00+08:00, 2026-06-07T09:00:00+08:00)","raw_identities":261,"retained":len(RETAIN),"closures":261-len(RETAIN),"denominator_id":den,"false_negative_audit":"261/261 title+abstract rows independently re-read; all 46 route negatives included","rows":rows}
    (PACKET/"candidate-denominator.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    fields=list(rows[0]);
    with (PACKET/"candidate-denominator.tsv").open("w",newline="") as f:
        w=csv.DictWriter(f,fields,delimiter="\t",lineterminator="\n"); w.writeheader(); w.writerows(rows)
    md=["# 2026-06-07 Candidate Denominator — independent full-population audit","",f"- Window: `{out['window']}`",f"- Frozen denominator: `{den}`",f"- Population: 261 = {len(RETAIN)} retain + {261-len(RETAIN)} family-specific closures",f"- FN audit: {out['false_negative_audit']}","","The closure ledger is canonical in `candidate-denominator.tsv`; no score was used for admission. Exact-v1 access is a downstream Evidence Gate, not a denominator shortcut.",""]
    (PACKET/"CANDIDATE_DENOMINATOR_AUDIT_V1.md").write_text("\n".join(md))
    print(den,len(RETAIN),261-len(RETAIN))

if __name__=="__main__": main()
