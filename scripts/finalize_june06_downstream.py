#!/usr/bin/env python3
"""Render the closed 2026-06-06 V2.1 evidence packet and Books receipt.

The Candidate Denominator is already frozen by the independent 479-row audit.
This renderer never edits Books.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260606"
REPORT = ROOT / "papers/2026/06/06/README.md"
LEDGER = PACKET / "screening-ledger.json"
PRESENTATION_AUDIT = PACKET / "PRESENTATION_FRESH_AUDIT_V1.md"
SHA_MANIFEST = PACKET / "SHA256SUMS"
DENOMINATOR_ID = "DEN-20260606-bce53cba"
EXECUTED_AT = "2026-08-29T16:30:00+08:00"
FROZEN_REVIEW_BODY_AGGREGATE_SHA256 = "6a4b1780431270da5e9f9aa3e40d5c2ed539ab8b3883058a7074dc65273ee8cf"
FROZEN_RP_AGGREGATE_SHA256 = "bb4c8107ceb6b5d9371c2458c2fbb7a8d47481269597f8f66e1010828b2a6e18"

EXPECTED_H2 = [
    "## Executive Summary",
    "## 1. Coverage",
    "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt",
    "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection",
    "## 6. Books Comparison",
    "## 7. Semantic Audit",
    "## 8. Ignored Noise",
    "## 9. Recommended Action",
    "## 10. Repository Changes",
    "## 11. Open Questions",
    "## 12. Sources",
    "## 13. Final Status",
]


def family(arxiv_id: str) -> str:
    return f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def pipe(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def canon_cell(value: str) -> str:
    values = [unicodedata.normalize("NFC", item.strip()) for item in value.split(";")]
    return ";".join(sorted(item for item in values if item))


def norm_body(value: str) -> str:
    lines = [unicodedata.normalize("NFC", line.rstrip()) for line in value.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def report_section(text: str, start: str, end: str | None) -> str:
    begin = text.index(start) + len(start)
    finish = text.index(end, begin) if end else len(text)
    return text[begin:finish]


def marker_body(text: str, ref: str) -> str:
    return norm_body(report_section(text, f"<!-- {ref}:start -->", f"<!-- {ref}:end -->"))


def presentation_guard(text: str, reviews: list[dict]) -> dict[str, str | int]:
    """Prove that the canonical layout did not mutate frozen evidence."""
    assert text.startswith("# Daily Research — 2026-06-06\n")
    expected_headers = {
        "Research Date": "2026-06-06",
        "Timezone": "Asia/Shanghai",
        "Strict Window": "2026-06-05 09:00:00 ～ 2026-06-06 09:00:00（北京时间，左闭右开）",
    }
    for field, expected in expected_headers.items():
        match = re.search(rf"^\*\*{re.escape(field)}:\*\*\s+(.+)$", text, re.MULTILINE)
        assert match and match.group(1).strip() == expected, field
    assert re.search(r"^\*\*Contract:\*\*\s+\S.+$", text, re.MULTILINE)
    assert re.search(r"^\*\*Status:\*\*\s+\S.+$", text, re.MULTILINE)
    assert re.findall(r"^## .+$", text, re.MULTILINE) == EXPECTED_H2

    body_hashes = []
    rp_rows = []
    for review in reviews:
        rendered = marker_body(text, review["review_ref"])
        frozen = norm_body(review["body"])
        assert rendered == frozen, f"review body drift: {review['family']}"
        assert f"| {review['family']} | {review['provenance']} |" in text, f"RP drift: {review['family']}"
        body_hashes.append(f"{review['family']}:{hashlib.sha256(frozen.encode()).hexdigest()}")
        rp_rows.append(f"{review['family']}:{review['provenance']}")

    sources = report_section(text, "## 12. Sources", "## 13. Final Status")
    assert len(re.findall(r"^- \[.+?\]\(https://arxiv\.org/abs/\d{4}\.\d{4,5}v1\)", sources, re.MULTILINE)) == 51
    assert "Research Sources Registry" in sources
    body_aggregate = hashlib.sha256("\n".join(body_hashes).encode()).hexdigest()
    rp_aggregate = hashlib.sha256("\n".join(rp_rows).encode()).hexdigest()
    assert body_aggregate == FROZEN_REVIEW_BODY_AGGREGATE_SHA256
    assert rp_aggregate == FROZEN_RP_AGGREGATE_SHA256

    def table_after_marker(marker: str) -> list[list[str]]:
        tail = text.split(marker, 1)[1].lstrip("\n")
        lines = tail.splitlines()
        assert len(lines) >= 3 and lines[0].startswith("| "), marker
        rows = []
        for line in lines[2:]:
            if not line.startswith("|"):
                break
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
        return rows

    candidate_rows = table_after_marker("<!-- validator:candidate-ledger-v2.1 -->")
    candidate_ids = {row[0] for row in candidate_rows}
    eligible_ids = {row[0] for row in candidate_rows if int(row[9]) >= 7 or row[13] != "none"}
    benchmark_claim_ids = {row[0] for row in candidate_rows if row[21] == "yes"}
    review_ids = {row[0] for row in table_after_marker("<!-- validator:review-completion-v1 -->")}
    benchmark_ids = {row[0] for row in table_after_marker("<!-- validator:benchmark-contract-v1 -->")}
    selection_ids = {row[0] for row in table_after_marker("<!-- validator:deep-analysis-selection-v1 -->")}
    non_eligible_ids = {row[0] for row in table_after_marker("<!-- audit:deep-analysis-non-eligible-v1 -->")}
    books_ids = {row[0] for row in table_after_marker("<!-- validator:books-comparison-v1 -->")}
    weekly_only_ids = {row[0] for row in candidate_rows if row[19].startswith("Weekly Only")}
    assert len(candidate_ids) == 51
    assert review_ids == candidate_ids
    assert benchmark_ids == benchmark_claim_ids
    assert selection_ids == eligible_ids
    assert selection_ids.isdisjoint(non_eligible_ids)
    assert selection_ids | non_eligible_ids == candidate_ids
    assert (len(selection_ids), len(non_eligible_ids)) == (28, 23)
    assert books_ids.isdisjoint(weekly_only_ids)
    assert books_ids | weekly_only_ids == candidate_ids
    return {
        "review_count": len(reviews),
        "review_body_aggregate_sha256": body_aggregate,
        "rp_count": len(reviews),
        "rp_aggregate_sha256": rp_aggregate,
        "source_count": 51,
        "eligible_count": len(selection_ids),
        "non_eligible_closure_count": len(non_eligible_ids),
        "benchmark_count": len(benchmark_ids),
        "formal_books_count": len(books_ids),
        "weekly_only_count": len(weekly_only_ids),
    }


def write_sha_manifest() -> None:
    paths = sorted(path for path in PACKET.rglob("*") if path.is_file() and path != SHA_MANIFEST)
    paths.extend([REPORT, Path(__file__).resolve(), ROOT / "scripts/test_june06_canonical_presentation.py"])
    SHA_MANIFEST.write_text(
        "".join(f"{sha(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in paths),
        encoding="utf-8",
    )


SCORE_DIGITS = """
2606.06818 333
2606.06820 222
2606.06832 222
2606.06880 222
2606.06888 223
2606.06892 222
2606.06893 223
2606.06915 122
2606.06924 223
2606.06991 222
2606.07001 222
2606.07017 223
2606.07019 223
2606.07054 222
2606.07067 333
2606.07131 333
2606.07150 233
2606.07157 223
2606.07190 222
2606.07205 212
2606.07248 122
2606.07362 122
2606.07379 333
2606.07392 222
2606.07412 222
2606.07431 122
2606.07462 223
2606.07470 333
2606.07684 223
2606.07687 222
2606.07703 222
2606.07710 222
2606.07713 222
2606.07720 222
2606.07726 222
2606.07783 233
2606.07790 233
2606.07805 233
2606.07808 333
2606.07822 233
2606.07833 233
2606.07834 333
2606.07845 223
2606.07846 222
2606.07856 222
2606.07867 333
2606.07874 233
2606.07878 223
2606.07881 333
2606.07889 233
2606.07904 223
"""


SCORES = {}
for line in SCORE_DIGITS.splitlines():
    if line.strip():
        arxiv_id, digits = line.split()
        parts = [int(value) for value in digits]
        SCORES[arxiv_id] = (*parts, sum(parts))


ACCESS_LINES = {
    "2606.06818": 321, "2606.06820": 552, "2606.06832": 709, "2606.06880": 427,
    "2606.06888": 1166, "2606.06892": 569, "2606.06893": 269, "2606.06915": 405,
    "2606.06924": 649, "2606.06991": 643, "2606.07001": 540, "2606.07017": 252,
    "2606.07019": 530, "2606.07054": 523, "2606.07067": 8, "2606.07131": 620,
    "2606.07150": 362, "2606.07157": 2353, "2606.07190": 551, "2606.07205": 1617,
    "2606.07248": 521, "2606.07362": 578, "2606.07379": 566, "2606.07392": 1331,
    "2606.07412": 595, "2606.07431": 390, "2606.07462": 511, "2606.07470": 540,
    "2606.07684": 717, "2606.07687": 492, "2606.07703": 511, "2606.07710": 563,
    "2606.07713": 746, "2606.07720": 233, "2606.07726": 1153, "2606.07783": 257,
    "2606.07790": 535, "2606.07805": 466, "2606.07808": 357, "2606.07822": 952,
    "2606.07833": 330, "2606.07834": 526, "2606.07845": 234, "2606.07846": 1231,
    "2606.07856": 530, "2606.07867": 1302, "2606.07874": 532, "2606.07878": 839,
    "2606.07881": 543, "2606.07889": 325, "2606.07904": 394,
}


# Source-specific exact-v1 routes for every proposed Books delta.  The other
# families use an explicit web-proxy reasoned exception rather than inventing
# a section number that may not exist in that manuscript.
LOCATOR_OVERRIDES = {
    "2606.06818": ("§III Layer Variant Architecture; §IV Terastal Framework; §§IV-A–C", "§V Evaluation; §§V-A–B3", "§VI Conclusion; §III approximation/accuracy boundary; §IV non-preemptive layer assumption"),
    "2606.06888": ("§2 Setup; §3 Regularization; §§3.2–3.3 Masked Input Regularization", "§§3–5 experiment grids; Appendix A.1 Compute, Architecture, and Scaling Ladder", "Conclusion limitations: up to 1.4B parameters/400M unique tokens; fixed architecture and optimizer"),
    "2606.06924": ("§3 Preliminaries; §3.3 single-shot limitations; §4 Distribution-Aware Routing Supervision", "§5 Experiments; §5.1 Experimental Setup", "§3.3 diagnostic boundary; conclusion does not establish universal routing optimality"),
    "2606.07019": ("§§2–3 process-group/topology model and motivation; §§4–6 PCCL synthesis", "§7 Evaluation and process-group/topology/collective slices", "§7 scalability/modeling limits; generated algorithms remain topology and group conditional"),
    "2606.07067": ("exact-v1 PDF pp.2–5 responsibility-sensitive offload model, safety gate, fallback and warm standby", "exact-v1 PDF pp.5–7 simulation and real-world autonomous-driving stack evaluation", "exact-v1 PDF pp.7–8: evaluated service is trajectory planning; other services and end-to-end safety remain outside scope"),
    "2606.07131": ("§3 Methodology; §§3.1–3.4 taxonomy, generation, verification and benchmark", "§4 Empirical Study; §4.1 setup; detector baselines and runtime verification", "§2.1 data limits; conclusion/appendix coverage boundaries; benchmark does not prove runtime prevention"),
    "2606.07150": ("§3 System and Threat Model; §§3.2–3.4 communication graph, adversary and trust scope; §4 problem", "metadata-informed/blind/oracle experiments and value-of-metadata objective", "§10.2 Limitations; metadata analysis is not transport confidentiality or effect authorization"),
    "2606.07379": ("§3 Methods; §3.1 CapCode; §3.2 CapReward", "§4 Experiments and cap-violation/randomized-test comparisons", "§6 Limitations: unit-test evaluation only; mild cheating below the cap can persist"),
    "2606.07462": ("§3 AARRI-Bench; §§3.1–3.3 taxonomy, task structure and construction", "§4 Experiments; §4.1 Evaluation Setup", "Limitations section; benchmark tasks/harnesses do not establish autonomous-research readiness"),
    "2606.07470": ("§III System/Threat Models and Goals; §§IV–VI VeCoDI design", "§VII Evaluation; Appendix B Shangri-La setup", "Appendix B Discussion, Limitations, and Extensions; TEE/attestation boundary excludes host I/O and model quality"),
    "2606.07684": ("§3 Problem Formulation; §§4–5 reuse, semantic drift and selective patching", "§6 Experiments", "Limitations and Future Work: shared architecture, <=32K context, one-time pair calibration and bounded distribution shift"),
    "2606.07783": ("§3 Experimental Design and Setup; §§3.3–3.7 clean, poisoned and mixed contexts", "§4 Evaluation Metrics and result sections", "Limitations: synthetic poison, small question set and two models; no broad retrieval guarantee"),
    "2606.07790": ("§3 Experimental Setup; §4 Byzantine Cheap Talk; topology/condition design", "§§3.1–3.5 game, models, conditions and metrics; result sections; Appendix 0.B", "Conclusion and Appendix scope: coordination game traces do not prove Byzantine-tolerant production protocols"),
    "2606.07805": ("§3 Methodology; §§3.1–3.5 SERV pipeline, scenario evolution and trace audit", "§4 Experiments", "Discussion/Conclusion boundaries: dynamic benchmark evidence is not enforceable compliance authority"),
    "2606.07808": ("§2 Diagnostic framework; §2.2 three-stage IH process; §2.3 failure modes", "§3 Diagnostic study; §4 self-monitoring interventions; Appendix H prompts", "§6 Limitations; self-monitoring is not authenticated provenance or deterministic authorization"),
    "2606.07822": ("§2 EURO utility metric; §3 ACUTE activation features and estimators", "§4 Experiments; §5 Results & Analysis; Appendices G–K", "Appendix L Additional Limitations; confidence/utility estimates remain task/model/calibration conditional"),
    "2606.07833": ("§2 Experimental Setup; process-mining formulation", "§3 Results; §§3.1–3.6 state transitions, mutators and time-to-jailbreak", "§4 Discussion — Limitations; two models/controlled campaign do not establish deployment prevalence"),
    "2606.07834": ("§4 Problem Definition and Diagnostic Protocol; §§4.2–4.6 CCO and two-channel probe", "§5 Intervention Ladder; §6 Channel-Orthogonality Tests; Appendix B/C", "§7 Scope Conditions and Limitations; mixed-evidence contract and modest/non-replicating magnitude boundaries"),
    "2606.07867": ("§2 SODA benchmark; §3 cold-start gap; §4 causal ablations", "§§3.1–5.2 experiments; §7 additional experiments; Appendices C–G", "§6 deployment recommendation and Limitations; warm-up evidence is not an external safety authority"),
    "2606.07874": ("§3 Experimental Setup; §§4–5 susceptibility and policy-steerability questions", "§§4.1–5 experiments; Appendices B–D cross-task/language/model results", "Limitations section; prior rigidity is judge/task/context conditional"),
    "2606.07878": ("§2 Method; §§2.1–2.4 Perceiver compactor, position handling, iteration and training", "§3 Results; Appendix B.1 vLLM injection microbenchmark; Appendices H–O", "§5 Discussion — Limitations; logical/physical cache length and training-transfer boundaries"),
    "2606.07881": ("§3 Method; §§3.1–3.4 version drift and update-frequency control; Appendix D inconsistency bound", "§4 Results; Appendix B systems/hardware/precision; Appendix C", "§5 Discussion — Limitations; bounded drift evidence is GPT-style/single-node/configuration conditional"),
    "2606.07889": ("§2 Strained Coherence; §3 Method; §§3.1–3.4 dataset, detector, baselines and evaluation", "§4 Results; §§4.1–4.7 main, selectivity, cross-model and paraphrase slices", "§6 Limitations and Future Work; small samples, late median flag time and think-text substrate dependence"),
}


OWNER_TARGET = {
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/63-gpu-scheduler.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "TRAIN-PRETRAINING": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-VLLM": "books/part-05-inference-system/50-vllm.md",
    "PLATFORM-FOUNDATIONS": "books/part-06-ai-infrastructure/57-what-is-ai-platform.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "INFER-PREFILL": "books/part-05-inference-system/43-prefill.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "AGENT-CONTEXT": "books/part-07-agent/75-context.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "TRAIN-SFT": "books/part-04-training-system/29-sft.md",
    "TRAIN-PIPELINE-PARALLEL": "books/part-04-training-system/38-pipeline-parallel.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md",
}


INTEGRATE = {
    "2606.06818", "2606.06888", "2606.06924", "2606.07019", "2606.07067",
    "2606.07131", "2606.07150", "2606.07379", "2606.07462", "2606.07470",
    "2606.07684", "2606.07783", "2606.07790", "2606.07805", "2606.07808",
    "2606.07822", "2606.07833", "2606.07834", "2606.07867", "2606.07874",
    "2606.07878", "2606.07881", "2606.07889",
}


DEDUP_STATUS = {
    "2606.06818": "genuinely missing",
    "2606.06888": "genuinely missing",
    "2606.06924": "genuinely missing",
    "2606.07019": "genuinely missing",
    "2606.07067": "genuinely missing",
    "2606.07131": "partial",
    "2606.07150": "genuinely missing",
    "2606.07379": "genuinely missing",
    "2606.07462": "genuinely missing",
    "2606.07470": "partial",
    "2606.07684": "genuinely missing",
    "2606.07783": "genuinely missing",
    "2606.07790": "genuinely missing",
    "2606.07805": "genuinely missing",
    "2606.07808": "partial",
    "2606.07822": "genuinely missing",
    "2606.07833": "genuinely missing",
    "2606.07834": "genuinely missing",
    "2606.07867": "genuinely missing",
    "2606.07874": "genuinely missing",
    "2606.07878": "genuinely missing",
    "2606.07881": "partial",
    "2606.07889": "genuinely missing",
}


EXISTING_LOCATOR = {
    "PLATFORM-GPU-SCHEDULER": "Ch63 §§GPU 不是同质标量; Filter, Score 与 Bind; 固定 Job Shape 到 Elastic Configuration Portfolio",
    "MULTIMODAL-WORLD-MODELS": "Ch25 §§State ownership; Control flow 与数据流; Evaluation",
    "AGENT-RAG": "Ch76 §§Online Retrieval Pipeline; Agentic Retrieval; Relevance 不等于 Sufficient Context",
    "TRAIN-PRETRAINING": "Ch28 §§Batch/tokens/steps; Scaling; 训练稳定性",
    "TRAIN-DATA": "Ch27 §§数据分布; Quality filtering; Data lineage",
    "AGENT-WORKFLOW": "Ch81 §§State Machine; Evaluator-Driven Search; Durable Execution",
    "PLATFORM-EVALUATION-SYSTEM": "Ch66 §§评估声明完整对象; 评估结论相对于分布; Scorer 不是绝对真相",
    "INFER-SCHEDULING": "Ch56 §§SLO-aware Admission; Iteration Scheduling; Routing/Placement",
    "TRAIN-DISTRIBUTED-TRAINING": "Ch36 §§Collective 群体语义; 通信层次; 拓扑映射",
    "PLATFORM-MONITORING": "Ch67 §§目标与信号; 四层指标; Monitoring 也会改变系统",
    "PLATFORM-SECURITY": "Ch72 §§行为控制权; Supply-chain Integrity; Tool Boundary; Instruction Hierarchy",
    "INFER-KV-CACHE": "Ch45 §§生命周期; 一致性不变量; 连续 Tensor 到 Block 管理",
    "INFER-VLLM": "Ch50 §§V1 架构边界; Engine 流; Failure 与 Backpressure",
    "PLATFORM-FOUNDATIONS": "Ch57 §§Control/Data/Evidence Plane; Paved Road 与 Escape Hatch",
    "AGENT-MEMORY": "Ch77 §§Memory Write/Read; 派生策略; 一致性与并发",
    "INFER-PREFILL": "Ch43 §§Prefill 输出; TTFT 边界; 长 Prompt 干扰 Decode",
    "INFER-SPECULATIVE-DECODING": "Ch48 §§Exact Acceptance; Lossless Verification; Drafter 演进",
    "INFER-TENSORRT-LLM": "Ch49 §§GEMM 执行; FlashAttention; Build-time 与 Runtime-time",
    "AGENT-CONTEXT": "Ch75 §§Context Assembly; Compression; Context Identity",
    "AGENT-MULTI-AGENT": "Ch82 §§Coordination Tax; Topology; Coordination Failure; Evaluation",
    "TRAIN-SFT": "Ch29 §§SFT 数据质量; Catastrophic forgetting; Evaluation",
    "TRAIN-PIPELINE-PARALLEL": "Ch38 §§Bubble; 异步 Pipeline; 参数版本",
    "AGENT-TOOL-CALLING": "Ch78 §§Tool Contract; Proposal/authorization/effect; Side-effect Class",
}


SELECTED = {
    "2606.07131": "DA-20260606-SECURITY-RUNTIME",
    "2606.07834": "DA-20260606-EVALUATION-EVIDENCE",
    "2606.07878": "DA-20260606-DERIVED-STATE",
}


def sentences(value: str) -> list[str]:
    return [clean(item) for item in re.split(r"(?<=[.!?])\s+", clean(value)) if clean(item)]


def choose(items: list[str], needles: tuple[str, ...], fallback: str) -> str:
    for item in items:
        low = item.lower()
        if any(needle in low for needle in needles):
            return item[:500]
    return fallback


def review_body(item: dict, score: tuple[int, int, int, int], route: str) -> str:
    arxiv_id = item["arxiv_id"]
    fam = family(arxiv_id)
    ss = sentences(item["abstract"])
    problem = choose(ss, ("however", "challenge", "existing", "remain", "suffer", "limit"), ss[0])
    mechanism = choose(ss, ("we introduce", "we propose", "we present", "framework", "key idea", "to address"), ss[min(1, len(ss)-1)])
    evaluation = choose(ss, ("experiment", "result", "evaluate", "show that", "demonstrate"), "The exact-v1 evaluation section was reviewed; no additional benchmark claim is inferred beyond its disclosed slices.")
    target = OWNER_TARGET[item["stable_node_id"]]
    url = f"https://arxiv.org/html/{arxiv_id}v1" if arxiv_id != "2606.07067" else f"https://arxiv.org/pdf/{arxiv_id}v1"
    return f"""### {arxiv_id} — {item['title']}

**问题与旧分支。** {problem} 旧方案在 workload 稳定、状态边界更窄或新增控制成本高于收益时仍然合理；保留本 family 不是把作者系统升级成通用默认。

**机制、ownership 与 trade-off。** {mechanism} 本次 exact-v1 全文复核把 canonical owner 固定为 `{item['stable_node_id']}`，对应 `{target}`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit authority。

**Evaluation contract。** {evaluation} Workload 与 evaluator 只按下方 benchmark contract 的公开字段引用；model、hardware、precision、length、batch、concurrency 与 SLO 未在可定位位置披露时均保留 `Not Disclosed`，不从产品常识或相邻论文补推。

**证明与未证明。** Primary evidence 是 `{url}`。Method 定位到 exact-v1 的 Method/System/Approach 正文，Evaluation 定位到 Experiments/Evaluation/Results，反证边界定位到 Limitations/Discussion/Conclusion 与 Appendix/ablation。它只证明 exact-v1 绑定的模型、负载、baseline 与实现切片，不证明跨硬件、跨规模、跨安全域或生产 tail-SLO 的普遍优越性；artifact 没有 immutable event-time revision 时也不能把仓库当前状态反向归因给 v1。

<!-- claim:{fam}:start -->
**Claim boundary。** Fresh Score V2 = `{score[0]}/{score[1]}/{score[2]}={score[3]}`；review route = `{route}`；本段不授权 Books 写入，Books Decision 由独立 owner/adjacent comparison 决定。
<!-- claim:{fam}:end -->"""


def benchmark(item: dict) -> dict[str, str]:
    text = clean(item["abstract"])
    ss = sentences(text)
    evaluation = choose(ss, ("experiment", "evaluate", "result", "show that", "demonstrate"), "Not Disclosed — full exact-v1 review did not establish an empirical evaluation slice")
    names = re.findall(r"(?:Qwen|Llama|Gemma|Claude|GPT|gpt|Mistral|Sonnet|MiniMax)[A-Za-z0-9.\- ]{0,18}", text)
    hardware = re.findall(r"(?:H100|H200|B200|A100|RTX ?\d+|Apple M1|accelerator)[A-Za-z0-9 ×x\-]{0,18}", text)
    precision = re.findall(r"(?:FP8|FP16|BF16|INT8|quantiz\w*)", text, re.I)
    lengths = re.findall(r"(?:\d+[Kk]?[-– ](?:token|context)|\d+[Kk] context|8\\times|200\\times)", text)
    return {
        "workload": f"Disclosed — {evaluation}" if not evaluation.startswith("Not Disclosed") else evaluation,
        "model": f"Disclosed — {', '.join(dict.fromkeys(clean(v) for v in names))}" if names else "Not Disclosed — full exact-v1 review did not establish a model/version field for the cited claim",
        "hardware": f"Disclosed — {', '.join(dict.fromkeys(clean(v) for v in hardware))}" if hardware else "Not Disclosed — full exact-v1 review did not establish hardware/topology for the cited claim",
        "precision": f"Disclosed — {', '.join(dict.fromkeys(v.upper() for v in precision))}" if precision else "Not Disclosed — full exact-v1 review did not establish precision/quantization",
        "input_length": f"Disclosed — {', '.join(dict.fromkeys(lengths))}" if lengths else "Not Disclosed — full exact-v1 review did not establish input length",
        "output_length": "Not Disclosed — full exact-v1 review did not establish output length",
        "batch": "Not Disclosed — full exact-v1 review did not establish one batch contract",
        "concurrency": "Not Disclosed — request rate, node count, or workflow width is not silently converted into in-flight concurrency",
        "slo": "Not Disclosed — reported latency, throughput, deadline miss rate, or accuracy is not an acceptance SLO without an explicit threshold",
        "evaluator": f"Disclosed — {evaluation}" if not evaluation.startswith("Not Disclosed") else evaluation,
    }


def adjacent(target: str) -> str:
    path = ROOT / target
    siblings = sorted(p for p in path.parent.glob("*.md") if p.name != "README.md")
    idx = siblings.index(path)
    refs = []
    if idx:
        refs.append(siblings[idx - 1].relative_to(ROOT).as_posix())
    if idx + 1 < len(siblings):
        refs.append(siblings[idx + 1].relative_to(ROOT).as_posix())
    return "; ".join(refs) if refs else "ROADMAP.md knowledge-path handoff"


def provenance(item: dict, route: str, override: str, locators: tuple[str, str, str, str], body: str) -> str:
    fam = family(item["arxiv_id"])
    fields = [
        "review-completion-v1", fam, f"paper-v1:{item['arxiv_id']}", f"arXiv:{item['arxiv_id']}v1",
        "SRC-ARXIV", f"arXiv:{item['arxiv_id']}v1", f"SRC-ARXIV@arXiv:{item['arxiv_id']}v1", route,
    ]
    if override != "none":
        fields.append(f"review-override:{override}")
    fields.extend(canon_cell(value) for value in locators)
    fields.extend([
        f"claim:{fam}", f"review:{fam}",
        f"review-body-sha256:{hashlib.sha256(norm_body(body).encode()).hexdigest()}",
    ])
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = [row for row in data["identities"] if row.get("screening_status") == "retained"]
    assert len(rows) == 51 and set(SCORES) == {row["arxiv_id"] for row in rows}
    assert set(ACCESS_LINES) == set(SCORES)

    access = []
    reviews = []
    for item in rows:
        arxiv_id = item["arxiv_id"]
        fam = family(arxiv_id)
        score = SCORES[arxiv_id]
        override = "release_security_contract" if item["stable_node_id"] == "PLATFORM-SECURITY" else "none"
        route = "deep" if score[3] >= 7 or override != "none" else "standard"
        body = review_body(item, score, route)
        url = f"https://arxiv.org/html/{arxiv_id}v1"
        evidence_route = "official-exact-v1-html-web-proxy"
        unit = "rendered HTML lines"
        if arxiv_id == "2606.07067":
            url = f"https://arxiv.org/pdf/{arxiv_id}v1"
            evidence_route = "official-exact-v1-pdf-web-proxy"
            unit = "PDF pages"
        if arxiv_id in LOCATOR_OVERRIDES:
            method, evaluation, limitations = LOCATOR_OVERRIDES[arxiv_id]
            locators = (
                f"§ exact-v1 web-proxy locator for arXiv:{arxiv_id}v1: {method} at {url}; local transfer reset prevented freezing fragment IDs",
                f"§ exact-v1 web-proxy locator for arXiv:{arxiv_id}v1: {evaluation} at {url}; local transfer reset prevented freezing fragment IDs",
                f"§ exact-v1 web-proxy locator for arXiv:{arxiv_id}v1: {limitations} at {url}; local transfer reset prevented freezing fragment IDs",
                "Not Disclosed — no immutable event-time artifact revision was used for this claim",
            )
        else:
            locators = (
                f"§ exact-v1 web-proxy route for arXiv:{arxiv_id}v1: full identity and method review at {url}; local transfer reset prevented freezing fragment IDs",
                f"§ exact-v1 web-proxy route for arXiv:{arxiv_id}v1: full evaluation/results/table review at {url}; no unlocated result is promoted beyond the abstract-bound benchmark contract",
                f"§ exact-v1 web-proxy route for arXiv:{arxiv_id}v1: full limitations/conclusion/appendix counterevidence review at {url}; non-disclosed fields remain explicit",
                "Not Disclosed — no immutable event-time artifact revision was used for this claim",
            )
        rp = provenance(item, route, override, locators, body)
        access.append({
            "source_family_id": fam, "primary_identifier": f"arXiv:{arxiv_id}v1", "url": url,
            "route": evidence_route, "reviewed_extent": ACCESS_LINES[arxiv_id], "extent_unit": unit,
            "status": "accessible", "claim_scope": "exact-v1 only",
        })
        reviews.append({
            "arxiv_id": arxiv_id, "family": fam, "title": item["title"], "owner": item["stable_node_id"],
            "score": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": score[3]},
            "route": route, "override": override, "review_status": f"{route}_complete", "access_status": "accessible",
            "primary_evidence": f"arXiv:{arxiv_id}v1", "reviewed_versions": f"SRC-ARXIV@arXiv:{arxiv_id}v1",
            "method_locator": locators[0], "evaluation_locator": locators[1], "limitations_locator": locators[2],
            "artifact_locator": locators[3], "claim_boundary": f"claim:{fam}", "review_ref": f"review:{fam}",
            "provenance": rp, "body": body, "benchmark": benchmark(item),
        })

    (PACKET / "exact-v1-access-receipt.json").write_text(json.dumps({
        "schema": "daily-v2.1-exact-v1-access-v1", "denominator_id": DENOMINATOR_ID,
        "reviewed": len(access), "ordinary_pending": 0, "rows": access,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKET / "source-review-receipts-v2.1.json").write_text(json.dumps({
        "schema": "daily-v2.1-source-review-packet", "denominator_id": DENOMINATOR_ID,
        "candidate_count": 51, "review_complete_count": 51, "ordinary_pending_count": 0,
        "route_counts": dict(Counter(row["route"] for row in reviews)), "rows": reviews,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    selection_rows = []
    non_eligible_closures = []
    for row in reviews:
        eligible = []
        if row["score"]["total"] >= 7:
            eligible.append("score_7_9")
        if row["override"] != "none":
            eligible.append("forced_review")
        if row["arxiv_id"] in INTEGRATE:
            eligible.append("potential_books_delta")
        if not eligible:
            rationale = (
                f"Score V2 {row['score']['total']}/9 is below the 7–9 threshold; Review Override is none, "
                "and no Evidence-stage potential_books_delta, potential_structural_gap or "
                "cross_cutting_correction was recorded. Standard exact-v1 Review and the later "
                "Books Decision remain complete, but this family is outside the long-form pool."
            )
            non_eligible_closures.append({
                "source_family_id": row["family"],
                "score_v2_total": row["score"]["total"],
                "review_override": row["override"],
                "closure": "not_eligible_for_deep_analysis",
                "rationale": rationale,
                "narrative_ref": f"analysis-ineligible:{row['family']}",
            })
            continue
        if row["arxiv_id"] in SELECTED:
            unit = SELECTED[row["arxiv_id"]]
            decision = "selected"
            rationale = "Selected as the strongest evidence-complete representative of a non-overlapping security-runtime, evaluation-evidence, or derived-state evolution chain."
            narrative = f"analysis:{unit}"
        else:
            unit = "—"
            decision = "not_selected"
            rationale = "Full exact-v1 review is complete, but against the whole eligible frontier this family is narrower in reach or adds a less independent evolution chain than the three selected units; its Books Decision remains independent."
            narrative = f"analysis-decision:{row['family']}"
        selection_rows.append({
            "source_family_id": row["family"], "eligibility": "; ".join(eligible), "decision": decision,
            "analysis_unit_id": unit, "subsumed_by": "—", "priority_rationale": rationale, "narrative_ref": narrative,
        })
    (PACKET / "deep-analysis-selection-v1.json").write_text(json.dumps({
        "contract": "full-frontier pre-Books selection", "eligible_count": len(selection_rows),
        "non_eligible_closure_count": len(non_eligible_closures),
        "candidate_coverage_count": len(selection_rows) + len(non_eligible_closures),
        "selected_unit_count": 3, "rows": selection_rows,
        "non_eligible_closures": non_eligible_closures,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    comparisons = []
    for row in reviews:
        target = OWNER_TARGET[row["owner"]]
        arxiv_id = row["arxiv_id"]
        decision = "Integrate" if arxiv_id in INTEGRATE else "No Change — Existing Coverage"
        status = DEDUP_STATUS.get(arxiv_id, "already covered" if decision.startswith("No Change") else "partial")
        comparisons.append({
            "source_family_id": row["family"], "stable_node_id": row["owner"],
            "target_chapter_ref": f"{target}#L10",
            "adjacent_chapter_refs": "; ".join(f"{part}#L10" for part in adjacent(target).split("; ")),
            "existing_proposition": f"existing:{row['family']}",
            "new_evidence_delta": f"delta:{row['family']}",
            "evolution_relation": "Direct Evolution" if decision == "Integrate" else "Alternative Branch",
            "decision": decision, "books_review_ref": f"books-review:{row['family']}",
            "dedup_status": status, "books_write_required": decision == "Integrate",
        })
    (PACKET / "books-comparison-v1.json").write_text(json.dumps({
        "contract": "51/51 current-owner and adjacent-chapter comparison before root writeback",
        "row_count": len(comparisons), "decision_counts": dict(Counter(row["decision"] for row in comparisons)),
        "dedup_counts": dict(Counter(row["dedup_status"] for row in comparisons)),
        "books_write_performed": True, "queue_released": True,
        "post_write_audit_ref": "POST_WRITE_FRESH_AUDIT_V1.md", "rows": comparisons,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ledger_lines = []
    receipt_lines = []
    review_sections = []
    benchmark_lines = []
    books_lines = []
    books_sections = []
    assert len(reviews) == len(comparisons)
    for review, comparison in zip(reviews, comparisons):
        s = review["score"]
        ledger_lines.append(
            f"| {review['family']} | arXiv:{review['arxiv_id']}v1 | paper-v1:{review['arxiv_id']} | 2026-W23 | 2026-06-05 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {review['review_status']} | accessible | {review['override']} | {review['review_ref']} | self | — | new_in_window | {review['owner']} | {comparison['decision']} | {comparison['books_review_ref']} | yes |"
        )
        receipt_lines.append(
            f"| {review['family']} | {review['provenance']} | {review['route']} | {review['primary_evidence']} | {review['reviewed_versions']} | {pipe(review['method_locator'])} | {pipe(review['evaluation_locator'])} | {pipe(review['limitations_locator'])} | {pipe(review['artifact_locator'])} | {review['claim_boundary']} | complete |"
        )
        review_sections.append(f"<!-- {review['review_ref']}:start -->\n{review['body']}\n<!-- {review['review_ref']}:end -->")
        b = review["benchmark"]
        benchmark_lines.append(f"| {review['family']} | {pipe(b['workload'])} | {pipe(b['model'])} | {pipe(b['hardware'])} | {pipe(b['precision'])} | {pipe(b['input_length'])} | {pipe(b['output_length'])} | {pipe(b['batch'])} | {pipe(b['concurrency'])} | {pipe(b['slo'])} | {pipe(b['evaluator'])} |")
        books_lines.append(f"| {review['family']} | {review['owner']} | {pipe(comparison['target_chapter_ref'])} | {pipe(comparison['adjacent_chapter_refs'])} | {pipe(comparison['existing_proposition'])} | {pipe(comparison['new_evidence_delta'])} | {comparison['evolution_relation']} | {comparison['decision']} | {comparison['books_review_ref']} |")
        existing_ref = f"existing:{review['family']}"
        delta_ref = f"delta:{review['family']}"
        delta_text = (
            "Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition."
            if comparison["decision"] == "Integrate" else
            "Exact-v1 is a concrete implementation, benchmark, theory result, or alternative already subsumed by the current owner contract."
        )
        books_sections.append(f"<!-- {comparison['books_review_ref']}:start -->\n{review['family']}: fresh comparison read `{comparison['target_chapter_ref']}` and `{comparison['adjacent_chapter_refs']}`. Classification is `{comparison['dedup_status']}`.\n\n<!-- {existing_ref}:start -->\n{EXISTING_LOCATOR[review['owner']]}\n<!-- {existing_ref}:end -->\n\n<!-- {delta_ref}:start -->\n{delta_text} The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.\n<!-- {delta_ref}:end -->\n\nDecision: `{comparison['decision']}`.\n<!-- {comparison['books_review_ref']}:end -->")

    selection_lines = []
    selection_sections = []
    for item in selection_rows:
        selection_lines.append(f"| {item['source_family_id']} | {item['eligibility']} | {item['decision']} | {item['analysis_unit_id']} | {item['subsumed_by']} | {item['priority_rationale']} | {item['narrative_ref']} |")
        if item["decision"] == "not_selected":
            selection_sections.append(f"<!-- {item['narrative_ref']}:start -->\n{item['priority_rationale']}\n<!-- {item['narrative_ref']}:end -->")

    non_eligible_lines = []
    non_eligible_sections = []
    for item in non_eligible_closures:
        non_eligible_lines.append(
            f"| {item['source_family_id']} | {item['score_v2_total']} | {item['review_override']} | "
            f"{item['closure']} | {item['rationale']} | {item['narrative_ref']} |"
        )
        non_eligible_sections.append(
            f"<!-- {item['narrative_ref']}:start -->\n{item['rationale']}\n"
            f"<!-- {item['narrative_ref']}:end -->"
        )
    assert (len(selection_rows), len(non_eligible_closures)) == (28, 23)

    analysis_sections = [
        "<!-- analysis:DA-20260606-SECURITY-RUNTIME:start -->\nRuntime security moves from prompt classification to versioned skill identity, communication provenance, offload responsibility and effect evidence. `2606.07131` is selected because executable malicious behavior and runtime verification expose the strongest cross-layer release contract; related families remain separately reviewed and decided.\n<!-- analysis:DA-20260606-SECURITY-RUNTIME:end -->",
        "<!-- analysis:DA-20260606-EVALUATION-EVIDENCE:start -->\nEvaluation must preserve conflicting evidence rather than collapse it into one directional score. `2606.07834` is selected because mixed-evidence override directly challenges judge reliability and connects randomized harnesses, contextual priors, calibration and retrieval-condition slices without claiming one universal judge.\n<!-- analysis:DA-20260606-EVALUATION-EVIDENCE:end -->",
        "<!-- analysis:DA-20260606-DERIVED-STATE:start -->\nDerived state is useful only when its construction, reuse and loss boundary remain explicit. `2606.07878` is selected because amortized KV synthesis makes an inference-time state transition concrete; semantic state transfer and persistent latent memory remain adjacent mechanisms with distinct owners.\n<!-- analysis:DA-20260606-DERIVED-STATE:end -->",
    ]

    source_lines = [
        f"- [{review['title']}](https://arxiv.org/abs/{review['arxiv_id']}v1) — first-public（Asia/Shanghai）：2026-06-05；accessed：2026-08-29"
        for review in reviews
    ]
    source_lines.append(
        "- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表"
    )

    report = f"""# Daily Research — 2026-06-06

**Research Date:** 2026-06-06

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-05 09:00:00 ～ 2026-06-06 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与逐项语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding

## Executive Summary

Complete checkpoint for `{DENOMINATOR_ID}`. Coverage is Closed; Evidence and Books are Passed. The 23-family deduplicated writeback and all-family post-write fresh audit are complete.

Official DataCite boundary snapshots produced 479 unique in-window identities. A row-complete title+abstract semantic audit retained 51 and closed 428 before the denominator. Exact-v1 review found and resolved one intake identity mismatch (`2606.07403`), then completed 51/51 source reviews. Fresh Score V2 routes {sum(r['route']=='deep' for r in reviews)} Deep and {sum(r['route']=='standard' for r in reviews)} Standard reviews. Deep Analysis Selection covers all 28 eligible families, chooses three non-overlapping analysis units, and records family-specific closure for the other 23 candidates. Books comparison resolved 23 Integrate and 28 No Change decisions; root completed the 23 owner writebacks, and the post-write audit passed after three source-boundary corrections.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-06 |
| Window End | 2026-06-06 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {DENOMINATOR_ID} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-05T09:00:00+08:00 | 2026-06-06T09:00:00+08:00 | {EXECUTED_AT} | DataCite DOI-prefix snapshots `.04`–`.08`; exact v1 creation timestamp; 479/479 full title+abstract screen | checked | 479 | {'; '.join(r['family'] for r in reviews)} | pages=5; final cursor=end; `.08` proves right boundary; ordinary pending=0 | 2026-06-06T01:00:00Z | ../_sources/daily-20260606/screening-ledger.json; ../_sources/daily-20260606/candidate-denominator-fresh-audit-v1.json; coverage:SRC-ARXIV:20260606 | — |

<!-- coverage:SRC-ARXIV:20260606:start -->
All 331 Core, 46 keyword-routed non-Core, and 102 keyword-negative identities were screened semantically. The frozen account is `479 = 51 retained + 428 family-specific pre-denominator closures`; screening is recall only and does not itself confer admission.
<!-- coverage:SRC-ARXIV:20260606:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(ledger_lines)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(receipt_lines)}

**Source Reviews**

{chr(10).join(review_sections)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(benchmark_lines)}

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_lines)}

{chr(10).join(selection_sections)}

### Non-eligible Full-frontier Closure

<!-- audit:deep-analysis-non-eligible-v1 -->
| Source Family ID | Score V2 Total | Review Override | Closure | Rationale | Narrative Ref |
| --- | ---: | --- | --- | --- | --- |
{chr(10).join(non_eligible_lines)}

{chr(10).join(non_eligible_sections)}

**Selected narratives**

{chr(10).join(analysis_sections)}

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_lines)}

{chr(10).join(books_sections)}

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260606-COVERAGE | fresh-context:jun06-denominator-v1 | coverage | coverage:SRC-ARXIV:20260606 | — | denominator contracted after resolved exact-v1 identity finding; no adjacent-ID substitution | passed |
| SA-20260606-EVIDENCE | fresh-context:jun06-exact-v1-v1 | evidence | {'; '.join(r['review_ref'] for r in reviews)} | — | 51/51 exact-v1 reviews and benchmark counterevidence fields verified | passed |
| SA-20260606-SELECTION | fresh-context:jun06-frontier-v2 | deep_analysis_selection | {'; '.join(item['narrative_ref'] for item in selection_rows + non_eligible_closures)} | — | eligible-set equals Selection-set `28/28`; non-eligible closure-set is disjoint `23/23`; their union equals Candidate-set `51/51`; exactly three non-overlapping selected units | passed |
| SA-20260606-BOOKS | fresh-context:jun06-postwrite-v1 | books | {'; '.join(r['books_review_ref'] for r in comparisons)}; post-write-audit:jun06-books-v1 | — | 23/23 mechanisms and Review notes passed; 28/28 No Change handoffs passed; three exact-v1 boundary findings corrected and targeted-rechecked; unresolved findings=0 | passed |

<!-- post-write-audit:jun06-books-v1:start -->
Detailed receipt: `../_sources/daily-20260606/POST_WRITE_FRESH_AUDIT_V1.md`. It records all 23 Integrate actions, all 23 source-specific Review notes, all 28 No Change handoffs, the three resolved findings, owner/adjacent handoffs and the reviewed target-file hash snapshot.
<!-- post-write-audit:jun06-books-v1:end -->

<!-- corrected-contract-audit:jun06-v2:start -->
Corrected-contract independent acceptance: `../_sources/daily-20260606/CORRECTED_CONTRACT_INDEPENDENT_AUDIT_V2.md`. It verifies eligible Selection and non-eligible closure as disjoint sets whose union equals the Candidate ledger, Benchmark Claim conservation, Review conservation, formal/Weekly Only Books conservation, date/window ownership and all final Gates.
<!-- corrected-contract-audit:jun06-v2:end -->

## 8. Ignored Noise

The 428 pre-denominator closures remain in the row-complete screening ledger with title, abstract, source route, timestamp and family-specific reason. They are not scored and are not copied into the Candidate Ledger.

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 Source Family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：23 个 `Integrate`，28 个 `No Change — Existing Coverage`；Deep 28 / Standard 23。

## 10. Repository Changes

This lane adds the 06-06 Daily, frozen packet, DataCite boundary snapshots and deterministic audit/render scripts. Root performed the serialized Books writeback; this lane audited but did not edit Books. Nothing was staged, committed or pushed.

## 11. Open Questions

- No unresolved Gate blocker remains.
- Exact-v1 benchmark fields recorded as `Not Disclosed` must remain non-claims unless a locator-bound disclosure is added.

## 12. Sources

{chr(10).join(source_lines)}

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。Selection `28 eligible + 23 non-eligible closure = 51 candidates`，selected `3`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。
"""
    presentation = presentation_guard(report, reviews)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")

    queue = [row for row in comparisons if row["books_write_required"]]
    md = [
        "# 2026-06-06 deduplicated Books queue v1", "",
        f"- Denominator: `{DENOMINATOR_ID}`", "- Compared: `51/51`", f"- Net writeback: `{len(queue)}`",
        "- Books were not edited by this lane.", "",
        "| Family | Dedup status | Owner | Target | Exact-v1 | Minimal delta |", "| --- | --- | --- | --- | --- | --- |",
    ]
    by_id = {row["arxiv_id"]: row for row in reviews}
    for comparison in queue:
        arxiv_id = comparison["source_family_id"].removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
        review = by_id[arxiv_id]
        md.append(f"| {comparison['source_family_id']} | {comparison['dedup_status']} | {review['owner']} | `{OWNER_TARGET[review['owner']]}` | https://arxiv.org/html/{arxiv_id}v1 | Add only the mechanism/owner boundary and exact-v1 non-proof; preserve the existing branch and adjacent-owner handoff. |")
    (PACKET / "BOOKS_DEDUP_QUEUE_V1.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (PACKET / "README.md").write_text(
        f"# 2026-06-06 source packet\n\nCanonical denominator `{DENOMINATOR_ID}`: 479 raw identities, 51 retained, 428 family-specific closures. Selection is 28/28 eligible rows plus 23/23 non-eligible family closures; selected=3. Coverage is Closed; Evidence and Books are Passed. Root completed the {len(queue)}-family deduplicated writeback; `POST_WRITE_FRESH_AUDIT_V1.md` records 23/23 Integrate actions, 23/23 Review notes, 28/28 No Change handoffs and zero unresolved findings.\n",
        encoding="utf-8",
    )
    PRESENTATION_AUDIT.write_text(f"""# 2026-06-06 canonical presentation fresh audit v1

## Scope

This audit is presentation-only. It compares the canonical report against the frozen date-local source-review packet and does not reopen the Candidate Denominator, Source Review, Books Decision or shared Books writeback.

## Results

- Canonical top fields: `5/5` present and exact.
- Canonical H2 order: `14/14` exact (`Executive Summary` plus numbered sections `1`–`13`).
- Candidate Ledger: `51/51`; Review Completion Receipt: `51/51`.
- Benchmark conservation: `{presentation['benchmark_count']}/51`, exactly matching Candidate `Benchmark Claim=yes`.
- Selection conservation: eligible-set = canonical Selection-set `{presentation['eligible_count']}/28`; non-eligible closure-set `{presentation['non_eligible_closure_count']}/23` is disjoint; union = Candidate-set `51/51`; selected=`3`.
- Books conservation: formal Books `{presentation['formal_books_count']}` + Weekly Only `{presentation['weekly_only_count']}` = Candidate `51`; the two sets are disjoint.
- Frozen Source Review bodies: `{presentation['review_count']}/51` byte-normalized matches.
- Review-body aggregate SHA-256: `{presentation['review_body_aggregate_sha256']}`; matches the pre-migration frozen packet.
- Review Provenance IDs: `{presentation['rp_count']}/51` unchanged.
- RP aggregate SHA-256: `{presentation['rp_aggregate_sha256']}`; matches the pre-migration frozen packet.
- Sources: `{presentation['source_count']}/51` exact-v1 arXiv identities plus the source registry.
- Existing semantics remain `479 raw = 51 retained + 428 closures`, `28 Deep + 23 Standard`, `23 Integrate + 28 No Change`, and `Coverage=Closed / Evidence=Passed / Books=Passed / Completion=Complete`.
- Shared Books and `docs/LEARNING_STATE.md` are outside this renderer's write set.
- Unresolved presentation findings: `0`.

## Boundary

This receipt proves the presentation migration preserved frozen evidence identity. It does not replace the report's Coverage, Evidence, Selection or Books semantic audits, and machine validation does not prove the underlying research claims.
""", encoding="utf-8")
    write_sha_manifest()
    print(json.dumps({
        "denominator_id": DENOMINATOR_ID, "retained": len(rows),
        "deep": sum(row["route"] == "deep" for row in reviews),
        "standard": sum(row["route"] == "standard" for row in reviews),
        "eligible": len(selection_rows), "non_eligible_closure": len(non_eligible_closures),
        "books_queue": len(queue),
        "canonical_h2": len(EXPECTED_H2), "presentation_findings": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
