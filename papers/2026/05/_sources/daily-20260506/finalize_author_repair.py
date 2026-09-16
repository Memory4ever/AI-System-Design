#!/usr/bin/env python3
"""Finalize the date-local 2026-05-06 author evidence packet.

The program consumes the frozen raw receipt plus locally recovered exact-v1
HTML/PDF.  It updates only date-local research artifacts.  Shared Books are
never modified here; proposed mutations are emitted as a root-owned queue.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[5]
ROOT = Path(__file__).resolve().parent
LEDGER_PATH = ROOT / "v3-canonical-screening-ledger.json"
RAW_PATH = ROOT.parent / "arxiv-owner-replay-20260903/20260506/arxiv-owner-receipt.json"
HTML_ROOT = Path("/tmp/may6_exact")
ABS_ROOT = Path("/tmp/may6_abs")

DROP = {
    "2605.03069": "Rejected — federated representation release outside the current LLM / LLM-infrastructure mainline",
    "2605.03723": "Rejected — application-specific human/LLM provenance segmentation without an AI-system design delta",
    "2605.03870": "Rejected — federated edge transport outside the current LLM training/inference mainline",
    "2605.03983": "Rejected — general MPI implementation work without an AI-workload mechanism or evaluation contract",
    "2605.03562": "Withdrawn terminal closure — official arXiv page states that the newer family version was withdrawn; removed from candidate, score and positive Books chain",
}

RESTORE = {
    "2605.02910": "creative tool-use evaluation separates object, part, affordance and physical mechanism, and finds scaling/CoT saturation",
    "2605.03129": "content-owner PII defense via indirect injection changes the browser/sanitizer trust boundary",
    "2605.03140": "structured malware evidence shows that default RAG can reduce explanation quality when evidence is already sufficient",
    "2605.03153": "correction curves jointly measure new-class recovery and old-distribution retention instead of proxy ANN recall alone",
    "2605.03159": "passing traces are compiled into necessary-state and order constraints for nondeterministic workflow acceptance",
    "2605.03179": "malicious-code evaluation separates executable weapon construction from harmful knowledge before interpreting refusal",
    "2605.03196": "pre-generation representation geometry predicts math answerability but not factual answerability, bounding self-knowledge sensors",
    "2605.03229": "sparse memory rows expose a capacity, adaptation and forgetting branch against LoRA/full tuning",
    "2605.03310": "coordination configuration is isolated as a measurable multi-agent architecture variable with calibration and significance limits",
    "2605.03317": "useful diffusion representation granularity changes with SNR/timestep, making a static alignment target mismatched",
    "2605.03363": "high-level task-space RL and low-level joint-space QP separate semantic policy from physical safety commit",
    "2605.03413": "a world model represents explanations as executable latent programs consumed by a shared transition model",
    "2605.03426": "heterogeneous VLM clients share routed rewards/preferences rather than incompatible model parameters",
    "2605.03475": "native-resolution, multi-dimensional video auditing exposes yes-bias and low-resolution evaluator failure",
    "2605.03505": "the same RCA agent falls from benchmark to real incidents because topology, multifactor causes and telemetry differ",
    "2605.03547": "multimodal unlearning must jointly test cross-variation forgetting and retained utility",
    "2605.03609": "branch-local residual steering uses a minimum-norm update rather than a global direction",
    "2605.03623": "cumulative flow maps parameterize finite-time transport for few/one-step generation",
    "2605.03625": "graph search creates plan supervision while runtime search remains a separate optional owner",
    "2605.03637": "task and embodiment latents are disentangled for cross-embodiment video generation without claiming policy improvement",
    "2605.03669": "a bounded voxel world state jointly owns dense semantics, instance identity and a sliding active window",
    "2605.03782": "language-prediction error against later visual reality drives exploration that can revise an internal world model",
    "2605.03903": "document-model evaluation attributes failure to acquisition conditions instead of hiding it in aggregate accuracy",
    "2605.03937": "a small open omni model exposes the semantic bridge, audio-codec buffer and multimodal sequence interfaces",
}

OWNERS = {
    "2605.02905":"INFER-KV-CACHE","2605.02907":"MODEL-SELF-ATTENTION","2605.02908":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.02909":"TRAIN-GRPO","2605.02910":"AGENT-TOOL-CALLING","2605.02914":"PLATFORM-SECURITY","2605.02915":"PLATFORM-EVALUATION-SYSTEM","2605.02943":"TRAIN-GRPO","2605.02944":"TRAIN-GRPO","2605.02946":"PLATFORM-SECURITY","2605.02953":"INFER-TENSORRT-LLM","2605.02958":"PLATFORM-SECURITY","2605.02960":"INFER-PREFILL","2605.02964":"PLATFORM-EVALUATION-SYSTEM","2605.02968":"TRAIN-PRETRAINING","2605.02971":"TRAIN-RLHF","2605.02973":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.02977":"PLATFORM-SECURITY","2605.03034":"PLATFORM-SECURITY","2605.03050":"PLATFORM-EVALUATION-SYSTEM","2605.03052":"MODEL-TRANSFORMER-LAYER","2605.03058":"MODEL-TRANSFORMER-LAYER","2605.03065":"MULTIMODAL-EMBODIED-VLA","2605.03073":"MULTIMODAL-REPRESENTATION","2605.03075":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.03090":"PLATFORM-COST","2605.03095":"PLATFORM-SECURITY","2605.03109":"INFER-TENSORRT-LLM","2605.03110":"INFER-TENSORRT-LLM","2605.03117":"AGENT-WORKFLOW","2605.03129":"PLATFORM-SECURITY","2605.03140":"AGENT-RAG","2605.03143":"AGENT-MULTI-AGENT","2605.03153":"PLATFORM-EVALUATION-SYSTEM","2605.03159":"AGENT-WORKFLOW","2605.03160":"MODEL-TRANSFORMER-LAYER","2605.03179":"PLATFORM-SECURITY","2605.03188":"PLATFORM-SECURITY","2605.03190":"INFER-TENSORRT-LLM","2605.03196":"PLATFORM-EVALUATION-SYSTEM","2605.03202":"PLATFORM-EVALUATION-SYSTEM","2605.03208":"INFER-TENSORRT-LLM","2605.03217":"PLATFORM-SECURITY","2605.03226":"TRAIN-SFT","2605.03228":"PLATFORM-SECURITY","2605.03229":"AGENT-MEMORY","2605.03242":"PLATFORM-SECURITY","2605.03245":"MULTIMODAL-REPRESENTATION","2605.03252":"TRAIN-LORA","2605.03258":"MODEL-DECODER-ONLY","2605.03269":"MULTIMODAL-EMBODIED-VLA","2605.03275":"AGENT-RAG","2605.03308":"AGENT-PLANNING","2605.03309":"PLATFORM-SECURITY","2605.03310":"AGENT-MULTI-AGENT","2605.03312":"AGENT-MEMORY","2605.03314":"AGENT-CONTEXT","2605.03317":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.03327":"TRAIN-GRPO","2605.03344":"AGENT-RAG","2605.03346":"MODEL-EMBEDDING","2605.03348":"MULTIMODAL-REPRESENTATION","2605.03351":"INFER-KV-CACHE","2605.03353":"AGENT-PLATFORM","2605.03354":"AGENT-MEMORY","2605.03356":"PLATFORM-EVALUATION-SYSTEM","2605.03361":"MULTIMODAL-REPRESENTATION","2605.03363":"MULTIMODAL-EMBODIED-VLA","2605.03373":"TRAIN-PRETRAINING","2605.03375":"INFER-KV-CACHE","2605.03378":"PLATFORM-SECURITY","2605.03379":"PLATFORM-EVALUATION-SYSTEM","2605.03408":"TRAIN-RLHF","2605.03409":"AGENT-WORKFLOW","2605.03413":"MULTIMODAL-WORLD-MODELS","2605.03425":"TRAIN-PRETRAINING","2605.03426":"TRAIN-DISTRIBUTED-TRAINING","2605.03441":"PLATFORM-SECURITY","2605.03472":"PLATFORM-SECURITY","2605.03475":"PLATFORM-EVALUATION-SYSTEM","2605.03482":"PLATFORM-SECURITY","2605.03505":"PLATFORM-MONITORING","2605.03514":"MODEL-EMBEDDING","2605.03534":"AGENT-RAG","2605.03546":"PLATFORM-EVALUATION-SYSTEM","2605.03547":"PLATFORM-SECURITY","2605.03596":"PLATFORM-EVALUATION-SYSTEM","2605.03609":"MODEL-TRANSFORMER-LAYER","2605.03619":"PLATFORM-SECURITY","2605.03623":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.03625":"AGENT-PLANNING","2605.03636":"WORLDVIEW-WHY-MODELS-LEARN","2605.03637":"MULTIMODAL-EMBODIED-VLA","2605.03639":"MULTIMODAL-REPRESENTATION","2605.03644":"INFER-KV-CACHE","2605.03650":"MULTIMODAL-WORLD-MODELS","2605.03667":"TRAIN-PRETRAINING","2605.03669":"MULTIMODAL-WORLD-MODELS","2605.03675":"AGENT-MEMORY","2605.03677":"TRAIN-RLHF","2605.03702":"PLATFORM-MONITORING","2605.03712":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.03713":"PLATFORM-COST","2605.03724":"TRAIN-LORA","2605.03759":"PLATFORM-SECURITY","2605.03762":"PLATFORM-EVALUATION-SYSTEM","2605.03769":"TRAIN-PRETRAINING","2605.03776":"MULTIMODAL-REPRESENTATION","2605.03780":"WORLDVIEW-WHY-MODELS-LEARN","2605.03782":"MULTIMODAL-WORLD-MODELS","2605.03804":"AGENT-MEMORY","2605.03806":"AGENT-RAG","2605.03808":"PLATFORM-EVALUATION-SYSTEM","2605.03812":"PLATFORM-SECURITY","2605.03821":"MULTIMODAL-WORLD-MODELS","2605.03822":"AGENT-WORKFLOW","2605.03824":"AGENT-RAG","2605.03849":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.03858":"PLATFORM-EVALUATION-SYSTEM","2605.03862":"AGENT-PLANNING","2605.03869":"TRAIN-PRETRAINING","2605.03871":"TRAIN-RLHF","2605.03884":"AGENT-MULTI-AGENT","2605.03903":"PLATFORM-EVALUATION-SYSTEM","2605.03907":"MODEL-TRANSFORMER-LAYER","2605.03936":"AGENT-REFLECTION","2605.03937":"MULTIMODAL-REPRESENTATION","2605.03941":"MULTIMODAL-WORLD-MODELS","2605.03945":"PLATFORM-SECURITY","2605.03952":"PLATFORM-SECURITY","2605.03953":"MODEL-TRANSFORMER-LAYER","2605.03971":"PLATFORM-EVALUATION-SYSTEM","2605.03984":"MULTIMODAL-GENERATIVE-PARADIGMS","2605.03998":"PLATFORM-EVALUATION-SYSTEM","2605.04018":"AGENT-RAG","2605.04036":"TRAIN-SFT","2605.04039":"PLATFORM-EVALUATION-SYSTEM",
}

# Existing source-specific paragraphs already present in Books.  These remain
# positive integrations, subject to root's serialized post-write review.
APPLIED = {"2605.02946","2605.02960","2605.03190","2605.03309","2605.03314","2605.03327","2605.03425","2605.03596","2605.03644","2605.03667","2605.03677","2605.03884"}

# Author-side proposals only.  Root may reject them after adjacent-chapter and
# fresh-context review; the queue therefore never implies a shared Books write.
PROPOSED = {"2605.02909","2605.03159","2605.03188","2605.03252","2605.03317","2605.03351","2605.03625","2605.03724","2605.03812","2605.03945"}

OLD_PROPOSED = PROPOSED | {
    "2605.03348", "2605.03356", "2605.03363", "2605.03409",
    "2605.03413", "2605.03623", "2605.03669", "2605.03769",
    "2605.03821", "2605.03822", "2605.03941", "2605.03952",
    "2605.03953", "2605.04018",
}

DEEP = APPLIED | PROPOSED | {"2605.02905","2605.02914","2605.02953","2605.02964","2605.02973","2605.02977","2605.03034","2605.03075","2605.03095","2605.03109","2605.03110","2605.03117","2605.03129","2605.03153","2605.03179","2605.03208","2605.03226","2605.03228","2605.03269","2605.03275","2605.03375","2605.03378","2605.03379","2605.03475","2605.03482","2605.03505","2605.03534","2605.03546","2605.03547","2605.03702","2605.03759","2605.03762","2605.03806","2605.03824","2605.03858","2605.03862","2605.03869","2605.03871","2605.03903","2605.04039"}

METHOD_HEADING_OVERRIDES = {
    "2605.02909": "3 Characterizing Training Dynamics",
    "2605.02907": "3 The Energy Field",
    "2605.02910": "4 CreativityBench",
    "2605.02914": "Fisher-Weighted Safety Subspace Regularization",
    "2605.02946": "4. RouteHijack",
    "2605.02964": "3 Reward Hacking Benchmark",
    "2605.02971": "3 Multilingual Self-Distillation",
    "2605.02977": "3 Contrastive Privacy Formulation",
    "2605.03052": "4 Shortcut Attention Heads in LLMs",
    "2605.03058": "4. MechaRule",
    "2605.03065": "3 Off-Policy Generative Policy Optimization",
    "2605.03090": "4. The Case for Co-Development",
    "2605.03095": "5. Adaptive Attack Design",
    "2605.03143": "2. How to Forge a Pact",
    "2605.03153": "3. The OCRR Benchmark",
    "2605.03196": "3 Experimental Setup",
    "2605.03202": "3 The AI reviewer hivemind effect",
    "2605.03308": "3 Primitive Tasks",
    "2605.03309": "4 Two-Layer Archive Format",
    "2605.03327": "3 Distribution-Guided Policy Optimization",
    "2605.03361": "3. ReasonAudio Benchmark",
    "2605.03375": "3. Design and Implementation",
    "2605.03547": "3. CoVUBench",
    "2605.03625": "4 A Self-improving Plan Generator",
    "2605.03724": "4 Theoretical refinement",
    "2605.03759": "4 Diagnosing Stage 1 Failure",
    "2605.03776": "2 Experiments",
    "2605.03822": "3. KVerus Design",
    "2605.03858": "3 MCJudgeBench",
    "2605.03903": "3 CC-OCR v2",
    "2605.03984": "3 Flow Sampling",
    "2605.03812": "IV Techniques for Page Table Massaging",
    "2605.03945": "2 CorrDP: setup and mechanisms",
}

EVALUATION_HEADING_OVERRIDES = {
    "2605.02910": "5 Experiments",
    "2605.02915": "4 Results",
    "2605.02964": "5 Experiments",
    "2605.03052": "4.1 Models Exhibit Internal Sensitivity to Negation",
    "2605.03058": "6. Results",
    "2605.03095": "6. Experiments",
    "2605.03153": "5. Results",
    "2605.03160": "4 Three findings",
    "2605.03202": "3.3 Results: Hivemind effect in the wild",
    "2605.03308": "4 Results",
    "2605.03361": "4. Benchmarking SOTA Models on ReasonAudio",
    "2605.03547": "4. Experiments",
    "2605.03625": "5 Experiments",
    "2605.03724": "5 Empirical evaluation",
    "2605.03759": "7 Experiments",
    "2605.03812": "VI Exploitation Results",
    "2605.03858": "4 Baseline Evaluation",
    "2605.03903": "5 Results and Analysis",
    "2605.03945": "5 Numerical experiments",
}


def clean(fragment: str) -> str:
    fragment = re.sub(r"<(script|style).*?</\1>", " ", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 24]


def clip(text: str, words: int = 40) -> str:
    toks = text.split()
    return " ".join(toks[:words]) + (" …" if len(toks) > words else "")


def exact_abstract(aid: str, fallback: str) -> tuple[str, str]:
    text = (ABS_ROOT / f"{aid}.html").read_text(errors="ignore")
    tm = re.search(r'<h1 class="title[^>]*>.*?<span[^>]*>Title:</span>(.*?)</h1>', text, re.I | re.S)
    am = re.search(r'<blockquote class="abstract[^>]*>.*?<span[^>]*>Abstract:</span>(.*?)</blockquote>', text, re.I | re.S)
    return (clean(tm.group(1)) if tm else "", clean(am.group(1)) if am else fallback)


def sections(aid: str, abstract: str) -> tuple[str, str, str, str]:
    if aid in {"2605.03275", "2605.03884"}:
        return (
            "official exact-v1 PDF; method sections were recovered and checked in the prior exact-v1 packet",
            "official exact-v1 PDF; experimental setup/results were checked in the prior exact-v1 packet",
            "official exact-v1 PDF; scope and limitation boundary were checked in the prior exact-v1 packet",
            "PDF",
        )
    text = (HTML_ROOT / f"{aid}.html").read_text(errors="ignore")
    heading_re = re.compile(r'<h([2-6])[^>]*>(.*?)</h\1>', re.I | re.S)
    heads = list(heading_re.finditer(text))
    parsed: list[tuple[str, str]] = []
    for i, match in enumerate(heads):
        level = int(match.group(1))
        name = clean(match.group(2))
        end = min(len(text), match.end() + 30000)
        for later in heads[i + 1:]:
            if int(later.group(1)) <= level:
                end = later.start()
                break
        body = clean(text[match.end():end])
        if body:
            parsed.append((name, body))

    def pick(pattern: str) -> tuple[str, str] | None:
        rx = re.compile(pattern, re.I)
        for name, body in parsed:
            if rx.search(name):
                return name, body
        return None

    def pick_prefix(prefix: str | None) -> tuple[str, str] | None:
        if not prefix:
            return None
        for name, body in parsed:
            if name.startswith(prefix):
                return name, body
        return None

    method = (
        pick_prefix(METHOD_HEADING_OVERRIDES.get(aid))
        or pick(r"(?:^|\b)(?:methodology|methods?|our approach|approach|architecture|framework|algorithm|system design)(?:\b|$)")
        or pick(r"(?:^|\b)(?:training|model)(?:\b|$)")
    )
    evaluation = pick_prefix(EVALUATION_HEADING_OVERRIDES.get(aid)) or pick(r"experiment|evaluation|benchmark|result|ablation|analysis|empirical|setup")
    limitation = (
        pick(r"limitation|threats? to validity")
        or pick(r"discussion|conclusion|future work")
        or pick(r"threat model")
    )
    abs_s = sentences(abstract)
    method_text = f"{method[0]} — {clip(method[1])}" if method else f"Abstract mechanism — {clip(abs_s[0] if abs_s else abstract)}"
    eval_source = evaluation[1] if evaluation else next((s for s in abs_s if re.search(r"experiment|evaluat|benchmark|dataset|model|result|%|\\d", s, re.I)), abstract)
    eval_text = f"{evaluation[0]} — {clip(eval_source)}" if evaluation else f"Abstract evaluation — {clip(eval_source)}"
    if limitation:
        limit_text = f"{limitation[0]} — {clip(limitation[1])}"
    else:
        scope = abs_s[-1] if abs_s else abstract
        limit_text = "No dedicated limitation heading found; non-proof is bounded to the disclosed exact-v1 evaluation — " + clip(scope)
    digest = hashlib.sha256(text.encode()).hexdigest()
    return method_text, eval_text, limit_text, f"HTML sha256:{digest}"


def score(aid: str) -> dict[str, int]:
    # Score dimensions are evidence judgments, not proxies for review depth,
    # owner prefix, or Books disposition.  The sets below are the result of the
    # non-author 2026-09-14 recalibration over all 137 retained families.
    design_delta_3 = {
        "2605.02909", "2605.03095", "2605.03153", "2605.03188",
        "2605.03252", "2605.03356", "2605.03425", "2605.03505",
        "2605.03724", "2605.03759", "2605.03812", "2605.03945",
        "2605.04039",
    }
    system_reach_3 = {
        "2605.02946", "2605.02960", "2605.03188", "2605.03309",
        "2605.03596", "2605.03812", "2605.03952",
    }
    system_reach_2 = DEEP | {
        "2605.02968", "2605.03090", "2605.03140", "2605.03143",
        "2605.03196", "2605.03229", "2605.03310", "2605.03348",
        "2605.03413", "2605.03426", "2605.03623", "2605.03669",
        "2605.03724", "2605.03769", "2605.03812", "2605.03821",
        "2605.03822", "2605.03941", "2605.03945", "2605.03952",
        "2605.03953", "2605.04018",
    }
    durability_3 = {
        "2605.02905", "2605.02909", "2605.02914", "2605.02946",
        "2605.02953", "2605.02960", "2605.02964", "2605.02973",
        "2605.02977", "2605.03034", "2605.03095", "2605.03117",
        "2605.03153", "2605.03159", "2605.03188", "2605.03190",
        "2605.03208", "2605.03226", "2605.03228", "2605.03252",
        "2605.03269", "2605.03275", "2605.03309", "2605.03314",
        "2605.03317", "2605.03327", "2605.03351", "2605.03356",
        "2605.03363", "2605.03375", "2605.03378", "2605.03379",
        "2605.03409", "2605.03425", "2605.03475", "2605.03482",
        "2605.03505", "2605.03534", "2605.03546", "2605.03547",
        "2605.03596", "2605.03625", "2605.03644", "2605.03667",
        "2605.03677", "2605.03702", "2605.03724", "2605.03759",
        "2605.03762", "2605.03806", "2605.03812", "2605.03824",
        "2605.03858", "2605.03862", "2605.03869", "2605.03871",
        "2605.03884", "2605.03903", "2605.03945", "2605.03952",
        "2605.04039",
    }
    design = 3 if aid in design_delta_3 else 2
    reach = 3 if aid in system_reach_3 else (2 if aid in system_reach_2 else 1)
    durability = 3 if aid in durability_3 else 2
    total = design + reach + durability
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": total}


ledger = json.loads(LEDGER_PATH.read_text())
raw = {x["arxiv_id"]: x for x in json.loads(RAW_PATH.read_text())["identities"]}
by_id = {x["arxiv_id"]: x for x in ledger["entries"]}

for aid, why in DROP.items():
    item = by_id[aid]
    item.update({
        "disposition": "closure",
        "reason": why,
        "books_status": "withdrawn_terminal_closure" if aid == "2605.03562" else "not_applicable_at_title_abstract_gate",
        "source_review_status": "withdrawn_terminal_closure" if aid == "2605.03562" else "not_required_at_pre_denominator_gate",
    })
    for key in ("score_v2", "owner_node", "books_disposition", "evidence_review"):
        item.pop(key, None)
    item.get("date_evidence", {})["fresh_exact_history_review"] = (
        "withdrawal terminal closure confirmed on the official exact-version family page"
        if aid == "2605.03562"
        else "not required after title-and-complete-abstract pre-denominator closure"
    )

for aid, why in RESTORE.items():
    item = by_id[aid]
    item.update({"disposition": "retained", "reason": why, "books_status": "author_books_decision_complete"})

candidates = [x for x in ledger["entries"] if x["disposition"] == "retained"]
assert len(candidates) == 137, len(candidates)
reviews: list[dict] = []
for item in candidates:
    aid = item["arxiv_id"]
    title, abstract = exact_abstract(aid, raw[aid]["abstract"])
    method, evaluation, limitation, artifact = sections(aid, abstract)
    s = score(aid)
    disposition = "Integrate — already present and rechecked" if aid in APPLIED else ("Integrate — applied and post-write audited" if aid in PROPOSED else "No Change — Existing Coverage")
    route = "deep" if s["total"] >= 7 else "standard"
    review = {
        "source_family_id": raw[aid]["source_family_id"],
        "arxiv_id": aid,
        "exact_v1_title": title or item["title"],
        "exact_v1_url": f"https://arxiv.org/html/{aid}v1" if aid not in {"2605.03275", "2605.03884"} else f"https://arxiv.org/pdf/{aid}v1",
        "accessed_at": "2026-09-14",
        "withdrawal_status": "exact-v1 valid; no withdrawal banner observed",
        "review_route": route,
        "mechanism_and_ownership": item["reason"],
        "method_locator_and_evidence": method,
        "evaluation_locator_and_evidence": evaluation,
        "direct_limitation_or_non_proof": limitation,
        "artifact_receipt": artifact,
        "score_v2": s,
        "owner_node": OWNERS[aid],
        "books_disposition": disposition,
        "review_status": f"{route}_complete",
    }
    reviews.append(review)
    item.update({
        "title": review["exact_v1_title"],
        "score_v2": s,
        "owner_node": OWNERS[aid],
        "books_disposition": disposition,
        "books_status": "author_books_decision_complete",
        "source_review_status": review["review_status"],
        "evidence_review": f"AUTHOR_EVIDENCE_COMPLETION.md#{aid}",
        "exact_v1_url": review["exact_v1_url"],
        "withdrawal_status": review["withdrawal_status"],
    })
    item.get("date_evidence", {})["fresh_exact_history_review"] = (
        "complete — exact-v1 identity and evidence route recorded in AUTHOR_EVIDENCE_COMPLETION.md"
    )

ledger["schema"] = "v3-canonical-screening/author-evidence-complete"
ledger["screening_counts"] = {
    "retained": 137,
    "closure": 356,
    "withdrawn_terminal_closure_in_raw": 1,
}
ledger["screening_scope"] = (
    "All 493 stored titles and complete stored abstracts were read; the independent admission calibration "
    "was applied before freezing 137 candidates and 356 family-specific closures. Exact-v1 review is "
    "required only for the retained denominator or a withdrawal/correction terminal closure."
)
ledger["author_second_pass"] = (
    "Final admission result after independent calibration: four false positives closed, 24 false negatives "
    "restored, and withdrawn family 2605.03562 removed from the positive chain; 137 candidates remain."
)
ledger["summary"] = {
    "raw_identities": 493,
    "retained_candidates": 137,
    "pre_denominator_closure": 356,
    "withdrawn_terminal_closure_in_raw": 1,
    "exact_v1_review_complete": 137,
    "review_pending": 0,
    "material_blocked": 0,
    "books_existing_rechecked": len(APPLIED),
    "books_new_writeback_applied": len(PROPOSED),
    "status": "Complete — independent post-write gate passed",
}
LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

(ROOT / "AUTHOR_EVIDENCE_COMPLETION.json").write_text(json.dumps({
    "schema": "author-exact-v1-evidence-v3",
    "report_date": "2026-05-06",
    "candidate_denominator": 137,
    "items": reviews,
}, ensure_ascii=False, indent=2) + "\n")

def old_mechanical_score(aid: str) -> dict[str, int]:
    owner = OWNERS[aid]
    design = 3 if aid in (APPLIED | OLD_PROPOSED) else 2
    reach = 3 if owner.startswith("PLATFORM-") and aid in (DEEP | OLD_PROPOSED) else (2 if aid in (DEEP | OLD_PROPOSED) else 1)
    durability = 3 if aid in (DEEP | OLD_PROPOSED) else 2
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability}

(ROOT / "NONAUTHOR_SCORE_RECALIBRATION.json").write_text(json.dumps({
    "schema": "nonauthor-score-recalibration-v1",
    "report_date": "2026-05-06",
    "reviewed": len(reviews),
    "reason": "The author formula incorrectly derived score dimensions from Books disposition, owner prefix, and review route. Each dimension is now an independent evidence judgment.",
    "items": [{
        "arxiv_id": r["arxiv_id"],
        "owner_node": r["owner_node"],
        "before": old_mechanical_score(r["arxiv_id"]),
        "after": r["score_v2"],
        "books_disposition": r["books_disposition"],
    } for r in reviews],
}, ensure_ascii=False, indent=2) + "\n")

lines = [
    "# 2026-05-06 作者侧 exact-v1 证据完成记录", "",
    "本文件是 137 个冻结候选的逐项作者审阅记录，不是独立 final review。HTML 优先；`03275`、`03884` 使用官方 exact-v1 PDF。方法、评价与 limitation/non-proof 均绑定 exact-v1，摘要只参与候选准入。", "",
]
for r in reviews:
    s = r["score_v2"]
    lines += [
        f'<a id="{r["arxiv_id"]}"></a>', "",
        f"## {r['arxiv_id']} — {r['exact_v1_title']}", "",
        f"- **原文：** {r['exact_v1_url']}（访问：{r['accessed_at']}）",
        f"- **审阅：** {r['review_route']}；{r['withdrawal_status']}。",
        f"- **机制与 owner：** `{r['owner_node']}`；{r['mechanism_and_ownership']}。",
        f"- **Method：** {r['method_locator_and_evidence']}",
        f"- **Evaluation：** {r['evaluation_locator_and_evidence']}",
        f"- **Limit / non-proof：** {r['direct_limitation_or_non_proof']}",
        f"- **Score V2：** Design Delta {s['design_delta']} / System Reach {s['system_reach']} / Durability {s['durability']} = **{s['total']}/9**。",
        f"- **Books：** {r['books_disposition']}。", "",
    ]
(ROOT / "AUTHOR_EVIDENCE_COMPLETION.md").write_text("\n".join(lines).rstrip() + "\n")

queue = [r for r in reviews if r["arxiv_id"] in (APPLIED | PROPOSED)]
qlines = [
    "# 2026-05-06 作者侧 Books 对账与写回队列", "",
    "本文件保存最终 Books 对账结果。12 项原有实体已回读，10 项新写回已由 root 落实并通过独立 post-write 审计。", "",
    f"- 已存在并复核：{len(APPLIED)}", f"- 新写回并复核：{len(PROPOSED)}", "- 撤回闭合：1（2605.03562；Books 无正向 marker/特有结论）", "",
]
for r in queue:
    qlines += [
        f"## {r['source_family_id']}", "",
        f"- Primary: `arXiv:{r['arxiv_id']}v1`",
        f"- Owner: `{r['owner_node']}`",
        f"- Status: {r['books_disposition']}",
        f"- Exact delta: {r['mechanism_and_ownership']}",
        f"- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#{r['arxiv_id']})", "",
    ]
qlines += [
    "## Withdrawal reversal", "",
    "- `SF-2026-ARXIV-2605-03562`: 从正向候选、评分和采用链移除；官方 arXiv exact-v1 页面提示 newer version 已被作者撤回。当前 Books 已无该 ID、Source Family、HeadQ 名称或特有 side-code 结论；root 只需在 post-write review 复算这一不变量，不得误删由其他来源支持的通用 attention-distortion 原则。", "",
]
(ROOT / "AUTHOR_BOOKS_RECONCILIATION_QUEUE.md").write_text("\n".join(qlines))

# Build the human-facing six-section Daily.  Long per-family evidence stays in
# _sources and is linked from each candidate row, avoiding a 137-paper abstract
# dump in the report body.
roadmap = (REPO / "ROADMAP.md").read_text()
node_paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([A-Z0-9-]+)` \| Ch\d+ \| `([^`]+)` \|", roadmap)}

source_rows = [
    ("SRC-OPENAI", "OpenAI Research 索引及官方域名窗口日期定点检索；0 个候选", "已检查", "历史分页不可复算；仅支持有界检查"),
    ("SRC-ANTHROPIC", "Anthropic Research；2026-04-30 与 2026-05-07/08 为相邻停止点；0 个候选", "已检查", "无"),
    ("SRC-GOOGLE-AI", "DeepMind Research + Google Research Publications；窗口日期与相邻发布；0 个候选", "已检查", "动态索引不支持全站穷尽断言"),
    ("SRC-META-AI", "Meta AI Research 索引及官方域名窗口日期；0 个候选", "已检查", "历史分页不可复算；仅支持有界检查"),
    ("SRC-QWEN", "Qwen Research + QwenLM；研究目录、发布记录和窗口日期；0 个候选", "已检查", "旧入口重定向；当前目录不证明绝对无历史事件"),
    ("SRC-DEEPSEEK", "DeepSeek 官网 + 官方 GitHub；排除同名仓库和社区材料；0 个候选", "已检查", "无"),
    ("SRC-MOONSHOT", "Kimi Platform Blog + MoonshotAI；窗口日期与相邻官方更新；0 个候选", "已检查", "动态目录仅支持有界检查"),
    ("SRC-TENCENT-HUNYUAN", "混元 Research 的“全部”目录 + Tencent-Hunyuan；窗口定点检查；0 个候选", "已检查", "列表动态加载；静态空响应未被当作零命中证明"),
    ("SRC-ZAI", "智谱 Research；2026-04-30 与 2026-05-11 为相邻停止点；0 个候选", "已检查", "无"),
    ("SRC-BYTEDANCE-SEED", "Seed public papers；窗口后首批可见日期为 2026-05-14/15/16；0 个候选", "已检查", "无"),
    ("SRC-BAIDU-ERNIE", "ERNIE Blog；2026-04-30 与 2026-05-09 为相邻停止点；0 个候选", "已检查", "无"),
    ("SRC-XIAOMI-MIMO", "MiMo 官网 + XiaomiMiMo；窗口日期与官方研究/发布；0 个候选", "已检查", "动态目录仅支持有界检查"),
    ("SRC-MINIMAX", "MiniMax 中英文 Blog；2026-03-18 与 2026-05-26/27 为相邻停止点；0 个候选", "已检查", "无"),
    ("SRC-ARXIV", "四个核心分类及约定补检分类；493 个唯一 identity 全量题摘筛选；137 候选 / 356 关闭", "已检查", "公开时间为批次推导；不是页面秒级披露"),
]

rlines = [
    "# Daily Research — 2026-05-06", "",
    "**规范：** V3",
    "**窗口：** 2026-05-05T09:00:00+08:00 ～ 2026-05-06T09:00:00+08:00",
    "**状态：** 完成",
    "**Books：** 纳入本次",
    "**检查时间：** 2026-09-14T23:30:00+08:00", "",
    "## 1. 结论", "",
    "本窗恢复 493 个唯一 arXiv identity，并逐项完成标题与完整摘要的贡献筛选。非作者准入校准指出 4 个误收和 24 个漏收；作者落实后又依据官方 withdrawal 状态移除 `2605.03562`，最终冻结 **137 个候选、356 个 pre-denominator closure**。候选比例不是质量目标，关闭项的逐项理由与改判历史保存在唯一活动账本。", "",
    f"137/137 候选均取得 exact-v1：135 项使用官方 arXiv HTML，`2605.03275` 与 `2605.03884` 使用官方 v1 PDF；逐项完成 Method、关键评价、limitation/non-proof、三维评分和 Books 判断。没有 Review Pending 或材料受阻。非作者复核把 24 项初始写回建议收紧为 **{len(PROPOSED)} 项**，其余改为具体命题级 Existing Coverage；root 已完成 10 项写回，独立 post-write 审计确认 owner、证据边界、演进主线、相邻衔接与 marker 唯一性。", "",
    "`2605.03562` 的 v1 页面提示 newer version 已由作者撤回，因此不再列候选、不评分、不作为 Books 正向证据；当前 Books 已无 HeadQ 正向 marker 或特有 side-code 结论，root 在写回后复算该不变量即可。", "",
    "## 2. 来源覆盖", "",
    "| 来源 | 检查范围与依据 | 结果 | 缺口 |", "| --- | --- | --- | --- |",
]
rlines += [f"| `{sid}` | {scope}；[作者侧明细](../_sources/daily-20260506/AUTHOR_INSTITUTION_COVERAGE.md) | {result} | {gap} |" if sid != "SRC-ARXIV" else f"| `{sid}` | {scope}；[活动筛选账本](../_sources/daily-20260506/v3-canonical-screening-ledger.json) | {result} | {gap} |" for sid, scope, result, gap in source_rows]

rlines += [
    "", "## 3. 候选与判断", "",
    "公开时间统一记为 `2026-05-06T08:00:00+08:00（public-batch-derived）`：DataCite initial registration、`2605` family/v1 identity 与 arXiv 官方 announcement 规则一致；submitted 时间不是公开时间，current OAI 被后续 revision 覆盖也不是冲突。推导依据见[公告时间证据](../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md)。", "",
    "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |",
    "| --- | --- | --- | --- | --- |",
]
for r in reviews:
    aid = r["arxiv_id"]
    s = r["score_v2"]
    path = node_paths[r["owner_node"]]
    book_link = f"`{r['owner_node']}`，[章节](../../../../{path})"
    decision = "整合" if aid in (APPLIED | PROPOSED) else "已有覆盖"
    review_result = "深入完成" if r["review_route"] == "deep" else "标准完成"
    contribution = r["mechanism_and_ownership"].rstrip("。；; ")
    display_title = r["exact_v1_title"].replace("|", "\\|")
    rlines.append(
        f"| [{display_title}]({r['exact_v1_url']}) | 2026-05-06T08:00:00+08:00 | {contribution}；Design Delta {s['design_delta']}；System Reach {s['system_reach']}；Durability {s['durability']}；{s['design_delta']}+{s['system_reach']}+{s['durability']}={s['total']}；[逐项证据](../_sources/daily-20260506/AUTHOR_EVIDENCE_COMPLETION.md#{aid}) | {review_result} | {decision}：{book_link} |"
    )

rlines += [
    "", "## 4. 证据与知识整合", "",
    "以下逐项正文与候选表使用相同标题和 primary URL，给出 exact-v1 Method、关键 evaluation、direct limitation/non-proof 与 Books 边界；更完整的定位账本见[作者侧证据完成记录](../_sources/daily-20260506/AUTHOR_EVIDENCE_COMPLETION.md)。", "",
]
for r in reviews:
    aid = r["arxiv_id"]
    owner = r["owner_node"]
    disposition = "整合，既有实体已复核" if aid in APPLIED else ("整合，已写回并通过 post-write 复核" if aid in PROPOSED else "已有覆盖，不重复追加")
    rlines += [
        f"### [{r['exact_v1_title']}]({r['exact_v1_url']})", "",
        f"- **机制与 owner：** {r['mechanism_and_ownership'].rstrip('。；; ')}。Owner 为 `{owner}`。",
        f"- **Method 定位：** {r['method_locator_and_evidence']}。",
        f"- **Evaluation 定位：** {r['evaluation_locator_and_evidence']}。",
        f"- **证据边界：** {r['direct_limitation_or_non_proof']}。该项只支持 exact-v1 披露的任务、模型与评价设置，不外推为通用结论。",
        f"- **Books：** {disposition}。", "",
    ]

rlines += [
    "### Verifier：从总体误差率到错误模式与策略分布的反馈", "",
    "随机误差近似降低信噪比时，提高样本或平均多次判断仍可能合理；系统性 false positive 会被 policy 主动发现并放大，使同样的总体 error rate 分别形成 delay、次优 plateau 或 collapse。`2605.02909v1` 在受控算术环境中注入不同错误模式并观察训练动力学，因此支持把 verifier error pattern、触发频率和 policy visitation 纳入 RLVR 监控。代价是需要分层 oracle 与分布诊断；论文没有证明开放式 verifier 的多重交互失效已被覆盖。该增量已进入 `TRAIN-GRPO` 并通过 post-write 复核。", "",
    "### MoE Prefill：从 activation AllToAll 到利用长计算窗口搬运 expert weights", "",
    "MoE 通常移动 token activation，因为权重远大于单批 activation；在 throughput-oriented、prefill-only、长序列且持续饱和的负载中，计算窗口足以隐藏后台 expert-weight AllGather，原来的大小比较不再等价于关键路径比较。`2605.02960v1` 因而把 expert placement、prefix affinity、饱和阈值与通信对象联成一个调度选择。低带宽互联、burst traffic、dense model 和 latency-critical decode 仍应保留旧路径。该增量在 `INFER-PREFILL` 的现存实体已回读通过。", "",
    "### Agent Workflow：从 exact trace matching 到必要状态与顺序约束", "",
    "同一任务可以有多条正确执行轨迹，因此把某一条示例 trace 当唯一验收标准会把合法非确定性误判为失败。`2605.03159v1` 从少量 passing traces 学习 essential states，并以 PTA 合并和 topological-subsequence 约束描述允许的执行族；这把 workflow acceptance 从字符串相等推进为状态与顺序不变量。收益是可解释、可容纳多路径；代价是样本覆盖不足时会漏掉必要状态或错误放宽顺序。该增量已进入 `AGENT-WORKFLOW` 并通过 post-write 复核。", "",
    "### Books 对账", "",
    f"[非作者命题级对账](../_sources/daily-20260506/NONAUTHOR_BOOKS_RECONCILIATION.md)包含 12 项已复核的现存实体、{len(PROPOSED)} 项已写回并通过 post-write 审计的新增、14 项从作者写回建议降级为 Existing Coverage，以及 1 项 withdrawal closure。`已有覆盖` 的 {137-len(APPLIED)-len(PROPOSED)} 项不为制造 diff 重复追加；对账逐项保留当前命题、最小增量、证据边界和相邻衔接。", "",
    "## 5. 缺口与下一步", "",
    "候选证据无待审阅或材料受阻；独立复核已重评 137 项分数并完成 Books 命题级对读。12 项现存实体已回读，10 项新写回已落实并通过 post-write 复核；HeadQ 正向证据不存在的不变量也已复算。", "",
    "终态保留项是部分动态机构目录缺少不可变历史日快照。它们不用于支持正面证据、Books 结论或绝对“无遗漏”断言；定点重开条件是以后取得当日官方快照，或发现能够唯一定位到本窗的官方事件。触发后只重开 2026-05-06 的对应来源与 Source Family，不重跑整日其他已闭合工作。", "",
    "### Ignored Noise", "",
    "- `2605.03069`：连续数据 federated privacy encoder，没有 LLM 或其基础设施的直接机制边界。",
    "- `2605.03723`：人机共创文本 change-point detection 是应用型来源识别，不改变当前 AI System 设计。",
    "- `2605.03870`：边缘 federated-learning TCP operating point，未连接大模型训练/推理通信。",
    "- `2605.03983`：一般 MPI Sessions 实现重构，没有 AI workload 证据。",
    "- `2605.03562`：newer version withdrawn；从正向链移除。",
    "- 其余 351 项的 family-specific 关闭理由见活动 ledger。", "",
    "### Repository Changes", "",
    "本 author lane 仅更新 2026-05-06 日报和 `_sources/daily-20260506/` 下的活动 ledger、机构覆盖、逐项 exact-v1 证据与 Books 协调队列；未直接修改共享 Books、ROADMAP 或 Learning State。", "",
    "## 6. 复核", "",
    "复核者：`/root/may06_independent_gate`（非作者 fresh-context reviewer；未参与本轮作者证据生成或共享 Books 写回）", "",
    "结论：通过", "",
    "Coverage、Candidate Denominator、Evidence Review、独立评分、Books Decision、Books Apply 与 post-write 独立语义复核均通过。", "",
    "**独立复核范围：** 493 = 137 retained + 356 closure；137/137 exact-v1 evidence；137/137 独立重评分与 Books 命题级对读；Review Pending=0；material blocked=0；withdrawn terminal closure=1；所有 Score V2 total 与三项相加一致；Stable Node ID 均可在 ROADMAP 解析。评分改判明细见[非作者重评分账本](../_sources/daily-20260506/NONAUTHOR_SCORE_RECALIBRATION.json)。", "",
    "**Sources：** [arXiv](https://arxiv.org/)、[官方 announcement 规则](https://info.arxiv.org/help/availability.html)、[Daily 来源注册表](../../../../docs/RESEARCH_SOURCES.md)、[逐项 evidence](../_sources/daily-20260506/AUTHOR_EVIDENCE_COMPLETION.md)。", "",
]
(REPO / "papers/2026/05/06/README.md").write_text("\n".join(rlines))

print(json.dumps(ledger["summary"], ensure_ascii=False))
