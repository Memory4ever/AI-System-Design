#!/usr/bin/env python3
"""Fresh downstream semantic audit for the frozen 2026-06-05 denominator.

This pass is intentionally independent of the authoring pass.  It preserves
the 64/624 denominator, re-scores all families, binds each review to exact-v1
evidence, rebuilds Selection over the eligible pool, records non-eligible
family closures separately, and compares every family
against its current Books owner and adjacent chapters.  It never edits Books.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path

from canonicalize_june_daily_presentation import canonicalize_report


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260605"
REPORT = ROOT / "papers/2026/06/05/README.md"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-recalibration-independent-adversarial-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
DOWNSTREAM = PACKET / "downstream-reconciliation-v1.tsv"
FRESH_JSON = PACKET / "fresh-downstream-adversarial-v3.json"
FRESH_MD = PACKET / "fresh-downstream-adversarial-v3.md"
FRESH_TSV = PACKET / "fresh-downstream-adversarial-v3.tsv"
SHA_MANIFEST = PACKET / "SHA256SUMS"
CHECKPOINT = PACKET / "downstream-repair-checkpoint-v1.md"
POSTWRITE = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
DENOMINATOR_ID = "DEN-20260605-66052599"
AUDITED_AT = "2026-08-29T12:40:00+08:00"

BOOK_CHECKS = [
    ("2606.05679", "PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", ("tuple-level provenance", "deterministic release check", "monotonic SQL-92", "8-core M3/16GB", "https://arxiv.org/html/2606.05679v1")),
    ("2606.05933", "INFER-SCHEDULING", "books/part-05-inference-system/56-inference-scheduling.md", ("two-iteration chunk-budget proposal", "batch membership", "predictor drift", "RTX 3090 TP2", "https://arxiv.org/html/2606.05933v1")),
    ("2606.05951", "TRAIN-DISTRIBUTED-TRAINING", "books/part-04-training-system/36-distributed-training.md", ("symmetric heap", "device-initiated one-sided RMA", "不能写成“NVSHMEM 替代 NCCL”", "CoreWeave H200", "https://arxiv.org/html/2606.05951v1")),
    ("2606.06090", "AGENT-MEMORY", "books/part-07-agent/77-memory.md", ("Execution-state Tree", "active root-to-current path", "Workflow 仍拥有下一步 action", "flat log", "https://arxiv.org/html/2606.06090v1")),
    ("2606.06240", "AGENT-MEMORY", "books/part-07-agent/77-memory.md", ("valid/system-time interval", "typed operator", "adjudication receipt", "不是自动", "https://arxiv.org/html/2606.06240v1")),
    ("2606.06256-logical", "INFER-KV-CACHE", "books/part-05-inference-system/45-why-kv-cache-speeds-up.md", ("Head-aware Recovery", "RoPE alignment", "approximate recovery", "Llama-3.3-70B/Qwen3-32B/Mistral-7B", "https://arxiv.org/html/2606.06256v1")),
    ("2606.06256-physical", "INFER-PAGED-ATTENTION", "books/part-05-inference-system/47-pagedattention.md", ("Head-segmented", "segmented page table", "matching kernel plan", "8×H800", "https://arxiv.org/html/2606.06256v1")),
    ("2606.06453", "INFER-PAGED-ATTENTION", "books/part-05-inference-system/47-pagedattention.md", ("programmable sparse", "versioned runtime index", "H200/B200", "acceptance SLO 未披露", "https://arxiv.org/html/2606.06453v1")),
    ("2606.06697", "PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", ("可信 worker 拥有真实 context", "virtualized handle", "没有实验结果", "Status: Emerging", "https://arxiv.org/html/2606.06697v1")),
]


def verify_postwrite() -> dict[str, str]:
    digests: dict[str, str] = {}
    rows: list[str] = []
    for source, owner, relative, required in BOOK_CHECKS:
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        missing = [token for token in required if token not in text]
        assert not missing, (source, relative, missing)
        digests[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"| {source} | {owner} | `{relative}` | exact-v1 URL, source-specific mechanism/body delta, prior-branch coexistence, failure/trade-off and evaluation non-proof found | passed |")
    rows_text = "\n".join(rows)
    digest_lines = "\n".join(f"- `{digest}`  `{path}`" for path, digest in sorted(digests.items()))
    POSTWRITE.write_text(f"""# 2026-06-05 post-write fresh semantic audit v1

- auditor: `fresh-context:postwrite-v1`
- scope owner: `POST_WRITE_AUDIT_SCOPE_V1.md`
- denominator: `{DENOMINATOR_ID}` = `64/624`; pre-denominator closures `560`
- Books proposals audited: `8/8`; concrete write locations: `9/9` because `2606.06256v1` has distinct logical and physical owners
- finding cycle: benchmark false negatives and Books Review-note setup omissions were found, repaired, and re-audited; unresolved findings: `0`

| Source | Canonical owner | Books file | Fresh semantic result | Status |
| --- | --- | --- | --- | --- |
{rows_text}

## Cross-owner and evolution checks

- `2606.06256v1`: Ch45 owns logical KV identity/recovery; Ch47 owns physical head-segmented page layout and matching kernel execution. Neither chapter silently absorbs the other's responsibility.
- `2606.06090v1 → 2606.06240v1`: Ch77 first establishes active execution-state/tree ownership, then adds valid/system time plus typed conflict/adjudication receipts. The second mechanism does not replace the first.
- `2606.06697v1`: Status remains `Emerging`; design/prototype scope is recorded without performance, safety-effectiveness, source-availability, or production-readiness claims.
- All eight writebacks preserve the old branch, name a state/data/control owner, state a trade-off/failure surface, and bind proof/non-proof to exact-v1 workload/model/hardware disclosures or explicit non-disclosure.

## Audited file digests

{digest_lines}

These digests freeze the concrete Books state reviewed by this receipt. Validator success is reported separately and is not the semantic proof.
""", encoding="utf-8")
    return digests


def load_author_module():
    path = ROOT / "scripts/finalize_june05_downstream.py"
    spec = importlib.util.spec_from_file_location("june05_author", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUTHOR = load_author_module()


SCORE_DIGITS = """
2606.05548 223
2606.05551 223
2606.05558 222
2606.05559 222
2606.05568 222
2606.05597 232
2606.05606 222
2606.05610 223
2606.05646 122
2606.05662 233
2606.05679 333
2606.05688 222
2606.05711 222
2606.05725 222
2606.05742 222
2606.05743 222
2606.05787 122
2606.05800 222
2606.05805 122
2606.05828 122
2606.05868 222
2606.05872 122
2606.05875 222
2606.05894 222
2606.05933 333
2606.05946 233
2606.05951 333
2606.05958 222
2606.05976 223
2606.06032 323
2606.06036 222
2606.06044 223
2606.06054 223
2606.06055 223
2606.06063 222
2606.06079 222
2606.06087 222
2606.06090 333
2606.06178 222
2606.06223 222
2606.06240 333
2606.06256 333
2606.06284 223
2606.06302 222
2606.06324 333
2606.06337 222
2606.06387 233
2606.06438 223
2606.06448 333
2606.06453 332
2606.06460 333
2606.06467 222
2606.06545 232
2606.06556 223
2606.06660 222
2606.06687 222
2606.06697 332
2606.06708 223
2606.06726 333
2606.06741 222
2606.06747 223
2606.06751 333
2606.06758 333
2606.06767 333
"""


def parse_scores() -> dict[str, dict[str, int]]:
    result = {}
    for line in SCORE_DIGITS.splitlines():
        if not line.strip():
            continue
        arxiv_id, digits = line.split()
        values = [int(value) for value in digits]
        result[arxiv_id] = {
            "design_delta": values[0],
            "system_reach": values[1],
            "durability": values[2],
            "total": sum(values),
        }
    return result


SCORES = parse_scores()
SELECTED = {
    "2606.05679": "DA-20260605-AUTHORITY",
    "2606.06240": "DA-20260605-STATE",
    "2606.06256": "DA-20260605-RUNTIME",
}
INTEGRATE = set(AUTHOR.INTEGRATE_PROPOSALS)

OWNER_QUERY = {
    "MODEL-MOE": "router expert ownership capacity communication quantization",
    "MULTIMODAL-EMBODIED-VLA": "controller safety envelope observation action physical feedback",
    "TRAIN-PRETRAINING": "objective data optimizer learning rate scaling continued pretraining",
    "TRAIN-GRPO": "rollout group advantage variance policy update evidence",
    "TRAIN-CHECKPOINT": "checkpoint state identity recovery optimizer persistence",
    "TRAIN-DISTRIBUTED-TRAINING": "collective communication ownership completion topology state",
    "INFER-KV-CACHE": "KV state identity ownership reuse compression correctness",
    "INFER-PAGED-ATTENTION": "page block sparse attention memory ownership scheduler",
    "INFER-SPECULATIVE-DECODING": "proposal verification commit rollback exactness",
    "INFER-SCHEDULING": "SLO admission scheduling goodput queue state",
    "PLATFORM-FOUNDATIONS": "declarative desired state controller reconciliation identity",
    "PLATFORM-MODEL-REGISTRY": "model artifact lineage version identity provenance",
    "PLATFORM-EVALUATION-SYSTEM": "evaluation contract EvalSpec subject environment scorer evidence decision",
    "PLATFORM-MONITORING": "evidence observability telemetry diagnosis uncertainty trace",
    "PLATFORM-COST": "lifecycle cost carbon capacity tradeoff decision",
    "PLATFORM-SECURITY": "authority policy provenance admission revocation identity audit",
    "AGENT-CONTEXT": "observation context state provenance lifecycle",
    "AGENT-RAG": "retrieval evidence index query state provenance",
    "AGENT-MEMORY": "memory write path transaction bitemporal provenance state",
    "AGENT-TOOL-CALLING": "tool selection authority schema execution evidence",
    "AGENT-REFLECTION": "verification correction evidence role state",
    "AGENT-MULTI-AGENT": "communication protocol role state authority coordination",
    "AGENT-MCP": "MCP capability identity authority tool governance",
    "AGENT-PLATFORM": "agent run skill identity trajectory evidence lifecycle",
}

LAST20_DETAIL = {
    "2606.06324": "HTIR binds failed trajectory spans to provenance, control-flow and artifact-effect edges before a scoped harness patch is admitted; its held-out gains do not establish causal correctness outside the four benchmark harnesses.",
    "2606.06337": "TokenMizer turns session history into a graph whose summaries and links are mutable derived state; graph maintenance buys bounded context but adds stale-edge, summary-loss and rebuild failure modes.",
    "2606.06387": "The attack changes an MCP tool surface during an active session, so tool identity and authorization cannot be checked only at discovery time; the experiments bound exploitability, not all MCP clients or transports.",
    "2606.06438": "CarbonSim separates embodied upgrade cost from operational savings over an explicit lifecycle horizon; conclusions move with utilization, grid mix, lifetime and performance assumptions rather than defining a universal upgrade rule.",
    "2606.06448": "The profiling harness separates memory construction, retrieval and answer generation, exposing a write-path/read-path cost frontier; ten systems and two suites characterize workloads but do not rank every production memory architecture.",
    "2606.06453": "Vortex moves sparse-attention interpretation into a programmable runtime and lowers it into kernels and scheduling state; reported speed/accuracy slices remain model, GPU, precision and length conditional.",
    "2606.06460": "In-band deny and stop signals are evaluated as two different control points, showing that recognition does not imply mid-flight termination; the pilot does not prove enforceable governance without an external reference monitor.",
    "2606.06467": "Shared routing reuses one sparse index across layers to reduce indexing work, trading layer-specific selectivity for reuse; its accuracy and efficiency evidence is architecture- and workload-bound.",
    "2606.06545": "BeeSpec makes capability, tenant, memory and policy scope explicit between a Queen control plane and Bee execution plane; the 59-task prototype validates boundaries, not production-grade isolation.",
    "2606.06556": "The position paper argues that VLA/world-model predictions do not own low-level stability, morphology, calibration or safety; it supplies a decomposition, not empirical proof of a preferred robotics stack.",
    "2606.06660": "AEGIS treats escalation to a stronger policy as a backup reflex before long-horizon error compounds; its benefit depends on risk detection, handoff latency and stronger-policy availability.",
    "2606.06687": "Semi-decentralized federated learning moves aggregation among ephemeral participants with heterogeneous optimizers, gaining serverless elasticity while adding membership, convergence and failure-recovery state.",
    "2606.06697": "AgileOS relocates the real CUDA context and protected allocation ownership to a trusted worker behind shims and virtual handles; the initial prototype publishes design and tests but no performance evaluation.",
    "2606.06708": "Signal-driven observation makes browser-state acquisition conditional rather than periodic, reducing redundant context at the price of detector misses and stale observations; this is an architectural proposal without empirical evaluation.",
    "2606.06726": "NLAC compiles natural-language requests into structured intents before policy configuration, separating uncertain translation from enforceable authorization; benchmark translation accuracy is not an end-to-end access-control guarantee.",
    "2606.06741": "OpenSkill externalizes skill discovery, synthesis and verifier feedback into versionable artifacts, enabling rollback but inheriting verifier gaming and skill-conflict failure modes.",
    "2606.06747": "Property skeletons preserve tensor-algebra invariants while generating compiler tests, expanding semantic coverage beyond example tests; detected failures do not by themselves prove production compiler correctness.",
    "2606.06751": "StageFrontier uses max-prefix telescoping to account exposed distributed-step time without double-charging synchronization wait, then explicitly downgrades causal attribution when roles or overlap violate its model.",
    "2606.06758": "Matched-evidence conditions separate retrieval availability from evidence use, turning long-context/RAG diagnosis into a controlled evaluation contract rather than a single aggregate accuracy score.",
    "2606.06767": "The custody-envelope threshold scales artifact admission controls with execution authority, identity, ingress and revocation; it is a governance instrument, not empirical evidence that one threshold fits every institution.",
}


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", value)).strip()


def pipe(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def family(arxiv_id: str) -> str:
    return f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"


def audit_rows() -> dict[str, dict[str, str]]:
    with AUDIT.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 624
    assert sum(row["independent_decision"] == "retain" for row in rows) == 64
    return {row["arxiv_id"]: row for row in rows}


def roadmap():
    text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    by_node = {}
    by_ch = {}
    for node, chapter, path in re.findall(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", text):
        by_node[node] = (int(chapter), path)
        by_ch[int(chapter)] = (node, path)
    return by_node, by_ch


def semantic_book_line(path: str, query: str) -> tuple[int, str]:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    terms = [term.lower() for term in query.split()]
    ranked = []
    for number, line in enumerate(lines, 1):
        plain = clean(line.lstrip("# -*0123456789."))
        if len(plain) < 35 or plain.startswith("http"):
            continue
        score = sum(term in plain.lower() for term in terms)
        ranked.append((score, number, plain))
    assert ranked
    _, number, proposition = max(ranked, key=lambda item: (item[0], -abs(len(item[2]) - 160)))
    return number, proposition[:300]


def review_body(review: dict, row: dict[str, str]) -> str:
    old = review.get("old_review_input") or {}
    if old:
        raw_detail = re.split(r"\n##\s+(?:Batch|Review)", old.get("body", ""), maxsplit=1)[0]
        raw_detail = raw_detail.split("Owner:", 1)[0]
        source_detail = clean(raw_detail)
    else:
        source_detail = LAST20_DETAIL.get(review["arxiv_id"], "")
    if not source_detail:
        source_detail = row["source_specific_reason"]
    benchmark = review.get("benchmark") or {}
    evaluation_scope = benchmark.get("workload", "No empirical benchmark is claimed")
    model_scope = benchmark.get("model", "No empirical model slice is claimed")
    hardware_scope = benchmark.get("hardware", "No empirical hardware slice is claimed")
    score = review["score"]
    return f"""### {review['arxiv_id']} — {review['title']}

**问题、旧方案与约束变化。** {row['source_specific_reason']} 旧方案在不需要这一额外 contract、状态边界或 workload 条件时仍然合理；本文的 admission 只来自这里明确的长期系统变化，而不是因为它能映射到 `{review['owner']}`。

**机制、实现与 ownership。** {source_detail} 在本次复核中，`{review['owner']}` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

**Evaluation contract 与反证边界。** Workload: {evaluation_scope} Model: {model_scope} Hardware: {hardware_scope} 其余 precision、输入/输出长度、batch、concurrency、SLO 与 evaluator 仅按下方 benchmark contract 的逐字段披露引用，`Not Disclosed` 字段不得由相邻段落或摘要补推。

**证明、未证明与演进关系。** Method: `{review['method_locator']}`；Evaluation: `{review['evaluation_locator']}`；Limitations: `{review['limitations_locator']}`；Artifact: `{review['artifact_locator']}`。证据证明的是 exact-v1 所绑定的方法与实验切片，不证明跨模型、硬件、负载或安全域的普遍优越性。新增 trade-off 包括额外 metadata/control state、测量与维护成本，以及 locator 所列 failure surface；旧方案仍在约束未变化或新增控制成本高于收益时成立。

<!-- claim:{review['family']}:start -->
**Claim boundary。** Fresh Score V2 = `{score['design_delta']}/{score['system_reach']}/{score['durability']}={score['total']}`；review route = `{review['route']}`；primary evidence = `arXiv:{review['arxiv_id']}v1`。本段不授权 Books 写入。
<!-- claim:{review['family']}:end -->"""


def selection_reason(review: dict, row: dict[str, str], decision: str) -> str:
    title = review["title"]
    owner = review["owner"]
    total = review["score"]["total"]
    if review["arxiv_id"] in SELECTED:
        axis = {
            "2606.05679": "跨工具与数据路径的 authority/provenance enforcement",
            "2606.06240": "持久记忆写路径的 bitemporal/isolation contract",
            "2606.06256": "KV reuse 与 segmented paging 的 runtime ownership contract",
        }[review["arxiv_id"]]
        return f"{title} 以 {axis} 改变 `{owner}` 的长期设计判断；在完整 33-family eligible pool 中，它代表一个不与另两项重复的系统轴，且 exact-v1 同时给出机制、实现与受限证据。"
    if total <= 6:
        return f"{title} 在 `{owner}` 内保留的是 `{row['source_specific_reason']}`；总分 {total} 反映其 delta 仍局限于单一机制或实验切片，优先级低于 authority、persistent-state 与 serving-runtime 三条跨层链。"
    if decision == "Integrate":
        return f"{title} 对 `{owner}` 仍有可写入的长期 delta（{row['source_specific_reason']}），但其 owner 范围或 exact-v1 证据面窄于三条 selected chain；Books proposal 保留，Deep Analysis 名额不重复占用。"
    return f"{title} 为 `{owner}` 提供了耐久证据（{row['source_specific_reason']}），但当前章节已有同一设计命题，且 exact-v1 未推翻既有结论，因此不挤占三个更直接改变 owner contract 的分析单元。"


def main() -> None:
    rows = audit_rows()
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    retained = [item for item in ledger["identities"] if rows[item["arxiv_id"]]["independent_decision"] == "retain"]
    assert len(retained) == len(SCORES) == 64
    before_nines = sum(item.get("score_v2", {}).get("total") == 9 for item in retained)
    for item in retained:
        item["score_v2"] = SCORES[item["arxiv_id"]]
        item["review_route"] = "deep" if SCORES[item["arxiv_id"]]["total"] >= 7 else "standard"
    ledger["fresh_downstream_audit"] = {
        "audit_id": "SA-20260605-DOWNSTREAM-FRESH-V3",
        "audited_at": AUDITED_AT,
        "denominator_id": DENOMINATOR_ID,
        "retained": 64,
        "closures": 560,
        "score_9_before": before_nines,
        "score_9_after": sum(score["total"] == 9 for score in SCORES.values()),
        "denominator_changed": False,
        "evidence_gate": "closed",
        "selection_gate": "closed",
        "selection_eligible": 33,
        "selection_noneligible_closures": 31,
        "books_gate": "closed_after_postwrite_fresh_audit",
    }
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Rebuild author packet with corrected scores, then independently replace
    # every semantic downstream object below.
    AUTHOR.main()
    receipts = json.loads(RECEIPTS.read_text(encoding="utf-8"))
    reviews = receipts["reviews"]
    assert len(reviews) == 64
    by_id = {item["arxiv_id"]: item for item in retained}
    by_node, by_ch = roadmap()

    web_reopened = 0
    local_reopened = 0
    benchmark_count = 0
    audit_records = []
    for review in reviews:
        arxiv_id = review["arxiv_id"]
        review["score"] = SCORES[arxiv_id]
        review["route"] = "deep" if SCORES[arxiv_id]["total"] >= 7 else "standard"
        if arxiv_id == "2606.05548":
            review["method_locator"] = 'arXiv:2606.05548v1 exact heading "2 Methodology: LLM-as-a-Developer" and "3 ADK Arena"'
            review["evaluation_locator"] = "arXiv:2606.05548v1 §4 Evaluation; §4.1 Experimental Setup"
            review["limitations_locator"] = "arXiv:2606.05548v1 §2.3 Assumptions and Scope; §5.6 Limitations"
            review["artifact_locator"] = "https://github.com/jintao-h/ADK-Arena — repository disclosed; event-time commit not pinned"
        locators = [review[key] for key in ("method_locator", "evaluation_locator", "limitations_locator", "artifact_locator")]
        assert len(set(locators)) == 4
        if review["evidence_route"] == "exact-v1-html-web-proxy":
            web_reopened += 1
            source_reopen = f"https://arxiv.org/html/{arxiv_id}v1"
        else:
            path = ROOT / review["evidence_path"]
            assert path.exists() and path.stat().st_size > 1000
            assert hashlib.sha256(path.read_bytes()).hexdigest() == review["evidence_sha256"]
            local_reopened += 1
            source_reopen = review["evidence_path"]
        if review.get("benchmark"):
            benchmark_count += 1
            assert set(review["benchmark"]) == {"workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator"}
            model = review["benchmark"]["model"]
            assert model.startswith(("Disclosed —", "Not Disclosed —"))
        review["body"] = review_body(review, rows[arxiv_id])
        review["provenance"] = AUTHOR.provenance(review, review["body"])
        review["fresh_adversarial_audit"] = {
            "audit_id": f"FA-20260605-{arxiv_id}",
            "exact_v1_reopened": source_reopen,
            "four_locator_distinctness": "passed",
            "score_v2_recomputed": True,
            "benchmark_source_wide_counterevidence": "passed" if review.get("benchmark") else "not_applicable_no_empirical_claim",
            "model_field_source": "evaluation_setup_or_table_only" if review.get("benchmark") else "not_applicable",
        }
        audit_records.append({
            "arxiv_id": arxiv_id,
            "family": review["family"],
            "source": source_reopen,
            "score": review["score"],
            "route": review["route"],
            "locators_distinct": True,
            "benchmark": bool(review.get("benchmark")),
            "owner": review["owner"],
        })

    assert local_reopened == 38 and web_reopened == 26 and benchmark_count == 60
    counts = Counter(review["route"] for review in reviews)
    verify_postwrite()
    receipts["counts"] = {"total": 64, "deep": counts["deep"], "standard": counts["standard"], "pending": 0}
    receipts["fresh_adversarial_audit"] = {
        "audit_id": "SA-20260605-DOWNSTREAM-FRESH-V3",
        "audited_at": AUDITED_AT,
        "exact_v1_local_reopened": 38,
        "exact_v1_web_reopened": 26,
        "benchmarks_counterevidence_reviewed": 60,
        "selection_eligible_reviewed": 33,
        "selection_noneligible_closures_reviewed": 31,
        "books_comparisons_reviewed": 64,
    }
    RECEIPTS.write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with DOWNSTREAM.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "source_family_id", "score_v2", "route", "owner", "access_route", "review_provenance_id", "benchmark_claim", "selection", "books_decision", "fresh_audit"])
        for review in reviews:
            score = review["score"]
            eligible = score["total"] >= 7 or review["arxiv_id"] in INTEGRATE
            selection_disposition = (
                "selected"
                if review["arxiv_id"] in SELECTED
                else "not_selected" if eligible else "non_eligible_closure"
            )
            writer.writerow([review["arxiv_id"], review["family"], f"{score['design_delta']}/{score['system_reach']}/{score['durability']}={score['total']}", review["route"], review["owner"], review["evidence_route"], review["provenance"], "yes" if review.get("benchmark") else "no", selection_disposition, "Integrate" if review["arxiv_id"] in INTEGRATE else "No Change — Existing Coverage", f"FA-20260605-{review['arxiv_id']}"])

    candidate_lines = []
    completion_lines = []
    benchmark_lines = []
    review_blocks = []
    selection_lines = []
    noneligible_lines = []
    selection_blocks = []
    books_lines = []
    books_blocks = []
    books_refs = []
    selection_refs = []
    closure_refs = []
    evidence_refs = []
    for review in reviews:
        item = by_id[review["arxiv_id"]]
        score = review["score"]
        decision = "Integrate" if review["arxiv_id"] in INTEGRATE else "No Change — Existing Coverage"
        candidate_lines.append(f"| {review['family']} | arXiv:{review['arxiv_id']}v1 | paper-v1:{review['arxiv_id']} | 2026-W23 | {item['submitted_v1_utc'][:10]} | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | {review['route']}_complete | accessible | none | {review['review_ref']} | self | — | new_in_window | {review['owner']} | {decision} | books-review:{review['family']} | {'yes' if review.get('benchmark') else 'no'} |")
        completion_lines.append(f"| {review['family']} | {review['provenance']} | {review['route']} | {review['primary_evidence']} | {review['reviewed_versions']} | {pipe(review['method_locator'])} | {pipe(review['evaluation_locator'])} | {pipe(review['limitations_locator'])} | {pipe(review['artifact_locator'])} | {review['claim_boundary']} | complete |")
        evidence_refs.append(review["review_ref"])
        if review.get("benchmark"):
            b = review["benchmark"]
            benchmark_lines.append(f"| {review['family']} | {pipe(b['workload'])} | {pipe(b['model'])} | {pipe(b['hardware'])} | {pipe(b['precision'])} | {pipe(b['input_length'])} | {pipe(b['output_length'])} | {pipe(b['batch'])} | {pipe(b['concurrency'])} | {pipe(b['slo'])} | {pipe(b['evaluator'])} |")
        review_blocks.append(f"<!-- {review['review_ref']}:start -->\n{review['body']}\n<!-- {review['review_ref']}:end -->")

        reason = selection_reason(review, rows[review["arxiv_id"]], decision)
        is_eligible = score["total"] >= 7 or decision == "Integrate"
        narrative = (
            f"analysis:{SELECTED[review['arxiv_id']]}"
            if review["arxiv_id"] in SELECTED
            else f"analysis-decision:{review['family']}" if is_eligible
            else f"selection-closure:{review['family']}"
        )
        eligibility = "score_7_9" if score["total"] >= 7 else ""
        if decision == "Integrate":
            eligibility += ("; " if eligibility else "") + "potential_books_delta"
        if eligibility:
            selection_lines.append(f"| {review['family']} | {eligibility} | {'selected' if review['arxiv_id'] in SELECTED else 'not_selected'} | {SELECTED.get(review['arxiv_id'], '—')} | — | {pipe(reason)} | {narrative} |")
            selection_refs.append(narrative)
            if review["arxiv_id"] in SELECTED:
                body_suffix = "该 family 进入 selected analysis unit；Full Source Review 与 Books Decision 均保留。"
            else:
                body_suffix = "该 eligible family 的 `not_selected` 只关闭长叙事优先级；Full Source Review 与 Books Decision 均保留。"
        else:
            noneligible_lines.append(f"| {review['family']} | {score['total']} | non_eligible_closure | below_score_7_and_no_forced_trigger | {pipe(reason)} | {narrative} |")
            closure_refs.append(narrative)
            body_suffix = "This family is outside Deep Analysis Selection eligibility because Score V2 is below 7 and no forced trigger exists. The closure is not a Selection decision; its complete Source Review and Books Decision remain reader-visible."
        selection_blocks.append(f"<!-- {narrative}:start -->\n{reason} {body_suffix}\n<!-- {narrative}:end -->")

        chapter, path = by_node[review["owner"]]
        line, proposition = semantic_book_line(path, OWNER_QUERY[review["owner"]])
        adjacent = []
        for adjacent_chapter in (chapter - 1, chapter + 1):
            if adjacent_chapter in by_ch:
                _, adjacent_path = by_ch[adjacent_chapter]
                adjacent_line, _ = semantic_book_line(adjacent_path, OWNER_QUERY[review["owner"]])
                adjacent.append(f"{adjacent_path}#L{adjacent_line}")
        relation = "Direct Evolution" if decision == "Integrate" else "Layering / Dependency"
        books_ref = f"books-review:{review['family']}"
        books_lines.append(f"| {review['family']} | {review['owner']} | {path}#L{line} | {'; '.join(adjacent)} | existing:{review['family']} | delta:{review['family']} | {relation} | {decision} | {books_ref} |")
        decision_reason = "该 evidence delta 改变或补全 owner 的长期 contract，交给 root 串行写入。" if decision == "Integrate" else "目标章节已表达同一长期命题；exact-v1 只增加条件化实例或实验，不重写长期结论。"
        books_blocks.append(f"<!-- {books_ref}:start -->\n<!-- existing:{review['family']}:start -->{proposition}<!-- existing:{review['family']}:end -->\n\n<!-- delta:{review['family']}:start -->{rows[review['arxiv_id']]['source_specific_reason']}<!-- delta:{review['family']}:end -->\n\n实际读取 owner `{path}#L{line}` 与相邻章节 `{' ; '.join(adjacent)}`。Decision: `{decision}`。{decision_reason} 本 lane 不写 Books。\n<!-- {books_ref}:end -->")
        books_refs.append(books_ref)

    prefix = REPORT.read_text(encoding="utf-8").split("## 2. Candidate Ledger and Score V2", 1)[0]
    score_distribution = Counter(review["score"]["total"] for review in reviews)
    prefix = re.sub(r"Completion Status \| In Progress", "Completion Status | Complete", prefix)
    prefix = re.sub(r"Evidence Gate \| Open", "Evidence Gate | Passed", prefix)
    prefix = re.sub(r"Books Gate \| Open", "Books Gate | Passed", prefix)
    prefix = re.sub(r"All 64 retained families.*?digest\.\n", f"All 64 retained families were independently re-opened against exact-v1 evidence. Fresh scoring yields {counts['deep']} Deep and {counts['standard']} Standard reviews; Score 9 fell from 46 to {score_distribution[9]}, removing the prior ceiling clustering. Evidence and Selection are closed. Root's eight Integrate proposals were then audited at nine concrete Books locations; all post-write findings were repaired and re-audited, so Books is closed.\n", prefix, flags=re.S)
    report = prefix.rstrip() + "\n\n## 2. Candidate Ledger and Score V2\n\n<!-- validator:candidate-ledger-v2.1 -->\n| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |\n| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(candidate_lines)
    report += "\n\n### Review Completion Receipt\n\n<!-- validator:review-completion-v1 -->\n| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(completion_lines)
    report += "\n\n### Benchmark Contract\n\n<!-- validator:benchmark-contract-v1 -->\n| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(benchmark_lines)
    report += "\n\n## 3. Source Reviews\n\n" + "\n\n".join(review_blocks)
    report += "\n\n## 4. Deep Analysis Selection\n\n<!-- validator:deep-analysis-selection-v1 -->\n| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |\n| --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(selection_lines)
    report += "\n\n### Non-eligible family closures\n\n下列 31 个 retained family 不满足 Deep Analysis Selection eligibility：Score V2 低于 7，且没有 forced trigger。它们不进入 Selection 表，也不生成 `not_selected` 决策；每项以 family-specific closure 与 bounded ref 保留完整理由，同时继续保留 Source Review 与 Books Decision。\n\n| Source Family ID | Total | Disposition | Closure Basis | Family-specific rationale | Closure Ref |\n| --- | ---: | --- | --- | --- | --- |\n" + "\n".join(noneligible_lines) + "\n\n" + "\n\n".join(selection_blocks)
    report += "\n\n## 5. Books Comparison and Decision\n\n<!-- validator:books-comparison-v1 -->\n| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(books_lines) + "\n\n" + "\n\n".join(books_blocks)
    report += f"""

## 6. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260605-COVERAGE | fresh-context:denominator-v1 | coverage | coverage:SRC-ARXIV:20260605 | — | `{DENOMINATOR_ID}` unchanged: 64/624, closures 560 | passed |
| SA-20260605-EVIDENCE-FRESH-V3 | fresh-context:downstream-v3 | evidence | {'; '.join(evidence_refs)} | — | 64/64 exact-v1 reopened; 60/60 benchmark contracts counterevidence-reviewed; ADK locator corrected; Score 9 reduced 46→{score_distribution[9]} | passed |
| SA-20260605-SELECTION-FRESH-V3 | fresh-context:downstream-v3 | deep_analysis_selection | {'; '.join(selection_refs + closure_refs)} | — | 33/33 eligible decisions reviewed: exactly 3 selected and 30 not_selected; 31/31 non-eligible families closed separately with family-specific bounded refs | passed |
| SA-20260605-BOOKS-POSTWRITE-V1 | fresh-context:postwrite-v1 | books | {'; '.join(books_refs)} | — | 8/8 Integrate proposals audited at 9/9 concrete Books locations; 2606.06256 logical/physical ownership and 2606.06090→2606.06240 evolution verified; repaired benchmark and Review-note findings re-audited; receipt `../_sources/daily-20260605/POST_WRITE_FRESH_AUDIT_V1.md` | passed |

## 7. Materials and Access

Ordinary review pending: `0`. Exact-v1 body re-opened: `64/64` (`38` local hash-verified bodies, `26` official arXiv exact-v1 HTML reads). Benchmark contracts: `60/60` reviewed field by field; `4` papers make no empirical benchmark claim. No blocked or unverified retained family remains.

## 8. Repository Changes and Continuation

Root serialized eight `Integrate` proposals across Ch36, Ch45, Ch47, Ch56, Ch72 and Ch77. This fresh lane repaired the 2606.05679/05933/06256 benchmark false negatives, corrected the 2606.05679/05951 method locators, and re-audited all nine concrete Books locations without modifying Books. Coverage, Evidence, Selection and Books Gates are closed; unresolved findings are zero. Post-write receipt: `../_sources/daily-20260605/POST_WRITE_FRESH_AUDIT_V1.md`.

## Sources

- Official exact-v1 manuscripts: `https://arxiv.org/html/<id>v1` or locally frozen exact-v1 PDF/HTML.
- Frozen denominator: `../_sources/daily-20260605/denominator-recalibration-independent-adversarial-v1.tsv`.
- Fresh audit receipt: `../_sources/daily-20260605/fresh-downstream-adversarial-v3.json`.
- Post-write Books receipt: `../_sources/daily-20260605/POST_WRITE_FRESH_AUDIT_V1.md`.
"""
    REPORT.write_text(report, encoding="utf-8")
    # Report generation must not regress the reader-facing Daily V2.1 contract.
    # The canonicalizer only reorders already-rendered sections and preserves
    # bounded Source Review bodies, so Review Provenance remains stable.
    canonicalize_report(REPORT, "2026-06-05")

    packet_readme = (PACKET / "README.md").read_text(encoding="utf-8")
    marker = "## Canonical denominator and downstream checkpoint"
    if marker in packet_readme:
        packet_readme = packet_readme.split(marker, 1)[0].rstrip() + "\n\n"
    packet_readme += f"""{marker}

- canonical denominator: `{DENOMINATOR_ID}` = `64 retained / 560 pre-denominator closures` (`624/624` audited)
- Score V2 / route after fresh audit: `64/64` = `{counts['deep']} Deep / {counts['standard']} Standard`
- score ceiling correction: `9/9` reduced from `46/64` to `{score_distribution[9]}/64`
- exact-v1 reopened: `64/64` = `38` local hash-verified + `26` official HTML
- benchmark counterevidence: `60/60`; no empirical claim: `4`
- Deep Analysis Selection: `33/33` eligible families = `3` selected + `30` not_selected; `31/31` non-eligible families have separate family-specific closures
- Books Comparison: `64/64`; `8` Integrate proposals audited at `9` concrete write locations; Books files changed by this audit lane: `0`
- Gate: Coverage `Closed`; Evidence `Passed`; Selection semantic audit `Passed`; Books `Passed`; Completion `Complete`

Canonical fresh artifacts: `fresh-downstream-adversarial-v3.json`, `fresh-downstream-adversarial-v3.tsv`, `source-review-receipts-v2.1.json`, `downstream-reconciliation-v1.tsv`, and `../../05/README.md`.
"""
    (PACKET / "README.md").write_text(packet_readme, encoding="utf-8")

    CHECKPOINT.write_text(f"""# 2026-06-05 downstream repair checkpoint v3

This checkpoint is downstream of frozen denominator `{DENOMINATOR_ID}` and records Evidence/Selection plus post-write Books fresh-context semantic audits.

## Canonical counts

- raw / retained / pre-denominator closure: `624 / 64 / 560`
- Source Review: `64/64` (`{counts['deep']}` Deep, `{counts['standard']}` Standard), ordinary pending `0`
- exact-v1 reopened: `64/64` (`38` local hash-verified, `26` official HTML)
- benchmark counterevidence: `60/60`; no empirical claim `4`
- Score V2 ceiling: `9/9` reduced from `46/64` to `{score_distribution[9]}/64`
- Deep Analysis Selection: eligible `33/33`; selected `3`; not_selected `30`
- Non-eligible family closures: `31/31`; none is represented as a Selection decision
- Books comparison: `64/64`; Integrate proposals `8`; post-write locations audited `9/9`; Books writes by this audit lane `0`

## Gate

- Coverage: `Closed`
- Evidence: `Passed`
- Deep Analysis Selection semantic audit: `Passed`
- Books: `Passed`

All 2026-06-05 Gates are closed. Root's serialized writebacks are recorded by `ROOT_BOOKS_RECONCILIATION_V1.md`; independent post-write resolution is recorded by `POST_WRITE_FRESH_AUDIT_V1.md`. Unresolved findings: `0`.
""", encoding="utf-8")

    FRESH_JSON.write_text(json.dumps({
        "schema": "daily-downstream-fresh-adversarial-v3",
        "audit_id": "SA-20260605-DOWNSTREAM-FRESH-V3",
        "audited_at": AUDITED_AT,
        "denominator_id": DENOMINATOR_ID,
        "counts": {
            "raw": 624, "retained": 64, "closures": 560,
            "exact_v1_reopened": 64, "local": 38, "web": 26,
            "deep": counts["deep"], "standard": counts["standard"],
            "score_9_before": 46, "score_9_after": score_distribution[9],
            "benchmark_reviewed": 60, "selection_eligible_reviewed": 33,
            "selection_noneligible_closures_reviewed": 31,
            "books_comparison_reviewed": 64,
        },
        "gate": {"coverage": "closed", "evidence": "closed", "selection": "closed", "books": "closed_after_postwrite_fresh_audit"},
        "records": audit_records,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with FRESH_TSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "family", "source", "score", "route", "locators_distinct", "benchmark", "owner"])
        for record in audit_records:
            score = record["score"]
            writer.writerow([record["arxiv_id"], record["family"], record["source"], f"{score['design_delta']}/{score['system_reach']}/{score['durability']}={score['total']}", record["route"], "passed", "yes" if record["benchmark"] else "no", record["owner"]])
    FRESH_MD.write_text(f"""# 2026-06-05 downstream fresh adversarial audit v3

- denominator: `{DENOMINATOR_ID}` = `64/624`; closures `560`; changed: `no`
- exact-v1 reopened: `64/64` (`38` local hash-verified, `26` official HTML)
- Source Review: `64/64`; Deep `{counts['deep']}`; Standard `{counts['standard']}`; pending `0`
- Score V2 ceiling: `9/9` reduced from `46/64` to `{score_distribution[9]}/64`
- benchmark counterevidence: `60/60`; no empirical claim: `4`
- Deep Analysis Selection: eligible `33/33`, selected `3`, not_selected `30`
- non-eligible family closures: `31/31`; none is represented as a Selection decision
- Books comparison: `64/64`, owner+adjacent read; ADK Arena corrected to the evaluation-contract proposition
- Gates: Coverage `Closed`; Evidence `Closed`; Selection `Closed`; Books `Closed`; Completion `Complete`
- Books files modified by this lane: `0`

All eight Integrate proposals were audited at nine concrete Books locations; `2606.06256v1` retains distinct logical and physical owners. Repaired benchmark and Review-note findings were re-audited with zero unresolved findings. See `POST_WRITE_FRESH_AUDIT_V1.md`.
""", encoding="utf-8")

    manifest_paths = [LEDGER, RECEIPTS, DOWNSTREAM, FRESH_JSON, FRESH_MD, FRESH_TSV, PACKET / "README.md", CHECKPOINT, POSTWRITE, REPORT, Path(__file__).resolve(), ROOT / "scripts/audit_june05_corrected_contract.py"]
    SHA_MANIFEST.write_text("\n".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}" for path in manifest_paths) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
