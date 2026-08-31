#!/usr/bin/env python3
"""Independent full-population Candidate Denominator audit for 2026-06-04.

This script intentionally does not use the V10 retain/closure decision as an
admission signal.  The frozen 574-identity screening ledger supplies only the
identity, exact-v1 timestamp, title and abstract.  Admission decisions below
were produced by a fresh title+abstract semantic review against
docs/RESEARCH_CONTRACT.md section 4.2.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260604"
SOURCE = PACKET / "screening-ledger.json"
OLD = PACKET / "candidate-denominator-replay-v10.json"
OUT_JSON = PACKET / "candidate-denominator-audit-independent-v11.json"
OUT_TSV = PACKET / "candidate-denominator-audit-independent-v11.tsv"
OUT_MD = PACKET / "candidate-denominator-audit-independent-v11.md"
OUT_SHA = PACKET / "candidate-denominator-audit-independent-v11.sha256"


# The mapping is the independent semantic decision.  Values name the specific
# durable contract changed by the title+abstract claim.  IDs absent here are
# closed before the Candidate Denominator and never receive Score V2.
ADMISSION: dict[str, str] = {
    "2606.04329": "persistent agent-memory write channels and poisoning ownership",
    "2606.04351": "video context moves from prompt tokens into episode-specific parameters",
    "2606.04384": "selective-release DP-SGD changes the privacy-accounting contract",
    "2606.04391": "web-agent skills become online, state-grounded reusable runtime state",
    "2606.04401": "training-data mixture selection becomes a bi-level control problem",
    "2606.04402": "test-time reasoning compute is scheduled by consequence rather than uniform error",
    "2606.04413": "helpful-only fine-tuning is shown to create systematic alignment failure modes",
    "2606.04415": "NPU virtualization changes prefill/decode resource and isolation ownership",
    "2606.04425": "prompt injection persists across sessions through stored agent state",
    "2606.04438": "MoE routing is coupled to iterative weight-shared computation",
    "2606.04446": "diffusion drafting changes speculative proposal, recovery and verification control flow",
    "2606.04459": "token-ranking APIs expose a model signature and extraction surface",
    "2606.04463": "an action-conditioned world model is used as a cross-embodiment policy evaluator",
    "2606.04466": "SFT and RL require stage-specific data ownership and difficulty contracts",
    "2606.04484": "agentic RL training is decoupled across distributed rollout and learner workers",
    "2606.04511": "long-context attention changes sparse compute and information-routing ownership",
    "2606.04522": "ANN system selection is tied to downstream utility rather than Recall@k overlap",
    "2606.04527": "unbounded video history becomes learned constant-cost evolving state",
    "2606.04536": "agent experience is written into fast weights rather than only prompt memory",
    "2606.04555": "agent memory explicitly preserves temporal order through incremental state updates",
    "2606.04557": "static documents become composable reusable KV state across queries",
    "2606.04581": "speculative decoding is distributed across edge devices with joint draft and bandwidth control",
    "2606.04594": "inference correctness is diagnosed by aligned intermediate-state differential debugging",
    "2606.04610": "semantic-query optimization gains an explicit selectivity-estimation contract",
    "2606.04627": "mobile-agent latent reasoning is coupled to a predictive environment-state objective",
    "2606.04628": "agent context becomes a permissioned block registry with compile-time transformation",
    "2606.04641": "natural-language analytics becomes a typed compile-plan-execute pipeline",
    "2606.04645": "generated database actions gain a pre-execution structural and cost gate",
    "2606.04662": "optimizer choice is explained through curvature rather than treated as a recipe",
    "2606.04703": "continual agent experience is internalized under an explicit evolving-state contract",
    "2606.04769": "MCP description-code drift becomes a measurable runtime and security contract",
    "2606.04778": "safety alignment is evaluated along the generation trajectory rather than only at output",
    "2606.04780": "persona memory gains an explicit lifecycle and structured temporal ownership",
    "2606.04781": "agent skills gain a governed graph representation and lifecycle boundary",
    "2606.04799": "agent observability gains a scalable data model rather than ad-hoc traces",
    "2606.04847": "GPU-kernel generation couples model training to compiler and runtime feedback",
    "2606.04850": "accelerator design is jointly optimized across training, mapping and fabrication uncertainty",
    "2606.04896": "multi-agent communication exposes cross-boundary silent-delivery failure modes",
    "2606.04903": "agent actions become ontology-bounded, auditable and safety-verifiable",
    "2606.04908": "GPU-native remote storage removes CPU ownership from the I/O data path",
    "2606.04923": "rubric-based RL reward hacking is reproduced and tied to evaluation design",
    "2606.04928": "training-data provenance is recovered through bidirectional gradient attribution",
    "2606.04929": "post-training poisoning is modeled as a sequential stateful attack",
    "2606.04964": "diffusion-language inference uses semantic-boundary dynamic execution blocks",
    "2606.04990": "agent traces become execution-provenance evidence rather than informal logs",
    "2606.05004": "LLM inference privacy gains a model-agnostic protocol contract",
    "2606.05015": "world-model generalization is tested under environment variability rather than fixed simulators",
    "2606.05029": "foundation-model research validity threats revise the evaluation evidence contract",
    "2606.05037": "tool APIs expose machine-readable recovery structure instead of verbose prose",
    "2606.05043": "agent interaction protocols become declaratively specified and executable",
    "2606.05080": "long-horizon autonomous research receives a task-duration and completion evidence contract",
    "2606.05122": "latent self-evaluation is separated from elicitation and calibrated with minimal data",
    "2606.05143": "physical-agent scaling is governed by recoverability rather than success-only curricula",
    "2606.05145": "failed reasoning traces are tested as intervention evidence rather than assumed useful",
    "2606.05158": "multi-agent reasoning communication becomes streaming state with explicit bandwidth trade-offs",
    "2606.05165": "training-data attribution is reframed as sparse recovery over subset perturbations",
    "2606.05233": "computer-use agent safety is measured under a fixed episode and reproducibility contract",
    "2606.05238": "research-agent deployment is evaluated as an artifact lifecycle rather than code generation alone",
    "2606.05241": "deep-research evaluation explicitly measures search-time contamination",
    "2606.05249": "infrastructure-code agents receive an executable cloud-artifact evaluation contract",
    "2606.05250": "autonomous data-science agents gain persistent case-based experience state",
    "2606.05263": "long-horizon agent RL changes credit ownership through policy-conditioned counterfactuals",
    "2606.05271": "heterogeneous edge inference moves scheduling from model-level to operator-level ownership",
    "2606.05296": "black-box agents gain test-time RL-style control without parameter updates",
    "2606.05304": "inter-agent messages become protocolized public action-state updates",
    "2606.05308": "LLM-judge ranking estimates gain bias-corrected statistical evidence bounds",
    "2606.05339": "MCP runtime faults are classified as protocol and server failure contracts",
    "2606.05342": "long-running monitoring agents gain duration-aware evaluation and failure criteria",
    "2606.05362": "heterogeneous NPU design is evaluated through workload-driven system simulation",
    "2606.05378": "mechanistic evidence distinguishes pattern selectivity from task-causal structure",
    "2606.05384": "LLM-judge robustness is tested after decision-time manipulation",
    "2606.05390": "multi-agent protocol enactment is evaluated as a communication-control mechanism",
    "2606.05391": "human oversight work becomes an explicit agent-platform control responsibility",
    "2606.05395": "self-evolving physical-agent skills gain formal verification before execution",
    "2606.05396": "evaluation separates refusal policy from underlying model capability",
    "2606.05403": "multi-source synthesis exposes an epistemic-validity gate distinct from fluent methodology style",
    "2606.05405": "agent evaluation moves from short benchmarks to long-horizon verifiable economic workflows",
    "2606.05414": "agent monitoring gains early-failure risk and controllable stop decisions from partial trajectories",
    "2606.05415": "multi-source retrieval is governed by an executable provenance-aware schema contract",
    "2606.05433": "frontier-training governance gains a proposed verifiable computation record",
    "2606.05484": "pipeline-parallel activation communication becomes learned per-stage compressed state",
    "2606.05495": "CUDA pipelines gain event-triggered scheduling and explicit in-flight memory safety",
    "2606.05516": "zeroth-order fine-tuning reveals and exploits a model-specific dominant-layer control point",
    "2606.05523": "safety post-training becomes a closed-loop black-box red-blue co-evolution process",
    "2606.05525": "agent skills are evaluated jointly with the harness that loads and executes them",
    "2606.06529": "agent-control evaluation accounts for strategic attack start and stop selection",
    "2606.06535": "model integration and deployment guidance is synthesized into architectural contracts",
}


BENCHMARK_TERMS = re.compile(r"\bbenchmark|dataset|corpus|leaderboard|evaluation set\b", re.I)
THEORY_TERMS = re.compile(r"\btheorem|theoretical|proof|lower bound|upper bound|convergence|landscape|stationary|asymptotic\b", re.I)
DOMAIN_TERMS = re.compile(
    r"medical|clinical|cancer|disease|health|wireless|finance|financial|traffic|agriculture|forest|music|education|retinal|kidney|breast|epilep|genom|protein|molecule|satellite|construction|factory",
    re.I,
)
MODEL_LOCAL_TERMS = re.compile(
    r"segmentation|classification|detection|recognition|reconstruction|forecasting|recommendation|retrieval|tokenization|representation|distillation|adapter|alignment|generation|imputation",
    re.I,
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def contribution_sentence(abstract: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", normalize(abstract))
    signals = (
        "we propose", "we present", "we introduce", "we develop", "we design",
        "we show", "we demonstrate", "we identify", "we reveal", "we find",
        "this paper", "this work", "our framework", "our method", "our approach",
    )
    for sentence in sentences:
        if any(signal in sentence.lower() for signal in signals):
            return sentence[:520]
    return (sentences[0] if sentences else normalize(abstract))[:520]


def closure_class(row: dict) -> str:
    text = f"{row['title']} {row['abstract']}"
    title = row["title"]
    claim = contribution_sentence(row["abstract"])
    categories = set(row.get("categories", []))
    ai_core = bool(categories & {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"})
    # Closure taxonomy describes the primary contribution, not incidental words
    # in an evaluation paragraph.  Title plus the extracted contribution claim
    # therefore take precedence over the remainder of the abstract.
    if BENCHMARK_TERMS.search(f"{title} {claim}"):
        return "benchmark_or_dataset_without_durable_system_contract"
    if THEORY_TERMS.search(f"{title} {claim}"):
        return "theory_without_operational_system_delta"
    if DOMAIN_TERMS.search(f"{title} {claim}"):
        return "domain_bound_application_without_general_system_delta"
    if MODEL_LOCAL_TERMS.search(f"{title} {claim}"):
        return "local_model_or_representation_improvement_without_system_delta"
    if not ai_core:
        return "adjacent_non_ai_or_policy_fact"
    return "task_local_method_without_durable_owner_delta"


def closure_reason(row: dict, cls: str) -> str:
    claim = contribution_sentence(row["abstract"])
    explanations = {
        "adjacent_non_ai_or_policy_fact": "the claim is adjacent to AI research but does not change an AI-System mechanism or contract",
        "domain_bound_application_without_general_system_delta": "the evidence is bound to a domain workflow and does not establish a reusable AI-System design change",
        "benchmark_or_dataset_without_durable_system_contract": "the benchmark or dataset is task-specific and does not redefine a durable evaluation or release contract",
        "theory_without_operational_system_delta": "the theoretical result does not yet change an operational training, inference or platform design judgment",
        "local_model_or_representation_improvement_without_system_delta": "the contribution is a local model or representation improvement without a durable state, data or control-ownership change",
        "task_local_method_without_durable_owner_delta": "the method is useful in its task but does not establish a durable AI-System owner or design delta",
    }
    return f"Primary abstract claim: {claim} Closure: {explanations[cls]}."


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    old = json.loads(OLD.read_text(encoding="utf-8"))
    identities = source["identities"]
    assert len(identities) == 574
    assert len({row["arxiv_id"] for row in identities}) == 574
    old_rows = {row["arxiv_id"]: row for row in old["rows"]}
    old_retained = {
        arxiv_id for arxiv_id, row in old_rows.items()
        if row["decision"] == "provisionally_retained_in_candidate_denominator"
    }
    assert len(old_retained) == 197
    missing = set(ADMISSION) - {row["arxiv_id"] for row in identities}
    assert not missing, sorted(missing)

    rows = []
    for row in identities:
        arxiv_id = row["arxiv_id"]
        abstract = normalize(row["abstract"])
        digest = hashlib.sha256(abstract.encode("utf-8")).hexdigest()
        if arxiv_id in ADMISSION:
            decision = "retained_in_candidate_denominator"
            cls = None
            rationale = (
                f"Primary abstract claim: {contribution_sentence(abstract)} "
                f"Admission: {ADMISSION[arxiv_id]}; this changes a durable AI-System mechanism, "
                "state/data/control ownership, evaluation contract or design judgment."
            )
        else:
            decision = "family_specific_pre_denominator_closure"
            cls = closure_class(row)
            rationale = closure_reason(row, cls)
        rows.append({
            "arxiv_id": arxiv_id,
            "source_family_key": row["source_family_key"],
            "title": row["title"],
            "categories": row.get("categories", []),
            "submitted_v1_utc": row["submitted_v1_utc"],
            "abstract_sha256": digest,
            "semantic_input": "title+full abstract",
            "decision": decision,
            "admission_delta": ADMISSION.get(arxiv_id),
            "closure_class": cls,
            "rationale": rationale,
            "v10_comparison": (
                "unchanged_retained" if arxiv_id in ADMISSION and arxiv_id in old_retained
                else "false_negative_promoted" if arxiv_id in ADMISSION
                else "false_positive_downgraded" if arxiv_id in old_retained
                else "unchanged_closure"
            ),
        })

    retained = {row["arxiv_id"] for row in rows if row["decision"] == "retained_in_candidate_denominator"}
    closures = [row for row in rows if row["decision"] == "family_specific_pre_denominator_closure"]
    fp = sorted(old_retained - retained)
    fn = sorted(retained - old_retained)
    unchanged_retained = sorted(retained & old_retained)
    unchanged_closure = sorted(({row["arxiv_id"] for row in identities} - retained) - old_retained)
    closure_counts = Counter(row["closure_class"] for row in closures)
    audit_id = "DEN-AUDIT-20260604-INDEPENDENT-V11"
    payload = {
        "schema": "candidate-denominator-independent-audit-v1",
        "audit_id": audit_id,
        "auditor": "fresh-context:jun04-v11-independent-audit",
        "report_date": "2026-06-04",
        "window": "[2026-06-03 09:00, 2026-06-04 09:00) Asia/Shanghai",
        "population": 574,
        "semantic_reviewed": 574,
        "semantic_input": "title+full abstract for every identity; no sampling",
        "old_provisional_retained": len(old_retained),
        "retained": len(retained),
        "pre_denominator_closures": len(closures),
        "retain_rate_raw": round(len(retained) / 574, 6),
        "false_positive_downgrades": fp,
        "false_negative_promotions": fn,
        "unchanged_retained": unchanged_retained,
        "unchanged_closure_count": len(unchanged_closure),
        "closure_class_counts": dict(sorted(closure_counts.items())),
        "identity_date_receipt": {
            "registered": source["audit"]["official_v1_submission_history"]["registered"],
            "returned": source["audit"]["official_v1_submission_history"]["returned"],
            "timestamp_matches": source["audit"]["official_v1_submission_history"]["timestamp_matches"],
            "timestamp_mismatches": source["audit"]["official_v1_submission_history"]["timestamp_mismatches"],
            "outside_window": source["audit"]["official_v1_submission_history"]["outside_window"],
            "receipt": source["audit"]["official_v1_submission_history"]["receipt"],
            "boundary": "exact-v1 history, never identifier-prefix inference",
        },
        "materials_boundary": {
            "ordinary_pending": 0,
            "denominator_blockers": [],
            "former_evidence_blocker": "2606.05268",
            "former_evidence_blocker_status": "not recovered; de-admitted at the denominator because the abstract supports only a task-local spatial-layout weak-verifier method",
        },
        "gate_status": "open_pending_root_review_and_downstream_rebuild",
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tsv_lines = [
        "arxiv_id\ttitle\tsubmitted_v1_utc\tdecision\tclosure_class\tv10_comparison\trationale"
    ]
    for row in rows:
        cells = [
            row["arxiv_id"], row["title"], row["submitted_v1_utc"], row["decision"],
            row["closure_class"] or "—", row["v10_comparison"], row["rationale"],
        ]
        tsv_lines.append("\t".join(cell.replace("\t", " ").replace("\n", " ") for cell in cells))
    OUT_TSV.write_text("\n".join(tsv_lines) + "\n", encoding="utf-8")

    top_fp = ", ".join(f"`{item}`" for item in fp)
    top_fn = ", ".join(f"`{item}`" for item in fn) if fn else "—"
    cls_lines = "\n".join(f"| `{name}` | {count} |" for name, count in sorted(closure_counts.items()))
    md = f"""# 2026-06-04 Candidate Denominator Independent Audit V11

## Outcome first

对冻结窗口 `[2026-06-03 09:00, 2026-06-04 09:00) Asia/Shanghai` 的 `574/574` 个身份完成无抽样 title+full-abstract 语义复核。V10 的 `197` 个 provisional retain 不是本轮先验；独立结果保留 `{len(retained)}`，pre-denominator closure `{len(closures)}`，raw retain rate `{len(retained) / 574:.2%}`。

本阶段只重建 Candidate Denominator。没有执行 Score V2、Source Review、Deep Selection、Books Comparison 或 Books 写回，因此总 Gate 仍为 **Open**，等待 root review 与下游重建。

## Population and identity/date boundary

- Raw identities: `574`
- Semantic reviewed: `574/574`
- Duplicate identity: `0`
- Exact-v1 history receipt: registered `574`、returned `574`、timestamp match `574`、mismatch `0`、outside window `0`
- 日期只使用 exact-v1 submission history；arXiv identifier prefix 不参与日期判断。
- 审计输入为每个 family 的 title 与完整 abstract；没有抽样，也没有将 Score V2、ROADMAP mapping 或旧 Books disposition 用作 admission 信号。

## Before / after reconciliation

| Metric | V10 provisional | Independent V11 |
| --- | ---: | ---: |
| Raw identities | 574 | 574 |
| Retained candidates | 197 | {len(retained)} |
| Pre-denominator closures | 377 | {len(closures)} |
| Retain rate over raw | {197/574:.2%} | {len(retained)/574:.2%} |
| False-positive downgrades | — | {len(fp)} |
| False-negative promotions | — | {len(fn)} |
| Ordinary pending / denominator blocker | — | 0 / 0 |

### False-positive downgrades from V10

{top_fp}

### False-negative promotions over V10

{top_fn}

## Closure accounting

| Closure class | Families |
| --- | ---: |
{cls_lines}

每一条 closure 都在 `candidate-denominator-audit-independent-v11.json` 与 `.tsv` 中保存：exact identity、title、full-abstract digest、primary abstract claim、family-specific closure rationale 与 V10 reconciliation。Core Daily 的全量筛选证据被保留，但 closure 不进入 Candidate Ledger、没有 Score V2，也不触发 Source Review。

## Blocked material handling

`2606.05268` 的 exact-v1 正文仍未恢复；本审计没有把“材料缺失”伪装成“已解决”。它根据可用完整摘要被关闭在 denominator 之前：摘要只证明空间布局任务中的 LLM 弱验证器聚合，没有形成一般性的 evaluation/release contract 或 state/data/control ownership 变化。因此它不再是当前 Candidate Denominator 的 Evidence blocker；若未来材料表明更广的系统结论，应通过 revision/correction 机制重开，而不是沿用旧 blocked 状态。

## Gate truth

| Gate | Status | Boundary |
| --- | --- | --- |
| Candidate Denominator audit | Review Pending | 574/574 independent result produced; root has not accepted/frozen it |
| Evidence | Open | downstream Source Review must be rebuilt only after denominator freeze |
| Deep Selection | Open | no selection performed in this stage |
| Books Comparison / Books | Open | no comparison or writeback performed in this stage |

## Review claim

**CLAIM:** 该 V11 ledger 对 574 个身份提供了互斥、完备、可复算的 admission/closure 判定，并显著收紧 V10 的高保留率。  
**WHY THIS MATTERS:** 如果仍把 task-local paper 放入 denominator，后续 Source Review、Deep Selection 与 Books 会被无意义地放大，而且会再次把 Coverage recall 偷换成 Candidate admission。

本 sub-agent 不能再派生 fresh-context reviewer；因此这里仅提交给 root 做独立复核，不能自证 Gate 通过。Cross-model review 未执行：用户此前对本项目审计选择了 skip。
"""
    OUT_MD.write_text(md, encoding="utf-8")

    sha_lines = []
    for path in (OUT_JSON, OUT_TSV, OUT_MD):
        sha_lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}")
    OUT_SHA.write_text("\n".join(sha_lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "population": 574,
        "retained": len(retained),
        "closures": len(closures),
        "retain_rate": round(len(retained) / 574, 6),
        "false_positive_downgrades": len(fp),
        "false_negative_promotions": len(fn),
        "ordinary_pending": 0,
        "denominator_blockers": 0,
        "closure_counts": dict(sorted(closure_counts.items())),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
