#!/usr/bin/env python3
"""Render the 2026-05-26 V2.1 author packet without touching shared Books.

The report schema is shared with the independently reviewed 2026-05-25 packet;
this adapter owns only date-local candidate, evidence, and Books-decision data.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Every locator below was recovered from the official exact-v1 HTML table of
# contents and then checked against the corresponding method/evaluation/scope
# sections. BigMac is the sole exact-v1 body exception and remains blocked.
LOC = {
    "2606.00093": ("§2.1 Judgment Scale and Scope; §3 Closed-Form Metric Definitions", "§4–§7 binary equivalence, kappa, abstention and multi-judge analysis", "§8 reporting checklist; the paper is methodological rather than a benchmark of judge quality"),
    "2605.25338": ("§3 Problem Setup; §4.1–§4.3 causal attribution, counterfactual repair and multi-agent validation", "§5–§6 intervention protocol, repair performance, minimality and ablations", "§7 Discussion; Appendix A.10 Runtime Analysis; Appendix B Future Work"),
    "2605.25375": ("§III problem definition; §III-B dynamic priority, bandwidth pathfinder and cost allocator", "§IV-A–§IV-E geo-cluster setup, bandwidth/GPU/workload sensitivity and ablation", "§II-A prior limitations; §V conclusion; evidence is simulator/trace-bound"),
    "2605.25376": ("§2 threat model; §3 three-layer runtime gates; §5 dynamic rogue signals; §6 evidence chain", "§4.4 worked fleets; §8–§10 evaluation, red-team and performance sections", "§4.5 calibration and limitations; §11 limitations and threat-model boundary"),
    "2605.25379": ("§1.2 structured retrieval state; §3 tree memory, adaptive routing, MARS/SMP and access control", "§4 datasets, main results, component ablation and verifier-guided recovery", "§5 Limitations; Appendix A.4 efficiency accounting; Appendix F.3 failure modes"),
    "2605.25389": ("§2 threat model; §3.1–§3.3 attack memory, memory-augmented attack and Attack-Flow GRPO", "§4 main, ablation, stealth and cross-model experiments", "§6 Conclusion; Appendix C framework/dataset/training scope"),
    "2605.25421": ("§2.2–§2.4 dual-channel protocol, cross-channel alignment and interactive co-training", "§3–§4 task/metric setup, ablation, compatibility, robustness and scale analysis", "§6 Conclusion; Appendix B model-family/scale boundary"),
    "2605.25422": ("§3 system model; §4 token/KV latency; §5.1–§5.2 constrained mode and bandwidth optimization", "§5.3 numerical validation and multi-round mode switching", "§6 Conclusion and Future Work; wireless/model assumptions bound generality"),
    "2605.25424": ("§3 session-budget MDP; §4.1–§4.3 HBR, CQL and deployment lambda-sweep", "§5 cost-safety frontier, delayed-gratification and ablation experiments", "§6 Conclusion; offline reward proxy, single model pair and fixed-cost assumptions"),
    "2605.25451": ("exact-v1 method body unavailable", "exact-v1 evaluation body unavailable", "arXiv HTML/PDF retrieval failed; abstract alone cannot support mechanism, evaluation or limitations"),
    "2605.25475": ("§3.1 learned token indexer; §3.2 latent fast/slow-weight memory", "§4 RULER, NIAH, LongBench, compression and ablation", "§6 Conclusion & Limitation; Appendix A limited budgets, models and frozen backbone"),
    "2605.25492": ("§3 configuration grid; §4 SDI/CFR/rank-concordance/variance metrics", "§5 configuration-conditional reversals and cross-package analysis", "§6 Threats to Validity: narrow model/benchmark/envelope and qualitative variance attribution"),
    "2605.25521": ("§3 motivation; §4 centroid-parallel SIMD, cache organization and ranking-preserving reformulation", "§5 setup, end-to-end, microbenchmark, ablation and microarchitecture evidence", "§7 Conclusion; evaluated CPU/PQ construction boundary"),
    "2605.25535": ("§3–§4 static/dynamic PerMem-Bench; §7.1 session-level personalized storage gating", "§5 meta-evaluation; §6 protocol; §7.2 memory-system results", "§8 Conclusion; appendix construction/judge/checkpoint-sampling boundaries"),
    "2605.25537": ("§III problem; §IV-A action-prior denoising; §IV-B inference blending", "§V–§VI Kinetix setup, real-robot pilot and delay/window sweeps", "§VII Discussion; small real-robot pilot and policy/workload scope"),
    "2605.25547": ("§3.2 posterior action sampling; §3.3 task-progress verification", "§4 simulation, real-world and sample/latent ablations", "Appendix I linear-progress assumption and base-policy capacity boundary"),
    "2605.25550": ("§2 workload/stage imbalance; §3 async pipeline and hybrid instance scheduler; §4 implementation", "§5 quality, latency, scale, robustness, elasticity and utilization", "§7 Conclusion; diffusion-stage topology and disclosed hardware/workload boundary"),
    "2605.25621": ("§4.1 evidence construction; §4.2 long/short memory update; §4.3 response trigger", "§3 SOVBench and §5 audio-visual/visual-only/ablation evaluation", "Appendix J trigger failures; Appendix K limitations and future work"),
    "2605.25624": ("§2.1 adversarial task/reward co-generation; §2.2 environment scaling", "§3–§4 training results, data/environment scaling and emergent multi-action calls", "§6 Limitations; synthetic task and environment-fidelity boundary"),
    "2605.25632": ("§3 action taxonomy and quote-bind-commit; §4 authority frontier and capital metrics", "§5–§7 simulation, calibration and runtime-control experiments", "§8 Limitations; actuarial assumptions and empirical deployment boundary"),
    "2605.25641": ("§3 production correction setting; §4 factual-nugget variants and iterative optimization", "§5–§6 held-out, transfer, negative-control and answer-level results", "§7 Conclusion: one retrieval architecture, English-only and LLM dependence"),
    "2605.25645": ("§2 hardware; §3 TPU recipe; §4 checkpoint conversion; §7 serving setup", "§5–§9 training, evaluation, inference and cost comparison", "§10 Summary; single Gemma/cloud recipe and non-equivalent TPU/GPU stack boundary"),
    "2605.25653": ("§3 threat/system model; §4 typed zero-trust enforcement and physical-impact tiers", "§5 deployed instantiation, 60 traces and coverage analysis", "§6 Conclusion; small system/model/trace envelope"),
    "2605.25655": ("§III-A framework; §III-B operators; §III-C graph schedule; §III-D adaptive parallelism", "§IV throughput, ablation and operator scaling experiments", "§V Conclusion; MT-3000-specific architecture and bandwidth boundary"),
    "2605.25673": ("§3 referential stability; §4 threat model; §5 workflows; §8 attestation/fingerprinting architectures", "§7 provider identifier survey and workflow analysis", "§9 Conclusions; proposal-level evidence without broad deployed evaluation"),
    "2605.25674": ("§2 layer-wise target; §3 unbiased estimator; §4 variance analysis", "§5 memorisation-regime setup, decision rule and empirical validation", "§6 Discussion and limitations; modest model/monitoring setting"),
    "2605.25682": ("§3 segment communication, staging bottleneck and adaptive inference", "§4 prototype; §5 latency, energy, qualitative and instrumentation results", "§6 Conclusion; Jetson/Wi-Fi prototype and qualitative-output boundary"),
    "2605.25698": ("§3 quality-aware functional scaling law; §4 optimal schedule; §5.1 Drop-Stable-Rampup", "§5.2–§5.4 batch drop, phase ratio and schedule comparison", "§6 scope: theoretical simplification, multi-task heterogeneity, scale dependence and overhead"),
    "2605.25704": ("§3 PowLU formulation and theory", "§4 scaling, 7.9B/124B, stability and ablation experiments", "§5 Conclusion; activation/model/precision envelope and no universal stability guarantee"),
    "2605.25707": ("§3 corruption benchmark; §4 robustness method", "§5 setup, main results and ablation; Appendix E case studies", "§6 Conclusion; OSWorld corruption/model envelope"),
    "2605.25716": ("§3 threat model; §4 scrambled distributed attention; §5 role-aware collaborative RAG", "§6 privacy analysis; §7 latency, network, utility and quantization evaluation", "§8 Discussion; honest-but-curious assumptions and disclosed network/topology boundary"),
    "2605.25798": ("§III cached-token reuse and softmax-threshold mask reuse; §IV hash-distributed hardware", "§V methodology, performance, area/power and high-resolution comparison", "§VII Conclusion; specialized architecture and diffusion-workload simulation boundary"),
    "2605.25820": ("§3.2 visual redundancy; §3.3 redundancy-controlled parallel decoding", "§4 model/benchmark comparison, certainty analysis and ablation", "Appendix A.3 limitations; backbone and multimodal-task scope"),
    "2605.25831": ("§3.1 belief-state construction; §3.2 clarify/abstain/answer strategy", "§4–§7 interaction simulation, accuracy, clarification and faithfulness", "§9 Limitations; simulated-user/judge and dataset ambiguity boundary"),
    "2605.25869": ("§3.1 typed memory atoms; §3.2 multi-route projection; §3.3 provenance-scoped use", "§4 main results, ablation, backbone and hyperparameter analysis", "§5 Conclusion; benchmark/prompt and long-term deployment boundary"),
    "2605.25874": ("§3 multi-turn dataset; §4 world-model evaluation suite", "§5 protocol, per-dimension, cross-dimension and human-alignment results", "§6 Conclusion; Appendix B web-model access and configuration boundary"),
    "2605.25893": ("§3 hesitation signals; §4 cascade monitor and probe routing", "§5 datasets/models, efficiency-effectiveness, robustness and ablation", "Appendix A Limitation; evaluated diffusion models/remasking strategies only"),
    "2605.25954": ("§2 LEIR; §3 verified one-step transformation dataset", "§4 token efficiency, single/multi-step and ablation", "§5 Conclusion; compiler/program set and verification coverage boundary"),
    "2605.25966": ("§3 QAT implementation, LR schedule and factorial/ablation grid", "§4–§5 compute/statistical protocol and schedule×bit-width results", "§6.8 Limitations; sub-100M and tested optimizer/data regime"),
    "2605.25988": ("§3 checker backends and reward; §5 signal collapse; §6 reward-hacking cascade", "§4 main/cross-model results and appendices 9–16", "§8 listed limitations: evaluation independence, seeds, test size, domain and incomplete cascade resolution"),
    "2605.26029": ("§3 interactive SCM environment; §4 parsable causal-trajectory DSL", "§5 mechanism recovery, interventions, scale and verification results", "§8 Limitations; synthetic SCM and benchmark-agent scope"),
    "2605.26046": ("§3 decomposition grid; §5 gradient-specificity and instruction-interference analysis", "§4 results and appendices B–F trajectory/task diagnostics", "§6–§7 conclusion/future work; two datasets and textual-gradient optimizer scope"),
    "2605.26079": ("§2 evidence-collector/auditor; §3 benchmark-quality audit protocol", "§4 fix/manual validation and §5 trajectory audit analysis", "§7 Conclusion; automated auditor false-positive/coverage and sampled-benchmark boundary"),
    "2605.26112": ("§3 harness infrastructure and temporal layers; §4 context/memory/skill bottlenecks", "§5 process/longitudinal evaluation and safe evolution argument", "§6 alternative views and limitations; position/framework paper without controlled deployment study"),
    "2605.26114": ("§3.1 layered state model; §3.2 programmable/serializable state and verifiable outcomes", "§4 protocol; §5 benchmark, sim-to-real, judge error and efficiency", "§6 listed visual/backend/app/legal/misuse limitations"),
    "2605.26177": ("§3 repository perturbations; §4 derived tasks; §5 diagnosis and RepoAnchor", "§2 setup; §3–§5 performance, structural-hint validation and behavior analysis", "Appendix C.1 Limitations; repository/task/model scope"),
    "2605.26184": ("§3 noise model, proxies, online estimation and adaptive controller", "§4 reasoning/code/scale/training-health results and signal ablations", "Appendix B honest covariance assessment; Appendix C idealized stability assumptions; Appendix E overhead"),
    "2605.26200": ("§2 workflow/scientific closure; §3 three collapses; §6 design implications", "§4–§5 survey-coded patterns and remediation analysis", "§8 Limitations; §9 alternative views; survey/position evidence rather than causal experiment"),
    "2605.26252": ("§2 record-abstraction failures; §3 GEM operators/correctness; §4 MemState realization", "§4 prototype feasibility and §5 research agenda", "§6 Conclusion; prototype/vision evidence without comparative production evaluation"),
    "2605.26266": ("§4.1 Jensen attention bias; §4.2 correction; §4.3 cost", "§5 video-diffusion and partial-prefill experiments plus ablations", "§6 Limitations & future work; model/quantizer and partial-prefill transfer boundary"),
    "2605.26269": ("§2 properties/threat model; §3 intent-execution formalization; §4 security games; §5 defenses", "§6–§7 protocol, adversarial advantage, utility and cost", "§8 residual risk; later limitations section and finite task/model envelope"),
    "2605.26289": ("§2 workload/cost; §3 sequence pool, caches, scheduler, speculative decode and streaming validator", "§4–§5 multi-turn/burst/cache latency evaluation", "§6.2 Limitations; single implementation/hardware and prompt-determinism assumptions"),
    "2605.26297": ("§3 trace infrastructure; §4 agent execution; §5 runtime; §6 tool-call characterization", "§7 Evaluation — five agent benchmarks across reasoning/non-reasoning Gemma/Qwen configurations", "§8 Conclusion; benchmark/model/serving-stack characterization boundary"),
    "2605.26298": ("§2 threat model; §3 policy; §4 Landlock/seccomp/network design; §5 implementation", "§6 effectiveness, startup, throughput, COW, network and compatibility", "§8 threat-model/integration/rollback limitations; local Linux host only"),
    "2605.26302": ("§3 aging taxonomy; §4 benchmark; §5 component diagnosis and counterfactual intervention", "§6 setup/results and Appendix D typed-state/controller probes", "§7 Conclusion; synthetic scenarios, closed agents and aging-preview boundary"),
    "2605.26321": ("§2 Anchor; §3 ERP-Bench; Appendix D deterministic generator and E verifier", "§4 evaluation; appendices G–I reliability, failure and validity checks", "§5 Limitations; single ERP domain and generated-artifact scope"),
    "2605.26327": ("§3 full/subspace basis reparameterization and BF16 storage", "§4 five optimizer/memory/runtime experiments", "Appendix C Limitations and Future Work; tested model/optimizer regime"),
    "2605.26329": ("§2 principles, tasks and benchmark construction", "§3 model/scaffold/cost and occupational analysis", "Appendix B limitations, ethics and judge/task coverage"),
    "2605.26340": ("§3 Chain-of-Evidence; §4 literature/discovery/writing/verification workflow; §5 integrity audit", "§6–§7 audit, review, discovery and cross-benchmark generalization", "§9 limitations: coverage, reference depth, automated review, comparison fairness and audit false negatives"),
    "2605.26349": ("§III requirements; §IV semantic/telemetry/cross-modal quality and feedback pipeline", "§V–§VI hardware, framework validation and pilot results", "§VII Conclusion; small pilot/task/teleoperator boundary"),
    "2605.26362": ("§3 SSR/SAS diagnostics; §4 setup; §6 detector transfer", "§5 findings; §6 graph/table/multi-hop generalization and detector comparison", "§8 Limitations; linearization, model and structured-dataset scope"),
    "2605.26384": ("§2 one-second control example; §3 three-tier controller, safety island and PUE-aware control", "§4–§5 real-hardware methodology and multi-tier/multi-country measurements", "§6 Discussion and limitations; tested cluster/grid interface boundary"),
    "2605.26403": ("§3 policy/simulator shift; §4 simulator calibration plus interactive GRPO", "§5 dialogue benchmarks, ablations and simulator-alignment results", "§6 Conclusion; Appendix A assumptions and Appendix B simulator/judge setup"),
    "2605.27091": ("§3.2 sampling-failure bound; §3.3 conformal selection; §3.4 combined guarantee", "§4 finite-sampling, conditional-selection and overall-miscoverage experiments", "Appendix A conditional exchangeability and population-bound assumptions"),
    "2605.27461": ("§II hardware/software; §III execution; §IV data collection and training loop", "§V results and §VI deployment failures/lessons", "§VII Conclusion; one factory task, 2,535 episodes and no cross-site generality"),
    "2605.28873": ("§3 paired MDE bound; §4 quantization/benchmark/scoring protocol", "§5 pilot audit and §6 interpretation", "§9 Limitations; QRI is descriptive, small NF4 pilot and prompt confounding"),
}

# Provisional Integrate is intentionally narrower than the denominator. The
# independent reviewer must still challenge every owner+adjacent comparison.
INTEGRATE = {
    "2605.25375", "2605.25376", "2605.25379", "2605.25422", "2605.25424",
    "2605.25475", "2605.25492", "2605.25535", "2605.25550", "2605.25624",
    "2605.25632", "2605.25641", "2605.25653", "2605.25673", "2605.25674",
    "2605.25698", "2605.25704", "2605.25716", "2605.25831", "2605.25869",
    "2605.25874", "2605.25893", "2605.25988", "2605.26029", "2605.26079",
    "2605.26114", "2605.26184", "2605.26252", "2605.26269", "2605.26289",
    "2605.26297", "2605.26298", "2605.26302", "2605.26321", "2605.26327",
    "2605.26340", "2605.26384", "2605.26403", "2605.27091", "2605.28873",
}

DEEP = {
    "2605.26114": "DA-STATE-PROGRAMMABLE-ENVIRONMENT",
    "2605.26252": "DA-GOVERNED-EVOLVING-MEMORY",
    "2605.26289": "DA-STATEFUL-AGENT-INFERENCE",
}

ledger = json.loads((HERE / "screening-ledger-final.json").read_text())
retained = [
    r
    for r in ledger["identities"]
    if r.get("candidate_state") == "retained" or r.get("screening_status") == "retained"
]
assert len(retained) == 66
assert set(LOC) == {r["arxiv_id"] for r in retained}

candidates = {}
for row in retained:
    aid = row["arxiv_id"]
    if aid == "2605.25451":
        disposition, total = "Blocked / Unverified", 8
    elif aid in INTEGRATE:
        disposition, total = "Integrate", 8
    else:
        disposition, total = "No Change — Existing Coverage", 7
    candidates[aid] = [row["owner_node"], total, disposition, *LOC[aid]]

(HERE / "candidate-config-author.json").write_text(json.dumps({
    "candidates": candidates,
    "deep": DEEP,
    "pdf_ids": ["2605.25451"],
}, ensure_ascii=False, indent=2) + "\n")

template = HERE.parent / "daily-20260525" / "render_author_packet.py"
code = template.read_text()
code = code.replace("2026-05-24", "__WINDOW_START__")
code = code.replace("2026-05-25", "2026-05-26")
code = code.replace("__WINDOW_START__", "2026-05-25")
code = code.replace("2026-W21", "2026-W22")
code = code.replace("papers/2026/05/25/README.md", "papers/2026/05/26/README.md")
analysis = {
    "2605.26114": "真实设备或完整模拟器在交互保真度最高时合理，但它们难以提供可并行复制、可编程且可逐状态验证的训练环境。MobileGym 把环境状态从截图副产品提升为可序列化、可比较的控制面，使任务生成、reward 验证、并行副本和 sim-to-real 检查共享同一状态契约。收益是可扩展且可证伪的环境训练；代价是视觉/backend/动态内容保真度和模拟器维护成本，作者结果不能证明任意应用都可被等价模拟。",
    "2605.26252": "把长期记忆视为向量或记录集合，在短会话、只追加和人工清理条件下足够简单；跨月运行引入修订、遗忘、依赖传播和读取后改写后，正确性属于整条状态轨迹。GEM 将 ingestion、revision、forgetting、retrieval 定义为受治理的状态算子，使 memory substrate 而非生成模型拥有演化不变量。收益是可审计和可维护，代价是依赖图、冲突处理、迁移及垃圾回收成本；MemState 只证明原型可行，未证明生产规模性能。",
    "2605.26289": "把每次工具调用当独立请求，在短 prompt、低复用和无长期会话时边界清楚；多 Agent 重复进入模型且上下文持续增长后，反复 render/tokenize/prefill 成为主要浪费。该架构让 sequence pool 持有跨轮 KV、render、token、response 与验证状态，调度器只提交变化部分。收益是降低重复前缀成本和 burst latency，代价是生命周期、隔离、失效、determinism 与缓存一致性复杂度；单一实现和硬件结果不能外推为普遍加速。",
}
replacement = "analysis_text = " + repr(analysis) + "\nfor arxiv_id"
code = re.sub(r"analysis_text = \{.*?\n\}\nfor arxiv_id", replacement, code, flags=re.S)
exec(compile(code, str(HERE / "_shared_renderer_20260526.py"), "exec"), {"__file__": str(HERE / "render_author_packet.py"), "__name__": "__main__"})

# Correct the one exact-v1 access blocker without turning a transient network
# failure into a month-wide evidence gap.
sf = "SF-2026-ARXIV-2605-25451"
packet_path = HERE / "exact-v1-review-packet.json"
packet = json.loads(packet_path.read_text())
for item in packet:
    if item["source_family_id"] == sf:
        item.update(
            retrieval_route="official arXiv abstract accessible; exact-v1 HTML/PDF body unavailable after direct and official-web retry",
            access_status="blocked",
            review_status="blocked",
            claim_boundary="Only identity, date, title and abstract are verified. Method, evaluation, limitations and Books mechanism remain unverified.",
        )
packet_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")

report = Path(__file__).resolve().parents[5] / "papers/2026/05/26/README.md"
text = report.read_text()
text = text.replace("DEN-20260525-V2-AUTHOR", "DEN-20260526-V2-AUTHOR")
text = text.replace("GAP-20260525-INDEPENDENT-AUDIT", "GAP-20260526-INDEPENDENT-AUDIT")
text = text.replace("coverage:SRC-ARXIV:20260525", "coverage:SRC-ARXIV:20260526")
text = text.replace("SA-20260525-", "SA-20260526-")
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith(f"| {sf} |") and "| retained |" in line:
        lines[i] = line.replace("| deep_complete | accessible |", "| blocked | blocked |")
    if line.startswith(f"| {sf} | RP-"):
        lines[i] = line.rsplit("| complete |", 1)[0] + "| blocked |"
text = "\n".join(lines) + "\n"
text = text.replace(
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n\n## 12. Sources",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
    "| MR-20260526-2605-25451 | P1 Full Text | SF-2026-ARXIV-2605-25451 | — | — | 2026-W22 | arXiv:2605.25451v1; https://arxiv.org/abs/2605.25451v1 | Exact-v1 paper body, including BigMac method, training setup, evaluation tables and limitations | Abstract confirms identity and headline but cannot establish compute/memory ownership, benchmark conditions or counterevidence | Event-time v1 PDF, TeX source, or author-hosted exact-v1 HTML/TXT | 2605.25451v1.pdf | Full Method/Evaluation/Limitations review, Score confirmation and Books comparison |\n\n## 12. Sources"
)
text = text.replace("exact-v1 author reviews=66/66，blocked=0", "exact-v1 author reviews=65/66，blocked=1")
text = text.replace("reviewed=66，blocked=0", "reviewed=65，blocked=1")
report.write_text(text)

# Keep machine artifacts aligned with the canonical report.
final_ledger = json.loads((HERE / "screening-ledger-final.json").read_text())
for row in final_ledger["identities"]:
    if row.get("arxiv_id") == "2605.25451":
        row.update(review_status="blocked", access_status="blocked", integration_disposition="Blocked / Unverified")
(HERE / "screening-ledger-final.json").write_text(json.dumps(final_ledger, ensure_ascii=False, indent=2) + "\n")

audit = json.loads((HERE / "semantic-author-audit.json").read_text())
audit["counts"]["reviewed"] = 65
audit["counts"]["blocked"] = 1
audit["unresolved_findings"] = [
    "Different reviewer must perform the fresh-context denominator/evidence/selection/Books audit.",
    "SF-2026-ARXIV-2605-25451 lacks the exact-v1 full body; precise material request is recorded.",
    "Root serial Books writeback and post-write semantic audit are pending.",
]
(HERE / "semantic-author-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"registered": 587, "screened": 587, "retained": 66, "closures": 521, "exact_v1_complete": 65, "blocked": 1, "provisional_integrate": len(INTEGRATE)}, ensure_ascii=False))
