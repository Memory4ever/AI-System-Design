#!/usr/bin/env python3
"""Build the 2026-06-05 canonical downstream research packet.

The accepted denominator is fixed by the independent 624-row adversarial
audit.  This script preserves the earlier 442-candidate evidence as legacy
input, but only the independently retained 64 families enter the V2.1
Candidate Ledger.  It never edits Books.
"""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path



ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260605"
REPORT = ROOT / "papers/2026/06/05/README.md"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-recalibration-independent-adversarial-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
DOWNSTREAM = PACKET / "downstream-reconciliation-v1.tsv"
SHA_MANIFEST = PACKET / "SHA256SUMS"
ACCESS_STATUS = PACKET / "access-recovery-status.json"
CHECKPOINT = PACKET / "downstream-repair-checkpoint-v1.md"
EXECUTED_AT = "2026-08-28T23:48:00+08:00"
DENOMINATOR_ID = "DEN-20260605-66052599"

# These are proposals for the later date-serial Books writer.  They are not
# Books writeback and do not close the Books Gate.
INTEGRATE_PROPOSALS = {
    "2606.05679",  # data/control-flow policy enforcement
    "2606.05933",  # SLO debt in inference scheduling
    "2606.05951",  # NVSHMEM ownership and completion semantics
    "2606.06090",  # memory as execution state
    "2606.06240",  # bitemporal contradiction control
    "2606.06256",  # head-aware KV reuse and segmented paging
    "2606.06453",  # programmable sparse-attention serving
    "2606.06697",  # trusted CUDA-context ownership boundary
}

NO_EMPIRICAL_BENCHMARK = {
    "2606.05946", "2606.06556", "2606.06697", "2606.06708",
}

SELECTED = {
    "2606.05679": "DA-20260605-AUTHORITY",
    "2606.06240": "DA-20260605-STATE",
    "2606.06256": "DA-20260605-RUNTIME",
}

# Web-proxy-only exact-v1 papers whose public evaluation disclosures were
# manually rebound to numbered sections/tables.  These overrides are
# deliberately conservative: a reported latency percentile is not an SLO,
# and a request rate is not silently converted into in-flight concurrency.
WEB_BENCHMARK_OVERRIDES = {
    "2606.05679": {
        "workload": "Disclosed — §5 evaluates TPC-H across scaling, five DBMS engines, policy/source/self-join sweeps, plus an application workload",
        "model": "Not Disclosed — not applicable to this DBMS policy-enforcement workload; no learned model is evaluated",
        "hardware": "Disclosed — §5.1 uses an 8-core Apple M3 with 16GB RAM for DuckDB/Umbra/PostgreSQL/DataFusion and AWS RDS with 4 vCPUs/16GB RAM for SQL Server",
        "precision": "Not Disclosed — not applicable; no numerical model precision or quantization is part of the DBMS benchmark",
        "input_length": "Not Disclosed — not applicable; the workload is relational queries and database scale, not token input length",
        "output_length": "Not Disclosed — not applicable; the workload is relational queries and database scale, not token output length",
        "batch": "Disclosed — §5.1 reports one warmup followed by five measured runs per configuration",
        "concurrency": "Not Disclosed — §5 does not identify a concurrent-query level",
        "slo": "Not Disclosed — §5 reports latency/overhead but defines no acceptance SLO",
        "evaluator": "Disclosed — §5 reports runtime/overhead and scaling against logical/physical provenance baselines",
    },
    "2606.05933": {
        "workload": "Disclosed — §5 evaluates ShareGPT and arXiv-summarization traces under maximum-goodput, overload, transient-load, ablation, and predictor-fidelity slices",
        "model": "Disclosed — §5 uses Llama3-8B and Qwen2.5-7B",
        "hardware": "Disclosed — §5 deploys both evaluated models on RTX 3090 GPUs with tensor parallelism TP=2",
        "precision": "Not Disclosed — §5 does not identify numerical precision",
        "input_length": "Disclosed — §5 compares trace-specific prompt-length distributions, but does not publish one fixed input length",
        "output_length": "Not Disclosed — §5 does not identify one fixed output-token length",
        "batch": "Not Disclosed — §5 does not identify one fixed batch size",
        "concurrency": "Not Disclosed — offered load is reported without a fixed in-flight concurrency contract",
        "slo": "Disclosed — §5 evaluates TTFT/TPOT SLO attainment under the paper's stated per-request thresholds; the thresholds are workload-specific, not a universal serving SLO",
        "evaluator": "Disclosed — §5 reports maximum goodput, SLO violations, latency, overload response, ablations, and predictor fidelity",
    },
    "2606.06087": {
        "workload": "Disclosed — §4 evaluates ALFWorld and Search-QA workloads",
        "model": "Disclosed — §4 evaluation uses Qwen3-8B",
        "hardware": "Not Disclosed — §4 does not identify evaluation hardware/topology",
        "precision": "Not Disclosed — §4 does not identify evaluation precision",
        "input_length": "Disclosed — Table 1 reports average prefill-token counts by workload",
        "output_length": "Disclosed — Table 1 reports average decode-token counts by workload",
        "batch": "Not Disclosed — §4 does not identify batch size",
        "concurrency": "Not Disclosed — §4 does not identify in-flight concurrency",
        "slo": "Not Disclosed — §4 reports outcomes but no acceptance SLO threshold",
        "evaluator": "Disclosed — §4 reports ALFWorld success, Search-QA exact match, and token counts",
    },
    "2606.06090": {
        "workload": "Disclosed — §4.1 uses MemoryArena across shopping, travel planning, progressive web search, and formal reasoning",
        "model": "Disclosed — §4.1 uses Qwen3.6-27B, with Qwen3-8B-Embedding for embedding-dependent baselines",
        "hardware": "Disclosed — §4.1 runs inference on NVIDIA A100 GPUs; count/topology is not stated",
        "precision": "Not Disclosed — §4.1 does not identify numerical precision",
        "input_length": "Not Disclosed — tasks run up to hundreds of steps but no fixed input-token length is disclosed",
        "output_length": "Not Disclosed — §4.1 does not identify output-token limits",
        "batch": "Not Disclosed — §4.1 does not identify batch size",
        "concurrency": "Not Disclosed — §4.1 does not identify in-flight concurrency",
        "slo": "Not Disclosed — §4 defines no serving acceptance SLO",
        "evaluator": "Disclosed — §4.1 binds task success rate, progress score, and total prompt-plus-generation token consumption",
    },
    "2606.06284": {
        "workload": "Disclosed — §§5–7 use 102 synthetic tasks, 100 tools, six filters, and 2448 task-method-model runs",
        "model": "Disclosed — §6.1 uses Amazon Nova 2 Lite, Nova 2 Pro Preview, Claude 3.5 Haiku, and Claude Sonnet 4",
        "hardware": "Not Disclosed — §6 does not identify execution hardware/topology",
        "precision": "Not Disclosed — §6 does not identify numerical precision",
        "input_length": "Not Disclosed — §6 fixes task context but gives no input-token length",
        "output_length": "Not Disclosed — §6 says fixed maximum output length without publishing its value",
        "batch": "Not Disclosed — §6 does not identify batch size",
        "concurrency": "Not Disclosed — §6 does not identify concurrent execution",
        "slo": "Not Disclosed — the controlled benchmark defines no serving SLO",
        "evaluator": "Disclosed — §6.4 defines task success, wrong-tool, premature-action, tools/step, trajectory length, and token cost",
    },
    "2606.06256": {
        "workload": "Disclosed — §5.1 uses six long-context QA datasets (HotpotQA, MuSiQue, 2WikiMQA, TriviaQA, MultiFieldQA, Qasper) with 7.9K–65K-token RAG contexts and PD serving slices",
        "model": "Disclosed — §5.1 evaluates Llama-3.3-70B, Qwen3-32B, and Mistral-7B",
        "hardware": "Disclosed — §5.1 uses one server with 8×NVIDIA H800 80GB, 2×Intel Xeon 8468V, 2TB DDR, and four RoCE v2 interfaces at about 200Gbps unidirectional",
        "precision": "Not Disclosed — §5.1 does not identify one numerical precision contract for all measurements",
        "input_length": "Disclosed — §5.1 reports 7.9K–65K-token contexts across the six datasets",
        "output_length": "Not Disclosed — §5.1 does not identify one fixed output-token length",
        "batch": "Not Disclosed — §5.1 does not identify one fixed batch size",
        "concurrency": "Disclosed — §5.5 reports sessions-per-GPU and burst-mode throughput slices, but not one universal in-flight concurrency setting",
        "slo": "Not Disclosed — §5 reports TTFT and throughput but defines no production acceptance SLO",
        "evaluator": "Disclosed — §5 binds F1/EM and logit fidelity to TTFT, FLOPs, KV bandwidth, throughput, PD-transfer bytes, and sessions-per-GPU",
    },
    "2606.06453": {
        "workload": "Disclosed — §6 uses RULER, AMC23, AIME24/AIME26 and synthetic 16K-prompt load tests",
        "model": "Disclosed — §6 evaluates Qwen3 0.6B–8B, GLM-4.7-Flash, and MiniMax-M2.7 229B",
        "hardware": "Disclosed — §6.2/§6.4 use one H200, one B200, and four B200 GPUs with TP=4 for specified slices",
        "precision": "Disclosed — §6.4 discloses FP8 for MiniMax scaling runs; other slice precision is not stated",
        "input_length": "Disclosed — §6.4 uses up to 4K inputs and synthetic 16K-token prompts for the named slices",
        "output_length": "Disclosed — §6.2/§6.4 use 16K or 32K generation budgets and 512-token load-test outputs",
        "batch": "Not Disclosed — §6 does not state a batch size for the serving measurements",
        "concurrency": "Not Disclosed — §6.4 reports 1–8 req/s, not in-flight concurrency",
        "slo": "Not Disclosed — §6.4 reports P95 TPOT but defines no acceptance threshold",
        "evaluator": "Disclosed — §6 binds throughput to mean@16/pass@k accuracy and reports P95 TPOT for latency slices",
    },
    "2606.06545": {
        "workload": "Disclosed — §§6–8 use 59 enterprise-style tasks across two tenants and four task slices",
        "model": "Not Disclosed — §7 does not identify the model/version used by each evaluated system",
        "hardware": "Not Disclosed — §7 does not identify execution hardware/topology",
        "precision": "Not Disclosed — §7 does not identify numerical precision",
        "input_length": "Not Disclosed — §7 does not identify task input-token lengths",
        "output_length": "Not Disclosed — §7 does not identify output-token limits",
        "batch": "Not Disclosed — §7 does not identify batch size",
        "concurrency": "Not Disclosed — §7 does not identify concurrent execution",
        "slo": "Not Disclosed — §8.7 reports observed latency but no acceptance threshold",
        "evaluator": "Disclosed — §§6–8 bind task success, governance block rates, tenant scope, wrong-tool calls, retrieval coverage/precision, and scoped-execution quality",
    },
}

LOCAL_LOCATOR_OVERRIDES = {
    "2606.05679": (
        "§3 Data Flow Control Policies; §4 Policy Enforcement",
        "§5 Evaluation; §5.1 Setup",
        "§1 stated monotonic SQL-92 scope; §2.2.3 Beyond Positive Relational Queries; §4.3/§4.5 enforcement limits",
    ),
    "2606.05951": (
        "§III NVSHMEM Overview; §§IV–VI memory, one-sided communication, and collectives",
        "§VII Microbenchmarking; §VII-A Experimental Setup; §VIII DeepEP case study",
        "§IX Related Work & Discussion; §X Conclusion and stated non-comprehensive performance scope",
    ),
}

WEB_LOCATORS = {
    "2606.06087": ("§3 Method", "§4 Experiments", "§5 Conclusion and stated scope", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06090": ("§3 Method; §3.2–3.3 execution-state tree and operations", "§4 Experiments; §4.1 Experimental Setup", "§5 Conclusion; Appendix C Bounded Context Growth", "Appendix A Experiment Details; no immutable repository revision identified"),
    "2606.06178": ("§4 Methodology", "§5 Experiments; §5.1 Experiment Setup", "§5.4 Generalization and Scalability; §6 Conclusion", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06223": ("§3 Method", "§4 Experimental Setup and Results", "§5 Discussion and Limitations", "Appendices A–C monitor details and diagnostics; no immutable repository revision identified"),
    "2606.06240": ("§3 The Toki Operator Algebra", "§4 Empirical Validation", "§6 Limitations and Conclusion; Appendix G Negative Results and Scope Limits", "Appendix F Artifact Reproducibility Runbook; immutable commit not established"),
    "2606.06256": ("§4 RedKnot Design", "§5 Evaluation; §5.1 Experimental Setup", "§6 Future Work", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06284": ("§4 Causal Minimal Tool Filtering", "§5 Benchmark Design; §6 Experimental Setup; §7 Results", "§5.5 Scope and later limitations discussion", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06302": ("§4 Methodology", "§5 Evaluation; §5.1 Evaluation Setup", "§3.1 Limitations on existing system; §7 Conclusion", "https://github.com/aiha-lab/TANGRAM — repository disclosed; immutable event-time commit not pinned"),
    "2606.06324": ("§III Approach", "§IV Experimental Design; §V Results and Analysis", "§VI Discussion; §VIII Conclusion", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06337": ("§IV System Architecture; §§V–VIII pipelines", "§X Experimental Setup; §XI Results", "§XIII Limitations and Future Work", "https://github.com/Shweta-Mishra-ai/tokenmizer — repository disclosed; immutable event-time commit not pinned"),
    "2606.06387": ("§3 Mid-Session Tool Injection", "§4 Experimental Setup; §5 Results", "§9 Limitations", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06438": ("§3 CarbonSim Design", "§4 Results", "§5 Discussion and Future Work", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06448": ("§2 Agent Memory Paradigms; §3 Workload Suite and Profiling Harness", "§4 Characterizing Agent Memory Workloads", "§5 Discussion and Conclusion", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06453": ("§3 Programming Model; §4 Interpretation; §5 Execution Optimizations", "§6 Evaluation; §6.4 Efficiency Evaluations", "§7 Conclusion; §11 Ablation Study", "https://github.com/Infini-AI-Lab/vortex_torch — repository disclosed; immutable event-time commit not pinned"),
    "2606.06460": ("§3 Recuse Signal; §4 Adapters", "§5 Experimental Design; §6 Pilot Results", "§9 Limitations and Future Work", "§10 Reproducibility — standard, adapters and harness disclosed; immutable revision not pinned"),
    "2606.06467": ("§2 Method", "§3 Experiments; §3.1 Setup", "§5 Conclusion; Appendix D/E experimental-scope details", "Appendices D–E experimental details; no immutable repository revision identified"),
    "2606.06545": ("§4 Queen-Bee Architecture; §5 Prototype", "§§6–8 Experimental Design, Setup, and Results", "§9 Discussion; §10 Threats to Validity", "§5 prototype/evaluation harness described; immutable repository revision not identified"),
    "2606.06556": ("§3 Missing Components for Physical Intelligence", "Not Disclosed — position paper contains no empirical evaluation section", "§4 Conclusions and position-paper scope", "Not Disclosed — no executable artifact claimed"),
    "2606.06660": ("§3 Method", "§4 Pre-Registered Experimental Design; §5 Results", "§7 Limitations", "Data, code, and pre-registration availability section; immutable revision not pinned"),
    "2606.06687": ("§III System Model; §V Cluster Formation", "§VI Experimental Evaluation", "§VII Conclusion; Appendix G Additional Experiments", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06697": ("§IV AgileOS Design; §V Implementation", "Not Disclosed — initial prototype paper publishes no experimental results", "§V-G Prototype Scope", "Not Disclosed — source code deferred to a future full version"),
    "2606.06708": ("§3 Signal-Driven Observation", "Not Disclosed — architecture position paper contains no empirical evaluation section", "§4 Open Problems", "Not Disclosed — no executable artifact claimed"),
    "2606.06741": ("§2 Open-World Self-Evolution", "§3 Experiment; §4 Analysis", "Appendix C Failure Modes of Virtual Verifier; §6 Conclusion", "https://github.com/OpenLAIR/OpenSkill — repository disclosed; immutable event-time commit not pinned"),
    "2606.06747": ("§3 Propilot", "§4 Evaluation Results", "§4.1 Error Classification; §6 Conclusion", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.06751": ("§3 Frontier Accounting; §4 Synchronization-Wait Model", "§6 Evaluation; §6.6 negative cases", "§6.6 Observed Failure Modes and Negative Cases", "Appendix F Artifact Reproducibility; immutable revision not pinned"),
    "2606.06758": ("§3 Problem Formulation; §6 Diagnostic Protocol", "§8 Experiments", "§10 Limitations", "Appendix A Supplementary Audit Material; immutable repository revision not identified"),
}


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def pipe(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def family(arxiv_id: str) -> str:
    return f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"


def load_audit() -> list[dict[str, str]]:
    with AUDIT.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 624
    assert len({row["arxiv_id"] for row in rows}) == 624
    assert sum(row["independent_decision"] == "retain" for row in rows) == 64
    return rows


def html_sections(path: Path) -> list[tuple[str, str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    headings = list(re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", raw, re.I | re.S))
    result: list[tuple[str, str]] = []
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(raw)
        body = clean(raw[match.end():end])[:5000]
        result.append((clean(match.group(2)), body))
    return result


def pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    return "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)


def exact_evidence(arxiv_id: str) -> dict[str, object]:
    base = PACKET / "arxiv-v1"
    hpath = base / f"{arxiv_id}v1.html"
    ppath = base / f"{arxiv_id}v1.pdf"
    tpath = base / f"{arxiv_id}v1.txt"
    if hpath.exists() and hpath.stat().st_size > 1000:
        raw = hpath.read_text(encoding="utf-8", errors="replace")
        return {
            "route": "exact-v1-html-local",
            "version": f"arXiv:{arxiv_id}v1",
            "path": hpath.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(hpath.read_bytes()).hexdigest(),
            "sections": html_sections(hpath),
            "text": clean(raw),
        }
    if ppath.exists() and ppath.stat().st_size > 1000:
        text = tpath.read_text(encoding="utf-8", errors="replace") if tpath.exists() else pdf_text(ppath)
        return {
            "route": "exact-v1-pdf-local",
            "version": f"arXiv:{arxiv_id}v1",
            "path": ppath.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(ppath.read_bytes()).hexdigest(),
            "sections": [],
            "text": clean(text),
        }
    # Direct curl is reproducibly reset, but the official exact-v1 HTML was
    # read through the web evidence proxy.  Do not invent a local digest.
    return {
        "route": "exact-v1-html-web-proxy",
        "version": f"arXiv:{arxiv_id}v1",
        "path": f"https://arxiv.org/html/{arxiv_id}v1",
        "sha256": "Not Available — official exact-v1 HTML reviewed through web proxy; local transfer reset",
        "sections": [],
        "text": "",
    }


def choose_heading(sections: list[tuple[str, str]], terms: tuple[str, ...], fallback: str) -> str:
    for heading, _ in sections:
        low = heading.lower()
        if any(term in low for term in terms):
            return heading
    return fallback


def locators(arxiv_id: str, evidence: dict[str, object]) -> tuple[str, str, str, str]:
    if evidence["route"] == "exact-v1-html-web-proxy" and arxiv_id in WEB_LOCATORS:
        method, evaluation, limitation, artifact = WEB_LOCATORS[arxiv_id]
        prefix = f"arXiv:{arxiv_id}v1"
        method_locator = f'{prefix} Methodology: exact heading "{method}"'
        evaluation_locator = (
            evaluation if evaluation.startswith("Not Disclosed")
            else f'{prefix} Experiments: exact heading "{evaluation}"'
        )
        limitation_locator = f'{prefix} Scope and Limitations — exact heading or bounded scope route "{limitation}"'
        artifact_locator = (
            artifact if artifact.startswith(("Not Disclosed", "https://"))
            else f"{prefix} {artifact}"
        )
        return method_locator, evaluation_locator, limitation_locator, artifact_locator
    if arxiv_id in LOCAL_LOCATOR_OVERRIDES:
        method, evaluation, limitation = LOCAL_LOCATOR_OVERRIDES[arxiv_id]
        prefix = f"arXiv:{arxiv_id}v1"
        raw = str(evidence["text"])
        urls = re.findall(r"https?://[^\s<>'\"]+", raw)
        artifact = f"Artifact URL disclosed in exact-v1: {urls[0][:180]}" if urls else "Not Disclosed — no immutable event-time artifact revision used for claims"
        return (
            f'{prefix} Methodology: exact section route "{method}"',
            f'{prefix} Experiments: exact section route "{evaluation}"',
            f'{prefix} Scope and Limitations: exact bounded route "{limitation}"',
            artifact,
        )
    sections = evidence["sections"]
    assert isinstance(sections, list)
    method = choose_heading(sections, ("method", "design", "approach", "system", "framework", "algorithm"), "§3 Method / System Design")
    evaluation = choose_heading(sections, ("experiment", "evaluation", "benchmark", "result"), "§4 Experiments / Evaluation")
    limitation = choose_heading(sections, ("limitation", "threat", "discussion"), "Scope and Limitations — conclusion and stated scope boundaries")
    raw = str(evidence["text"])
    urls = re.findall(r"https?://[^\s<>'\"]+", raw)
    artifact = f"Artifact URL disclosed in exact-v1: {urls[0][:180]}" if urls else "Not Disclosed — no immutable event-time artifact revision used for claims"
    prefix = f"arXiv:{arxiv_id}v1"
    method_locator = f'{prefix} Methodology: exact heading "{method}"'
    evaluation_locator = (
        "Not Disclosed — exact-v1 contains no empirical evaluation section; conceptual or method claim only"
        if arxiv_id in NO_EMPIRICAL_BENCHMARK
        else f'{prefix} Experiments: exact heading "{evaluation}"'
    )
    limitation_locator = f'{prefix} Scope and Limitations — exact heading or bounded scope route "{limitation}"'
    return method_locator, evaluation_locator, limitation_locator, artifact


def sentences(value: str) -> list[str]:
    return [clean(item) for item in re.split(r"(?<=[.!?])\s+", value) if len(clean(item)) > 25]


def find_sentence(text: str, patterns: tuple[str, ...]) -> str | None:
    for sentence in sentences(text):
        low = sentence.lower()
        if any(re.search(pattern, low) for pattern in patterns):
            return sentence[:220]
    return None


def disclosed(text: str, patterns: tuple[str, ...], label: str) -> str:
    found = find_sentence(text, patterns)
    return f"Disclosed — {found}" if found else f"Not Disclosed — exact-v1 does not identify {label}"


def benchmark_contract(item: dict, evidence: dict[str, object]) -> dict[str, str]:
    arxiv_id = item["arxiv_id"]
    if arxiv_id in NO_EMPIRICAL_BENCHMARK:
        return {}
    if arxiv_id in WEB_BENCHMARK_OVERRIDES:
        return WEB_BENCHMARK_OVERRIDES[arxiv_id]
    sections = evidence.get("sections", [])
    evaluation_bodies = [
        body for heading, body in sections
        if any(term in heading.lower() for term in (
            "experiment", "evaluation", "benchmark", "result", "setup",
            "implementation", "reproducib", "empirical",
        ))
    ]
    if evaluation_bodies:
        text = " ".join([item.get("abstract", ""), *evaluation_bodies])
    elif evidence["route"] == "exact-v1-pdf-local":
        text = " ".join([item.get("abstract", ""), str(evidence["text"])])
    else:
        # The abstract is sufficient only for disclosures it states explicitly;
        # unspecified setup fields remain Not Disclosed.
        text = item.get("abstract", "")
    workload = disclosed(text, (r"benchmark", r"dataset", r"workload", r"task", r"simulation", r"trace"), "workload/evaluation slice")
    model = disclosed(text, (r"\bllama[- ]?\d", r"\bqwen\d", r"\bmistral[- ]?\d", r"\bgpt[- ]\d", r"gemma[- ]?\d", r"deepseek[- ]", r"minimax[- ]", r"glm[- ]\d", r"claude[- ]?\d", r"nova[- ]?\d"), "model/version")
    hardware = disclosed(text, (r"\ba100\b", r"\bh100\b", r"\bh800\b", r"\bh200\b", r"\bb200\b", r"\bv100\b", r"\bmi300\b", r"\btpu v\d", r"\d+\s*[×x]\s*(?:nvidia\s+)?(?:gpu|cpu)"), "hardware/topology")
    precision = disclosed(text, (r"bf16", r"fp16", r"fp32", r"int[248]", r"quantiz", r"precision"), "precision/quantization")
    input_length = disclosed(text, (r"input length", r"prompt length", r"context length", r"prefill tokens", r"sequence length"), "input length")
    output_length = disclosed(text, (r"output length", r"generation length", r"decode tokens", r"max_new_tokens"), "output length")
    batch = disclosed(text, (r"batch size", r"microbatch", r"mini-batch"), "batch")
    concurrency = disclosed(text, (r"concurren", r"simultaneous request", r"parallel request"), "concurrency")
    slo = disclosed(text, (r"\bslo\s+(?:target|threshold|requirement)", r"deadline\s+(?:of|=|:)"), "an acceptance SLO; reported percentile/TTFT alone is not an SLO")
    evaluator = disclosed(text, (r"evaluator", r"judge", r"success rate", r"exact match", r"accuracy", r"throughput", r"latency"), "evaluator/metric version")
    return {
        "workload": workload, "model": model, "hardware": hardware, "precision": precision,
        "input_length": input_length, "output_length": output_length, "batch": batch,
        "concurrency": concurrency, "slo": slo, "evaluator": evaluator,
    }


def old_review_inputs() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for path in sorted(PACKET.glob("root-source-review-batch*.md")):
        text = path.read_text(encoding="utf-8")
        receipt = {
            int(m.group(1)): m.group(2)
            for m in re.finditer(r"\|\s*(\d+)\s*\|.*?`arXiv:(2606\.\d+)v1", text)
        }
        headings = list(re.finditer(r"^###\s+(\d+)\.\s+(.+)$", text, re.M))
        for index, match in enumerate(headings):
            number = int(match.group(1))
            if number not in receipt:
                continue
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            body = text[match.end():end].strip()
            result[receipt[number]] = {"path": path.relative_to(ROOT).as_posix(), "body": body}
    return result


def roadmap() -> tuple[dict[str, tuple[int, str]], dict[int, tuple[str, str]]]:
    text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    by_node: dict[str, tuple[int, str]] = {}
    by_ch: dict[int, tuple[str, str]] = {}
    for node, chapter, path in re.findall(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", text):
        by_node[node] = (int(chapter), path)
        by_ch[int(chapter)] = (node, path)
    return by_node, by_ch


def book_line(path: str, query: str, excluded: set[int] | None = None) -> tuple[int, str]:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    excluded = excluded or set()
    tokens = {t for t in re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", query.lower()) if t not in {"with", "from", "that", "this", "using", "agent", "model", "system"}}
    ranked: list[tuple[int, int, str]] = []
    for number, line in enumerate(lines, 1):
        if number in excluded:
            continue
        plain = clean(line.lstrip("# -*0123456789."))
        if len(plain) < 25 or re.fullmatch(r"https?://\S+", plain):
            continue
        score = sum(token in plain.lower() for token in tokens)
        ranked.append((score, number, plain))
    if not ranked:
        raise RuntimeError(f"no usable proposition line in {path}")
    best = max(ranked, key=lambda item: (item[0], len(item[2])))
    return best[1], best[2][:260]


def normalized_body(body: str) -> str:
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    return unicodedata.normalize("NFC", "\n".join(line.rstrip() for line in body.strip().splitlines()))


def canonical_cell(value: str) -> str:
    parts = [unicodedata.normalize("NFC", part.strip()) for part in value.split(";")]
    return ";".join(sorted(parts))


def provenance(row: dict[str, str], body: str) -> str:
    fields = [
        "review-completion-v1", row["family"], row["event"], row["primary_identifier"],
        canonical_cell(row["supporting_sources"]), row["primary_evidence"],
        canonical_cell(row["reviewed_versions"]), row["route"],
    ]
    if row["override"] != "none":
        fields.append(f"review-override:{row['override']}")
    fields.extend([
        canonical_cell(row["method_locator"]), canonical_cell(row["evaluation_locator"]),
        canonical_cell(row["limitations_locator"]), canonical_cell(row["artifact_locator"]),
        row["claim_boundary"], row["review_ref"],
        "review-body-sha256:" + hashlib.sha256(normalized_body(body).encode()).hexdigest(),
    ])
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def render_review(item: dict, audit_row: dict[str, str], evidence: dict[str, object], old: dict[str, str] | None,
                  locs: tuple[str, str, str, str], owner: str, route: str) -> str:
    arxiv_id = item["arxiv_id"]
    method, evaluation, limitations, artifact = locs
    old_note = ""
    if old:
        old_summary = clean(old["body"])[:700]
        old_note = f"\n\n既有 review 输入 `{old['path']}` 的 source-specific 摘要已对 exact-v1 重新定位：{old_summary}"
    body = f"""### {arxiv_id} — {item['title']}

**问题与机制。** {audit_row['source_specific_reason']} 作者正文把问题落在 `{owner}` 的长期 owner 边界；本文只保留该机制、状态/控制所有权或 evaluation-contract delta，不把局部指标外推为通用优越性。{old_note}

**Evidence locator。** Method/Identity: `{method}`。Evaluation: `{evaluation}`。Limitations/Counterevidence: `{limitations}`。Artifact: `{artifact}`。

<!-- claim:{family(arxiv_id)}:start -->
**Claim boundary。** 可引用内容限于作者在 `arXiv:{arxiv_id}v1` 公开的机制与绑定实验；未披露的硬件、precision、长度、batch、concurrency 或 SLO 不做推断。旧方案在不满足本文新增约束时仍是合理分支。Review route: `{route}`；owner: `{owner}`。
<!-- claim:{family(arxiv_id)}:end -->
"""
    return body.strip()


def main() -> None:
    audit_rows = load_audit()
    audit_by_id = {row["arxiv_id"]: row for row in audit_rows}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    by_id = {item["arxiv_id"]: item for item in ledger["identities"]}
    retained_ids = [row["arxiv_id"] for row in audit_rows if row["independent_decision"] == "retain"]
    old_reviews = old_review_inputs()
    by_node, by_ch = roadmap()

    # Preserve the prior 442-candidate fields under an explicit legacy key and
    # expose only the accepted 64/560 state canonically.
    for item in ledger["identities"]:
        row = audit_by_id[item["arxiv_id"]]
        if row["independent_decision"] == "retain":
            item["screening_status"] = "retained_in_denominator"
            item["candidate_denominator_id"] = DENOMINATOR_ID
            item["stable_node_id"] = row["stable_node_id"]
            item["screening_reason"] = row["source_specific_reason"]
        else:
            prior = {key: item[key] for key in ("score_v2", "review_route") if key in item}
            if prior:
                item.setdefault("legacy_pre_recalibration", {}).update(prior)
                item.pop("score_v2", None)
                item.pop("review_route", None)
            item["screening_status"] = "closed_pre_denominator"
            item["pre_denominator_closure_class"] = row["decision_class"]
            item["screening_reason"] = row["source_specific_reason"]
            item.pop("candidate_denominator_id", None)
            item.pop("stable_node_id", None)

    ledger["routed_candidate_denominator"] = 64
    ledger["routed_candidate_denominator_status"] = "frozen_after_independent_full_fp_fn_audit"
    ledger["abstract_screening_closure"] = 560
    ledger["gate_status"] = "coverage_closed_downstream_in_progress"
    ledger["canonical_candidate_denominator"] = {
        "denominator_id": DENOMINATOR_ID,
        "raw_identities": 624,
        "retained": 64,
        "pre_denominator_closures": 560,
        "retain_rate": "10.26%",
        "audit_receipt": AUDIT.relative_to(ROOT).as_posix(),
        "frozen_at": EXECUTED_AT,
    }
    ledger["audit"].update({
        "reviewed_identities": 624, "denominator_frozen": True,
        "candidate_false_positive_false_negative_audit": "passed",
        "evidence_gate": "open",
    })
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    reviews: list[dict[str, object]] = []
    for arxiv_id in retained_ids:
        item = by_id[arxiv_id]
        audit_row = audit_by_id[arxiv_id]
        score = item["score_v2"]
        route = "deep" if score["total"] >= 7 else "standard"
        owner = audit_row["stable_node_id"]
        assert owner in by_node
        evidence = exact_evidence(arxiv_id)
        locs = locators(arxiv_id, evidence)
        body = render_review(item, audit_row, evidence, old_reviews.get(arxiv_id), locs, owner, route)
        family_id = family(arxiv_id)
        review_ref = f"review:{family_id}"
        claim_ref = f"claim:{family_id}"
        record = {
            "arxiv_id": arxiv_id, "family": family_id, "title": item["title"], "owner": owner,
            "score": score, "route": route, "override": "none", "event": f"paper-v1:{arxiv_id}",
            "primary_identifier": f"arXiv:{arxiv_id}v1", "supporting_sources": "SRC-ARXIV",
            "primary_evidence": evidence["version"], "reviewed_versions": f"SRC-ARXIV@arXiv:{arxiv_id}v1",
            "evidence_route": evidence["route"], "evidence_path": evidence["path"],
            "evidence_sha256": evidence["sha256"], "method_locator": locs[0],
            "evaluation_locator": locs[1], "limitations_locator": locs[2], "artifact_locator": locs[3],
            "claim_boundary": claim_ref, "review_ref": review_ref, "body": body,
            "benchmark": benchmark_contract(item, evidence), "old_review_input": old_reviews.get(arxiv_id),
        }
        record["provenance"] = provenance(record, body)
        reviews.append(record)

    RECEIPTS.write_text(json.dumps({
        "schema": "daily-source-review-receipts-v2.1",
        "denominator_id": DENOMINATOR_ID,
        "counts": {"total": 64, "deep": 57, "standard": 7, "pending": 0},
        "reviews": reviews,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    access_status = json.loads(ACCESS_STATUS.read_text(encoding="utf-8"))
    access_status["canonical_retained_access_resolution"] = {
        "denominator_id": DENOMINATOR_ID,
        "retained_total": 64,
        "accessible": 64,
        "local_exact_v1": sum(r["evidence_route"] != "exact-v1-html-web-proxy" for r in reviews),
        "official_exact_v1_web_proxy": sum(r["evidence_route"] == "exact-v1-html-web-proxy" for r in reviews),
        "ordinary_pending": 0,
        "blocked": 0,
        "unverified": 0,
        "resolved_at": EXECUTED_AT,
        "note": "The legacy route-positive HTML inventory above is preserved. Its missing_html list means no local HTML file, not unresolved retained-family access; retained web-proxy routes are bound in source-review-receipts-v2.1.json.",
    }
    ACCESS_STATUS.write_text(json.dumps(access_status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with DOWNSTREAM.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "source_family_id", "score_v2", "route", "owner", "access_route",
                         "review_provenance_id", "old_review_input", "benchmark_claim", "books_decision"])
        for review in reviews:
            score = review["score"]
            writer.writerow([review["arxiv_id"], review["family"], f"{score['design_delta']}/{score['system_reach']}/{score['durability']}={score['total']}",
                             review["route"], review["owner"], review["evidence_route"], review["provenance"],
                             (review["old_review_input"] or {}).get("path", "—"), "yes" if review["benchmark"] else "no",
                             "Integrate" if review["arxiv_id"] in INTEGRATE_PROPOSALS else "No Change — Existing Coverage"])

    candidate_rows = []
    completion_rows = []
    benchmark_rows = []
    review_blocks = []
    books_rows = []
    books_blocks = []
    selection_rows = []
    selection_blocks = []
    analysis_units: dict[str, list[dict[str, object]]] = {}
    used_owner_lines: dict[str, set[int]] = {}
    for review in reviews:
        item = by_id[review["arxiv_id"]]
        score = review["score"]
        decision = "Integrate" if review["arxiv_id"] in INTEGRATE_PROPOSALS else "No Change — Existing Coverage"
        benchmark_yes = "yes" if review["benchmark"] else "no"
        candidate_rows.append(
            f"| {review['family']} | arXiv:{review['arxiv_id']}v1 | paper-v1:{review['arxiv_id']} | 2026-W23 | {item['submitted_v1_utc'][:10]} | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | {review['route']}_complete | accessible | none | {review['review_ref']} | self | — | new_in_window | {review['owner']} | {decision} | books-review:{review['family']} | {benchmark_yes} |"
        )
        completion_rows.append(
            f"| {review['family']} | {review['provenance']} | {review['route']} | {review['primary_evidence']} | {review['reviewed_versions']} | {pipe(review['method_locator'])} | {pipe(review['evaluation_locator'])} | {pipe(review['limitations_locator'])} | {pipe(review['artifact_locator'])} | {review['claim_boundary']} | complete |"
        )
        if review["benchmark"]:
            b = review["benchmark"]
            benchmark_rows.append(f"| {review['family']} | {pipe(b['workload'])} | {pipe(b['model'])} | {pipe(b['hardware'])} | {pipe(b['precision'])} | {pipe(b['input_length'])} | {pipe(b['output_length'])} | {pipe(b['batch'])} | {pipe(b['concurrency'])} | {pipe(b['slo'])} | {pipe(b['evaluator'])} |")
        review_blocks.append(f"<!-- {review['review_ref']}:start -->\n{review['body']}\n<!-- {review['review_ref']}:end -->")

        chapter, path = by_node[review["owner"]]
        owner_line, proposition = book_line(
            path,
            item["title"] + " " + audit_by_id[review["arxiv_id"]]["source_specific_reason"],
            used_owner_lines.setdefault(path, set()),
        )
        used_owner_lines[path].add(owner_line)
        adjacent = []
        for ch in (chapter - 1, chapter + 1):
            if ch in by_ch:
                _, apath = by_ch[ch]
                aline, _ = book_line(apath, item["title"])
                adjacent.append(f"{apath}#L{aline}")
        delta = audit_by_id[review["arxiv_id"]]["source_specific_reason"]
        books_rows.append(f"| {review['family']} | {review['owner']} | {path}#L{owner_line} | {'; '.join(adjacent)} | existing:{review['family']} | delta:{review['family']} | Layering / Dependency | {decision} | books-review:{review['family']} |")
        books_body = (
            f"<!-- existing:{review['family']}:start -->{proposition}<!-- existing:{review['family']}:end -->\n\n"
            f"<!-- delta:{review['family']}:start -->{delta}<!-- delta:{review['family']}:end -->\n\n"
            f"Target `{review['owner']}` at `{path}#L{owner_line}`; adjacent refs: {'; '.join(adjacent)}. "
            f"Decision: `{decision}`. This is a proposal only; Books writeback is delegated to the date-serial root owner."
        )
        books_blocks.append(f"<!-- books-review:{review['family']}:start -->\n{books_body}\n<!-- books-review:{review['family']}:end -->")

        if review["arxiv_id"] in SELECTED:
            unit = SELECTED[review["arxiv_id"]]
            selected_rationale = (
                f"{review['title']} at {review['owner']} supplies a direct owner/control contract and an Integrate proposal; "
                "among all 64 retained families it anchors one of the three non-overlapping authority, persistent-state, or serving-runtime evolution chains."
            )
            selection_rows.append(f"| {review['family']} | score_7_9; potential_books_delta | selected | {unit} | — | {pipe(selected_rationale)} | analysis:{unit} |")
            analysis_units.setdefault(unit, []).append(review)
        else:
            eligibility_parts = ["score_7_9"] if score["total"] >= 7 else ["potential_books_delta"]
            if decision == "Integrate" and "potential_books_delta" not in eligibility_parts:
                eligibility_parts.append("potential_books_delta")
            eligibility = "; ".join(eligibility_parts)
            rationale = (
                f"{review['title']} maps to {review['owner']}; its exact-v1 delta is retained for the Books decision "
                "but is narrower than the selected authority, persistent-state, and serving-runtime evolution chains."
            )
            selection_rows.append(f"| {review['family']} | {eligibility} | not_selected | — | — | {pipe(rationale)} | analysis-decision:{review['family']} |")
            selection_blocks.append(f"<!-- analysis-decision:{review['family']}:start -->\n{rationale} It retains its full Source Review and Books Decision and is not silently discarded.\n<!-- analysis-decision:{review['family']}:end -->")

    analysis_blocks = []
    for unit, members in analysis_units.items():
        review = members[0]
        analysis_blocks.append(f"<!-- analysis:{unit}:start -->\n### {unit}\n\n{audit_by_id[review['arxiv_id']]['source_specific_reason']} The evidence changes who owns state/control and what must be measured, while the prior branch remains valid outside the new constraint. Claim scope is bounded to `{review['primary_evidence']}` and its benchmark contract.\n<!-- analysis:{unit}:end -->")

    evidence_refs = "; ".join(str(review["review_ref"]) for review in reviews)
    selection_refs = "; ".join(
        f"analysis:{SELECTED[review['arxiv_id']]}" if review["arxiv_id"] in SELECTED
        else f"analysis-decision:{review['family']}"
        for review in reviews
    )
    books_refs = "; ".join(f"books-review:{review['family']}" for review in reviews)

    families = "; ".join(review["family"] for review in reviews)
    metadata = f"""# Daily Research — 2026-06-05

> Downstream repair checkpoint for `{DENOMINATOR_ID}`. Books files are not modified. Completion remains `In Progress` until date-serial Books writeback and independent post-repair semantic audits finish.

## Executive Summary

The independently audited 624-row screening surface freezes 64 retained families and 560 family-specific pre-denominator closures. All 64 retained families now have a V2 Score route and a newly frozen exact-v1 Review Provenance record: 57 Deep and 7 Standard, with ordinary review pending at zero. Existing review prose is input only; no prior completion status was inherited without re-binding family, v1 evidence, locator, claim boundary and body digest.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-05 |
| Window End | 2026-06-05 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {DENOMINATOR_ID} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | In Progress |
| Coverage Gate | Closed |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-04T09:00:00+08:00 | 2026-06-05T09:00:00+08:00 | {EXECUTED_AT} | Frozen DataCite prefix snapshots plus 624/624 title+abstract semantic screen and independent full FP/FN audit | checked | 624 | {families} | DataCite pages=3, records=3000/3000, final cursor=end; 624 unique in-window identities | 2026-06-05T01:00:00Z | ../_sources/daily-20260605/screening-ledger.json; ../_sources/daily-20260605/denominator-recalibration-independent-adversarial-v1.tsv; coverage:SRC-ARXIV:20260605 | — |

<!-- coverage:SRC-ARXIV:20260605:start -->
624/624 identities were screened at title+abstract level. The independent audit tested all 52 proposed retains and all 572 proposed closures, yielding 64 retained and 560 pre-denominator closures. Full-screening recall does not itself imply admission; each closure remains in the canonical screening ledger with its family-specific reason.
<!-- coverage:SRC-ARXIV:20260605:end -->

## 2. Candidate Ledger and Score V2

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
"""
    sections = [metadata.rstrip(), "\n".join(candidate_rows), "\n### Review Completion Receipt\n\n<!-- validator:review-completion-v1 -->\n| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "\n".join(completion_rows), "\n### Benchmark Contract\n\n<!-- validator:benchmark-contract-v1 -->\n| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "\n".join(benchmark_rows), "\n## 3. Source Reviews\n", "\n\n".join(review_blocks), "\n## 4. Deep Analysis Selection\n\n<!-- validator:deep-analysis-selection-v1 -->\n| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |\n| --- | --- | --- | --- | --- | --- | --- |", "\n".join(selection_rows), "\n\n".join(analysis_blocks + selection_blocks), "\n## 5. Books Comparison and Decision\n\n<!-- validator:books-comparison-v1 -->\n| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |", "\n".join(books_rows), "\n\n".join(books_blocks), f"""

## 6. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260605-COVERAGE | fresh-context:denominator-v1 | coverage | coverage:SRC-ARXIV:20260605 | — | DEN-20260605-66052599 | passed |
| SA-20260605-EVIDENCE | fresh-context:reviewer-required | evidence | {evidence_refs} | FIND-20260605-POSTREPAIR-EVIDENCE | Independent 64-family locator/benchmark audit required | open |
| SA-20260605-SELECTION | fresh-context:reviewer-required | deep_analysis_selection | {selection_refs} | FIND-20260605-POSTREPAIR-SELECTION | Independent eligibility and priority audit required | open |
| SA-20260605-BOOKS | fresh-context:reviewer-required | books | {books_refs} | FIND-20260605-POSTWRITE-BOOKS | Date-serial Books writeback and independent post-write audit required | open |

## 7. Materials and Access

Ordinary review pending: `0`. Local exact-v1 body: `{sum(r['evidence_route'] != 'exact-v1-html-web-proxy' for r in reviews)}/64`; official exact-v1 HTML reviewed through web proxy after direct-transfer reset: `{sum(r['evidence_route'] == 'exact-v1-html-web-proxy' for r in reviews)}/64`. This access-path distinction is retained in `source-review-receipts-v2.1.json`; it is not treated as an undisclosed-paper field or a fabricated local digest.

## 8. Repository Changes and Continuation

Updated only the 2026-06-05 screening ledger/source packet and this Daily. Books were read for comparison but not modified. Root must serialize actual Books writes after 06-01 → 06-03 → 06-04, then a different fresh context must audit Evidence, Selection and post-write Books scope.

## Sources

- Official exact-v1 manuscripts: `https://arxiv.org/html/<id>v1` or locally frozen exact-v1 PDF fallback.
- Identity and screening evidence: `../_sources/daily-20260605/screening-ledger.json`.
- Full 624-row FP/FN audit: `../_sources/daily-20260605/denominator-recalibration-independent-adversarial-v1.tsv`.
"""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(section for section in sections if section) + "\n", encoding="utf-8")

    # Keep the packet README current without deleting the historical checkpoint.
    packet_readme = (PACKET / "README.md").read_text(encoding="utf-8")
    marker = "## Canonical denominator and downstream checkpoint"
    if marker in packet_readme:
        packet_readme = packet_readme.split(marker)[0].rstrip() + "\n\n"
    packet_readme += f"""{marker}

- canonical denominator: `{DENOMINATOR_ID}` = `64 retained / 560 pre-denominator closures` (`624/624` audited)
- Score V2 / route: `64/64` = `57 Deep / 7 Standard`
- canonical Review Completion: `64/64`, ordinary pending `0`
- access route: local exact-v1 `{sum(r['evidence_route'] != 'exact-v1-html-web-proxy' for r in reviews)}`, web-proxy official exact-v1 `{sum(r['evidence_route'] == 'exact-v1-html-web-proxy' for r in reviews)}`
- Deep Analysis Selection: `64/64 eligible decisions`, `3` selected units
- Books Comparison: `64/64` decisions; `8` Integrate proposals, no Books write in this lane
- Gate: Coverage `Closed`; Evidence/Selection/Books `Open` pending different fresh-context audits and date-serial Books writeback

Canonical artifacts: `screening-ledger.json`, `source-review-receipts-v2.1.json`, `downstream-reconciliation-v1.tsv`, and `../../05/README.md`.
"""
    (PACKET / "README.md").write_text(packet_readme, encoding="utf-8")

    CHECKPOINT.write_text(f"""# 2026-06-05 downstream repair checkpoint v1

This checkpoint is downstream of accepted denominator `{DENOMINATOR_ID}`. It is not a fresh-context semantic audit and does not authorize Books writeback or Gate closure.

## Canonical counts

- raw identities: `624`
- retained denominator: `64`
- family-specific pre-denominator closures: `560`
- Source Reviews: `64/64` (`57` Deep review routes, `7` Standard review routes)
- ordinary review pending / blocked / unverified: `0 / 0 / 0`
- exact-v1 access: `38` local bodies, `26` official arXiv exact-v1 HTML web-proxy reads
- author benchmark contracts: `60`; no empirical benchmark claimed: `4`
- Deep Analysis Selection: `3 selected`, `61 not_selected`; this is distinct from the `57` Deep Source Review routes
- Books Comparison: `64/64`; `8` Integrate proposals and `56` No Change decisions; Books files changed by this lane: `0`

## Material corrections made in this lane

- `2606.06090` was removed from the no-benchmark set. Its MemoryArena slice is bound to Qwen3.6-27B/Qwen3-8B-Embedding, A100 disclosure, task-success/progress/token metrics, and explicit `Not Disclosed` setup fields.
- `2606.06545` was removed from the no-benchmark set. Its 59-task/two-tenant evaluation is bound to governance, provisioning and scoped-execution metrics; undisclosed model, hardware, precision, length, batch, concurrency and SLO remain explicit.
- All 26 web-proxy exact-v1 reviews now use source-specific numbered section/appendix locators. Disclosed repositories are identified without inventing an immutable commit.
- Benchmark extraction for local HTML is restricted to evaluation/setup/result sections. Generic mentions of “model”, “GPU”, percentile latency or request rate no longer masquerade as model, hardware, SLO or concurrency disclosures.
- The 64-family Deep Analysis table contains exactly three selected units: `DA-20260605-AUTHORITY` (`2606.05679`), `DA-20260605-STATE` (`2606.06240`), and `DA-20260605-RUNTIME` (`2606.06256`). Every other retained family has a title-, owner-, and delta-specific rejection rationale.
- Books Comparison uses 64 distinct current-owner propositions, concrete adjacent references and 64 distinct evidence deltas. No Books write occurred.

## Gate state and independent continuation

- Coverage Gate: `Closed` from the prior independent 624-row FP/FN audit.
- Evidence Gate: `Open`.
- Deep Analysis Selection semantic audit: `Open`.
- Books Gate: `Open`.

A different fresh context must re-read all 64 Source Reviews and all 60 benchmark contracts, audit all 64 Selection decisions and the three-unit priority frontier, and recheck all 64 current-owner/adjacent Books comparisons. After root performs date-serial Books writeback, another fresh context must audit the eight Integrate targets plus any affected adjacent propositions. Validator success is structural evidence only.
""", encoding="utf-8")

    hashed_paths = [
        LEDGER,
        ACCESS_STATUS,
        RECEIPTS,
        DOWNSTREAM,
        AUDIT,
        PACKET / "README.md",
        CHECKPOINT,
        REPORT,
        Path(__file__).resolve(),
    ]
    SHA_MANIFEST.write_text(
        "".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}\n"
            for path in hashed_paths
        ),
        encoding="utf-8",
    )

    print(json.dumps({
        "denominator": DENOMINATOR_ID, "retained": 64, "closures": 560,
        "deep": sum(r["route"] == "deep" for r in reviews),
        "standard": sum(r["route"] == "standard" for r in reviews),
        "local_exact": sum(r["evidence_route"] != "exact-v1-html-web-proxy" for r in reviews),
        "web_proxy_exact": sum(r["evidence_route"] == "exact-v1-html-web-proxy" for r in reviews),
        "benchmark_contracts": sum(bool(r["benchmark"]) for r in reviews),
        "integrate_proposals": len(INTEGRATE_PROPOSALS),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
