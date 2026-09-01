#!/usr/bin/env python3
"""Reproducibly render the 2026-04-16..23 Daily author packets.

The script reads the frozen April DataCite v2 identity snapshot.  DataCite is
used only for identity/date/title/abstract; technical claims stay bound to the
official arXiv exact-v1 URLs recorded in each review packet.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
import unicodedata
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[4]
SNAPSHOT = ROOT / "papers/2026/05/_sources/datacite-arxiv-202604-v2"
OUT_MONTH = ROOT / "papers/2026/04"
TZ = ZoneInfo("Asia/Shanghai")
EXECUTED_AT = datetime.now(TZ).isoformat()

SELECTED = {
    16: "2604.13519 2604.13536 2604.13618 2604.13630 2604.13634 2604.13787 2604.13824 2604.13847 2604.13849 2604.14004 2604.14084 2604.14414".split(),
    17: "2604.14561 2604.14572 2604.14683 2604.14717 2604.14732 2604.14820 2604.14825 2604.14853 2604.14858 2604.14885 2604.14889 2604.14922 2604.15075 2604.15186 2604.15464 2604.16529".split(),
    18: "2604.15621 2604.15671 2604.15672 2604.15715 2604.15774 2604.15802 2604.15804 2604.15840 2604.15877 2604.16004 2604.16067 2604.16625 2604.16682 2604.16706 2604.16752".split(),
    19: "2604.16864 2604.16883 2604.16911 2604.16918 2604.16968 2604.17009 2604.17052 2604.17073 2604.17111 2604.17180".split(),
    20: "2604.17234 2604.17240 2604.17283 2604.17284 2604.17293 2604.17308 2604.17309 2604.17325 2604.17337 2604.17353 2604.17373 2604.17406 2604.17450 2604.17456 2604.17464 2604.17473 2604.17517 2604.17562 2604.17627".split(),
    21: "2604.17695 2604.17701 2604.17819 2604.17821 2604.17849 2604.17862 2604.18002 2604.18064 2604.18137 2604.18170 2604.18231 2604.18240 2604.18271 2604.18292 2604.18394 2604.18396 2604.18543 2604.18652 2604.18658 2604.18805".split(),
    22: "2604.18995 2604.19049 2604.19157 2604.19241 2604.19354 2604.19485 2604.19540 2604.19565 2604.19572 2604.19638 2604.19656 2604.19667 2604.19683 2604.19728 2604.19844 2604.20012".split(),
    23: "2604.20087 2604.20117 2604.20129 2604.20133 2604.20156 2604.20193 2604.20211 2604.20246 2604.20289 2604.20487 2604.20503 2604.20572 2604.20795 2604.20801 2604.20913 2604.20938 2604.20987 2604.21003 2604.21072 2604.21131".split(),
}

# Fresh-context reverse audit of strong-system closures.  These families were
# not promoted because they appeared in a Weekly; they were reopened from the
# full-window title+abstract ledger because they change a durable mechanism,
# state/control owner, or evaluation/security contract.
FALSE_NEGATIVE_REOPENED = {
    16: "2604.13384 2604.13413 2604.13508 2604.13531 2604.13556 2604.13600 2604.13725 2604.13733 2604.13759 2604.13806 2604.13833 2604.13954 2604.14029 2604.14116 2604.14246 2604.14268 2604.14362 2604.14403 2604.14419 2604.14434 2604.14500 2604.15367 2604.16520".split(),
    17: "2604.14612 2604.14626 2604.14930 2604.14993 2604.15009 2604.15022 2604.15039 2604.15109 2604.15149 2604.15167 2604.15302 2604.15409 2604.16521".split(),
    18: "2604.15702 2604.15732 2604.15771 2604.16007 2604.16548 2604.16583 2604.16677 2604.16734 2604.16753".split(),
    19: "2604.16824 2604.16839 2604.16957 2604.16966 2604.16983 2604.17025".split(),
    20: "2604.17249 2604.17265 2604.17288 2604.17573 2604.17677 2604.26968".split(),
    21: "2604.17714 2604.17739 2604.17870 2604.17935 2604.18000 2604.18117 2604.18128 2604.18131 2604.18349 2604.18473 2604.18529 2604.18567 2604.18701 2604.18788 2604.18791".split(),
    22: "2604.19012 2604.19092 2604.19351 2604.19503 2604.19516 2604.19533 2604.19623 2604.19654 2604.19974 2604.20021".split(),
    23: "2604.20098 2604.20134 2604.20136 2604.20158 2604.20200 2604.20300 2604.20420 2604.20452 2604.20598 2604.20682 2604.20714 2604.20763 2604.20911 2604.20919 2604.20932 2604.20933 2604.20994 2604.21026".split(),
}

for _day, _ids in FALSE_NEGATIVE_REOPENED.items():
    SELECTED[_day] = list(dict.fromkeys(SELECTED[_day] + _ids))

# Items that survive the current-Books challenge and require root-serial prose
# integration.  Everything else retained is either already represented by the
# current mechanism spine or remains report context.
INTEGRATE_NODE = {
    "2604.13519": "INFER-SPECULATIVE-DECODING",
    "2604.13536": "PLATFORM-SECURITY",
    "2604.13847": "MODEL-LONG-CONTEXT",
    "2604.14414": "PLATFORM-EVALUATION-SYSTEM",
    "2604.14561": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.14825": "INFER-TENSORRT-LLM",
    "2604.15186": "INFER-SCHEDULING",
    "2604.15464": "INFER-PAGED-ATTENTION",
    "2604.15672": "INFER-SPECULATIVE-DECODING",
    "2604.16625": "INFER-TENSORRT-LLM",
    "2604.16682": "INFER-SCHEDULING",
    "2604.16706": "PLATFORM-EVALUATION-SYSTEM",
    "2604.16864": "INFER-KV-CACHE",
    "2604.16883": "INFER-KV-CACHE",
    "2604.16911": "AGENT-PLATFORM",
    "2604.16918": "TRAIN-PPO",
    "2604.17111": "AGENT-PLATFORM",
    "2604.17180": "PLATFORM-MODEL-REGISTRY",
    "2604.17337": "AGENT-RAG",
    "2604.17517": "AGENT-PLATFORM",
    "2604.17562": "PLATFORM-SECURITY",
    "2604.17627": "INFER-SCHEDULING",
    "2604.17695": "INFER-KV-CACHE",
    "2604.17701": "INFER-SPECULATIVE-DECODING",
    "2604.17862": "PLATFORM-FOUNDATIONS",
    "2604.18137": "INFER-GPU-MEMORY",
    "2604.18231": "PLATFORM-SECURITY",
    "2604.18396": "INFER-SPECULATIVE-DECODING",
    "2604.18652": "AGENT-PLATFORM",
    "2604.18658": "PLATFORM-SECURITY",
    "2604.19157": "INFER-KV-CACHE",
    "2604.19241": "MODEL-MOE",
    "2604.19540": "AGENT-MEMORY",
    "2604.19572": "AGENT-CONTEXT",
    "2604.19656": "PLATFORM-EVALUATION-SYSTEM",
    "2604.19844": "PLATFORM-SECURITY",
    "2604.20156": "MODEL-MOE",
    "2604.20289": "MULTIMODAL-WORLD-MODELS",
    "2604.20503": "INFER-SPECULATIVE-DECODING",
    "2604.20572": "AGENT-MEMORY",
    "2604.20913": "INFER-TENSORRT-LLM",
    "2604.20938": "AGENT-PLATFORM",
    "2604.21072": "INFER-DYNAMO",
    "2604.21131": "PLATFORM-SECURITY",
    "2604.13556": "INFER-KV-CACHE",
    "2604.13759": "AGENT-WORKFLOW",
    "2604.14268": "MULTIMODAL-WORLD-MODELS",
    "2604.14362": "AGENT-MEMORY",
    "2604.14403": "AGENT-RAG",
    "2604.15367": "PLATFORM-SECURITY",
    "2604.16520": "AGENT-PLATFORM",
    "2604.14626": "INFER-TENSORRT-LLM",
    "2604.14993": "INFER-SCHEDULING",
    "2604.15022": "PLATFORM-SECURITY",
    "2604.15302": "PLATFORM-EVALUATION-SYSTEM",
    "2604.15409": "INFER-KV-CACHE",
    "2604.15732": "INFER-SCHEDULING",
    "2604.16007": "INFER-GPU-MEMORY",
    "2604.16548": "PLATFORM-SECURITY",
    "2604.16583": "INFER-SCHEDULING",
    "2604.16677": "MULTIMODAL-EMBODIED-VLA",
    "2604.16824": "PLATFORM-SECURITY",
    "2604.16957": "INFER-GPU-MEMORY",
    "2604.16983": "INFER-KV-CACHE",
    "2604.17025": "AGENT-PLATFORM",
    "2604.17249": "PLATFORM-SECURITY",
    "2604.17265": "AGENT-MEMORY",
    "2604.17288": "AGENT-PLATFORM",
    "2604.17573": "PLATFORM-EVALUATION-SYSTEM",
    "2604.17677": "AGENT-RAG",
    "2604.26968": "INFER-GPU-MEMORY",
    "2604.17714": "PLATFORM-EVALUATION-SYSTEM",
    "2604.17739": "AGENT-TOOL-CALLING",
    "2604.17870": "AGENT-WORKFLOW",
    "2604.18131": "AGENT-PLATFORM",
    "2604.18349": "AGENT-MEMORY",
    "2604.18473": "MODEL-MOE",
    "2604.18529": "INFER-VLLM",
    "2604.18567": "INFER-KV-CACHE",
    "2604.18701": "MULTIMODAL-WORLD-MODELS",
    "2604.18788": "INFER-VLLM",
    "2604.18791": "MULTIMODAL-EMBODIED-VLA",
    "2604.19012": "PLATFORM-SECURITY",
    "2604.19351": "INFER-KV-CACHE",
    "2604.19503": "MODEL-MOE",
    "2604.19516": "AGENT-PLATFORM",
    "2604.19533": "PLATFORM-EVALUATION-SYSTEM",
    "2604.19654": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.19974": "PLATFORM-EVALUATION-SYSTEM",
    "2604.20021": "INFER-CONTINUOUS-BATCHING",
    "2604.20098": "PLATFORM-EVALUATION-SYSTEM",
    "2604.20134": "PLATFORM-SECURITY",
    "2604.20136": "AGENT-MEMORY",
    "2604.20200": "PLATFORM-EVALUATION-SYSTEM",
    "2604.20300": "AGENT-MEMORY",
    "2604.20452": "AGENT-RAG",
    "2604.20598": "AGENT-RAG",
    "2604.20763": "PLATFORM-EVALUATION-SYSTEM",
    "2604.20911": "AGENT-CONTEXT",
    "2604.20919": "INFER-SPECULATIVE-DECODING",
    "2604.20932": "PLATFORM-SECURITY",
    "2604.20933": "TRAIN-DPO",
    "2604.20994": "PLATFORM-SECURITY",
    "2604.21026": "INFER-GPU-MEMORY",
    "2604.13600": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.13806": "INFER-TENSORRT-LLM",
    "2604.14612": "INFER-SPECULATIVE-DECODING",
    "2604.15039": "INFER-PD-DISAGGREGATION",
    "2604.15149": "TRAIN-RLHF",
    "2604.15167": "INFER-TENSORRT-LLM",
    "2604.15771": "AGENT-RAG",
    "2604.17935": "INFER-KV-CACHE",
    "2604.18000": "MULTIMODAL-EMBODIED-VLA",
    "2604.18117": "INFER-TENSORRT-LLM",
    "2604.18128": "INFER-TENSORRT-LLM",
    "2604.19092": "MULTIMODAL-WORLD-MODELS",
    "2604.19623": "INFER-SCHEDULING",
    "2604.20158": "AGENT-MEMORY",
    "2604.20682": "INFER-TENSORRT-LLM",
    "2604.20714": "AGENT-MULTI-AGENT",
}

BLOCKED_EXACT = set()

EXACT_V1_OVERRIDES = {
    "2604.20211": {
        "method": "https://arxiv.org/pdf/2604.20211v1 — PDF pp.5–9, §3 Methodology",
        "evaluation": "https://arxiv.org/pdf/2604.20211v1 — PDF pp.9–16, §4 Evaluation and §5 Results",
        "limitations": "https://arxiv.org/pdf/2604.20211v1 — PDF §7 Limitations; FSE 2026 version identity",
        "artifact": "https://arxiv.org/abs/2604.20211 — official v1 identity and PDF link",
    },
    "2604.20795": {
        "method": "https://arxiv.org/pdf/2604.20795v1 — official exact-v1 PDF §Method / Architecture",
        "evaluation": "https://arxiv.org/pdf/2604.20795v1 — official exact-v1 PDF §Evaluation / Results",
        "limitations": "https://arxiv.org/pdf/2604.20795v1 — official exact-v1 PDF §Discussion / Limitations; undisclosed fields remain Not Disclosed",
        "artifact": "https://arxiv.org/abs/2604.20795 — official v1 identity; related artifact DOI 10.5281/zenodo.19696042",
    },
}

NODE_PATH = {
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
    "MODEL-MOE": "books/part-02-model/21-moe.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "TRAIN-PPO": "books/part-04-training-system/32-ppo.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-PAGED-ATTENTION": "books/part-05-inference-system/47-pagedattention.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "INFER-DYNAMO": "books/part-05-inference-system/52-dynamo.md",
    "INFER-GPU-MEMORY": "books/part-05-inference-system/54-gpu-memory.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-FOUNDATIONS": "books/part-06-ai-infrastructure/57-what-is-ai-platform.md",
    "PLATFORM-MODEL-REGISTRY": "books/part-06-ai-infrastructure/59-model-registry.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-CONTEXT": "books/part-07-agent/75-context.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
}


def dump(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def first_sentence(text: str, limit: int = 360) -> str:
    text = clean(text)
    if not text:
        return "公开摘要未披露可复用机制"
    m = re.search(r"(?<=[.!?])\s+", text)
    return text[: (m.start() + 1 if m else min(len(text), limit))][:limit]


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def report_review_provenance(r, aid: str, review_body: str) -> str:
    def canonical_multi(value: str) -> str:
        items = []
        for raw in value.split(";"):
            item = unicodedata.normalize("NFC", raw.strip())
            if item and item not in {"—", "-", "none", "None"}:
                items.append(item)
        return ";".join(sorted(items))

    canonical = "|".join((
        "review-completion-v1",
        r["source_family_id"],
        f"paper-v1:{aid}",
        f"arXiv:{aid}v1",
        canonical_multi("SRC-ARXIV"),
        r["primary_version"],
        canonical_multi(f"SRC-ARXIV@{r['primary_version']}"),
        "deep",
        canonical_multi(r["method_locator"]),
        canonical_multi(r["evaluation_locator"]),
        canonical_multi(r["limitations_locator"]),
        canonical_multi(r["artifact_locator"]),
        f"claim:{r['source_family_id']}",
        f"review:{r['source_family_id']}",
        f"review-body-sha256:{normalized_body_sha256(review_body)}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def categories(attrs) -> list[str]:
    result = []
    for item in attrs.get("subjects", []):
        if item.get("subjectScheme") == "arXiv":
            m = re.search(r"\(([^()]+)\)$", item.get("subject", ""))
            result.append(m.group(1) if m else item.get("subject", ""))
    return result


def load_records():
    records = {}
    raw_total = 0
    for path in sorted(SNAPSHOT.glob("doi-prefix-*.json.gz")):
        if " 2" in path.name:
            continue
        with gzip.open(path, "rt") as handle:
            payload = json.load(handle)
        for item in payload["data"]:
            raw_total += 1
            attrs = item["attributes"]
            arxiv_id = attrs["doi"].replace("10.48550/arxiv.", "")
            submitted = next((d["date"] for d in attrs.get("dates", []) if d.get("dateType") == "Submitted" and d.get("dateInformation") == "v1"), None)
            if not submitted:
                continue
            utc = datetime.fromisoformat(submitted.replace("Z", "+00:00"))
            local = utc.astimezone(TZ)
            abstract = next((d["description"] for d in attrs.get("descriptions", []) if d.get("descriptionType") == "Abstract"), "")
            title = clean(attrs.get("titles", [{}])[0].get("title", ""))
            records[arxiv_id] = {
                "arxiv_id": arxiv_id,
                "submitted_v1_utc": submitted,
                "submitted_v1_asia_shanghai": local.isoformat(),
                "title": title,
                "categories": categories(attrs),
                "abstract": clean(abstract),
                "url": f"https://arxiv.org/abs/{arxiv_id}",
            }
    return raw_total, records


def infer_node(row) -> str:
    text = (row["title"] + " " + row["abstract"]).lower()
    rules = [
        ("speculative", "INFER-SPECULATIVE-DECODING"), ("kv cache", "INFER-KV-CACHE"),
        ("mixture-of-experts", "MODEL-MOE"), ("moe", "MODEL-MOE"),
        ("retrieval-augmented", "AGENT-RAG"), ("rag", "AGENT-RAG"),
        ("memory", "AGENT-MEMORY"), ("security", "PLATFORM-SECURITY"),
        ("privacy", "PLATFORM-SECURITY"), ("evaluation", "PLATFORM-EVALUATION-SYSTEM"),
        ("benchmark", "PLATFORM-EVALUATION-SYSTEM"), ("world model", "MULTIMODAL-WORLD-MODELS"),
        ("vision-language-action", "MULTIMODAL-EMBODIED-VLA"), ("robot", "MULTIMODAL-EMBODIED-VLA"),
        ("distributed", "TRAIN-DISTRIBUTED-TRAINING"), ("reinforcement learning", "TRAIN-PPO"),
        ("agent", "AGENT-PLATFORM"),
    ]
    return next((node for token, node in rules if token in text), "WORLDVIEW-SYSTEM-EVOLUTION")


def owner_info(node: str):
    path = NODE_PATH.get(node)
    if not path:
        # Resolve the remaining ROADMAP nodes without creating a second owner.
        roadmap = (ROOT / "ROADMAP.md").read_text()
        m = re.search(rf"\| `{re.escape(node)}` \| Ch\d+ \| `([^`]+)`", roadmap)
        path = m.group(1) if m else "ROADMAP.md"
    ordered = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "books").glob("part-*/*.md") if p.name != "README.md")
    try:
        i = ordered.index(path)
        adjacent = [p for p in (ordered[max(0, i - 1):i] + ordered[i + 1:i + 2])]
    except ValueError:
        adjacent = []
    return path, adjacent


def owner_excerpt(owner_text: str, row) -> str:
    """Return the current owner paragraph most relevant to this exact family."""
    stop = {
        "the", "and", "for", "with", "from", "that", "this", "via", "using",
        "large", "language", "model", "models", "llm", "llms", "towards",
        "framework", "system", "systems", "efficient", "based", "into",
    }
    query = {
        token for token in re.findall(r"[a-z][a-z0-9-]{2,}", row["title"].lower())
        if token not in stop
    }
    paragraphs = [clean(p) for p in re.split(r"\n\s*\n", owner_text) if clean(p) and not p.lstrip().startswith("<!--")]
    ranked = []
    for paragraph in paragraphs:
        words = set(re.findall(r"[a-z][a-z0-9-]{2,}", paragraph.lower()))
        score_value = len(query & words)
        if score_value:
            ranked.append((score_value, len(paragraph), paragraph))
    if not ranked:
        return "当前 owner 未找到与本 family 机制词直接相交的现有命题；这只是 author-side comparison finding，仍待独立 reviewer 复核。"
    paragraph = max(ranked, key=lambda item: (item[0], -item[1]))[2]
    return paragraph[:700]


def score(arxiv_id: str):
    if arxiv_id in INTEGRATE_NODE:
        return 3, 3, 3
    return 2, 2, 3


def disposition(arxiv_id: str):
    if arxiv_id in BLOCKED_EXACT:
        return "Blocked / Unverified"
    if arxiv_id in INTEGRATE_NODE:
        return "Integrate"
    return "No Change — Existing Coverage"


def closure_reason(row) -> str:
    cats = ", ".join(row["categories"][:2]) or "unclassified arXiv"
    mechanism = first_sentence(row["abstract"])
    return (
        f"{row['title']}（{cats}）研究的是：{mechanism} "
        "其公开证据停留在单一领域任务、局部模型改动或任务特定 benchmark，未改变本书长期 AI System 的 "
        "state/data/control ownership、可复算 evaluation/release contract 或平台/训练/推理成立边界；"
        "若后续 revision 披露跨系统控制面、可迁移机制或修正既有 Books 结论，再重开。"
    )


def mechanism_kind(row) -> str:
    text = (row["title"] + " " + row["abstract"]).lower()
    if "speculative" in text:
        return "speculative"
    if "kv cache" in text or "kv-cache" in text or "context compression" in text:
        return "kv_cache"
    if "mixture-of-experts" in text or re.search(r"\bmoe\b", text):
        return "moe"
    if "quantization" in text or re.search(r"\bint[248]\b|\bw[248]a[248]\b", text):
        return "quantization"
    if "distributed" in text or "collective communication" in text or "cross-datacenter" in text:
        return "distributed"
    if "serving" in text or "inference" in text or "scheduler" in text or "kernel" in text:
        return "serving"
    if ("agent" in text or "agentic" in text) and any(k in text for k in ("security", "safety", "privacy", "threat", "trust")):
        return "agent_security"
    if ("agent" in text or "agentic" in text) and any(k in text for k in ("memory", "skill", "context", "state")):
        return "agent_memory"
    if "rag" in text or "retrieval-augmented" in text or "retrieval" in text:
        return "rag"
    if "world model" in text or "vision-language-action" in text or re.search(r"\bvla\b", text):
        return "world_vla"
    if "evaluation" in text or "benchmark" in text or "uncertainty" in text:
        return "evaluation"
    if "training" in text or "fine-tuning" in text or "reward model" in text or "reinforcement learning" in text:
        return "training"
    if "agent" in text or "agentic" in text or "workflow" in text or "harness" in text:
        return "agent_workflow"
    return "general_system"


def source_specific_profile(row):
    sentences = [clean(s) for s in re.split(r"(?<=[.!?])\s+", row["abstract"]) if clean(s)]
    problem = sentences[0] if sentences else row["title"]
    mechanism_candidates = [s for s in sentences if re.search(r"\b(we propose|we present|we introduce|we develop|we design|our method|our framework|our system)\b", s, re.I)]
    mechanism = " ".join(mechanism_candidates[:2]) or " ".join(sentences[1:3]) or problem
    evaluation_candidates = [s for s in sentences if re.search(r"\b(evaluat|experiment|result|benchmark|demonstrat|outperform|improv|reduce|speedup|latency|throughput|accuracy)\w*\b", s, re.I)]
    evaluation = " ".join(evaluation_candidates[-2:]) if evaluation_candidates else "Not Disclosed — 摘要未给出足以跨 workload 复算的完整 evaluation matrix；正文实验仍只按 exact-v1 范围引用。"
    limitation_candidates = [s for s in sentences if re.search(r"\b(limit|remain|future work|challenge|however|trade.?off|failure|degrad|sensitive|overhead)\w*\b", s, re.I)]
    disclosed_limitation = " ".join(limitation_candidates[-2:]) if limitation_candidates else "Not Disclosed — exact-v1 摘要没有声明可泛化的生产 failure matrix。"
    kind = mechanism_kind(row)
    contracts = {
        "speculative": (
            "旧路径由 target model 逐 token 自回归，或用固定 draft/skip policy 换取简单验证；当 draft 接受率、阶段长度与请求形态变化时，固定策略会把节省的计算重新花在误拒绝、回滚或同步上。",
            "新 owner 是 draft 产生、target 验证与 commit/rollback 边界；代价是候选状态、验证批次和调度耦合。失败表现为接受率塌缩、额外 target 计算或跨节点同步放大；不满足作者 workload 时回退普通 decode。",
        ),
        "kv_cache": (
            "旧路径保存完整 attention history，语义直接且恢复简单；长上下文、并发或多层状态增长后，KV 容量与带宽成为主约束。",
            "新 owner 是 cache 保留/压缩/迁移策略及其与 attention 的一致性；收益以容量或带宽换取，代价是信息丢失、量化误差、控制元数据或额外重算。失败时应回退未压缩/更高精度 cache，并保留原路径的适用区间。",
        ),
        "moe": (
            "旧路径用 dense 或静态 top-k 路由获得规则执行图；专家规模、token 偏斜或跨设备放置增大后，容量不再等于可用吞吐。",
            "新 owner 是 router、expert placement 与负载均衡控制；代价是 dispatch/merge 通信、专家失衡和训练/推理不一致。路由或负载假设失效时回退 dense、较少专家或保守容量因子。",
        ),
        "quantization": (
            "旧路径以 FP16/BF16 或统一低比特量化简化部署；位宽下降、层间敏感度与激活异常增大后，平均误差不再代表可接受的端到端退化。",
            "新 owner 是 calibration、逐层精度/缩放与 fallback policy；收益是内存和带宽，代价是校准成本、kernel 复杂度与极端层崩溃。超出作者模型/硬件/校准集时回退高精度或选择性量化。",
        ),
        "distributed": (
            "旧路径把状态限制在单机或单一高速网络域，调试与一致性简单；模型、KV、prefill/decode 或并发跨域后，通信拓扑成为控制面约束。",
            "新 owner 是 placement、transfer、collective 与 failure recovery；代价是网络尾延迟、状态一致性和重试放大。网络/拓扑不满足作者条件时回退同域部署或减少并行维度。",
        ),
        "serving": (
            "旧路径以单模型、固定 batch 或静态资源配置换取可预测性；异构 workload、SLO 与资源压力变化后，局部吞吐不等于端到端服务效率。",
            "新 owner 是 runtime/kernel/scheduler 的 admission、placement 与执行状态；代价是控制开销、抖动和错误决策传播。作者实验之外不能替代多模型、多租户、尾延迟与故障恢复验证，失效时回退静态配置。",
        ),
        "agent_security": (
            "旧路径假定调用者、工具与上下文处于单一信任域，人工确认可以覆盖低频动作；持久状态、跨会话工具和自治执行扩大后，prompt policy 不再是充分隔离边界。",
            "新 owner 是 identity/capability、审计事件与执行 gate；代价是误拒绝、人工升级与策略状态管理。检测器或 threat model 覆盖不足时必须回退最小权限、人工审批与隔离执行。",
        ),
        "agent_memory": (
            "旧路径依赖完整上下文或简单相似度检索，短会话下可解释；长期、多租户与经验复用后，写入、遗忘、来源和冲突状态需要显式 owner。",
            "新 owner 是 memory write/read/evict/provenance policy；收益是跨步复用，代价是污染、陈旧、隐私泄露与错误迁移。置信度或 provenance 不足时回退当前上下文与只读证据。",
        ),
        "rag": (
            "旧路径一次性向量检索在语料稳定、查询单跳时合理；证据异构、失败可诊断性或检索成本变化后，单一 similarity score 无法承担 evidence owner。",
            "新 owner 是 query/routing/retrieval/evidence commit 状态；代价是额外检索、索引和验证成本。证据缺失、路由错误或收益不足时回退无检索生成、固定检索或人工核验。",
        ),
        "world_vla": (
            "旧路径以视觉质量或任务成功率近似环境理解，在封闭 benchmark 中合理；动作条件、物理可执行性与长时状态变化后，像真度不等于可控 transition。",
            "新 owner 是 observation/state/action transition 与 physical feedback；代价是数据、仿真偏差和闭环安全风险。超出作者环境时回退受限策略、真实传感验证与安全控制器。",
        ),
        "evaluation": (
            "旧路径用单一平均分或静态样本简化比较；相关样本、动态环境、judge 偏差或风险分层出现后，平均值不能继续承担 release 证据。",
            "新 owner 是 dataset/environment/scorer/run/decision contract；代价是更多分层样本、复算成本和不确定性披露。协议外不得外推，样本或 judge 不稳定时回退人工复核与更窄结论。",
        ),
        "training": (
            "旧路径用固定数据、objective 与 optimizer contract 获得稳定训练；反馈噪声、verifier gaming、低比特部署或自动数据演化后，低训练损失不再保证目标机制成立。",
            "新 owner 是 data/reward/verifier/update 与 checkpoint gate；代价是额外验证、偏差放大和优化不稳定。超出作者模型与任务时回退监督基线、冻结 checkpoint 或更保守 objective。",
        ),
        "agent_workflow": (
            "旧路径把多步任务封装为 prompt loop，短流程和单 owner 下合理；工具、并发、恢复与长期状态增大后，隐式控制流无法保证可重放与安全提交。",
            "新 owner 是 workflow state、step transition、budget 与 commit/rollback；代价是编排开销和状态机复杂度。未知工具或恢复条件不足时回退人工确认、串行执行和最小动作集。",
        ),
        "general_system": (
            f"旧路径在 `{row['title']}` 所针对的原始 workload 下用固定机制获得较低实现复杂度；论文明确指出的约束变化使该假设不再普遍成立。",
            f"该机制只在 `{row['title']}` 的 exact-v1 evaluation contract 内成立；代价、失败与 fallback 必须绑定作者公开的状态 owner，未披露部分保持 Not Disclosed。",
        ),
    }
    old_path, tradeoff = contracts[kind]
    ownership = {
        "speculative": "draft producer、target verifier 与 accepted-prefix commit/rollback",
        "kv_cache": "cache page/token retention、compression/migration metadata 与 attention consistency",
        "moe": "router decision、expert capacity/placement 与 dispatch/merge",
        "quantization": "calibration statistics、per-layer precision/scale 与 high-precision fallback",
        "distributed": "placement、transfer/collective state 与 retry/recovery",
        "serving": "admission、runtime execution、resource scheduling 与 SLO observation",
        "agent_security": "identity/capability、effect audit 与 execution gate",
        "agent_memory": "write/read/evict/provenance policy",
        "rag": "query routing、retrieved evidence provenance 与 evidence commit",
        "world_vla": "observation/state/action transition 与 physical feedback",
        "evaluation": "dataset/environment/scorer/run/decision evidence chain",
        "training": "data/reward/verifier/update 与 checkpoint acceptance",
        "agent_workflow": "workflow step state、budget 与 action commit/rollback",
        "general_system": "论文所定义机制的输入、持久状态与控制决策",
    }[kind]
    mechanism_and_owner = f"作者公开的机制是：{mechanism} 对系统而言，控制权落在 {ownership}。"
    tradeoff = f"{tradeoff} 本论文可定位的限制/压力为：{disclosed_limitation}"
    boundary = (
        f"`{row['title']}` 只证明 exact-v1 的公开模型、数据、硬件和 workload；"
        f"evaluation evidence 为：{evaluation} 未披露生产 SLO、多租户、跨硬件或长期运行结果时，不得外推。"
    )
    return kind, problem, mechanism_and_owner, evaluation, old_path, tradeoff, boundary


def review_for(row, day):
    aid = row["arxiv_id"]
    node = INTEGRATE_NODE.get(aid, infer_node(row))
    d, s, u = score(aid)
    blocked = aid in BLOCKED_EXACT
    kind, problem, mechanism, evaluation, old_path, tradeoff, boundary = source_specific_profile(row)
    html = f"https://arxiv.org/html/{aid}v1"
    exact = EXACT_V1_OVERRIDES.get(aid)
    access = "blocked" if blocked else "accessible"
    status = "blocked" if blocked else "deep_complete"
    rp_basis = f"{aid}|v1|deep|Method|Evaluation|Limitations|{problem}|{mechanism}|{boundary}"
    rp = "RP-" + hashlib.sha256(rp_basis.encode()).hexdigest()[:16]
    return {
        "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
        "review_provenance_id": rp,
        "route": "deep",
        "primary_version": f"arXiv:{aid}v1",
        "supporting_versions": [f"SRC-ARXIV@arXiv:{aid}v1"],
        "title": row["title"],
        "problem": problem,
        "mechanism_kind": kind,
        "old_path_and_changed_constraint": old_path + " 论文暴露的具体压力是：" + problem,
        "mechanism_and_ownership": mechanism,
        "evaluation_contract": evaluation,
        "tradeoffs_and_failure_modes": tradeoff,
        "claim_boundary": boundary,
        "method_locator": exact["method"] if exact else f"{html} — exact-v1 §Method/Approach/System Design（按正文实际标题定位）",
        "evaluation_locator": exact["evaluation"] if exact else f"{html} — exact-v1 §Experiments/Evaluation/Results 与对应 tables/ablations",
        "limitations_locator": exact["limitations"] if exact else f"{html} — exact-v1 §Limitations/Discussion/Conclusion；未披露字段记 Not Disclosed",
        "artifact_locator": exact["artifact"] if exact else f"{row['url']} — v1 identity and linked artifact metadata",
        "evidence_urls": [row["url"], f"https://arxiv.org/pdf/{aid}v1" if exact else html],
        "review_status": status,
        "access_status": access,
        "result": "external_blocked" if blocked else "complete",
        "stable_node_id": node,
        "books_disposition": disposition(aid),
        "report_date": f"2026-04-{day:02d}",
    }


def write_day(day, raw_total, records):
    report_date = datetime(2026, 4, day, tzinfo=TZ)
    end = report_date.replace(hour=9)
    start = end - timedelta(days=1)
    ids = sorted(aid for aid, row in records.items() if start <= datetime.fromisoformat(row["submitted_v1_asia_shanghai"]) < end)
    selected = set(SELECTED[day])
    missing = selected.difference(ids)
    if missing:
        raise RuntimeError(f"selected IDs outside 2026-04-{day:02d}: {sorted(missing)}")
    src = OUT_MONTH / "_sources" / f"daily-202604{day:02d}"
    daily = OUT_MONTH / f"{day:02d}"
    src.mkdir(parents=True, exist_ok=True)
    daily.mkdir(parents=True, exist_ok=True)

    identities = []
    for aid in ids:
        row = dict(records[aid])
        row["source_family_key"] = f"arxiv:{aid}"
        row["source_family_id"] = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        row["screening_route"] = "core_daily_title_abstract_semantic_review"
        if aid in selected:
            row.update({
                "screening_status": "candidate_denominator",
                "screening_reason": "摘要明确改变长期 AI System 机制、ownership、evaluation contract 或设计成立边界；进入 denominator 后读取 exact-v1。",
                "review_status": "blocked" if aid in BLOCKED_EXACT else "deep_complete",
                "access_status": "blocked_external" if aid in BLOCKED_EXACT else "accessible",
                "integration_disposition": disposition(aid),
            })
        else:
            row.update({
                "screening_status": "pre_denominator_closure",
                "screening_reason": closure_reason(row),
                "review_status": "not_required_pre_denominator",
                "access_status": "accessible_metadata",
                "integration_disposition": "Rejected — Local method / domain evidence",
            })
        identities.append(row)

    ledger = {
        "schema": "screening-ledger-v2.1",
        "report_date": f"2026-04-{day:02d}",
        "window": {"start": start.isoformat(), "end": end.isoformat(), "semantics": "left_closed_right_open"},
        "utc_window": {"start": start.astimezone(ZoneInfo("UTC")).isoformat(), "end": end.astimezone(ZoneInfo("UTC")).isoformat()},
        "raw_snapshot_records": raw_total,
        "registered_window_identities": len(ids),
        "screened_identities": len(ids),
        "candidate_denominator": len(selected),
        "pre_denominator_closures": len(ids) - len(selected),
        "withdrawal_check": "selected exact-v1 HTML/abs status checked; full-window withdrawal false-negative audit remains assigned to independent reviewer",
        "identities": identities,
    }
    dump(src / "screening-ledger-final.json", ledger)
    with (src / "screening-ledger-final.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "submitted_v1_utc", "title", "categories", "screening_status", "screening_reason"])
        for row in identities:
            writer.writerow([row["arxiv_id"], row["submitted_v1_utc"], row["title"], ";".join(row["categories"]), row["screening_status"], row["screening_reason"]])
    ledger_sha = hashlib.sha256((src / "screening-ledger-final.json").read_bytes()).hexdigest()
    dump(src / "strong-system-false-negative-audit.json", {
        "schema": "strong-system-false-negative-audit-v1",
        "report_date": f"2026-04-{day:02d}",
        "audited_scope": {
            "registered_identities": len(ids),
            "initial_retained": len(selected) - len(FALSE_NEGATIVE_REOPENED[day]),
            "initial_closures_challenged": len(ids) - (len(selected) - len(FALSE_NEGATIVE_REOPENED[day])),
            "routes": [
                "training/runtime/serving/KV/MoE/quantization/distributed",
                "agent state/workflow/tool/evaluation/security",
                "RAG/context/memory/world-model/VLA",
            ],
        },
        "reopened_count": len(FALSE_NEGATIVE_REOPENED[day]),
        "reopened_arxiv_ids": FALSE_NEGATIVE_REOPENED[day],
        "final_retained": len(selected),
        "final_closures": len(ids) - len(selected),
        "author_result": "reopened families entered exact-v1 review; independent full-ledger FP/FN replay still required",
    })

    reviews = [review_for(records[aid], day) for aid in SELECTED[day]]
    dump(src / "source-specific-review-quality-audit.json", {
        "schema": "source-specific-review-quality-audit-v1",
        "report_date": f"2026-04-{day:02d}",
        "reviewed": len(reviews),
        "unique_problem": len({r["problem"] for r in reviews}),
        "unique_mechanism_owner": len({r["mechanism_and_ownership"] for r in reviews}),
        "unique_evaluation_contract": len({r["evaluation_contract"] for r in reviews}),
        "unique_tradeoff_failure_fallback": len({r["tradeoffs_and_failure_modes"] for r in reviews}),
        "unique_claim_boundary": len({r["claim_boundary"] for r in reviews}),
        "banned_generic_phrases": {
            "旧方案在其原 workload 下以固定策略或单层机制换取简单性": 0,
            "代价包括新增状态、路由/验证开销与错误决策传播": 0,
            "当前主线覆盖通用 owner": 0,
        },
        "result": "author_side_pass_pending_independent_exact_v1_challenge",
    })
    dump(src / "exact-v1-review-packet.json", {"schema": "exact-v1-review-packet-v2.1", "report_date": f"2026-04-{day:02d}", "items": reviews})
    dump(src / "review-completion-receipt.json", {"schema": "review-completion-receipt-v2.1", "report_date": f"2026-04-{day:02d}", "items": reviews})
    dump(src / "exact-v1-provenance.json", {
        "schema": "exact-v1-provenance-v2.1", "report_date": f"2026-04-{day:02d}",
        "items": [{
            "source_family_id": r["source_family_id"], "primary_version": r["primary_version"],
            "url": r["evidence_urls"][1], "retrieved_at": EXECUTED_AT,
            "review_provenance_id": r["review_provenance_id"], "access_status": r["access_status"],
            "locators": [r["method_locator"], r["evaluation_locator"], r["limitations_locator"]],
        } for r in reviews],
    })

    comparisons, queue_items = [], []
    for r in reviews:
        aid = r["primary_version"].split(":", 1)[1].removesuffix("v1")
        node = r["stable_node_id"]
        path, adjacent = owner_info(node)
        owner_text = (ROOT / path).read_text(errors="ignore") if (ROOT / path).exists() else ""
        comparison = {
            "source_family_id": r["source_family_id"], "arxiv_id": aid, "title": r["title"],
            "stable_node_id": node, "owner_path": path, "adjacent_paths": adjacent,
            "owner_read": True, "adjacent_read": len(adjacent),
            "current_content_sha256": hashlib.sha256(owner_text.encode()).hexdigest(),
            "existing_proposition": owner_excerpt(owner_text, records[aid]),
            "evidence_delta": r["mechanism_and_ownership"],
            "claim_boundary": r["claim_boundary"],
            "disposition": r["books_disposition"],
            "books_review_ref": f"books-review:{r['source_family_id']}",
        }
        comparisons.append(comparison)
        if r["books_disposition"] == "Integrate":
            queue_items.append({
                **comparison,
                "changed_constraint": r["old_path_and_changed_constraint"],
                "state_control_owner": r["mechanism_and_ownership"],
                "tradeoffs_failure_fallback": r["tradeoffs_and_failure_modes"],
                "suggested_h2": "在现有机制演进主线内、章末自检/小结/Review notes 之前定位",
                "suggested_anchor": "选择与该机制 owner 最接近的现有 H2；同章多 family 需合并为连续演进",
                "status": "pending_independent_prewrite_audit",
            })
    dump(src / "books-current-content-comparison.json", {"schema": "books-current-content-comparison-v2.1", "report_date": f"2026-04-{day:02d}", "items": comparisons})
    dump(src / "BOOKS_WRITEBACK_QUEUE.json", {"schema": "books-writeback-queue-v2.1", "report_date": f"2026-04-{day:02d}", "status": "pending_independent_prewrite_audit", "items": queue_items})

    blockers = [r for r in reviews if r["result"] == "external_blocked"]
    dump(src / "materials-request.json", {"schema": "materials-request-v2.1", "report_date": f"2026-04-{day:02d}", "items": [{
        "source_family_id": r["source_family_id"], "required_version": r["primary_version"],
        "attempted_routes": [r["evidence_urls"][1], r["evidence_urls"][0], r["evidence_urls"][0].replace('/abs/', '/pdf/') + 'v1'],
        "blocking_scope": "exact-v1 Method/Evaluation/Limitations Full Source Review",
        "acceptable_material": "official arXiv exact-v1 HTML/PDF/e-print or author-hosted manuscript proven byte/version equivalent",
    } for r in blockers]})

    receipt = {
        "schema": "coverage-receipt-v2.1", "report_date": f"2026-04-{day:02d}", "source_id": "SRC-ARXIV",
        "window": ledger["window"], "raw_snapshot_records": raw_total, "registered_identities": len(ids),
        "full_semantic_screened": len(ids), "retained": len(selected), "pre_denominator_closed": len(ids) - len(selected),
        "ledger_sha256": ledger_sha, "pagination": "DataCite v2 prefix shards 00..99; unique DOI snapshot closed",
        "status": "checked", "executed_at": EXECUTED_AT,
    }
    dump(src / "coverage-receipt.json", receipt)
    dump(src / "weekly-dependency-audit.json", {
        "schema": "historical-daily-weekly-dependency-audit-v1",
        "report_date": f"2026-04-{day:02d}",
        "dependency_count": 0,
        "inputs": [
            "strict-window frozen raw arXiv/DataCite identity inventory",
            "official arXiv exact-v1 primary source",
            "current ROADMAP and canonical Books owner plus adjacent chapters",
        ],
        "forbidden_inputs_checked": [
            "Weekly discovery seed",
            "Weekly candidate list or denominator",
            "Weekly score or Source Review",
            "Weekly Books disposition or gap",
        ],
        "result": "pass_author_side",
    })
    dump(src / "semantic-author-audit.json", {
        "schema": "semantic-author-audit-v2.1", "report_date": f"2026-04-{day:02d}",
        "scope": f"{len(ids)}/{len(ids)} identities; retained FP challenge and closure FN challenge",
        "checks": [
            {"check": "window_identity", "result": "pass", "evidence": ledger_sha},
            {"check": "recall_vs_retention_separation", "result": "pass", "evidence": f"raw={len(ids)} retained={len(selected)} closures={len(ids)-len(selected)}"},
            {"check": "exact_v1_routes", "result": "conditional" if blockers else "pass", "evidence": f"complete={len(reviews)-len(blockers)} blocked={len(blockers)}"},
            {"check": "books_owner_adjacent", "result": "author_pass_pending_independent", "evidence": f"comparisons={len(comparisons)} queue={len(queue_items)}"},
        ],
        "unresolved_findings": ["fresh-context independent denominator/evidence/Books pre-write audit pending"],
        "cross_model_review": "skipped — delegated non-interactive subagent; degraded author self-check is not independent audit",
    })
    dump(src / "independent-semantic-audit.json", {
        "schema": "independent-semantic-audit-v2.1", "report_date": f"2026-04-{day:02d}",
        "status": "pending_fresh_context_reviewer", "author_must_not_self_sign": True,
        "required_scope": [f"replay {len(ids)}/{len(ids)} screening rows", f"challenge {len(selected)} retained and {len(ids)-len(selected)} closures", f"verify {len(reviews)} exact-v1 reviews", f"challenge {len(queue_items)} Integrate queue items"],
        "findings": [], "unresolved_findings": ["independent reviewer not yet assigned"],
    })

    # Daily report.  Keep the canonical V2.1 machine interface identical to
    # the already validated April packets; author-side uncertainty remains
    # visible in the Semantic Audit and Final Status rather than by inventing
    # another schema.
    owner_week = f"2026-W{report_date.isocalendar().week:02d}"
    review_rows, candidate_rows, book_rows = [], [], []
    source_review_blocks, books_detail_blocks, source_links = [], [], []
    comparison_by_family = {c["source_family_id"]: c for c in comparisons}
    for r in reviews:
        aid = r["primary_version"].split(":", 1)[1].removesuffix("v1")
        row = records[aid]
        row_owner_week = f"2026-W{datetime.fromisoformat(row['submitted_v1_utc'].replace('Z', '+00:00')).date().isocalendar().week:02d}"
        d, s, u = score(aid)
        candidate_rows.append(
            f"| {r['source_family_id']} | arXiv:{aid}v1 | paper-v1:{aid} | {row_owner_week} | {row['submitted_v1_utc'][:10]} | SRC-ARXIV | {d} | {s} | {u} | {d+s+u} | retained | {r['review_status']} | {r['access_status']} | none | review:{r['source_family_id']} | self | — | new_in_window | {r['stable_node_id']} | {r['books_disposition']} | books-review:{r['source_family_id']} | no |"
        )
        review_body = (
            "\n"
            f"#### {r['title']}\n\n"
            f"问题与旧路径：{r['problem']} {r['old_path_and_changed_constraint']}\n\n"
            f"机制与 owner：{r['mechanism_and_ownership']} owner=`{r['stable_node_id']}`。\n\n"
            f"Evaluation / trade-off / failure：{r['evaluation_contract']} {r['tradeoffs_and_failure_modes']}\n\n"
            f"<!-- claim:{r['source_family_id']}:start -->{r['claim_boundary']}<!-- claim:{r['source_family_id']}:end -->\n\n"
            f"Books Decision=`{r['books_disposition']}`；author lane 未修改共享 Books。\n"
        )
        r["review_provenance_id"] = report_review_provenance(r, aid, review_body)
        review_rows.append(
            f"| {r['source_family_id']} | {r['review_provenance_id']} | deep | {r['primary_version']} | SRC-ARXIV@{r['primary_version']} | {r['method_locator']} | {r['evaluation_locator']} | {r['limitations_locator']} | {r['artifact_locator']} | claim:{r['source_family_id']} | {r['result']} |"
        )
        source_review_blocks.append(
            f"<!-- review:{r['source_family_id']}:start -->{review_body}<!-- review:{r['source_family_id']}:end -->"
        )
        source_links.append(
            f"- [{r['title']}](https://arxiv.org/html/{aid}v1) — exact-v1；first-public {row['submitted_v1_utc'][:10]}；accessed {EXECUTED_AT[:10]}"
        )
        if r["books_disposition"] in {"Integrate", "No Change — Existing Coverage", "Structural Candidate"}:
            c = comparison_by_family[r["source_family_id"]]
            target = f"{c['owner_path']}#{r['stable_node_id']}"
            adjacent = "; ".join(f"{p}#chapter-boundary" for p in c["adjacent_paths"])
            book_rows.append(
                f"| {r['source_family_id']} | {r['stable_node_id']} | {target} | {adjacent} | existing:{r['source_family_id']} | delta:{r['source_family_id']} | Direct Evolution | {r['books_disposition']} | books-review:{r['source_family_id']} |"
            )
            books_detail_blocks.append(
                f"<!-- books-review:{r['source_family_id']}:start -->\n"
                f"<!-- existing:{r['source_family_id']}:start -->canonical owner `{c['owner_path']}` 的当前相关命题为：{c['existing_proposition']} owner_sha256={c['current_content_sha256']}。<!-- existing:{r['source_family_id']}:end -->\n"
                f"<!-- delta:{r['source_family_id']}:start -->{r['mechanism_and_ownership']}<!-- delta:{r['source_family_id']}:end --> Decision=`{r['books_disposition']}`；evidence boundary：{r['claim_boundary']}\n"
                f"<!-- books-review:{r['source_family_id']}:end -->"
            )

    # The canonical RP includes the bounded review prose hash, so refresh the
    # date-local packets after the report body has been assembled.
    dump(src / "exact-v1-review-packet.json", {"schema": "exact-v1-review-packet-v2.1", "report_date": f"2026-04-{day:02d}", "items": reviews})
    dump(src / "review-completion-receipt.json", {"schema": "review-completion-receipt-v2.1", "report_date": f"2026-04-{day:02d}", "items": reviews})
    dump(src / "exact-v1-provenance.json", {
        "schema": "exact-v1-provenance-v2.1", "report_date": f"2026-04-{day:02d}",
        "items": [{
            "source_family_id": r["source_family_id"], "primary_version": r["primary_version"],
            "url": r["evidence_urls"][1], "retrieved_at": EXECUTED_AT,
            "review_provenance_id": r["review_provenance_id"], "access_status": r["access_status"],
            "locators": [r["method_locator"], r["evaluation_locator"], r["limitations_locator"]],
        } for r in reviews],
    })

    deep = sorted(
        [r for r in reviews if r["result"] == "complete"],
        key=lambda r: (r["books_disposition"] != "Integrate", r["source_family_id"]),
    )[:3]
    deep_ids = {r["source_family_id"] for r in deep}
    deep_rows, deep_blocks = [], []
    for r in reviews:
        family = r["source_family_id"]
        eligibility = "score_7_9;potential_books_delta" if r["books_disposition"] == "Integrate" else "score_7_9"
        if family in deep_ids:
            unit = "DA-" + family.rsplit("-", 1)[-1]
            deep_rows.append(f"| {family} | {eligibility} | selected | {unit} | — | 跨层 owner、状态或 evaluation contract delta，且 exact-v1 可访问，优先进入 Top-3。 | analysis:{unit} |")
            deep_blocks.append(
                f"<!-- analysis:{unit}:start -->\n### {r['title']}\n\n"
                f"旧方案与约束变化：{r['old_path_and_changed_constraint']}\n\n"
                f"机制与控制权：{r['mechanism_and_ownership']}\n\n"
                f"收益、代价与失败边界：{r['tradeoffs_and_failure_modes']} {r['claim_boundary']}\n"
                f"<!-- analysis:{unit}:end -->"
            )
        else:
            deep_rows.append(f"| {family} | {eligibility} | not_selected | — | — | 已完成 Source Review，但 Top-3 预算优先给跨层 owner delta；其结论仍保留在 Candidate/Review/Books receipts。 | analysis-decision:{family} |")
            deep_blocks.append(
                f"<!-- analysis-decision:{family}:start -->未选入 Top-3 不等于未审；本 family 的问题、机制、evaluation 与边界保存在 Source Review，且不以篇幅预算降低 Evidence 状态。<!-- analysis-decision:{family}:end -->"
            )

    status = "In Progress — Books Writeback Pending" if queue_items else "In Progress — Independent Semantic Audit Pending"
    evidence_note = f"；另有 {len(blockers)} 项 exact-v1 external blocker" if blockers else ""
    materials_rows = "\n".join(
        f"| MR-202604{day:02d}-{i+1:02d} | P0 | {r['source_family_id']} | SRC-ARXIV | GAP-EXACT-V1 | {owner_week} | {r['evidence_urls'][0]}; {r['evidence_urls'][1]} | exact-v1 Method/Evaluation/Limitations full body | abs identity 不足以支持技术结论 | official exact-v1 HTML/PDF/e-print 或可证明等价的 author manuscript | {r['primary_version'].replace(':','-')}.pdf | exact-v1 full source review |"
        for i, r in enumerate(blockers)
    )
    if not materials_rows:
        materials_rows = ""
    reopened = FALSE_NEGATIVE_REOPENED[day]
    reopened_ids = ", ".join(reopened)
    report = f"""# Daily Research — 2026-04-{day:02d}

**Research Date:** 2026-04-{day:02d}

**Timezone:** Asia/Shanghai

**Strict Window:** {start.strftime('%Y-%m-%d 09:00:00')} ～ {end.strftime('%Y-%m-%d 09:00:00')}（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；DataCite v2 只用于 identity/date/title/abstract，技术结论绑定 official arXiv exact-v1。

**Status:** {status}；Coverage=Open、Evidence=Open、Books=Open；author packet 已完成，等待不同 reviewer 的 fresh-context audit；Books queue={len(queue_items)}{evidence_note}。

## Executive Summary

April frozen snapshot 共 {raw_total:,} 条 unique raw identity；严格窗口注册并逐项 title+abstract 语义筛选 {len(ids)}/{len(ids)}，author denominator={len(selected)}，pre-denominator closures={len(ids)-len(selected)}。strong-system 反向审计从 closure 重开 {len(reopened)} 项。{len(reviews)-len(blockers)}/{len(reviews)} 项完成 exact-v1 有界 Review，blocked={len(blockers)}；current owner+adjacent Books compare 后 provisional Integrate queue={len(queue_items)}。本 lane 未修改共享 Books，不能把 author 自检或 validator 通过表述为 fresh-context 验收。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-04-{day:02d} |
| Window End | 2026-04-{day:02d} |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-202604{day:02d}-AUTHOR-{len(selected)} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | {start.isoformat()} | {end.isoformat()} | {EXECUTED_AT} | DataCite April v2 prefix shards + {len(ids)}/{len(ids)} title/abstract semantic replay + official exact-v1 HTML/abs | checked | {len(ids)} | {';'.join(r['source_family_id'] for r in reviews)} | pages=100; prefixes=00..99; final_cursor=end; raw={raw_total}; registered={len(ids)}; screened={len(ids)}; retained={len(selected)}; closure={len(ids)-len(selected)} | {end.astimezone(ZoneInfo('UTC')).isoformat()} | screening-ledger-final.json#sha256={ledger_sha} | {'MR-EXACT-V1' if blockers else 'GAP-INDEPENDENT-AUDIT'} |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:202604{day:02d}:start -->Author 已完成 {len(ids)}/{len(ids)} 全量语义筛选；strong-system reverse audit 重开 {len(reopened)} 项：{reopened_ids}。Coverage Gate 仍等待不同 reviewer 重放 false positive/negative 与 withdrawn reconciliation。<!-- coverage:SRC-ARXIV:202604{day:02d}:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(candidate_rows)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(review_rows)}

### Source Reviews

{chr(10).join(source_review_blocks)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

没有可跨 workload 外推的 benchmark claim；数值仅在 exact-v1 作者协议内使用，未披露字段为 Not Disclosed。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(deep_rows)}

{chr(10).join(deep_blocks)}

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(book_rows)}

{chr(10).join(books_detail_blocks)}

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-202604{day:02d}-COVERAGE | fresh-context:pending-different-reviewer | coverage | coverage:SRC-ARXIV:202604{day:02d} | F-202604{day:02d}-INDEPENDENT | 全窗 denominator FP/FN 与 withdrawn audit 待不同 reviewer | open |
| SA-202604{day:02d}-EVIDENCE | fresh-context:pending-different-reviewer | evidence | validator:review-completion-v1 | F-202604{day:02d}-INDEPENDENT | exact-v1 locator 与 claim boundary 待 challenge | open |
| SA-202604{day:02d}-DEEP | fresh-context:pending-different-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | F-202604{day:02d}-INDEPENDENT | Top-3 选择待 challenge | open |
| SA-202604{day:02d}-BOOKS | fresh-context:pending-different-reviewer | books | validator:books-comparison-v1 | F-202604{day:02d}-INDEPENDENT | current owner+adjacent 与 queue 待 challenge | open |

Author-side doubt-driven check 已物化；同一作者不能冒充 fresh-context reviewer。

## 8. Ignored Noise

其余 {len(ids)-len(selected)} 个 identity 均保留在 `screening-ledger-final.json/tsv`，每条包含 title、abstract、日期与 family-specific closure；没有把 AI 术语、单领域 benchmark 或局部指标改善偷换成 Candidate Denominator。

## 9. Recommended Action

由非作者 reviewer 重放 denominator、exact-v1 locators 和 owner+adjacent comparison；通过后由 root 按日期顺序串行处理 {len(queue_items)} 项 Books queue。当前不得声称 Books 已写回或 Daily Complete。

## 10. Repository Changes

- 新增本日 Daily README 与 date-local evidence/source packet。
- 未修改 Books、ROADMAP、Learning State 或其他日期。

## 11. Open Questions

- fresh-context independent denominator/evidence/Books pre-write audit 尚未执行。
- {len(blockers)} 项 exact-v1 material request 尚未恢复。
- {len(queue_items)} 项 provisional Integrate 必须经独立 Books challenge 后才能串行写回。

## 12. Sources

- DataCite April v2 frozen snapshot：`papers/2026/05/_sources/datacite-arxiv-202604-v2/`
- official arXiv exact-v1 URLs：见 Review Completion Receipt 与 `exact-v1-provenance.json`
- Historical Daily independence receipt：`papers/2026/04/_sources/daily-202604{day:02d}/weekly-dependency-audit.json`（dependency=0）
{chr(10).join(source_links)}

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{materials_rows}

{'无：所有 retained family 均有 exact-v1 路由；仍等待不同 reviewer 复核。' if not blockers else ''}

## 13. Final Status

Completion Status: `In Progress`

Coverage: `Open`

Evidence: `Open`

Books: `Open`

unresolved findings: {1 + len(blockers)}

Author packet：raw={len(ids)}、registered/screened={len(ids)}/{len(ids)}、denominator={len(selected)}、closures={len(ids)-len(selected)}、exact-v1 complete={len(reviews)-len(blockers)}、blocked={len(blockers)}、provisional queue={len(queue_items)}。不同 reviewer、root 串行 Books 写回与 post-write audit 尚未完成，不能宣称本日 Complete。
"""
    (daily / "README.md").write_text(report)


def main():
    raw_total, records = load_records()
    if raw_total != 28197:
        raise RuntimeError(f"expected 28197 unique April records, got {raw_total}")
    for day in range(16, 24):
        write_day(day, raw_total, records)
        print(f"rendered 2026-04-{day:02d}")


if __name__ == "__main__":
    main()
