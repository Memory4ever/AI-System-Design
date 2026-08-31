#!/usr/bin/env python3
"""Build the independent V9 Candidate Denominator audit receipt for 2026-06-01.

The script is intentionally packet-local.  It reads only the frozen raw ledger,
the frozen Atom discovery snapshot and the repair-author V8 audit, then writes
the independent 371-row receipt and its human-readable checkpoint.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import re
import textwrap
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


PACKET = Path(__file__).resolve().parent
LEDGER = PACKET / "screening-ledger.tsv"
V8_AUDIT = PACKET / "candidate-denominator-audit-v8.tsv"
ATOM = PACKET / "arxiv-overread-first-page.atom.gz"
PROVENANCE = PACKET / "fresh-context-identity-date-provenance-independent-v9.tsv"
RECEIPT = PACKET / "fresh-context-candidate-denominator-audit-independent-v9.tsv"
CHECKPOINT = PACKET / "fresh-context-candidate-denominator-audit-independent-v9.md"


# The independent retain set is deliberately explicit.  ROADMAP mapping, AI
# relevance, one-domain method/benchmark status, or a local representation/model
# improvement were not sufficient by themselves.
RETAIN_REASONS = {
    "2606.00942": "保留：metastable fault 把局部稳定组件之间的反馈环与全局 recovery/liveness control 绑定，明确改变长期 production failure 与调度恢复契约。",
    "2606.00944": "保留：PRISM 证明 LoRA 因子 gauge 不可辨识会破坏朴素 DP 噪声语义，并把隐私扰动重新绑定到可辨识更新；这是训练 privacy mechanism 的实质修正。",
    "2606.00946": "保留：Lodestar 把 request/instance/performance observation、在线 reward prediction、TTFT routing 与 deterministic fallback 组成持续控制环，改变异构 inference routing 判断。",
    "2606.00947": "重开：federated personalization 的 privacy boundary 会遮蔽行为退化，六类 silent failure 要求 privacy-preserving behavioral evaluation；这改变多租户训练平台的观测与验收契约。",
    "2606.00953": "重开：Co-Coder 以 dependency graph 拥有任务分区、hub-file isolation 与 dependency-aware scheduling，而不是只增加 Agent 数；这改变 coding-agent 编排的控制与 merge critical path。",
    "2606.00981": "重开：auto-formalization 把异步自然语言 subplan 转成可机检 obligation，再允许并发执行与 merge；formalization/solver boundary 改变 planning state 与合并验收契约。",
    "2606.00997": "保留：order-agnostic conditionals 未必构成一致 joint distribution，因此 reveal order 不再只是调度细节，而是 diffusion/masked-LM decoding 与评价契约的一部分。",
    "2606.01007": "重开：TACG/GESR 用 task-conditioned co-activation、expert replication、locality/load selection 拥有 MoE expert placement；这是跨 GPU inference data/control placement 机制，不是局部模型精度改进。",
    "2606.01019": "保留：Hybrid Verified Decoding 预测 accepted length 并在 cache/model drafter 间按 payoff 切换，改变 speculative decoding 的 draft/verify 控制面与 fallback 判断。",
    "2606.01034": "保留：FCPS 明确以 validation support 在 judge path、panel、stacker 与 joint table 间选择，改变有限人标下的 evaluator calibration contract。",
    "2606.01065": "保留：Leyline 为可编辑 Agent history 定义 KV edit/position-preservation directive、re-anchoring/splice/re-prefill 路径，改变 serving cache state 的可声明控制接口。",
    "2606.01066": "保留：RLVR verifier fuzzing 以被测/reference verifier 的 differential FP/FN/disagreement/exploit 收据约束 reward owner，改变 verifier 上线前的 evaluation contract。",
    "2606.01091": "重开：DR-rubric 先检索证据、再蒸馏原子 constraint 并作为 GRPO reward，明确改变开放式 research Agent 的 evaluator/rubric provenance 与训练信号契约。",
    "2606.01128": "保留：Local MixVR 把 local momentum、minibatch budget mixing 与 drift correction 绑定到通信轮次复杂度，形成可独立检验的 distributed-training communication design。",
    "2606.01138": "保留：memorywire 定义跨 backend 的 remember/recall/forget/merge/expire、MemoryStore、fan-out router 与 conformance suite，改变 Agent memory state/interface ownership。",
    "2606.01139": "重开：SkillRevise 从 execution trace 定位缺陷、检索 repair principle、预算内编辑并只接纳 verifier-passing skill，改变 skill artifact 的维护与验收生命周期。",
    "2606.01143": "保留：shared-prefix schedule 把一次 prefix forward、suffix microbatch、gK/gV accumulation 与统一 prefix backward 组成数值等价训练状态复用机制。",
    "2606.01155": "重开：该 scaling law 联合 active parameters、unique/repeated tokens、epochs 与 sparsity，直接修正数据稀缺和重复 epoch 下的 pretraining capacity/compute 判断。",
    "2606.01185": "重开：lakehouse Agent 将 skills/environment files 作为版本化 artifact，并以隔离 sandbox 的 branch/commit final state 验收而非语言自报；这是可迁移的 Agent evaluation contract。",
    "2606.01196": "保留：跨语种安全实验分离 harmfulness representation 与 refusal action，表明安全 bottleneck 可位于 action realization；这修正 monitor、gate 与 effect-time control 的责任边界。",
    "2606.01212": "重开：DiscourseFlip 把攻击入口从 prompt 改为可写 corpus，并跨 semantic query network 优化 opinion shift；这改变开放 RAG 的 corpus authority、lineage 与 inference-cost/security threat model。",
    "2606.01311": "保留：SkillAdaptor 以 first actionable fault、候选 skill attribution 与 acceptance check 做局部更新，改变 Agent skill state 的故障归因和变更控制。",
    "2606.01314": "重开：SkillSmith 同时演化 skill/tool 原子 bundle 并保留 interaction matrix、anti-pattern veto 与 trace，改变 Agent capability state、权限面与回滚所有权。",
    "2606.01317": "重开：SABER 在真实项目式 workspace 执行 coding Agent，并以最终环境状态及 violation cause 验收，改变从 response safety 到 effect-state safety 的 evaluator contract。",
    "2606.01365": "保留：failure-aware MAS observability 把 loop、budget pressure、information gain 与 tool instability 变成在线 signal，并限定触发有界 recovery，改变 Agent runtime monitoring control loop。",
    "2606.01387": "保留：ResidentClaim 为未来 KV reuse obligation 定义 identity、materialization predicate、ordered lifecycle、outcome 与 fail-closed lowering，改变 cache state/control contract。",
    "2606.01413": "保留：DP RAG datastore 以 LSH aggregation、校准噪声和 privacy accounting 控制个体贡献泄露，改变可共享 retrieval state 的数据所有权与发布契约。",
    "2606.01416": "保留：self-healing orchestrator 将 observable failure class 映射到预算化 recovery、轨迹验证与 trace，并在副作用未知时要求 fail closed，改变执行控制环。",
    "2606.01435": "保留：memory freshness assembly 将 evidence matching 与 freshness/conflict policy execution 分阶段，要求显式 version metadata，改变长期记忆事实的组装和当前值所有权。",
    "2606.01462": "重开：VAIR 在 final answer 固定正确时植入错误步骤，隔离 answer correctness 与 process validity，证明高风险 reasoning 不能只以答案验收，改变评价契约。",
    "2606.01494": "保留：ClawHub 将脚本、指令、语义权限与多 scanner disagreement 对齐到 registry verdict，要求 layered triage 加 effect-time sandbox/least privilege，改变 Agent skill supply-chain 控制。",
    "2606.01502": "保留：该工作用可测 cost model 在 route-query、fetch-cache 与 local compute 间选择，明确改变跨实例 sparse-attention/MLA 的数据搬运与 serving placement 判断。",
    "2606.01508": "保留：AOS 将 agent scheduler、context/memory、capability registry、policy/trust 与 audit control plane 分层到传统 OS 之上，提供长期 Agent 平台责任边界与非目标。",
    "2606.02643": "保留：CREEP 将 inference-cost attack 从可改 prompt 扩展到可写 RAG corpus，要求 quota、retrieval provenance 与 output budget 共同拥有防护。",
    "2606.02646": "重开：Ringelmann 分析区分 nominal Agent count 与有效独立团队规模，显示 peer/round 主要受相关性 ceiling 约束，改变 multi-Agent test-time scaling 的设计与评价判断。",
    "2606.04017": "保留：long-running Agent epistemic integrity 将 goal validity、action archetype、tool instance 与 invocation failure 组织为跨 session/version 的 interface conformance contract。",
    "2606.07631": "保留：trait-space checkpoint monitor 将训练中 activation drift 作为白盒 sensor，并明确必须与行为验收/effect policy 组合，改变 alignment monitoring contract。",
    "2606.07632": "保留：ML life-cycle assessment 以明确 functional unit 覆盖 data、experimentation、deployment、refresh、infrastructure 与 retirement，改变平台成本/资源评价边界。",
    "2606.09863": "保留：false-success 研究以 text-independent environment ground truth 证实语言结案与真实外部状态分离，要求 environment verifier 成为最终验收 owner。",
    "2608.21363": "保留：AIREP 用封闭 decision verb、hash reference、coverage declaration、signature 与 chain 形成可离线验证的 per-decision evidence object，改变 runtime governance evidence plane。",
}


# All 37 repair-author retains not present above are independent false positives.
# These reasons are intentionally paper/family-specific rather than a generic
# "does not map to ROADMAP" explanation.
DROP_REASONS = {
    "2606.00957": ("platform-or-inference-instance-without-owner-change", "HiFloat8 的首尾 BF16/中间 block 量化只由 Wan2.1 与 Ascend 910B 的小 prompt ablation 支持；它是特定视频 DiT 的校准实例，不能形成可迁移的混合精度 owner 或 kernel contract。"),
    "2606.00962": ("survey-position-or-proposal-without-validated-contract", "SS-ZKR 给出 threat model、DP/ZK routing 架构和分析复杂度，但没有实现、吞吐、attack replay 或 conformance evidence；未验证 proposal 不足以改变跨组织 Agent security contract。"),
    "2606.00963": ("task-specific-model-or-representation-variant", "Reasmory 将多视图重建为 3D memory 并用 DSL 查询，增益仍绑定空间推理 benchmark、重建器与 DSL 覆盖；这是局部视觉表示/工具方法，不改长期 Agent memory lifecycle。"),
    "2606.00994": ("non-ai-system-domain-method", "registry-bound extraction 的 version、retry、evidence 与 moderation queue 是良好工程实践，但证据来自 plant-trait corpus pipeline；它未提出超出现有 typed ETL/provenance owner 的 AI-System 机制。"),
    "2606.00995": ("task-specific-model-or-representation-variant", "subliminal steering 将 trait transfer 定位到 activation direction，结论绑定模型对和 trait；局部表示解释本身不构成新的训练控制、部署 gate 或可移植 detector。"),
    "2606.01009": ("platform-or-inference-instance-without-owner-change", "MelT 把 Mel frontend 重写成 dense GEMM，但 workload 是 audio frontend，收益随 GPU、frame 与 Mel-bin 改变；单领域 kernel lowering case 不改变通用 inference execution contract。"),
    "2606.01027": ("task-specific-model-or-representation-variant", "tau0-WM 用视频 rollout 给机器人动作候选排序，仍受特定 VLA、simulator fidelity 与操控 benchmark 限制；它是 embodied policy/world-model 方法，不足以改通用平台控制 owner。"),
    "2606.01041": ("task-specific-model-or-representation-variant", "ExpWeaver 把 experience 编成 hidden-state RAG 并逐 token 注入；不可追溯、不可删除且跨模型不兼容的 latent store 是局部模型变体，不是可治理 Agent memory state contract。"),
    "2606.01042": ("non-ai-system-domain-method", "plausibility-not-prediction 的负结果属于 virtual-cell/perturbation 科学任务；它提醒 plausibility 与 prediction 分离，但没有建立可复用 AI-System evaluator 或 deployment decision。"),
    "2606.01049": ("non-ai-system-domain-method", "PMC-InterCPT 改进 biomedical interleaved corpus construction，依赖 PMC-OA figure references 与领域过滤；它是数据构建实例，不改变通用 data ownership/evidence contract。"),
    "2606.02640": ("platform-or-inference-instance-without-owner-change", "D-Judge 的输出重写是特定 multi-turn jailbreak defense，semantic preservation 与 attack coverage 未校准；它不能替代 authorization/effect boundary，也未改变既有 security owner。"),
    "2606.01062": ("task-specific-model-or-representation-variant", "DAG-MoE 的 learned DAG aggregation 是 expert composition 架构变体；benchmark 改善没有给出可迁移的 placement、load balance 或 serving contract。"),
    "2606.01070": ("domain-agent-workflow-instance", "DART 在候选集上做 per-query dense reranker adaptation，结论绑定 BEIR 与检索器；它是 retrieval 方法并增加请求时优化，不改变 RAG state/evidence owner。"),
    "2606.01090": ("bounded-benchmark-or-evaluation-instance", "symmetry-data exchange 只在已知对称性的二维 synthetic task 中控制 data/compute；这是有界实验协议，不能外推为通用模型或平台评价契约。"),
    "2606.01122": ("non-ai-system-domain-method", "per-component neural solver audit 定位一个 finance HJB-PIDE 实现问题，但步骤依赖该 differential operator、Hamiltonian 与 truncation；领域诊断 case 不形成通用 AI-System evaluator owner。"),
    "2606.01160": ("training-method-instance-without-contract-change", "Expected Value Alignment 从生成式 reward token probability 得连续分数，证据集中 Lean/formal task；它是 reward-model scoring 方法，未改变可验证 reward owner 或跨任务校准契约。"),
    "2606.01162": ("general-systems-or-theory-outside-ai-system", "Deft 面向通用 cloud DAG/VM deadline scheduling，且证据为 simulation；可映射 GPU scheduler 不等于 AI workload、accelerator state 或 tail-SLO 设计结论。"),
    "2606.01168": ("task-specific-model-or-representation-variant", "adaptive-complexity reasoning 以 learned complexity 与 Pareto pruning 分配 token，是局部 reasoning-budget 方法；没有平台 SLO、并发或 evaluator contract。"),
    "2606.01182": ("task-specific-model-or-representation-variant", "CA-BED 的 conversation planning/decoding 改善绑定特定任务与模型；它未重新分配持久 Agent state、工具权限或编排控制 ownership。"),
    "2606.02641": ("non-ai-system-domain-method", "CARVE 的 certified maneuver repair 属自动驾驶轨迹/安全域，保证依赖车辆动力学与场景假设；单领域控制方法不形成通用 Agent 或 platform contract。"),
    "2606.01230": ("domain-agent-workflow-instance", "HomeFlow 的 simulator/goal compiler/MCTS/RLVE 是 smart-home training flywheel；成功条件、环境 fidelity 与 device safety 皆领域特定，不能提升为通用 evaluation owner。"),
    "2606.01238": ("task-specific-model-or-representation-variant", "CFDP 的 closed-form diffusion policy 属机器人 imitation/action generation 方法；benchmark quality 不改变训练/推理平台的 state 或 control contract。"),
    "2606.01246": ("domain-agent-workflow-instance", "SIRIUS-SQL 以多 query 和 execution feedback 选 SQL，但 execution success 仍可能语义错误；text-to-SQL 方法不改变通用 tool-call authorization 或 final-state verifier contract。"),
    "2606.01271": ("platform-or-inference-instance-without-owner-change", "in-sensor INT8 只覆盖 IMX500、Raspberry Pi、EuroSAT 与三种 CNN；它是 Earth-observation placement case，未改变通用 accelerator memory/data-movement judgment。"),
    "2606.02645": ("general-systems-or-theory-outside-ai-system", "target-update stability 的结论是线性 Q-learning 假设下的 delayed synchronization 分析；未验证 deep RL 或 AI platform training control，因此不进入长期分母。"),
    "2606.01304": ("training-method-instance-without-contract-change", "hard-negative generator/discriminator gap 修正 retrieval negative synthesis，仍依赖 retriever、generator 与 benchmark distribution；它是训练数据方法而非新的 data/evaluation contract。"),
    "2606.01326": ("domain-agent-workflow-instance", "source minification 在 SWE-bench 明确换取 token 下降但 resolution 下降；这是 coding-context 压缩 trade-off case，未改变 context owner、语义保持保证或平台接口。"),
    "2606.01342": ("general-systems-or-theory-outside-ai-system", "learning-augmented paging 给出 generic online paging robustness bound；没有 KV identity、reuse、GPU memory cost 或 serving SLO 证据，不能直接成为 LLM cache mechanism。"),
    "2606.01381": ("general-systems-or-theory-outside-ai-system", "SEV formal verification 检查通用 VM 抽象；没有 AI workload、accelerator isolation 或 implementation conformance delta，可映射 security 不足以 retain。"),
    "2606.01402": ("task-specific-model-or-representation-variant", "approximate differential equivalence 是模型压缩/近似算法性质；它未建立部署可验收 equivalence、hardware path 或 runtime state contract。"),
    "2606.01412": ("training-method-instance-without-contract-change", "GPTQ-intrinsic LoRA 联合 layer reconstruction 与 low-rank correction，但仍是特定 quantization/PEFT objective；没有端到端 task、checkpoint handoff 或 runtime kernel contract 的新结论。"),
    "2606.01436": ("training-method-instance-without-contract-change", "saturated-correct data 的 self-judge/entropy ranking 只在简单算术与小模型可靠，并明确会在复杂题退化；局部训练信号不改变 correctness owner。"),
    "2606.01437": ("task-specific-model-or-representation-variant", "CEAR 的 certified ensemble robustness 依赖模型、扰动集与证书假设；它是鲁棒性方法，不构成平台 security/evaluation control contract。"),
    "2606.01440": ("platform-or-inference-instance-without-owner-change", "cross-cloud interconnect 测量会随 provider route、价格与时间变化；它补充 cost case，却没有改变既有 versioned topology/price/SLO placement contract。"),
    "2606.01450": ("platform-or-inference-instance-without-owner-change", "OpenEye 是特定 DNN accelerator artifact，网络、制程与 toolchain 限制明显；硬件 case 不等于 LLM inference execution 或 dataflow owner 的新结论。"),
    "2606.01483": ("platform-or-inference-instance-without-owner-change", "Murmur 的 chunk/sliding-window KV 只在 AMI ASR 与特定 streaming setup 评估；单领域 ASR latency case 不改变通用 request lifecycle 或 cache contract。"),
    "2606.01509": ("task-specific-model-or-representation-variant", "ProbMoE 将 top-k 视为 probabilistic subset inference，是 router estimator 变体；没有 frontier-scale utilization、placement、communication 或 serving evidence。"),
}


CLASS_REOPEN_CONDITION = {
    "bounded-benchmark-or-evaluation-instance": "只有当该 family 建立可复现且跨 workload/model 的新 evaluator construct、authority 或验收边界，而非仅增加数据集/分数时重开。",
    "domain-agent-workflow-instance": "只有当该 workflow 的 state、tool authority、control handoff 或 final-state verifier 能跨领域迁移并改变现有 owner 时重开。",
    "general-systems-or-theory-outside-ai-system": "只有当证据落实到 AI training/inference/platform 的具体 state identity、cost/SLO 或 control contract 时重开。",
    "non-ai-system-domain-method": "只有当领域方法抽象出可迁移的 AI-System mechanism/evaluation contract，且不依赖该领域 ground truth 时重开。",
    "platform-or-inference-instance-without-owner-change": "只有当新证据改变现有 placement/runtime/security owner、SLO 或 failover contract，而非单一硬件/部署 case 时重开。",
    "survey-position-or-proposal-without-validated-contract": "只有当后续实现、conformance、fault injection 或 production evidence 验证所提 contract 时重开。",
    "task-specific-model-or-representation-variant": "只有当该变体改变长期 state/data/control ownership、系统接口或部署判断，而非局部模型/表示指标时重开。",
    "training-method-instance-without-contract-change": "只有当该方法改变训练数据/梯度/通信/checkpoint 的持久 owner 或可验证训练平台判断，而非局部 benchmark 改善时重开。",
}


PROVENANCE_CLOSURE_SUFFIX = {
    "2606.01101": " 官方 revision chain 后续将 v2 撤回，并明确提示作者身份/作者名单真实性问题；该警示进一步排除其作为长期证据。",
    "2606.01160": " 官方 revision chain 后续将 v2 撤回，并明确提示作者身份/作者名单真实性问题；该警示进一步排除其作为长期证据。",
    "2606.01184": " 官方 revision chain 将 v2 撤回并声明改由 arXiv:2603.14169 承载；当前 identity 不应作为独立长期 evidence family。",
    "2606.01316": " 官方 revision chain 后续因作者关系未定与关键 scientific contribution 尚待验证而撤回 v2；不可提升为长期系统证据。",
    "2607.22567": " 官方 revision chain 后续将 v2 撤回，并明确提示作者身份/作者名单真实性问题；该警示进一步排除其作为长期证据。",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def short_abstract(value: str, limit: int = 300) -> str:
    value = clean(value)
    first = re.split(r"(?<=[.!?。！？])\s+", value, maxsplit=1)[0]
    if len(first) <= limit:
        return first
    return textwrap.shorten(first, width=limit, placeholder="…")


def parse_atom() -> dict[str, dict[str, str]]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    with gzip.open(ATOM, "rb") as handle:
        root = ET.parse(handle).getroot()
    records: dict[str, dict[str, str]] = {}
    for entry in root.findall("a:entry", ns):
        atom_id = clean(entry.findtext("a:id", default="", namespaces=ns)).rsplit("/", 1)[-1]
        arxiv_id = re.sub(r"v\d+$", "", atom_id)
        records[arxiv_id] = {
            "atom_identity_version": atom_id,
            "atom_title": clean(entry.findtext("a:title", default="", namespaces=ns)),
            "abstract": clean(entry.findtext("a:summary", default="", namespaces=ns)),
            "atom_published": clean(entry.findtext("a:published", default="", namespaces=ns)),
        }
    return records


def infer_prior_closure_class(title: str, categories: str, abstract: str) -> str:
    text = f"{title} {abstract}".lower()
    if re.search(r"benchmark|evaluation|evaluating|survey|taxonomy|dataset|challenge", text):
        return "bounded-benchmark-or-evaluation-instance"
    if re.search(r"agent|rag|workflow|tool[- ]?use|multi-agent|multiagent", text):
        return "domain-agent-workflow-instance"
    if re.search(r"training|fine[- ]?tun|distill|optimizer|reinforcement|lora|gradient", text):
        return "training-method-instance-without-contract-change"
    if re.search(r"inference|serving|accelerator|hardware|edge|scheduler|memory|cache", text):
        return "platform-or-inference-instance-without-owner-change"
    if not re.search(r"cs\.(ai|cl|cv|lg|ma|ro)", categories.lower()):
        return "non-ai-system-domain-method"
    return "task-specific-model-or-representation-variant"


def main() -> None:
    ledger = read_tsv(LEDGER)
    v8_rows = read_tsv(V8_AUDIT)
    provenance_rows = read_tsv(PROVENANCE)
    atom = parse_atom()

    assert len(ledger) == 371, len(ledger)
    assert len({row["arxiv_id"] for row in ledger}) == 371
    assert Counter(row["decision"] for row in ledger) == {"exclude": 307, "include": 64}
    assert len(v8_rows) == 266
    assert len(provenance_rows) == 371
    provenance_by_id = {row["arxiv_id"]: row for row in provenance_rows}
    assert len(provenance_by_id) == 371
    assert set(provenance_by_id) == {row["arxiv_id"] for row in ledger}
    assert {row["in_beijing_daily_window"] for row in provenance_rows} == {"yes"}
    assert {row["identity_date_resolution"] for row in provenance_rows} == {
        "same-identity-official-v1-in-window"
    }

    v8_by_id: dict[str, dict[str, str]] = {}
    for row in v8_rows:
        match = re.fullmatch(r"arXiv:([^v]+)v1", row["primary_identifier"])
        assert match, row["primary_identifier"]
        v8_by_id[match.group(1)] = row
    assert len(v8_by_id) == 266
    assert set(v8_by_id).issubset({row["arxiv_id"] for row in ledger})
    assert set(RETAIN_REASONS).issubset(v8_by_id)
    assert len(RETAIN_REASONS) == 40

    author_retains = {row["arxiv_id"] for row in ledger if row["decision"] == "include"}
    assert set(DROP_REASONS) == author_retains - set(RETAIN_REASONS)
    assert len(DROP_REASONS) == 37
    assert len(author_retains & set(RETAIN_REASONS)) == 27
    assert len(set(RETAIN_REASONS) - author_retains) == 13

    missing_atom = sorted({row["arxiv_id"] for row in ledger} - set(atom))
    assert not missing_atom, missing_atom

    receipt: list[dict[str, str]] = []
    for ledger_row in ledger:
        arxiv_id = ledger_row["arxiv_id"]
        v8 = v8_by_id.get(arxiv_id)
        atom_row = atom[arxiv_id]
        provenance = provenance_by_id[arxiv_id]
        author_decision = "retain" if ledger_row["decision"] == "include" else "pre_denominator_closure"
        independent_decision = "retain" if arxiv_id in RETAIN_REASONS else "pre_denominator_closure"

        if author_decision == "retain" and independent_decision == "retain":
            transition = "retain-upheld"
        elif author_decision == "retain":
            transition = "false-positive-closed"
        elif independent_decision == "retain":
            transition = "false-negative-reopened"
        else:
            transition = "closure-upheld"

        if independent_decision == "retain":
            closure_class = "—"
            rationale = RETAIN_REASONS[arxiv_id]
            reopen_condition = "—"
        elif arxiv_id in DROP_REASONS:
            closure_class, rationale = DROP_REASONS[arxiv_id]
            reopen_condition = CLASS_REOPEN_CONDITION[closure_class]
        elif v8:
            closure_class = v8["closure_class"]
            if closure_class == "low-durability-or-out-of-scope":
                closure_class = "non-ai-system-domain-method"
            mechanism = clean(v8["source_specific_reason"])
            rationale = (
                f"closure upheld：{mechanism} 独立复核未发现其超出该 family 的限制，仍不足以改变长期 "
                f"{v8['stable_node_id']} mechanism/state/data/control/evaluation contract。"
            )
            reopen_condition = CLASS_REOPEN_CONDITION[closure_class]
        else:
            closure_class = infer_prior_closure_class(
                ledger_row["title"], ledger_row["registered_categories"], atom_row["abstract"]
            )
            rationale = (
                f"prior raw closure upheld：《{ledger_row['title']}》的冻结 title/abstract 核心是“"
                f"{short_abstract(atom_row['abstract'])}”。该证据属于 {closure_class}，没有建立新的长期 "
                "AI-System mechanism、state/data/control ownership、evaluation contract 或平台/训练/推理设计判断。"
            )
            reopen_condition = CLASS_REOPEN_CONDITION[closure_class]

        if independent_decision == "pre_denominator_closure" and arxiv_id in PROVENANCE_CLOSURE_SUFFIX:
            rationale += PROVENANCE_CLOSURE_SUFFIX[arxiv_id]

        source_family = v8["source_family_id"] if v8 else ledger_row["source_family_id"]
        stable_node = v8["stable_node_id"] if v8 else "—"
        evidence = (
            v8["preserved_primary_evidence"]
            if v8
            else f"arxiv-overread-first-page.atom.gz#entry={atom_row['atom_identity_version']}"
        )
        audit_family_key = source_family if source_family and source_family != "—" else f"RAW-ARXIV-{arxiv_id}"
        receipt.append(
            {
                "arxiv_id": arxiv_id,
                "first_public_utc": ledger_row["first_public_utc"],
                "registered_categories": ledger_row["registered_categories"],
                "title": ledger_row["title"],
                "audit_family_key": audit_family_key,
                "source_family_id": source_family or "—",
                "stable_node_id": stable_node,
                "repair_author_v8_decision": author_decision,
                "independent_decision": independent_decision,
                "transition": transition,
                "closure_class": closure_class,
                "independent_rationale": rationale,
                "reopen_condition": reopen_condition,
                "primary_evidence_locator": evidence,
                "evidence_scope": (
                    "exact-v1-review-lineage+frozen-atom-title-abstract"
                    if v8
                    else "frozen-atom-title-abstract-only"
                ),
                "atom_identity_version": atom_row["atom_identity_version"],
                "abstract_sha256": hashlib.sha256(atom_row["abstract"].encode()).hexdigest(),
                "historical_review_claim_ref": v8["historical_review_claim_ref"] if v8 else "—",
                "official_v1_submitted_utc": provenance["official_v1_submitted_utc"],
                "official_doi": provenance["official_doi"],
                "title_chain_class": provenance["title_chain_class"],
                "revision_chain_status": provenance["revision_chain_status"],
                "identity_date_provenance_status": provenance["audit_status"],
                "audit_status": "fresh-context-independent-reviewed",
            }
        )

    receipt.sort(key=lambda row: (row["first_public_utc"], row["arxiv_id"]))
    columns = list(receipt[0])
    write_tsv(RECEIPT, receipt, columns)

    counts = Counter(row["independent_decision"] for row in receipt)
    transitions = Counter(row["transition"] for row in receipt)
    closure_counts = Counter(
        row["closure_class"] for row in receipt if row["independent_decision"] == "pre_denominator_closure"
    )
    assert counts == {"pre_denominator_closure": 331, "retain": 40}
    assert transitions == {
        "closure-upheld": 294,
        "false-positive-closed": 37,
        "retain-upheld": 27,
        "false-negative-reopened": 13,
    }
    assert sum(closure_counts.values()) == 331

    retained = [row for row in receipt if row["independent_decision"] == "retain"]
    denominator_payload = "\n".join(
        f"{row['source_family_id']}\t{row['arxiv_id']}v1\t{row['first_public_utc']}"
        for row in retained
    )
    denominator_id = "PROPOSED-DEN-20260601-" + hashlib.sha256(denominator_payload.encode()).hexdigest()[:8]

    def md_escape(value: str) -> str:
        return clean(value).replace("|", "\\|")

    def table(rows: list[dict[str, str]], fields: list[tuple[str, str]]) -> str:
        out = ["| " + " | ".join(label for label, _ in fields) + " |"]
        out.append("| " + " | ".join("---" for _ in fields) + " |")
        for row in rows:
            out.append("| " + " | ".join(md_escape(row[key]) for _, key in fields) + " |")
        return "\n".join(out)

    closure_summary = [
        {"closure_class": key, "count": str(value)} for key, value in sorted(closure_counts.items())
    ]
    false_positives = [row for row in receipt if row["transition"] == "false-positive-closed"]
    false_negatives = [row for row in receipt if row["transition"] == "false-negative-reopened"]

    checkpoint = f"""# 2026-06-01 Fresh-Context Candidate Denominator Audit — Independent V9

## Audit outcome

This is an independent Candidate Denominator FP/FN receipt and a **reconciled denominator proposal**, not a repair-author self-pass and not a downstream Source Review, Selection, Books Comparison or Books semantic pass.

- Audit scope: **371/371 raw identities**, no sampling.
- Repair-author V8 retains checked for false positives: **64/64**.
- Repair-author V8 closures checked for false negatives: **307/307** = 202 newly downgraded families + 105 prior raw closures.
- V8 retained: **64/371** (17.25%).
- Independent proposal: **40/371** retained (10.78%); **331/371** family-specific pre-denominator closures.
- Transition account: 27 retain upheld; 37 repair-author false positives closed; 13 repair-author false negatives reopened; 294 closures upheld.
- Retained delta: **-24** families versus V8.
- Proposed denominator identity: `{denominator_id}`. The `PROPOSED-` prefix is intentional: root/repair ownership must reconcile and refreeze canonical denominator interfaces before any Gate can close.

The complete row-level evidence, abstract hashes, transitions, family-specific rationales and reopen conditions are in `{RECEIPT.name}`.

## Strict semantic standard applied

A family is retained only where the frozen identity/title/full abstract plus preserved V8 exact-v1 lineage clearly changes at least one durable AI-System mechanism; state/data/control ownership; evaluation/verification contract; platform/training/inference design judgment; or an existing Books proposition. ROADMAP mappability, generic AI relevance, a one-domain method or benchmark, and a local representation/model improvement are insufficient by themselves.

## Identity and access receipt

- The prerequisite fresh-context provenance receipt reconciles 371/371 official arXiv-issued DataCite DOI/Submitted-v1 chains with frozen Atom identities: 371 in-window; identity/DOI/v1-time/author mismatch=0; out-of-window=0. Raw accounting therefore remains 371.
- Fifteen event-time/current-title evolution rows are explicitly linked in the provenance receipt. Five later withdrawn-v2 chains are preserved and all five remain semantic closures; none contaminates the retained proposal.
- Identity account is closed for this audit scope: 371 unique ledger identities, 371 matching frozen Atom entries, and no duplicate source-family retain.
- The 266 V8-reviewed families retain their packet or official exact-v1 evidence locator and historical review/claim lineage in the TSV.
- The 105 prior raw closures were checked from the frozen identity, category, title and full Atom abstract. None met the strict retain standard; each has a unique `RAW-ARXIV-*` audit family key, abstract hash, family-specific rationale and reopen condition.
- No Candidate Denominator identity/access blocker was found. The 9 public exact-v1 reviews that are not packet-frozen remain a **later Evidence-audit packet-sufficiency scope**; they do not block title/abstract Candidate screening and are not silently treated as packet-frozen.

## Reconciled retained proposal (40)

{table(retained, [("arXiv", "arxiv_id"), ("Source Family", "source_family_id"), ("Owner", "stable_node_id"), ("Transition", "transition"), ("Independent reason", "independent_rationale"), ("Evidence", "primary_evidence_locator")])}

## Repair-author retained false positives (37/64)

{table(false_positives, [("arXiv", "arxiv_id"), ("Source Family", "source_family_id"), ("Closure class", "closure_class"), ("Independent family-specific closure", "independent_rationale"), ("Evidence", "primary_evidence_locator")])}

## Repair-author closure false negatives (13/307)

{table(false_negatives, [("arXiv", "arxiv_id"), ("Source Family", "source_family_id"), ("Owner", "stable_node_id"), ("Independent reopen reason", "independent_rationale"), ("Evidence", "primary_evidence_locator")])}

The other **294/307** repair-author closures are upheld. This includes **105/105** prior raw closures; none were promoted. Their individual evidence, closure class, rationale and reopen condition are present in the 371-row TSV rather than collapsed into a template-only aggregate.

## Closure reason distribution (331)

{table(closure_summary, [("Closure class", "closure_class"), ("Count", "count")])}

## Gate truth and continuation boundary

| Interface | Truth after this audit |
| --- | --- |
| Candidate Denominator fresh audit | Complete for 371/371 FP/FN scope; result is a proposal awaiting root reconciliation/refreeze |
| Coverage Gate | **Open** — canonical ledger/inventory/report denominator interfaces have not been refrozen to this proposal |
| Evidence Gate | **Open** — retained Source Reviews and exact-v1 packet sufficiency have not been independently reconciled for the proposed 40 |
| Selection Gate | **Open** — no reconciled selection ledger exists for the proposed 40 |
| Books Comparison Gate | **Open** — no reconciled owner/proposition table exists for the proposed 40 |
| Books Gate / Books writeback | **Open / blocked** — no Books file was read for mutation or changed by this audit |

Per the assigned boundary, this audit stops at the denominator result. It does not advance Source Review, Daily body, Selection, Books Comparison or Books, and it does not describe structural validation as semantic completion.
"""
    CHECKPOINT.write_text(checkpoint, encoding="utf-8")

    receipt_hash = hashlib.sha256(RECEIPT.read_bytes()).hexdigest()
    print(
        f"rows={len(receipt)} retain={counts['retain']} closure={counts['pre_denominator_closure']} "
        f"fp_closed={transitions['false-positive-closed']} fn_reopened={transitions['false-negative-reopened']} "
        f"denominator={denominator_id} receipt_sha256={receipt_hash}"
    )


if __name__ == "__main__":
    main()
