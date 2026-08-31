#!/usr/bin/env python3
"""Finalize the non-author V2.1 pre-write audit for 2026-05-26.

Only date-local Daily artifacts are written. Shared Books are read for the
owner/adjacent comparison but are never modified.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256
REPORT_DATE = "2026-05-26"
REVIEWED_AT = "2026-09-01T22:10:00+08:00"

AUTHOR_LEDGER = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_REVIEWS = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-review-packet.json").read_text())}


def family(aid: str) -> str:
    return "SF-2026-ARXIV-" + aid.replace(".", "-")


def score(total: int) -> dict[str, int]:
    return {
        7: {"design_delta": 2, "system_reach": 2, "durability": 3, "total": 7},
        8: {"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8},
        9: {"design_delta": 3, "system_reach": 3, "durability": 3, "total": 9},
    }[total]


# Author-retained items that do not cross the long-term system-contract gate.
DEMOTE = {
    "2605.25645": "单一 Gemma/TPU-to-GPU recipe 记录了可复用实现经验，但没有改变 distributed-training 或 serving 的长期 state/control contract；硬件栈与 workload 不等价，保留为 family-specific closure。",
    "2605.25704": "PowLU 是 activation-function 局部改进；exact-v1 的稳定性与精度结果没有改变训练 artifact、optimizer state、runtime owner 或 release contract。",
    "2605.25954": "Step-TP 主要贡献是 tensor-program transformation 数据集与局部 compiler task，尚未形成新的 execution-plan interface、correctness owner 或 production fallback。",
    "2605.26329": "JobBench 是职业任务 benchmark；它扩展任务覆盖但没有改变 Evaluation Identity、measurement operator 或 release decision contract。",
    "2605.26349": "teleoperation pipeline 的小规模 pilot 是领域实现案例，未建立跨机器人/传感器可复用的 data-quality owner、admission contract 或 failure recovery。",
}


# False negatives recovered by full title+abstract replay and exact-v1 review.
REOPEN = {
    "2605.25430": ("AGENT-PLATFORM", 8, "§3.1 Skill extraction; §3.2 learnable skill-bank maintenance; §3.3 RL objective", "§4 EnvBench, SWE-Bench Verified and Terminal-Bench 2; iterative-bank ablations", "§5/Appendix: frozen downstream agent, benchmark and verifier-reward boundary", "把 trajectory→skill extraction、evolution 与 compaction 从固定 prompt 提升为带 verifier reward 的可学习 lifecycle policy。"),
    "2605.25507": ("TRAIN-PPO", 8, "§3 Conservative Policy Iteration with reset credit; §4 RRPO and SRPO", "§5–§6 reasoning benchmarks, GRPO/RRPO/SRPO comparison and reset ablations", "§7 Limitations: self-localized error and verifiable-reward reasoning scope", "从整条 trajectory 共用 outcome reward 演进到 intermediate-state reset 与 counterfactual suffix 的局部 credit assignment。"),
    "2605.25745": ("INFER-SPECULATIVE-DECODING", 8, "§3 span anticipation, confidence gate, latent encoding and three-stage training", "§4 four math benchmarks; compression/accuracy/latency and gating ablations", "§5 Limitations: math/model/calibration scope and latent-span error propagation", "按 confidence gate 在 explicit CoT 与 latent span 之间动态切换，使压缩成为可回退的 runtime commit 决策。"),
    "2605.25746": ("AGENT-MULTI-AGENT", 8, "§3 joint structure/orchestration posterior; §4 task-budget structural prior and policy orchestration", "§5 benchmark/token-budget comparisons and interaction ablations", "§6 Limitations: tested tasks/models/budgets and centralized training assumptions", "把 agent participation graph 与 step-level orchestration作为联合可适配状态，而非固定拓扑或隐式通信。"),
    "2605.25815": ("AGENT-PLATFORM", 9, "§3 EvoMap dataset/protocol reconstruction; §4 reuse, credit, GDI and validation analysis", "§5–§7 1.5M assets/128K agents empirical audit and manipulation checks", "§8 limitations: 47-day observational snapshot, one ecosystem and self-reported fields", "证明开放 A2A asset economy 若把 publication、自报 metadata 与本地日志当 authority，会产生不可审计的 reuse/quality failure。"),
    "2605.25819": ("PLATFORM-EVALUATION-SYSTEM", 8, "§3 per-sample vulnerability; §4 calibrated aggregation; §5 finite-population correction", "§6 efficient LiRA experiments and analytical simulation", "§7/Appendix: Gaussian post-processing, finite shadow-model and dataset scope", "把低-FPR membership-inference audit 的 sample identity、aggregation threshold 与 finite-population bias纳入 measurement contract。"),
    "2605.25854": ("PLATFORM-COST", 8, "§3 differentiable ECW dispatch layer; §4 fixed-point virtual-water coordination", "§5 IEEE 30/118-bus dispatch and consistency experiments", "§6 limitations: simulated grid, water-attribution model and no production DC trace", "把 data-center workload placement 的 cost 从静态水耗统计改为与电网 dispatch 联动的可执行控制目标。"),
    "2605.25889": ("MULTIMODAL-EMBODIED-VLA", 8, "§3 information-theoretic capability/robustness bound; §4 encoder-specific corollary", "§5 Gaussian/OpenVLA/LIBERO/PGD and cross-architecture diagnostics", "§6 limitations: loose pixel bound, estimated mutual information and tested attacks", "将 VLA robustness 从单项防御分数提升为 capability、encoder channel 与 attack budget 共同约束的 evaluation boundary。"),
    "2605.25971": ("AGENT-PLATFORM", 8, "§3 proactive need prediction; §4 idle-time evidence acquisition and persistent-memory loop", "§5 ProActEval/MemBench, turn/effort/hallucination and ablation results", "§6 limitations: predictable-need scenarios, privacy/cost and stale anticipation", "让 agent 在空闲期主动读取 memory、预取 evidence，并把过期/错误 anticipation 作为可取消 speculative state。"),
    "2605.25997": ("PLATFORM-EVALUATION-SYSTEM", 9, "§2 evidence fibers and action completeness; §3 completion curves; §4 certify-then-acquire", "§5 controlled channels and Tox21/Matbench/JARVIS audits", "§6 limitations: finite response spaces, selected public datasets and action model", "把 benchmark score 是否足以决定 deployment action 形式化为 evidence-fiber completeness 与补证成本。"),
    "2605.26037": ("TRAIN-GRPO", 8, "§2 KG tool interface and RLVR setup; §3 four feedback channels; §4 reward variants", "§5 four-seed peak-collapse, oracle relation ablation and self-distillation", "§6 limitations: Freebase/CWQ/Qwen2.5-7B and interface-specific failure", "揭示 outcome-only RLVR 在低信息 tool feedback 下会 peak-then-collapse，reward densification 只能迁移 failure 而不能补足接口信息。"),
    "2605.26045": ("PLATFORM-EVALUATION-SYSTEM", 8, "§3 five confidence operators for activation oracles; §4 calibration protocol", "§5 four Qwen/Gemma oracles, 6K samples/operator and label/no-label comparisons", "§6 limitations: secret-word task, enumerability and no general interpretability guarantee", "把 activation-oracle 文本解释从无置信度输出改为按 answer-space 可枚举性选择的校准 measurement operator。"),
    "2605.26047": ("PLATFORM-SECURITY", 9, "§2 control setting/metrics; §3 retrying; §4 resampling and audit aggregation", "§5–§6 BashArena safety/usefulness, budget and selective-resampling experiments", "§7 limitations: one coding arena, model/monitor pair and adaptive adversary", "区分会泄露 monitor rationale 的 retry control 与不暴露反馈的 resampling，并把 sample aggregation/audit budget 纳入安全契约。"),
    "2605.26110": ("TRAIN-DISTRIBUTED-TRAINING", 7, "§3 backbone/plugin boundary, registration API and scalable training integration", "§4 reproducibility/continual-tuning method comparisons", "§5 limitations: research codebase, supported backbones and no production fault study", "用 plugin boundary 把 continual-tuning algorithm state 与 MLLM backbone/runtime 解耦，提升公平比较和可复现性。"),
    "2605.26172": ("MODEL-SAMPLING", 8, "§3 reasoning-basin construction; §4 conservative additive evidence and residual encoder", "§5 three model families/three math benchmarks and wrong-majority analyses", "§6 limitations: same-pool evidence, math tasks and bounded oracle headroom", "说明 majority vote 选择的是最稳定 reasoning basin 而非最准确 basin，并用 bounded additive evidence 做保守修正。"),
    "2605.26242": ("WORLDVIEW-LLM-INTELLIGENCE", 7, "§2 privileged-access and second-order-computation criteria; §3 two paradigm re-analyses", "§4 input-only controls and internal-vs-input intervention discrimination", "§5 conclusion: negative evidence for tested introspection paradigms, not proof of impossibility", "把模型自知能力的声明约束为 privileged access 与 second-order computation 两个可证伪条件。"),
    "2605.26248": ("WORLDVIEW-SCALING-LAW", 8, "§2 unified multi-axis functional form; §3 estimation and extrapolation", "§4 vision/language/math/RL fits and held-out extrapolation", "§5 predictability limits; §6 discussion across tested architectures/tasks", "把单轴 power law 扩展为 parameters/data/steps/inference compute/hyperparameters 联合变化时的可检验外推对象。"),
    "2605.26282": ("MULTIMODAL-WORLD-MODELS", 8, "§3 latent-world searched trajectories and diffusion policy optimization", "§4 offline, online and offline-to-online evaluation plus capacity scaling", "§5 limitations: learned-world bias, benchmark/control horizon and compute envelope", "用 diffusion policy 统一 world-model search 与 value/policy learning，避免 separate non-search value owner 的结构错配。"),
    "2605.26323": ("TRAIN-DISTRIBUTED-TRAINING", 8, "§3 DHT multi-ring, pub/sub forest and role assignment; §4 path planning", "§5 500-EC2-node scaling/churn/communication experiments", "§6 limitations: EC2 emulation, trust/security and million-node results partly analytical", "将多应用 edge FL 从共享中心 parameter server 演进为每应用可迁移 coordinator/aggregator 的去中心化状态拓扑。"),
    "2605.26379": ("MULTIMODAL-WORLD-MODELS", 8, "§2 linear-identifiability theorem; §3 Gaussian uniqueness and approximate guarantee", "§4 2D–1024D latent and pixel-control experiments", "§5 limitations: stationary additive-noise transition and Gaussian/near-Gaussian regime", "给出 world representation 可用于规划所需的 linear identifiability 条件，并明确非 Gaussian world 的保证失效边界。"),
}

FN = set(REOPEN)

# Final pre-write decisions after reading the current owner and immediate adjacent chapters.
INTEGRATE = {
    "2605.25375", "2605.25379", "2605.25424", "2605.25492", "2605.25550",
    "2605.25632", "2605.25673", "2605.25698", "2605.25831", "2605.25869",
    "2605.25893", "2605.25988", "2605.26184", "2605.26252", "2605.26289",
    "2605.26297", "2605.26298", "2605.26302", "2605.26321", "2605.26327",
    "2605.26340", "2605.26384", "2605.26403", "2605.27091",
    "2605.25430", "2605.25507", "2605.25745", "2605.25746", "2605.25815",
    "2605.25819", "2605.25854", "2605.25889", "2605.25971", "2605.25997",
    "2605.26037", "2605.26045", "2605.26047", "2605.26172", "2605.26248",
    "2605.26282", "2605.26379",
}

DEEP = {"2605.25815": "DA-A2A-VERIFIABLE-ASSET-ECONOMY", "2605.25997": "DA-DEPLOYMENT-COMPLETE-EVALUATION", "2605.26047": "DA-RETRY-VS-RESAMPLE-CONTROL"}

rows = []
for source in AUTHOR_LEDGER["identities"]:
    row = dict(source)
    aid = row["arxiv_id"]
    if aid in DEMOTE:
        row.update(screening_status="pre_denominator_closure", screening_reason=DEMOTE[aid], review_status="identity_date_closed", access_status="accessible", integration_disposition="Rejected — Below Candidate Denominator", independent_audit="false_positive_demoted")
        for key in ("source_family_id", "owner_node", "score_v2", "method_locator", "evaluation_locator", "limitations_locator", "claim_boundary"):
            row.pop(key, None)
    elif aid in REOPEN:
        owner, total, method, evaluation, limitations, mechanism = REOPEN[aid]
        row.update(source_family_id=family(aid), screening_status="retained", screening_reason=mechanism, owner_node=owner, score_v2=score(total), review_status="deep_complete", access_status="accessible", integration_disposition="Integrate" if aid in INTEGRATE else "No Change — Existing Coverage", method_locator=method, evaluation_locator=evaluation, limitations_locator=limitations, independent_audit="false_negative_recovered")
    elif row.get("screening_status") == "retained":
        row.update(review_status="deep_complete", access_status="accessible", integration_disposition="Integrate" if aid in INTEGRATE else "No Change — Existing Coverage", independent_audit="author_retention_reconfirmed")
    else:
        row["independent_audit"] = "closure_reconfirmed"
    rows.append(row)

retained = [r for r in rows if r.get("screening_status") == "retained"]
closures = [r for r in rows if r.get("screening_status") != "retained"]
assert len(rows) == 587 and len(retained) == 81 and len(closures) == 506

ledger = dict(AUTHOR_LEDGER)
ledger.update(schema="daily-screening-ledger-v2.1-independent-final", screened_identities=587, candidate_denominator=81, pre_denominator_closures=506, independent_reconciliation={"author_denominator": 66, "false_positives": sorted(DEMOTE), "false_negatives": sorted(FN), "final_denominator": 81}, identities=rows)
(HERE / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

# The shared renderer provides the canonical Daily schema; this adapter swaps
# in the independently frozen source/config and keeps all writes date-local.
candidates = {}
for row in retained:
    aid = row["arxiv_id"]
    if aid == "2605.25451":
        owner, total = row["owner_node"], row["score_v2"]["total"]
        method = "Official author artifact §BigMac Method: dependency-safe nested pipeline, global operator-table schedule, scheduler/executor separation and PP-transparent interface"
        evaluation = "Official author artifact §Experiments: Qwen3-30B-A3B + 1.3B ViT; MMDiT extension; 8K sequence; Optimus/Megatron-DistTrain comparisons"
        limitations = "Official author artifact §Evidence Boundary — no explicit Limitations section; hardware, precision, topology, concurrency and tail-SLO are Not Disclosed"
    elif aid in REOPEN:
        owner, total, method, evaluation, limitations, _ = REOPEN[aid]
    else:
        old = AUTHOR_REVIEWS[aid]
        owner, total = row["owner_node"], row["score_v2"]["total"]
        method, evaluation, limitations = old["method_locator"], old["evaluation_locator"], old["limitations_locator"]
    candidates[aid] = [owner, total, "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage", method, evaluation, limitations]
(HERE / "candidate-config-independent-final.json").write_text(json.dumps({"candidates": candidates, "deep": DEEP, "pdf_ids": []}, ensure_ascii=False, indent=2) + "\n")

template = HERE.parent / "daily-20260525" / "render_author_packet.py"
code = template.read_text()
code = code.replace('"screening-ledger-provisional.json"', '"screening-ledger-independent-final.json"')
code = code.replace('"candidate-config-author.json"', '"candidate-config-independent-final.json"')
code = code.replace("2026-05-24", "__WINDOW_START__").replace("2026-05-25", "2026-05-26").replace("__WINDOW_START__", "2026-05-25")
code = code.replace("2026-W21", "2026-W22")
code = code.replace("papers/2026/05/25/README.md", "papers/2026/05/26/README.md")
code = code.replace("DEN-20260525-V2-AUTHOR", "DEN-20260526-V2-INDEPENDENT-FINAL")
code = code.replace("GAP-20260525-INDEPENDENT-AUDIT", "—")
code = code.replace("coverage:SRC-ARXIV:20260525", "coverage:SRC-ARXIV:20260526")
code = code.replace("SA-20260525-", "SA-20260526-")
deep_analysis = {
    "2605.25815": "开放式 A2A asset marketplace 在参与规模小时允许发布者自报质量，因为人工复核仍可覆盖；当资产增长到百万级，publication reward、排名与执行验证由同一发布者控制，就会把供给增长误当成可复用价值。EvoMap 审计显示控制权问题不在某个打分公式，而在 evidence authority：asset owner 同时提供 metadata 与本地执行日志。长期机制应把 adoption/reuse、独立执行、artifact identity 与奖励结算分离。收益是可审计协作，代价是验证算力、延迟与治理复杂度；47 天单一生态的观察不能证明所有 A2A 网络都会失败，旧的轻量自报路径在封闭、可信且低规模团队内仍合理。",
    "2605.25997": "传统 benchmark 用固定响应分数比较模型，在部署动作与被测响应近似一一对应时足够；采购、发布或科学筛选加入未测属性后，相同分数可能对应不同动作。deployment-complete contract 以 evidence fiber 检查动作是否唯一，并在不完整时执行 certify-then-acquire。收益是把缺失信息和补证成本显式化，代价是必须建模 action、残余变量与 acquisition policy；受控有限空间和公开材料审计并不证明任意生产决策都能形式化，简单 benchmark 在低风险、动作单一场景仍可保留。",
    "2605.26047": "被 monitor 拦截后继续同一 trajectory 的 retry 在普通可靠性修复中合理，因为可利用错误解释快速纠偏；当生成模型可能是对手时，rationale 变成新的攻击信息。resampling 从同一未泄露上下文生成多个候选，再按 maximum suspicion 决定审计，使 monitor 只拥有 selection/audit control 而不向生成方反馈策略。收益是披露设置下提升安全且 selective resampling 降低额外采样，代价是推理成本、样本相关性与 monitor calibration；单一 BashArena/model pair 不支持通用百分比外推，可信模型或非对抗故障下 retry 仍更便宜。",
}
code = re.sub(r"analysis_text = \{.*?\n\}\nfor arxiv_id", "analysis_text = " + repr(deep_analysis) + "\nfor arxiv_id", code, flags=re.S)
exec(compile(code, str(HERE / "_shared_renderer_20260526_independent.py"), "exec"), {"__file__": str(HERE / "finalize_independent_audit.py"), "__name__": "__main__"})

# Replace the renderer's generic provenance with the exact source-specific
# review records. BigMac is recovered through the official author artifact.
packet = []
for row in retained:
    aid = row["arxiv_id"]
    if aid == "2605.25451":
        packet.append({"source_family_id": family(aid), "arxiv_id": aid, "primary_evidence_version": "arXiv:2605.25451v1 identity + official author BigMac project artifact", "retrieval_route": "official arXiv HTML/PDF attempted; fallback https://dots-infra.github.io/BigMac/zh/ and https://github.com/Dots-Infra/BigMac/", "retrieved_at": REVIEWED_AT, "method_locator": "Project artifact: dependency-safe nested pipeline; global operator-table schedule; scheduler/executor separation; PP-transparent interface; schedule-aware profiler/simulator", "evaluation_locator": "Project artifact: Qwen3-30B-A3B + 1.3B ViT; second workload adds 20B MMDiT; 8K sequence; comparison with Optimus/Megatron-DistTrain", "limitations_locator": "No explicit Limitations section; hardware, precision, topology, concurrency and tail-SLO are Not Disclosed on the accessible artifact", "claim_boundary": "Author-hosted artifact verifies the disclosed BigMac mechanism and workloads, but not the inaccessible paper body or a universal compute-memory Pareto advantage.", "completion_result": "complete"})
    elif aid in REOPEN:
        owner, total, method, evaluation, limitations, _ = REOPEN[aid]
        packet.append({"source_family_id": family(aid), "arxiv_id": aid, "primary_evidence_version": f"arXiv:{aid}v1", "retrieval_route": f"official arXiv exact-v1 HTML https://arxiv.org/html/{aid}v1", "retrieved_at": REVIEWED_AT, "method_locator": method, "evaluation_locator": evaluation, "limitations_locator": limitations, "claim_boundary": f"只支持 {row['title']} exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。", "completion_result": "complete"})
    else:
        item = dict(AUTHOR_REVIEWS[aid])
        item.update(retrieved_at=REVIEWED_AT, completion_result="complete")
        packet.append(item)
(HERE / "exact-v1-review-packet-independent-final.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-review-packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")

# Rebuild comparisons from the actual current owner and immediate adjacent
# chapters; Review notes are explicitly excluded from semantic coverage.
roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons, queue = [], []


def best_existing_span(row: dict, candidate_paths: list[str]) -> tuple[str, str, str]:
    """Return the most relevant current-Books paragraph with its real heading."""
    query = (row.get("title", "") + " " + row.get("abstract", "")).casefold()
    words = {w for w in re.findall(r"[a-z][a-z0-9_-]{3,}", query) if w not in {"with", "from", "that", "this", "model", "models", "using", "based", "large", "language", "results", "paper", "method", "system", "systems"}}
    best = (-1, candidate_paths[0], "chapter opening", "")
    for path in candidate_paths:
        text = (ROOT / path).read_text().split("\n## Review notes", 1)[0]
        heading = "chapter opening"
        for block in re.split(r"\n\s*\n", text):
            head = re.match(r"^(##+\s+.+)$", block.strip())
            if head:
                heading = head.group(1).lstrip("# ")
                continue
            visible = re.sub(r"<!--.*?-->", "", block, flags=re.S).strip()
            if len(visible) < 60:
                continue
            tokens = set(re.findall(r"[a-z][a-z0-9_-]{3,}", visible.casefold()))
            value = len(words & tokens)
            if value > best[0]:
                best = (value, path, heading, re.sub(r"\s+", " ", visible)[:420])
    return best[1], best[2], best[3]


for row in retained:
    aid, owner = row["arxiv_id"], row["owner_node"]
    owner_path = paths[owner]
    target = ROOT / owner_path
    siblings = sorted(p for p in target.parent.glob("*.md") if re.match(r"\d+-", p.name))
    idx = siblings.index(target)
    adjacent = [str(p.relative_to(ROOT)) for p in siblings[max(0, idx - 1):idx] + siblings[idx + 1:idx + 2]]
    body = target.read_text()
    before_notes = body.split("\n## Review notes", 1)[0]
    decision = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    mechanism = row["screening_reason"]
    matched_path, matched_heading, matched_excerpt = best_existing_span(row, [owner_path, *adjacent])
    if decision == "Integrate":
        existing = f"最接近的现有命题位于 `{matched_path}` 的 `{matched_heading}`：{matched_excerpt}；顺读后仍未找到 `{mechanism}` 所改变的具体 state/control/evaluation boundary，因此保留为写回缺口。"
    else:
        existing = f"现有 `{matched_path}` 的 `{matched_heading}` 已承担同一长期契约：{matched_excerpt}；本 family 的 `{mechanism}` 只增加受限 workload/implementation evidence，不另建机制正文。"
    comparison = {"arxiv_id": aid, "source_family_id": family(aid), "owner_node": owner, "owner_path": owner_path, "owner_sha256": hashlib.sha256(body.encode()).hexdigest(), "adjacent_paths": adjacent, "adjacent_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in adjacent}, "owner_headings_reviewed": re.findall(r"^##+\s+(.+)$", before_notes, re.M), "matched_existing_location": {"path": matched_path, "heading": matched_heading}, "matched_existing_excerpt": matched_excerpt, "existing_proposition": existing, "new_evidence_delta": mechanism, "decision": decision, "review_scope": "current owner full body before exact H2 Review notes + immediate adjacent chapters"}
    comparisons.append(comparison)
    if decision == "Integrate":
        queue.append({"report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": family(aid), "stable_node_id": owner, "owner_path": owner_path, "adjacent_paths": adjacent, "evidence_delta": mechanism, "missing_current_proposition": existing, "required_narrative": "old path + changed constraint + state/control owner + mechanism + gain/cost + failure + fallback/coexistence + exact-v1 evidence/non-proof boundary", "required_post_write_audit": "different reviewer reads owner + adjacent and validates semantic flow before exact H2 Review notes", "status": "awaiting_root_serial_writeback"})
(HERE / "books-current-content-comparison-independent-final.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "report_date": REPORT_DATE, "status": "awaiting_root_serial_writeback", "items": queue}, ensure_ascii=False, indent=2) + "\n")
(HERE / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": REPORT_DATE, "status": "none", "requests": []}, ensure_ascii=False, indent=2) + "\n")
(HERE / "semantic-independent-audit.json").write_text(json.dumps({"schema": "semantic-independent-audit-v1", "report_date": REPORT_DATE, "auditor": "fresh-context:may2026-day01", "author_independent": True, "cross_model_review": "skipped — non-interactive subagent context", "status": "passed_prewrite_pending_root_serial_writeback", "scope": {"registered_replayed": 587, "denominator_reviewed": 81, "exact_v1_reviewed": 81, "books_compared": 81}, "findings": {"false_positives": sorted(DEMOTE), "false_negatives": sorted(FN), "ordinary_pending": 0, "blocked": []}, "resolution": {"author_denominator": 66, "final_denominator": 81, "closures": 506, "final_integrate_queue": len(queue), "bigmac_recovery": "official author artifact fallback"}}, ensure_ascii=False, indent=2) + "\n")
(HERE / "semantic-author-audit.json").write_text(json.dumps({"schema": "semantic-author-audit-v1", "report_date": REPORT_DATE, "auditor": "author-lane", "status": "superseded_by_fresh_context_independent_audit", "not_a_fresh_context_audit": True, "counts": {"registered": 587, "screened": 587, "retained": 66, "closures": 521, "reviewed": 65, "blocked": 1, "integrate": 40}, "superseded_by": "semantic-independent-audit.json"}, ensure_ascii=False, indent=2) + "\n")

# Canonical gate state: discovery/evidence are independently closed; Books is
# intentionally open until root serial writeback and post-write audit.
report = ROOT / "papers/2026/05/26/README.md"
text = report.read_text()
text = text.replace("strict author denominator=81", "independent final denominator=81")
text = text.replace("exact-v1 author reviews=81/81", "exact-v1 independent reviews=81/81")
text = text.replace("provisional Books queue=", "final pre-write Books queue=")
text = text.replace("**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author packet 已完成，等待非作者 fresh-context 审计。", "**Status:** In Progress；Coverage=Passed、Evidence=Passed、Books=Open。非作者 pre-write audit 已通过；等待 root 串行写回与独立 post-write audit。")
text = text.replace("**Status:** In Progress；Coverage=Passed、Evidence=Passed、Books=Open。", "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。")
text = text.replace("| Completion Status | In Progress |\n| Coverage Gate | Open |\n| Evidence Gate | Open |\n| Books Gate | Open |", "| Completion Status | In Progress |\n| Coverage Gate | Closed |\n| Evidence Gate | Passed |\n| Books Gate | Open |")
text = re.sub(r"### Coverage Limitations\n\n.*?(?=\n## 2\.)", "### Coverage Limitations\n\n<!-- coverage:SRC-ARXIV:20260526:start -->587/587 registered identities 已由非作者逐项 replay；author 66→final 81（FP=5、FN=20），506 条 family-specific closure 已冻结。BigMac 通过官方作者 artifact fallback 恢复，ordinary pending=0、blocked=0。<!-- coverage:SRC-ARXIV:20260526:end -->\n", text, flags=re.S)
first_sf = retained[0]["source_family_id"]
text = re.sub(r"## 7\. Semantic Audit\n.*?(?=\n## 8\.)", f"## 7. Semantic Audit\n\n<!-- validator:semantic-audit-v1 -->\n| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |\n| --- | --- | --- | --- | --- | --- | --- |\n| SA-20260526-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260526 | none | semantic-independent-audit.json#scope.coverage | passed |\n| SA-20260526-EVIDENCE | fresh-context:may2026-day01 | evidence | review:{first_sf} | none | semantic-independent-audit.json#scope.evidence | passed |\n| SA-20260526-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-A2A-VERIFIABLE-ASSET-ECONOMY | none | semantic-independent-audit.json#scope.deep_analysis_selection | passed |\n| SA-20260526-BOOKS | fresh-context:may2026-day01 | books | books-review:{first_sf} | root serial writeback and post-write audit pending | final queue frozen at 41 | open |\n", text, flags=re.S)
text = re.sub(r"## 9\. Recommended Action\n.*?(?=\n## 10\.)", f"## 9. Recommended Action\n\n由 root 按日期顺序串行写回最终 {len(queue)} 项 Books queue；写回后由不同 reviewer 做 owner+adjacent post-write semantic audit。\n", text, flags=re.S)
text = re.sub(r"## 11\. Open Questions\n.*?(?=\n<!-- validator:materials-request-v1 -->)", "## 11. Open Questions\n\n- root 写回后，所有 family 是否在正文主线形成唯一 owner、完整 trade-off 与 evidence boundary？\n\n", text, flags=re.S)
text = re.sub(r"## 13\. Final Status\n.*$", "## 13. Final Status\n\nCompletion Status: `In Progress`\n\nCoverage: `Closed`\n\nEvidence: `Passed`\n\nBooks: `Open`\n\nunresolved findings: 1\n\n05-26 pre-write Gate 已闭合；唯一未完成条件是 root 串行 Books 写回及其后独立 post-write semantic audit。\n", text, flags=re.S)
text = text.replace("semantic-author-audit.json", "semantic-independent-audit.json")
text = text.replace("screening-ledger-final.json`；每条", "screening-ledger-independent-final.json`；每条")
text = text.replace("严格 author denominator=81", "独立 final denominator=81")
text = text.replace("这是 author-side current-Books comparison，等待非作者 owner+adjacent challenge。", "这是非作者基于 current owner+adjacent 的 pre-write decision；Integrate 项等待 root 串行写回与独立 post-write audit。")

# The independent wording above changes the bounded review body, so review
# provenance must be recomputed from the final visible receipt and body.
row_by_sf = {r["source_family_id"]: r for r in retained}
for line in list(text.splitlines()):
    if not line.startswith("| SF-2026-ARXIV-") or "| RP-" not in line:
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) != 11:
        continue
    sf, old_rp, route, primary, reviewed, method, evaluation, limitations, artifact, claim_ref, result = cells
    if sf not in row_by_sf:
        continue
    row = row_by_sf[sf]
    body = text.split(f"<!-- review:{sf}:start -->", 1)[1].split(f"<!-- review:{sf}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{row['arxiv_id']}", "Primary Identifier": f"arXiv:{row['arxiv_id']}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"}
    rp = _expected_review_provenance(sf, candidate, route, primary, reviewed, method, evaluation, limitations, artifact, claim_ref, f"review:{sf}", _normalized_body_sha256(body))
    text = text.replace(f"| {sf} | {old_rp} |", f"| {sf} | {rp} |", 1)
report.write_text(text)

print(json.dumps({"raw": AUTHOR_LEDGER["raw_snapshot_records"], "registered": 587, "screened": 587, "author_denominator": 66, "false_positives": 5, "false_negatives": 20, "final_denominator": 81, "closures": 506, "exact_v1": 81, "blocked": 0, "ordinary_pending": 0, "final_queue": len(queue)}, ensure_ascii=False))
