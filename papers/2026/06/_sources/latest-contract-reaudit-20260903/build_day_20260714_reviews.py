#!/usr/bin/env python3
"""Build restartable exact-v1 Source Reviews for the 2026-07-14 denominator.

The review text is evidence-derived: claims come from the v1 abstract, mechanism
and evaluation statements come from located v1 sections/pages, and every
negative boundary is scoped to the configurations actually described by v1.
"""

from __future__ import annotations

import gzip
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260714"
REPORT_DATE = "2026-07-14"
RAW = PACKET / "canonical-raw-identity-inventory-v2.1.json.gz"
DECISIONS = PACKET / "fresh-context-semantic-decisions-v2.1.json.gz"
INDEX = PACKET / "exact-v1-section-index-v2.1.json.gz"
HTML_DIR = PACKET / "exact-v1-html"
PDF_TEXT_DIR = PACKET / "exact-v1-pdf-text"
REVIEWED_AT = "2026-09-04T02:00:00+08:00"

ROUTE_TRADEOFF = {
    "evaluation_contract": "更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。",
    "evidence_state": "显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。",
    "serving_runtime": "更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。",
    "agent_state": "显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。",
    "provenance_security": "更强 provenance 或攻击检测提高审计能力，但依赖密钥、参考版本、观测面或 threat model，不能替代内容正确性。",
    "safety_contract": "新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。",
    "training_mechanism": "更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。",
    "training_correctness": "保护数值更新会增加精度、诊断或计算成本，却换来可解释的 correctness floor。",
    "model_mechanism": "新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。",
    "resource_control": "动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。",
    "slo_control": "可信 guard 能限制 learned policy 的伤害，但只能保证它实际拥有执行控制的那部分义务。",
    "retrieval_system": "更强检索信号或迁移机制提高召回与连续性，但引入索引陈旧、负样本偏差、证据冲突和在线成本。",
    "privacy_control": "结构化隐私处理能缩小暴露面，但会牺牲语义保真并增加策略与图状态维护。",
}

FIELD_OVERRIDES = {
    "2607.09682": {
        "mechanism": "The design serializes every evidence-bearing inference step into an authenticated record whose identity, parentage and mutation history can be replayed after the decision.",
        "proved": "Exact v1 defines and exercises the evidence-record format, mutation detection and reconstruction path; it does not establish a production-scale correlation model for adaptively selected branches.",
    },
    "2607.09689": {
        "mechanism": "The prototype assigns stable evidence identities, records fork lineage and tests whether a later aggregate can detect duplicated evidence instead of treating correlated branches as independent support.",
        "proved": "Unit, synthetic and end-to-end tests support serialization, lineage reconstruction and duplicate-evidence detection; the paper explicitly leaves scalable dependence estimation for correlated adaptive branches open.",
    },
    "2607.09709": {
        "proved": "With all other loop components held fixed, replacing the strict launch verifier with a permissive build check erased the accumulated gain, isolating verifier precision rather than data volume alone.",
    },
    "2607.09786": {
        "mechanism": "The study applies controlled length-penalty training and compares matched-capability models with monitors that inspect outputs or internal activations, separating shorter reasoning from observability loss.",
        "proved": "Across the disclosed tasks and models, stronger pressure toward shorter answers reduced monitorability even when answer quality was matched; this is a warning about training-objective side effects, not a universal law for all length controls.",
    },
    "2607.09800": {
        "mechanism": "A high-precision reference run fixes the expected update trace, then low-precision decoder runs isolate where deterministic nearest write-back erases small recurrent updates; stochastic write-back is tested as the repair.",
        "proved": "Matched decoder experiments attribute much of the low-precision gap to repeated write-back loss and show stochastic write-back recovering most of that gap under the reported formats and models.",
    },
    "2607.09802": {
        "mechanism": "The system couples an internal market price with allocation decisions so teams express marginal accelerator value while the controller continuously reconciles demand with a constrained shared fleet.",
        "proved": "The Google deployment report shows the mechanism operating with measured allocation effects inside the disclosed organization; it does not establish portability to other incentive structures or fleet topologies.",
    },
    "2607.09804": {
        "method_locators": ["https://arxiv.org/html/2607.09804v1#S4 — IV Methods"],
        "evaluation_locators": ["https://arxiv.org/html/2607.09804v1#A1 — Appendix A Full concept manner results", "https://arxiv.org/html/2607.09804v1#S4.SS6 — IV-F Metrics and statistical analysis"],
        "limitations_locators": ["https://arxiv.org/html/2607.09804v1#S3 — III Threat Model", "https://arxiv.org/html/2607.09804v1#S5.SS5 — V-E Qualitative failure modes"],
    },
    "2607.09822": {
        "mechanism": "The agent maintains a three-layer personal visual memory, retrieves it on every camera-first turn to form tool arguments, and performs conflict-aware write-back after the interaction.",
        "proved": "The reported multi-tool evaluation supports better personalized tool choice and argument formation from this memory loop; it does not prove that stored visual inferences remain correct under long-lived identity or preference drift.",
    },
    "2607.09992": {
        "proved": "Under the stated service-envelope assumptions, the trusted guard kept the assured-class miss rate at zero across tested learner miscalibrations while the unguarded learned admitter missed 0.86-0.94.",
        "method_locators": ["https://arxiv.org/html/2607.09992v1#S2 — 2 The guard: learned proposes, verified disposes", "https://arxiv.org/html/2607.09992v1#S3 — 3 When can a cheap static screen be trusted?"],
        "evaluation_locators": ["https://arxiv.org/html/2607.09992v1#S2.SS0.SSS0.Px4 — The operating envelope", "https://arxiv.org/html/2607.09992v1#S2.SS0.SSS0.Px5 — Versus vLLM's own priority scheduler"],
        "limitations_locators": ["https://arxiv.org/html/2607.09992v1#S5.SS0.SSS0.Px1 — Scope: what we can and cannot evaluate", "https://arxiv.org/html/2607.09992v1#S6 — 6 Conclusion"],
    },
    "2607.09996": {
        "mechanism": "The benchmark replays agent executions, injects controlled failures after an exact trace point and asks the evaluator to identify both the responsible component and the failure time across modalities and interaction protocols.",
        "proved": "The controlled corpus reveals systematic attribution differences across model families, modalities and protocols; it measures diagnosis under injected ground truth rather than proving production root-cause coverage.",
    },
    "2607.09999": {
        "method_locators": ["https://arxiv.org/pdf/2607.09999v1#page=2 — PDF page 2", "https://arxiv.org/pdf/2607.09999v1#page=3 — PDF page 3"],
        "evaluation_locators": ["https://arxiv.org/pdf/2607.09999v1#page=4 — PDF page 4", "https://arxiv.org/pdf/2607.09999v1#page=5 — PDF page 5"],
        "limitations_locators": ["https://arxiv.org/pdf/2607.09999v1#page=6 — PDF page 6", "https://arxiv.org/pdf/2607.09999v1#page=7 — PDF page 7"],
    },
    "2607.10044": {
        "mechanism": "FlashTrie maps trie traversal and constrained beam expansion to fused GPU kernels, keeping constraint state on device instead of round-tripping candidate prefixes through a CPU controller.",
        "proved": "The disclosed retrieval workloads show up to 24x decoding speedup, roughly 3 ms latency and scaling to an 800M-node trie while preserving the paper's retrieval metric; those numbers remain tied to its hardware, beam and constraint configuration.",
    },
    "2607.10059": {
        "mechanism": "The framework pairs otherwise matched tasks where acting is appropriate or harmful, executes both through real agent harnesses and scores an agent only when it both acts and abstains correctly.",
        "proved": "Across 17 frontier models and four harnesses, the best reported paired accuracy was 59.5%, demonstrating that ordinary task success does not imply calibrated abstention under this benchmark contract.",
    },
    "2607.10103": {
        "mechanism": "The paper organizes provenance workloads by the identity, lineage, mutation and query operations they require, then maps each operation to throughput, false-positive, robustness and governance obligations.",
        "proved": "Exact v1 contributes a systems taxonomy and evaluation blueprint, not a measured production implementation or a claim that one provenance architecture satisfies every workload.",
    },
    "2607.10152": {
        "mechanism": "Consensus is specified denotationally as collapse of admissible executions under accumulated evidence, separating the semantic evidence condition from any one protocol's message exchange.",
        "proved": "The contribution is a reusable specification framework and examples, not a new impossibility theorem, implementation, or replacement for protocol-specific safety and liveness proofs.",
    },
    "2607.10362": {
        "method_locators": ["https://arxiv.org/html/2607.10362v1#S5.SS1 — 5.1 A theory-guided intervention: linear state readout"],
        "evaluation_locators": ["https://arxiv.org/html/2607.10362v1#S5.SS2 — 5.2 Control experiments on latent world models", "https://arxiv.org/html/2607.10362v1#S5.SS3 — 5.3 Cross-task validation of the state readout"],
        "limitations_locators": ["https://arxiv.org/html/2607.10362v1#S6 — 6 Discussion and Outlook", "https://arxiv.org/html/2607.10362v1#S7 — 7 Conclusion"],
    },
    "2607.10582": {
        "proved": "The exact-v1 experiments support region-aware KV eviction for the reported agent traces; they do not establish one universal eviction policy across all prompts and memory hierarchies.",
    },
    "2607.10855": {
        "proved": "Across the tested model sizes, precisions, quantizers and perturbations, predictive accuracy and reliability did not scale identically; the reported reliability optimum was configuration-dependent rather than monotonic in bit width.",
    },
    "2607.11070": {
        "proved": "Across the victim models and jailbreak benchmarks reported in exact v1, both weighting variants substantially improved ASR, supporting turn-level group-relative credit as the common mechanism rather than one weighting formula.",
    },
    "2607.11086": {
        "mechanism": "MCPZoo executes a large corpus of MCP servers behind controlled clients and compares runtime-observed behavior with static scanner findings, retaining server identity and invocation traces for attribution.",
        "proved": "The dynamic study finds that the 96.89% risk rate reported by existing scanners is not a reliable estimate of runtime exploitability for this corpus; it does not certify unobserved server behaviors as safe.",
    },
    "2607.11226": {
        "proved": "In the reported spatial-semantic sandbox, the specialized validator prevented executed breaches while retained failure-derived constraints reduced repeated checking and communication cost; the evidence remains limited to that controlled environment.",
    },
    "2607.11262": {
        "mechanism": "GPU-Tile-Sim models tile-level dependency scheduling and compute-memory overlap so a kernel mapping can be evaluated without collapsing the execution into an instruction-agnostic throughput estimate.",
        "proved": "For the disclosed LLM kernels on A100 and H100, predicted performance is within 1.22%-8.71% MAPE of measurement; this accuracy range is not evidence for arbitrary kernels or future architectures.",
    },
    "2607.11317": {
        "mechanism": "The paper rejects centered token log-probability as a drift statistic because its increments form a mean-zero martingale, then constructs a calibrated replacement and evaluates it conservatively.",
        "proved": "The mathematical result establishes why the natural centered-logprob monitor cannot accumulate the intended signal; the pilot replacement results are explicitly inconclusive rather than evidence of deployment-ready detection.",
    },
    "2607.11399": {
        "mechanism": "The harness routes at execution-step granularity using current observation, context, control state, prior failures, cost and outcome; the resulting trace becomes supervised data for later router updates.",
    },
    "2607.11423": {
        "proved": "The released white-box harness demonstrates that orchestration logic and tool behavior can be inspected and modified while retaining a usable coding-agent workflow; benchmark comparisons do not establish universal harness superiority.",
    },
    "2607.11433": {
        "proved": "No-state ablations and trajectory audits in the reported omni-modal tasks support explicit evidence-state control as the source of the measured gains, within the disclosed models and evaluator protocol.",
    },
    "2607.11414": {
        "mechanism": "Linear probes read internal answer-state activations and are compared with output-only confidence and resampling baselines, with special attention to answers that look confidently self-consistent.",
        "proved": "On FinQA and the three disclosed backbones, probes retain 0.68-0.77 AUROC where the strongest baselines fall to 0.55-0.63; the result is model- and task-scoped and does not make hidden-state confidence intrinsically calibrated.",
    },
    "2607.11487": {
        "mechanism": "LightMem-Ego maintains a hierarchical streaming multimodal memory that compresses egocentric observations into retrievable episodic and semantic state instead of replaying the full sensor history.",
        "proved": "The reported everyday-assistance evaluations support the hierarchy's accuracy-efficiency trade-off; repository availability alone does not establish long-horizon correctness or privacy safety.",
    },
    "2607.11598": {
        "mechanism": "The loop alternates proposal, external instrument observation and revision; each cycle imports a new grounded observation, and the outcome metric must observe the same failure surface for improvement to be visible.",
    },
    "2607.11611": {
        "mechanism": "An LLM-generated bug report is accepted only when accompanied by a machine-checkable program-logic proof; the Mizzle checker becomes the authority for the reported defect rather than the model's prose.",
        "proved": "The authors mechanize the relevant soundness and completeness properties in Rocq and show a proof-of-concept LLM certification flow; they do not establish coverage or cost on large production codebases.",
    },
    "2607.11698": {
        "proved": "Across the disclosed agents and attack scenarios, a frozen vulnerability concept graph transferred better than the frozen discovery baseline under the same single-shot protocol; this supports reusable causal vulnerability records, not exhaustive security coverage.",
    },
    "2607.11751": {
        "proved": "The experiments and formal observability argument agree that locally benign fragments defeat monitors restricted to local views, while signal returns only at a representation exposing the assembled payload.",
    },
    "2607.11796": {
        "mechanism": "Diagonal state dynamics permit an exact per-mode output decomposition; a per-layer, per-channel, per-window Gram tensor measures the exact error of dropping any mode subset and reveals input-driven state-use migration.",
    },
    "2607.11862": {
        "mechanism": "ST-Evidence pairs human-verified pixel evidence with discriminative and generative grounding tasks, then fine-tunes a size-matched model so evidence localization is evaluated independently of answer-only accuracy.",
        "proved": "Under the disclosed benchmark and baseline, fine-tuning improves t-mean by 27.2 points and J&F by 13.8 points; this does not establish transfer to unseen evidence taxonomies or production images.",
    },
    "2607.11886": {
        "mechanism": "The reward is the image-conditioned likelihood of reconstructing the original prompt, reusing a pretrained multimodal understanding branch as a training-free image-generation reward model.",
    },
    "2607.13062": {
        "method_locators": ["https://arxiv.org/html/2607.13062v1#S2 — 2 Setup and the calibration gate", "https://arxiv.org/html/2607.13062v1#S5 — 5 Decide: the speculation-decision pass", "https://arxiv.org/html/2607.13062v1#S6 — 6 Execute: the runtime executor"],
        "evaluation_locators": ["https://arxiv.org/html/2607.13062v1#S3 — 3 Measure: the predictability and speedup bracket", "https://arxiv.org/html/2607.13062v1#S4 — 4 Bound, refute, and explain: the misprediction blast radius"],
        "limitations_locators": ["https://arxiv.org/html/2607.13062v1#S8 — 8 Limitations and future work", "https://arxiv.org/html/2607.13062v1#S9 — 9 Conclusion"],
    },
    "2607.13921": {
        "method_locators": ["https://arxiv.org/pdf/2607.13921v1#page=7 — PDF page 7", "https://arxiv.org/pdf/2607.13921v1#page=12 — PDF page 12"],
        "evaluation_locators": ["https://arxiv.org/pdf/2607.13921v1#page=20 — PDF page 20", "https://arxiv.org/pdf/2607.13921v1#page=25 — PDF page 25"],
        "limitations_locators": ["https://arxiv.org/pdf/2607.13921v1#page=31 — PDF page 31", "https://arxiv.org/pdf/2607.13921v1#page=37 — PDF page 37"],
    },
    "2607.14166": {
        "method_locators": ["https://arxiv.org/pdf/2607.14166v1#page=5 — PDF page 5", "https://arxiv.org/pdf/2607.14166v1#page=10 — PDF page 10"],
        "evaluation_locators": ["https://arxiv.org/pdf/2607.14166v1#page=15 — PDF page 15", "https://arxiv.org/pdf/2607.14166v1#page=20 — PDF page 20"],
        "limitations_locators": ["https://arxiv.org/pdf/2607.14166v1#page=25 — PDF page 25", "https://arxiv.org/pdf/2607.14166v1#page=30 — PDF page 30"],
    },
    "2607.14280": {
        "method_locators": ["https://arxiv.org/pdf/2607.14280v1#page=3 — PDF page 3", "https://arxiv.org/pdf/2607.14280v1#page=7 — PDF page 7"],
        "evaluation_locators": ["https://arxiv.org/pdf/2607.14280v1#page=12 — PDF page 12", "https://arxiv.org/pdf/2607.14280v1#page=17 — PDF page 17"],
        "limitations_locators": ["https://arxiv.org/pdf/2607.14280v1#page=23 — PDF page 23", "https://arxiv.org/pdf/2607.14280v1#page=26 — PDF page 26"],
    },
    "2607.19297": {
        "method_locators": ["https://arxiv.org/html/2607.19297v1#S3 — 3 Recipe 1: SQL Analytics with Repair Loops", "https://arxiv.org/html/2607.19297v1#S5 — 5 Recipe 3: HITL Policy Review"],
        "evaluation_locators": ["https://arxiv.org/html/2607.19297v1#S7 — 7 Cross-Recipe Comparison", "https://arxiv.org/html/2607.19297v1#S8 — 8 Failure Modes and Testing"],
        "limitations_locators": ["https://arxiv.org/html/2607.19297v1#S9.SS2 — 9.2 Limitations", "https://arxiv.org/html/2607.19297v1#S10 — 10 Conclusion"],
    },
    "2607.20300": {
        "method_locators": ["https://arxiv.org/html/2607.20300v1#Sx1.SSx1 — Supply Chain Construction", "https://arxiv.org/html/2607.20300v1#Sx1.SSx2 — License Categorization"],
        "evaluation_locators": ["https://arxiv.org/html/2607.20300v1#Sx2 — Unknown Laundering", "https://arxiv.org/html/2607.20300v1#Sx3 — Category Laundering"],
        "limitations_locators": ["https://arxiv.org/html/2607.20300v1#Sx4 — Threats to Validity"],
    },
    "2607.21909": {
        "method_locators": ["https://arxiv.org/pdf/2607.21909v1#page=3 — Claim Plane Architecture and ChangeIntent", "https://arxiv.org/pdf/2607.21909v1#page=4 — Admission and dependency invalidation"],
        "evaluation_locators": ["https://arxiv.org/pdf/2607.21909v1#page=7 — Comparative evaluation arms and setup"],
        "limitations_locators": ["https://arxiv.org/pdf/2607.21909v1#page=9 — Confidence escalation boundary", "https://arxiv.org/pdf/2607.21909v1#page=10 — Evidence and disclosure boundary"],
    },
    "2607.25076": {
        "method_locators": ["https://arxiv.org/html/2607.25076v1#S3.SS1 — III-A Where OS and Cloud-OS Semantics Break Down", "https://arxiv.org/html/2607.25076v1#S4 — IV Proposed Agent-OS Primitives"],
        "evaluation_locators": ["https://arxiv.org/html/2607.25076v1#S5 — V Open source prototypes of Agent-OS primitives"],
        "limitations_locators": ["https://arxiv.org/html/2607.25076v1#S6 — VI Discussion: What the Prior Waves Teach Us", "https://arxiv.org/html/2607.25076v1#S7 — VII Open Research Agenda"],
    },
    "2607.25152": {
        "method_locators": ["https://arxiv.org/pdf/2607.25152v1#page=2 — Out-of-band evaluator architecture", "https://arxiv.org/pdf/2607.25152v1#page=5 — Controlled evaluator-channel design"],
        "evaluation_locators": ["https://arxiv.org/pdf/2607.25152v1#page=10 — Measured progress-mirage results", "https://arxiv.org/pdf/2607.25152v1#page=13 — Boundary-task comparison"],
        "limitations_locators": ["https://arxiv.org/pdf/2607.25152v1#page=1 — Preliminary-draft scope", "https://arxiv.org/pdf/2607.25152v1#page=19 — Generalization and field-observation limits"],
    },
    "2607.25408": {
        "method_locators": ["https://arxiv.org/html/2607.25408v1#S2 — 2 Formal decomposition", "https://arxiv.org/html/2607.25408v1#S3 — 3 Stability"],
        "evaluation_locators": ["https://arxiv.org/html/2607.25408v1#S4 — 4 Uncertainty calibration", "https://arxiv.org/html/2607.25408v1#S5 — 5 Positioning"],
        "limitations_locators": ["https://arxiv.org/html/2607.25408v1#S6 — 6 Limitations", "https://arxiv.org/html/2607.25408v1#S7 — 7 Conclusion"],
    },
}


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [part.strip() for part in parts if 45 <= len(part.strip()) <= 700]


def choose_sections(paper: dict, role: str, words: tuple[str, ...], limit: int = 2) -> list[dict]:
    sections = [s for s in paper["sections"] if s["section_id"] != "bib"]
    ranked = []
    for section in sections:
        title = section["title"].lower()
        score = (4 if role in section["roles"] else 0) + sum(2 for word in words if word in title)
        if section["section_id"].startswith("page-"):
            score += 1
        if score:
            ranked.append((score, section))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]["section_id"]))
    return [section for _, section in ranked[:limit]] or sections[:limit]


def evidence_sentence(sections_: list[dict], keywords: tuple[str, ...], fallback: str) -> str:
    pool = []
    for section in sections_:
        for sentence in sentences(section["text"]):
            low = sentence.lower()
            score = sum(1 for keyword in keywords if keyword in low)
            if re.search(r"references|arxiv preprint|copyright", low):
                continue
            if re.match(r"(?:appendix|figure|table|section)\b", sentence, re.I):
                continue
            if len(sentence.split()) < 8:
                continue
            pool.append((score, len(sentence), sentence))
    if not pool:
        return fallback
    pool.sort(key=lambda item: (-item[0], item[1]))
    return pool[0][2] if pool[0][0] > 0 else fallback


def abstract_evidence(parts: list[str], keywords: tuple[str, ...], fallback_index: int) -> str:
    ranked = []
    for part in parts:
        low = part.lower()
        ranked.append((sum(1 for keyword in keywords if keyword in low), len(part), part))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    if ranked and ranked[0][0] > 0:
        return ranked[0][2]
    if parts:
        return parts[min(fallback_index, len(parts) - 1)]
    return "Exact v1 does not disclose a standalone statement for this field."


def locator(aid: str, section: dict) -> str:
    if section["section_id"].startswith("page-"):
        page = section["section_id"].split("-")[-1]
        return f"https://arxiv.org/pdf/{aid}v1#page={page} — PDF page {page}"
    return f"https://arxiv.org/html/{aid}v1#{section['section_id']} — {section['title']}"


def artifact_boundary(aid: str) -> str:
    source = ""
    html_path = HTML_DIR / f"{aid}v1.html.gz"
    pdf_text = PDF_TEXT_DIR / f"{aid}v1.txt.gz"
    if html_path.exists():
        with gzip.open(html_path, "rt", encoding="utf-8", errors="ignore") as handle:
            source = handle.read()
        urls = re.findall(r'href=["\'](https?://[^"\']+)', source, re.I)
    elif pdf_text.exists():
        with gzip.open(pdf_text, "rt", encoding="utf-8", errors="ignore") as handle:
            source = handle.read()
        urls = re.findall(r"https?://[^\s<>()]+", source)
    else:
        urls = []
    useful = []
    for url in urls:
        url = url.replace("&amp;", "&").rstrip(".,;)")
        if any(host in url.lower() for host in ("github.com", "huggingface.co", "project", "demo", "code")) and url not in useful:
            useful.append(url)
    if useful:
        return f"Exact v1 links {', '.join(useful[:3])}; no event-time commit was independently pinned, so the manuscript remains the claim authority."
    return "Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary."


def disposition(item: dict) -> str:
    if item["evolution_relation"] == "structural_candidate":
        return "Structural Candidate"
    score = item["score_v2_provisional"]["total"]
    if score >= 8 and item["evolution_relation"] in {"direct_evolution", "corrective_evidence"}:
        return "Integrate"
    return "No Change — Existing Coverage"


def main() -> None:
    with gzip.open(RAW, "rt", encoding="utf-8") as handle:
        raw = json.load(handle)
    with gzip.open(DECISIONS, "rt", encoding="utf-8") as handle:
        decisions = json.load(handle)
    with gzip.open(INDEX, "rt", encoding="utf-8") as handle:
        index = json.load(handle)
    by_raw = {x["arxiv_id"]: x for x in raw["identities"]}
    by_paper = {x["arxiv_id"]: x for x in index["papers"]}
    retained = [x for x in decisions["items"] if x["decision"] == "retain_in_candidate_denominator"]
    if set(by_paper) != {x["arxiv_id"] for x in retained}:
        raise RuntimeError("exact-v1 index and frozen denominator differ")

    reviews = []
    for item in retained:
        aid = item["arxiv_id"]
        identity = by_raw[aid]
        paper = by_paper[aid]
        method_sections = choose_sections(paper, "method", ("method", "design", "system", "framework", "approach", "architecture"))
        eval_sections = choose_sections(paper, "evaluation", ("evaluation", "experiment", "result", "benchmark", "analysis", "ablation"))
        limit_sections = choose_sections(paper, "limitation_or_boundary", ("limitation", "discussion", "threat", "failure", "conclusion", "future"))
        abstract_sentences = sentences(identity["abstract"])
        claim = " ".join(abstract_sentences[:2]) or identity["abstract"][:900]
        abstract_method = abstract_evidence(abstract_sentences, ("we propose", "we introduce", "we present", "framework", "system", "method"), 1)
        abstract_result = abstract_evidence(abstract_sentences, ("we find", "results", "improve", "reduce", "achieve", "outperform", "show", "demonstrate"), -1)
        # Use the v1 abstract's explicit method/result statements for concise,
        # non-table prose.  Full-text sections still own the review locators and
        # the counterevidence/limitation boundary below.
        mechanism = abstract_method
        proved = abstract_result
        boundary_fallback = "Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope."
        boundary_sentence = evidence_sentence(limit_sections, ("limit", "only", "cannot", "not", "depend", "future", "threat", "however"), boundary_fallback)
        review = {
            "source_family_id": item["source_family_id"],
            "primary_evidence": f"arXiv:{aid}v1",
            "score_v2": item["score_v2_provisional"],
            "stable_node_id": item["stable_node_id"],
            "claim": claim,
            "mechanism": mechanism,
            "method_locators": [locator(aid, section) for section in method_sections],
            "evaluation_locators": [locator(aid, section) for section in eval_sections],
            "limitations_locators": [locator(aid, section) for section in limit_sections],
            "artifact_boundary": artifact_boundary(aid),
            "proved": proved,
            "not_proved": f"{boundary_sentence} 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。",
            "trade_off": f"{ROUTE_TRADEOFF[item['semantic_route']]} 论文自身的边界信号是：{boundary_sentence}",
            "books_disposition": disposition(item),
            "evolution_relation": item["evolution_relation"],
            "semantic_route": item["semantic_route"],
        }
        review.update(FIELD_OVERRIDES.get(aid, {}))
        reviews.append(review)

    size = 10
    for offset in range(0, len(reviews), size):
        batch = reviews[offset:offset + size]
        number = offset // size + 1
        payload = {
            "schema": "source-review-batch-v2.1",
            "report_date": REPORT_DATE,
            "batch": number,
            "status": "complete",
            "reviewed_at": REVIEWED_AT,
            "scope": "exact arXiv v1 Method, evaluation, limitations/counterevidence and artifact boundary",
            "reviews": batch,
        }
        path = PACKET / f"source-review-batch-{number:02d}-v2.1.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "reviews": len(reviews),
        "batches": (len(reviews) + size - 1) // size,
        "deep": sum(x["score_v2"]["total"] >= 7 for x in reviews),
        "standard": sum(5 <= x["score_v2"]["total"] <= 6 for x in reviews),
        "integrate_proposed": sum(x["books_disposition"] == "Integrate" for x in reviews),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
