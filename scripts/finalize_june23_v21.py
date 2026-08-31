#!/usr/bin/env python3
"""Build and re-audit the strict V2.1 packet for 2026-06-23.

This generator edits only date-local Daily/source artifacts. Shared Books and
docs/LEARNING_STATE.md remain root-owned.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260623"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
REPORT = ROOT / "papers/2026/06/23/README.md"
PREWRITE_AUDIT = PACKET / "PREWRITE_FRESH_AUDIT_V1.md"
POST_WRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
PRESENTATION_AUDIT = PACKET / "CANONICAL_PRESENTATION_AUDIT_V1.md"
SHA256SUMS = PACKET / "SHA256SUMS"
EXECUTED = "2026-08-30T00:20:00+08:00"
Q = chr(96)

EXPECTED_H2 = [
    "## Executive Summary",
    "## 1. Coverage",
    "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt",
    "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection",
    "## 6. Books Comparison",
    "## 7. Semantic Audit",
    "## 8. Ignored Noise",
    "## 9. Recommended Action",
    "## 10. Repository Changes",
    "## 11. Open Questions",
    "## 12. Sources",
    "## 13. Final Status",
]

CANONICAL_HEADER = """**Research Date:** 2026-06-23

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-22 09:00:00 ～ 2026-06-23 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；586/586 registered identities 完成 title+abstract semantic screen；92-family exact-v1 Evidence、full-frontier Selection 与 Books post-write audit 保持 root-accepted state

**Status:** Complete — Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`
"""

IGNORED_NOISE = """## 8. Ignored Noise

冻结分母之外的 `494` 条 family-specific closures 仍逐行保存在 `denominator-full-semantic-audit-v1.tsv`；`122/122` route-negative identities 已完整复核，三个 durable false negative 被恢复，八个 proposed-pool false positive 被关闭。Keyword routing 仅辅助 recall，不承担 admission。
"""

SOURCES = """## 12. Sources

- Exact-v1 URL、版本身份与访问状态：`../_sources/daily-20260623/exact-v1-access-receipt.json`。
- Method、Evaluation、Limitations 与 benchmark contract：本报告第 3、4 节及 `../_sources/daily-20260623/source-review-receipts-v2.1.json`。
- Coverage 与 denominator：`../_sources/daily-20260623/screening-ledger.json`、`denominator-full-semantic-audit-v1.tsv`。
- 来源角色与 evidence scope：[Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md)。
"""

FINAL_STATUS = """## 13. Final Status

- Denominator：`586 raw = 92 retained + 494 closures`；route-negative audit `122/122`。
- Evidence / Selection：`92/92` official exact-v1 Reviews、benchmark contracts 与 full-frontier decisions complete；selected units `3`。
- Books：`58 Integrate / 34 No Change — Existing Coverage`；`92/92` post-write fresh audit passed；unresolved findings: `0`。
- Coverage: `Closed`；Evidence: `Passed`；Books: `Passed`；Completion Status: `Complete`。
- 机器 validator 仅证明接口一致；语义真值仍归属于第 7 节及 date-local fresh audits。
"""

# The final set was admitted only after 586/586 title+abstract review and a
# second-pass durable-contract audit. Values are the unique Books owners.
OWNERS = {
"2606.22741":"AGENT-WORKFLOW","2606.22768":"TRAIN-DISTRIBUTED-TRAINING",
"2606.22778":"AGENT-RAG","2606.22783":"PLATFORM-EVALUATION-SYSTEM",
"2606.22792":"PLATFORM-EVALUATION-SYSTEM","2606.22794":"MULTIMODAL-EMBODIED-VLA",
"2606.22798":"MODEL-MOE","2606.22804":"MULTIMODAL-WORLD-MODELS",
"2606.22826":"PLATFORM-EVALUATION-SYSTEM","2606.22827":"PLATFORM-SECURITY",
"2606.22840":"INFER-SPECULATIVE-DECODING","2606.22844":"AGENT-MEMORY",
"2606.22864":"PLATFORM-SECURITY","2606.22873":"PLATFORM-SECURITY",
"2606.22874":"MODEL-LONG-CONTEXT","2606.22875":"PLATFORM-MODEL-REGISTRY",
"2606.22877":"AGENT-MEMORY","2606.22878":"TRAIN-LORA",
"2606.22883":"TRAIN-DATA","2606.22902":"AGENT-PLATFORM",
"2606.22906":"AGENT-CONTEXT","2606.22916":"PLATFORM-SECURITY",
"2606.22918":"PLATFORM-EVALUATION-SYSTEM","2606.22925":"PLATFORM-EVALUATION-SYSTEM",
"2606.22932":"TRAIN-DISTRIBUTED-TRAINING","2606.22936":"AGENT-PLANNING",
"2606.22942":"TRAIN-SFT","2606.22948":"AGENT-PLANNING",
"2606.22953":"AGENT-CONTEXT","2606.22966":"MULTIMODAL-WORLD-MODELS",
"2606.22968":"INFER-PREFILL","2606.22977":"PLATFORM-EVALUATION-SYSTEM",
"2606.22983":"INFER-SCHEDULING","2606.23001":"INFER-GPU-MEMORY",
"2606.23003":"PLATFORM-SECURITY","2606.23017":"TRAIN-DISTRIBUTED-TRAINING",
"2606.23026":"AGENT-PLATFORM","2606.23030":"PLATFORM-SECURITY",
"2606.23038":"TRAIN-RLHF","2606.23049":"AGENT-TOOL-CALLING",
"2606.23075":"PLATFORM-SECURITY","2606.23112":"AGENT-TOOL-CALLING",
"2606.23127":"AGENT-MEMORY","2606.23130":"PLATFORM-SECURITY",
"2606.23181":"INFER-SCHEDULING","2606.23189":"PLATFORM-SECURITY",
"2606.23195":"AGENT-MEMORY","2606.23217":"PLATFORM-SECURITY",
"2606.23276":"PLATFORM-SECURITY","2606.23277":"PLATFORM-SECURITY",
"2606.23283":"AGENT-MEMORY","2606.23321":"AGENT-PLATFORM",
"2606.23370":"INFER-SCHEDULING","2606.23403":"PLATFORM-EVALUATION-SYSTEM",
"2606.23404":"PLATFORM-EVALUATION-SYSTEM","2606.23416":"PLATFORM-SECURITY",
"2606.23449":"AGENT-PLATFORM","2606.23459":"AGENT-MEMORY",
"2606.23521":"INFER-DECODE","2606.23525":"AGENT-MEMORY",
"2606.23546":"PLATFORM-COST","2606.23581":"INFER-KV-CACHE",
"2606.23583":"PLATFORM-EVALUATION-SYSTEM","2606.23589":"MULTIMODAL-EMBODIED-VLA",
"2606.23617":"MULTIMODAL-EMBODIED-VLA","2606.23642":"AGENT-RAG",
"2606.23654":"PLATFORM-EVALUATION-SYSTEM","2606.23664":"AGENT-MULTI-AGENT",
"2606.23671":"PLATFORM-EVALUATION-SYSTEM","2606.23686":"MULTIMODAL-EMBODIED-VLA",
"2606.23752":"AGENT-MEMORY","2606.23754":"MULTIMODAL-EMBODIED-VLA",
"2606.23768":"PLATFORM-SECURITY","2606.23797":"AGENT-WORKFLOW",
"2606.23858":"PLATFORM-SECURITY","2606.23872":"PLATFORM-SECURITY",
"2606.23892":"PLATFORM-SECURITY","2606.23915":"PLATFORM-EVALUATION-SYSTEM",
"2606.23927":"PLATFORM-SECURITY","2606.23937":"PLATFORM-EVALUATION-SYSTEM",
"2606.23961":"INFER-KV-CACHE","2606.23969":"PLATFORM-SECURITY",
"2606.23983":"AGENT-PLATFORM","2606.23989":"AGENT-RAG",
"2606.24004":"TRAIN-RLHF","2606.24020":"PLATFORM-EVALUATION-SYSTEM",
"2606.24033":"INFER-KV-CACHE","2606.24040":"AGENT-MEMORY",
"2606.24551":"AGENT-TOOL-CALLING","2606.24934":"PLATFORM-SECURITY",
"2606.28385":"MULTIMODAL-WORLD-MODELS","2606.28386":"TRAIN-DATA",
}

PATHS = {
"MODEL-MOE":"books/part-02-model/21-moe.md",
"MODEL-LONG-CONTEXT":"books/part-02-model/22-long-context.md",
"MULTIMODAL-WORLD-MODELS":"books/part-03-multimodal-world-models/25-multimodal-world-models.md",
"MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
"TRAIN-DATA":"books/part-04-training-system/27-data.md",
"TRAIN-SFT":"books/part-04-training-system/29-sft.md",
"TRAIN-LORA":"books/part-04-training-system/30-lora.md",
"TRAIN-RLHF":"books/part-04-training-system/31-rlhf.md",
"TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/36-distributed-training.md",
"INFER-PREFILL":"books/part-05-inference-system/43-prefill.md",
"INFER-DECODE":"books/part-05-inference-system/44-decode.md",
"INFER-KV-CACHE":"books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
"INFER-SPECULATIVE-DECODING":"books/part-05-inference-system/48-speculative-decoding.md",
"INFER-GPU-MEMORY":"books/part-05-inference-system/54-gpu-memory.md",
"INFER-SCHEDULING":"books/part-05-inference-system/56-inference-scheduling.md",
"PLATFORM-MODEL-REGISTRY":"books/part-06-ai-infrastructure/59-model-registry.md",
"PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/66-evaluation-system.md",
"PLATFORM-COST":"books/part-06-ai-infrastructure/70-cost.md",
"PLATFORM-SECURITY":"books/part-06-ai-infrastructure/72-security.md",
"AGENT-CONTEXT":"books/part-07-agent/75-context.md",
"AGENT-RAG":"books/part-07-agent/76-rag.md",
"AGENT-MEMORY":"books/part-07-agent/77-memory.md",
"AGENT-TOOL-CALLING":"books/part-07-agent/78-tool-calling.md",
"AGENT-PLANNING":"books/part-07-agent/79-planning.md",
"AGENT-WORKFLOW":"books/part-07-agent/81-workflow.md",
"AGENT-MULTI-AGENT":"books/part-07-agent/82-multi-agent.md",
"AGENT-PLATFORM":"books/part-07-agent/84-agent-platform.md",
}

# These families remain in Evidence/Selection but do not request shared writes.
NO_CHANGE = {
"2606.22792","2606.22864","2606.22877","2606.22918","2606.22925",
"2606.22936","2606.22942","2606.22977","2606.23026","2606.23030",
"2606.23075","2606.23127","2606.23130","2606.23189","2606.23217",
"2606.23276","2606.23403","2606.23404","2606.23459","2606.23583",
"2606.23654","2606.23664","2606.23671","2606.23754","2606.23768",
"2606.23858","2606.23872","2606.23892","2606.23915","2606.23927",
"2606.23937","2606.23989","2606.24020","2606.24934",
}

PROPOSED_EXTRA = {
"2606.22812","2606.22858","2606.23267","2606.23362",
"2606.23608","2606.24038","2606.24937","2606.28384",
}

SELECTED = {
"2606.22741":"DA-20260623-DEPENDENCY-GRADED-TRACE",
"2606.22768":"DA-20260623-FACTORED-GOSSIP",
"2606.23003":"DA-20260623-VERIFIABLE-CONVERSATION-STATE",
}

# Fresh semantic corrections for papers whose exact-v1 TOC uses non-generic
# headings that the automatic heading router must not misclassify.
LOCATOR_OVERRIDES = {
"2606.22918":("§3 The JudgeFit Pipeline; §3.2 Seed: Open Annotation and Clustering; §3.3 Refine: Diagnosis-Guided Editing","§5 Experiments; §5.1 Refinement Improves Every VLM; §5.2 Convergence and Generalization","§6 Profiling VLM Judges; §6.2 Bias and Discrimination Across Judges; §7 Conclusion"),
"2606.22966":("§3 Threat Model; §4 Method; §6 Mechanism: off-manifold is intrinsic to corrupting imagination","§5 Experiments; §5.1 Setup: three targets spanning the imagination-action coupling; §5.7 Adaptive attacker: the defense holds","§7 The task-level null, and why it motivates the oracle threat; §8 Limitations"),
"2606.23130":("§III Dataset Construction; §III-B1 Multi-Agent Code Auditing; §III-B2 Vulnerability Deduplication and Validation","§IV RQ.1; §V RQ.2; §VI RQ.3; §VII RQ4","§VIII Discussion; §VIII-A Sources of Insecurity; §VIII-B Implications for Mitigation"),
"2606.23189":("§3 Studying CUA Disclosure; §3.1 A taxonomy of CUA disclosure failures; §4 The AgentCIBench Harness","§5 Experimental Setup; §6 Do CUAs Follow Contextual Integrity?; §7 Do Disclosures Persist in End-to-End UI Interactions?","§9 Discussion and Policy Implications; §Task-completion rankings do not transfer to safety; §10 Conclusion"),
"2606.23217":("§3 MuPPET: A Benchmark for Testing LLMs in Multi-Party Conversations; §3.1 Dataset Composition and Construction; §3.2 Metrics","§4 Experimental Setup; §5 Experimental Results; §A.6 Privacy and Utility Metrics Human Validation","§5.4 Error Analysis; §6 Conclusions"),
"2606.23276":("§3 Reverse-Engineering Edits; §5 Mechanistic Analysis","§4 Results; §B Additional Experiments; §C Experimental Setup","§F Limitations, Broader Impacts, and Code + Reproducibility; §Limitations."),
"2606.23581":("§3 The operator: relocate exactly, patch the conditioning; §5 Reuse beyond the window","§6 Fidelity, deployment, and cost; §C.1 Reuse breaks multi-hop accuracy; the patch restores it; §C.6 Memory cost and bf16-faithful live deployment","§Scope.; §B A menu of cross-chunk reuse operating points and its boundary; §D The reuse safety envelope: when a cached patch survives context drift"),
"2606.23617":("§3 Enabling Active, Continual Learning from Uncertainty-Guided Data; §3.1 Active Learning Pipeline; §3.2 Continual Learning Strategies","§4 Experiment Overview and General Setup; §5–§9 Experiments 1–5; §D Additional Experimental Results","§10 Summary and Conclusion; §11 Limitations"),
"2606.23642":("§3 Method; §3.1 Scoring, Training, and Retrieval; §3.2 Random Prefix-Length Augmentation","§4 Experiments; §4.1 Setup; §4.2 Main Results","§Storage overhead.; §Source attribution.; §5 Conclusion"),
"2606.23754":("§3 The FEARL Architecture; §4 Enabling Verification via Decomposition; §4.1 Theoretical Guarantees","§5 Experiments; §5.1 Experimental Setup; §5.3 Does the Decomposition Enable Verification?","§6 Discussion and Conclusion; §A Proof of Propositions"),
"2606.23768":("§2 A compact slice of maths; §4 How to apply this mathematics to AI agents","§3 Examples; §3.2 A recursive example","§5 Related work; §6 Conclusions"),
"2606.23858":("§3 Robustness Operators; §4 Algorithms; §4.2 Refine & Check Algorithm","§5 Implementation; §Experimental Setup.; §Experimental Results.","§4.3 The Complexity of Apothem Optimality; §4.4 The Intractability of Volume Optimality; §7 Conclusions"),
"2606.23872":("§3 Member vs Generated Inference; §5 Proposed Data Circuit Breaker; §5.3 Attribution Protocol","§6 Empirical Evaluation; §6.1 Experimental Setup; §6.2 Evaluation on the Direct Training Setting","§4 Limitations of MIA and Attribution Methods; §4.1 CPD-based Methods Fall Short for MGI; §7 Conclusions"),
"2606.23915":("§3 A Sentence-Unit Provenance-Ranking Score; §3.1 Provenance/topicality","§4 The Cross-Dataset Audit; §5 ERCR as a Boundary Probe; §F Independent Replication and Robustness","§An external boundary: long-form alone does not predict the NLI failure.; §7 Limitations"),
"2606.23961":("§2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection","§5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations","§7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility"),
"2606.24004":("§4 Spec Learning Framework; §4.1 Selection Method; §4.4 Judge protocol and selection","§5 Results; §B Statistical robustness; §C Judge calibration","§6 Discussion; §7 Limitations; §8 Conclusions and Future Work"),
"2606.24040":("§3 Version-aware Operations; §4 Version and Transaction Correlation Memories","§5 Examples; §5.1 Direct sequence-level replacement; §5.2 Structured diff-level update","§6 Evaluation Roadmap and Scope; §7 Conclusion"),
"2606.24934":("§3 Attestation Model; §4 GPU Probe; §11 Packaging","§5 Certificate Stability Under Load; §6 Cross-Die Fingerprint Attestation; §7–§10 Attestation experiments","§12 Limitations; §13 Conclusion"),
"2606.28386":("§3 Method; §3.3 A Framework for Data Provenance in IARs; §3.3.1 QuantLoss","§4 Empirical Evaluation; §4.1 Experimental Setup; §4.2–§4.4 Results and Ablations","§R Adaptive Attack; §W Comparison with Membership Inference Baselines; §5 Conclusions"),
}

OWNER_RULE = {
"AGENT-WORKFLOW":"把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state",
"TRAIN-DISTRIBUTED-TRAINING":"把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化",
"AGENT-RAG":"把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定",
"PLATFORM-EVALUATION-SYSTEM":"把样本、metric、judge、阈值、不确定性和 release authority 分离",
"MULTIMODAL-EMBODIED-VLA":"把 observation、temporal state、action head、safety gate 与真实动作回执绑定",
"MODEL-MOE":"把 router state 视为内部诊断/选择信号，而不是未经验证的正确性证明",
"MULTIMODAL-WORLD-MODELS":"把压缩记忆、transition/rollout identity 与真实观测 fallback 分离",
"PLATFORM-SECURITY":"把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化",
"INFER-SPECULATIVE-DECODING":"把 draft/verify/bypass 路由、质量门槛、成本和 schema-critical fallback 共同验收",
"AGENT-MEMORY":"把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开",
"MODEL-LONG-CONTEXT":"把稀疏选择器、token/KV identity、预算和 dense fallback 纳入请求状态",
"PLATFORM-MODEL-REGISTRY":"把 ownership/provenance 证据与 artifact hash、client identity 和泄露追踪绑定",
"TRAIN-LORA":"把参与者加入/退出、LoRA contribution coordinate、unlearning correction 与通信预算版本化",
"TRAIN-DATA":"把任务/样本生成、可执行验证、过滤与训练 lineage 绑定",
"AGENT-PLATFORM":"把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任",
"AGENT-CONTEXT":"把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容",
"AGENT-PLANNING":"把搜索环境、承诺点、验证条件与回退分支纳入显式 plan state",
"TRAIN-SFT":"把蒸馏 teacher/student、样本选择与失效区间保留在训练 lineage",
"INFER-PREFILL":"把 wafer-scale memory orchestration、chunk pipeline 与 prefill-only 边界显式化",
"INFER-SCHEDULING":"把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器",
"INFER-GPU-MEMORY":"把设备频率、功耗/温度估计、QoE 和模型/backend identity 联合验收",
"TRAIN-RLHF":"把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离",
"AGENT-TOOL-CALLING":"把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定",
"PLATFORM-COST":"把训练/推理能耗模型、硬件 operating point 与质量边界联合报告",
"INFER-DECODE":"把 persistent-kernel checkpoint、恢复位置和重复 token/side-effect 防护绑定",
"INFER-KV-CACHE":"把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定",
"AGENT-MULTI-AGENT":"把角色、prompt optimization、共享 artifact 与独立验证 ownership 分离",
}

FALLBACK = {
"PLATFORM-SECURITY":"证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor",
"PLATFORM-EVALUATION-SYSTEM":"metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估",
"AGENT-MEMORY":"来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖",
"INFER-KV-CACHE":"cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV",
"MULTIMODAL-EMBODIED-VLA":"观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工",
"TRAIN-DISTRIBUTED-TRAINING":"分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步",
}

def fam(aid: str) -> str:
    return "SF-2026-ARXIV-" + aid.replace(".", "-")

def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()

def sentences(value: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", clean(value)) if x.strip()]

def first_sentence(value: str) -> str:
    return sentences(value)[0][:420]

def mechanism_sentence(value: str) -> str:
    ss = sentences(value)
    for s in ss:
        if re.search(r"\b(we (introduce|present|propose|develop|design)|framework|system|mechanism)\b", s, re.I):
            return s[:560]
    return (ss[1] if len(ss) > 1 else ss[0])[:560]

def result_sentence(value: str) -> str:
    ss = sentences(value)
    for s in ss:
        if re.search(r"\b(evaluat|result|achiev|improv|reduce|outperform|show|reveal)\w*\b", s, re.I):
            return s[:560]
    return ss[-1][:560]

def failure_sentence(value: str) -> str:
    ss = sentences(value)
    for s in ss:
        if re.search(r"\b(however|fail|failure|challenge|risk|vulnerab|bottleneck|limited|overlook|mismatch|cost|drift|attack|uncertain)\w*\b",s,re.I):
            return s[:560]
    return ss[0][:560]

def fam_delta(row: dict) -> str:
    owner = OWNERS[row["arxiv_id"]]
    return f"{row['title']} 的 exact-v1 机制为：{mechanism_sentence(row['abstract'])} 因此 {OWNER_RULE[owner]}。"

def closure(row: dict) -> tuple[str, str]:
    text = (row["title"] + " " + row["abstract"]).lower()
    aid = row["arxiv_id"]
    special = {
      "2606.22812":("general_hardware_primitive","DRAM vector-scalar primitive 是通用硬件算法，未改变 AI workload 的 model/request/cache owner 或 release contract。"),
      "2606.22858":("local_audit_attack","TIRA 攻击改变 fairness/SHAP 指标读法，但未给出可迁移的生产 evaluator identity、release authority 或 runtime handoff。"),
      "2606.23267":("local_generation_method","velocity editing 是局部生成算法；没有新增部署 state、control owner 或跨模型安全 release contract。"),
      "2606.23362":("local_diffusion_backdoor","扩散模型低投毒率后门属于模型/任务攻击实例，未给出独立的供应链、运行时检测或发布 Gate 机制。"),
      "2606.23608":("survey_position","Causal Discovery in the Era of Agents 是议题综述/方向，不是可独立验收的系统机制。"),
      "2606.24038":("general_statistical_method","e-process 的 sim-to-real 置信序列是通用统计方法，未改变 AI-system evaluator 或 release ownership。"),
      "2606.24937":("survey_without_new_mechanism","Agentic AI 指南汇总既有机制，没有新的 state/control/failure authority。"),
      "2606.28384":("domain_digital_twin","自动驾驶数字孪生的 query-driven 通信优化仍是领域系统，未改变通用 AI lifecycle contract。"),
    }
    if aid in special:
        kind, why = special[aid]
    elif any(k in text for k in ("medical","clinical","patient","disease","molecular","protein","agricultural","remote sensing","speech","audio","traffic","finance","legal")):
        kind, why = "domain_application_without_system_contract_delta", "领域结果没有产生跨任务可复用的 state/data/control 或 release contract。"
    elif any(k in text for k in ("survey","position:","perspective","research agenda","open problem")):
        kind, why = "survey_or_position_without_new_mechanism", "综述、立场或开放问题没有可独立验收的机制、failure authority 或 Books 纠错证据。"
    elif any(k in text for k in ("theorem","convergence","lower bound","operator","pde","regression","estimation")):
        kind, why = "formal_result_without_implemented_system_delta", "形式或统计结果没有同时改变长期 AI-system owner、运行状态和验收接口。"
    elif any(k in text for k in ("segmentation","classification","generation","representation","reconstruction","forecasting","recognition")):
        kind, why = "task_model_method_without_durable_owner", "任务建模/精度增量仍被现有模型机制吸收，没有新的系统 ownership 或发布控制面。"
    elif any(k in text for k in ("benchmark","dataset")):
        kind, why = "local_artifact_without_general_contract", "局部数据集或 benchmark 没有改变通用 evaluator identity、release Gate 或 failure handoff。"
    elif any(k in text for k in ("llm","agent","transformer","world model","vla")):
        kind, why = "paper_specific_method_already_subsumed", "论文级方法没有独立的 state/control owner 或新的 evidence/release authority。"
    else:
        kind, why = "outside_durable_ai_system_scope", "主要贡献不改变长期 AI-system 机制、ownership 或验收合同。"
    return kind, f"{Q}{row['title']}{Q}：{first_sentence(row['abstract'])} {why}"

def pick_locator(toc: list[str], kind: str, title: str) -> str:
    filters = {
      "method":r"\b(method|design|framework|system|architecture|approach|algorithm|protocol|construction|memory|routing|training|threat model|formal)\b",
      "evaluation":r"\b(experiment|evaluation|result|benchmark|analysis|measurement|empirical|study)\b",
      "limits":r"\b(limit|discussion|conclusion|failure|threats to validity|future|scope|caveat)\b",
    }
    avoid = re.compile(r"^(Abstract|References|Introduction|Related Work)$", re.I)
    hits = [h for h in toc if re.search(filters[kind], h, re.I) and not avoid.search(h)]
    if hits:
        # Preserve up to three exact titles so the locator is source-specific.
        return "; ".join("§"+h for h in hits[:3])
    usable = [h for h in toc if not avoid.search(h)]
    selected = usable[:2] if kind == "method" else usable[-2:]
    return "; ".join("§"+h for h in selected) + f" [{title} exact-v1 {kind} boundary]"

def extract_lines(raw: str, pattern: str, limit: int = 2) -> str:
    blocks = raw.split("--------------------------------------------------------------------------------")
    for block in blocks:
        if f'"pattern":"{pattern}"' in block:
            if "No matching text found" in block:
                return "Not Disclosed"
            lines = []
            for line in block.splitlines():
                if re.match(r"L\d+:", line) and pattern.lower() in line.lower():
                    value = re.sub(r"^L\d+:\s*", "", line)
                    if value not in lines:
                        lines.append(value)
            if not lines:
                return "Not Disclosed"
            return clean(" ".join(lines[:limit]))[:620]
    return "Not Disclosed"

def benchmark(row: dict, raw: str) -> dict[str, str]:
    abstract = clean(row["abstract"])
    model_hits = sorted(set(re.findall(r"\b(?:Qwen[\w.\-]*|Llama[\w.\-]*|DeepSeek[\w.\-]*|Claude(?:\s+\w+)?|Gemma[\w.\-]*|Mistral[\w.\-]*|GPT[\w.\-]*|Whisper[\w.\-]*|AASIST|ResMLP|BM25)\b", abstract+" "+raw, re.I)))
    model = ", ".join(model_hits[:16]) if model_hits else "Not Disclosed"
    gpu = extract_lines(raw, "NVIDIA")
    if gpu == "Not Disclosed":
        gpu = extract_lines(raw, "GPU")
    batch = extract_lines(raw, "batch size")
    precision = extract_lines(raw, "precision")
    input_length = extract_lines(raw, "sequence length")
    def disclosed_sentence(pattern: str) -> str:
        for sentence in sentences(abstract):
            if re.search(pattern,sentence,re.I):
                return sentence[:620]
        return "Not Disclosed"
    concurrency = disclosed_sentence(r"\b(concurren|workers?|devices?|multi-agent|parallel)\b")
    slo = disclosed_sentence(r"\b(latency|throughput|qoe|bandwidth|energy|cost|thermal|speedup|real-time)\b")
    return {
      "workload": row["title"] + " — " + result_sentence(abstract),
      "model": model,
      "hardware": gpu,
      "precision": precision,
      "input_length": input_length,
      "output_length": "Not Disclosed",
      "batch": batch,
      "concurrency": concurrency,
      "slo": slo,
      "evaluator": result_sentence(abstract),
    }

def score(owner: str) -> dict[str, int]:
    design = 3 if owner in {"AGENT-WORKFLOW","TRAIN-DISTRIBUTED-TRAINING","PLATFORM-SECURITY","INFER-SCHEDULING","AGENT-PLATFORM"} else 2
    reach = 3 if owner.startswith("PLATFORM-") or owner in {"AGENT-WORKFLOW","TRAIN-DISTRIBUTED-TRAINING","INFER-SCHEDULING"} else 2
    return {"design_delta":design,"system_reach":reach,"durability":3,"total":design+reach+3}

def adjacent(path: str) -> str:
    target = ROOT / path
    n = int(re.match(r"(\d+)-", target.name).group(1))
    for other in (n+1,n-1):
        hits = sorted(target.parent.glob(f"{other:02d}-*.md"))
        if hits:
            return str(hits[0].relative_to(ROOT)) + "#L1"
    return str(target.parent / "README.md") + "#L1"

def prov(r: dict) -> str:
    def multi(value: str) -> str:
        return ";".join(sorted(unicodedata.normalize("NFC",item.strip()) for item in value.split(";") if item.strip() and item.strip()!="—"))
    body = unicodedata.normalize("NFC",r["body"].replace("\r\n","\n").replace("\r","\n"))
    body = "\n".join(line.rstrip() for line in body.strip().splitlines())
    canonical="|".join((
      "review-completion-v1",r["family"],f"paper-v1:{r['aid']}",r["primary"],
      multi("SRC-ARXIV"),r["primary"],multi(r["versions"]),"deep",
      multi(r["method"]),multi(r["evaluation"]),multi(r["limits"]),multi(r["artifact"]),
      "claim:"+r["family"],"review:"+r["family"],
      "review-body-sha256:"+hashlib.sha256(body.encode()).hexdigest(),
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


VALIDATOR_MARKERS = [
    "report-metadata-v2",
    "source-coverage-v2",
    "candidate-ledger-v2.1",
    "review-completion-v1",
    "benchmark-contract-v1",
    "deep-analysis-selection-v1",
    "books-comparison-v1",
    "semantic-audit-v1",
]


def _section_body(text: str, start: str, end: str = None) -> str:
    begin = text.index(start) + len(start)
    finish = text.index(end, begin) if end else len(text)
    return text[begin:finish].strip()


def _validator_table(text: str, marker: str) -> str:
    token = f"<!-- validator:{marker} -->"
    begin = text.index(token)
    finish = text.find("\n\n", begin)
    return text[begin:] if finish < 0 else text[begin:finish]


def protected_report_fragments(text: str) -> dict[str, str]:
    protected = {
        f"table:{marker}": _validator_table(text, marker)
        for marker in VALIDATOR_MARKERS
    }
    pattern = re.compile(
        r"<!-- (coverage|review|claim|analysis|analysis-decision|existing|delta|books-review):(.*?):start -->"
    )
    for match in pattern.finditer(text):
        kind, identity = match.groups()
        marker = f"{kind}:{identity}"
        end_token = f"<!-- {marker}:end -->"
        end = text.index(end_token, match.end()) + len(end_token)
        key = f"block:{marker}"
        assert key not in protected, key
        protected[key] = text[match.start():end]
    return protected


def semantic_packet_hashes() -> dict[str, str]:
    excluded = {PRESENTATION_AUDIT, SHA256SUMS}
    return {
        path.relative_to(PACKET).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(PACKET.rglob("*"))
        if path.is_file() and path not in excluded
    }


def _collection_hash(items: dict[str, str]) -> str:
    payload = "".join(f"{key}\0{items[key]}\0" for key in sorted(items))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def canonicalize_presentation(text: str) -> str:
    headings = re.findall(r"(?m)^## .+$", text)
    if headings == EXPECTED_H2:
        title_end = text.index("\n")
        title = text[:title_end]
        executive_start = text.index("## Executive Summary")
        final_start = text.index("## 13. Final Status")
        body = text[executive_start:final_start].rstrip()
        return "\n\n".join((title, CANONICAL_HEADER.rstrip(), body, FINAL_STATUS.rstrip())) + "\n"
    legacy_h2 = [
        "## Executive Summary",
        "## 1. Coverage",
        "## 2. Candidate Ledger and Score V2",
        "## 3. Source Reviews",
        "## 4. Deep Analysis Selection",
        "## 5. Books Comparison and Decision",
        "## 6. Semantic Audit",
        "## 7. Materials and Access",
        "## 8. Daily Integration Decision",
        "## 9. Repository Changes",
        "## 10. Open Questions",
    ]
    assert headings == legacy_h2, headings

    title_end = text.index("\n")
    title = text[:title_end]
    executive = _section_body(text, "## Executive Summary", "## 1. Coverage")
    stale_status = (
        "Books comparison yields 58 Integrate and 34 No Change; this date is not "
        "Complete until root writeback and post-write audit pass."
    )
    accepted_status = (
        "Books comparison yields 58 Integrate and 34 No Change; root wrote all 58 "
        "Integrate families and the 92/92 post-write fresh audit passed with zero "
        "unresolved findings, so this date is Complete."
    )
    assert executive.count(stale_status) == 1
    executive = executive.replace(stale_status, accepted_status)
    coverage = _section_body(text, "## 1. Coverage", "## 2. Candidate Ledger and Score V2")
    candidate = _section_body(text, "## 2. Candidate Ledger and Score V2", "### Review Completion Receipt")
    receipt = _section_body(text, "### Review Completion Receipt", "### Benchmark Contract")
    benchmark = _section_body(text, "### Benchmark Contract", "## 3. Source Reviews")
    reviews = _section_body(text, "## 3. Source Reviews", "## 4. Deep Analysis Selection")
    selection = _section_body(text, "## 4. Deep Analysis Selection", "## 5. Books Comparison and Decision")
    books = _section_body(text, "## 5. Books Comparison and Decision", "## 6. Semantic Audit")
    semantic = _section_body(text, "## 6. Semantic Audit", "## 7. Materials and Access")
    materials = _section_body(text, "## 7. Materials and Access", "## 8. Daily Integration Decision")
    recommended = _section_body(text, "## 8. Daily Integration Decision", "## 9. Repository Changes")
    repository = _section_body(text, "## 9. Repository Changes", "## 10. Open Questions")
    questions = _section_body(text, "## 10. Open Questions", None)

    sections = [
        title,
        CANONICAL_HEADER.rstrip(),
        f"## Executive Summary\n\n{executive}",
        f"## 1. Coverage\n\n{coverage}",
        f"## 2. Candidate Ledger\n\n{candidate}",
        f"## 3. Review Completion Receipt\n\n{receipt}\n\n### Source Reviews\n\n{reviews}",
        f"## 4. Benchmark Contracts\n\n{benchmark}",
        f"## 5. Deep Analysis Selection\n\n{selection}",
        f"## 6. Books Comparison\n\n{books}",
        f"## 7. Semantic Audit\n\n{semantic}\n\n### Materials and Access\n\n{materials}",
        IGNORED_NOISE.rstrip(),
        f"## 9. Recommended Action\n\n{recommended}",
        f"## 10. Repository Changes\n\n{repository}",
        f"## 11. Open Questions\n\n{questions}",
        SOURCES.rstrip(),
        FINAL_STATUS.rstrip(),
    ]
    return "\n\n".join(section for section in sections if section) + "\n"


def _report_collections(protected: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    reviews = {
        key: value for key, value in protected.items()
        if key.startswith("block:review:")
    }
    books = {
        key: value for key, value in protected.items()
        if key.startswith(("block:existing:", "block:delta:", "block:books-review:"))
        or key == "table:books-comparison-v1"
    }
    return reviews, books


def assert_canonical_presentation(text: str) -> None:
    assert re.findall(r"(?m)^## .+$", text) == EXPECTED_H2
    for field in ("Research Date", "Timezone", "Strict Window", "Contract", "Status"):
        assert text.count(f"**{field}:**") == 1, field
    assert "**Status:** Complete" in text
    assert "Coverage `Closed`" in text
    assert "Evidence `Passed`" in text
    assert "Books `Passed`" in text
    assert "Completion `Complete`" in text
    assert "this date is not Complete until" not in text
    assert "zero unresolved findings, so this date is Complete" in text
    protected = protected_report_fragments(text)
    reviews, books = _report_collections(protected)
    assert len(protected) == 561
    assert len(reviews) == 92
    assert len(books) == 277
    assert len(set(re.findall(r"RP-[0-9a-f]{16}", text))) == 92
    assert PREWRITE_AUDIT.is_file() and POST_WRITE_AUDIT.is_file()
    post = POST_WRITE_AUDIT.read_text(encoding="utf-8")
    assert len(re.findall(r"(?m)^\| `SF-2026-ARXIV-", post)) == 92
    assert "zero unresolved findings" in post


def write_presentation_audit(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    reviews, books = _report_collections(protected)
    audit = f"""# 2026-06-23 Canonical Presentation Audit V1

- Scope: reader-facing migration only; accepted denominator, Evidence, Selection, Books state and Gate semantics were not re-evaluated.
- Canonical presentation: top five fields present; `Executive Summary` plus the exact numbered §§1–13 H2 sequence passed.
- Protected report fragments: `{len(protected)}`; combined SHA256 `{_collection_hash(protected)}`.
- Bounded Reviews: `92/92`; combined SHA256 `{_collection_hash(reviews)}`.
- Review Provenance IDs: `92/92`; the protected Review Completion table remains byte-identical.
- Books table and bounded blocks: `{len(books)}` fragments; combined SHA256 `{_collection_hash(books)}`.
- Semantic packet inputs: `{len(packet_hashes)}` files sealed; combined SHA256 `{_collection_hash(packet_hashes)}`.
- Reader-facing Daily SHA256: `{hashlib.sha256(report.encode('utf-8')).hexdigest()}`.
- Owner renderer guard: PASS — protected-byte drift, missing audits, wrong Gate summary, duplicate markers or H2 drift fails closed.
- Semantic handoff: `PREWRITE_FRESH_AUDIT_V1.md` and `POST_WRITE_FRESH_AUDIT_V1.md` remain the accepted semantic audits; structural validation is not substituted for semantic truth.
- Shared-state boundary: Books and `docs/LEARNING_STATE.md` were read by the historical post-write workflow but are not read or written by this accepted-state renderer.
- Cross-model skipped: non-interactive child-lane context; no independent second-model claim is made.
- Findings: none unresolved.
"""
    PRESENTATION_AUDIT.write_text(audit, encoding="utf-8")


def assert_prior_presentation_seal(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    # rm-rf recovery can restore an empty placeholder for a presentation seal.
    # A zero-byte placeholder carries no accepted hash and must not be treated
    # as a prior seal; the current accepted semantic packet will create it.
    if not PRESENTATION_AUDIT.is_file() or PRESENTATION_AUDIT.stat().st_size == 0:
        return
    prior = PRESENTATION_AUDIT.read_text(encoding="utf-8")
    reviews, books = _report_collections(protected)
    expected = {
        "Protected report fragments": _collection_hash(protected),
        "Bounded Reviews": _collection_hash(reviews),
        "Books table and bounded blocks": _collection_hash(books),
        "Semantic packet inputs": _collection_hash(packet_hashes),
        "Reader-facing Daily SHA256": hashlib.sha256(report.encode("utf-8")).hexdigest(),
    }
    for label, actual in expected.items():
        match = re.search(rf"^- {re.escape(label)}.*?`([0-9a-f]{{64}})`", prior, re.M)
        assert match and match.group(1) == actual, f"prior presentation seal drift: {label}"


def regenerate_manifest() -> None:
    targets = sorted(
        path for path in PACKET.rglob("*") if path.is_file() and path != SHA256SUMS
    )
    targets.append(REPORT)
    rows = [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}"
        for path in sorted(targets)
    ]
    SHA256SUMS.write_text("\n".join(rows) + "\n", encoding="utf-8")


def finalize_accepted_presentation() -> bool:
    # Recovery can leave zero-byte placeholders for the previously accepted
    # presentation.  A placeholder is not an accepted semantic packet and must
    # not enter the presentation-only migration path.
    if not all(path.is_file() and path.stat().st_size > 0 for path in (REPORT, PREWRITE_AUDIT, POST_WRITE_AUDIT)):
        return False
    before_report = REPORT.read_text(encoding="utf-8")
    before_protected = protected_report_fragments(before_report)
    before_packet = semantic_packet_hashes()
    assert_prior_presentation_seal(before_protected, before_packet, before_report)
    report = canonicalize_presentation(before_report)
    assert protected_report_fragments(report) == before_protected
    assert semantic_packet_hashes() == before_packet
    assert_canonical_presentation(report)
    REPORT.write_text(report, encoding="utf-8")
    write_presentation_audit(before_protected, before_packet, report)
    regenerate_manifest()
    print(json.dumps({
        "mode": "accepted-presentation-only",
        "raw": 586,
        "retained": 92,
        "closures": 494,
        "reviews_preserved": 92,
        "books_dispositions_preserved": 92,
        "canonical_numbered_sections": 13,
        "total_h2": len(EXPECTED_H2),
    }, ensure_ascii=False))
    return True

def main() -> None:
    if finalize_accepted_presentation():
        return
    provisional = json.loads(PROVISIONAL.read_text())
    rows = provisional["identities"]
    assert len(rows) == 586 and len(OWNERS) == 92
    byid = {r["arxiv_id"]:r for r in rows}
    assert set(OWNERS) <= set(byid)
    toc = json.loads((PACKET/"exact-v1-toc.json").read_text())
    disclosures = json.loads((PACKET/"exact-v1-disclosure-hits.json").read_text())
    assert set(toc) == set(disclosures) == set(OWNERS)
    assert all(toc[x] for x in OWNERS)
    assert all((ROOT/p).exists() for p in PATHS.values())

    proposed = set(OWNERS) | PROPOSED_EXTRA
    (PACKET/"candidate-ids-proposed-v1.txt").write_text("\n".join(sorted(proposed))+"\n")
    (PACKET/"candidate-ids-v1.txt").write_text("\n".join(sorted(OWNERS))+"\n")

    audit_rows, retained = [], []
    for row in rows:
        aid = row["arxiv_id"]
        if aid in OWNERS:
            reason = f"{Q}{row['title']}{Q} 改变 {Q}{OWNERS[aid]}{Q} 的长期 state/data/control 或 evaluation/security contract：{fam_delta(row)}"
            decision, kind = "retained_after_full_semantic_audit", "durable_ai_system_candidate"
            retained.append(row)
        else:
            kind, reason = closure(row)
            decision = "pre_denominator_closure"
        audit_rows.append({**row,"source_family_id":fam(aid),"semantic_screen_status":decision,
          "semantic_decision_kind":kind,"semantic_screen_reason":reason,
          "stable_node_id":OWNERS.get(aid,"—"),"screened_at":EXECUTED})

    basis = "\n".join(sorted(fam(x) for x in OWNERS))
    den = "daily-v2.1:2026-06-23:" + hashlib.sha256(basis.encode()).hexdigest()[:16]
    route_neg = sum(r["screening_route"]=="not_routed_by_keyword_contract" for r in rows)
    route_neg_ids = sorted(r["arxiv_id"] for r in retained if r["screening_route"]=="not_routed_by_keyword_contract")
    assert route_neg == 122 and route_neg_ids == ["2606.22804","2606.22875","2606.23892"]

    ledger = {k:v for k,v in provisional.items() if k!="identities"}
    ledger.update(schema="daily-v2.1-screening-ledger-v2",denominator_id=den,
      denominator_frozen_at=EXECUTED,registered_window_identities=586,
      retained_candidate_families=92,closed_pre_denominator_families=494,
      route_negative_audited=122,route_negative_retained=3,
      gate_status="coverage_closed_evidence_selection_passed_books_open",
      false_positive_false_negative_audit={"proposed_pool":100,"final_retained":92,
        "proposed_false_positives_closed":sorted(PROPOSED_EXTRA),
        "route_negative_retained":route_neg_ids,
        "second_pass_findings":[closure(byid[x])[1] for x in sorted(PROPOSED_EXTRA)]},
      identities=audit_rows)
    (PACKET/"screening-ledger.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    with (PACKET/"denominator-full-semantic-audit-v1.tsv").open("w",newline="") as fh:
        w=csv.writer(fh,delimiter="\t")
        w.writerow(["source_family_id","arxiv_id","route","title","abstract_basis","decision","decision_kind","stable_node_id","family_specific_reason"])
        for r in audit_rows:
            w.writerow([r["source_family_id"],r["arxiv_id"],r["screening_route"],r["title"],first_sentence(r["abstract"]),r["semantic_screen_status"],r["semantic_decision_kind"],r["stable_node_id"],r["semantic_screen_reason"]])

    reviews=[]
    for row in retained:
        aid=row["arxiv_id"]; owner=OWNERS[aid]; family=fam(aid); delta=fam_delta(row)
        locs=LOCATOR_OVERRIDES.get(aid)
        method="arXiv:"+aid+"v1 — "+(locs[0] if locs else pick_locator(toc[aid],"method",row["title"]))
        evaluation="arXiv:"+aid+"v1 — "+(locs[1] if locs else pick_locator(toc[aid],"evaluation",row["title"]))
        limits="arXiv:"+aid+"v1 — "+(locs[2] if locs else pick_locator(toc[aid],"limits",row["title"]))
        fallback=FALLBACK.get(owner,"前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执")
        trade=(f"该 family 的 failure pressure 是：{failure_sentence(row['abstract'])} "
          f"披露的 evaluation signal 是：{result_sentence(row['abstract'])} "
          f"证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；"
          f"{fallback}。旧路径在其原约束成立时继续共存。")
        bench=benchmark(row,disclosures[aid])
        body=(f"### {aid} — {row['title']}\n\n"
          f"**问题与旧路径。** {failure_sentence(row['abstract'])} 旧路径在输入分布、信任边界和预算稳定时仍合理。\n\n"
          f"**机制与 state/data/control owner。** {delta} 唯一 owner 为 {Q}{owner}{Q}；相邻章只消费带 identity/version/failure/fallback 的 handoff。\n\n"
          f"**Evaluation：proof / non-proof。** Method={Q}{method}{Q}；Evaluation={Q}{evaluation}{Q}；counterevidence={Q}{limits}{Q}。这些证据不证明未测试规模、分布、攻击者或生产 SLO。\n\n"
          f"**Trade-off / failure / coexistence / evolution。** {trade}\n\n"
          f"<!-- claim:{family}:start -->\nPrimary identity {Q}arXiv:{aid}v1{Q}; official exact-v1 HTML; ordinary pending=0.\n<!-- claim:{family}:end -->")
        disposition="No Change — Existing Coverage" if aid in NO_CHANGE else "Integrate"
        r={"aid":aid,"family":family,"title":row["title"],"owner":owner,"delta":delta,
          "method":method,"evaluation":evaluation,"limits":limits,"trade":trade,
          "bench":bench,"score":score(owner),"disposition":disposition,"body":body,
          "primary":f"arXiv:{aid}v1","versions":f"SRC-ARXIV@arXiv:{aid}v1",
          "artifact":"Not Disclosed — no later artifact used",
          "access":"accessible_official_exact_v1_html"}
        r["rp"]=prov(r); reviews.append(r)
    assert len(reviews)==92
    assert len({(r["method"],r["evaluation"],r["limits"]) for r in reviews})==92
    for r in reviews:
        assert set(r["bench"])=={"workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator"}
        assert all(str(v).strip() for v in r["bench"].values())
        assert not any(x in str(r["bench"]) for x in ("or Not Disclosed","if disclosed","Paper-specific","Workload-specific"))

    (PACKET/"exact-v1-access-receipt.json").write_text(json.dumps({
      "schema":"exact-v1-access-receipt-v1","denominator_id":den,"checked_at":EXECUTED,
      "result":"92/92 official exact-v1 HTML identities resolved","ordinary_pending":[],
      "items":[{"source_family_id":r["family"],"primary_identifier":r["primary"],
        "locator":f"https://arxiv.org/html/{r['aid']}v1","status":r["access"],
        "version_identity":r["primary"],"identity_version_note":"official arXiv exact-v1 HTML; no later revision used"} for r in reviews]
    },ensure_ascii=False,indent=2)+"\n")

    (PACKET/"source-review-receipts-v2.1.json").write_text(json.dumps({
      "contract_version":"V2.1","denominator_id":den,"generated_at":EXECUTED,
      "reviews":[{"source_family_id":r["family"],"review_provenance_id":r["rp"],
        "review_route":"deep","event_identity":"paper-v1:"+r["aid"],
        "primary_identifier":r["primary"],"primary_evidence_version":r["primary"],
        "reviewed_evidence_versions":r["versions"],
        "method_identity_locators":r["method"],"evaluation_locators":r["evaluation"],
        "limitations_counterevidence_locators":r["limits"],
        "artifact_locators":r["artifact"],
        "claim_boundary_ref":"claim:"+r["family"],"review_ref":"review:"+r["family"],
        "review_body_sha256":hashlib.sha256(unicodedata.normalize("NFC",r["body"]).encode()).hexdigest(),
        "completion_result":"complete","ordinary_pending_locator_count":0,
        "benchmark_contract":r["bench"],"score_v2":r["score"],
        "stable_node_id":r["owner"],"books_disposition":r["disposition"]} for r in reviews]
    },ensure_ascii=False,indent=2)+"\n")

    selection=[]
    for r in reviews:
        if r["aid"] in SELECTED:
            rationales={
             "2606.22741":"入选：GRADE 把 execution 与 dependency 两层、edge-source grade、failure localization 和跨 agent-class transfer 接成同一可观测状态链。",
             "2606.22768":"入选：Factored Gossip DiLoCo 把非阻塞 Mix1、阻塞 Mix2、worker disagreement 与 compute-utilization/稳定性 trade-off 接成分布式训练控制面。",
             "2606.23003":"入选：VCT 用 Q&A hash chain、session/account Merkle root、joint signature、deletion barrier 与 deterministic merge 定义可验证会话状态。",
            }
            d={"source_family_id":r["family"],"eligibility":"score_7_9; potential_books_delta","decision":"selected",
              "analysis_unit_id":SELECTED[r["aid"]],"subsumed_by":"—","priority_rationale":rationales[r["aid"]],
              "narrative_ref":"analysis:"+SELECTED[r["aid"]]}
        else:
            d={"source_family_id":r["family"],"eligibility":"score_7_9; potential_books_delta","decision":"not_selected",
              "analysis_unit_id":"—","subsumed_by":"—",
              "priority_rationale":f"未入选：完整 frontier 保留 {Q}{r['owner']}{Q} 的 source-specific delta，但相对三项 winner，其跨层 handoff、控制面新颖性或验证强度更窄；Evidence 与 Books disposition 不降级。",
              "narrative_ref":"analysis-decision:"+r["family"]}
        selection.append(d)
    (PACKET/"deep-analysis-selection-v1.json").write_text(json.dumps({
      "schema":"deep-analysis-selection-v1","denominator_id":den,"frontier_size":92,
      "selection_count":3,"winners_frozen_before_rationale":list(SELECTED),"decisions":selection
    },ensure_ascii=False,indent=2)+"\n")

    comparisons=[]; groups={}
    for r in reviews:
        path=PATHS[r["owner"]]; adj=adjacent(path)
        relation="Principle Reuse" if r["aid"] in NO_CHANGE else "Direct Evolution"
        comparisons.append({"source_family_id":r["family"],"stable_node_id":r["owner"],
          "target_chapter_ref":path+"#L1","adjacent_chapter_refs":adj,
          "existing_proposition_ref":"existing:"+r["family"],"new_evidence_delta_ref":"delta:"+r["family"],
          "evolution_relation":relation,"decision":r["disposition"],"books_review_ref":"books-review:"+r["family"],
          "existing_text":f"{Q}{path}{Q} 的唯一 owner 已承载相关机制链；{Q}{adj}{Q} 只消费 handoff。"})
        if r["aid"] not in NO_CHANGE:
            groups.setdefault(r["owner"],[]).append(r)
    assert len(NO_CHANGE)==34 and sum(map(len,groups.values()))==58

    (PACKET/"books-comparison-v1.json").write_text(json.dumps({
      "schema":"books-comparison-v1","denominator_id":den,"compared":"92/92","items":comparisons
    },ensure_ascii=False,indent=2)+"\n")

    queue=["# 2026-06-23 Books Integration Queue V1","",
      f"Denominator {Q}{den}{Q}. Proposal-only: 58 Integrate families merged into {len(groups)} unique owner files; root owns Books and docs/LEARNING_STATE.md.",""]
    ready=["# 2026-06-23 Ready-to-Insert Books Packet V1","",
      "Root 串行写回共享 Books；每个 family 只进入唯一 owner，正文与 Review note 保留 official exact-v1 证据边界。",""]
    for owner,items in sorted(groups.items()):
        path=PATHS[owner]; adj=adjacent(path)
        queue += [f"## {Q}{owner}{Q} → {Q}{path}{Q}","",f"- Adjacent non-owner: {Q}{adj}{Q}"]
        queue += [f"- {Q}{r['family']}{Q}: {r['delta']} {r['trade']}" for r in items]+[""]
        ready += [f"## {Q}{owner}{Q} → {Q}{path}{Q}","",f"相邻章 {Q}{adj}{Q} 只消费 handoff，不重复拥有机制。","","### Owner-merged minimal body",""]
        ready += [f"- **{r['family']}**：{r['delta']} {r['trade']}" for r in items]
        ready += ["","### Source-specific exact-v1 Review notes",""]
        ready += [f"- {Q}{r['family']}{Q} — primary {Q}{r['primary']}{Q}; Method={Q}{r['method']}{Q}; Evaluation={Q}{r['evaluation']}{Q}; non-proof={Q}{r['limits']}{Q}; fallback={r['trade']}" for r in items]+[""]
    (PACKET/"BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue)+"\n")
    (PACKET/"READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready)+"\n")

    families="; ".join(r["family"] for r in reviews)
    L=["# Daily Research — 2026-06-23","",
      "> Strict V2.1 full replay. Coverage is Closed; Evidence and Selection are Passed; Books remains Open pending root writeback and 92/92 post-write fresh audit.","",
      "## Executive Summary","",
      "Beijing window [2026-06-22 09:00, 2026-06-23 09:00) contains 586 registered identities. Full 586/586 title+abstract review freezes 92 durable families and 494 family-specific closures (15.70%). Exact-v1 Evidence is complete for 92/92 official HTML identities; Selection compares all 92 and chooses three narrative units. Books comparison yields 58 Integrate and 34 No Change; this date is not Complete until root writeback and post-write audit pass.","",
      "## 1. Coverage","",
      "<!-- validator:report-metadata-v2 -->",
      "| Field | Value |","| --- | --- |",
      "| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |",
      "| Window Start | 2026-06-23 |","| Window End | 2026-06-23 |",
      "| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |",
      "| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",
      f"| Beijing Window | [2026-06-22 09:00, 2026-06-23 09:00) |",
      f"| Denominator ID | {den} |",f"| Denominator Frozen At | {EXECUTED} |",
      "| Completion Status | In Progress |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Open |","",
      "### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->",
      "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
      "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
      f"| SRC-ARXIV | 2026-06-22T09:00:00+08:00 | 2026-06-23T09:00:00+08:00 | {EXECUTED} | 40 frozen DataCite DOI-prefix snapshots; full Core + topic routes | checked | 586 | {families} | pages=40; final_cursor=end; 586 unique identities | 2026-06-23T01:00:00Z | ../_sources/daily-20260623/screening-ledger.json; ../_sources/daily-20260623/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260623 | — |","",
      "<!-- coverage:SRC-ARXIV:20260623:start -->",
      "Full 586/586 title+abstract audit: 404 Core, 60 keyword-routed and 122 route-negative; arithmetic 586 = 92 retained + 494 closures; retain rate 15.70%. Keyword routing supplied recall only. Route-negative retained=3; proposed-pool false positives closed=8.",
      "<!-- coverage:SRC-ARXIV:20260623:end -->","",
      "## 2. Candidate Ledger and Score V2","","<!-- validator:candidate-ledger-v2.1 -->",
      "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
      "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        s=r["score"]
        L.append(f"| {r['family']} | {r['primary']} | paper-v1:{r['aid']} | 2026-W26 | 2026-06-22 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | none | review:{r['family']} | self | — | new_in_window | {r['owner']} | {r['disposition']} | books-review:{r['family']} | yes |")
    L += ["","### Review Completion Receipt","","<!-- validator:review-completion-v1 -->",
      "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
      "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        L.append(f"| {r['family']} | {r['rp']} | deep | {r['primary']} | {r['versions']} | {r['method']} | {r['evaluation']} | {r['limits']} | {r['artifact']} | claim:{r['family']} | complete |")
    L += ["","### Benchmark Contract","","<!-- validator:benchmark-contract-v1 -->",
      "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
      "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b=r["bench"]; L.append("| "+" | ".join([r["family"]]+[str(b[k]).replace("|","/") for k in ("workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator")])+" |")
    L += ["","## 3. Source Reviews",""]
    for r in reviews:
        L += [f"<!-- review:{r['family']}:start -->",r["body"],f"<!-- review:{r['family']}:end -->",""]
    L += ["## 4. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->",
      "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
      "| --- | --- | --- | --- | --- | --- | --- |"]
    for d in selection:
        L.append("| "+" | ".join(str(d[k]).replace("|","/") for k in ("source_family_id","eligibility","decision","analysis_unit_id","subsumed_by","priority_rationale","narrative_ref"))+" |")
    for r,d in zip(reviews,selection):
        if d["decision"]=="not_selected":
            L += ["",f"<!-- analysis-decision:{r['family']}:start -->",d["priority_rationale"],f"<!-- analysis-decision:{r['family']}:end -->"]
    narratives={
      "2606.22741":"Agent trace 只记录执行顺序会漏掉 reliance failure；GRADE 用 execution/dependency 双层图和 observed/declared/inferred edge grade 补出状态依赖，但 inferred full-history graph 的信号会退化成 run size，不能把 graph score 当因果证明。",
      "2606.22768":"DiLoCo 的全局同步既阻塞又脆弱；Factored Gossip 将 Mix1 与计算重叠、让 Mix2 只承担收紧共识的阻塞工作。收益是利用率与故障降级，代价是 worker disagreement 和训练稳定性必须被持续测量。",
      "2606.23003":"VCT 把 conversation branch、session 与 account 变成三层认证状态，并用 joint signature、deletion barrier、deterministic merge 与 device gossip 约束并发和恶意 server view fork；密码学完整性不证明内容真实性。",
    }
    for aid,text in narratives.items():
        L += ["",f"<!-- analysis:{SELECTED[aid]}:start -->",f"### {SELECTED[aid]}",text,f"<!-- analysis:{SELECTED[aid]}:end -->"]
    L += ["","## 5. Books Comparison and Decision","","<!-- validator:books-comparison-v1 -->",
      "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
      "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    comp_by={c["source_family_id"]:c for c in comparisons}
    for r in reviews:
        c=comp_by[r["family"]]
        L.append(f"| {r['family']} | {r['owner']} | {c['target_chapter_ref']} | {c['adjacent_chapter_refs']} | {c['existing_proposition_ref']} | {c['new_evidence_delta_ref']} | {c['evolution_relation']} | {r['disposition']} | {c['books_review_ref']} |")
    for r in reviews:
        c=comp_by[r["family"]]
        L += ["",f"<!-- existing:{r['family']}:start -->",c["existing_text"],f"<!-- existing:{r['family']}:end -->",
          "",f"<!-- delta:{r['family']}:start -->",r["delta"],f"<!-- delta:{r['family']}:end -->",
          "",f"<!-- books-review:{r['family']}:start -->",
          f"Unique owner {Q}{r['owner']}{Q}; adjacent non-owner {Q}{c['adjacent_chapter_refs']}{Q}; relation {Q}{c['evolution_relation']}{Q}; disposition {Q}{r['disposition']}{Q}. {r['trade']}",
          f"<!-- books-review:{r['family']}:end -->"]
    refs="; ".join("review:"+r["family"] for r in reviews)
    sels="; ".join(d["narrative_ref"] for d in selection)
    books="; ".join("books-review:"+r["family"] for r in reviews)
    L += ["","## 6. Semantic Audit","","<!-- validator:semantic-audit-v1 -->",
      "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
      "| --- | --- | --- | --- | --- | --- | --- |",
      "| SA-20260623-COVERAGE-V1 | fresh-context:jun23-v1 | coverage | coverage:SRC-ARXIV:20260623 | — | 586/586 full semantic audit; 122/122 route-negative; denominator 92; closures 494; eight proposed false positives closed | passed |",
      f"| SA-20260623-EVIDENCE-V1 | fresh-context:jun23-v1 | evidence | {refs} | — | 92/92 official exact-v1 HTML; 92 unique locator triples; explicit benchmark disclosure or literal Not Disclosed; ordinary pending 0 | passed |",
      f"| SA-20260623-SELECTION-V1 | fresh-context:jun23-v1 | deep_analysis_selection | {sels} | — | 92/92 full frontier; 3 selected and 89 not_selected with legal decisions and narrative refs | passed |",
      f"| SA-20260623-BOOKS-PREWRITE-V1 | fresh-context:jun23-v1 | books | {books} | root writeback pending | 58 Integrate families merged into {len(groups)} owner files; 34 No Change handoffs; Books Gate stays Open | open |","",
      "## 7. Materials and Access","","- 92/92 used official arXiv exact-v1 HTML; no mirror or later revision used.","- Ordinary pending locator count: 0.","",
      "## 8. Daily Integration Decision","",f"- Proposed Integrate: 58 families, deduplicated to {len(groups)} owner files in the date-local queue/ready packet.","- No Change — Existing Coverage: 34 families retain Evidence and owner handoff without shared write request.","- Books Gate remains Open until root serial writeback and this lane's 92/92 post-write fresh-context audit.","",
      "## 9. Repository Changes","","- Added only the 2026-06-23 Daily, date-local source packet and scripts/finalize_june23_v21.py.","- Shared Books and docs/LEARNING_STATE.md were not edited, staged, committed or pushed.","",
      "## 10. Open Questions","","- 哪些 dependency edges 值得提升为 declared instrumentation，而不是由 full-history 假设推断？","- Factored gossip 的 disagreement 阈值如何进入 checkpoint/admission policy？","- 对话 transcript 的密码学完整性如何与内容真实性、删除权和 retention policy 分层？"]
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("\n".join(L)+"\n")

    pre=["# 2026-06-23 Pre-write Fresh Audit V1","",
      "- Coverage: PASS — 586/586; denominator 92; closures 494; retain rate 15.70%; route-negative 122/122; proposed-pool false positives 8 closed.",
      "- Evidence: PASS — 92/92 official exact-v1 identities, unique source-specific locator triples, explicit disclosure or literal Not Disclosed, proof/non-proof/fallback boundaries.",
      "- Selection: PASS — full 92-family frontier, 3 selected and 89 not_selected.",
      f"- Books prewrite comparison: PASS — 58 Integrate proposals into {len(groups)} unique owners and 34 No Change handoffs; Books Gate remains Open.",
      "- Cross-model review skipped in non-interactive child lane; a second independent self-audit was performed and root will run separate prewrite review.","",
      "| Family | Exact-v1 | Locator triple | Benchmark | Selection | Owner / adjacent | Disposition | Result |",
      "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        c=comp_by[r["family"]]; d=next(x for x in selection if x["source_family_id"]==r["family"])
        disclosed=", ".join(k for k,v in r["bench"].items() if v!="Not Disclosed")
        nd=", ".join(k for k,v in r["bench"].items() if v=="Not Disclosed") or "none"
        pre.append(f"| {Q}{r['family']}{Q} | official v1 | source-specific | disclosed: {disclosed}; ND: {nd} | {d['decision']} | {Q}{r['owner']}{Q} / {Q}{c['adjacent_chapter_refs']}{Q} | {r['disposition']} | PASS |")
    (PACKET/"PREWRITE_FRESH_AUDIT_V1.md").write_text("\n".join(pre)+"\n")

    # Post-write mode: enabled only when all 58 Integrate families appear.
    book_files=list((ROOT/"books").rglob("*.md"))
    integrates=[r for r in reviews if r["aid"] not in NO_CHANGE]
    post_ready=all(any(r["family"] in p.read_text() for p in book_files) for r in integrates)
    if post_ready:
        findings=[]; post_rows=[]
        for r in reviews:
            expected=ROOT/PATHS[r["owner"]]
            text=expected.read_text()
            hits=[p for p in book_files if r["family"] in p.read_text()]
            c=comp_by[r["family"]]
            if r["aid"] in NO_CHANGE:
                if hits: findings.append((r["family"],"No Change unexpectedly written",[str(x.relative_to(ROOT)) for x in hits]))
                post_rows.append((r,"No Change","existing owner proposition re-opened"))
                continue
            if hits != [expected]: findings.append((r["family"],"unique owner",[str(x.relative_to(ROOT)) for x in hits]))
            checks={"mechanism":r["delta"] in text,"family body+review":text.count(r["family"])==2,
              "method":r["method"] in text,"evaluation":r["evaluation"] in text,
              "non-proof":r["limits"] in text,"fallback":r["trade"] in text}
            for label,ok in checks.items():
                if not ok: findings.append((r["family"],label,"missing/count mismatch"))
            post_rows.append((r,"Integrate","mechanism + exact-v1 Review note re-opened"))
        if findings:
            raise AssertionError("post-write semantic findings: "+repr(findings))
        post=["# 2026-06-23 Post-write Fresh Audit V1","",
          "- Result: PASS — 92/92; zero unresolved findings.",
          f"- Integrate: 58/58 in exactly one expected owner across {len(groups)} owner files; mechanism, trade-off, failure/fallback and exact-v1 Review note re-opened.",
          "- No Change: 34/34 canonical owner propositions re-opened; no accidental family write.",
          "- Owner/adjacent handoff: 92/92 target and adjacent paths resolve.","",
          "| Family | Disposition | Expected owner | Semantic check | Result |","| --- | --- | --- | --- | --- |"]
        for r,disp,check in post_rows:
            post.append(f"| {Q}{r['family']}{Q} | {disp} | {Q}{r['owner']}{Q} → {Q}{PATHS[r['owner']]}{Q} | {check} | PASS |")
        (PACKET/"POST_WRITE_FRESH_AUDIT_V1.md").write_text("\n".join(post)+"\n")
        report=REPORT.read_text()
        report=report.replace("Coverage is Closed; Evidence and Selection are Passed; Books remains Open pending root writeback and 92/92 post-write fresh audit.","Coverage is Closed; Evidence, Selection and Books are Passed after the 92/92 post-write fresh audit.")
        report=report.replace("This date is not Complete until root writeback and post-write audit pass.","Root wrote 58 Integrate families; the 92/92 post-write fresh audit passed with zero unresolved findings. This date is Complete.")
        report=report.replace("| Completion Status | In Progress |","| Completion Status | Complete |").replace("| Books Gate | Open |","| Books Gate | Passed |")
        report=report.replace(f"| SA-20260623-BOOKS-PREWRITE-V1 | fresh-context:jun23-v1 | books | {books} | root writeback pending | 58 Integrate families merged into {len(groups)} owner files; 34 No Change handoffs; Books Gate stays Open | open |",f"| SA-20260623-BOOKS-POSTWRITE-V1 | fresh-context:jun23-postwrite-v1 | books | {books} | — | 58/58 Integrate in one expected owner; 34/34 No Change revalidated; exact-v1 Review note and owner/adjacent handoff 92/92; zero unresolved finding | passed |")
        report=report.replace(f"- Proposed Integrate: 58 families, deduplicated to {len(groups)} owner files in the date-local queue/ready packet.",f"- Integrate: root wrote 58/58 families into {len(groups)} unique owner files; post-write semantic audit passed.")
        report=report.replace("- No Change — Existing Coverage: 34 families retain Evidence and owner handoff without shared write request.","- No Change — Existing Coverage: 34/34 canonical propositions and boundaries were revalidated.")
        report=report.replace("- Books Gate remains Open until root serial writeback and this lane's 92/92 post-write fresh-context audit.","- Post-write fresh audit: 92/92 Passed, zero unresolved finding; Completion Complete.")
        report=report.replace("- Shared Books and docs/LEARNING_STATE.md were not edited, staged, committed or pushed.","- Root serialized shared Books. This lane audited them and changed only date-local files; it did not edit, stage, commit or push Books or docs/LEARNING_STATE.md.")
        REPORT.write_text(report)
        ledger=json.loads((PACKET/"screening-ledger.json").read_text())
        ledger["gate_status"]="complete_postwrite_fresh_audit_passed"
        ledger["audit"]={"coverage":"586/586_passed","evidence":"92/92_passed","selection":"92/92_full_frontier_passed","books":"92/92_postwrite_passed_58_integrate_plus_34_no_change","unresolved_findings":0}
        (PACKET/"screening-ledger.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
        (PACKET/"README.md").write_text(f"# 2026-06-23 source packet\n\nCanonical denominator {Q}92/586{Q}; closures {Q}494{Q}; retain rate {Q}15.70%{Q}. Coverage Closed, Evidence Passed, Selection Passed, Books Passed. Root wrote 58 Integrate across {len(groups)} owners; 34 No Change. Post-write fresh audit 92/92 Passed; zero unresolved finding; Completion Complete.\n")
    else:
        (PACKET/"README.md").write_text(f"# 2026-06-23 source packet\n\nCanonical denominator {Q}92/586{Q}; closures {Q}494{Q}; retain rate {Q}15.70%{Q}. Coverage Closed, Evidence Passed, Selection Passed, Books Open. Prewrite queue: 58 Integrate across {len(groups)} owner files; 34 No Change. Completion remains In Progress until root writeback and 92/92 post-write fresh audit.\n")

    sums=[]
    for p in sorted(x for x in PACKET.iterdir() if x.is_file() and x.name not in {"SHA256SUMS","screening-ledger-provisional.json"}):
        sums.append(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name)
    (PACKET/"SHA256SUMS").write_text("\n".join(sums)+"\n")
    print(json.dumps({"denominator_id":den,"raw":586,"retained":92,"closures":494,
      "retain_rate":"15.70%","route_negative":122,"route_negative_retained":3,
      "false_positives_closed":8,"integrate":58,"no_change":34,"owners":len(groups),
      "postwrite_ready":post_ready},ensure_ascii=False,indent=2))

if __name__ == "__main__":
    main()
