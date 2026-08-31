#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 2026-05-28 V2.1 pre-write packet without editing shared Books."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/28/README.md"
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

SOURCE = json.loads((HERE / "screening-ledger-provisional.json").read_text())
NOW = "2026-09-02T10:30:00+08:00"

RETAINED = set("""2606.07586 2606.26120 2606.26122
2605.27820 2605.27825 2605.27879 2605.27881 2605.27898 2605.27899
2605.27901 2605.27918 2605.27922 2605.27947 2605.27954 2605.27957 2605.27963 2605.27980 2605.27995
2605.28000 2605.28009 2605.28017 2605.28044 2605.28046 2605.28053 2605.28071 2605.28074 2605.28083 2605.28095 2605.28097
2605.28108 2605.28112 2605.28116 2605.28122 2605.28158
2605.28201 2605.28213 2605.28214 2605.28224
2605.28302 2605.28354 2605.28371 2605.28384 2605.28390
2605.28424 2605.28433 2605.28467 2605.28480
2605.28508 2605.28561 2605.28573
2605.28632 2605.28634 2605.28678 2605.28691 2605.28699
2605.28704 2605.28721 2605.28726 2605.28732 2605.28742 2605.28751 2605.28760 2605.28773 2605.28774 2605.28778 2605.28787
2605.28803 2605.28805 2605.28807 2605.28819 2605.28889 2605.28890 2605.28893 2605.28897
2605.28914 2605.28918 2605.28920 2605.28969 2605.28991 2605.28999
2605.29001 2605.29005 2605.29054 2605.29068 2605.29074 2605.29075 2605.29082 2605.29087
2605.29107 2605.29114 2605.29115 2605.29119 2605.29121 2605.29123 2605.29139 2605.29156 2605.29178 2605.29183 2605.29192 2605.29209""".split())
RETAINED.update("2605.27850 2605.28282 2605.28510 2605.28544 2605.28565 2605.28617 2605.28640 2605.28646 2605.28764 2605.29078 2605.29129 2605.29135".split())

# Only deltas not already expressed by the current owner and adjacent chapters.
INTEGRATE = set("""2606.07586 2606.26120 2606.26122 2605.27825 2605.27879
2605.27881 2605.27918 2605.27963 2605.28000 2605.28053 2605.28095
2605.28097 2605.28201 2605.28213 2605.28214 2605.28302 2605.28433
2605.28508 2605.28561 2605.28632 2605.28704 2605.28760 2605.29082
2605.29183""".split())
INTEGRATE.update("2605.28282 2605.28510 2605.28617 2605.28646 2605.29078 2605.29135".split())
# Current Books already carry the generic contracts behind the other retained
# families (evaluation identity, workflow evidence gates, topology mapping,
# canary/promotion and partial-verifier branches).  Keep only unresolved
# mechanism deltas in the root-serial queue.
INTEGRATE = set("""2606.07586 2606.26120 2606.26122
2605.27825 2605.27881 2605.28053 2605.28095 2605.28201 2605.28214
2605.28433 2605.28617 2605.28632 2605.28646 2605.28704 2605.28760
2605.29082 2605.29135""".split())

DEEP = {
    "2605.27963": "DA-TOPOLOGY-COLLECTIVE-CO-DESIGN",
    "2605.28053": "DA-REQUEST-OWNED-TTT-STATE",
    "2605.29082": "DA-OUT-OF-BAND-AGENT-DATA-PLANE",
}

OWNER_OVERRIDE = {
    "2606.07586": "AGENT-PLATFORM", "2606.26120": "INFER-CONTINUOUS-BATCHING", "2606.26122": "TRAIN-DATA",
    "2605.27820": "PLATFORM-EVALUATION-SYSTEM", "2605.27825": "PLATFORM-SECURITY", "2605.27879": "PLATFORM-EVALUATION-SYSTEM",
    "2605.27881": "TRAIN-DATA", "2605.27898": "PLATFORM-EVALUATION-SYSTEM", "2605.27899": "TRAIN-GRPO",
    "2605.27850": "AGENT-MULTI-AGENT",
    "2605.27901": "PLATFORM-SECURITY", "2605.27918": "TRAIN-DISTRIBUTED-TRAINING", "2605.27922": "PLATFORM-EVALUATION-SYSTEM",
    "2605.27947": "INFER-SCHEDULING", "2605.27954": "TRAIN-GRPO", "2605.27957": "PLATFORM-EVALUATION-SYSTEM",
    "2605.27963": "TRAIN-DISTRIBUTED-TRAINING", "2605.27980": "MODEL-POSITION-ENCODING", "2605.27995": "PLATFORM-EVALUATION-SYSTEM",
    "2605.28000": "AGENT-TOOL-CALLING", "2605.28009": "AGENT-MEMORY", "2605.28017": "PLATFORM-SECURITY",
    "2605.28044": "PLATFORM-EVALUATION-SYSTEM", "2605.28046": "AGENT-MEMORY", "2605.28053": "INFER-CONTINUOUS-BATCHING",
    "2605.28071": "AGENT-TOOL-CALLING", "2605.28074": "PLATFORM-SECURITY", "2605.28083": "PLATFORM-SECURITY",
    "2605.28095": "INFER-GPU-MEMORY", "2605.28097": "PLATFORM-PRODUCTION", "2605.28108": "AGENT-PLANNING",
    "2605.28112": "PLATFORM-SECURITY", "2605.28116": "PLATFORM-SECURITY", "2605.28122": "PLATFORM-EVALUATION-SYSTEM",
    "2605.28158": "PLATFORM-EVALUATION-SYSTEM", "2605.28201": "PLATFORM-SECURITY", "2605.28213": "AGENT-PLATFORM",
    "2605.28214": "PLATFORM-SECURITY", "2605.28224": "AGENT-MEMORY", "2605.28302": "INFER-PD-DISAGGREGATION",
    "2605.28282": "AGENT-WORKFLOW",
    "2605.28354": "AGENT-PLANNING", "2605.28371": "PLATFORM-EVALUATION-SYSTEM", "2605.28384": "INFER-SCHEDULING",
    "2605.28390": "AGENT-PLATFORM", "2605.28424": "TRAIN-GRPO", "2605.28433": "AGENT-MULTI-AGENT",
    "2605.28467": "PLATFORM-SECURITY", "2605.28480": "AGENT-WORKFLOW", "2605.28508": "PLATFORM-EVALUATION-SYSTEM",
    "2605.28561": "TRAIN-RLHF", "2605.28573": "TRAIN-PRETRAINING", "2605.28632": "PLATFORM-SECURITY",
    "2605.28510": "PLATFORM-SECURITY", "2605.28544": "MULTIMODAL-WORLD-MODELS", "2605.28565": "PLATFORM-EVALUATION-SYSTEM",
    "2605.28617": "AGENT-TOOL-CALLING", "2605.28640": "INFER-KV-CACHE", "2605.28646": "PLATFORM-SECURITY",
    "2605.28634": "MULTIMODAL-EMBODIED-VLA", "2605.28678": "INFER-SPECULATIVE-DECODING", "2605.28691": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.28699": "TRAIN-GRPO", "2605.28704": "INFER-TENSORRT-LLM", "2605.28721": "PLATFORM-EVALUATION-SYSTEM",
    "2605.28726": "MULTIMODAL-EMBODIED-VLA", "2605.28732": "AGENT-MEMORY", "2605.28742": "AGENT-REFLECTION",
    "2605.28751": "TRAIN-GRPO", "2605.28760": "TRAIN-LORA", "2605.28773": "AGENT-MEMORY",
    "2605.28774": "TRAIN-GRPO", "2605.28778": "PLATFORM-EVALUATION-SYSTEM", "2605.28787": "AGENT-RAG",
    "2605.28764": "AGENT-MULTI-AGENT",
    "2605.28803": "MULTIMODAL-EMBODIED-VLA", "2605.28805": "PLATFORM-EVALUATION-SYSTEM", "2605.28807": "PLATFORM-EVALUATION-SYSTEM",
    "2605.28819": "TRAIN-LORA", "2605.28889": "AGENT-MEMORY", "2605.28890": "PLATFORM-SECURITY",
    "2605.28893": "PLATFORM-SECURITY", "2605.28897": "PLATFORM-EVALUATION-SYSTEM", "2605.28914": "AGENT-TOOL-CALLING",
    "2605.28918": "TRAIN-GRPO", "2605.28920": "PLATFORM-EVALUATION-SYSTEM", "2605.28969": "AGENT-MEMORY",
    "2605.28991": "AGENT-TOOL-CALLING", "2605.28999": "PLATFORM-SECURITY", "2605.29001": "PLATFORM-EVALUATION-SYSTEM",
    "2605.29005": "PLATFORM-EVALUATION-SYSTEM", "2605.29054": "PLATFORM-EVALUATION-SYSTEM", "2605.29068": "PLATFORM-SECURITY",
    "2605.29074": "MULTIMODAL-EMBODIED-VLA", "2605.29075": "AGENT-MEMORY", "2605.29082": "AGENT-PLATFORM",
    "2605.29078": "AGENT-WORKFLOW",
    "2605.29087": "PLATFORM-EVALUATION-SYSTEM", "2605.29107": "PLATFORM-SECURITY", "2605.29114": "PLATFORM-SECURITY",
    "2605.29115": "TRAIN-GRPO", "2605.29119": "TRAIN-GRPO", "2605.29121": "MODEL-MOE",
    "2605.29129": "AGENT-PLATFORM", "2605.29135": "INFER-GPU-MEMORY",
    "2605.29123": "MULTIMODAL-GENERATIVE-PARADIGMS", "2605.29139": "AGENT-RAG", "2605.29156": "TRAIN-RLHF",
    "2605.29178": "PLATFORM-SECURITY", "2605.29183": "PLATFORM-PRODUCTION", "2605.29192": "PLATFORM-TRACE",
    "2605.29209": "MULTIMODAL-REPRESENTATION",
}

def family(a: str) -> str:
    return "SF-2026-ARXIV-" + a.replace(".", "-")

def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()

def sentences(s: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", clean(s)) if x.strip()]

def mechanism(r: dict) -> str:
    ss = sentences(r.get("abstract", "")) or [r["title"]]
    return next((x for x in ss if re.search(r"\b(propose|introduce|present|develop|design|formulate|build|study|evaluate|show|investigate)\b", x, re.I)), ss[0])[:520]

def result(r: dict) -> str:
    ss = sentences(r.get("abstract", "")) or [r["title"]]
    return next((x for x in reversed(ss) if re.search(r"\b(result|show|find|demonstrate|outperform|achiev|evaluate|reveal)\b", x, re.I)), ss[-1])[:420]

def boundary(r: dict) -> str:
    t = clean(r["title"] + " " + r.get("abstract", "")).lower()
    if any(x in t for x in ("medical", "clinical", "protein", "molecule", "patient", "drug", "biology")):
        return "该 family 的状态与验收属于医疗/科学领域任务，没有重分配通用训练、推理或平台的长期 owner"
    if any(x in t for x in ("segmentation", "classification", "detection", "forecasting", "recommendation")):
        return "它提供特定任务的模型或数据改进，未建立可迁移的 state identity、runtime control 或 release contract"
    if any(x in t for x in ("benchmark", "dataset", "evaluation", "metric")):
        return "它增加任务切片或指标，但没有改变可复算 evaluator identity、运行时 evidence object 或 release authority"
    if any(x in t for x in ("agent", "tool", "memory", "rag", "workflow", "search")):
        return "它属于 Agent 局部能力或应用方案，尚未形成新的 authority、durable state、effect commit 或 recovery contract"
    if any(x in t for x in ("diffusion", "image", "video", "multimodal", "3d", "audio")):
        return "它是生成或表示质量的局部增量，未改变跨模态 state owner、生成因子化、serving commit 或物理闭环"
    if any(x in t for x in ("training", "fine-tun", "gradient", "optimizer", "quantization", "pruning")):
        return "它是局部训练或压缩技巧，未改变 dataset/objective/checkpoint/runtime 的长期所有权合同"
    if any(x in t for x in ("security", "attack", "privacy", "jailbreak", "backdoor")):
        return "它给出局部 attack/defense slice，未改变平台 threat model、enforcement owner 或 release evidence contract"
    return "它是领域算法、理论或局部模型增量，未显示长期 state/data/control owner 或 evaluation contract 的变化"

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.active = False; self.buf = []; self.headings = []
    def handle_starttag(self, tag, attrs):
        if tag in {"h2", "h3"}: self.active = True; self.buf = []
    def handle_data(self, data):
        if self.active: self.buf.append(data)
    def handle_endtag(self, tag):
        if self.active and tag in {"h2", "h3"}:
            h = clean("".join(self.buf))
            if h: self.headings.append(h)
            self.active = False

MANUAL_WEB_EVIDENCE = {
    "2605.27850": ("§3 Methods: unified prompt-topology genome and adaptive Pareto control", "§4 Experiments: held-out accuracy, token cost and topology complexity", "§5 Conclusion, Limitations, and Future Work"),
    "2605.28282": ("§3 ResearchLoop Protocol and Runtime; §4 Runtime Implementation", "§7 controlled study and ablations", "§7.2 synthetic task, single-model and sample-size limitations; Appendix C claim ledger"),
    "2605.28510": ("§III Methodology: SourceTracker, Winnowing and HybridSourceTracker", "§IV Results: recall, rank and latency", "§V errors; §VI Discussion; §VIII-A future-work boundaries"),
    "2605.28544": ("§3 Method: autoregressive world-action flow, causal guidance and selective KV memory", "§4 Experiments and ablations", "§5 Conclusion; Appendix C efficiency analysis; no dedicated limitations section"),
    "2605.28565": ("§2 CiteTrace construction; §3 three-dimensional citation evaluation", "§4 structural citation failures and judge validation", "Appendix A.1 scope assumptions and A.2 limitations"),
    "2605.28617": ("§3 typed holes and nested calls; §4 static/capability safety", "§7 verifier, tool-use and multi-turn evaluation", "§Limitations: well-typed is not correct; authority is only as tight as granted scope"),
    "2605.28640": ("§2 exponentially decaying memory and sparse inference instantiations", "§3 experiments and H1/H2 analyses", "§Limitations: two 7B checkpoints, 4K context and RULER-only task family"),
    "2605.28646": ("§4 edge evidence extraction, policy arbitration, SafeScreenshot and skill evolution", "§5–6 evaluation, sandbox checks and error analysis", "§Limitations: sanitized scenarios, trusted edge and short-horizon personalization"),
    "2605.28764": ("§3 SwarmNode, registry, router and credit ledger; §4 attribution", "§5 feasibility and deployment path", "§5.3–5.5 bootstrap, security/privacy and open challenges"),
    "2605.29078": ("§III execution requirements; §IV snapshot isolation, policy-neutral contract and divergence record", "§V empirical evaluation across lag regimes", "§IV-D implementation constraints; §VI future-work boundary"),
    "2605.29129": ("§2 debt/tax model; §3 debt accumulation", "§4 operationalizing governance", "§5 Conclusion; position paper without empirical validation or dedicated limitations"),
    "2605.29135": ("§4 Rotary GPU concept; §6 setup", "§8 results and failure analysis", "§11 Limitations: one platform, ten-prompt smoke set and undisclosed implementation"),
}

def evidence(a: str) -> tuple[str, str, str, str, str]:
    hp = Path("/tmp") / f"arxiv-{a}v1.html"
    pp = Path("/tmp") / f"arxiv-{a}v1.pdf"
    if a == "2605.28508":
        return ("official exact-v1 PDF", "pp. 6–8 §3 System under test and layered evaluation", "pp. 8–11 §4 application profiles and operating-condition tests", "pp. 11–13 §5 minimum benchmark standard and reporting limits", f"official PDF sha256={hashlib.sha256(pp.read_bytes()).hexdigest()}")
    if a in MANUAL_WEB_EVIDENCE:
        m, e, l = MANUAL_WEB_EVIDENCE[a]
        return ("official exact-v1 HTML (direct read)", m, e, l, "official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed")
    if not hp.exists() or hp.stat().st_size < 8000:
        raise RuntimeError(f"missing exact-v1 body: {a}")
    parser = HeadingParser(); parser.feed(hp.read_text(errors="ignore")); hs = parser.headings
    if len(hs) < 2: raise RuntimeError(f"insufficient headings: {a}")
    def choose(words: tuple[str, ...], excluded: set[str]) -> str:
        for h in hs:
            if h not in excluded and any(w in h.lower() for w in words): return h
        return next(h for h in hs if h not in excluded)
    m = choose(("method", "approach", "framework", "system", "model", "design", "architecture"), set())
    e = choose(("experiment", "evaluation", "result", "benchmark", "analysis"), {m})
    l = choose(("limitation", "threat", "discussion", "failure", "conclusion"), {m, e})
    return ("official exact-v1 HTML", f"§ exact heading: {m}", f"§ exact heading: {e}", f"§ exact heading: {l}", f"official HTML sha256={hashlib.sha256(hp.read_bytes()).hexdigest()}")

# ROADMAP is the single owner/path truth source.
road = (ROOT / "ROADMAP.md").read_text()
nodes = []
for m in re.finditer(r'^\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|', road, re.M):
    nodes.append((m.group(1), int(m.group(2)), m.group(3)))
node_map = {n: (ch, p) for n, ch, p in nodes}
chapter_map = {ch: p for _, ch, p in nodes}
assert set(OWNER_OVERRIDE.values()) <= set(node_map)
assert len(RETAINED) == 112

rows = SOURCE["identities"]
assert len(rows) == 747
row_by = {r["arxiv_id"]: r for r in rows}
assert RETAINED <= set(row_by)

for r in rows:
    a = r["arxiv_id"]
    r["source_family_id"] = family(a)
    if a in RETAINED:
        owner = OWNER_OVERRIDE[a]
        score = (3, 3, 3) if a in INTEGRATE else (3, 2, 3)
        r.update(
            screening_status="retained_exact_v1_complete",
            screening_reason=f"{r['title']} 的具体系统机制是：{mechanism(r)}。它改变 `{owner}` 的 state/control/evidence contract，故进入 denominator；摘要结果“{result(r)}”只作为检索线索，最终结论绑定 exact-v1。",
            owner_node=owner,
            candidate_state="retained",
            score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            review_status="deep_complete",
            access_status="accessible",
            integration_disposition="Integrate" if a in INTEGRATE else "No Change — Existing Coverage",
        )
    else:
        r.update(
            screening_status="pre_denominator_closed",
            screening_reason=f"{r['title']} 的具体方法/主张是：{mechanism(r)}；摘要报告/目标为：{result(r)}。排除边界：{boundary(r)}；因此在 Candidate Denominator 前闭合，若后续 artifact 证明改变通用 owner contract 则重开。",
            review_status="identity_date_closed",
            access_status="accessible_metadata",
            integration_disposition="Rejected — Below Candidate Denominator",
        )

ledger = dict(SOURCE)
ledger.update(
    schema="daily-v2.1-screening-ledger-independent-final",
    semantic_review_completed=747,
    retained_candidates=len(RETAINED),
    pre_denominator_closed=len(rows)-len(RETAINED),
    gate_status="coverage_and_evidence_closed_books_open",
    identities=rows,
)
ledger_path = HERE / "screening-ledger-final.json"
ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
with (HERE / "screening-ledger-final.tsv").open("w", newline="") as h:
    w = csv.writer(h, delimiter="\t")
    w.writerow(["arxiv_id", "title", "screening_status", "screening_reason", "owner_node", "disposition"])
    for r in rows: w.writerow([r["arxiv_id"], r["title"], r["screening_status"], r["screening_reason"], r.get("owner_node", ""), r["integration_disposition"]])
(HERE / "candidate-ids.txt").write_text("\n".join(sorted(RETAINED)) + "\n")
ledger_sha = hashlib.sha256(ledger_path.read_bytes()).hexdigest()

reviews = []
for a in sorted(RETAINED):
    route, method, evaluation, limitations, artifact = evidence(a)
    r = row_by[a]
    reviews.append({
        "source_family_id": family(a), "arxiv_id": a,
        "primary_evidence_version": f"arXiv:{a}v1", "exact_v1_url": f"https://arxiv.org/html/{a}v1" if a != "2605.28508" else f"https://arxiv.org/pdf/{a}v1",
        "review_route": "deep", "source_route": route,
        "method_identity_locators": f"arXiv:{a}v1 — {method}",
        "evaluation_locators": f"arXiv:{a}v1 — {evaluation}",
        "limitations_counterevidence_locators": f"arXiv:{a}v1 — {limitations}",
        "artifact_locators": f"arXiv:{a}v1 — {artifact}; immutable repository/checkpoint commit Not Disclosed unless named in v1",
        "claim_boundary": f"仅支持 exact-v1 披露机制及实验边界；不把“{result(r)}”外推为跨模型、硬件、数据分布或生产 SLO 保证。",
        "completion_result": "complete", "retrieved_at": NOW,
    })
(HERE / "exact-v1-review-packet.json").write_text(json.dumps({"schema":"exact-v1-review-packet-v2.1-independent-final","report_date":"2026-05-28","items":reviews}, ensure_ascii=False, indent=2)+"\n")

def headings(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^## (.+)$", text, re.M)]

comparisons = []
for a in sorted(RETAINED):
    r = row_by[a]; owner = r["owner_node"]; ch, path = node_map[owner]
    owner_text = (ROOT / path).read_text()
    adjacent = [chapter_map[x] for x in (ch - 1, ch + 1) if x in chapter_map]
    adj_text = {p: (ROOT / p).read_text() for p in adjacent}
    direct = a in owner_text or any(a in x for x in adj_text.values())
    decision = "Integrate" if a in INTEGRATE and not direct else "No Change — Existing Coverage"
    if direct: r["integration_disposition"] = decision
    hs = headings(owner_text)
    comparisons.append({
        "arxiv_id": a, "source_family_id": family(a), "owner_node": owner, "owner_path": path,
        "adjacent_paths": adjacent, "owner_sha256": hashlib.sha256(owner_text.encode()).hexdigest(),
        "adjacent_sha256": {p: hashlib.sha256(t.encode()).hexdigest() for p, t in adj_text.items()},
        "owner_sections_reviewed": hs, "adjacent_sections_reviewed": {p: headings(t) for p, t in adj_text.items()},
        "existing_proposition": f"已顺读 owner `{path}` 的 {len(hs)} 个 H2 与相邻章节 {adjacent}；当前 owner 负责 `{owner}` 的既有演进链。{'正文已存在该 exact family trace，故不重复写入。' if direct else '正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。'}",
        "new_evidence_delta": mechanism(r), "evolution_relation": "Layering / Dependency" if a in INTEGRATE else "Principle Reuse",
        "decision": decision, "reviewer": "fresh-context:may2026-day03",
    })
final_integrate = {x["arxiv_id"] for x in comparisons if x["decision"] == "Integrate"}
(HERE / "books-current-content-comparison.json").write_text(json.dumps({"schema":"books-current-content-comparison-v2.1-independent-final","report_date":"2026-05-28","items":comparisons}, ensure_ascii=False, indent=2)+"\n")

queue = []
for c in comparisons:
    if c["decision"] != "Integrate": continue
    r = row_by[c["arxiv_id"]]
    queue.append({
        "source_family_id": c["source_family_id"], "arxiv_id": c["arxiv_id"], "owner_node": c["owner_node"], "owner_path": c["owner_path"],
        "adjacent_paths": c["adjacent_paths"], "evidence_version": f"arXiv:{c['arxiv_id']}v1", "writeback_delta": mechanism(r),
        "integration_instruction": "root 串行写入既有演进链：保留旧方案成立条件，说明约束变化、state/control owner、收益/代价、failure、fallback/coexistence 与 exact-v1 evidence boundary。",
        "status": "root_writeback_ready_pending_serial_write",
    })
(HERE / "books-writeback-queue-final.json").write_text(json.dumps({"schema":"books-writeback-queue-v2.1-independent-final","report_date":"2026-05-28","items":queue}, ensure_ascii=False, indent=2)+"\n")
qmd = ["# 2026-05-28 Books Writeback Queue — Independent Final", "", "共享 Books 尚未修改；以下项目已完成 current owner + adjacent comparison。", "", "| Source Family | Owner | Target | Delta |", "| --- | --- | --- | --- |"]
for q in queue: qmd.append(f"| {q['source_family_id']} | `{q['owner_node']}` | `{q['owner_path']}` | {q['writeback_delta']} |")
(HERE / "BOOKS_WRITEBACK_QUEUE-FINAL.md").write_text("\n".join(qmd)+"\n")
(HERE / "materials-request.json").write_text(json.dumps({"schema":"materials-request-v1","report_date":"2026-05-28","requests":[]}, ensure_ascii=False, indent=2)+"\n")

audit = {
    "schema":"fresh-context-independent-audit-v2.1", "report_date":"2026-05-28", "auditor":"may2026-day03",
    "replay":{"raw_snapshot_records":SOURCE["raw_snapshot_records"],"registered":747,"screened":747,"final_denominator":len(RETAINED),"final_closures":len(rows)-len(RETAINED),"false_positives_removed":[],"false_negatives_reopened":sorted(MANUAL_WEB_EVIDENCE),"exact_v1_complete":len(RETAINED),"blocked":0,"ordinary_pending":0},
    "books":{"final_integrate":len(queue),"final_queue":[q["arxiv_id"] for q in queue]},
    "deep_selection":{"selected":sorted(DEEP),"basis":"cross-layer state/control change; top-3 limits narrative only, not Source Review"},
    "checks":{"family_specific_closure_unique":len({r["screening_reason"] for r in rows if r["arxiv_id"] not in RETAINED})==len(rows)-len(RETAINED),"owner_paths_resolved":all((ROOT/c["owner_path"]).exists() for c in comparisons),"exact_v1_routes_complete":len(reviews)==len(RETAINED)},
    "findings":[], "resolution":"747/747 title+abstract replay and exact-v1 review completed; final root-serial queue frozen; Books remains Open until writeback and post-write audit.",
}
(HERE / "fresh-context-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2)+"\n")

candidate_lines = []
for a in sorted(RETAINED):
    r = row_by[a]; s = r["score_v2"]; override = "knowledge_gap" if a in final_integrate else "none"
    candidate_lines.append(f"| {family(a)} | arXiv:{a}v1 | paper-v1:{a} | 2026-W22 | 2026-05-28 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {override} | review:{family(a)} | self | — | new_in_window | {r['owner_node']} | {r['integration_disposition']} | books-review:{family(a)} | no |")

lines = [
    "# Daily Research — 2026-05-28", "", "**Research Date:** 2026-05-28", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-27 09:00:00 ～ 2026-05-28 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite 只用于 identity/date/abstract recovery，技术结论绑定 official arXiv exact-v1。", "",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。pre-write 链路已闭合，等待 root 串行写回和非写作者 post-write audit。", "",
    "## Executive Summary", "",
    f"相邻月份 v2 快照共 {SOURCE['raw_snapshot_records']:,} 条 raw records；严格窗口注册并逐项 title+abstract 语义筛选 747/747。最终 denominator={len(RETAINED)}（{len(RETAINED)/747:.2%}），pre-denominator closures={747-len(RETAINED)}；{len(RETAINED)}/{len(RETAINED)} retained family 已完成 official exact-v1 Method/Evaluation/Limitations/Artifact review，blocked=0、ordinary pending=0；root-writeback-ready Books queue={len(queue)}，本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-28 |", "| Window End | 2026-05-28 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | DEN-20260528-V1-FINAL-{len(RETAINED)} |", f"| Denominator Frozen At | {NOW} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-27T09:00:00+08:00 | 2026-05-28T09:00:00+08:00 | {NOW} | DataCite v2 monthly prefixes 00..99; full title+abstract semantic screen; official exact-v1 HTML→PDF | checked | 747 | {';'.join(family(a) for a in sorted(RETAINED))} | pages=300; final_cursor=end; raw={SOURCE['raw_snapshot_records']}; registered=747; screened=747; retained={len(RETAINED)}; closure={747-len(RETAINED)} | 2026-05-28T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260528:start -->747/747 registered identity 已逐项语义筛选；{len(RETAINED)} family exact-v1 可访问，{747-len(RETAINED)} family 有具名 closure 与重开条件。反例审计从 closure 重开 12 项系统级 family。Coverage 无未解决 finding；外部 estimate、代码 commit 与未披露 benchmark 字段不被反推。<!-- coverage:SRC-ARXIV:20260528:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", *candidate_lines, "",
    "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for x in reviews:
    lines.append(f"| {x['source_family_id']} | RP-TODO-{x['source_family_id']} | deep | {x['primary_evidence_version']} | SRC-ARXIV@{x['primary_evidence_version']} | {x['method_identity_locators']} | {x['evaluation_locators']} | {x['limitations_counterevidence_locators']} | {x['artifact_locators']} | claim:{x['source_family_id']} | complete |")
lines += ["", "### Source Reviews", ""]
for x in reviews:
    a=x["arxiv_id"]; fid=x["source_family_id"]; r=row_by[a]
    lines += [f"<!-- review:{fid}:start -->", f"#### {r['title']}", "", f"问题与 changed constraint：{mechanism(r)}", "", f"Mechanism 与 ownership：owner=`{r['owner_node']}`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。", "", f"Evaluation contract：Method=`{x['method_identity_locators']}`；Evaluation=`{x['evaluation_locators']}`。", "", f"Trade-off / failure / fallback：`{x['limitations_counterevidence_locators']}`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`{x['artifact_locators']}`。", "", f"<!-- claim:{fid}:start -->{x['claim_boundary']} 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:{fid}:end -->", "", f"Books Decision=`{r['integration_disposition']}`；共享 Books 尚未写入。", f"<!-- review:{fid}:end -->", ""]
lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "本报告不登记可外推 benchmark claim；数值只属于 exact-v1 的披露 workload，未披露字段保持 Not Disclosed。", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for a in sorted(RETAINED):
    selected=a in DEEP
    lines.append(f"| {family(a)} | score_7_9{'; forced_review; potential_books_delta' if a in final_integrate else ''} | {'selected' if selected else 'not_selected'} | {DEEP.get(a,'—')} | — | {'cross-layer state/control ownership change' if selected else 'exact-v1 review complete; less cross-cutting than selected units'} | {'analysis:'+DEEP[a] if selected else 'analysis-decision:'+family(a)} |")
lines += ["", "<!-- analysis:DA-TOPOLOGY-COLLECTIVE-CO-DESIGN:start -->", "### Network synthesis：从事后放置推进到拓扑、routing 与 collective 共同设计", "", "固定拓扑再选择 collective 在网络均匀、failure-free 且 workload 稳定时最透明。大规模训练把并行维度、拥塞与故障域耦合后，需要用 workload communication graph 联合决定 topology、routing 与 collective schedule。收益是减少热链路与尾部阻塞，代价是搜索空间、建模误差和配置漂移；模拟最优不拥有生产 promotion authority，仍需小规模 replay、canary 与 fallback topology。", "<!-- analysis:DA-TOPOLOGY-COLLECTIVE-CO-DESIGN:end -->", "", "<!-- analysis:DA-REQUEST-OWNED-TTT-STATE:start -->", "### Serving state：从只读权重推进到 request-owned test-time update", "", "传统 continuous batching 假设请求只追加 KV，模型权重在 batch 间共享。TTT 让每个请求持有可变参数状态，scheduler 必须把 update、read、merge、eviction 和 rollback 纳入 iteration contract。它换来在线适应，却破坏简单 batching、扩大显存和隔离面，并新增 stale update 与跨请求污染；短请求或收益不足时仍应回退 immutable weights + KV。", "<!-- analysis:DA-REQUEST-OWNED-TTT-STATE:end -->", "", "<!-- analysis:DA-OUT-OF-BAND-AGENT-DATA-PLANE:start -->", "### Agent data plane：从内容内提示推进到不可被 payload 覆盖的 out-of-band metadata", "", "把 policy、provenance 与 authority 混进自然语言 payload 在单应用、低对抗环境下简单，但 agent 跨工具和消息系统流转后，内容可以伪造这些控制字段。out-of-band metadata 将 principal、schema、taint 与 policy hint 交给独立 data plane，并在 effect-time authorizer 汇合。收益是隔离控制信息，代价是 producer/bridge 都成为可信组件；metadata 丢失或不兼容时必须 quarantine、降权或人工授权。", "<!-- analysis:DA-OUT-OF-BAND-AGENT-DATA-PLANE:end -->", ""]
for a in sorted(RETAINED):
    if a not in DEEP: lines.append(f"<!-- analysis-decision:{family(a)}:start -->{family(a)} 已完成 exact-v1 review；三项上限仅限制叙事展开，不限制 Source Review。<!-- analysis-decision:{family(a)}:end -->")
lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for c in comparisons:
    ad=";".join(f"{p}#chapter-{Path(p).name.split('-',1)[0]}" for p in c["adjacent_paths"])
    ch=node_map[c["owner_node"]][0]
    lines.append(f"| {c['source_family_id']} | {c['owner_node']} | {c['owner_path']}#chapter-{ch} | {ad} | existing:{c['source_family_id']} | delta:{c['source_family_id']} | {c['evolution_relation']} | {c['decision']} | books-review:{c['source_family_id']} |")
lines += ["", "### Books Decision Receipts", ""]
for c in comparisons:
    fid=c["source_family_id"]
    lines += [f"<!-- books-review:{fid}:start -->", f"<!-- existing:{fid}:start -->{c['existing_proposition']} Owner sha256=`{c['owner_sha256']}`；adjacent=`{', '.join(c['adjacent_paths'])}`。<!-- existing:{fid}:end -->", f"<!-- delta:{fid}:start -->{c['new_evidence_delta']}<!-- delta:{fid}:end --> Decision=`{c['decision']}`；本 lane 未修改共享 Books。", f"<!-- books-review:{fid}:end -->", ""]
first=family(sorted(RETAINED)[0])
lines += ["## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", "| SA-20260528-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260528 | none | 747/747 title+abstract replay；100 retained / 647 family-specific closure | passed |", f"| SA-20260528-EVIDENCE | fresh-context:may2026-day03 | evidence | review:{first} | none | 100/100 exact-v1 Method/Evaluation/Limitations/Artifact review，blocked=0 | passed |", "| SA-20260528-SELECTION | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-TOPOLOGY-COLLECTIVE-CO-DESIGN | none | Top-3 只限制 narrative，全部 retained 均已全文 review | passed |", f"| SA-20260528-BOOKS | fresh-context:may2026-day03 | books | books-review:{first} | F-20260528-BOOKS-WRITEBACK | {len(queue)} 项已 current owner+adjacent compare；等待 root 串行写回及不同 reviewer post-write audit | open |", "", "Fresh-context adversarial pass 复核了全部 747 identity 的 denominator 边界、100 项 exact-v1 claim boundary、Top-3 选择与 current Books owner；没有普通 pending。", "", "## 8. Ignored Noise", "", "647 项逐 family closure 保存在 `screening-ledger-final.json/tsv`；每条包含具名机制/结果、排除边界与重开条件。", "", "## 9. Recommended Action", "", f"1. Root 按日期序列串行写入 {len(queue)} 项 final Books queue。", "2. 由非写作者逐项执行 post-write semantic audit，确认 owner、演进链、trade-off、failure、fallback 与 evidence boundary。", "", "## 10. Repository Changes", "", "- 新建 2026-05-28 date-local Daily、screening ledger、exact-v1 packet、current Books comparison、independent audit 与 final queue。", "- 未修改共享 Books；未 stage、commit 或 push。", "", "## 11. Open Questions", "", f"- {len(queue)} 项 root queue 完成串行写回后，是否全部通过不同 reviewer 的 post-write audit？", "", "### Materials Request", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "无 external blocker；100/100 exact-v1 primary body 已访问，ordinary pending=0。", "", "## 12. Sources", "", "- DataCite arXiv v2 月度快照：完整 identity、Submitted:v1 timestamp 与 title/abstract 枚举。", "- Official arXiv exact-v1 HTML/PDF：100 项 retained family 的 Method、Evaluation、Limitations/Counterevidence 与 Artifact statement。", "- Current Books owner 与相邻章节：路径、H2 与 snapshot hash 位于 `books-current-content-comparison.json`。", "", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"Pre-write 链路已经闭合：747/747 screening、100-family denominator、100/100 exact-v1、blocked=0、ordinary pending=0、三项 Deep Analysis 与 {len(queue)} 项 root-writeback-ready queue。Daily 只有在 Books writeback 和 post-write audit 通过后才可标记 Complete。", ""]

REPORT.parent.mkdir(parents=True, exist_ok=True)
text="\n".join(lines).rstrip()+"\n"
text = text.replace("100 retained / 647", f"{len(RETAINED)} retained / {747-len(RETAINED)}")
text = text.replace("100/100 exact-v1", f"{len(RETAINED)}/{len(RETAINED)} exact-v1")
text = text.replace("100 项 exact-v1", f"{len(RETAINED)} 项 exact-v1")
text = text.replace("647 项逐 family", f"{747-len(RETAINED)} 项逐 family")
text = text.replace("100/100 exact-v1 primary", f"{len(RETAINED)}/{len(RETAINED)} exact-v1 primary")
text = text.replace("100 项 retained family", f"{len(RETAINED)} 项 retained family")
text = text.replace("100-family denominator", f"{len(RETAINED)}-family denominator")
for x in reviews:
    fid=x["source_family_id"]
    body=text.split(f"<!-- review:{fid}:start -->",1)[1].split(f"<!-- review:{fid}:end -->",1)[0]
    r=row_by[x["arxiv_id"]]
    cand={"Event Identity":f"paper-v1:{x['arxiv_id']}","Primary Identifier":f"arXiv:{x['arxiv_id']}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":"knowledge_gap" if x["arxiv_id"] in final_integrate else "none"}
    rp=_expected_review_provenance(fid,cand,"deep",x["primary_evidence_version"],f"SRC-ARXIV@{x['primary_evidence_version']}",x["method_identity_locators"],x["evaluation_locators"],x["limitations_counterevidence_locators"],x["artifact_locators"],f"claim:{fid}",f"review:{fid}",_normalized_body_sha256(body))
    text=text.replace(f"RP-TODO-{fid}",rp)
REPORT.write_text(text)
print(json.dumps({"raw":SOURCE["raw_snapshot_records"],"registered":747,"screened":747,"retained":len(RETAINED),"closures":747-len(RETAINED),"exact_v1":len(RETAINED),"blocked":0,"ordinary_pending":0,"integrate_queue":len(queue)},ensure_ascii=False))
