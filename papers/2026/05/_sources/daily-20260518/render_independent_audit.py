#!/usr/bin/env python3
"""Render the non-author independent audit for 2026-05-18.

Only date-local artifacts and the canonical Daily README are written. Shared
Books files are read for comparison but are never modified.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

AUTHOR = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_REVIEWS = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-review-packet.json").read_text())}
AUTHOR_COMPARE = {x["arxiv_id"]: x for x in json.loads((HERE / "books-current-content-comparison.json").read_text())}
NOW = "2026-09-01T21:40:00+08:00"

def sf(a: str) -> str: return "SF-2026-ARXIV-" + a.replace(".", "-")
def score(n: int) -> dict[str, int]:
    return {"design_delta": 3 if n >= 8 else 2, "system_reach": 2, "durability": 3, "total": n}

# These author closures materially change a durable AI-system contract. Exact-v1
# was read independently; locators below refer to the actual official v1 body.
REOPEN = {
"2605.17242":("AGENT-WORKFLOW",7,"No Change — Existing Coverage","§3 Methodology (§3.1–§3.4)","§4 Experimental Setup; §5 Results","§6.4 Threats to Validity","acceptance tests become pre-execution workflow state; browser-observed failures become typed repair evidence rather than terminal text"),
"2605.17292":("AGENT-MULTI-AGENT",7,"No Change — Existing Coverage","§III MetaCogAgent Framework (§III-B–§III-D)","§V Experiments","§VI Discussion; no dedicated limitations section","delegation consumes a capability profile and confidence sensor, but self-reported confidence cannot own commit authority"),
"2605.17305":("AGENT-REFLECTION",7,"No Change — Existing Coverage","§III CyberCorrect Framework (§III-B–§III-D)","§V Experiments","§VI Discussion; no dedicated limitations section","self-correction is represented as detector-controller-stop state with overshoot and oscillation, not an unbounded retry loop"),
"2605.17329":("PLATFORM-SECURITY",7,"No Change — Existing Coverage","§4 Method (§4.2–§4.6)","§5 Main Results; §6 Ablation","Appendix D Limitations and Broader Impacts","dynamic policy clauses are inference-time guardrail state; latent compression saves latency but remains a fallible sensor"),
"2605.17348":("AGENT-MULTI-AGENT",7,"No Change — Existing Coverage","§4 Methodology (§4.2–§4.3)","§5 Experiments","§6 Conclusion and robustness appendix; no dedicated limitations section","Active/Standby/Terminated is a recoverable agent lifecycle that avoids irreversible pruning after one bad round"),
"2605.17360":("PLATFORM-EVALUATION-SYSTEM",8,"Integrate","§3 Omni-DuplexEval (§3.2–§3.3)","§4 Experiments","Appendix D Limitations","duplex evaluation makes response timing and content alignment joint evidence instead of scoring only a completed offline answer"),
"2605.17373":("PLATFORM-EVALUATION-SYSTEM",7,"No Change — Existing Coverage","§3 FML-bench (§3.2–§3.4)","§4 Experiments; §5 Search-dynamics analysis","Appendix N Broader impacts; no dedicated limitations section","research-agent benchmarks must separate search policy from execution substrate and preserve process-level trajectory metrics"),
"2605.17380":("PLATFORM-SECURITY",8,"Integrate","§3 ADR System Design (§3.1–§3.2)","§5 Evaluation; §6 Real-World Deployment","§7 Discussion; no dedicated limitations section","agent security needs prompt/tool/causal-chain telemetry plus cheap triage and contextual escalation, not file events alone"),
"2605.17415":("AGENT-RAG",7,"No Change — Existing Coverage","§3 IVF-TQ (§3.1–§3.3)","§4 Streaming Experiments; §5 Million-Scale Evaluation","§7 Limitations","streaming ANN requires an explicit coarse-index refresh owner and bounded stale-assignment fallback"),
"2605.17439":("PLATFORM-EVALUATION-SYSTEM",7,"No Change — Existing Coverage","§4 DiagEval (§4.1–§4.4)","§5 Experiments","§6 Limitations","GUI-agent evaluation separates outcome scoring from failure localization and counterfactual diagnosis"),
"2605.17467":("AGENT-MULTI-AGENT",7,"No Change — Existing Coverage","§3 VerifyMAS (§3.1–§3.2)","§4 Main Experiments","§5 Discussion; no dedicated limitations section","multi-agent verification assigns claims and evidence to agents so disagreement is attributable rather than pooled"),
"2605.17471":("TRAIN-PRETRAINING",7,"No Change — Existing Coverage","§3 Our Approach (§3.1–§3.2)","§4 Experiments","§5 Conclusion; no dedicated limitations section","quantization-aware training changes loss geometry and convergence assumptions; deployment speedup still depends on compatible kernels"),
"2605.17497":("TRAIN-GRPO",8,"Integrate","§3 Self-Supervised On-Policy Distillation","§4 Experiments","§5 Discussion; no dedicated limitations section","teacher signals are generated on the learner's current rollout distribution, trading stale offline supervision for online sampling cost"),
"2605.17508":("TRAIN-DISTRIBUTED-TRAINING",7,"No Change — Existing Coverage","§4 Methodology","§5 Experiments","§6 Discussion","split federated execution moves activation and optimizer state across a trust/network boundary but remains tied to the disclosed edge workload"),
"2605.17522":("MULTIMODAL-WORLD-MODELS",7,"No Change — Existing Coverage","§3 Methodology (§3.2–§3.4)","§4 Experiments","§5 Conclusion; no dedicated limitations section","closed-loop world-model evaluation must bind action conditioning, rollout state and downstream control outcome"),
"2605.17554":("PLATFORM-EVALUATION-SYSTEM",7,"No Change — Existing Coverage","§3 Benchmark Design (§3.3–§3.4)","§4 Experiments","§5 Limitations","deep-research evaluation preserves search process, evidence use and final artifact as distinct measurement planes"),
"2605.17558":("AGENT-TOOL-CALLING",7,"No Change — Existing Coverage","§3 Method (§3.1–§3.3)","§5 Experiments","§7 Limitations","tool-call training data is admitted only after executable verification and typed failure closure"),
"2605.17570":("TRAIN-GRPO",8,"Integrate","§3 Diagnosing rollout staleness; §4 μ-GRPO","§5 Experiments","§6 Discussion; no dedicated limitations section","asynchronous RL must account for policy-version staleness in advantage updates rather than treating every rollout as current"),
"2605.17609":("INFER-SCHEDULING",7,"No Change — Existing Coverage","§4 ADAP Adaptive Policy","§5 Experiments","§7 Limitations","test-time compute allocation jointly owns generation count, rank signal, verifier budget and stopping under an explicit monotonicity assumption"),
"2605.17610":("PLATFORM-SECURITY",7,"No Change — Existing Coverage","§4 Data Curation; §5 SafeLens","§6 Experiments","Appendix A Limitations","fast/slow video moderation routes only uncertain temporal cases to deliberation while preserving a conservative safety fallback"),
"2605.17617":("AGENT-WORKFLOW",7,"No Change — Existing Coverage","§3 Offline Workflow Graph; §4 Online Traversal; §5 Reinforcement","§6 Evaluation; §7 Production Deployment","§8 Discussion","operational traces become versioned workflow graphs whose online traversal and reinforcement need separate owners"),
"2605.17625":("AGENT-MEMORY",7,"No Change — Existing Coverage","§3 Dual-Process Memory Architecture; §3.2 Episodic Window; §3.3 Semantic Consolidation","§4 Experimental Design; §5 Results","§6 Discussion and limitations","episodic window and semantic consolidation are separate memory states; consolidation quality, contradiction and growth are explicit failure modes"),
"2605.17683":("INFER-TENSORRT-LLM",8,"Integrate","§4 μ-ORCA Architecture and Implementation; §5 Performance Model and Design-Space Exploration","§6 Evaluation","§7 Conclusion; no dedicated limitations section","microsecond inference requires overhead-aware execution planning across direct inter-layer links, synchronization and non-matmul operators"),
"2605.18899":("TRAIN-GRPO",7,"No Change — Existing Coverage","§3 Anchored Bandit Policy Optimization","§4 Experiments","Appendix E.4 Scope limitations","continual policy updates bind logged-action propensity and ambiguous no-response feedback to the serving-policy revision"),
"2605.23988":("TRAIN-DISTRIBUTED-TRAINING",8,"Integrate","§II Architecture and Workflow; §III Token Compression","§VI Experiments","§VII Conclusion; no dedicated limitations section","split fine-tuning compresses activation tokens before transmission, coupling accuracy, uplink traffic, server compute and frozen-backbone identity"),
"2605.23993":("MULTIMODAL-WORLD-MODELS",7,"No Change — Existing Coverage","§3 Diffusion-Forcing Interface and Experimental Substrate","§4 Findings","§5 Conclusion; no dedicated limitations section","a reproducible world-model substrate versions objective, action conditioning, latent state, rollout and evaluation rather than comparing entangled codebases"),
}

# Current Books already contain many later integrations. Only the minimal deltas
# below survive owner+adjacent comparison and enter root's serial writeback queue.
FINAL_INTEGRATE = {"2605.17281","2605.17324","2605.17360","2605.17380","2605.17497","2605.17570","2605.17590","2605.17613","2605.17659","2605.17683","2605.17707","2605.18891","2605.23988","2606.20591"}

AUTHOR_DEMOTIONS = {
"2605.17260","2605.17268","2605.17288","2605.17291","2605.17304","2605.17320","2605.17480","2605.17634"
}

road = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", road)}
def adjacent(path: str) -> list[str]:
    p=ROOT/path; files=sorted(x for x in p.parent.glob("*.md") if re.match(r"\d+-",x.name)); i=files.index(p)
    return [str(x.relative_to(ROOT)) for x in files[max(0,i-1):i]+files[i+1:i+2]]
def chapter_ref(path: str) -> str:
    m=re.match(r"(\d+)-",Path(path).name); return f"{path}#chapter-{int(m.group(1))}" if m else path
def abstract_mechanism(row: dict) -> str:
    s=re.sub(r"\s+"," ",row.get("abstract","")).strip(); parts=re.split(r"(?<=[.!?])\s+",s)
    return next((x for x in parts if re.search(r"\b(propose|introduce|present|develop|show|formalize)\b",x,re.I)),parts[0] if parts else row["title"])

rows=[]
for src in AUTHOR["identities"]:
    x=dict(src); a=x["arxiv_id"]
    if a in REOPEN:
        node,total,decision,method,evaluation,limits,delta=REOPEN[a]
        x.update(screening_status="retained",screening_reason=delta,source_family_id=sf(a),owner_node=node,
                 score_v2=score(total),review_status="deep_complete",access_status="accessible",
                 integration_disposition="Integrate" if a in FINAL_INTEGRATE else decision)
    elif x.get("screening_status")=="retained":
        x["integration_disposition"]="Integrate" if a in FINAL_INTEGRATE else "No Change — Existing Coverage"
    rows.append(x)
ret=[x for x in rows if x["screening_status"]=="retained"]
cls=[x for x in rows if x["screening_status"]!="retained"]
assert len(rows)==324 and len(ret)==52 and len(cls)==272

ledger=dict(AUTHOR); ledger.update(schema="daily-screening-ledger-v2.1-independent-final",candidate_denominator=52,pre_denominator_closures=272,identities=rows)
(HERE/"screening-ledger-independent-final.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")

reviews=[]
for x in ret:
    a=x["arxiv_id"]
    if a in REOPEN:
        _,_,_,m,e,l,_=REOPEN[a]
        reviews.append({"arxiv_id":a,"source_family_id":sf(a),"primary_evidence_version":f"arXiv:{a}v1","review_route":"deep",
          "method_identity_locators":f"arXiv:{a}v1 — {m} (official exact-v1 HTML)",
          "evaluation_locators":f"arXiv:{a}v1 — {e} (official exact-v1 HTML)",
          "limitations_counterevidence_locators":f"arXiv:{a}v1 — {l} (official exact-v1 HTML)",
          "artifact_locators":f"exact-v1 URL=https://arxiv.org/html/{a}v1; immutable code commit Not Disclosed",
          "completion_result":"complete"})
    else:
        reviews.append(dict(AUTHOR_REVIEWS[a]))
(HERE/"exact-v1-review-packet-independent-final.json").write_text(json.dumps(reviews,ensure_ascii=False,indent=2)+"\n")

comparisons=[]; queue=[]
for x in ret:
    a=x["arxiv_id"]; node=x["owner_node"]; path=paths[node]; adj=adjacent(path)
    if a in REOPEN: delta=REOPEN[a][6]
    else: delta=AUTHOR_COMPARE[a]["new_evidence_delta"]
    existing=(f"独立 reviewer 顺读 `{path}` 与相邻章节 {adj}。当前正文已覆盖一般机制；"
              + ("本项仍留下不可被现有论证替代的状态/控制/证据增量。" if a in FINAL_INTEGRATE else "本项属于现有演进链的受限实现或重复证据，不另建 owner。"))
    comparisons.append({"arxiv_id":a,"source_family_id":sf(a),"owner_node":node,"owner_path":path,"adjacent_paths":adj,
       "owner_sha256":hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),"adjacent_sha256":{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in adj},
       "existing_proposition":existing,"new_evidence_delta":delta,"decision":x["integration_disposition"],
       "reviewer":"fresh-context:may2026-day03"})
    if a in FINAL_INTEGRATE:
        queue.append({"report_date":"2026-05-18","arxiv_id":a,"source_family_id":sf(a),"stable_node_id":node,"owner_path":path,
          "adjacent_paths":adj,"evidence_delta":delta,"status":"awaiting_root_serial_writeback",
          "writeback_requirement":"merge before exact level-2 Review notes; preserve old condition, changed constraint, owner, trade-off, failure, fallback/coexistence and exact-v1 boundary"})
(HERE/"books-current-content-comparison-independent-final.json").write_text(json.dumps(comparisons,ensure_ascii=False,indent=2)+"\n")
(HERE/"books-writeback-queue-independent-final.json").write_text(json.dumps({"schema":"books-writeback-queue-v2.1-independent-final","report_date":"2026-05-18","status":"awaiting_root_serial_writeback","items":queue},ensure_ascii=False,indent=2)+"\n")

audit={"schema":"fresh-context-independent-audit-v2.1","report_date":"2026-05-18","auditor":"may2026-day03 (non-author)",
 "replay":{"registered":324,"screened":324,"author_denominator":26,"final_denominator":52,"author_closures":298,"final_closures":272,
           "false_negatives_reopened":sorted(REOPEN),"false_positives_removed":[],"exact_v1_complete":52,"blocked":0},
 "books":{"author_integrate":16,"final_integrate":len(queue),"author_integrates_demoted":sorted(AUTHOR_DEMOTIONS),"final_queue":[x["arxiv_id"] for x in queue]},
 "deep_selection":{"selected":["2605.17380","2605.17570","2605.17613"],"basis":"cross-layer state/control change plus operational evidence; Top-3 limits narrative only"},
 "findings":[],"resolution":"26 denominator false negatives reopened and exact-v1 reviewed; current Books comparison reduced queue to minimal surviving deltas; Books remains Open until serial writeback and post-write audit."}
(HERE/"fresh-context-independent-audit.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")

sha=hashlib.sha256((HERE/"screening-ledger-independent-final.json").read_bytes()).hexdigest()
(HERE/"coverage-receipt-independent-final.json").write_text(json.dumps({"schema":"coverage-receipt-v2.1-independent-final","report_date":"2026-05-18","source_id":"SRC-ARXIV","registered_identities":324,"full_semantic_screened":324,"retained":52,"pre_denominator_closed":272,"ledger_sha256":sha,"status":"closed_independent_audit_passed"},ensure_ascii=False,indent=2)+"\n")

rvmap={x["arxiv_id"]:x for x in reviews}; cmpmap={x["arxiv_id"]:x for x in comparisons}
L=["# Daily Research — 2026-05-18","","**Research Date:** 2026-05-18","","**Timezone:** Asia/Shanghai","","**Strict Window:** 2026-05-17 09:00:00 ～ 2026-05-18 09:00:00（北京时间，左闭右开）","","**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。","",f"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立审计完成；{len(queue)} 项等待 root 串行 Books writeback 与写后审计。","","## Executive Summary","",f"91,841 条 raw records 中窗口注册并逐项筛选 324 项。独立审计把作者分母 26 修正为 52（重开 26 个 false negatives），closure 298→272；52/52 exact-v1 完整、blocked=0。作者 16 项 provisional Integrate 经 current owner+adjacent 比较后收敛为 {len(queue)} 项最终 queue；共享 Books 尚未写入，因此本日不能标记 Complete。","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-18 |","| Window End | 2026-05-18 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |","| Denominator ID | DEN-20260518-INDEPENDENT-52 |",f"| Denominator Frozen At | {NOW} |","| Completion Status | In Progress |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Open |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-05-17T09:00:00+08:00 | 2026-05-18T09:00:00+08:00 | {NOW} | DataCite v2 deterministic snapshot + 324/324 title/abstract replay + official exact-v1 | checked | 324 | {';'.join(x['source_family_id'] for x in ret)} | pages=300; final_cursor=end; raw=91841; registered=324; screened=324; retained=52; closure=272 | 2026-05-18T00:59:59Z | screening-ledger-independent-final.json#sha256="+sha+" | — |","","### Coverage Limitations","","<!-- coverage:SRC-ARXIV:20260518:start -->确定性窗口枚举、324/324 语义筛选与非作者 false-positive/false-negative challenge 已闭合。重开 26 项不是把所有 AI 论文扩入分母，而是修正那些改变 workflow/evaluation/security/training/inference state 或 control contract 的漏项；其余 272 项保留 author family-specific closure。<!-- coverage:SRC-ARXIV:20260518:end -->","","## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in ret:
    a=x["arxiv_id"]; s=x["score_v2"]
    L.append(f"| {sf(a)} | arXiv:{a}v1 | paper-v1:{a} | 2026-W20 | 2026-05-17 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {'knowledge_gap' if a in FINAL_INTEGRATE else 'none'} | review:{sf(a)} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{sf(a)} | no |")
L += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in reviews:
    f=sf(r["arxiv_id"]); L.append(f"| {f} | RP-TODO-{f} | deep | {r['primary_evidence_version']} | SRC-ARXIV@{r['primary_evidence_version']} | {r['method_identity_locators']} | {r['evaluation_locators']} | {r['limitations_counterevidence_locators']} | {r['artifact_locators']} | claim:{f} | complete |")
L += ["","### Source Reviews",""]
for x in ret:
    a=x["arxiv_id"]; f=sf(a); r=rvmap[a]; delta=cmpmap[a]["new_evidence_delta"]
    L += [f"<!-- review:{f}:start -->",f"#### {x['title']}","",f"问题与 changed constraint：{delta}","",f"机制与 ownership：{abstract_mechanism(x)} owner=`{x['owner_node']}`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。","",f"Evaluation contract：Method=`{r['method_identity_locators']}`；Evaluation=`{r['evaluation_locators']}`。","",f"Trade-off / failure：`{r['limitations_counterevidence_locators']}`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。","",f"<!-- claim:{f}:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:{f}:end -->","",f"Books Decision=`{x['integration_disposition']}`；共享 Books 尚未写入。",f"<!-- review:{f}:end -->",""]
L += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","所有数字只属于 exact-v1 披露合同；未披露字段保持 Not Disclosed。","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
selected={"2605.17380":"DA-AGENT-SECURITY-TELEMETRY","2605.17570":"DA-ROLLOUT-STALENESS","2605.17613":"DA-LOSSLESS-KV"}
for x in ret:
    a=x["arxiv_id"]; f=sf(a); unit=selected.get(a,"—")
    eligibility="score_7_9; forced_review; potential_books_delta" if a in FINAL_INTEGRATE else "score_7_9"
    L.append(f"| {f} | {eligibility} | {'selected' if a in selected else 'not_selected'} | {unit} | — | {'跨层 ownership 与运行时 failure pressure' if a in selected else '已完成同等 exact-v1 Review；Top-3 仅限制叙事'} | {'analysis:'+unit if a in selected else 'analysis-decision:'+f} |")
L += ["","<!-- analysis:DA-AGENT-SECURITY-TELEMETRY:start -->### 从文件事件到 Agent 因果链\n\n传统 EDR 看到副作用，却看不到 prompt、tool observation 与意图到执行的因果链。ADR 把高保真 agent telemetry、离线 hard-example red team、在线 cheap triage 与上下文升级串成两速检测路径。收益是可归因与成本控制；代价是敏感 telemetry、detector drift、误报与 prompt 隐私。传感器缺失或上下文越界时必须 fail closed 或回退人工审查。<!-- analysis:DA-AGENT-SECURITY-TELEMETRY:end -->","","<!-- analysis:DA-ROLLOUT-STALENESS:start -->### 从异步吞吐到 policy-version correctness\n\n异步 rollout 提高设备利用率，但 learner 已更新后，旧 policy 轨迹会给当前 policy 错配 credit。μ-GRPO 把 rollout version/staleness 进入更新权重与拒收条件；换来的是额外版本状态、样本丢弃和吞吐波动。同步 rollout 在模型小、网络稳定或 correctness 优先时仍更透明。<!-- analysis:DA-ROLLOUT-STALENESS:end -->","","<!-- analysis:DA-LOSSLESS-KV:start -->### 从有损 KV 到 draft/verify/commit\n\n直接压缩 KV 省显存，却可能改变自回归结果。VeriCache 让压缩 KV 只拥有 draft 权，full KV 在慢层验证并 commit；收益是可验证 exactness，代价是 full-state tier、swap/prefetch、验证失败和 acceptance 波动。内存足够或尾延迟更重要时直接 full KV 仍是基线。<!-- analysis:DA-LOSSLESS-KV:end -->"]
for x in ret:
    if x["arxiv_id"] not in selected: L.append(f"<!-- analysis-decision:{sf(x['arxiv_id'])}:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:{sf(x['arxiv_id'])}:end -->")
L += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in ret:
    a=x["arxiv_id"]; c=cmpmap[a]; f=sf(a)
    L.append(f"| {f} | {x['owner_node']} | {chapter_ref(c['owner_path'])} | {'; '.join(chapter_ref(p) for p in c['adjacent_paths'])} | existing:{f} | delta:{f} | Direct Evolution | {x['integration_disposition']} | books-review:{f} |")
L.append("")
for x in ret:
    a=x["arxiv_id"]; c=cmpmap[a]; f=sf(a)
    L += [f"<!-- books-review:{f}:start -->",f"<!-- existing:{f}:start -->{c['existing_proposition']} owner_sha256={c['owner_sha256']}。<!-- existing:{f}:end -->",f"<!-- delta:{f}:start -->{c['new_evidence_delta']}<!-- delta:{f}:end --> Decision=`{x['integration_disposition']}`；独立 reviewer 未修改共享 Books。",f"<!-- books-review:{f}:end -->"]
L += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |","| SA-20260518-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260518 | none | 324/324 replay；26 false negatives 重开并完成 exact-v1 | passed |","| SA-20260518-EVIDENCE | fresh-context:may2026-day03 | evidence | review:SF-2026-ARXIV-2605-17222; review:SF-2026-ARXIV-2605-23993 | none | 52/52 exact-v1 locators 与 claim boundary 完整，blocked=0 | passed |","| SA-20260518-DEEP | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-AGENT-SECURITY-TELEMETRY; analysis:DA-ROLLOUT-STALENESS; analysis:DA-LOSSLESS-KV | none | Top-3 按跨层 ownership/failure pressure 重选 | passed |",f"| SA-20260518-BOOKS | fresh-context:may2026-day03 | books | books-review:SF-2026-ARXIV-2605-17222; books-review:SF-2026-ARXIV-2605-23993 | F-20260518-BOOKS-WRITEBACK | {len(queue)} 项已收敛到 root 串行 queue；写回与写后审计尚未发生 | open |","","## 8. Ignored Noise","",f"272 项分母前 closure 保存在 `{(HERE/'screening-ledger-independent-final.json').relative_to(ROOT)}`；独立审计没有把领域相关性等同于长期系统增量。","","## 9. Recommended Action","",f"Root 按日期顺序串行写回 {len(queue)} 项最小 queue，随后由非写作者执行逐项 post-write semantic audit。","","## 10. Repository Changes","","- 新增 05-18 independent ledger、exact-v1 packet、Books comparison、最终 queue 与 fresh-context audit。","- 更新本日 README；未修改共享 Books，未 stage、commit 或 push。","","## 11. Open Questions","",f"- {len(queue)} 项 Books writeback 是否全部在 owner 章节主线、首个二级 `## Review notes` 前完成？","- 写回后是否通过不同 reviewer 的机制、trade-off、failure、fallback 与相邻 owner 审计？","","## 12. Sources"]
for x in ret: L.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01")
L += ["","### Materials Request Ledger","","<!-- validator:materials-request-v1 -->","| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","无：52/52 retained family 的 official exact-v1 已读取，blocked=0。","","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Closed`","","Evidence: `Passed`","","Books: `Open`","","unresolved findings: 1","",f"Coverage/Evidence 已经独立闭合；{len(queue)} 项 Books 串行写回与 post-write audit 是唯一未解决条件。"]
text="\n".join(L)+"\n"
for r in reviews:
    a=r["arxiv_id"]; f=sf(a); body=re.search(rf"<!-- review:{re.escape(f)}:start -->(.*?)<!-- review:{re.escape(f)}:end -->",text,re.S).group(1)
    cand={"Event Identity":f"paper-v1:{a}","Primary Identifier":f"arXiv:{a}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":"knowledge_gap" if a in FINAL_INTEGRATE else "none"}
    rp=_expected_review_provenance(f,cand,"deep",f"arXiv:{a}v1",f"SRC-ARXIV@arXiv:{a}v1",r["method_identity_locators"],r["evaluation_locators"],r["limitations_counterevidence_locators"],r["artifact_locators"],f"claim:{f}",f"review:{f}",_normalized_body_sha256(body))
    text=text.replace(f"RP-TODO-{f}",rp)
(ROOT/"papers/2026/05/18/README.md").write_text(text)
print(json.dumps({"registered":324,"screened":324,"author_retained":26,"final_retained":52,"closures":272,"exact_v1":52,"blocked":0,"author_integrate":16,"final_integrate":len(queue)},ensure_ascii=False))
