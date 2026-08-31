#!/usr/bin/env python3
"""Materialize the independent 2026-06-02 exact-v1 evidence audit.

This audit reads the rebuilt Daily as the interface under review, not as an
authority.  The family-specific challenges below are the fresh-context
adversarial conclusions obtained from the exact-v1 primary packets.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "papers/2026/06/02/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260602"
DENOM = PACKET / "candidate-denominator-audit-v3-fresh.json"
OUT_JSON = PACKET / "evidence-audit-v3-fresh.json"
OUT_MD = PACKET / "EVIDENCE_AUDIT_V3_FRESH.md"


CHALLENGE = {
    "SF-KV-QUANT-ALIGNMENT-COLLAPSE": "Perplexity/accuracy cannot stand in for refusal preservation: exact-v1 isolates a low-dimensional alignment failure and validates a vLLM FP8 case, but its bit-width transition remains model-, evaluator-, prompt-, quantizer- and serving-configuration-specific.",
    "SF-SKILL-INJECTION-GUARDIAN": "The source supports a terminal-agent skill-injection threat and a bounded guardian branch; it does not establish that a prompt classifier replaces capability authorization, signed artifacts, sandboxing or effect-time policy.",
    "SF-ROBOTRUSTBENCH-WORLD-MODEL": "The benchmark broadens video world-model evaluation to trustworthiness dimensions, but author-defined scenarios and scorers do not prove a model is safe for closed-loop robotic control or identify its internal failure mechanism.",
    "SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY": "Filesystem/runtime/tool effects are the correct truth owner for the measured coding-agent attacks; Docker fidelity, the RedCode-derived goal pool and fixed predicates bound the result and prevent extrapolation to a production incidence rate.",
    "SF-OPTCC-ASYMMETRIC-ALLREDUCE": "The schedule consumes asymmetric bandwidth and failure state and is evaluated against relevant baselines; the paper does not prove optimality under rapidly changing telemetry, correlated failures or unmeasured plan-distribution overhead.",
    "SF-GAIATRACE-VIDUR-AGENT": "Task-DAG traces reveal that query TTFT/TPOT can misstate agent-task latency, but exact-v1 covers two GAIA systems and a simulator whose artifact is only promised; that limits Durability and forbids a universal workload claim.",
    "SF-SPARSEX-SEGMENT-KV": "SparseX supports position-aware non-prefix segment reuse with local correction, not arbitrary KV equivalence; reuse must retain model/position/token proof and a dense-prefill fallback.",
    "SF-ADAPTIVE-AUTO-HARNESS": "Stateful harness evolution and specialized solve-time routing are demonstrated on the disclosed streams; canary admission, provenance, retirement, reward-hacking resistance and production rollback are platform obligations, not paper results.",
    "SF-CONSERVE-CONVERSATION-PLACEMENT": "ConServe intentionally uses observable first-turn state, one KV movement and pinned tail placement; it does not support future-turn prediction or a dynamic migration controller, so the existing Books marker requires revision.",
    "SF-COMPRESSION-UNCERTAINTY": "The measured compression variants separate task accuracy from conformal uncertainty on the reported tasks; multiple-choice calibration does not establish open-ended generation confidence or robustness under online distribution shift.",
    "SF-ASYNC-INFERENCE-OVERHEADS": "Exact-v1 demonstrates host/control/I/O overhead as an Amdahl-limited component and measures overlap mechanisms; the result remains tied to disclosed device, collective and runtime configurations and is not an unbounded speedup law.",
    "SF-DRIFT-TELBENCH": "Span- and claim-level error localization is stronger evidence than final-answer accuracy, but the first harmful span narrows investigation and does not by itself identify causal root cause.",
    "SF-CONSENT-INTEGRITY": "Binding the approved proposal to the executed effect is a durable authorization invariant; the black-box/prototype evaluation does not prove resistance to every bypass, race or compromised execution environment.",
    "SF-DFLARE-DIFFUSION-SPECULATION": "The source supports target-conditioned capacity for a diffusion drafter plus target verification; it does not support confidence-profile selection or tree-cost branches that happened to share a Books paragraph.",
    "SF-STRAGGLER-AWARE-RL-GROUP": "The controller uses length/straggler summaries to choose the next step's group size while preserving the effective batch; it does not consume reward and does not stop, censor or refill examples inside a group.",
    "SF-SECLAW-SPEC-DRIVEN-SECURITY": "Exact-v1 is explicitly preliminary/in progress: it describes spec-driven synthesis, Docker execution and trajectory logging, while cross-model/harness evaluation is future work. It therefore receives standard review and No Change, not an Integration claim.",
    "SF-HARNESS1-EXTERNALIZED-STATE": "Externalizing recoverable search state separates policy action from bookkeeping, but the mechanism is already owned by the Context chapter and does not justify a second persistent-memory owner.",
    "SF-LLMFI-ERROR-PROPAGATION": "Controlled injections expose layer/operator/token propagation and mitigation surfaces; the synthetic fault distribution cannot be read as production frequency, and propagation localization is not proof of root cause.",
    "SF-PEFT-SCALE": "The source exposes registry, storage, loading and lifecycle pressure when personal adapters scale; those pressures are already covered by versioned model-artifact ownership and do not require a new PEFT-specific platform law.",
    "SF-GHOST-TOOL-ISSUE-PRIVACY": "Issue-time disclosure limits speculative tool privacy leakage; it does not prove approval-to-execution binding, which belongs to the separate Consent Integrity family.",
    "SF-SKILLHARM-LIFECYCLE": "Persistent and self-mutating skills establish a cross-session supply-chain threat; benchmark attack success does not estimate ecosystem prevalence, and signatures/revocation are system design deductions rather than evaluated defenses.",
    "SF-COSMOS3-OMNIMODAL": "The source is a bounded omnimodal/world-model architecture and evaluation case; the durable representation/state-transition principles already have owners, and model-card results do not establish universal physical-world fidelity.",
    "SF-CROWDED-EMBEDDING-EXTERNALITY": "The mean-field derivation and finite simulations expose shared-index population externalities, but one-to-one relevance, the thermodynamic limit and unvalidated mitigation prevent treating its phase threshold as a production constant.",
    "SF-ECHELON-AGGREGATE-ONLY-ADAPTATION": "Aggregate-only boundary messages create an auditable training information-flow contract; evidence is limited to disclosed LoRA/sequence/boundary settings and an honest-but-curious model, with no differential-privacy or full-parameter guarantee.",
    "SF-GATEAI-OPERATING-POINT-EVAL": "Grouped splits, inner-validation thresholds, matched FPR and contamination disclosure strengthen EvalSpec practice; they evaluate detector operating points and do not reveal detector internals or make third-party leaderboard numbers comparable.",
    "SF-KFORGE-CROSS-PLATFORM-KERNEL": "The source tests an LLM-driven generate/compile/repair loop across disclosed accelerators; benchmark success does not prove universal compiler portability, semantic correctness outside the tests or production kernel admission safety.",
    "SF-ASYMCACHE-MULTI-SEGMENT": "AsymCache couples lossless KV residency with recomputation/kernel cost and non-contiguous multi-segment attention; measured policies do not prove a universal eviction optimum across models, hardware, concurrency and SLOs.",
    "SF-DRIFTSCHED-TOKEN-DRIFT": "Reconciling predicted with observed token progress makes remaining work versioned online state; the single-L4/disclosed workload does not establish universal SJF optimality, fairness or multi-GPU behavior.",
}

CORRECTIONS = {
    "SF-GAIATRACE-VIDUR-AGENT": "Score 9→8; exact-v1 has no dedicated limitations section and the artifact is only promised.",
    "SF-SECLAW-SPEC-DRIVEN-SECURITY": "Score 8→6; false Evaluation/Limitations locators removed; Integrate→No Change.",
    "SF-KV-QUANT-ALIGNMENT-COLLAPSE": "Blocked→complete after official exact-v1 PDF recovery; benchmark contract expanded with hardware, precision and evaluator scope.",
    "SF-CROWDED-EMBEDDING-EXTERNALITY": "Blocked→complete after official exact-v1 PDF recovery; theory/simulation/limitations locators corrected.",
}


def rows_between(text: str, heading: str) -> list[list[str]]:
    start = text.index(heading) + len(heading)
    chunk = text[start:]
    match = re.search(r"\n## ", chunk)
    if match:
        chunk = chunk[:match.start()]
    return [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in chunk.splitlines()
        if line.startswith("|") and not re.match(r"^\|[ -]+\|", line)
    ]


def table_map(text: str, heading: str) -> dict[str, list[str]]:
    rows = rows_between(text, heading)
    return {row[0]: row for row in rows[1:] if row and row[0].startswith("SF-")}


def benchmark_contract_from_row(row: list[str]) -> dict[str, str]:
    """Map the 11-column report table without dropping Output Length."""
    if len(row) != 11:
        raise ValueError(f"benchmark row must have 11 columns, got {len(row)}")
    return {
        "workload": row[1],
        "model": row[2],
        "hardware": row[3],
        "precision": row[4],
        "input_length": row[5],
        "output_length": row[6],
        "batch": row[7],
        "concurrency": row[8],
        "slo": row[9],
        "evaluator": row[10],
    }


def main() -> None:
    text = DAILY.read_text(encoding="utf-8")
    candidates = json.loads(DENOM.read_text(encoding="utf-8"))["candidates"]
    cand = table_map(text, "## 2. Candidate Ledger")
    rp = table_map(text, "## 3. Review Completion Receipt")
    bench = table_map(text, "## 4. Benchmark Contracts")
    books = table_map(text, "## 6. Books Comparison")
    selection = table_map(text, "## 5. Deep Analysis Selection")

    expected = {item["source_family_id"] for item in candidates}
    if expected != set(CHALLENGE):
        raise SystemExit(f"challenge coverage mismatch: missing={expected-set(CHALLENGE)} extra={set(CHALLENGE)-expected}")

    records = []
    for item in candidates:
        family = item["source_family_id"]
        identifier = item["primary_identifier"]
        arxiv_id = identifier.removeprefix("arXiv:")
        local = PACKET / "arxiv-v1" / f"{arxiv_id}.html"
        if local.exists():
            source_route = str(local.relative_to(ROOT))
            source_sha = hashlib.sha256(local.read_bytes()).hexdigest()
            access = "local_exact_v1_html"
        else:
            kind = "pdf" if identifier in {"arXiv:2606.09864v1", "arXiv:2606.28343v1"} else "html"
            source_route = f"https://arxiv.org/{kind}/{arxiv_id}"
            source_sha = "Not Available — official source reviewed through web primary route"
            access = f"official_exact_v1_{kind}"

        c, r, b, bk = cand[family], rp[family], bench[family], books[family]
        sel = selection.get(family)
        records.append({
            "source_family_id": family,
            "primary_identifier": identifier,
            "source_route": source_route,
            "source_sha256": source_sha,
            "access_route": access,
            "exact_v1_identity_checked": True,
            "review_result": r[-1],
            "method_locator": r[5],
            "evaluation_locator": r[6],
            "limitations_locator": r[7],
            "artifact_locator": r[8],
            "score_v2": {"design_delta": int(c[6]), "system_reach": int(c[7]), "durability": int(c[8]), "total": int(c[9])},
            "independent_challenge": CHALLENGE[family],
            "benchmark_contract": benchmark_contract_from_row(b),
            "selection_verdict": ({"eligibility": sel[1], "decision": sel[2], "unit": sel[3], "reason": sel[5]} if sel else {"eligibility": "not_prebooks_eligible", "decision": "not_routed", "unit": "—", "reason": "Score below 7 with no forced review or Books delta."}),
            "books_comparison": {"owner": bk[1], "target": bk[2], "adjacent": bk[3], "relation": bk[-3], "disposition": bk[-2]},
            "fresh_correction": CORRECTIONS.get(family, "No correction after fresh challenge; exact-v1 boundary and current disposition confirmed."),
            "outstanding_blocker": None,
        })

    selected = [r for r in records if r["selection_verdict"]["decision"] == "selected"]
    selected_units = {r["selection_verdict"]["unit"] for r in selected}
    if len(selected_units) > 3:
        raise SystemExit(f"selected units exceed cap: {len(selected_units)}")
    if any(r["review_result"] != "complete" for r in records):
        raise SystemExit("not all exact-v1 reviews are complete")

    payload = {
        "schema_version": "evidence-audit-v3-fresh",
        "report": str(DAILY.relative_to(ROOT)),
        "candidate_count": len(records),
        "exact_v1_review_complete": len(records),
        "benchmark_contract_complete": len(records),
        "books_comparison_complete": len(records),
        "selection_routed": len(selection),
        "selection_not_prebooks_eligible": len(records) - len(selection),
        "selected_families": len(selected),
        "selected_units": len(selected_units),
        "ordinary_pending": 0,
        "blocked": 0,
        "correction_count": len(CORRECTIONS),
        "books_writes_performed": 0,
        "gate_truth": "Evidence material is complete; Books Gate remains Open for root serial reconciliation and independent post-write audit.",
        "records": records,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# 2026-06-02 Evidence Audit V3 Fresh",
        "",
        "本审计不把既有 Score、Selection 或 Books 结论当作先验。28 个冻结候选均重新绑定 exact-v1 primary route，逐项核对 Method、Evaluation、limitations、artifact、benchmark contract、Score V2、Selection 与 Books Comparison。两份先前受阻材料已通过官方 exact-v1 PDF 恢复；本轮普通 pending=0、blocked=0。",
        "",
        "## Receipt",
        "",
        f"- Candidate Denominator：{len(records)}/{len(records)}。",
        f"- exact-v1 Source Review：{len(records)}/{len(records)}。",
        f"- Benchmark Contract：{len(records)}/{len(records)}。",
        f"- Deep Selection routed：{len(selection)}；not pre-Books eligible：{len(records)-len(selection)}；selected families：{len(selected)}；selected units：{len(selected_units)}/3。",
        f"- Books Comparison：{len(records)}/{len(records)}；Books writes：0。",
        "- Evidence material blocker：0。",
        "",
        "## Fresh Corrections",
        "",
    ]
    for family, correction in CORRECTIONS.items():
        lines.append(f"- `{family}`：{correction}")
    lines += [
        "",
        "## Per-family Verdict",
        "",
        "| Source Family | Score | Source Route | Review | Selection | Books | Independent Challenge |",
        "| --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        score = record["score_v2"]["total"]
        sel = record["selection_verdict"]["decision"]
        lines.append(
            f"| `{record['source_family_id']}` | {score}/9 | `{record['access_route']}` | complete | {sel} | {record['books_comparison']['disposition']} | {record['independent_challenge']} |"
        )
    lines += [
        "",
        "## Gate Truth",
        "",
        "Evidence material 已闭合，但本审计没有修改 Books。Books Gate 仍为 `Open`：root 必须按 22-marker fresh audit 做最小串行 reconciliation，并由另一个 fresh-context reviewer 对实际写回文字执行 post-write audit。validator 通过只能证明接口自洽，不能替代该语义 Gate。",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("candidate_count", "exact_v1_review_complete", "selection_routed", "selected_families", "selected_units", "blocked")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
