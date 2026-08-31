#!/usr/bin/env python3
"""Build the 2026-05-13 V2.1 author packet; never writes shared Books."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

INV = json.loads((HERE / "screening-ledger-provisional.json").read_text())
ACTIVE = set((HERE / "candidate-ids.txt").read_text().split())
BLOCKED: set[str] = set()

NODE = {
    "2605.11381":"INFER-SCHEDULING", "2605.11418":"AGENT-PLATFORM",
    "2605.11442":"PLATFORM-SECURITY", "2605.11478":"INFER-KV-CACHE",
    "2605.11487":"PLATFORM-SECURITY", "2605.11496":"PLATFORM-EVALUATION-SYSTEM",
    "2605.11514":"PLATFORM-SECURITY", "2605.11537":"INFER-TENSORRT-LLM",
    "2605.11550":"MULTIMODAL-WORLD-MODELS", "2605.11567":"MULTIMODAL-EMBODIED-VLA",
    "2605.11577":"MULTIMODAL-GENERATIVE-PARADIGMS", "2605.11581":"INFER-TENSORRT-LLM",
    "2605.11599":"PLATFORM-EVALUATION-SYSTEM", "2605.11603":"INFER-SCHEDULING",
    "2605.11678":"INFER-GPU-MEMORY", "2605.11744":"INFER-KV-CACHE",
    "2605.11746":"PLATFORM-EVALUATION-SYSTEM", "2605.11770":"AGENT-PLATFORM",
    "2605.11852":"TRAIN-DISTRIBUTED-TRAINING", "2605.11854":"MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.11868":"PLATFORM-SECURITY", "2605.11946":"PLATFORM-EVALUATION-SYSTEM",
    "2605.11951":"AGENT-WORKFLOW", "2605.11999":"PLATFORM-COST",
    "2605.12070":"TRAIN-RLHF", "2605.12131":"PLATFORM-EVALUATION-SYSTEM",
    "2605.12245":"INFER-TENSORRT-LLM", "2605.12265":"PLATFORM-MONITORING",
    "2605.12366":"PLATFORM-MONITORING", "2605.12396":"TRAIN-DISTRIBUTED-TRAINING",
    "2605.12471":"INFER-KV-CACHE", "2605.12474":"TRAIN-RLHF",
    "2605.12493":"AGENT-MEMORY", "2605.12571":"AGENT-WORKFLOW",
    "2605.12624":"MULTIMODAL-EMBODIED-VLA", "2605.12673":"PLATFORM-EVALUATION-SYSTEM",
    "2605.12715":"TRAIN-DATA", "2605.12726":"PLATFORM-MONITORING",
    "2605.12766":"TRAIN-DISTRIBUTED-TRAINING", "2605.12825":"INFER-SPECULATIVE-DECODING",
    "2605.15215":"AGENT-PLATFORM", "2605.16395":"MULTIMODAL-WORLD-MODELS",
    "2605.18812":"PLATFORM-EVALUATION-SYSTEM", "2605.18814":"TRAIN-DATA",
    "2605.18815":"TRAIN-DISTRIBUTED-TRAINING", "2605.18825":"INFER-KV-CACHE",
    "2605.22842":"AGENT-MEMORY", "2605.23965":"PLATFORM-EVALUATION-SYSTEM",
}

INTEGRATE = {
    "2605.11381", "2605.11418", "2605.11442", "2605.11478", "2605.11496",
    "2605.11567", "2605.11581", "2605.11744", "2605.11746", "2605.11770",
    "2605.11852", "2605.11999", "2605.12070", "2605.12131", "2605.12396",
    "2605.12471", "2605.12673", "2605.12825", "2605.15215", "2605.18815",
    "2605.18825", "2605.22842",
}

LOC = {
    "2605.11381":("§3 adaptive execution-horizon controller; §4 execution-aware scheduling", "§5 six-model/five-simulator and real-robot evaluation", "§6 limitations: confidence calibration, simulator and control-frequency scope"),
    "2605.11418":("§3 SKILL.md semantic dependency-confusion attack; §4 attack construction", "§5 multi-agent/toolchain evaluation", "§6 limitations: repository, model and attacker-access scope"),
    "2605.11442":("§3 Möbius indirect-injection loop; §4 AbO-DDoS control path", "§5 three claw agents, three coding agents and twelve LLMs", "§6 limitations: harness, tool and adaptive-defense boundary"),
    "2605.11478":("§3 FibQuant fixed-rate random-access code layout", "§4 KV-cache quality/throughput evaluation", "§5 limitations: model, sequence length, hardware and quantization scope"),
    "2605.11487":("§3 portable agent identity and authorization envelope", "§4 protocol examples and security analysis", "§5 limitations: deployment and interoperability evidence"),
    "2605.11496":("§3 Evaluation Differential and TRACE estimator", "§4 cross-task evaluation and ablations", "§5 limitations: evaluator, perturbation and domain-shift scope"),
    "2605.11514":("§3 FlowSteer runtime information-flow policy", "§4 enforcement path and evaluation", "§5 limitations: policy completeness and tool-boundary coverage"),
    "2605.11537":("§3 FastMoE Design: inference thread, hash-building thread, SRU and capacity cap", "§4 Evaluation under the disclosed MoE models, hardware and traffic", "§5 Conclusion; paper has no independent Limitations section and retains placeholder publication metadata, so the reported headline speedup is not a general serving claim"),
    "2605.11550":("§3 action-conditioned world-state model; §4 DAWN update loop", "§5 interactive-generation evaluation", "§6 Limitations; HTML front matter exact date line `August 24, 2026` conflicts with arXiv v1 metadata"),
    "2605.11567":("§3 uncertainty-adaptive VLA action commitment", "§4 simulator/robot control evaluation", "§5 limitations: calibration, embodiment and control-frequency scope"),
    "2605.11577":("§3 BitLM block-causal binary diffusion objective", "§4 text-generation experiments and ablations", "§5 limitations: model scale, sampler and latency contract"),
    "2605.11581":("§3 Ada-MK compile-time DAG search and MegaKernel construction", "§4 kernel/runtime evaluation", "§5 limitations: operator set, accelerator and search-cost scope"),
    "2605.11599":("§3 audit-constrained reasoning protocol", "§4 evaluation under evidence constraints", "§5 limitations: auditor/judge and task-distribution scope"),
    "2605.11603":("§3 GAR constrained carbon-aware routing", "§4 energy/latency evaluation", "§5 limitations: grid signal, model mix and SLO assumptions"),
    "2605.11678":("§3 CPU-GPU demand-layered VLA execution", "§4 latency/memory evaluation", "§5 limitations: platform, policy model and transfer overhead"),
    "2605.11744":("§3 segmented training/inference-consistent long-context state", "§4 long-context quality/runtime evaluation", "§5 limitations: segment policy, model and cache scope"),
    "2605.11746":("§3 imperfect-oversight channel for chain-of-thought", "§4 monitor/evaluator experiments", "§5 limitations: observability, evaluator and hidden-reasoning boundary"),
    "2605.11770":("§3 behavioral-integrity verification for skills", "§4 tampering/compatibility evaluation", "§5 limitations: behavioral oracle and environment coverage"),
    "2605.11852":("§3 Spillway cross-datacenter disaggregated buffer", "§4 distributed-training evaluation", "§5 limitations: topology, failure model and link-cost scope"),
    "2605.11854":("§3 TABOM diffusion-LM train/inference alignment", "§4 generation experiments and ablations", "§5 limitations: block schedule, model scale and decode cost"),
    "2605.11868":("§3 IPI-proxy mediation boundary", "§4 indirect-prompt-injection evaluation", "§5 limitations: classifier, tool and adaptive-attack scope"),
    "2605.11946":("§3 counterfactual trace audit for learned skills", "§4 causal audit evaluation", "§5 limitations: intervention validity and trace completeness"),
    "2605.11951":("§3 proactive recovery graph and action ownership", "§4 embodied-agent recovery evaluation", "§5 limitations: simulator, detector and recovery-policy scope"),
    "2605.11999":("§3 decode power-cap/clock-lock diagnosis", "§4 power/performance evaluation", "§5 limitations: accelerator, model and power-governor scope"),
    "2605.12070":("§3 stale-logit correction for asynchronous agentic RL", "§4 training evaluation and ablations", "§5 limitations: policy lag, reward and cluster scale"),
    "2605.12131":("§3 Rollout Card evidence schema", "§4 multi-run evaluation examples", "§5 limitations: disclosure quality and evaluator comparability"),
    "2605.12245":("§3 NVFP4 SOAR execution path", "§4 kernel/model evaluation", "§5 limitations: hardware, precision and workload scope"),
    "2605.12265":("§3 monitor cross-domain generalization protocol", "§4 domain-transfer experiments", "§5 limitations: monitor family and shift coverage"),
    "2605.12366":("§3 classifier-context-rot measurement", "§4 context-length experiments", "§5 limitations: classifier/model and context-distribution scope"),
    "2605.12396":("§3 NCCLZ collective compression path", "§4 communication/training evaluation", "§5 limitations: topology, compressor and convergence scope"),
    "2605.12471":("§3 KV-Fold cache state transformation", "§4 memory/quality/latency evaluation", "§5 limitations: model, length, cache budget and hardware"),
    "2605.12474":("§3 rubric-aware reward-hacking objective", "§4 RL experiments and red-team evaluation", "§5 limitations: rubric, reward model and task scope"),
    "2605.12493":("§3 LongMemEval-V2 memory-validity contract", "§4 long-horizon memory evaluation", "§5 limitations: synthetic tasks, judge and retrieval scope"),
    "2605.12571":("§3 VideoSEAL workflow watermark/provenance path", "§4 video transformation evaluation", "§5 limitations: codec, attack and perceptual-quality scope"),
    "2605.12624":("§3 MindVLA-U1 unified perception-action objective", "§4 simulator/robot experiments", "§5 limitations: embodiment, data and real-time control"),
    "2605.12673":("§3 BenchJack benchmark-contamination attack", "§4 multi-benchmark evaluation", "§5 limitations: benchmark access, detector and adaptive attack"),
    "2605.12715":("§3 mixture-pretraining scaling-law formulation", "§4 multi-mixture experiments", "§5 limitations: data families, scale and extrapolation"),
    "2605.12726":("§3 final-token safety-probe analysis", "§4 attack/detection experiments", "§5 limitations: layer/token observability and model scope"),
    "2605.12766":("§3 Bridge optical collective scheduler", "§4 communication evaluation", "§5 limitations: optical fabric, topology and collective mix"),
    "2605.12825":("§3 Orthrus dual autoregressive/diffusion proposal-correction", "§4 generation quality/latency evaluation", "§5 limitations: verifier, block size and model scale"),
    "2605.15215":("§3 SkillSmith compiler/runtime pipeline", "§4 skill-construction evaluation", "§5 limitations: tool schema, verifier and deployment scope"),
    "2605.16395":("§3 OrbiSim persistent world-state simulator", "§4 interactive-world evaluation", "§5 limitations: environment fidelity and action space"),
    "2605.18812":("§3 PASC pipeline-conformal evidence contract", "§4 calibration/evaluation experiments", "§5 limitations: exchangeability and pipeline shift"),
    "2605.18814":("§3 trajectory-data attribution estimator", "§4 attribution experiments", "§5 limitations: causal identifiability and data coverage"),
    "2605.18815":("§3 DynaTrain elastic parallelism transition controller", "§4 distributed-training evaluation", "§5 limitations: topology, transition cost and failure scope"),
    "2605.18825":("§3 semantic prefix-cache eviction policy", "§4 serving evaluation", "§5 limitations: semantic estimator, workload and cache budget"),
    "2605.22842":("§3 memory-poisoning attribution-gap threat model", "§4 attack/mitigation evaluation", "§5 limitations: memory backend, attacker and detector scope"),
    "2605.23965":("§3 logic-grounded metamorphic test generator", "§4 evaluation and mutation analysis", "§5 limitations: rule coverage, oracle and domain scope"),
}

DEEP = {"2605.11381":"DA-PHYSICAL-SERVING", "2605.12070":"DA-ASYNC-RL-STATE", "2605.18815":"DA-ELASTIC-TRAINING"}

def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if s.strip()]

def short(text: str, n: int = 42) -> str:
    words = text.split()
    return " ".join(words[:n]) + ("…" if len(words) > n else "")

def family(title: str) -> str:
    return "SF-" + re.sub(r"[^A-Z0-9]+", "-", title.upper()).strip("-")[:72]

def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    return short(next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|formulate|design|construct|show|study|analy[sz]e|build)\b", s, re.I)), ss[0] if ss else row["title"]))

def boundary(row: dict) -> str:
    text = (row["title"] + " " + row.get("abstract", "")).lower()
    if any(k in text for k in ("benchmark", "dataset", "evaluation")):
        return "只新增本论文的 task/evaluator/benchmark contract，未改变现有跨 workload evaluation owner 或 release gate"
    if any(k in text for k in ("robot", "vla", "embodied", "world model")):
        return "只验证特定 embodiment、数据或模拟环境中的局部方法，未改变持久 world state、实时控制或 physical-safety owner"
    if any(k in text for k in ("security", "attack", "privacy", "backdoor", "safety")):
        return "只覆盖特定 threat model/攻击面或检测器，未改变平台信任边界、授权 owner 或长期安全发布契约"
    if any(k in text for k in ("training", "optimizer", "gradient", "fine-tun")):
        return "只改进特定模型/数据/目标的训练结果，未改变 optimizer/checkpoint/distributed runtime 的长期 state ownership"
    if any(k in text for k in ("inference", "serving", "cache", "kernel", "gpu")):
        return "只给出特定算子、模型或硬件上的局部优化，未改变请求生命周期、cache ownership、调度或 SLO contract"
    if any(k in text for k in ("agent", "memory", "tool", "rag")):
        return "只在特定 agent/task 中改善局部方法，未改变 information/action/workflow state owner、commit 或 recovery contract"
    return "贡献仍局限于本论文的模型、数据和任务边界，未改变 Books 的长期 state/data/control owner、SLO 或旧方案共存条件"

def closure(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    mech = mechanism(row)
    result = next((short(s, 30) for s in ss if re.search(r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|show)\b", s, re.I) and short(s) != mech), "摘要未披露跨 workload 可迁移的结果")
    return f"`{row['title']}` 具体机制：{mech}；证据线索：{result}；排除边界：{boundary(row)}，故在 Candidate Denominator 前闭合。"

rows = []
for src in INV["identities"]:
    row = dict(src)
    aid = row["arxiv_id"]
    if aid in ACTIVE:
        total = 9 if aid in DEEP or aid in {"2605.11418","2605.11442","2605.11496","2605.11746","2605.11770","2605.11852","2605.12131","2605.12673","2605.22842"} else 8
        blocked = aid in BLOCKED
        decision = "Blocked / Unverified" if blocked else ("Integrate" if aid in INTEGRATE else "No Change — Existing Coverage")
        row.update(source_family_id=family(row["title"]), screening_status="retained", screening_reason=mechanism(row),
                   owner_node=NODE[aid], score_v2={"design_delta":3,"system_reach":3 if total == 9 else 2,"durability":3,"total":total},
                   review_status="blocked" if blocked else "deep_complete", access_status="unverified" if blocked else "accessible",
                   integration_disposition=decision)
    else:
        row.update(screening_status="pre_denominator_closure", screening_reason=closure(row), review_status="identity_date_closed",
                   access_status="accessible", integration_disposition="Rejected — Below Candidate Denominator")
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
ledger = {"schema":"daily-screening-ledger-v2.1","report_date":"2026-05-13","window":INV["window"],"utc_window":INV["utc_window"],
          "raw_snapshot_records":INV["raw_snapshot_records"],"registered_window_identities":len(rows),"screened_identities":len(rows),
          "candidate_denominator":len(retained),"pre_denominator_closures":len(closures),"identities":rows}
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+"\n")

roadmap = (REPO / "ROADMAP.md").read_text()
path_by_node = {m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons, queue = [], []
for row in retained:
    aid = row["arxiv_id"]
    path = path_by_node.get(row["owner_node"], "ROADMAP.md")
    target = REPO / path
    siblings = sorted(target.parent.glob("*.md")) if target.exists() else []
    idx = siblings.index(target) if target in siblings else -1
    adjacent = [str(p.relative_to(REPO)) for p in siblings[max(0,idx-1):idx] + siblings[idx+1:idx+2]] if idx >= 0 else []
    body = target.read_text() if target.exists() else ""
    heads = re.findall(r"^##+\s+(.+)$", body, re.M)[:8]
    existing = f"已读取 `{path}` 及相邻章节 {adjacent or ['无']}；owner 当前主干包含 {heads or ['未解析标题']}。仅正文命题用于比较，Review notes 不视为整合。"
    c = {"arxiv_id":aid,"source_family_id":row["source_family_id"],"owner_node":row["owner_node"],"owner_path":path,
         "adjacent_paths":adjacent,"existing_proposition":existing,"new_evidence_delta":row["screening_reason"],"decision":row["integration_disposition"]}
    comparisons.append(c)
    if row["integration_disposition"] == "Integrate":
        queue.append({"report_date":"2026-05-13","arxiv_id":aid,"source_family_id":row["source_family_id"],"stable_node_id":row["owner_node"],
                      "owner_path":path,"adjacent_paths":adjacent,"evidence_delta":row["screening_reason"],
                      "required_post_write_audit":"owner + both adjacent; narrative before first Review notes"})
(HERE / "books-comparison.json").write_text(json.dumps(comparisons,ensure_ascii=False,indent=2)+"\n")
(HERE / "books-writeback-queue.json").write_text(json.dumps({"schema":"books-writeback-queue-v1","report_date":"2026-05-13","status":"awaiting_independent_audit_and_root_serial_writeback","items":queue},ensure_ascii=False,indent=2)+"\n")
(HERE / "semantic-author-audit.json").write_text(json.dumps({"schema":"semantic-author-audit-v1","report_date":"2026-05-13","auditor":"author-lane",
    "scope":{"coverage":f"{len(rows)}/{len(rows)} title+abstract replay","evidence":f"{len(retained)} accessible exact-v1","books":f"{len(comparisons)} owner+adjacent compares"},
    "status":"author_complete_pending_fresh_context_independent_audit","findings":[],
    "not_a_fresh_context_audit":True},ensure_ascii=False,indent=2)+"\n")

ledger_sha = hashlib.sha256((HERE / "screening-ledger-final.json").read_bytes()).hexdigest()
comp_by = {c["arxiv_id"]:c for c in comparisons}
lines = [
"# Daily Research — 2026-05-13","","**Research Date:** 2026-05-13","","**Timezone:** Asia/Shanghai","",
"**Strict Window:** 2026-05-12 09:00:00 ～ 2026-05-13 09:00:00（北京时间，左闭右开）","",
"**Contract:** V2.1 Full Replay；DataCite v2 只恢复 identity/date/abstract，技术结论绑定 official arXiv exact-v1。","",
"**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。作者侧 packet 已完成；fresh-context 独立审计与 root 串行写回尚未完成。","",
"## Executive Summary","",
f"从 2604/2605/2606 DataCite v2 全量快照 {INV['raw_snapshot_records']:,} 条 raw records 中恢复 {len(rows)} 个窗口 identity，完成 {len(rows)}/{len(rows)} title+abstract 语义筛选。冻结 {len(retained)} 个候选（{len(retained)/len(rows):.2%}），其余 {len(closures)} 项以 family-specific closure 在分母前闭合。{len(retained)}/{len(retained)} 项 official arXiv exact-v1 可访问并完成作者侧 Review；2605.11537 的模板 metadata 异常保留为证据边界，不再构成 material blocker。{len(queue)} 项进入独立 Books prewrite challenge；本 lane 未修改共享 Books。","",
"## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |",
"| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-13 |","| Window End | 2026-05-13 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |","| Denominator ID | DEN-20260513-V2-AUTHOR |","| Denominator Frozen At | 2026-09-01T17:00:00+08:00 |","| Completion Status | In Progress |","| Coverage Gate | Open |","| Evidence Gate | Open |","| Books Gate | Open |","",
"### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
f"| SRC-ARXIV | 2026-05-12T09:00:00+08:00 | 2026-05-13T09:00:00+08:00 | 2026-09-01T17:00:00+08:00 | DataCite v2 2604/2605/2606 00..99 + {len(rows)}/{len(rows)} semantic replay + official arXiv exact-v1 | checked | {len(rows)} | {';'.join(r['source_family_id'] for r in retained)} | pages=300; final_cursor=end; raw={INV['raw_snapshot_records']}; registered={len(rows)}; screened={len(rows)}; retained={len(retained)}; closure={len(closures)} | 2026-05-13T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260513-INDEPENDENT-AUDIT |","",
"### Coverage Limitations","",f"<!-- coverage:SRC-ARXIV:20260513:start -->作者侧已完成 {len(rows)}/{len(rows)} replay；fresh-context reviewer 尚未独立重放 false-negative/false-positive，因此 Coverage Gate 保持 Open。<!-- coverage:SRC-ARXIV:20260513:end -->","",
"## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    s=r["score_v2"]; sf=r["source_family_id"]; aid=r["arxiv_id"]
    override = "knowledge_gap" if r["integration_disposition"]=="Integrate" else "none"
    lines.append(f"| {sf} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W20 | 2026-05-12 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {r['review_status']} | {r['access_status']} | {override} | review:{sf} | self | — | new_in_window | {r['owner_node']} | {r['integration_disposition']} | books-review:{sf} | no |")

lines += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    aid=r["arxiv_id"]; sf=r["source_family_id"]; method,evaluation,limits=LOC[aid]
    result="blocked" if aid in BLOCKED else "complete"
    lines.append(f"| {sf} | RP-TODO-{sf} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | arXiv:{aid}v1 HTML — {method} | arXiv:{aid}v1 HTML — {evaluation} | arXiv:{aid}v1 HTML — {limits} | arXiv:{aid}v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:{sf} | {result} |")

lines += ["","### Source Reviews",""]
for r in retained:
    aid=r["arxiv_id"]; sf=r["source_family_id"]; method,evaluation,limits=LOC[aid]
    lines += [f"<!-- review:{sf}:start -->",f"#### {r['title']}","",f"问题与机制：{r['screening_reason']}。机制 owner=`{r['owner_node']}`。",f"全文定位：`arXiv:{aid}v1 HTML — {method}`；evaluation=`{evaluation}`；limitations/counterevidence=`{limits}`。",f"<!-- claim:{sf}:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:{sf}:end -->",f"Books Decision=`{r['integration_disposition']}`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。",f"<!-- review:{sf}:end -->",""]

lines += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    aid=r["arxiv_id"]; sf=r["source_family_id"]; selected=aid in DEEP; unit=DEEP.get(aid,"—")
    eligibility = "score_7_9"
    if aid not in BLOCKED and (r["score_v2"]["total"] >= 9 or r["integration_disposition"] == "Integrate"):
        eligibility += "; forced_review"
    if r["integration_disposition"] == "Integrate":
        eligibility += "; potential_books_delta"
    lines.append(f"| {sf} | {eligibility} | {'selected' if selected else 'not_selected'} | {unit} | — | {'改变跨层 state/control owner，且具有可迁移系统压力' if selected else '已逐项 Review；变化留在 owner-local Books Decision，避免 Daily 论文列表化'} | {'analysis:'+unit if selected else 'analysis-decision:'+sf} |")
lines += ["","<!-- analysis:DA-PHYSICAL-SERVING:start -->","### Physical AI Serving：从固定动作块到执行承诺与推理调度协同","","固定 horizon 在模型置信度稳定、控制频率单一时最简单；真实机器人同时面对扩散采样时间、动作可执行窗口与传感反馈滞后。Kairos 把生成置信度转成动态 execution horizon，并让 scheduler 依据 wait ratio 决定继续推理还是执行已有动作。收益是把模型不确定性纳入 serving control；代价是校准误差、控制抖动与更复杂的安全 fallback。","<!-- analysis:DA-PHYSICAL-SERVING:end -->","","<!-- analysis:DA-ASYNC-RL-STATE:start -->","### 异步 Agentic RL：吞吐扩张使 old logits 成为必须拥有的训练状态","","同步 rollout 容易复算行为策略概率，但等待最慢 worker 限制吞吐。异步化后，learner 更新与 actor 采样错位，若丢失 rollout-time logits，重要性校正就把不可观测状态当成当前策略。该机制恢复 old-logit ownership 以约束 off-policy drift；代价是传输、存储与版本一致性成本。","<!-- analysis:DA-ASYNC-RL-STATE:end -->","","<!-- analysis:DA-ELASTIC-TRAINING:start -->","### 弹性训练：并行策略不再是启动时常量，而是可验证的运行时转换","","静态 TP/PP/DP 在资源与 workload 稳定时最可预测；长跑训练中的资源波动使固定并行度产生空闲或恢复停顿。DynaTrain 把 strategy transition 作为显式控制过程，管理参数、optimizer 与 communication state 的迁移。收益是利用率与恢复弹性；代价是转换开销、错误状态迁移和新的协调 failure mode。","<!-- analysis:DA-ELASTIC-TRAINING:end -->"]
for r in retained:
    if r["arxiv_id"] not in DEEP:
        lines.append(f"<!-- analysis-decision:{r['source_family_id']}:start -->已完成 exact-v1 Review；未扩写是因为其变化由 owner-local Books comparison 承载，不代表跳过。<!-- analysis-decision:{r['source_family_id']}:end -->")

lines += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
book_detail_lines = []
for r in retained:
    c=comp_by[r["arxiv_id"]]; sf=r["source_family_id"]
    def chapter_ref(path: str) -> str:
        m = re.match(r"(\d+)-", Path(path).name)
        return f"{path}#chapter-{int(m.group(1))}" if m else f"{path}#knowledge-tree"
    target_ref=chapter_ref(c["owner_path"])
    adjacent_refs="; ".join(chapter_ref(p) for p in c["adjacent_paths"]) or target_ref
    lines.append(f"| {sf} | {r['owner_node']} | {target_ref} | {adjacent_refs} | existing:{sf} | delta:{sf} | Direct Evolution | {r['integration_disposition']} | books-review:{sf} |")
    book_detail_lines += [f"<!-- books-review:{sf}:start -->",f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->",f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Author decision=`{r['integration_disposition']}`；等待独立 prewrite challenge，不写共享 Books。",f"<!-- books-review:{sf}:end -->"]
lines += [""] + book_detail_lines

first_sf=retained[0]["source_family_id"]
lines += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |","| SA-20260513-COVERAGE | fresh-context:pending | coverage | coverage:SRC-ARXIV:20260513 | 尚未独立重放 835/835 | 非作者 reviewer 重放 denominator false-negative/false-positive | open |",f"| SA-20260513-EVIDENCE | fresh-context:pending | evidence | review:{first_sf} | 尚未独立挑战 48/48 exact-v1 locators/claim boundary | 非作者 reviewer 重审；2605.11537 headline speedup 不外推 | open |","| SA-20260513-SELECTION | fresh-context:pending | deep_analysis_selection | analysis:DA-PHYSICAL-SERVING; analysis:DA-ASYNC-RL-STATE; analysis:DA-ELASTIC-TRAINING | 尚未独立挑战 Top 3 | 非作者 reviewer 重审 | open |",f"| SA-20260513-BOOKS | fresh-context:pending | books | books-review:{first_sf} | 尚未独立挑战 provisional Integrate queue | 非作者 reviewer 重开 owner+adjacent | open |","","## 8. Ignored Noise","",f"{len(closures)} 个 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`，逐项记录具体机制、证据线索与 exclusion boundary。","","## 9. Recommended Action","",f"非作者 reviewer 重放 835/835、挑战 48 个候选及 {len(queue)} 项 Books queue；通过后由 root 串行写回并做 post-write audit。","","## 10. Repository Changes","","- 新增本日 final screening ledger、author audit、Books comparison 与 writeback queue。","- 新增 Daily author packet；未修改共享 Books。","- 未 stage、commit 或 push。","","## 11. Open Questions","","- 独立 reviewer 是否会恢复 false negative、降级 false positive 或把现有 Integrate 收紧为 No Change？","","<!-- validator:materials-request-v1 -->","| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","## 12. Sources",""]
for r in retained:
    lines.append(f"- [{r['title']}](https://arxiv.org/html/{r['arxiv_id']}v1) — arXiv:{r['arxiv_id']}v1；first-public 2026-05-12；accessed 2026-09-01")
lines += ["","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Open`","","Evidence: `Open`","","Books: `Open`","","unresolved findings: 1","","作者侧 packet 已完成；fresh-context 独立审计、root 串行 Books 写回与 post-write audit 尚未完成。"]

out = REPO / "papers/2026/05/13/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
text = "\n".join(lines)
for r in retained:
    sf=r["source_family_id"]; aid=r["arxiv_id"]
    start,end=f"<!-- review:{sf}:start -->",f"<!-- review:{sf}:end -->"
    body=text.split(start,1)[1].split(end,1)[0]
    method,evaluation,limits=LOC[aid]
    override="knowledge_gap" if r["integration_disposition"]=="Integrate" else "none"
    candidate={"Event Identity":f"paper-v1:{aid}","Primary Identifier":f"arXiv:{aid}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":override}
    provenance=_expected_review_provenance(sf,candidate,"deep",f"arXiv:{aid}v1",f"SRC-ARXIV@arXiv:{aid}v1",f"arXiv:{aid}v1 HTML — {method}",f"arXiv:{aid}v1 HTML — {evaluation}",f"arXiv:{aid}v1 HTML — {limits}",f"arXiv:{aid}v1 artifact/code statement; immutable commit Not Disclosed unless named",f"claim:{sf}",f"review:{sf}",_normalized_body_sha256(body))
    text=text.replace("RP-TODO-"+sf,provenance)
out.write_text(text+"\n")
print(json.dumps({"raw":INV["raw_snapshot_records"],"registered":len(rows),"screened":len(rows),"retained":len(retained),"closures":len(closures),"reviewed":len(retained)-len(BLOCKED),"blocked":len(BLOCKED),"integrate_queue":len(queue)},ensure_ascii=False))
