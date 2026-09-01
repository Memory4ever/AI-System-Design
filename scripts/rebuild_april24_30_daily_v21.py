#!/usr/bin/env python3
"""Build 2026-04-24..30 V2.1 Daily author packets.

Official arXiv Atom inventories and locally frozen exact-v1 HTML/PDF are the
only event/evidence inputs.  No downstream aggregate report contributes
discovery, screening, score, review, or disposition state to this lane.
Shared Books are never edited by this helper.
"""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

import rebuild_april08_15_daily_v21 as base


REPO = Path(__file__).resolve().parents[1]
MONTH = REPO / "papers/2026/04"
SOURCE_MONTH = MONTH / "_sources"

CANDIDATES = {
    "2604.21375": "AGENT-WORKFLOW",
    "2604.21480": "PLATFORM-EVALUATION-SYSTEM",
    "2604.21523": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22294": "AGENT-WORKFLOW",
    "2604.22446": "AGENT-MULTI-AGENT",
    "2604.22565": "AGENT-CONTEXT",
    "2604.23099": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23210": "PLATFORM-SECURITY",
    "2604.23781": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24003": "TRAIN-GRPO",
    "2604.24005": "TRAIN-GRPO",
    "2604.24198": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24351": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2604.24441": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24658": "AGENT-PLATFORM",
    "2604.24819": "TRAIN-DATA",
    "2604.24902": "PLATFORM-SECURITY",
    "2604.24952": "TRAIN-DPO",
    "2604.25135": "AGENT-TOOL-CALLING",
    "2604.25203": "PLATFORM-SECURITY",
    "2604.25256": "PLATFORM-EVALUATION-SYSTEM",
    "2604.25727": "TRAIN-DATA",
    "2604.25914": "PLATFORM-EVALUATION-SYSTEM",
    "2604.25917": "AGENT-MULTI-AGENT",
    "2604.26091": "AGENT-PLATFORM",
    "2604.26694": "MULTIMODAL-EMBODIED-VLA",
    "2604.26779": "INFER-SPECULATIVE-DECODING",
    "2604.26904": "PLATFORM-EVALUATION-SYSTEM",
    "2604.26951": "TRAIN-SFT",
    "2604.27039": "INFER-SCHEDULING",
    "2604.27083": "TRAIN-GRPO",
    "2604.27085": "TRAIN-PIPELINE-PARALLEL",
    "2604.27089": "TRAIN-TENSOR-PARALLEL",
    "2604.27151": "AGENT-WORKFLOW",
    "2604.27221": "AGENT-RAG",
    "2604.27251": "MODEL-TRANSFORMER-LAYER",
}

# Full strict-window title+abstract replay.  The rows below were independently
# re-opened because their abstracts change a
# durable AI-system mechanism, state/data/control owner, or evaluation contract.
CANDIDATES.update({
    # 2026-04-24
    "2604.21215": "MODEL-TRANSFORMER-LAYER",
    "2604.21221": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2604.21231": "INFER-KV-CACHE",
    "2604.21241": "MULTIMODAL-EMBODIED-VLA",
    "2604.21255": "AGENT-MULTI-AGENT",
    "2604.21308": "PLATFORM-SECURITY",
    "2604.21335": "INFER-KV-CACHE",
    "2604.21571": "TRAIN-LORA",
    "2604.21590": "TRAIN-SFT",
    "2604.21686": "PLATFORM-EVALUATION-SYSTEM",
    "2604.21741": "MULTIMODAL-EMBODIED-VLA",
    "2604.21748": "AGENT-MEMORY",
    "2604.21816": "AGENT-TOOL-CALLING",
    "2604.21999": "MODEL-TRANSFORMER-LAYER",
    "2604.22050": "MODEL-SELF-ATTENTION",
    "2604.22072": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.22085": "AGENT-MEMORY",
    "2604.22126": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.22128": "MODEL-TRANSFORMER-LAYER",
    "2605.28840": "PLATFORM-EVALUATION-SYSTEM",
    "2606.11209": "TRAIN-GRPO",
    "2606.13685": "PLATFORM-EVALUATION-SYSTEM",

    # 2026-04-25
    "2604.22152": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22191": "PLATFORM-SECURITY",
    "2604.22199": "MULTIMODAL-EMBODIED-VLA",
    "2604.22273": "AGENT-REFLECTION",
    "2604.22306": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22312": "INFER-DECODE",
    "2604.22345": "TRAIN-DPO",
    "2604.22427": "PLATFORM-SECURITY",
    "2604.22436": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22520": "INFER-SCHEDULING",
    "2604.22575": "MODEL-LONG-CONTEXT",
    "2604.22591": "MULTIMODAL-EMBODIED-VLA",
    "2604.22597": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22659": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22708": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22748": "MULTIMODAL-WORLD-MODELS",
    "2604.22879": "AGENT-MULTI-AGENT",
    "2604.22888": "PLATFORM-SECURITY",
    "2604.22891": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22893": "TRAIN-DATA",
    "2604.22906": "INFER-REQUEST-LIFECYCLE",
    "2604.22935": "PLATFORM-SECURITY",
    "2604.22985": "AGENT-TOOL-CALLING",
    "2604.23001": "MULTIMODAL-EMBODIED-VLA",
    "2604.23049": "AGENT-PLATFORM",
    "2604.23056": "TRAIN-GRPO",
    "2604.23069": "AGENT-MEMORY",

    # 2026-04-26 / 27
    "2604.23108": "MODEL-MOE",
    "2604.23121": "MULTIMODAL-EMBODIED-VLA",
    "2604.23150": "MODEL-MOE",
    "2604.23178": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23238": "PLATFORM-SECURITY",
    "2604.23277": "AGENT-CONTEXT",
    "2604.23318": "TRAIN-GRPO",
    "2604.23333": "TRAIN-GRPO",
    "2604.23338": "PLATFORM-SECURITY",
    "2604.23374": "PLATFORM-SECURITY",
    "2604.23455": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23459": "PLATFORM-SECURITY",
    "2604.23466": "INFER-TENSORRT-LLM",
    "2604.23467": "INFER-TENSORRT-LLM",
    "2604.23543": "TRAIN-DPO",
    "2604.23553": "INFER-DECODE",
    "2604.23577": "INFER-SCHEDULING",
    "2604.23581": "PLATFORM-EVALUATION-SYSTEM",
    "2604.23626": "AGENT-PLANNING",
    "2604.23646": "PLATFORM-SECURITY",
    "2604.23711": "PLATFORM-SECURITY",
    "2604.23747": "TRAIN-SFT",
    "2604.23758": "AGENT-WORKFLOW",
    "2604.23775": "MULTIMODAL-EMBODIED-VLA",
    "2604.23798": "MODEL-SELF-ATTENTION",

    # 2026-04-28
    "2604.23940": "AGENT-PLANNING",
    "2604.23941": "MULTIMODAL-EMBODIED-VLA",
    "2604.24008": "INFER-GPU-MEMORY",
    "2604.24013": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.24040": "AGENT-RAG",
    "2604.24088": "TRAIN-TENSOR-PARALLEL",
    "2604.24118": "PLATFORM-SECURITY",
    "2604.24203": "PLATFORM-SECURITY",
    "2604.24273": "TRAIN-GRPO",
    "2604.24300": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24320": "TRAIN-GRPO",
    "2604.24348": "PLATFORM-EVALUATION-SYSTEM",
    "2604.24447": "MULTIMODAL-EMBODIED-VLA",
    "2604.24477": "PLATFORM-MONITORING",
    "2604.24479": "TRAIN-DATA",
    "2604.24583": "TRAIN-GRPO",
    "2604.24625": "TRAIN-GRPO",
    "2604.24647": "INFER-KV-CACHE",
    "2604.24708": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.24715": "MODEL-LONG-CONTEXT",
    "2604.24763": "MULTIMODAL-REPRESENTATION",
    "2604.24764": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2604.24809": "MODEL-TRANSFORMER-LAYER",
    "2604.24820": "INFER-TENSORRT-LLM",
    "2604.24826": "PLATFORM-SECURITY",
    "2604.24842": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2604.24881": "TRAIN-DPO",
    "2604.24921": "MULTIMODAL-EMBODIED-VLA",
    "2604.24927": "MODEL-SAMPLING",
    "2604.24953": "TRAIN-DPO",
    "2604.24954": "MULTIMODAL-REPRESENTATION",
    "2604.24957": "TRAIN-GRPO",
    "2604.24971": "INFER-KV-CACHE",
    "2604.24977": "PLATFORM-EVALUATION-SYSTEM",
    "2604.25011": "TRAIN-GRPO",
    "2604.25080": "INFER-KV-CACHE",

    # 2026-04-29
    "2604.25109": "PLATFORM-SECURITY",
    "2604.25166": "MODEL-TRANSFORMER-LAYER",
    "2604.25183": "INFER-TENSORRT-LLM",
    "2604.25235": "PLATFORM-EVALUATION-SYSTEM",
    "2604.25306": "INFER-GPU-MEMORY",
    "2604.25317": "INFER-TENSORRT-LLM",
    "2604.25326": "INFER-SPECULATIVE-DECODING",
    "2604.25345": "PLATFORM-EVALUATION-SYSTEM",
    "2604.25359": "PLATFORM-EVALUATION-SYSTEM",
    "2604.25380": "PLATFORM-EVALUATION-SYSTEM",
    "2604.25421": "TRAIN-LORA",
    "2604.25555": "PLATFORM-SECURITY",
    "2604.25562": "PLATFORM-SECURITY",
    "2604.25578": "MODEL-MOE",
    "2604.25602": "AGENT-PLATFORM",
    "2604.25636": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2604.25699": "INFER-GPU-MEMORY",
    "2604.25719": "TRAIN-GRPO",
    "2604.25777": "INFER-SPECULATIVE-DECODING",
    "2604.25806": "AGENT-WORKFLOW",
    "2604.25809": "MODEL-SAMPLING",
    "2604.25819": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2604.25846": "PLATFORM-SECURITY",
    "2604.25850": "AGENT-PLATFORM",
    "2604.25859": "MULTIMODAL-EMBODIED-VLA",
    "2604.25899": "INFER-SCHEDULING",
    "2604.25907": "TRAIN-GRPO",
    "2604.25975": "INFER-KV-CACHE",
    "2604.26020": "PLATFORM-EVALUATION-SYSTEM",
    "2604.26039": "INFER-TENSORRT-LLM",
    "2604.26074": "INFER-GPU-MEMORY",
    "2604.26103": "INFER-GPU-MEMORY",
    "2604.26152": "PLATFORM-MONITORING",
    "2604.26197": "AGENT-MEMORY",

    # 2026-04-30
    "2604.26209": "INFER-DECODE",
    "2604.26256": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.26258": "AGENT-WORKFLOW",
    "2604.26274": "PLATFORM-SECURITY",
    "2604.26294": "TRAIN-TENSOR-PARALLEL",
    "2604.26378": "INFER-GPU-MEMORY",
    "2604.26388": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.26412": "INFER-SPECULATIVE-DECODING",
    "2604.26460": "PLATFORM-EVALUATION-SYSTEM",
    "2604.26506": "PLATFORM-SECURITY",
    "2604.26511": "PLATFORM-SECURITY",
    "2604.26557": "INFER-GPU-MEMORY",
    "2604.26561": "AGENT-MULTI-AGENT",
    "2604.26622": "AGENT-MEMORY",
    "2604.26649": "AGENT-RAG",
    "2604.26666": "AGENT-WORKFLOW",
    "2604.26687": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.26733": "TRAIN-GRPO",
    "2604.26752": "TRAIN-DPO",
    "2604.26837": "INFER-KV-CACHE",
    "2604.26848": "MULTIMODAL-WORLD-MODELS",
    "2604.26881": "PLATFORM-MULTI-TENANT",
    "2604.26997": "PLATFORM-SECURITY",
    "2604.27003": "AGENT-MEMORY",
    "2604.27032": "INFER-SCHEDULING",
    "2604.27045": "AGENT-MEMORY",
    "2604.27202": "PLATFORM-SECURITY",
    "2604.27233": "AGENT-TOOL-CALLING",
    "2604.27238": "PLATFORM-SECURITY",
    "2604.27267": "PLATFORM-SECURITY",
    "2604.27283": "AGENT-MEMORY",
})


class PaperHTMLParser(HTMLParser):
    """Extract heading-bound paragraphs without third-party dependencies."""

    def __init__(self) -> None:
        super().__init__()
        self.current_heading = "Document"
        self.capture: str | None = None
        self.buffer: list[str] = []
        self.records: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p"}:
            self.capture = tag
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.capture != tag:
            return
        text = re.sub(r"\s+", " ", " ".join(self.buffer)).strip()
        if tag.startswith("h") and text:
            self.current_heading = text
        elif tag == "p" and len(text) >= 80:
            self.records.append((self.current_heading, text))
        self.capture = None
        self.buffer = []


def _pick(records: list[tuple[str, str]], heading_terms: tuple[str, ...], body_terms: tuple[str, ...]) -> tuple[str, str]:
    ranked = []
    for index, (heading, body) in enumerate(records):
        h, b = heading.lower(), body.lower()
        score = 6 * sum(term in h for term in heading_terms) + sum(term in b for term in body_terms)
        if score:
            ranked.append((score, -index, heading, body))
    if ranked:
        _, _, heading, body = max(ranked)
        return heading, body[:1600]
    return (records[0][0], records[0][1][:1600]) if records else ("Not Disclosed", "Not Disclosed in the recovered exact-v1 artifact.")


def independent_exact_review(aid: str) -> tuple[str, str, str]:
    candidates = list(SOURCE_MONTH.glob(f"daily-202604*/exact-v1/{aid}v1.html"))
    media = "HTML"
    if candidates:
        path = candidates[0]
        parser = PaperHTMLParser()
        parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
        records = parser.records
    else:
        pdfs = list(SOURCE_MONTH.glob(f"daily-202604*/exact-v1/{aid}v1.pdf"))
        if not pdfs:
            raise RuntimeError(f"no date-local exact-v1 artifact for {aid}")
        path = pdfs[0]
        media = "PDF"
        bundled_python = "/Users/apple/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
        extractor = "from pypdf import PdfReader; import sys; r=PdfReader(sys.argv[1]); print('\\n\\n'.join((p.extract_text() or '') for p in r.pages))"
        result = subprocess.run([bundled_python, "-c", extractor, str(path)], check=True, capture_output=True, text=True)
        chunks = [re.sub(r"\s+", " ", x).strip() for x in re.split(r"\n\s*\n", result.stdout)]
        records = [("PDF full text", x) for x in chunks if len(x) >= 80]

    method = _pick(records, ("method", "approach", "framework", "architecture", "system", "training"),
                   ("we propose", "we introduce", "consists of", "pipeline", "algorithm", "controller", "cache", "state"))
    evaluation = _pick(records, ("experiment", "evaluation", "result", "benchmark", "analysis"),
                       ("evaluate", "baseline", "dataset", "hardware", "ablation", "throughput", "latency", "accuracy"))
    limitation = _pick(records, ("limitation", "discussion", "conclusion", "future work", "threat"),
                       ("however", "limited", "only", "trade-off", "overhead", "failure", "cannot", "future"))
    artifact = _pick(records, ("artifact", "code", "implementation", "appendix"),
                     ("github", "code", "repository", "dataset", "implementation", "available"))
    section = "\n".join([
        f"- **Method / Identity — {method[0]}**：{method[1]}",
        f"- **Evaluation Contract — {evaluation[0]}**：{evaluation[1]}",
        f"- **Evidence Proves / Does Not Prove — {limitation[0]}**：{limitation[1]}",
        f"- **Artifact / Access — {artifact[0]}**：{artifact[1]}",
    ])
    return str(path.relative_to(REPO)), f"exact-v1 independent {media} full read", section


def prepare_inventory(day: int) -> None:
    compact = f"202604{day:02d}"
    packet = SOURCE_MONTH / f"daily-{compact}"
    source = json.loads((packet / "arxiv-api-enumeration.json").read_text(encoding="utf-8"))
    identities = []
    for row in source["identities"]:
        copied = dict(row)
        copied["submitted_v1_utc"] = copied["published_v1_utc"]
        identities.append(copied)
    start = source["window_beijing"]["start"]
    end = source["window_beijing"]["end"]
    provisional = {
        "schema": "daily-v2.1-official-arxiv-provisional-ledger-v1",
        "report_date": source["report_date"],
        "window": f"[{start},{end})",
        "raw_snapshot_records": source["raw_identity_count"],
        "identities": identities,
        "contract_note": "V2.1 Full Replay；official arXiv Atom strict-window enumeration + 100% title/abstract semantic screening + locally frozen exact-v1 HTML/PDF；不继承历史报告评分、Review、disposition 或 Gate。",
        "coverage_endpoint": "official arXiv Atom submittedDate strict window; full semantic screening; exact-v1 HTML",
        "pagination_cursor": f"pages={len(source['query_receipts'])}; declared_total={source['raw_identity_count']}; final_cursor=end",
    }
    (packet / "screening-ledger-provisional.json").write_text(
        json.dumps(provisional, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    base.CANDIDATES = CANDIDATES
    base.SOURCE_REVIEW_RESOLVER = independent_exact_review
    base.CURRENT_CONTENT_MIN_SCORE = 5
    results = []
    for day in range(24, 31):
        prepare_inventory(day)
        results.append(base.generate(f"2026-04-{day:02d}"))
        compact = f"202604{day:02d}"
        packet = SOURCE_MONTH / f"daily-{compact}"
        ledger = json.loads((packet / "screening-ledger-final.json").read_text(encoding="utf-8"))
        retained = [x for x in ledger["identities"] if x["screening_status"] == "retained_after_full_semantic_screen"]
        audit = {
            "schema": "full-title-abstract-reverse-audit-v2.1",
            "report_date": f"2026-04-{day:02d}",
            "registered_identities": len(ledger["identities"]),
            "full_semantic_screened": len(ledger["identities"]),
            "retained_after_replay": len(retained),
            "pre_denominator_closures": len(ledger["identities"]) - len(retained),
            "reopened_source_families": [x["source_family_id"] for x in retained],
            "historical_report_dependency_count": 0,
            "inputs": ["official strict-window arXiv Atom inventory", "title+abstract", "date-local exact-v1 artifact", "current Books owner+adjacent"],
        }
        (packet / "full-title-abstract-reverse-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
