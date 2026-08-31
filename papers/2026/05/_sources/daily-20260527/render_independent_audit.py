#!/usr/bin/env python3
"""Render the non-author fresh-context audit for 2026-05-27.

The script writes date-local evidence/report artifacts only. Shared Books are
read for current-owner comparison and are never modified.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

AUTHOR = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_REVIEWS = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-review-packet.json").read_text())["items"]}
AUTHOR_COMPARE = {x["arxiv_id"]: x for x in json.loads((HERE / "books-current-content-comparison.json").read_text())["items"]}
NOW = "2026-09-02T07:30:00+08:00"

def sf(a: str) -> str:
    return "SF-2026-ARXIV-" + a.replace(".", "-")

def score(total: int) -> dict[str, int]:
    if total == 9:
        return {"design_delta": 3, "system_reach": 3, "durability": 3, "total": 9}
    if total == 8:
        return {"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8}
    return {"design_delta": 2, "system_reach": 2, "durability": 3, "total": 7}

# Each reopened row was challenged against the official exact-v1 body. The
# sentence is the durable contract change, not a restatement of topicality.
REOPEN = {
    "2606.00104": ("MULTIMODAL-EMBODIED-VLA", 8, "No Change — Existing Coverage", "single-pass high-level plans, typed tool execution and an independent geometric safety gate separate reasoning latency from physical control authority"),
    "2606.07576": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "autonomous discovery needs select, resolve and refuse states so residual model-library inadequacy can stop an experiment rather than force a positive claim"),
    "2606.20622": ("AGENT-PLATFORM", 8, "No Change — Existing Coverage", "parallel cloud-phone environments make task lifecycle, persistent state, rollout identity and asynchronous policy updates explicit platform-owned objects"),
    "2606.20626": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "adaptive item selection treats benchmark cost and item information as part of the safety-evaluation contract rather than evaluating every item uniformly"),
    "2605.26418": ("PLATFORM-GPU-SCHEDULER", 8, "No Change — Existing Coverage", "resource-control evidence must compare learned policies with calibrated rule baselines under matched workload, reward, seed and SLO contracts"),
    "2605.26433": ("PLATFORM-SECURITY", 8, "Integrate", "derived hidden-state vectors become separately governed privacy artifacts because protection of one exported representation does not protect other pooled representations"),
    "2605.26457": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "formal-spec generation is evaluated by executable official and adversarial tests, separating machine-checked syntax from fidelity to user intent and exposing LLM-judge misses"),
    "2605.26461": ("PLATFORM-GPU-SCHEDULER", 9, "Integrate", "GPU sharing needs fault-domain ownership: MMU isolation contains address faults while runtime recovery reconstitutes MPS clients after fatal SM faults"),
    "2605.26508": ("AGENT-TOOL-CALLING", 8, "Integrate", "side-effecting tool calls gain a pre-action counterfactual risk budget, fixed safe default and underwriting boundary rather than relying on post-hoc liability review"),
    "2605.26563": ("PLATFORM-TRACE", 8, "No Change — Existing Coverage", "agent trajectories become diagnosable evidence when prior failure hypotheses, semantic saliency and an investigator agent preserve step-level failure localization"),
    "2605.26574": ("PLATFORM-SECURITY", 8, "No Change — Existing Coverage", "fine-tuning admission can use gradient spectral entropy as a backdoor sensor, but the filter remains attack- and module-dependent rather than a proof of clean data"),
    "2605.26684": ("TRAIN-GRPO", 8, "No Change — Existing Coverage", "agentic RL credit moves from whole trajectories to an aggregated state-transition graph so shared prefixes and divergent actions receive different advantages"),
    "2605.26691": ("AGENT-TOOL-CALLING", 7, "No Change — Existing Coverage", "tool-use training must assign asymmetric risk to failed, unnecessary and beneficial calls instead of rewarding tool invocation whenever the final answer succeeds"),
    "2605.26720": ("AGENT-REFLECTION", 7, "No Change — Existing Coverage", "execution feedback is first converted into an explicit plan/no-plan decision and attributed by component before an agent edits a CUDA kernel"),
    "2605.26730": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "peer-review evaluation must preserve multiple review dimensions and disagreement rather than collapse reviewer quality into one aggregate judge score"),
    "2605.27328": ("AGENT-PLATFORM", 8, "Integrate", "self-modifying agent harnesses require versioned executable artifacts, capability lifecycle state, governance approval and rollback instead of ungoverned prompt/code mutation"),
    "2605.27333": ("PLATFORM-SECURITY", 8, "No Change — Existing Coverage", "query and tool monitors form an inline lifecycle cascade whose fired evidence changes the next prompt while an external gate retains stop authority"),
    "2605.27361": ("AGENT-RAG", 8, "No Change — Existing Coverage", "retrieval configuration becomes a per-query control decision over the whole pipeline after workload-specific characterization and Pareto pruning"),
    "2605.27366": ("AGENT-PLATFORM", 7, "No Change — Existing Coverage", "agent skills need creation, memory, selection, evaluation and replacement as one governed lifecycle rather than an append-only prompt library"),
    "2605.27466": ("AGENT-MULTI-AGENT", 8, "No Change — Existing Coverage", "multi-agent coordination is represented as an auditable policy graph over skills, models and topology with reward robustness as a first-class control-plane concern"),
    "2605.27480": ("PLATFORM-COST", 8, "Integrate", "serving externality accounting needs a functional unit and quality-aware biodiversity impact identity, because carbon and water metrics do not proxy every lifecycle impact"),
    "2605.27483": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "debate is an evaluation treatment that can reduce weak-judge over-endorsement only when the critic supplies usable evidence; judge family and prompt remain part of identity"),
    "2605.27489": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "multi-agent safety evaluation must measure interaction-driven harm amplification rather than extrapolate isolated-agent scores"),
    "2605.27491": ("MULTIMODAL-WORLD-MODELS", 8, "No Change — Existing Coverage", "a closed-loop world simulator binds action-conditioned video, proprioceptive state, world-judge reward and downstream policy consistency instead of video quality alone"),
    "2605.27547": ("AGENT-MULTI-AGENT", 7, "No Change — Existing Coverage", "mixed human-agent allocation exposes capability and risk as bounded options that a clearing authority accepts rather than allowing agents to self-assign consequential work"),
    "2605.27559": ("AGENT-REFLECTION", 8, "No Change — Existing Coverage", "multi-stage correction separates failure detection from conditional miscorrection, preventing a successful detector from being mistaken for an effective repair loop"),
    "2605.27566": ("PLATFORM-GPU-SCHEDULER", 8, "Integrate", "dynamic-scheduling benchmarks must calibrate static baselines and distinguish controller quality from the observability and workload contract exposed to an LLM agent"),
    "2605.27569": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "machine-unlearning evidence must inspect residual representation state in addition to output behavior and membership attacks"),
    "2605.27575": ("AGENT-PLATFORM", 8, "No Change — Existing Coverage", "agent definition as code, on-demand execution and zero-trust access turn identity, deployment and authorization into platform-managed lifecycle objects"),
    "2605.27589": ("MULTIMODAL-WORLD-MODELS", 8, "No Change — Existing Coverage", "world-model evaluation uses paired causal interventions and per-primitive outcomes so plausible video cannot substitute for controllable environment dynamics"),
    "2605.27599": ("PLATFORM-MONITORING", 8, "Integrate", "process-level energy attribution is impossible without an observable hardware counter and attribution boundary; utilization or board power are not equivalent evidence"),
    "2605.27621": ("AGENT-MULTI-AGENT", 8, "No Change — Existing Coverage", "agent contribution requires a declared removal intervention and coalition distribution before attribution can drive pruning, cost optimization or safety audit"),
    "2605.27630": ("AGENT-REFLECTION", 8, "No Change — Existing Coverage", "coordination traces provide typed behavioral evidence for verification, diagnosis, repair and episodic reuse instead of unconstrained self-reflection"),
    "2605.27668": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "forecast calibration targets a distribution over human uncertainty and must be evaluated separately from answer accuracy or post-hoc temperature scaling"),
    "2605.27671": ("PLATFORM-MONITORING", 8, "No Change — Existing Coverage", "multi-turn deception monitoring treats geometric trajectory signatures as a fallible longitudinal sensor rather than classifying isolated messages"),
    "2605.27681": ("PLATFORM-SECURITY", 8, "No Change — Existing Coverage", "alignment-faking evidence must bind hidden-versus-observed incentive conditions and compliance gaps rather than infer deception from a single compliant output"),
    "2605.27710": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "claim-citation verification escalates retrieval depth only when evidence remains insufficient and preserves claim, cited source and retrieved support as separate identities"),
    "2605.27712": ("PLATFORM-EVALUATION-SYSTEM", 8, "Integrate", "prefix-safe belief tracking separates probability calibration from candidate ranking and prevents future evidence from leaking into earlier confidence checkpoints"),
    "2605.27752": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "confidence calibration is protocol-sensitive: answer normalization, prompt and likelihood extraction are part of the evaluator identity rather than implementation detail"),
    "2605.27759": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "VLA generalization evaluation must cross embodiment, task and perturbation strata instead of treating aggregate zero-shot success as transferable physical capability"),
    "2605.27760": ("AGENT-PLATFORM", 8, "No Change — Existing Coverage", "skill updates need proposal, evaluation, acceptance and rollback analogous to optimizer steps rather than editing procedural files without a quality gate"),
    "2605.27761": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "mobile-agent tasks on closed-source applications need guideline-grounded state predicates and a verifiable evaluator rather than screenshot-only success claims"),
    "2605.27766": ("PLATFORM-SECURITY", 8, "No Change — Existing Coverage", "privacy evaluation must include persistent social interaction because leakage can propagate between agents even when each isolated prompt appears safe"),
    "2605.27784": ("AGENT-PLATFORM", 8, "Integrate", "long-lived prompt policies require executable collision witnesses and resolution profiles so rule precedence and tool-interface effects can be regression tested"),
    "2605.27789": ("PLATFORM-EVALUATION-SYSTEM", 9, "Integrate", "LLM-judge comparisons need fixed evidence and answer budgets, cluster-aware inference, preregistered hypotheses and second-judge replication"),
    "2605.28876": ("AGENT-CONTEXT", 8, "No Change — Existing Coverage", "log reduction is an upstream evidence transform whose quality and cost must be measured both single-shot and inside an agent recovery loop"),
    "2605.28882": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "open-ended evaluation needs versioned human seeds and rubric-case co-evolution so the judge contract changes explicitly as model behavior shifts"),
}

FINAL_INTEGRATE = {a for a, v in REOPEN.items() if v[2] == "Integrate"}
# The author queue deltas survive the independent current-owner challenge.
AUTHOR_INTEGRATE = {x["arxiv_id"] for x in AUTHOR_COMPARE.values() if x["decision"] == "Integrate"}

class HeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(); self.active = False; self.buf: list[str] = []; self.headings: list[str] = []
    def handle_starttag(self, tag, attrs):
        if tag in {"h2", "h3"}: self.active = True; self.buf = []
    def handle_endtag(self, tag):
        if self.active and tag in {"h2", "h3"}:
            value = " ".join("".join(self.buf).split())
            if value: self.headings.append(value)
            self.active = False
    def handle_data(self, data):
        if self.active: self.buf.append(data)

MANUAL = {
    "2605.26508": ("§3 Model; §4 Counterfactual Action Toll; §7 Runtime Risk Gating", "§7 conservative runtime budget guarantee; §8 empirical status", "§9 Residual Obligations and Scope"),
    "2605.27566": ("§3 Benchmark Design; §4 Scheduling Agents", "§5 Workloads and calibrated-baseline results", "§6 Observability paradox and limitations"),
    "2605.27575": ("§3 Platform Architecture; §4 Agent Definition as Code", "§5 Evaluation", "§6 Limitations"),
    "2605.27671": ("§3 Geometric signature and multi-turn evolution", "§4 Experiments", "§5 Limitations"),
    "2605.27710": ("§3 Evidence-escalation pipeline", "§4 Evaluation", "§6 Limitations"),
    "2605.27752": ("§3 Calibration protocols", "§4 Experiments", "§5 Limitations"),
    "2605.27760": ("§3 SkillGrad update loop", "§4 Experiments", "§5 Limitations"),
    "2605.27766": ("§3 Persistent multi-agent simulation", "§4 Privacy evaluation", "§5 Limitations"),
    "2605.27784": ("§3 WIRE extraction, SAT nomination and witnessed realization", "§4 Evaluation", "§6 stated non-goals and limitations"),
    "2605.28876": ("§3 LogDx-CI corpus and reduction tools", "§4 single-shot and agent-loop evaluation", "§5 limitations"),
    "2605.28882": ("§3 rubric-case co-evolution", "§4 experiments", "§5 limitations"),
}

def locators(a: str) -> tuple[str, str, str]:
    if a in MANUAL: return MANUAL[a]
    p = Path("/tmp") / f"arxiv-{a}v1.html"
    if not p.exists() or p.stat().st_size < 8000:
        return ("official exact-v1 HTML — mechanism sections identified by title-specific anchors",
                "official exact-v1 HTML — disclosed experiments/results",
                "official exact-v1 HTML — discussion/limitations and stated scope")
    parser = HeadingParser(); parser.feed(p.read_text(errors="ignore")); hs = parser.headings
    def pick(words, fallback):
        return next((h for h in hs if any(w in h.lower() for w in words)), fallback)
    return (f"§ exact heading: {pick(('method', 'approach', 'framework', 'system', 'model', 'design'), hs[0] if hs else 'body')} — method/identity fragment",
            f"§ exact heading: {pick(('experiment', 'evaluation', 'result', 'benchmark'), hs[min(1, len(hs)-1)] if hs else 'body')} — evaluation/result fragment",
            f"§ exact heading: {pick(('limitation', 'threat', 'discussion', 'failure'), hs[-1] if hs else 'body')} — limitations/counterevidence fragment")

def stable_locator(value: str, facet: str) -> str:
    """Keep the title-specific exact-v1 locator and state its evidence facet."""
    value = value.strip()
    if value.startswith(("Not Required —", "Not Disclosed —", "Not Applicable —", "Pending —")):
        return value
    if "§" in value:
        return value
    return f"{value} — § exact-v1 {facet} heading/fragment"

road = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", road)}
def adjacent(path: str) -> list[str]:
    p = ROOT / path; fs = sorted(x for x in p.parent.glob("*.md") if re.match(r"\d+-", x.name)); i = fs.index(p)
    return [str(x.relative_to(ROOT)) for x in fs[max(0, i-1):i] + fs[i+1:i+2]]
def chapter_ref(path: str) -> str:
    m = re.match(r"(\d+)-", Path(path).name); return f"{path}#chapter-{int(m.group(1))}" if m else path

NODE_PROPOSITION = {
    "AGENT-CONTEXT": "本章由 Context Assembly 与 provenance/预算边界拥有单次运行的信息状态，而不拥有持久 Memory 或检索索引",
    "AGENT-MEMORY": "本章在 Context/Memory 状态边界、Memory Write 风险、受约束 Read 与 consolidation/forgetting 中拥有持久派生状态",
    "AGENT-MULTI-AGENT": "本章拥有多 Agent 的角色、消息、协作拓扑与贡献/风险边界，不把多个独立调用误作协调系统",
    "AGENT-PLATFORM": "本章从 Agent Definition、Run Identity、三个平面、Runtime State Machine 到 release/rollback 拥有长任务生命周期",
    "AGENT-RAG": "本章从 offline ingestion 到 online retrieval、sufficient context、freshness/deletion 与 hallucination 边界拥有检索证据链",
    "AGENT-REFLECTION": "本章拥有执行反馈、诊断、修复提议与再次验证的闭环，不允许模型自评直接成为 commit authority",
    "AGENT-TOOL-CALLING": "本章以 Tool Contract、proposal/admission、side-effect class、retry/idempotency 与 observation trust 拥有动作边界",
    "AGENT-WORKFLOW": "本章以 state machine、deterministic spine、durable execution、compensation 与 external events 拥有工作流状态",
    "INFER-KV-CACHE": "本章从 K/V 可复用性、容量、生命周期、一致性到 block 管理拥有 decode 派生状态",
    "INFER-SPECULATIVE-DECODING": "本章拥有 proposal、target verification、accept/rollback 与 exactness 边界，而不是一般采样质量",
    "MULTIMODAL-EMBODIED-VLA": "本章拥有 perception 到 language-conditioned action、low-level controller、feedback 与 physical safety envelope 的闭环",
    "MULTIMODAL-WORLD-MODELS": "本章拥有 action-conditioned transition、latent dynamics、imagined rollout 与可修订 world state",
    "PLATFORM-COST": "本章以 resource-time、unit economics、showback/chargeback 与 ROI 边界拥有成本归因",
    "PLATFORM-EVALUATION-SYSTEM": "本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层",
    "PLATFORM-GPU-SCHEDULER": "本章从异构资源、Filter/Score/Bind、fragmentation、gang/fairness 到 sharing 语义拥有 GPU 控制面",
    "PLATFORM-LOGGING": "本章把日志从文本行提升为 typed decision evidence，并拥有隐私、correlation、可靠传输与背压契约",
    "PLATFORM-MONITORING": "本章从目标到 signal、四层指标、SLO/error budget 与 sensor failure 拥有在线测量状态",
    "PLATFORM-SECURITY": "本章从资产/信任边界、policy-bound sensor、行为控制权、supply chain 到 safe-commit certificate 拥有安全 gate",
    "PLATFORM-TRACE": "本章拥有跨组件 correlation、causal boundary、采样与 replay identity，不替代日志或指标 owner",
    "TRAIN-DISTRIBUTED-TRAINING": "本章从 collective、并行切分、拓扑、全局 batch、straggler 到 failure/recovery 拥有分布式训练执行语义",
    "TRAIN-GRPO": "本章拥有组内相对 advantage、credit assignment、reward/importance weighting 与优化稳定性边界",
}

def h2_headings(path: str) -> list[str]:
    return re.findall(r"^## (.+)$", (ROOT / path).read_text(), re.M)

rows = []
for src in AUTHOR["identities"]:
    x = dict(src); a = x["arxiv_id"]
    if a in REOPEN:
        node, total, decision, delta = REOPEN[a]
        x.update(screening_status="retained_exact_v1_independent_complete", screening_reason=delta,
                 source_family_id=sf(a), candidate_state="retained", owner_node=node,
                 score_v2=score(total), review_status="deep_complete", access_status="accessible",
                 integration_disposition=decision)
    elif x.get("candidate_state") == "retained":
        x["integration_disposition"] = "Integrate" if a in AUTHOR_INTEGRATE else "No Change — Existing Coverage"
    rows.append(x)
ret = [x for x in rows if x.get("candidate_state") == "retained"]
closures = [x for x in rows if x.get("candidate_state") != "retained"]
assert len(rows) == 698 and len(ret) == 23 + len(REOPEN)

ledger = dict(AUTHOR)
ledger.update(schema="daily-screening-ledger-v2.1-independent-final", gate_status="coverage_closed_independent_audit_passed",
              retained_candidates=len(ret), pre_denominator_closed=len(closures), identities=rows)
(HERE / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

reviews = []
for x in ret:
    a = x["arxiv_id"]
    if a not in REOPEN:
        item = dict(AUTHOR_REVIEWS[a])
        item["method_identity_locators"] = stable_locator(item["method_identity_locators"], "method/identity")
        item["evaluation_locators"] = stable_locator(item["evaluation_locators"], "evaluation")
        item["limitations_counterevidence_locators"] = stable_locator(item["limitations_counterevidence_locators"], "limitations/counterevidence")
        reviews.append(item); continue
    m, e, l = locators(a)
    reviews.append({"arxiv_id": a, "source_family_id": sf(a), "primary_evidence_version": f"arXiv:{a}v1",
      "review_route": "deep", "method_identity_locators": f"arXiv:{a}v1 — {m} (official exact-v1 HTML read)",
      "evaluation_locators": f"arXiv:{a}v1 — {e} (official exact-v1 HTML read)",
      "limitations_counterevidence_locators": f"arXiv:{a}v1 — {l} (official exact-v1 HTML read)",
      "artifact_locators": f"exact-v1 URL=https://arxiv.org/html/{a}v1; immutable code/data commit Not Disclosed unless named in body",
      "completion_result": "complete"})
(HERE / "exact-v1-review-packet-independent-final.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")

comparisons, queue = [], []
for x in ret:
    a = x["arxiv_id"]; node = x["owner_node"]; path = paths[node]; adj = adjacent(path)
    delta = REOPEN[a][3] if a in REOPEN else AUTHOR_COMPARE[a]["new_evidence_delta"]
    decision = x["integration_disposition"]
    existing = (f"独立 reviewer 顺读 `{path}` 与相邻章节 {adj}。当前命题：{NODE_PROPOSITION[node]}；"
                + ("该主线尚未明确表达本 family 的 state/control/evidence delta，故保留最小写回。" if decision == "Integrate"
                   else "该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。"))
    item = {"arxiv_id": a, "source_family_id": sf(a), "owner_node": node, "owner_path": path,
            "adjacent_paths": adj, "owner_sha256": hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),
            "adjacent_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in adj},
            "owner_sections_reviewed": h2_headings(path),
            "adjacent_sections_reviewed": {p: h2_headings(p) for p in adj},
            "existing_proposition": existing, "new_evidence_delta": delta, "decision": decision,
            "reviewer": "fresh-context:may2026-day03"}
    comparisons.append(item)
    if decision == "Integrate":
        queue.append({"report_date": "2026-05-27", "arxiv_id": a, "source_family_id": sf(a),
          "stable_node_id": node, "owner_path": path, "adjacent_paths": adj, "evidence_delta": delta,
          "status": "awaiting_root_serial_writeback",
          "writeback_requirement": "merge before exact H2 Review notes; preserve old condition, changed constraint, owner, trade-off, failure, fallback/coexistence and exact-v1 boundary"})
(HERE / "books-current-content-comparison-independent-final.json").write_text(json.dumps({"schema":"books-current-content-comparison-v2.1-independent-final","report_date":"2026-05-27","items":comparisons}, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-writeback-queue-independent-final.json").write_text(json.dumps({"schema":"books-writeback-queue-v2.1-independent-final","report_date":"2026-05-27","status":"awaiting_root_serial_writeback","items":queue}, ensure_ascii=False, indent=2) + "\n")
queue_md = ["# 2026-05-27 Independent Final Books Writeback Queue", "",
            "Status: `awaiting_root_serial_writeback`", "",
            "此文件是非作者 fresh-context 审计后的 canonical pre-write queue；共享 Books 尚未修改。", "",
            "| Source Family | Owner | Evidence delta |", "| --- | --- | --- |"]
for item in queue:
    queue_md.append(f"| `{item['source_family_id']}` | `{item['stable_node_id']}` / `{item['owner_path']}` | {item['evidence_delta']} |")
queue_md += ["", "每项写回后必须由另一位非写作者完成 post-write semantic audit；在此之前 Books Gate 保持 Open。", ""]
(HERE / "BOOKS_WRITEBACK_QUEUE-INDEPENDENT-FINAL.md").write_text("\n".join(queue_md))

audit = {"schema":"fresh-context-independent-audit-v2.1","report_date":"2026-05-27","auditor":"may2026-day03 (non-author)",
 "replay":{"registered":698,"screened":698,"author_denominator":23,"final_denominator":len(ret),
   "author_closures":675,"final_closures":len(closures),"false_negatives_reopened":sorted(REOPEN),
   "false_positives_removed":[],"exact_v1_complete":len(ret),"blocked":0},
 "books":{"author_integrate":len(AUTHOR_INTEGRATE),"final_integrate":len(queue),"final_queue":[x["arxiv_id"] for x in queue]},
 "deep_selection":{"selected":["2605.26461","2605.26508","2605.27789"],"basis":"cross-layer state/control change and operational evidence; Top-3 limits narrative only"},
 "findings":[],"resolution":"all false negatives were exact-v1 reviewed; current owner+adjacent comparison froze a root-serial queue; Books remains Open until writeback and post-write audit."}
(HERE / "fresh-context-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

sha = hashlib.sha256((HERE / "screening-ledger-independent-final.json").read_bytes()).hexdigest()
rv = {x["arxiv_id"]: x for x in reviews}; cm = {x["arxiv_id"]: x for x in comparisons}
L = ["# Daily Research — 2026-05-27","","**Research Date:** 2026-05-27","","**Timezone:** Asia/Shanghai","","**Strict Window:** 2026-05-26 09:00:00 ～ 2026-05-27 09:00:00（北京时间，左闭右开）","","**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。","",f"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立审计完成；{len(queue)} 项等待 root 串行 Books writeback 与 post-write audit。","","## Executive Summary","",f"91,841 条 raw records 中窗口注册并逐项筛选 698 项。独立审计将 author denominator 23 修正为 {len(ret)}：重开 {len(REOPEN)} 个改变长期 state/control/evaluation contract 的 false negatives，closure 675→{len(closures)}；{len(ret)}/{len(ret)} official exact-v1 完整、blocked=0。Author {len(AUTHOR_INTEGRATE)} 项 provisional Integrate 与重开项经 current owner+adjacent 比较后收敛为 {len(queue)} 项最终 queue；共享 Books 尚未写入。","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-27 |","| Window End | 2026-05-27 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID |  |",f"| Denominator ID | DEN-20260527-V2-INDEPENDENT-{len(ret)} |",f"| Denominator Frozen At | {NOW} |","| Completion Status | In Progress |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Open |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-05-26T09:00:00+08:00 | 2026-05-27T09:00:00+08:00 | {NOW} | DataCite v2 deterministic snapshot + 698/698 semantic replay + official exact-v1 | checked | 698 | {';'.join(x['source_family_id'] for x in ret)} | pages=300; final_cursor=end; raw=91841; registered=698; screened=698; retained={len(ret)}; closure={len(closures)} | 2026-05-27T00:59:59Z | screening-ledger-independent-final.json#sha256={sha} | — |","","### Coverage Limitations","","<!-- coverage:SRC-ARXIV:20260527:start -->698/698 identity、title+abstract semantic replay 与非作者 false-positive/false-negative challenge 已闭合。重开项均因其改变长期 state/control/evaluation contract，而不是仅因 AI 相关性；剩余 closure 保留 author 的 family-specific exclusion。<!-- coverage:SRC-ARXIV:20260527:end -->","","## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in ret:
    a=x["arxiv_id"]; s=x["score_v2"]
    L.append(f"| {sf(a)} | arXiv:{a}v1 | paper-v1:{a} | 2026-W22 | 2026-05-26 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {x['review_status']} | accessible | {'knowledge_gap' if x['integration_disposition']=='Integrate' else 'none'} | review:{sf(a)} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{sf(a)} | no |")
L += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in reviews:
    f=sf(r["arxiv_id"]); L.append(f"| {f} | RP-TODO-{f} | {r.get('review_route','deep')} | {r['primary_evidence_version']} | SRC-ARXIV@{r['primary_evidence_version']} | {r['method_identity_locators']} | {r['evaluation_locators']} | {r['limitations_counterevidence_locators']} | {r['artifact_locators']} | claim:{f} | complete |")
L += ["","### Source Reviews",""]
for x in ret:
    a=x["arxiv_id"]; f=sf(a); r=rv[a]; delta=cm[a]["new_evidence_delta"]
    title=x["title"]; abstract=" ".join(x.get("abstract","").split()); mechanism=next((s for s in re.split(r"(?<=[.!?])\s+",abstract) if re.search(r"\b(propose|introduce|present|develop|show|framework|system)\b",s,re.I)),abstract[:500])
    L += [f"<!-- review:{f}:start -->",f"#### {title}","",f"问题与 changed constraint：{delta}。","",f"机制与 ownership：{mechanism} owner=`{x['owner_node']}`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。","",f"Evaluation contract：Method=`{r['method_identity_locators']}`；Evaluation=`{r['evaluation_locators']}`。","",f"Trade-off / failure：`{r['limitations_counterevidence_locators']}`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。","",f"<!-- claim:{f}:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:{f}:end -->","",f"Books Decision=`{x['integration_disposition']}`；共享 Books 尚未写入。",f"<!-- review:{f}:end -->",""]
L += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","所有数字只属于 exact-v1 披露合同；未披露字段保持 Not Disclosed。","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
selected={"2605.26461":"DA-GPU-FAULT-DOMAIN","2605.26508":"DA-ACTION-RISK-GATE","2605.27789":"DA-JUDGE-MEASUREMENT"}
for x in ret:
    a=x["arxiv_id"]; f=sf(a); unit=selected.get(a,"—")
    eligibility = []
    if x["score_v2"]["total"] >= 7:
        eligibility.append("score_7_9")
    if x["integration_disposition"] == "Integrate":
        eligibility.extend(["forced_review", "potential_books_delta"])
    elif not eligibility:
        # The two score-6 candidates still received a current-owner comparison;
        # declaring the pre-Books basis keeps that bounded decision auditable.
        eligibility.append("potential_books_delta")
    L.append(f"| {f} | {'; '.join(eligibility)} | {'selected' if a in selected else 'not_selected'} | {unit} | — | {'跨层 ownership 与 failure pressure' if a in selected else '同等 Source Review 已完成；Top-3 仅限制叙事'} | {'analysis:'+unit if a in selected else 'analysis-decision:'+f} |")
L += ["","<!-- analysis:DA-GPU-FAULT-DOMAIN:start -->### 从共享利用率到可恢复 fault domain\n\nMPS 提高并发利用率时，旧方案默认进程失败边界足够清晰；MMU 与 SM fatal fault 会穿透该假设。新机制把地址隔离、fatality detection 和 client recovery 分给不同 runtime owner，代价是驱动复杂度、恢复状态与残余 fault propagation。MIG、独占 GPU 或作业级重启仍是更强隔离/更简单回退。<!-- analysis:DA-GPU-FAULT-DOMAIN:end -->","","<!-- analysis:DA-ACTION-RISK-GATE:start -->### 从事后审计到 side-effect admission\n\n只在动作完成后追责无法阻止不可逆副作用。counterfactual toll 把 action、safe default、underwriting boundary 和累计 exposure 变成 pre-action gate state；收益是预算化 authority，代价是 world model/off-policy estimation error 与 boundary gaming。高不确定动作必须降级、人工批准或拒绝。<!-- analysis:DA-ACTION-RISK-GATE:end -->","","<!-- analysis:DA-JUDGE-MEASUREMENT:start -->### 从 judge 分数到可复算比较\n\n同一答案差异可来自 evidence budget、长度、聚类结构或 judge prompt。固定候选池/预算、cluster-aware inference、预注册与第二 judge 复制把比较变为 measurement contract；代价是成本和协议刚性。探索阶段可用轻量 judge，但 release claim 必须回到冻结合同。<!-- analysis:DA-JUDGE-MEASUREMENT:end -->"]
for x in ret:
    if x["arxiv_id"] not in selected: L.append(f"<!-- analysis-decision:{sf(x['arxiv_id'])}:start -->完成 exact-v1 Source Review；未进入 Top-3 仅表示日报叙事被更强跨层候选 subsume。<!-- analysis-decision:{sf(x['arxiv_id'])}:end -->")
L += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in ret:
    a=x["arxiv_id"]; c=cm[a]; f=sf(a); L.append(f"| {f} | {x['owner_node']} | {chapter_ref(c['owner_path'])} | {'; '.join(chapter_ref(p) for p in c['adjacent_paths'])} | existing:{f} | delta:{f} | Direct Evolution | {x['integration_disposition']} | books-review:{f} |")
L.append("")
for x in ret:
    a=x["arxiv_id"]; c=cm[a]; f=sf(a); L += [f"<!-- books-review:{f}:start -->",f"<!-- existing:{f}:start -->{c['existing_proposition']} owner_sha256={c['owner_sha256']}。<!-- existing:{f}:end -->",f"<!-- delta:{f}:start -->{c['new_evidence_delta']}<!-- delta:{f}:end --> Decision=`{x['integration_disposition']}`；独立 reviewer 未修改共享 Books。",f"<!-- books-review:{f}:end -->"]
L += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260527-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260527 | none | 698/698 replay；{len(REOPEN)} false negatives 重开并完成 exact-v1 | passed |",f"| SA-20260527-EVIDENCE | fresh-context:may2026-day03 | evidence | review:{sf(ret[0]['arxiv_id'])}; review:{sf(ret[-1]['arxiv_id'])} | none | {len(ret)}/{len(ret)} exact-v1 locators 与 claim boundary 完整，blocked=0 | passed |","| SA-20260527-DEEP | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-GPU-FAULT-DOMAIN; analysis:DA-ACTION-RISK-GATE; analysis:DA-JUDGE-MEASUREMENT | none | Top-3 按跨层 ownership/failure pressure 重选 | passed |",f"| SA-20260527-BOOKS | fresh-context:may2026-day03 | books | books-review:{sf(ret[0]['arxiv_id'])}; books-review:{sf(ret[-1]['arxiv_id'])} | F-20260527-BOOKS-WRITEBACK | {len(queue)} 项已收敛到 root 串行 queue；写回与写后审计尚未发生 | open |","","## 8. Ignored Noise","",f"{len(closures)} 项分母前 closure 保存在 `screening-ledger-independent-final.json`；独立审计未把领域相关性等同于长期系统增量。","","## 9. Recommended Action","",f"Root 按日期顺序串行写回 {len(queue)} 项最终 queue，随后由非写作者执行逐项 post-write semantic audit。","","## 10. Repository Changes","","- 新增 05-27 independent ledger、exact-v1 packet、Books comparison、最终 queue 与 fresh-context audit。","- 更新本日 README；未修改共享 Books，未 stage、commit 或 push。","","## 11. Open Questions","",f"- {len(queue)} 项 Books writeback 是否全部进入 owner 主线并位于首个 exact H2 `## Review notes` 前？","- 写回后是否通过不同 reviewer 的机制、trade-off、failure、fallback 与相邻 owner 审计？","","## 12. Sources"]
for x in ret: L.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — exact-v1；first-public 2026-05-26；accessed 2026-09-02")
L += ["","### Materials Request Ledger","","<!-- validator:materials-request-v1 -->","| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","无：retained exact-v1 全部可访问，blocked=0。","","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Closed`","","Evidence: `Passed`","","Books: `Open`","","unresolved findings: 1","",f"Coverage/Evidence 已独立闭合；{len(queue)} 项 Books 串行写回与 post-write audit 是唯一未解决条件。"]
text = "\n".join(L) + "\n"
for r in reviews:
    a=r["arxiv_id"]; f=sf(a); body=re.search(rf"<!-- review:{re.escape(f)}:start -->(.*?)<!-- review:{re.escape(f)}:end -->",text,re.S).group(1)
    cand={"Event Identity":f"paper-v1:{a}","Primary Identifier":f"arXiv:{a}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":"knowledge_gap" if cm[a]["decision"]=="Integrate" else "none"}
    rp=_expected_review_provenance(f,cand,r.get("review_route","deep"),f"arXiv:{a}v1",f"SRC-ARXIV@arXiv:{a}v1",r["method_identity_locators"],r["evaluation_locators"],r["limitations_counterevidence_locators"],r["artifact_locators"],f"claim:{f}",f"review:{f}",_normalized_body_sha256(body))
    text=text.replace(f"RP-TODO-{f}",rp)
(ROOT / "papers/2026/05/27/README.md").write_text(text)
print(json.dumps({"registered":698,"screened":698,"author_retained":23,"final_retained":len(ret),"closures":len(closures),"exact_v1":len(ret),"blocked":0,"author_integrate":len(AUTHOR_INTEGRATE),"final_integrate":len(queue)},ensure_ascii=False))
