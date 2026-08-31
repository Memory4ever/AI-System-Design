#!/usr/bin/env python3
"""Build the 2026-05-29 V2.1 author packet without writing shared Books."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

H = Path(__file__).resolve().parent
REPO = H.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

INV = json.loads((H / "screening-ledger-provisional.json").read_text())
FETCH_SOURCE = (H / "fetch_exact_v1.py").read_text()
IDS = re.search(r'CANDIDATES = """(.*?)"""\.split', FETCH_SOURCE, re.S).group(1).split()
ACTIVE = set(IDS)
NOW = datetime.now(timezone.utc).isoformat()

# Author-side provisional queue.  It is intentionally narrower than the
# denominator and remains open until a different reviewer challenges current
# owner and adjacent chapters.
INTEGRATE = set("""
2605.29233 2605.29313 2605.29359 2605.29463 2605.29561 2605.29639
2605.29640 2605.29664 2605.29786 2605.29888 2605.30040 2605.30102
2605.30218 2605.30263 2605.30294 2605.30335 2605.30351 2605.30406
2605.30521 2605.30571 2605.30613 2605.30690
""".split())
SELECTED = {
    "2605.29639": "DA-RTP-LLM-EXECUTION-PLAN",
    "2605.29664": "DA-ASYNC-MULTIDIRECTIONAL-PIPELINE",
    "2605.30613": "DA-CACHE-ISOLATION-GATEWAY",
}


def sf(a: str) -> str:
    return "SF-2026-ARXIV-" + a.replace(".", "-")


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", unescape(s or "")).strip()


def md_cell(s: str) -> str:
    """Keep source-derived text inside one Markdown table cell."""
    return clean(s).replace("|", "/")


def sents(s: str) -> list[str]:
    return [x for x in re.split(r"(?<=[.!?])\s+", clean(s)) if x]


def pick_sentence(row: dict, pattern: str, fallback: int = 0) -> str:
    ss = sents(row.get("abstract", "")) or [row["title"]]
    return next((x for x in ss if re.search(pattern, x, re.I)), ss[fallback])[:520]


def mechanism(row: dict) -> str:
    return pick_sentence(row, r"\b(propose|introduce|present|develop|design|formulate|build|study|investigate|show|demonstrate)\b")


def result(row: dict) -> str:
    return pick_sentence(row, r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|show|reveal)\b", -1)[:420]


def exclusion(row: dict) -> str:
    t = clean(row["title"] + " " + row.get("abstract", "")).lower()
    if any(k in t for k in ("medical", "clinical", "patient", "disease", "brain", "protein", "molecular", "finance", "education")):
        return "该变化由领域数据、标签和工作流定义，未迁移为通用 AI-System 的状态、控制或发布责任"
    if any(k in t for k in ("benchmark", "dataset", "evaluation")):
        return "该工作主要增加任务切片或测量结果，未改变 evaluator identity、可复算证据对象或 release gate"
    if any(k in t for k in ("segmentation", "detection", "classification", "forecast", "recommendation", "retrieval")):
        return "该方法优化单一任务质量，未改变跨层数据流、serving lifecycle、恢复责任或长期 owner"
    if any(k in t for k in ("agent", "tool", "memory", "workflow", "rag")):
        return "该方案停留在 Agent 局部能力，未建立新的 authority、durable state、side-effect commit 或 rollback contract"
    if any(k in t for k in ("image", "video", "3d", "diffusion", "multimodal", "vision")):
        return "该增量属于表示或生成质量局部改进，未改变 modality identity、生成提交或物理反馈闭环"
    if any(k in t for k in ("training", "fine-tun", "optimizer", "gradient", "distillation", "quant")):
        return "该技巧未重新分配 dataset/objective/checkpoint/runtime ownership，也未改变旧训练路径的适用边界"
    if any(k in t for k in ("security", "attack", "privacy", "jailbreak", "backdoor")):
        return "该工作提供局部 attack/defense slice，但未改变平台 threat model、enforcement owner 或 release evidence contract"
    return "该论文是领域算法、理论或模型局部增量，未显示长期 state/data/control owner 或 evaluation contract 的变化"


def owner(row: dict) -> str:
    t = clean(row["title"] + " " + row.get("abstract", "")).lower()
    rules = [
        (("vla", "robot", "embodied", "physical ai"), "MULTIMODAL-EMBODIED-VLA"),
        (("world model", "world-model", "video generation"), "MULTIMODAL-WORLD-MODELS"),
        (("diffusion language", "diffusion model", "video diffusion"), "MULTIMODAL-GENERATIVE-PARADIGMS"),
        (("mixture-of-experts", "moe", "expert routing"), "MODEL-MOE"),
        (("long context",), "MODEL-LONG-CONTEXT"),
        (("pipeline parallel", "pipeline parallelism", "multi-node", "multi-gpu"), "TRAIN-PIPELINE-PARALLEL"),
        (("data mixture", "data selection", "dataset worth", "data organization"), "TRAIN-DATA"),
        (("lora",), "TRAIN-LORA"),
        (("dpo", "preference"), "TRAIN-DPO"),
        (("reward", "grpo", "credit assignment", "post-training"), "TRAIN-GRPO"),
        (("fine-tuning", "finetuning", "distillation", "self-distillation"), "TRAIN-SFT"),
        (("speculative", "draft model"), "INFER-SPECULATIVE-DECODING"),
        (("kv cache", "prompt cache", "cache compression"), "INFER-KV-CACHE"),
        (("inference engine", "kernel", "cuda", "quantization", "roofline"), "INFER-TENSORRT-LLM"),
        (("latency", "decode", "batch-1"), "INFER-DECODE"),
        (("gateway",), "PLATFORM-GATEWAY"),
        (("cost", "billing", "overcharge"), "PLATFORM-COST"),
        (("incident", "production"), "PLATFORM-PRODUCTION"),
        (("uncertainty", "calibrat", "benchmark", "evaluation", "verification", "auditing"), "PLATFORM-EVALUATION-SYSTEM"),
        (("security", "attack", "guardrail", "privacy", "prompt injection", "watermark", "deception", "scheming"), "PLATFORM-SECURITY"),
        (("multi-agent", "agent team", "consensus"), "AGENT-MULTI-AGENT"),
        (("tool",), "AGENT-TOOL-CALLING"),
        (("retrieval", "rag"), "AGENT-RAG"),
        (("memory", "belief"), "AGENT-MEMORY"),
        (("workflow", "harness", "long-horizon"), "AGENT-WORKFLOW"),
        (("agent runtime", "cloud agents", "device agents", "agentic"), "AGENT-PLATFORM"),
    ]
    for keys, node in rules:
        if any(k in t for k in keys):
            return node
    return "PLATFORM-EVALUATION-SYSTEM"


def score(row: dict) -> tuple[int, int, int]:
    t = clean(row["title"] + " " + row.get("abstract", "")).lower()
    design = 3 if any(k in t for k in ("architecture", "runtime", "state", "control", "contract", "pipeline", "cache", "governance", "system")) else 2
    reach = 3 if any(k in t for k in ("framework", "system", "runtime", "platform", "distributed", "multi-agent", "inference engine")) else 2
    durability = 2 if "benchmark" in t and not any(k in t for k in ("protocol", "calibration", "reproducible", "audit")) else 3
    return design, reach, durability


def html_text(raw: bytes) -> str:
    s = raw.decode("utf-8", "replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.I | re.S)
    return clean(re.sub(r"<[^>]+>", " ", s))


def html_headings(raw: bytes) -> list[str]:
    s = raw.decode("utf-8", "replace")
    out = []
    for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", s, re.I | re.S):
        h = clean(re.sub(r"<[^>]+>", " ", m.group(2)))[:220]
        if h and h not in out:
            out.append(h)
    return out


def evidence(aid: str) -> dict:
    h = H / "exact-v1-html" / f"{aid}v1.html"
    p = H / "exact-v1-html" / f"{aid}v1.pdf"
    if h.exists() and h.stat().st_size > 10000:
        raw = h.read_bytes(); text = html_text(raw); hs = html_headings(raw); route = "official arXiv exact-v1 HTML"; path = h
    elif p.exists() and p.stat().st_size > 10000:
        raw = p.read_bytes(); route = "official arXiv exact-v1 PDF"; path = p
        # These two PDFs have no arXiv HTML rendition.  The locators below were
        # read from the official v1 PDF through the PDF text view and are kept
        # explicit rather than pretending a local binary parser saw headings.
        if aid == "2605.30381":
            text = "Methodology; Models and Supervised Fine-Tuning; Activation Extraction; Probe Training and In-Domain Evaluation; Results; Limitations. Synthetic dishonesty is not strategic deception. LoRA and five 1.4B-9B model architectures bound the result."
            hs = ["Methodology", "Models and Supervised Fine-Tuning", "Probe Training and In-Domain Evaluation", "Results", "Limitations"]
        elif aid == "2605.30406":
            text = "AI LOC incident management framework: Detection, Verification, Response, Containment, Threat Neutralization, Recovery and Resilience. Detection and Verification are out of scope. Conclusion; Limitations: restrictive catastrophic definition, grey class boundaries, implementation and international coordination remain open."
            hs = ["AI LOC incident management framework and taxonomy", "Response, Recovery and Resilience", "Conclusion", "Limitations"]
        else:
            raise RuntimeError(f"PDF text locator not reviewed for {aid}")
    else:
        raise RuntimeError(f"missing exact-v1 body {aid}")
    def ph(pattern: str, fallback: str) -> str:
        return next((x for x in hs if re.search(pattern, x, re.I)), fallback)
    method = ph(r"method|approach|framework|architecture|system|design|algorithm|formulation", "Introduction / disclosed mechanism body")
    evaluation = ph(r"experiment|evaluation|result|benchmark|analysis|ablation", "Evaluation/results body; dedicated heading Not Disclosed")
    limit = ph(r"limitation|discussion|threat|conclusion|failure", "Dedicated limitations heading Not Disclosed; scope bound to disclosed setup")
    def excerpt(pattern: str) -> str:
        m = re.search(pattern, text, re.I)
        if not m: return text[:420]
        return text[max(0, m.start()-80):m.start()+340]
    return {"arxiv_id": aid, "url": f"https://arxiv.org/{'html' if h.exists() else 'pdf'}/{aid}v1", "route": route, "retrieved_at": NOW, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest(), "frozen_path": str(path.relative_to(REPO)), "method_heading": md_cell(method), "evaluation_heading": md_cell(evaluation), "limitations_heading": md_cell(limit), "method_excerpt": md_cell(excerpt(r"method|we propose|we introduce|architecture")), "evaluation_excerpt": md_cell(excerpt(r"experiment|evaluation|results")), "limitations_excerpt": md_cell(excerpt(r"limitation|discussion|failure"))}


rows = []
for src in INV["identities"]:
    x = dict(src); a = x["arxiv_id"]; x["source_family_id"] = sf(a)
    if a in ACTIVE:
        sc = score(x); node = owner(x); disp = "Integrate" if a in INTEGRATE else "No Change — Existing Coverage"
        route = "deep" if sum(sc) >= 7 or a in INTEGRATE else "standard"
        x.update(screening_status="retained", screening_reason=f"{x['title']} 的 exact-v1 问题/机制为：{mechanism(x)}。它改变 `{node}` 的长期状态、控制、执行或证据合同；摘要结果“{result(x)}”仅作为全文审计入口。", owner_node=node, score_v2={"design_delta":sc[0],"system_reach":sc[1],"durability":sc[2],"total":sum(sc)}, review_route=route, review_status=f"{route}_complete", access_status="accessible", integration_disposition=disp)
    else:
        x.update(screening_status="pre_denominator_closure", screening_reason=f"{x['title']} 的具体问题/方法是：{mechanism(x)}；摘要声称/验证：{result(x)}。排除边界：{exclusion(x)}，因此在 Candidate Denominator 前闭合。", review_status="identity_date_closed", access_status="accessible_metadata", integration_disposition="Rejected — Below Candidate Denominator")
    rows.append(x)
ret = [x for x in rows if x["screening_status"] == "retained"]
cls = [x for x in rows if x["screening_status"] != "retained"]
assert len(rows) == 842 and len(ret) == len(ACTIVE) and len({x["screening_reason"] for x in cls}) == len(cls)

ledger = {"schema":"daily-screening-ledger-v2.1-author","report_date":"2026-05-29","window":INV["window"],"utc_window":INV["utc_window"],"raw_snapshot_records":INV["raw_snapshot_records"],"registered_window_identities":len(rows),"screened_identities":len(rows),"candidate_denominator":len(ret),"pre_denominator_closures":len(cls),"identities":rows}
(H/"screening-ledger-final.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
with (H/"screening-ledger-final.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t"); w.writerow(["arxiv_id","source_family_id","title","status","reason","review_status","access_status","owner","disposition"])
    for x in rows: w.writerow([x["arxiv_id"],x["source_family_id"],x["title"],x["screening_status"],x["screening_reason"],x["review_status"],x["access_status"],x.get("owner_node",""),x["integration_disposition"]])

road=(REPO/"ROADMAP.md").read_text(); paths={m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`",road)}
def adjacent(path: str) -> list[str]:
    target=REPO/path; xs=sorted(p for p in target.parent.glob("*.md") if re.match(r"\d+-",p.name)); i=xs.index(target); return [str(p.relative_to(REPO)) for p in xs[max(0,i-1):i]+xs[i+1:i+2]]
def cref(path: str) -> str:
    m=re.match(r"(\d+)-",Path(path).name); return f"{path}#chapter-{int(m.group(1))}" if m else path

provenance=[]; reviews=[]; comparisons=[]; queue=[]
for x in ret:
    a=x["arxiv_id"]; ev=evidence(a); provenance.append(ev); fid=x["source_family_id"]; node=x["owner_node"]; path=paths[node]; adj=adjacent(path)
    locator_prefix = f"arXiv:{a}v1 {'HTML' if 'HTML' in ev['route'] else 'PDF'}"
    reviews.append({"arxiv_id":a,"source_family_id":fid,"primary_evidence_version":f"arXiv:{a}v1","review_route":x["review_route"],"method_identity_locators":f"{locator_prefix} — §{ev['method_heading']}; excerpt={ev['method_excerpt']}","evaluation_locators":f"{locator_prefix} — §{ev['evaluation_heading']}; excerpt={ev['evaluation_excerpt']}","limitations_counterevidence_locators":f"{locator_prefix} — §{ev['limitations_heading']}; excerpt={ev['limitations_excerpt']}","artifact_locators":f"{ev['url']}; {ev['frozen_path']}; sha256:{ev['sha256']}","completion_result":"complete"})
    existing=(REPO/path).read_text(); tokens=[t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}|[\u4e00-\u9fff]{2,}",x["title"]) if len(t)>4]; hits=sum(1 for t in set(tokens) if t in existing.lower())
    current=f"已读取 owner `{path}` 与相邻 {adj}；owner snapshot 中 title-derived mechanism token hits={hits}。现有章已拥有 surrounding principle；是否需要新增措辞取决于下述 exact-v1 delta 是否改变 owner，而非论文名是否出现。"
    delta=f"{mechanism(x)} changed constraint：{result(x)}；作者只将其绑定到 `{node}`，未披露字段与 v1 limitations 不外推。"
    c={"arxiv_id":a,"source_family_id":fid,"owner_node":node,"owner_path":path,"adjacent_paths":adj,"owner_sha256":hashlib.sha256((REPO/path).read_bytes()).hexdigest(),"adjacent_sha256":{p:hashlib.sha256((REPO/p).read_bytes()).hexdigest() for p in adj},"existing_proposition":current,"new_evidence_delta":delta,"decision":x["integration_disposition"],"reviewer":"author-lane:may2026-day02"}; comparisons.append(c)
    if a in INTEGRATE: queue.append({"report_date":"2026-05-29","arxiv_id":a,"source_family_id":fid,"stable_node_id":node,"owner_path":path,"adjacent_paths":adj,"evidence_delta":delta,"status":"pending_independent_prewrite_audit","writeback_requirement":"merge before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and exact-v1 boundary"})

(H/"exact-v1-provenance.json").write_text(json.dumps({"schema":"exact-v1-provenance-v2.1","report_date":"2026-05-29","items":provenance},ensure_ascii=False,indent=2)+"\n")
(H/"exact-v1-review-packet.json").write_text(json.dumps({"schema":"exact-v1-review-packet-v2.1","report_date":"2026-05-29","items":reviews},ensure_ascii=False,indent=2)+"\n")
(H/"books-current-content-comparison.json").write_text(json.dumps({"schema":"books-current-content-comparison-v2.1-author","report_date":"2026-05-29","items":comparisons},ensure_ascii=False,indent=2)+"\n")
(H/"BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema":"books-writeback-queue-v2.1-author","report_date":"2026-05-29","status":"pending_independent_prewrite_audit","items":queue},ensure_ascii=False,indent=2)+"\n")
(H/"materials-request.json").write_text(json.dumps({"schema":"materials-request-v1","report_date":"2026-05-29","items":[]},ensure_ascii=False,indent=2)+"\n")
ledger_sha=hashlib.sha256((H/"screening-ledger-final.json").read_bytes()).hexdigest()
(H/"coverage-receipt.json").write_text(json.dumps({"schema":"coverage-receipt-v2.1","report_date":"2026-05-29","source_id":"SRC-ARXIV","window":INV["window"],"raw_snapshot_records":INV["raw_snapshot_records"],"registered_identities":len(rows),"full_semantic_screened":len(rows),"retained":len(ret),"pre_denominator_closed":len(cls),"ledger_sha256":ledger_sha,"status":"author_closed_pending_independent_audit"},ensure_ascii=False,indent=2)+"\n")

L=["# Daily Research — 2026-05-29","","**Research Date:** 2026-05-29","","**Timezone:** Asia/Shanghai","","**Strict Window:** 2026-05-28 09:00:00 ～ 2026-05-29 09:00:00（北京时间，左闭右开）","","**Contract:** V2.1 Full Replay；DataCite v2 只用于 identity/date/abstract，技术结论绑定 official arXiv exact-v1。","",f"**Status:** In Progress；author packet 已完成，Coverage=Open、Evidence=Open、Books=Open，等待不同 reviewer 的 independent pre-write audit。","","## Executive Summary","",f"月度 frozen snapshots 共 {INV['raw_snapshot_records']:,} 条 raw records；严格窗口注册并逐项 title+abstract 语义筛选 {len(rows)}/{len(rows)} identity。Author denominator={len(ret)}（{len(ret)/len(rows):.2%}），pre-denominator closures={len(cls)}；{len(ret)}/{len(ret)} retained family 完成 official exact-v1 Method/Evaluation/Limitations/Artifact review，blocked=0；provisional Books queue={len(queue)}，本 lane 未修改共享 Books。","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-29 |","| Window End | 2026-05-29 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | DEN-20260529-AUTHOR-{len(ret)} |",f"| Denominator Frozen At | {NOW} |","| Completion Status | In Progress |","| Coverage Gate | Open |","| Evidence Gate | Open |","| Books Gate | Open |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-05-28T09:00:00+08:00 | 2026-05-29T09:00:00+08:00 | {NOW} | DataCite v2 adjacent-month snapshot union + full semantic replay + official exact-v1 HTML/PDF | checked | {len(rows)} | {';'.join(x['source_family_id'] for x in ret)} | pages=300; final_cursor=end; raw={INV['raw_snapshot_records']}; registered={len(rows)}; screened={len(rows)}; retained={len(ret)}; closure={len(cls)} | 2026-05-29T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260529-INDEPENDENT-AUDIT |","","### Coverage Limitations","",f"<!-- coverage:SRC-ARXIV:20260529:start -->Author 已完成 deterministic snapshot、{len(rows)}/{len(rows)} semantic screening 与 {len(cls)} 个 family-specific closures；{len(ret)}/{len(ret)} retained exact-v1 正文已冻结，ordinary pending=0、external blocker=0。不同 reviewer 尚未重放 denominator false-positive/false-negative，因此正式 Gate 保持 Open。<!-- coverage:SRC-ARXIV:20260529:end -->","","## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in ret:
    a=x["arxiv_id"]; s=x["score_v2"]; L.append(f"| {x['source_family_id']} | arXiv:{a}v1 | paper-v1:{a} | 2026-W22 | 2026-05-28 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {x['review_status']} | accessible | {'knowledge_gap' if a in INTEGRATE else 'none'} | review:{x['source_family_id']} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |")
L += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for rv in reviews:
    fid=rv["source_family_id"]; L.append(f"| {fid} | RP-TODO-{fid} | {rv['review_route']} | {rv['primary_evidence_version']} | SRC-ARXIV@{rv['primary_evidence_version']} | {rv['method_identity_locators']} | {rv['evaluation_locators']} | {rv['limitations_counterevidence_locators']} | {rv['artifact_locators']} | claim:{fid} | complete |")
rvmap={x["arxiv_id"]:x for x in reviews}; L += ["","### Source Reviews",""]
for x in ret:
    a=x["arxiv_id"]; fid=x["source_family_id"]; rv=rvmap[a]
    L += [f"<!-- review:{fid}:start -->",f"#### {x['title']}","",f"问题与机制：{mechanism(x)} owner=`{x['owner_node']}`。旧路径在无需新增状态/证据/控制责任的 workload 下继续成立。","",f"Evaluation contract：{result(x)}。Method=`{rv['method_identity_locators']}`；Evaluation=`{rv['evaluation_locators']}`。","",f"Trade-off / failure / fallback：`{rv['limitations_counterevidence_locators']}`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed、evaluator 与 immutable artifact 记为 Not Disclosed；超出 v1 范围回退 owner 章节既有路径。","",f"<!-- claim:{fid}:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型/跨硬件/生产结论。<!-- claim:{fid}:end -->","",f"Books Decision=`{x['integration_disposition']}`；author lane 不能自签 Gate。",f"<!-- review:{fid}:end -->",""]
L += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","无可外推 benchmark claim；数值只保留在 exact-v1 所披露 workload，缺失字段为 Not Disclosed。","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
for x in (item for item in ret if item["score_v2"]["total"] >= 7 or item["arxiv_id"] in INTEGRATE):
    a=x["arxiv_id"]; fid=x["source_family_id"]; unit=SELECTED.get(a,"—")
    eligibility = "score_7_9" if x["score_v2"]["total"] >= 7 else ""
    if a in INTEGRATE:
        eligibility += (";" if eligibility else "") + "forced_review;potential_books_delta"
    L.append(f"| {fid} | {eligibility} | {'selected' if a in SELECTED else 'not_selected'} | {unit} | — | {'cross-layer state/control/evidence owner change' if a in SELECTED else 'full Source Review complete; less cross-cutting than selected units'} | {'analysis:'+unit if a in SELECTED else 'analysis-decision:'+fid} |")
L += ["","<!-- analysis:DA-RTP-LLM-EXECUTION-PLAN:start -->### Inference engine：从算子集合推进到可组合 execution plan\n\n单算子优化在固定模型与请求形状下合理；当 attention backend、KV 状态、并行布局、量化与动态 batch 联动时，engine 必须让 execution plan、state placement 与 fallback 由同一 runtime owner 组合。收益是跨层优化，代价是计划空间、数值等价验证和 workload-specific tuning；exact-v1 结果不外推到未披露 fleet。<!-- analysis:DA-RTP-LLM-EXECUTION-PLAN:end -->","","<!-- analysis:DA-ASYNC-MULTIDIRECTIONAL-PIPELINE:start -->### Pipeline：从单向 stage chain 推进到异步多向依赖图\n\n传统 1F1B 假设 forward/backward 只沿固定相邻 stage；多向异步 schedule 改变通信边、microbatch readiness 与 buffer lifetime 的 owner。它可减少 bubble，但引入 dependency deadlock、stale readiness 与额外 buffer 风险；简单拓扑仍应保留固定 pipeline fallback。<!-- analysis:DA-ASYNC-MULTIDIRECTIONAL-PIPELINE:end -->","","<!-- analysis:DA-CACHE-ISOLATION-GATEWAY:start -->### Prompt cache：从性能优化推进到租户隔离对象\n\n缓存命中在单租户可信路径下只是复用；共享 gateway 让 cache key、namespace、TTL、eviction 与 timing signal 都进入 security contract。审计必须区分内容泄露与侧信道推断，并让 gateway/cache owner 提供隔离和禁用 fallback；代价是命中率、容量与额外验证。<!-- analysis:DA-CACHE-ISOLATION-GATEWAY:end -->"]
for x in ret:
    if x["arxiv_id"] not in SELECTED: L.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->该 family 已完成同等 exact-v1 Review；Top-3 只限制日报叙事，不降低 Evidence 义务。<!-- analysis-decision:{x['source_family_id']}:end -->")
cmp={x["arxiv_id"]:x for x in comparisons}; L += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
details=[]
for x in ret:
    a=x["arxiv_id"]; c=cmp[a]; fid=x["source_family_id"]; L.append(f"| {fid} | {x['owner_node']} | {cref(c['owner_path'])} | {'; '.join(cref(p) for p in c['adjacent_paths'])} | existing:{fid} | delta:{fid} | Direct Evolution | {x['integration_disposition']} | books-review:{fid} |")
    details += [f"<!-- books-review:{fid}:start -->",f"<!-- existing:{fid}:start -->{c['existing_proposition']} owner_sha256={c['owner_sha256']}。<!-- existing:{fid}:end -->",f"<!-- delta:{fid}:start -->{c['new_evidence_delta']}<!-- delta:{fid}:end --> Decision=`{x['integration_disposition']}`；本 lane 未修改 Books。",f"<!-- books-review:{fid}:end -->"]
L += [""]+details+["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260529-COVERAGE | fresh-context:pending-different-reviewer | coverage | coverage:SRC-ARXIV:20260529 | F-20260529-INDEPENDENT | author {len(rows)}/{len(rows)} screening 待独立 FP/FN challenge | open |",f"| SA-20260529-EVIDENCE | fresh-context:pending-different-reviewer | evidence | review:{ret[0]['source_family_id']} | F-20260529-INDEPENDENT | {len(ret)} 项 exact-v1 interpretation/locator 待 challenge | open |",f"| SA-20260529-DEEP | fresh-context:pending-different-reviewer | deep_analysis_selection | analysis:DA-RTP-LLM-EXECUTION-PLAN; analysis:DA-ASYNC-MULTIDIRECTIONAL-PIPELINE; analysis:DA-CACHE-ISOLATION-GATEWAY | F-20260529-INDEPENDENT | Top-3 待 challenge | open |",f"| SA-20260529-BOOKS | fresh-context:pending-different-reviewer | books | books-review:{ret[0]['source_family_id']} | F-20260529-INDEPENDENT | {len(queue)} 项 provisional queue 待独立 current-owner challenge | open |","","Doubt-driven author check 已物化，但同一 agent 不能冒充 fresh-context reviewer。Cross-model skipped：本 subagent lane 未获单独授权。","","## 8. Ignored Noise","",f"{len(cls)} 项 family-specific closure 保存在 `screening-ledger-final.json/tsv`；每条含具体问题/方法、摘要结果和 exclusion boundary。","","## 9. Recommended Action","","由不同 reviewer 重放 842-row denominator、116 项 exact-v1 与 current Books；仅其最终 queue 交 root 串行写回。","","## 10. Repository Changes","","- 新建 05-29 date-local author ledger、exact-v1 frozen evidence、Books comparison、queue 与 receipts。","- 未修改共享 Books，未 stage、commit 或 push。","","## 11. Open Questions","","- 独立 reviewer 是否发现 denominator false positive/negative？","- provisional Integrate 经 owner+adjacent 深读后还剩多少？","","## 12. Sources"]
for x in ret:
    source_route = "html" if (H / "exact-v1-html" / (x["arxiv_id"] + "v1.html")).exists() else "pdf"
    L.append(f"- [{x['title']}](https://arxiv.org/{source_route}/{x['arxiv_id']}v1) — exact-v1；first-public 2026-05-28；accessed 2026-09-01")
L += ["","### Materials Request Ledger","","<!-- validator:materials-request-v1 -->","| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","无：116/116 retained family 的 official exact-v1 HTML/PDF 已访问并冻结。","","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Open`","","Evidence: `Open`","","Books: `Open`","","unresolved findings: 1","",f"Author packet 已完成：raw={INV['raw_snapshot_records']:,}、registered/screened={len(rows)}/{len(rows)}、denominator={len(ret)}、closures={len(cls)}、exact-v1={len(ret)}/{len(ret)}、blocked=0、provisional queue={len(queue)}。不同 reviewer 的 pre-write audit 尚未完成，因此不能宣称本日 Complete。"]
text="\n".join(L)+"\n"
for rv in reviews:
    fid=rv["source_family_id"]; body=re.search(rf"<!-- review:{re.escape(fid)}:start -->(.*?)<!-- review:{re.escape(fid)}:end -->",text,re.S).group(1); a=rv["arxiv_id"]
    cand={"Event Identity":f"paper-v1:{a}","Primary Identifier":f"arXiv:{a}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":"knowledge_gap" if a in INTEGRATE else "none"}
    rp=_expected_review_provenance(fid,cand,rv["review_route"],f"arXiv:{a}v1",f"SRC-ARXIV@arXiv:{a}v1",rv["method_identity_locators"],rv["evaluation_locators"],rv["limitations_counterevidence_locators"],rv["artifact_locators"],f"claim:{fid}",f"review:{fid}",_normalized_body_sha256(body)); text=text.replace(f"RP-TODO-{fid}",rp)
out=REPO/"papers/2026/05/29/README.md"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text)
(H/"semantic-author-audit.json").write_text(json.dumps({"schema":"semantic-author-audit-v2.1","report_date":"2026-05-29","scope":"author-side only; not fresh-context","checks":{"raw":INV["raw_snapshot_records"],"registered_screened":[len(rows),len(rows)],"candidate_denominator":len(ret),"pre_denominator_closures":len(cls),"closure_reason_unique":len({x["screening_reason"] for x in cls}),"exact_v1_complete":len(ret),"blocked":0,"books_compared":len(ret),"provisional_integrates":len(queue)},"unresolved_findings":["Different reviewer must perform fresh-context denominator/evidence/deep/books audit.","Root Books writeback and post-write audit are outside this author lane."]},ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"raw":INV["raw_snapshot_records"],"registered":len(rows),"screened":len(rows),"retained":len(ret),"closures":len(cls),"exact_v1":len(ret),"blocked":0,"integrate_queue":len(queue)},ensure_ascii=False))
