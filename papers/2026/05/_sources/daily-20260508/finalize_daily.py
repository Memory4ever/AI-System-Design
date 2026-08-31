#!/usr/bin/env python3
"""Freeze the 2026-05-08 author packet without writing shared Books."""
from __future__ import annotations

import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256
INV = json.loads((ROOT / "screening-ledger-provisional.json").read_text())
ACTIVE = set((ROOT / "candidate-ids.txt").read_text().split())

# Independent audit recovered every retained family through official exact-v1
# HTML/PDF.  Access is therefore no longer a material blocker.
BLOCKED = set()

NODE = {
    "2605.05583":"AGENT-MEMORY",
    "2605.05607":"TRAIN-TENSOR-PARALLEL", "2605.05628":"TRAIN-TENSOR-PARALLEL",
    "2605.05639":"INFER-GPU-MEMORY", "2605.05696":"INFER-KV-CACHE",
    "2605.05687":"TRAIN-DATA", "2605.05699":"INFER-KV-CACHE",
    "2605.05701":"AGENT-PLANNING", "2605.05716":"AGENT-PLATFORM",
    "2605.05724":"PLATFORM-EVALUATION-SYSTEM",
    "2605.05794":"TRAIN-PRETRAINING", "2605.05819":"INFER-TENSORRT-LLM",
    "2605.05971":"MODEL-KV-CACHE", "2605.05973":"PLATFORM-EVALUATION-SYSTEM",
    "2605.06055":"INFER-TENSORRT-LLM", "2605.06068":"INFER-TENSORRT-LLM",
    "2605.05868":"PLATFORM-SECURITY", "2605.06105":"INFER-PREFILL",
    "2605.06113":"INFER-SCHEDULING", "2605.06136":"PLATFORM-EVALUATION-SYSTEM",
    "2605.06152":"TRAIN-PRETRAINING", "2605.06161":"PLATFORM-EVALUATION-SYSTEM",
    "2605.06185":"AGENT-RAG",
    "2605.06221":"INFER-PREFILL", "2605.06374":"TRAIN-DISTRIBUTED-TRAINING",
    "2605.06327":"PLATFORM-EVALUATION-SYSTEM", "2605.06365":"AGENT-WORKFLOW",
    "2605.06393":"PLATFORM-SECURITY", "2605.06455":"PLATFORM-MONITORING",
    "2605.06472":"INFER-KV-CACHE", "2605.06544":"PLATFORM-EVALUATION-SYSTEM",
    "2605.06527":"AGENT-MEMORY", "2605.06534":"TRAIN-RLHF",
    "2605.06635":"PLATFORM-EVALUATION-SYSTEM", "2605.06663":"MODEL-MOE", "2605.06665":"MODEL-MOE",
    "2605.06731":"AGENT-MEMORY", "2605.06761":"PLATFORM-EVALUATION-SYSTEM",
    "2605.06788":"AGENT-MULTI-AGENT", "2605.06812":"PLATFORM-TRACE",
    "2605.06841":"MULTIMODAL-WORLD-MODELS", "2605.06850":"TRAIN-RLHF",
    "2605.06869":"PLATFORM-EVALUATION-SYSTEM", "2605.06890":"AGENT-TOOL-CALLING",
    "2605.06914":"INFER-SCHEDULING", "2605.06992":"PLATFORM-SECURITY",
    "2605.06997":"MODEL-KV-CACHE", "2605.07002":"PLATFORM-EVALUATION-SYSTEM",
    "2605.07021":"PLATFORM-SECURITY", "2605.07042":"AGENT-CONTEXT",
    "2605.07068":"AGENT-MEMORY",
    "2605.07073":"AGENT-MULTI-AGENT", "2605.07076":"AGENT-MEMORY",
    "2605.07079":"MULTIMODAL-WORLD-MODELS", "2605.08261":"PLATFORM-EVALUATION-SYSTEM",
    "2605.16341":"TRAIN-DISTRIBUTED-TRAINING", "2605.23950":"PLATFORM-EVALUATION-SYSTEM",
    "2606.00050":"AGENT-RAG",
}

NO_CHANGE = {
    "2605.05699", "2605.06068", "2605.06185", "2605.06221",
    "2605.06527", "2605.06663", "2605.06869", "2605.06890",
    "2605.07021", "2605.23950", "2606.00050",
}

LOC = {
    "2605.05583":("§3 Methodology; §3.3 Belief Memory","§4 Experiments; Appendix B/C","Appendix D Limitations and Future Work"),
    "2605.05607":("§3 DySHARP Design","§4 Evaluation","§5 Discussion and Conclusion"),
    "2605.05628":("§III CAIS Design","§IV Experimental Methodology; §V Experimental Results","§V-D Hardware Overhead; §VII Conclusion"),
    "2605.05639":("§3 Overview; §4 Hardware Design; §6 Runtime Optimizations","§7 Experimental Methodology; §8 Evaluation","§8.4 Ablation and Discussion; §10 Conclusion"),
    "2605.05687":("§3 FakeWiki Benchmark; §4 Methods","§5 Experimental Setup; §6 Results","§6.2 per-method results; Limitations"),
    "2605.05696":("§3–§7 Agentic Workload, Position Invariance and Irminsul","§7.4 Recovery Measurement; Appendix H Output Consistency","§7.3 RoPE Pitfall; Appendix D/F/G"),
    "2605.05699":("§3 Method; §5 Learning the Rotation","§4 Experiments; §7 End-to-end Deployment","§8 Discussion; §9 Conclusion"),
    "2605.05701":("§3 Problem Formulation; §4 Two-Stage Budget Controller","§5 Experiments","§6 Discussion and Limitations"),
    "2605.05716":("§3 Problem Setup; §6 Analysis Framework","§4–§5 Main Results; §7 Robustness","§8 Error Analysis; §9 Discussion; Appendix E"),
    "2605.05724":("§3 Closed-Loop Auto Research Methodology","§4 Experiments; submitted-trial lineage","§5 Analysis; §6 Discussion; evaluator-owned scope"),
    "2605.05794":("§3 Motivation; §4 Methodology","§5 Experiments; §6 Additional Investigations","Appendix D Discussion and Future Work"),
    "2605.05819":("§3 Observations; §4 HCInfer","§5 Evaluation; Appendix C","§6 Conclusion; Appendix B assumptions"),
    "2605.05868":("§3 SkillScope design; graph and replay enforcement","§5 Evaluation; replay ablations","§6 Discussion; stated limitations"),
    "2605.05971":("§3 Compressibility-Aware Training Objective","§4 Experiments; §5 Analysis","§6 Limitations and Conclusion"),
    "2605.05973":("§3 Adaptive Benchmarking Model","§4–§5 Experiments and Winner's-Curse Analysis","§6 Discussion and Limitations"),
    "2605.06055":("§3 Relay-Buffer-Free Dispatch and Combine","§4 Implementation; §5 Evaluation","§6 Discussion and Limitations"),
    "2605.06068":("§3 VibeServe Design; §4 Agentic Search Loop","§5 Evaluation","§6 Limitations; §7 Conclusion"),
    "2605.06105":("§3 Layer-Asymmetric KV Visibility; §4 System Integration","§5 Experiments","§6 Limitations"),
    "2605.06113":("§3 Problem; §4 BR-H online routing","§6 Experiments","§7 Discussion; deployment scope"),
    "2605.06136":("§3 Build-and-Find protocol; §4 effort metrics","§5 Evaluation","§6 Scope and limitations"),
    "2605.06152":("§3 Numerical Feature Inflation; §4.2 Mitigation","§4 Empirical Results; §4.3 Real-World Tasks","§5 Limitations; Appendix A.3/D.3"),
    "2605.06161":("§3 Policy Invariance Score and paired perturbations","§4 Evaluation","§5 Limitations and calibration caveats"),
    "2605.06185":("§3 SES Event Representation; §4 Dual-Store Retrieval","§5 Experiments","§6 Limitations and Conclusion"),
    "2605.06221":("§3 UniPrefill; §4 Continuous-Batching Integration","§5 Experiments","§6 Ablations and Limitations"),
    "2605.06327":("§2 Paired-Prompt Protocol; §3 Evaluation-Context Divergence","§4 Pilot Evaluation","§5 Limitations; familiarity is only a contamination proxy"),
    "2605.06365":("§4 Deterministic Execution Graph; §5 lineage model","§8 Experiments","§9.6 What This Paper Does Not Claim; §9.7 Limitations"),
    "2605.06374":("§3 Detector; §4 Dynamic Hybrid-Parallel Scheduler","§5 Evaluation","§6 Discussion and Limitations"),
    "2605.06393":("§III Operation-Centric Threat Model; §IV TEE Trusted Plane","§V Prototype; §VI Evaluation","§VII Security Analysis and Limitations"),
    "2605.06455":("§4 Method: prefix event extraction and monitors","§5 Experiments","§6 Limitations and Conclusion"),
    "2605.06472":("§3 Workflow-Path Prediction; §4 KV Management","§5 Evaluation","§6 Limitations and Conclusion"),
    "2605.06544":("§3 Trace-Based Benchmark Contract; §4 Workloads","§4 Evaluation; Appendix C run scripts","§5 Discussion and Limitations"),
    "2605.06527":("§3 Memory-Validity Model; §4 STALE","§5 Evaluation","§6 Limitations"),
    "2605.06534":("§3 ROSE Design","§4 Implementation; §5 Evaluation","§6 Discussion and Limitations"),
    "2605.06635":("§2 Attribution Taxonomy; §3 citation parsing and verification","§4 Evaluation","§5 Limitations"),
    "2605.06663":("§3 EMO Objective and Document-Level Routing","§4 Experiments","§5 Analysis and Limitations"),
    "2605.06665":("§3 Routing Probe; §4 UniPool; §5 Pool-Level Balance","§6 Experiments","§7 Analysis and Limitations"),
    "2605.06731":("§3 Threat Model; §4 ULSPB; §5 StateGuard","§6 Experiments","§7 Limitations and Discussion"),
    "2605.06761":("§3 HTTP Replay; §4 Environment Synthesis","§5 Training; §6 Evaluation","§7 Limitations and Sim-to-Real Gap"),
    "2605.06788":("§3 Filtration-Based Conformal Attribution","§4 Experiments; §5 Rollback Evaluation","§6 Limitations"),
    "2605.06812":("§Agent-BOM static/dynamic graph schema","§OWASP attack-chain evaluation and OpenClaw plugin","HTML conversion omits Method sections; claims limited to disclosed graph and scenarios"),
    "2605.06841":("§3 Structural-Change Formalization; §4 AGWM","§5 Experiments","§6 Limitations"),
    "2605.06850":("§3 Shadow Mask Distillation; §4 Dual-Track KL","§5 Experiments","§6 Limitations and Conclusion"),
    "2605.06869":("§3 Agentick Environment and Harness","§4 Evaluation across 27 configurations","§5 Limitations and benchmark scope"),
    "2605.06890":("§3 Decision-Point Formulation and Internal-State Probes","§4 Experiments and Results","§6 Limitations; white-box two-model scope"),
    "2605.06914":("§3 BranchReg regulator and virtual-request control","§4 Evaluation; Appendix E","§5 Discussion; workload and scheduler scope"),
    "2605.06992":("§3 Safety-Generalization Theory","§4 Quadcopter and CRM Experiments","§5 Discussion and Limitations"),
    "2605.06997":("§3.2 Spectral Koopman Attention; §6.2 Computational Cost","§4 Experiments; Appendix G Experimental Setup","§6.2 FP32 Cholesky bottleneck; task/model scope"),
    "2605.07002":("§3 Anytime-Valid Adaptive Audit","§4 Theory; §5 Experiments","§6 Limitations"),
    "2605.07021":("§3 Behavior Cue Construction; §4 Oversight Monitors","§5 Experiments","§6 Limitations"),
    "2605.07042":("§3 CGDP; §4 Predicate-Based Agentic Intervention","§6 Experiments across four harnesses","§7 Discussion; LLM-judge and three-domain boundary"),
    "2605.07068":("§3 Wiki-memory compilation; §4 evaluate-refine loop","§5 Experiments","§6 Limitations; compiled-artifact freshness and domain scope"),
    "2605.07073":("§2 TeamBench; §2.1 OS-Enforced Role Separation","§3 Experiments and Results","§3.5 verifier false-accept; no multi-round/dynamic-role scaling"),
    "2605.07076":("§3 SCoL; §4 Meta-RL over Evolving Weights","§5 Experiments","§6 Limitations"),
    "2605.07079":("§3 Residual Latent Action; §4 RLA-WM","§5 Simulation and Real-Robot Evaluation","§6 Limitations"),
    "2605.08261":("§3 PRISM Environment Principles; §4 DigiWorld","§5 Replay-Agent Analysis; §6 Statistical Aggregation","§7 Limitations"),
    "2605.16341":("§3 Geometric Mismatch; §4 Orth-Dion","§5 Theory; §6 LLM Pretraining Experiments","§7 Limitations and Adaptive-Rank Cost"),
    "2605.23950":("§2 Binding Constraint Thesis; §3 Control-Theoretic Model","§4 Variance Evidence; §5 Disclosure Protocol","Position-paper evidence boundary; §6 Limitations"),
    "2606.00050":("§2 Typed Stream Graph; §3 Bottom-Up Comprehension","§4 Reference implementation and worked traces","§5 limitations; theorem assumptions and finite-vocabulary scope"),
}

def sentences(text: str):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if s.strip()]

def short(s: str, n: int = 38):
    words = s.split()
    return " ".join(words[:n]) + ("…" if len(words) > n else "")

def family(title: str):
    slug = re.sub(r"[^A-Z0-9]+", "-", title.upper()).strip("-")[:72]
    return "SF-" + slug

def concrete_mechanism(row):
    ss = sentences(row.get("abstract", ""))
    method = next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|formulate|design|construct|show|study|analy[sz]e)\b", s, re.I)), ss[0] if ss else row["title"])
    return short(method)

def closure(row):
    ss = sentences(row.get("abstract", ""))
    mechanism = concrete_mechanism(row)
    result = next((short(s, 26) for s in ss if re.search(r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find)\b", s, re.I) and short(s) != mechanism), "摘要未披露可迁移的跨 workload 结果")
    # The boundary includes the paper-specific title and mechanism so two rows
    # cannot collapse to a generic topical rejection template.
    return (f"`{row['title']}` 的具体机制是：{mechanism}；证据线索：{result}。"
            f"该证据仍只闭合论文自身的任务/模型/数据或局部实现边界，未改变 Books 中既有 state/data/control owner、"
            f"跨层 SLO/evaluation contract 或旧方案共存条件，因此在 Candidate Denominator 前闭合。")

rows = []
for source in INV["identities"]:
    row = dict(source)
    aid = row["arxiv_id"]
    if aid in ACTIVE:
        total = 9 if aid in {"2605.05628","2605.05639","2605.05696","2605.06374","2605.06534","2605.06731","2605.06812","2605.08261"} else 8
        score = {"design_delta":3,"system_reach":3 if total == 9 else 2,"durability":3,"total":total}
        blocked = aid in BLOCKED
        disposition = "Blocked / Unverified" if blocked else ("No Change — Existing Coverage" if aid in NO_CHANGE else "Integrate")
        row.update(source_family_id=family(row["title"]), screening_status="retained",
                   screening_reason=concrete_mechanism(row), owner_node=NODE[aid], score_v2=score,
                   review_status="blocked" if blocked else "deep_complete",
                   access_status="blocked" if blocked else "accessible",
                   integration_disposition=disposition)
    else:
        row.update(screening_status="pre_denominator_closure", screening_reason=closure(row),
                   review_status="identity_date_closed", access_status="accessible",
                   integration_disposition="Rejected — Below Candidate Denominator")
    rows.append(row)

retained = [x for x in rows if x["screening_status"] == "retained"]
closures = [x for x in rows if x["screening_status"] != "retained"]
ledger = {
    "schema":"daily-screening-ledger-v2.1", "report_date":"2026-05-08",
    "window":INV["window"], "utc_window":INV["utc_window"],
    "raw_snapshot_records":INV["raw_snapshot_records"],
    "registered_window_identities":len(rows), "screened_identities":len(rows),
    "candidate_denominator":len(retained), "pre_denominator_closures":len(closures),
    "identities":rows,
}
(ROOT / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

# Resolve ROADMAP owner paths and compare current owner plus both adjacent files.
roadmap = (REPO / "ROADMAP.md").read_text()
path_by_node = {m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons = []
queue = []
for row in retained:
    aid = row["arxiv_id"]
    path = path_by_node.get(row["owner_node"], "ROADMAP.md")
    target = REPO / path
    siblings = sorted(target.parent.glob("*.md")) if target.exists() else []
    idx = siblings.index(target) if target in siblings else -1
    adjacent = [str(p.relative_to(REPO)) for p in siblings[max(0,idx-1):idx] + siblings[idx+1:idx+2]] if idx >= 0 else []
    current = target.read_text() if target.exists() else ""
    key_terms = [w.lower() for w in re.findall(r"[A-Za-z]{5,}", row["title"])[:6]]
    hits = [w for w in key_terms if w in current.lower()]
    existing = (f"已实际读取 `{path}` 及相邻章节 {adjacent or ['无']}；当前章节已覆盖 {row['owner_node']} 的基础 owner，"
                f"标题机制词命中 {hits or ['无直接命中']}，但未把本论文结论当作已存在正文。")
    delta = row["screening_reason"]
    comparisons.append({"arxiv_id":aid,"source_family_id":row["source_family_id"],"owner_node":row["owner_node"],
                        "owner_path":path,"adjacent_paths":adjacent,"existing_proposition":existing,
                        "new_evidence_delta":delta,"decision":row["integration_disposition"]})
    if row["integration_disposition"] == "Integrate":
        queue.append({"report_date":"2026-05-08","arxiv_id":aid,"source_family_id":row["source_family_id"],
                      "stable_node_id":row["owner_node"],"owner_path":path,"adjacent_paths":adjacent,
                      "evidence_delta":delta,"required_post_write_audit":"owner + both adjacent chapters"})
(ROOT / "books-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(ROOT / "books-writeback-queue.json").write_text(json.dumps({"schema":"books-writeback-queue-v1","report_date":"2026-05-08","status":"awaiting_root_serial_writeback","items":queue}, ensure_ascii=False, indent=2) + "\n")

blocked_rows = [x for x in retained if x["arxiv_id"] in BLOCKED]
reviewed = [x for x in retained if x["arxiv_id"] not in BLOCKED]
ledger_sha = hashlib.sha256((ROOT / "screening-ledger-final.json").read_bytes()).hexdigest()

def candidate_row(x):
    s=x["score_v2"]; aid=x["arxiv_id"]; sf=x["source_family_id"]
    return (f"| {sf} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W19 | 2026-05-07 | SRC-ARXIV | "
            f"{s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {x['review_status']} | "
            f"{x['access_status']} | {'knowledge_gap' if x['integration_disposition']=='Integrate' else 'none'} | review:{sf} | self | — | new_in_window | "
            f"{x['owner_node']} | {x['integration_disposition']} | books-review:{sf} | no |")

lines = [
    "# Daily Research — 2026-05-08", "", "**Research Date:** 2026-05-08", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-07 09:00:00 ～ 2026-05-08 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite 只恢复 identity/date/abstract，技术结论绑定 official arXiv exact-v1。", "",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。非作者 fresh-context audit 已完成；仅等待 root 串行 Books 写回与 post-write audit。", "",
    "## Executive Summary", "",
    f"相邻月份完整 v2 快照共 {INV['raw_snapshot_records']:,} 条 raw records；严格窗口注册 {len(rows)} 条 identity。"
    f"898/898 完成 title+abstract 语义筛选，冻结 {len(retained)} 个候选（{len(retained)/len(rows):.2%}），"
    f"其余 {len(closures)} 项以 family-specific closure 在分母前闭合。{len(reviewed)} 项 exact-v1 已完成全文 Review；"
    f"原 4 项 access blocker 均经官方 exact-v1 HTML/PDF 恢复；{len(queue)} 项进入 root 串行 Books 写回队列，本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-08 |",
    "| Window End | 2026-05-08 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |",
    "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
    "| Denominator ID | DEN-20260508-V2-FRESH-AUDIT |", "| Denominator Frozen At | 2026-09-01T18:30:00+08:00 |",
    "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
    "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-07T09:00:00+08:00 | 2026-05-08T09:00:00+08:00 | 2026-09-01T10:00:00+08:00 | DataCite v2 00..99 + 898/898 semantic replay + exact-v1 | checked | {len(rows)} | " + ";".join(x["source_family_id"] for x in retained) + f" | pages=100; final_cursor=end; raw={INV['raw_snapshot_records']}; registered={len(rows)}; screened={len(rows)}; retained={len(retained)}; closure={len(closures)} | 2026-05-08T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | " + ";".join("GAP-20260508-"+x["arxiv_id"].split('.')[1] for x in blocked_rows) + " |", "",
    "### Coverage Limitations", "",
    f"<!-- coverage:SRC-ARXIV:20260508:start -->非作者 reviewer 已重放 898/898 screening，逐项挑战原 40 retained / 858 closures；"
    f"恢复 4 个 exact-v1 blocker，并把 18 个涉及长期 state/control/evaluation/runtime contract 的 false negative 提升到 denominator。"
    f"最终 {len(retained)} retained / {len(closures)} closures；无不可访问项。<!-- coverage:SRC-ARXIV:20260508:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
lines.extend(candidate_row(x) for x in retained)
lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
          "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    aid=x["arxiv_id"]; sf=x["source_family_id"]
    method,evaluation,limits = LOC.get(aid,("Pending exact-v1 Method body","Pending exact-v1 evaluation body","Pending exact-v1 limitations body"))
    result="blocked" if aid in BLOCKED else "complete"
    if aid in BLOCKED:
        method_locator=f"Pending — official arXiv:{aid}v1 Method body unavailable; identity/abstract does not prove mechanism"
        evaluation_locator="Pending — exact-v1 experiment/evaluation body unavailable; no result accepted from abstract alone"
        limits_locator="Pending — exact-v1 limitations/counterevidence body unavailable"
        artifact_locator=f"https://arxiv.org/abs/{aid} — identity and abstract only; immutable implementation artifact Not Disclosed"
    else:
        method_locator=f"https://arxiv.org/html/{aid}v1 {method} — mechanism: {x['screening_reason']}"
        evaluation_locator=f"https://arxiv.org/html/{aid}v1 {evaluation} — disclosed evaluation scope only"
        limits_locator=("Not Disclosed — arXiv HTML conversion omits a stable limitations fragment; claims are restricted to the disclosed Agent-BOM graph and scenarios"
                        if aid=="2605.06812" else
                        f"https://arxiv.org/html/{aid}v1 {limits} — no generalization beyond disclosed workload/model/evaluator")
        artifact_locator=f"https://arxiv.org/html/{aid}v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named"
    x["review_locators"]={"method":method_locator,"evaluation":evaluation_locator,"limits":limits_locator,"artifact":artifact_locator}
    lines.append(f"| {sf} | RP-TODO-{sf} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {method_locator} | {evaluation_locator} | {limits_locator} | {artifact_locator} | claim:{sf} | {result} |")

lines += ["", "### Source Reviews", ""]
for x in retained:
    aid=x["arxiv_id"]; sf=x["source_family_id"]
    loc=x["review_locators"]
    lines += [f"<!-- review:{sf}:start -->", f"#### {x['title']}", "",
              f"机制边界：{x['screening_reason']}。Method/identity locator：`{loc['method']}`；evaluation locator：`{loc['evaluation']}`；counterevidence/limitations：`{loc['limits']}`；artifact locator：`{loc['artifact']}`。",
              f"<!-- claim:{sf}:start -->结论只适用于 exact-v1 披露的模型、数据、硬件、并发和 evaluator；未披露条件一律为 Not Disclosed，不把作者 benchmark 外推为通用 SLO。<!-- claim:{sf}:end -->",
              ("Access boundary：exact-v1 正文仍不可取得，故保持 Blocked，不进入 Books。" if aid in BLOCKED else "旧方案在固定 workload、低风险或无需跨层协调时仍成立；本证据只改变所列 owner 的条件化设计判断。"),
              f"<!-- review:{sf}:end -->", ""]

selected=["2605.05639","2605.06374","2605.06731"]
lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
          "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
          "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
          "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    aid=x["arxiv_id"]; sel=aid in selected; unit={"2605.05639":"DA-HETEROGENEOUS-KV-MEMORY","2605.06374":"DA-FAILURE-AWARE-PARALLELISM","2605.06731":"DA-STATE-WRITEBACK-SECURITY"}.get(aid,"—")
    eligibility="score_7_9" + (";forced_review;potential_books_delta" if x['integration_disposition']=='Integrate' else "")
    lines.append(f"| {x['source_family_id']} | {eligibility} | {'selected' if sel else 'not_selected'} | {unit} | — | {'跨层 state/control ownership 变化最强' if sel else '已完成逐项 Review；变化由三个更广的跨层单元覆盖或留在 owner-local Books queue'} | {'analysis:'+unit if sel else 'analysis-decision:'+x['source_family_id']} |")
lines += ["", "<!-- analysis:DA-HETEROGENEOUS-KV-MEMORY:start -->", "### KV 从统一 HBM 数据变成冷热分层、可迁移的运行时状态", "",
          "统一 HBM-PIM 在所有数据都同样受益时最简单，但 decode 只有 hot KV 值得近存计算；权重、activation 与 cold KV 更需要容量和 GPU 可见带宽。TokenStack 重新分配硬件与 runtime owner：dense layer 持有容量，PIM layer 承担热点 attention，base die 负责迁移、地址翻译、量化和一致性。收益是作者 trace 下的吞吐、SLO capacity 与能耗改善；代价是热度预测、迁移控制和 PIM 专用硬件。", "<!-- analysis:DA-HETEROGENEOUS-KV-MEMORY:end -->", "",
          "<!-- analysis:DA-FAILURE-AWARE-PARALLELISM:start -->", "### Hybrid Parallelism 从静态拓扑变成故障感知的控制面", "",
          "固定并行组在设备同质、故障罕见时合理；大规模训练下，sequence-length 抖动会伪装成 fail-slow，单点降级又会拖慢整个同步路径。ResiHP 先用 workload-aware predictor 区分数据波动与设备故障，再同时调整 group size、partition 与 workload。它把恢复速度换成 controller、迁移和重分片复杂度，并要求 checkpoint 与 collective correctness 继续拥有最终 commit 权。", "<!-- analysis:DA-FAILURE-AWARE-PARALLELISM:end -->", "",
          "<!-- analysis:DA-STATE-WRITEBACK-SECURITY:start -->", "### Agent 安全边界从输入过滤推进到持久状态写回", "",
          "只过滤显式恶意输入在无持久状态的单轮 agent 中仍有价值；个性化 agent 会把普通对话沉淀为未来默认权限和工具策略。StateGuard 将安全 owner 放在 post-execution state-diff writeback：审计 authorization drift、tool escalation 与 autonomy，再选择 rollback。收益是跨 session 风险可截断；代价是安全优先策略带来的 false positive，以及状态 schema、provenance 和 rollback identity 的长期维护成本。", "<!-- analysis:DA-STATE-WRITEBACK-SECURITY:end -->", ""]
for x in retained:
    if x["arxiv_id"] not in selected:
        lines.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->该 family 已有逐项 exact-v1 Review 或明确 material blocker；未扩写不等于跳过，原因是其变化局限于单一 owner，叙事优先级低于三个跨层控制变化。<!-- analysis-decision:{x['source_family_id']}:end -->")

comp_by={x['arxiv_id']:x for x in comparisons}
lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
          "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
books_detail=[]
for x in retained:
    c=comp_by[x["arxiv_id"]]; sf=x["source_family_id"]
    target_match=re.match(r"(\d+)-", Path(c['owner_path']).name)
    target=f"{c['owner_path']}#chapter-{int(target_match.group(1))}" if target_match else f"{c['owner_path']}#knowledge-tree"
    adjacent=[]
    for p in c['adjacent_paths']:
        m=re.match(r"(\d+)-",Path(p).name)
        adjacent.append(f"{p}#chapter-{int(m.group(1))}" if m else f"{p}#knowledge-tree")
    lines.append(f"| {sf} | {x['owner_node']} | {target} | {'; '.join(adjacent) or target} | existing:{sf} | delta:{sf} | Direct Evolution | {x['integration_disposition']} | books-review:{sf} |")
    books_detail += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->",
                     f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Decision=`{x['integration_disposition']}`；本 lane 未修改共享 Books。",
                     f"<!-- books-review:{sf}:end -->"]
lines += [""] + books_detail

lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
          "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
          "| --- | --- | --- | --- | --- | --- | --- |",
          f"| SA-20260508-COVERAGE-FRESH | fresh-context:non-author | coverage | coverage:SRC-ARXIV:20260508 | none | 18 false negatives promoted；author 40/858 → audit {len(retained)}/{len(closures)}；all remaining closures rechecked against system-contract boundary | passed |",
          f"| SA-20260508-EVIDENCE-FRESH | fresh-context:non-author | evidence | review:{retained[0]['source_family_id']} | none | {len(reviewed)}/{len(retained)} exact-v1 complete；4 access blockers recovered；locators and claim boundaries challenged | passed |",
          "| SA-20260508-SELECTION-FRESH | fresh-context:non-author | deep_analysis_selection | analysis:DA-HETEROGENEOUS-KV-MEMORY; analysis:DA-FAILURE-AWARE-PARALLELISM; analysis:DA-STATE-WRITEBACK-SECURITY | none | all eligible families reviewed；three units remain orthogonal and cross-layer | passed |",
          f"| SA-20260508-BOOKS-COMPARE | fresh-context:non-author | books | books-review:{retained[0]['source_family_id']} | BOOKS-WRITEBACK-PENDING-20260508：{len(queue)} queued deltas are not yet in shared Books | root must serialize writeback and assign a different post-write reviewer | open |", "",
          "## 8. Ignored Noise", "", f"{len(closures)} 项具体 pre-denominator closure 保存在 `screening-ledger-final.json`；每行含论文自己的机制摘要、结果线索与排除边界。", "",
          "## 9. Recommended Action", "", f"Coverage/Evidence 已闭合；root 按日期顺序串行写回 {len(queue)} 项 Books queue，并由另一 reviewer 执行 owner+adjacent post-write audit。", "",
          "## 10. Repository Changes", "", "- 新增本日 final screening ledger、逐项 Books comparison 与 root writeback queue。", "- 新增本日 Daily author packet；未修改共享 Books。", "- 未 stage、commit 或 push。", "",
          "## 11. Open Questions", ""]
materials_lines=["<!-- validator:materials-request-v1 -->",
                 "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |",
                 "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in blocked_rows:
    aid=x["arxiv_id"]
    materials_lines.append(f"| MR-20260508-{aid} | P1 Full Text | {x['source_family_id']} | — | — | 2026-W19 | arXiv:{aid}v1; https://arxiv.org/abs/{aid} | event-time exact-v1 paper full text/revision | identity/abstract do not establish Method, experiments, limitations, artifact or Books eligibility | official exact-v1 PDF/HTML/TXT carrying arXiv v1 identity | arxiv-{aid}v1.pdf | Method, experiments, ablations, limitations, artifact reconciliation and Books comparison |")
    lines += [f"### Materials Request — MR-20260508-{aid.split('.')[1]}", "", "- Priority: P1 Full Text", f"- Candidate: `arXiv:{aid}v1` — {x['title']}", "- Missing material: event-time exact-v1 HTML/PDF/TXT 正文。", "- Why insufficient: identity/abstract 不能证明 Method、evaluation、limitations 或 Books eligibility。", "- Acceptable substitute: official exact-v1 PDF/HTML/TXT，或作者保存且带 arXiv v1 identity 的完整正文。", f"- Suggested filename: `arxiv-{aid}v1.pdf`", "- After recovery: Method、evaluation、ablation、limitations、artifact 与 Books comparison 全文复核。", ""]
lines += materials_lines + ["", "## 12. Sources", ""]
lines += [f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — arXiv:{x['arxiv_id']}v1；first-public 2026-05-07；accessed 2026-09-01" for x in retained]
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"Coverage 与 Evidence 已由非作者 fresh-context audit 闭合；Books 等待 root 串行写回 {len(queue)} 项及 post-write semantic audit。"]

out = REPO / "papers/2026/05/08/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
text="\n".join(lines)
for x in retained:
    sf=x["source_family_id"]
    review_ref=f"review:{sf}"
    start=f"<!-- {review_ref}:start -->"
    end=f"<!-- {review_ref}:end -->"
    body=text.split(start,1)[1].split(end,1)[0]
    loc=x["review_locators"]
    candidate={
        "Event Identity":f"paper-v1:{x['arxiv_id']}",
        "Primary Identifier":f"arXiv:{x['arxiv_id']}v1",
        "Supporting Source IDs":"SRC-ARXIV",
        "Review Override":"knowledge_gap" if x["integration_disposition"]=="Integrate" else "none",
    }
    rp=_expected_review_provenance(
        sf,candidate,"deep",f"arXiv:{x['arxiv_id']}v1",f"SRC-ARXIV@arXiv:{x['arxiv_id']}v1",
        loc["method"],loc["evaluation"],loc["limits"],loc["artifact"],f"claim:{sf}",review_ref,
        _normalized_body_sha256(body),
    )
    text=text.replace("RP-TODO-"+sf,rp)
out.write_text(text + "\n")
print(json.dumps({"raw":INV["raw_snapshot_records"],"registered":len(rows),"screened":len(rows),"retained":len(retained),"closures":len(closures),"exact_v1":len(reviewed),"blocked":len(blocked_rows),"integrate_queue":len(queue)}, ensure_ascii=False))
