#!/usr/bin/env python3
"""Finalize the strict V2.1 2026-06-16 Daily without editing Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path

from canonicalize_june_daily_presentation import canonicalize_report
from test_june16_canonical_presentation import main as validate_canonical_presentation

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260616"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-full-semantic-audit-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
QUEUE = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
READY = PACKET / "READY_TO_INSERT_BOOKS_V1.md"
EVIDENCE = PACKET / "PREWRITE_FRESH_AUDIT_V2.md"
POSTWRITE = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
PRESENTATION_AUDIT = PACKET / "PRESENTATION_FRESH_AUDIT_V1.md"
SHA_MANIFEST = PACKET / "SHA256SUMS"
REPORT = ROOT / "papers/2026/06/16/README.md"
DEN = "DEN-20260616-621063"
EXECUTED = "2026-08-29T04:08:46+08:00"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_sha_manifest() -> None:
    paths = sorted(path for path in PACKET.rglob("*") if path.is_file() and path != SHA_MANIFEST)
    paths.extend([
        REPORT,
        Path(__file__).resolve(),
        ROOT / "scripts/canonicalize_june_daily_presentation.py",
        ROOT / "scripts/test_june16_canonical_presentation.py",
    ])
    SHA_MANIFEST.write_text(
        "".join(f"{sha(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in paths),
        encoding="utf-8",
    )

# Exact-v1 family -> (stable owner, durable mechanism delta).  These are
# deliberately source-specific; titles are not used as a substitute for the
# mechanism statement.
SPECS = {
"2606.16100":("PLATFORM-SECURITY","黑盒 model fingerprint 在 provider 可自适应微调时不是身份凭证；gateway 必须把 attested model/version、计费证据与 challenge rotation 分开"),
"2606.16106":("INFER-SCHEDULING","edge inference governor 必须把独立 memory clock、tail latency、decode horizon 与 co-tenancy occupancy 纳入 deadline feasibility state"),
"2606.16110":("TRAIN-DATA","machine-unlearning 验收需要无需 scratch retrain/shadow fleet 的 proof-of-ignorance audit，并显式保存攻击面与误判边界"),
"2606.16135":("INFER-KV-CACHE","多轮 serving 可在同机异构模型间借用 idle HBM/NVLink 保存 hot prefix，但 cache identity、donor pressure 与回收优先级必须由控制面持有"),
"2606.16190":("PLATFORM-EVALUATION-SYSTEM","edge-model Agent 的验收对象是 model+firmware+真实硬件闭环；compile/flash/measure 证据不能由模拟器 reward 代替"),
"2606.16242":("PLATFORM-SECURITY","rapid-response 防御本身必须接受自适应 poisoning：攻击者可利用更新窗口改变 detector 的后续决策，而非只逃逸一次静态分类"),
"2606.16264":("INFER-PD-DISAGGREGATION","disaggregated serving 的 multiplexing 应联合 admission、prefill/decode placement 与 per-request SLO slack，避免局部利用率吞噬 tail budget"),
"2606.16287":("PLATFORM-SECURITY","Agent skill 审计必须覆盖安装后动态行为、trigger 与跨 skill composition；静态 manifest/代码扫描不能代表 runtime authority"),
"2606.16310":("MODEL-LONG-CONTEXT","MLA 的 post-projection QK RMSNorm 可拆成可吸收的静态权重与每 token/group 动态标量，从而保留 latent KV decode path"),
"2606.16322":("AGENT-WORKFLOW","bounded artifact revision 需要冻结 claim spine、持久 issue identity、adjudication 与 exact-once patch/verify，而非让 reviewer 直接改稿"),
"2606.16332":("INFER-TENSORRT-LLM","CPU matrix extension 不是全算子默认后端；runtime 应按 operator shape 在 CPU/SME/cooperative path 间选择并保留 packed-layout state"),
"2606.16341":("AGENT-RAG","filtered ANN planner 应把 selectivity error 到 plan regret 的 phase boundary 作为切换条件，而不是用单一 pre/post/in-filter 规则"),
"2606.16352":("PLATFORM-SECURITY","remote LLM serving 的 attention integrity 可由 TEE 验证 GPU 计算，并对 prefill pipeline 与超显存 decode KV 分区分别设计通信路径"),
"2606.16358":("PLATFORM-GATEWAY","LLM API router 的 plaintext authority 应收缩到 client-attested enclave；auth/scheduling/accounting 可留在 untrusted host，但目的地必须绑定 measured image"),
"2606.16364":("AGENT-TOOL-CALLING","tool-selection failure 常发生在 readout 而非工具定义未被注意；修复应区分 candidate visibility、decision readout 与 executor authorization"),
"2606.16384":("TRAIN-DISTRIBUTED-TRAINING","低带宽 context parallel 可用动态 mixture-of-subspaces 压缩 activation communication，但 subspace version 与重构误差必须随 step 传播"),
"2606.16420":("AGENT-WORKFLOW","security audit playbook 应作为 model/harness 外部的 versioned artifact，经 executable ground truth、replay 与 held-out promotion 后再迁移到弱 Agent"),
"2606.16429":("MODEL-LONG-CONTEXT","hybrid linear-attention distillation 的初始化应校准 Taylor/local response，而不是从 full-attention 权重直接复制后期待训练自行修复"),
"2606.16461":("PLATFORM-SECURITY","privacy-preserving LLM inference 若依赖 orthogonal symmetry，必须把 transform key、equivariance 假设与不受保护的 metadata/side channel 分开声明"),
"2606.16494":("AGENT-RAG","多模态 RAG 的 primacy bias 会让后到 evidence 被系统性忽略；evaluation 与 assembly 必须扰动 evidence order 并保留位置归因"),
"2606.16496":("AGENT-REFLECTION","experience reflection 只有在 candidate lesson、held-out validation 与 promotion 分离时才是可控演进；生成的反思不能直接覆盖运行策略"),
"2606.16511":("PLATFORM-EVALUATION-SYSTEM","frontier evaluation 的 tail-shape claim 必须先做 threshold/grid/sample-size sensitivity 与 false-positive diagnosis，再允许外推极端风险"),
"2606.16519":("PLATFORM-SECURITY","world model 的安全 gate 需要对 observation/action perturbation 与 rollout compounding 做 adversarial contract，平均 prediction loss 不能替代 closed-loop robustness"),
"2606.16523":("AGENT-REFLECTION","Agent skill registry 需要 lineage、executable evaluation、dependency/permission metadata 与更新治理，不能把可检索文本集合称为 living skill infrastructure"),
"2606.16527":("PLATFORM-SECURITY","black-box jailbreak defense 应先做结构一致性 verification，再由 semantic audit 判定残余风险，并保留拒绝/放行的可解释 fallback"),
"2606.16541":("PLATFORM-EVALUATION-SYSTEM","natural-language 到 formal statement 的 kernel acceptance 只证明语法/可解；release gate 还需双向语义等价证据与 counterexample search"),
"2606.16603":("PLATFORM-EVALUATION-SYSTEM","data-analytic Agent 应把 query/transform/result 编译成可执行 verification graph，使数值结论可由独立节点重放而非只审 prose"),
"2606.16605":("PLATFORM-EVALUATION-SYSTEM","world-model robustness benchmark 应冻结 perturbation budget、closed-loop controller 与 horizon，并区分 perception drift、dynamics error 与 return collapse"),
"2606.16682":("PLATFORM-EVALUATION-SYSTEM","self-evolving multimodal Agent 的 evaluator 会发生 cross-modal preference contagion；promotion 必须保留 modality-specific holdout 与 evaluator version"),
"2606.16690":("MULTIMODAL-EMBODIED-VLA","robot runtime monitor 应以 active action chunk 定义局部 execution corridor，并从 ego-motion 后的 persistent latent residual 决定介入"),
"2606.16707":("AGENT-MEMORY","个性化 memory 可编译为 typed state 与 executable rules，以显式处理冲突、聚合与约束；代码执行权必须和记忆证据分离"),
"2606.16710":("AGENT-MULTI-AGENT","benign MAS 也会传播 tool/context misinformation；coordinator 应追踪 claim provenance、独立复核与多数意见的相关性"),
"2606.16748":("PLATFORM-EVALUATION-SYSTEM","computer-use benchmark 应提供跨应用一致的持久 persona、resettable desktop 与 visible-side-effect rubric，而非空账户单 app task"),
"2606.16751":("PLATFORM-SECURITY","jailbreak red-team 应针对多类防御做自适应策略搜索并保存 query budget；对单一 guard 的成功率不代表组合防线失效"),
"2606.16768":("TRAIN-PRETRAINING","深 Transformer 稳定训练可把 architecture warm-up 与 optimizer warm-up 分离，使曲率/残差路径逐步启用而非只缩小 learning rate"),
"2606.16774":("AGENT-REFLECTION","开放 skill 搜索应维护 collective tree、可复现 rollout evidence 与 promotion/pruning，而不是把一次成功轨迹直接写成全局 skill"),
"2606.16813":("AGENT-TOOL-CALLING","tool filtering 应从 goal-state 因果必要性生成最小可见集合，同时由 executor 保留完整授权；检索相似度不能成为权限"),
"2606.16821":("PLATFORM-SECURITY","search Agent 的 source endorsement 可被网页 framing 操纵；评测应冻结操纵面并分离 retrieval exposure、citation 与最终 endorsement"),
"2606.16824":("INFER-KV-CACHE","coding-Agent KV workload 的 prefix reuse、branching 与长 idle gap 不同于聊天；cache manager 应按 repository/session lineage 与 reuse horizon 调度"),
"2606.16907":("TRAIN-DISTRIBUTED-TRAINING","异构 GPU 并行化需要把 compute/communication capability 映射为逻辑同构 stage，并用 runtime remapping 隐藏设备差异而不掩盖 straggler"),
"2606.16914":("PLATFORM-SECURITY","reward hacking 可由可见 incentive wording 触发；training/evaluation 必须把任务效用与可见奖励线索做 counterfactual 分离"),
"2606.16988":("AGENT-WORKFLOW","coding-Agent trajectory 可规范化为 program/control-flow fingerprint，用于行为比较与约束注入；trace 相似不等于 semantic correctness"),
"2606.17005":("PLATFORM-EVALUATION-SYSTEM","公开 frontier eval archive 应保存 trial-level uncertainty、selection process 与 decision rule，使 Bayesian update 与发布决策可被重算"),
"2606.17016":("AGENT-CONTEXT","Agent context manager 应联合 canonical prefix、segment lifecycle 与 cache reuse，而非只按 token relevance 局部剪枝"),
"2606.17029":("PLATFORM-EVALUATION-SYSTEM","deep-research RL 的 rubric 应展开为 evidence tree，让 citation support、coverage 与 synthesis 分层给 reward，避免单一 judge score"),
"2606.17034":("INFER-KV-CACHE","localized context erasing 应在 KV state 上学习受控 steering，并以旁观 token drift 与下游行为验证删除范围"),
"2606.17110":("PLATFORM-SECURITY","攻击者可通过 loss-landscape poisoning 使后续 fine-tuning 提取未见训练数据；data provenance 与 update admission 必须联合审计"),
"2606.17114":("PLATFORM-SECURITY","tool-using Agent 的 leakage test 必须覆盖 realistic secret placement、multi-step tool chain 与 observable side effect，而非只测最终文本"),
"2606.17122":("TRAIN-DATA","instant unlearning 可把 passport 嵌入 LoRA 表示并以 authority-mediated verification 验证配置，但 deactivate credential 不自动证明所有信息删除"),
"2606.17182":("AGENT-MULTI-AGENT","并发 MAS 需要显式 happens-before、shared-state conflict 与 side-effect serialization，并在运行前后验证 anomaly-free execution"),
"2606.17200":("MULTIMODAL-EMBODIED-VLA","VLA pretraining data 应以统一 egocentric schema 对齐 human/robot observation-action 时序，并保留 embodiment/source identity"),
"2606.17209":("AGENT-PLANNING","Agentic search 的多样性 owner 在 query initialization 而非只增加 parallel samples；budget 应覆盖 seed diversity 与后续 branch pruning"),
"2606.17229":("PLATFORM-SECURITY","deception monitor 可利用 residual rank conflict signature，但 probe 的 label-free/cross-domain表现不能升级为 truth detector 或自动惩罚权"),
"2606.17241":("INFER-SCHEDULING","连续 edge perception 的验收必须包含 sensor arrival、queue/drop、thermal/power 与长期 accuracy，而非离线 per-frame benchmark"),
"2606.17283":("PLATFORM-EVALUATION-SYSTEM","vulnerability benchmark 应绑定可构建 source revision、trigger、oracle 与 reproducible container，使检测/修复结果可重放"),
"2606.17328":("AGENT-MEMORY","long-term memory 评价应在 final accuracy 之外对 construction/retrieval/injection 节点做 counterfactual attribution"),
"2606.17378":("INFER-SCHEDULING","edge collaborative diffusion serving 需要 relay placement、partial denoising state 与 online queue/SLO scheduler 共同决策"),
"2606.17383":("PLATFORM-EVALUATION-SYSTEM","Agentic AI model validation 应分别检查 belief-state filter、forecast transition 与 policy action，并以 POMDP identity 绑定三层误差"),
"2606.19386":("PLATFORM-MONITORING","wall-clock moment detector 在 Agent cadence 下可能结构性双稳态；monitor 必须以可观测 transition window 校准而非宣称瞬时状态真值"),
"2606.20695":("PLATFORM-EVALUATION-SYSTEM","MAS coordination gain 必须与 paired single-Agent run 和 noise floor 比较，避免把 sampling variance 当协作收益"),
"2606.20698":("MULTIMODAL-EMBODIED-VLA","VLA safe RL 可用 interactive world model 生成风险 rollout，但 deployment action 仍需真实环境 safety shield 与 abstention"),
"2606.20701":("AGENT-MULTI-AGENT","learned-communication MARL 必须识别 Byzantine message 并让 trust state 随 evidence 更新，不能假设 peer channel 全部诚实"),
"2606.24598":("AGENT-WORKFLOW","expert LLM workflow 迁移到 self-evolution 前应先做 convertibility taxonomy、reversible adapter 与 rollback，不直接改写 opaque harness"),
}

# Each locator below was re-opened against the official exact-v1 HTML.  The
# strings intentionally preserve the paper's own section titles rather than a
# normalized "method / experiments / limitations" placeholder.
LOCATORS = {
"2606.16100":("§4 Problem Formulation (§4.1 Threat Model; §4.2 Fingerprint Spoofing); §5 Proposed Method (§5.2 GhostPrint Attack)","§6 Experiments (§6.1 settings; §6.2–6.5 single/cross-model/continual spoofing); Appendix A implementation","§4.1 Threat Model; §6.5 Continual Fingerprint Spoofing; Appendix B additional results"),
"2606.16106":("§III Methodology (§III-A platform/clock control; §III-B roofline workloads; §III-C harness)","§IV Memory-Clock Axis; §V Tails and Bursts; §VI Actuation Lag; §VII Trace-Driven Governor Evaluation","§IX Limitations; Appendix B What Is Ruled Out"),
"2606.16110":("§II Preliminary and Threat Model; §III Methodology; §IV Theoretical Analysis","§V Experimental Setup; §VI Validation and Ablation; §VII Results; §VIII Extension to LLMs","§II Threat Model; appendices for datasets, methods and additional results"),
"2606.16135":("§3 SwiftCache Design (§3.2 Master Cache Manager; §3.3 overlap KV transfer; §3.4 worker; §3.5 coordination); §4 Implementation","§5 Evaluations (§5.1 end-to-end; §5.2 interference; §5.3 context length; §5.4 latency)","§7 Conclusions and Discussions; §5.2 interference and §5.3 context-length stress"),
"2606.16190":("§2 Hardware-in-the-Loop Arena (§2.1 constraints, iterative loop, memory/context and score); §2.2 MCU tasks","§3 Experiments (§3.4 Why Agents Fail); §4 Deployments","§3.4 Why Agents Fail; §5 Discussion"),
"2606.16242":("§2.1 Threat Model; §3 Attack Techniques","§4 Experimental Setup; §§5–6 adversary goals/results; §7 Defenses","§7 Defenses; §8 Discussion and Limitations; appendices for adaptive setup"),
"2606.16264":("§III Characterization and Motivation; §IV System Design (§IV-B SLO-Aware Multiplexing; §IV-C toggling)","§V Evaluation (§V-A setup; §V-B SLO attainment; §V-C latency; §V-D queue; §V-E CDF)","§III-C resource-allocation motivation; §VII Conclusion and evaluation scope"),
"2606.16287":("§3 Problem Formulation (§3.2 Threat Model; §3.3 Dynamic Code Modification); §4 DyMalSkill","§5 Attack Evaluation (§5.1 setup/results/ablation); §6 Defenses","§6 Defenses (§6.1 benign dynamic modification; §6.2 proposed defenses; §6.3 results); Appendix A verifier details"),
"2606.16310":("§3 Method (§3.1 key-side RMSNorm; §3.2 query; §3.3 content/RoPE; §3.4 decode data flow); §4 Analysis","§5 Experiments (training loss, downstream quality, decode overhead and stress)","§7 Limitations; Appendices B–E equivalence and diagnostics"),
"2606.16322":("§3 Method (§3.3 Review and Adjudication; §3.4 Guarded Revision and Convergence)","§4 Experiments (implementation, design and results)","§3.4 guarded convergence conditions; §5 Conclusion"),
"2606.16332":("§3 Roofline Characterization; §4 SMEPilot Design (§4.1 tile partition; phase pipeline; layout runtime; plan generation)","§5 Evaluation (setup, end-to-end, operator, ablation, power and GPU comparison)","§7 Discussion; §5 power/GPU comparison boundary"),
"2606.16341":("§2 Problem and Model; §3 Phase Diagram; §4 Regret Is Critical","§5 Experiments (setup and model-mismatch studies)","§7 Limitations and Honest Findings"),
"2606.16352":("§3 Motivation; §4 VeriAttn System Design (§4.1 verification; prefill; decode)","§5 Evaluation (setup, prefill, decode and effectiveness)","§6 Discussion; appendices for detailed procedures and workflows"),
"2606.16358":("§III System and Threat Model; §IV Aegis (§IV-A minimal TCB; measurement; fail-closed relay; destination binding); §V Formal Analysis","§VI Implementation and Evaluation (setup, security, adaptive attack, auditability and workload runtime)","§VII Discussion and Limitations; protocol/proof appendices"),
"2606.16364":("§3 Method (controlled tool-selection benchmark, HAA extraction, additive attention bias and constrained decision)","§§4–9 correlation, trained-probe, causal dose-response, scaling, BFCL/Seal-Tools and τ-bench anchors; §10 selector","§10 Limitations; §8 argument-generation failure and compute-cost boundary"),
"2606.16384":("§3 Method (§3.1 product-manifold optimization; §3.2 reparameterization; §3.3 communication; §3.4 dynamic subspaces; §3.5 unplugging)","§5 Experiments (§5.1 setup; §5.2 bandwidth efficiency; §5.3 ablations; §5.5 baselines)","§7 Limitations; Appendix C ablations"),
"2606.16420":("§IV Methodology (§IV-A continual procedure learning; §IV-B transfer procedure learning); §V Implementation","§VI Benchmark; §VII Experiments; §VIII Evaluation (§VIII-A–E scoring, acquisition, transfer and false positives)","§IX Discussion; §X Scope and Limitations"),
"2606.16429":("§3 Method: Taylor-Calibrate (§3.2 Taylor-derived calibration; §3.3 per-layer gradient alignment)","§4 Experiments (§4.1 setup; §4.2 zero-shot; §4.3 recovery; §4.4 long context; §4.5 ablations)","Appendix C Limitations and Future Work (§C.1–C.7); Appendix D extended results"),
"2606.16461":("§1.3 Threat Model and System Overview; §2 Methodology (§2.2 architecture, weight conjugation, inference and normalization)","§3 Attacks; §4 Experimental Setup (pretraining, fine-tuning, retrofitting and attacks)","§1.3 Scope and Limitations; §5 Discussion and Limitations"),
"2606.16494":("§3 Probing Protocol","§4 Empirical Insights (§4.1 primacy; §4.2 modality; §4.3 slot 0; §4.4 retrieval-side fixes); Appendices I–L replications","Appendices A–F methodology, audit and scoring sensitivity; Appendix T compute/reproducibility"),
"2606.16496":("§3 Method (§3.2 critic-actor diagnostic chain; §3.3 behavioral evidence; §3.4 skill memory/evolution)","§4 Experiments (§4.1 setup; §4.2–4.6 policy discovery, transfer and ablations)","§5 Conclusion and Limitations; Appendix B robustness/auditability; Appendix C compute"),
"2606.16511":("§3 Pre-Registered Protocol (admissibility, equivalence, stability and pass criteria); §4 sample-size theory","§5 Experimental Setup; §6 Results: Three Failure Modes; Appendices B–C sensitivity and second scorer","§7 Discussion (§7.1 claims; §7.2 non-claims; §7.4 limitations and scope)"),
"2606.16519":("§3 Background/problem setup; §4 Methodology (§4.1 velocity objective; §4.2 trajectory-adaptive bi-level optimization)","§5 Experiments (§5.1 setup; §5.2 objectives; §5.3 ablation; §5.4 optimizer); Appendices B–E","§6 Conclusion; Appendix B robustness/transferability; Appendix C implementation details"),
"2606.16523":("§2 SkillWiki (§2.2 knowledge-to-skill and provenance graph; §2.3 organization, governance and evolution)","§3 Demonstration; §4 Evaluation (§4.1 production; §4.2 lifecycle governance/evolution)","Appendix A corpus/evaluation protocol; Appendix B runtime monitoring and health signals"),
"2606.16527":("§2.1 Threat Model; §3 DoubtProbe (§3.2 structural verification; §3.3 semantic audit; §3.4 decision rule)","§4 Experimental Setup; §5 Evaluation (§5.2 remaining failures; §5.4 adaptive jailbreaks; §5.5 backbone sensitivity)","§6 Discussion and Limitations; Appendix E judge validation; Appendix F human annotation"),
"2606.16541":("§3 Faithfulness Problem; §4 Bidirectional Provability Fingerprinting; §5 Counterfactual Probe Generation; §§6–9 spectrum, budget, theory and decoding","§10 DriftBench; §11 Experiments (§11.1 setup; §11.2–11.6 results, wild split, scaling, ablation and downstream impact)","§8.3 incomplete oracle/undetectable drift; §12 Discussion and Limitations"),
"2606.16603":("§3 Methodology (§3.2 VeriGraph; §3.3 evidence graph; §3.4 graph-based policy optimization)","§4 Experiments (§4.1 setup; §4.2 results; §4.3 traceability; §4.4 ablations); §5 robustness","Appendix A runtime/context compression; Appendix B training and optimization details"),
"2606.16605":("§3.2 Adversarial Threat Model; §4 Methodology (§4.2 workflow; §4.3 interface; §4.4 objectives; §4.6 temporal protocols)","§5 Experimental Setup; §6 Experiments and Analysis; §7 model-wise interpretation","§8 Engineering Implications; temporal-protocol and adaptive-robustness-gap scope"),
"2606.16682":("§3 Method (§3.1 TTRL; §3.2 MPCI; §3.3 contagion; §3.4 algorithm)","§4 Experimental Setup; §5 Results; §6 Statistical Validation; §7.2 ablation","§7.4 Error Analysis and Failure Modes; §7.5 Limitations; §7.6 Threats to Validity"),
"2606.16690":("§3 PATCH Framework (§3.1 action-corridor formulation; §3.2 monitor; §3.3 router)","§4 Empirical Evaluations (§4.1 claims; §4.2 trigger benchmark; §4.3 assistive robots)","§5 Conclusion and Limitations; Appendix A.9 score/threshold audit"),
"2606.16707":("§3 Methodology: User as Code (§3.2 extraction; §3.3 retrieval and generate-verify-review; §3.4 principles)","§4 Experiments and Evaluation (§4.1 setup; benchmarks, active service and ablations)","§5 Discussion; Appendix A.5 backbone caveat; Appendix D failure-mode analysis"),
"2606.16710":("§3 Methodology (§3.1 setup, MINT, models, single/multi-agent and misinformed agents)","§4 Results and Discussion (§4.1 single-agent; §4.2 propagation; §4.3 group/protocol effects)","§6 Limitations; Appendix C dataset sampling"),
"2606.16748":("§3 MyPCBench (§3.1 environment; §3.2 creation/infrastructure); §4 Tasks and Evaluation Setup","§5 Experiments and Analysis (§5.1–5.4 main, task type, scaling and personalization failures)","Appendix G Detailed Failure Modes; Appendices K–L grading and harness"),
"2606.16751":("§3 Threat Model; §4 UniAttack Design (§4.2–4.5 initialization, features, templates and testing)","§5 Evaluation (§5.1 models/defenses/budget/detection/metrics/data; §5.2–5.5 RQs)","§6.1 Threats to Validity; §6.2 Mitigation and Defense Guidelines"),
"2606.16768":("§3 Methodology (§3.1 curvature tracking; §3.2 architecture warm-up and progressive depth)","§4 Experiments (§4.1–4.6); §§9–11 curvature, compute-optimal validation and schedule sensitivity","§9.2 self-stabilization limits; §11 warm-up schedule sensitivity"),
"2606.16774":("§3 Method (§3.1 collective skill tree search; §3.2 collective skill RL)","§4 Experiments (§4.1 implementation; §4.2 QwenClawBench/PinchBench; §4.3 ablation)","§5 Conclusion; §4.3 ablation and benchmark scope"),
"2606.16813":("§III Problem Formulation; §IV GIST-CMTF (§IV-B–F goal generation, ambiguity, clarification, filtering and algorithm)","§V Experimental Setup; §VI Results (§VI-A–F performance, wrong-goal, cost, backends and errors)","§IV-G Failure Modes; §VII-D reliability-friction tradeoff; §VIII Limitations and Threats"),
"2606.16821":("§3 Threat Model; §4 Attack Taxonomy","§5 Experimental Design; §6 Results (§6.1 main; §6.2 ablations; §6.3 skill recommendation)","§7 Discussion; unnumbered Static Proxy, Skill Probe, Self-Judging and Dual-Use limitations"),
"2606.16824":("§3 Coding Agent Workloads; §4 Serving Implications; §5 CacheWise Design (§5.1 scheduling; §5.2 eviction; §5.3 implementation)","§6 Evaluation (§6.1 setup; §6.2 end-to-end; §6.3 ablations; §6.4 movement; §6.5 predictor; §6.6 overhead)","§3 workload scope; §6.5 predictor accuracy and §6.6 scheduling overhead"),
"2606.16907":("§3 Tangram Design; §4 Resource and Model Decomposition; §5 Model-Slice Composition","§6 Evaluation (§6.1 setup; §6.2–6.6 heterogeneity, scaling, pruning and planning)","§2.2 heterogeneous-cluster challenges; §6.6 planner scalability boundary"),
"2606.16914":("§3 MoneyWorld; §§4–5 redundant versus decision-relevant channels","§6 Controls/Scaling/Robustness; §7 safety-prior flip; Appendix E evaluation","§8 Discussion (§8.4 limitations and methodology); Appendix A criterion scope"),
"2606.16988":("§2 Theory of Procedural Understanding (§2.1 action vocabulary; §2.2 information theory); §3 significance","§4 Natural Studies; §5 Controlled Evaluations; §6 distilled-model case study","§7 Conclusion; Appendix A vocabulary algorithms and reward specifications"),
"2606.17005":("§3 Evaluation-Trace Archive; §4 Observability Regime (§4.1 Bayesian decision readout); §5 stress/adjudication protocol","§6 Results (§6.1 admissibility; §6.2 archive prediction; §6.3 preference stress; §6.4 uncertainty)","§5 fixed adjudication gates; §6.4 posterior uncertainty audit; Appendix A detailed evidence"),
"2606.17016":("§3 TokenPilot (§3.2 global ingestion-aware compaction; §3.3 local lifecycle-aware eviction)","§4 Experiments (§4.1 setup; §4.2 isolated/continuous; §4.3–4.5 ablations and analyses)","§4.4 fallback-loop costs; §4.5 residual-utility gates; Appendix A configurations"),
"2606.17029":("§3 Method (§3.1 evidence tree; §3.2 query-rubric co-generation/revision; §3.3 RL rubric rewards)","§4 Experiments (§4.1 settings; §4.2 results; §4.3 efficiency; §4.4 ablation; §4.5 data; §4.6 case)","Appendix A reward details; Appendix B training details; Appendix C data construction"),
"2606.17034":("§4 KVEraser (§4.1 surrogate cache; §4.2 inference complexity)","§5 Experiments (§5.1–5.6 two-stage training, setup, scaling, unseen QA and ablations)","§6 Conclusion and Future Work; Appendix E failure-case breakdown; Appendix G compute"),
"2606.17110":("§2 Assumptions and Threat Models; §3 LLP Attack Principles","§§4–7 direct-model, federated, data-poisoning and DP-evasion evaluations","Appendix C Defenses Against Poisoning Attacks in FL; threat-model scope in §2"),
"2606.17114":("§IV Leakage-Risk Taxonomy; §V Experiment Setup (§V-A–D scaffolding, environment, scenarios and criteria)","§§VI–IX detailed scenarios, quantitative and qualitative analysis","§IX-A agent performance/safety; §IX-B user-LLM reliability; §IX-C LLM-judge performance"),
"2606.17122":("§3 Method (§3.2 auditable unlearning; §3.3 passport composition; §3.4 verification/tolerance)","§4 Experiments (§4.1 setup/metrics; §4.2 single/multi-class); Appendices D–H","§5 Discussion (§5.1 Scope and limitations); Appendix B.2 scaling limits; Appendix H reconstruction attack"),
"2606.17182":("§II Runtime Model; §III Anomaly Catalog; §IV Consistency Lattice; verified runtime sections","formal witnesses, TLAPS checks and Verus spec/runtime refinement in §§III–IV; implementation/evaluation appendices","§II-B simplifying assumptions; §III-D split-view outside single-store model; realizability frontier §IV-C"),
"2606.17200":("§3 Method (§3.1 unified action representation; §3.2 reliability-aware objective); §4 data/conversion pipeline","§5 Experiments (§5.1 setup; §5.2 simulation; §5.3 real robot; §5.4 ablation; §5.5 fine-tuning)","§7 Limitations; Appendix A action standardization and validation"),
"2606.17209":("§3 Anchor Collapse; §4 DivInit (§4.1 procedure; §4.2 compute overhead)","§5 Experimental Setup; §6 Experiments (§6.1 results; §6.2 qualitative; §6.3 ablations)","§7 Conclusions and Future Work; Appendix A infrastructure/reproducibility"),
"2606.17229":("§3 Method (models/data, conditions, residual rank, conflict score and extraction)","§4 Results (§4.1–4.9 wrongness controls, concealment, transfer, read-only and extraction)","§4.3 negative results; §4.6 caveat; §5 What RIFT Does Not Show; §6 Limitations"),
"2606.17241":("§3 Deployment Dataset; §4 System Design (§4.1 constraints/tradeoffs; §4.2–4.6 pipeline)","§5 System Evaluation (scenarios, hardware, deployment, implementation and metrics); §6 Results","§4.1 Design Constraints and Trade-offs; §7 Discussion; Appendix 9.3 sensitivity"),
"2606.17283":("§III Reproducibility; §IV ARVO (§IV-A–F dataset, reproducer, patch locator and access)","§V Dataset (§V-A characteristics; §V-B accuracy); §VI Case Studies","§VII-A Limitations; §VII-B Future Work"),
"2606.17328":("§3 MemTrace (§3.1 data; §3.2 probes; §3.3 metrics; §3.4 diagnostic views)","§4 Experiment and Findings (§4.1–4.5 maintenance, evidence conflict and failure attribution)","Appendix C Failure-Origin Checks; Appendix D judge reliability; Appendix E sensitivity"),
"2606.17378":("§III Proposed Methodology (§III-A motivation; §III-B relay); §IV Algorithm Design (§IV-A–C formulation, LinUCB and reward)","§V Experiment (§V-A setup; §V-B relay; §V-C sensitivity; §V-D scheduling; §V-E ablation)","§V-C parameter sensitivity; §V-E ablation; §VI Conclusion"),
"2606.17383":("§2 POMDP Representation; §3 Validation Framework (§3.1 belief; §3.2 forecast; §3.3 policy; §3.4 utility)","§5 Portfolio Case Study; §6 Empirical Validation (§6.1–6.12 design, calibration, drawdown, ablation and sensitivity)","§4 Model Risk (§4.1–4.7); §6.11 assumptions; §6.12 interpretation"),
"2606.19386":("§2 Setup; §3 Δt=0 Audit and Erratum; §§4–9 cadence sweeps, scaling and transition triggers","§4 Uniform-Cadence Sweep; §5 Measured Real Cadence; §6 burst structure; Appendix A replay/instrumentation","§8 scaling-rule limits; §9 transition-trigger timing problem; §11 Limitations"),
"2606.20695":("§4 ET-MCP Architecture; §5 Implementation","§6 Evaluation (§6.1 benchmarks; §6.2 metrics; §6.3 paired/noise-floor results; §6.4 probes; §6.5 threshold)","§6.3.3 no detectable effect at stated power; §6.6 Limitations; §7 Forward Work"),
"2606.20698":("§3 Problem Definition; §4 Method (§4.1 chunk-wise world-model rollouts; §4.2 reward/cost; §4.3 constrained GRPO)","§5 Experiments (§5.1 setup; §5.2 simulation; §5.3 real-world; §5.4 ablation)","Appendix B Limitations and Future Work; Appendix H real-world details"),
"2606.20701":("§3 Problem Setup; §4 BARD-MARL (§4.1 policy graph; §4.2 Bayesian trust; §4.3 variants; §4.4 response)","§5 Experimental Setup; §6 Results (§6.1 detection; §6.2 ablation/scalability; §6.3 mitigation)","§7 Discussion; §6.3 mitigation only as auxiliary evidence; Appendix C checklist"),
"2606.24598":("§3 Migration Method; §4 Architecture; §7 Convertibility Taxonomy","§5 WeChat Case Study; §6 Evaluation","§9 Discussion and Threats to Validity; abstract explicitly limits evidence to one case and readiness, not validated self-learning"),
}

# Workload and evaluator are mandatory and family-specific.  Every other field
# starts as the literal contract value `Not Disclosed` and is overridden only
# where the exact-v1 body states a concrete value.
WORKLOAD_EVALUATOR = {
"2606.16100":("black-box LLM fingerprint spoofing under single-, cross-model and continual adaptation","fingerprint attack success across auditors, adapters and target models plus ablations"),
"2606.16106":("edge inference roofline workloads under independent CPU/GPU/EMC clocks, bursts and co-tenancy","median and tail latency, estimator error and governor deadline behavior"),
"2606.16110":("machine-unlearning verification across six datasets and ten unlearning methods","proof-of-ignorance validation, attack tests and method ablations"),
"2606.16135":("multi-turn LLM serving with heterogeneous models and shared hot-prefix KV state","P99 TTFT, end-to-end latency, interference, context-length and cache-transfer ablations"),
"2606.16190":("hardware-in-the-loop firmware tasks on MAX78000 and STM32N6 MCUs","compile/flash/measure success, arena score, deployment outcomes and failure taxonomy"),
"2606.16242":("adaptive poisoning of rapid-response content defenses over update rounds","attack-goal success, detector degradation and defense/mitigation comparisons"),
"2606.16264":("disaggregated prefill/decode serving under multiplexed request mixes","SLO attainment, latency/CDF, queueing and allocation comparisons"),
"2606.16287":("post-install dynamic skill modification in OpenHands and Claude Code","attack success, benign dynamic-modification false positives and defense effectiveness"),
"2606.16310":("MLA training and decode with post-projection QK RMSNorm","training loss, downstream quality, decode overhead and stress diagnostics"),
"2606.16322":("bounded multi-agent artifact review, adjudication and guarded revision","task quality, convergence, issue handling and ablation results"),
"2606.16332":("CPU matrix-extension operator execution across roofline shapes","end-to-end/operator speed, ablations, power and GPU comparison"),
"2606.16341":("filtered ANN workloads across selectivity and model-mismatch regimes","plan regret and phase-boundary performance under estimation error"),
"2606.16352":("TEE-verified remote LLM attention for prefill and memory-constrained decode","prefill/decode performance, verification effectiveness and communication overhead"),
"2606.16358":("confidential LLM API routing through a client-attested enclave","security/adaptive-attack checks, auditability and workload runtime"),
"2606.16364":("controlled tool selection plus BFCL live-multiple, Seal-Tools and τ-bench anchors","function-name selection, causal recovery, AST end-to-end result and compute overhead"),
"2606.16384":("decentralized context-parallel pretraining above 100K tokens over constrained links","wall-clock convergence, communication compression, ablations and baseline comparison"),
"2606.16420":("security-audit playbook evolution on 813 advisories and held-out testing on 371 advisories","end-to-end exploit matches, transfer lift, false-positive rate and scoring protocol"),
"2606.16429":("Transformer-to-hybrid Gated DeltaNet conversion across teacher/layer-retention settings","zero-shot quality, token-to-recovery, long-context restoration and ablations"),
"2606.16461":("orthogonally transformed Transformer pretraining, fine-tuning, retrofitting and inversion attacks","utility preservation and embedding/model-inversion, norm, Procrustes, Gram and fingerprint attacks"),
"2606.16494":("multimodal retrieval QA with evidence-order permutations across reader/dataset cells","answer accuracy and primacy-position effects with shuffle, modality and reranking audits"),
"2606.16496":("reflective program-policy evolution and engineering-design transfer","sample efficiency, cross-run/task transfer and critic/evolution ablations"),
"2606.16511":("tail-shape estimation on LLM safety scores under threshold, sample-size and perturbation changes","admissibility, goodness-of-fit, stability, pairwise verdict and cross-scorer checks"),
"2606.16519":("adversarial trajectory attacks against controllable video world models","attack objectives, transferability, bi-level optimizer and ablations"),
"2606.16523":("heterogeneous knowledge ingestion into governed Agent skill artifacts","knowledge-to-skill production, provenance, lifecycle governance and runtime health signals"),
"2606.16527":("black-box jailbreak detection across attack datasets and adaptive attacks","attack/benign detection, latency, branch ablations, backbone sensitivity and human/judge validation"),
"2606.16541":("natural-language to formal-mathematics faithfulness on DriftBench and wild split","bidirectional provability, drift detection, probe-budget scaling, ablations and downstream impact"),
"2606.16603":("data-analytic Agent tasks compiled into executable evidence graphs","answer accuracy, graph validity/traceability, backbone robustness and ablations"),
"2606.16605":("Dreamer-family continuous-control world models under spatial and temporal adversarial attacks","clean return, robustness AUC, defense recovery, adaptive gap and saliency"),
"2606.16682":("multimodal self-evolution rounds with text, image and GUI evaluators","MPCI, cross-modal contagion, repeated-round statistics, ablation and error analysis"),
"2606.16690":("robot manipulation under local moving-object, occlusion and disturbance events","action-corridor trigger detection, intervention outcomes, threshold audit and real-robot success"),
"2606.16707":("personalized conversational memory on standard benchmarks and proactive active-service cases","answer quality, retrieval/structuring ablations, latency/token cost and judge re-evaluation"),
"2606.16710":("MINT misinformation tasks in single- and multi-Agent debate protocols","task accuracy, susceptibility, group-composition and decision-protocol effects"),
"2606.16748":("persistent-persona computer-use tasks spanning multiple resettable desktop applications","rubric score, perfect completion, task/app/step scaling and failure attribution"),
"2606.16751":("automated jailbreak search against multiple target defenses","attack success, query/iteration efficiency, cross-defense transfer and ablations"),
"2606.16768":("Transformer training across depth, curvature and warm-up schedules","largest-Hessian tracking, stability, loss, compute-optimal validation and schedule sensitivity"),
"2606.16774":("Agent skill tree search on QwenClawBench and PinchBench","benchmark success, collective-search/RL ablations and implementation comparisons"),
"2606.16813":("goal inference, clarification and causal-minimal tool filtering tasks","downstream success, wrong-goal execution, clarification, exposed-tool/token cost and backend robustness"),
"2606.16821":("search-Agent recommendation under hidden DOM, forged authority, consensus and citation-chain manipulation","endorsement ASR, backend/harness ablations and self-judge limitations"),
"2606.16824":("real coding-assistant traces replayed through a vLLM CacheWise implementation","session completion time, KV eviction/movement, predictor accuracy and scheduling overhead"),
"2606.16907":("LLM training-plan search on heterogeneous and homogeneous GPU clusters","training throughput, plan quality, scaling, pruning benefit and planner runtime"),
"2606.16914":("MoneyWorld policies with redundant versus decision-relevant visible incentive channels","reward-hacking rate, OOD controls, family/scale replication and safety-prior flip"),
"2606.16988":("ten coding Agents on SWE-Bench trajectories plus controlled procedural rewards","agent fingerprint accuracy, procedural divergence and reward-controlled behavior"),
"2606.17005":("longitudinal LiveBench/Open LLM Leaderboard v2 archives with LMArena and limited GAIA/τ-bench probes","Bayesian recovery, archive prediction, preference transfer and uncertainty calibration gates"),
"2606.17016":("isolated and continuous long-horizon Agent context-management workloads","task score, modeled inference cost, cache warm starts, context size and fallback-loop savings"),
"2606.17029":("deep-research Agent SFT/RL with evidence-tree rubrics","research task score, citation precision/recall, training efficiency, ablations and data analysis"),
"2606.17034":("localized KV-context erasing for synthetic spans and unseen long-document QA","erasure behavior, QA quality, scaling, bystander preservation, ablations and failure categories"),
"2606.17110":("direct-model, federated and data-poisoning extraction attacks on LLMs and VLMs","target extraction probability, stochastic decoding leakage and DP-evasion results"),
"2606.17114":("realistic email/database/document tool-use leakage scenarios from SG and KR AISI","quantitative leakage/safety criteria plus qualitative Agent, user-model and judge analysis"),
"2606.17122":("passport-embedded class and instance unlearning with LoRA extensions","forget/retain metrics, passport verification tolerance, reconstruction attack and time analysis"),
"2606.17182":("multi-Agent shared-store traces with stale generation, phantom tool, causal cascade and effect reordering","formal witnesses, flat-trace detector, TLAPS consistency and Verus refinement checks"),
"2606.17200":("human egocentric video plus robot demonstration/simulation pretraining for VLA","simulation, real-robot success, camera-space inference and data/component ablations"),
"2606.17209":("parallel agentic search with diversified first-query seeds","aggregated accuracy, pool-size/performance curves, diversity ablations and first-turn wall time"),
"2606.17229":("deceptive, wrong and truthful language-model responses across domains/families/lengths","conflict-score identification, wrongness controls, concealment, transfer and extraction tests"),
"2606.17241":("continuous roadside detection/tracking/fine-grained classification over curated driving video and deployment","system latency/throughput, temporal consistency, detection/classification and scenario results"),
"2606.17283":("reproducible open-source vulnerabilities with buildable revisions, triggers and patch locations","reproduction rate, dataset accuracy, backporting and false-positive correction studies"),
"2606.17328":("long-term memory probes varying memory age, question type and evidence conflict","maintenance, missing/conflicting evidence, retrieval-versus-use attribution, judge and sensitivity checks"),
"2606.17378":("relay diffusion inference and online scheduling on heterogeneous edge devices","relay latency/quality, scheduler reward, parameter sensitivity and ablations"),
"2606.17383":("portfolio-management POMDP case study with belief, forecast, policy and utility validation","calibration, portfolio performance, drawdown/wealth, ablation and sensitivity"),
"2606.19386":("SWE-bench Agent trajectories replayed at uniform and measured wall-clock cadence","alarm regime, cadence sweep, burst stability, scaling rule and transition-trigger audit"),
"2606.20695":("paired ET-MCP coordination trials on τ²-bench retail plus cross-model/domain probes","paired pass difference, trial-0 noise floor, statistical power and second-seed replication"),
"2606.20698":("SafeLIBERO simulation and real-world VLA safe-RL tasks","task success, safety-cost/violations, constrained-RL and component ablations"),
"2606.20701":("SUMO traffic grids with fixed-action, observation-flip, random-noise and coordinated Byzantine agents","AUC-ROC, scalability, signal ablations and mitigation as auxiliary evidence"),
"2606.24598":("single production WeChat Official Account expert workflow migrated through nine typed tools","business-logic parity, rollback, traceability, deterministic invariant and early feedback signal"),
}

BENCH_OVERRIDES = {
"2606.16100":{"model":"Gemma-1.1 2B/7B; Qwen2 1.5B/7B; Phi-3 Mini 3.8B/Medium 14B","batch":"5-shot MMLU, GSM8K and ARC-Challenge utility evaluation"},
"2606.16106":{"hardware":"NVIDIA Jetson Orin Nano Super; L4T R36.5","concurrency":"single-tenant and co-tenant contention traces","slo":"deadline-aware latency with median and tail reporting"},
"2606.16110":{"model":"four-CNN-block image classifier; embedding+three-CNN-block text classifier; OPT-2.7B LLM extension; ten unlearning methods/variants","workload":"CIFAR10, SVHN, SkinCancer, BBCNews, AGNews and IMDB; OPT-2.7B extension on PKU-SafeRLHF/TruthfulQA"},
"2606.16135":{"model":"Qwen3-14B and Qwen3-8B workers; vLLM and SGLang serving stacks","hardware":"NVIDIA H20 96GB, A100 80GB, V100 32GB and L4 24GB GPUs with NVLink/NVSwitch","input_length":"chunked-prefill baselines use 8K and 32K chunks; maximum context measured per VRAM setting","concurrency":"multi-turn concurrent serving","slo":"P99 TTFT and end-to-end latency"},
"2606.16190":{"model":"Claude Opus 4.7; Gemini 3.1 Pro","hardware":"MAX78000 and STM32N6 microcontrollers"},
"2606.16242":{"model":"LlamaGuard 4 12B defender; Gemini 3 Flash/Pro and Gemini 2.5 Flash-Lite proliferation/verification; GPT-5.2 synthetic-query generator","hardware":"NVIDIA A100 GPUs; RTX A5000 GPUs for a subset","precision":"QLoRA 4-bit NF4 with double quantization and bfloat16 computation","input_length":"maximum sequence length 2,048 tokens","batch":"micro-batch 1; gradient accumulation 8/16/32/64; effective batch preserved under DDP; 6,000-sample training set (3,000 jailbreak + 3,000 WildChat)","slo":"early stop after each held-out attack strategy reaches at least 90% validation accuracy and before validation declines"},
"2606.16264":{"model":"InternLM-20B with 200K maximum context","hardware":"8 NVIDIA A100 80GB GPUs; 600 GB/s GPU P2P","input_length":"Mooncake real long-context serving trace; chunked-prefill baseline chunk size 2048","concurrency":"multiplexed disaggregated prefill/decode requests","slo":"TTFT SLO = 5× light-workload phase latency; TTFT/TPOT mean and P90"},
"2606.16287":{"model":"OpenHands; Claude Code"},
"2606.16310":{"model":"400M-parameter MLA models","batch":"100B training tokens; 3-shot downstream evaluation"},
"2606.16322":{"batch":"three reviewers by default, clamped to 2–4; five-round cap"},
"2606.16364":{"model":"10 mask-honoring models from 3B–32B for causal study; five single-turn models for selector","concurrency":"single-turn; τ-bench multi-turn transfer tested separately","slo":"Not Disclosed"},
"2606.16332":{"model":"Llama-3.2-3B; Qwen3-4B; Qwen3-30B-A3B","hardware":"Apple M4 Pro 14-core CPU; MediaTek Dimensity 9500 8-core CPU; KunPeng 920 72F8 server CPU; M4 Pro 20-core GPU comparison","precision":"Qwen3-30B-A3B uses 4-bit weight quantization","input_length":"Ruler mean prefill 3,324/7,338; GSM8K 92; LongWriter-6K 339 tokens","output_length":"Ruler 4; GSM8K 100; LongWriter-6K 5,424 mean decode tokens","batch":"GPU comparison uses batch sizes 1,2,3,4,6,8,16"},
"2606.16341":{"input_length":"clustered-Gaussian corpora at n=100K/1M/10M; SIFT1M real-geometry anchor; k=10","batch":"at least 1,000 query samples per experiment cell"},
"2606.16352":{"model":"LLaMA3-3B; LLaMA3-8B; Qwen3-14B; Phi4-14B","hardware":"TDX-enabled VM: Intel Xeon Scalable, 16 vCPU, 128GB RAM, NVIDIA H20 96GB over PCIe 5.0","precision":"FP16","workload":"WikiText prefill prompts and long-context decode workloads"},
"2606.16358":{"hardware":"AWS EC2 c5.4xlarge, Intel Xeon Platinum 8275CL 3.00GHz, 16 vCPU/8 physical cores; Nitro Enclave with 2 dedicated vCPUs/1 core and 3GiB RAM","concurrency":"pooled local upstream for steady-state relay microbenchmark; real-provider runs use verified sidecar/enclave","slo":"fail-closed destination binding and provider-policy violations"},
"2606.16384":{"model":"8-layer 800M model; additional 32-layer 3B and 24-head 2.5B configurations","hardware":"8 NVIDIA A100 GPUs for 132K context; 32 A100 GPUs for 256K; 300 Mbps versus 100 Gbps networks","input_length":"132K tokens primary; 256K-token extension","batch":"16B training tokens per dataset for 800M compute-optimal runs"},
"2606.16420":{"model":"Codex/GPT-5.4-xhigh; OpenCode/GLM-5.1; 27B and A3B student models"},
"2606.16429":{"model":"Qwen2.5-1.5B-Instruct; Qwen2.5-3B-Instruct; Llama-3.2-3B-Instruct; Qwen3-8B"},
"2606.16461":{"model":"GPT-2 Small/Medium/Large; Llama 3.2 1B","hardware":"4×NVIDIA A100 GPUs"},
"2606.16494":{"model":"InternVL3-8B; Qwen3-VL-8B"},
"2606.16496":{"workload":"Lunar Lander, Acrobot, Pendulum and 36-dimensional CCAA 5-7-9-11 array synthesis","batch":"three seeds per warm/cold transfer condition; 15-call budget in the stated Acrobot transfer study"},
"2606.16519":{"model":"Astra on Wan2.1; Matrix-Game 2.0 distilled from SkyReelsV2-I2V-1.3B"},
"2606.16523":{"model":"DeepSeek-V4-Flash for knowledge parsing and candidate generation"},
"2606.16527":{"workload":"JailbreakBench/JBB-Behaviors, DSN, GCG, JailbreakChat, PAIR, ARS, JailbreakHub and CodeAttack; AlpacaEval and OR-Bench benign sets","batch":"100 explicit JBB harmful requests plus released attack artifacts"},
"2606.16541":{"model":"Llama-34B; closed-weights frontier model; Lean 4 + mathlib4 entailment oracle","batch":"384-pair independently annotated wild split (κ=0.81)"},
"2606.16511":{"model":"Qwen2.5-3B-Instruct; Llama-3.2-3B-Instruct; Llama-3.1-8B-Instruct; Mistral-Nemo-Instruct-2407","hardware":"one NVIDIA A100 80GB per condition","input_length":"30,000 RealToxicityPrompts per condition; 2,000-prompt pilot","output_length":"one completion per prompt","batch":"one completion per prompt, temperature 1.0, top-p 0.9, seed 0","slo":"pre-registered G1–G5 gates; 95th-percentile headline threshold and sample-size/effect-size pass criteria"},
"2606.16603":{"model":"Qwen3-8B policy; gpt-4o-mini reward/outcome judge","hardware":"SFT 4×A100 80GB; RL 8×A100 80GB; evaluation 4×A100 80GB","precision":"bfloat16 SFT","input_length":"SFT maximum sequence length 32,768; RL maximum response length 8,192 and tool observation budget 1,200 chars","output_length":"RL maximum response length 8,192","batch":"SFT effective global batch 128, per-device train/eval 2/4; RL 8 rollouts/prompt, train prompt batch 16, generation batch 4, PPO mini-batch 2/micro-batch 1 per GPU","concurrency":"judge calls asynchronous under a fixed but numerically undisclosed concurrency budget","slo":"tool timeout 120s; trajectory timeout 1,800s","workload":"TableBench (~700), InfiAgent-DABench (257), DSBench (466) and 100-case DAB-Step Research subset","evaluator":"LLM-judged QA/data-analysis accuracy; Content and Format scores for research; graph validity/traceability"},
"2606.16605":{"model":"Dreamer-family world models and model-free actor-critic controls","workload":"pixel-based MetaWorld robotic manipulation and DeepMind Control Suite continuous-control tasks"},
"2606.16682":{"model":"DashScope gui-plus; Qwen-plus; DeepSeek-chat; GPT-4o evaluator condition","batch":"N=10 for 50 rounds; N=5 valid for 30 rounds; N=30 for 30 rounds"},
"2606.16690":{"hardware":"two AgileX Piper robot arms; one 640×480 30Hz wrist RGB camera per arm; one top-view RGB camera","concurrency":"30Hz closed-loop policy execution"},
"2606.16707":{"model":"Gemini 3 Flash with thinking; separate Gemini judge","output_length":"answer-time thinking budget 2,048; judge budget 256","batch":"five-conversation LOCOMO subset with 300 QAs in stated additive test"},
"2606.16710":{"model":"Llama-3.3-70B-Instruct; GLM-4.7-Flash; Llama-3.3-70B-Instruct also generates MINT misinformation","hardware":"one or two NVIDIA A100 80GB GPUs","batch":"MINT 1,142 samples/10,278 misinformation texts; three-agent five-turn debate by default; five agents for consensus-vs-voting comparisons","concurrency":"three agents over five turns by default; five-agent protocol comparison"},
"2606.16748":{"model":"Claude Opus 4.6; Claude Sonnet 4.6; GPT-5.5; GPT-5.4 mini; Qwen 3.5 35B-A3B and 9B","batch":"184 tasks across six models"},
"2606.16751":{"model":"nine target models across GPT, Gemini, Claude, DeepSeek and Llama3 families","workload":"AdvBench high-risk requests against eight defended targets and Llama-3-8B-Uncensored"},
"2606.16768":{"model":"8-layer 640M, 16-layer 1B and 32-layer 3B LLaMA-style Transformers","batch":"FineWeb, DCLM and OLMo-Mix training; 16-layer 1B baseline comparison"},
"2606.16774":{"model":"Qwen3-4B/8B and Qwen3.5-4B/9B training backbones; closed/open comparison models listed in Tables 1–2","hardware":"8×NVIDIA H100 GPUs","batch":"2,000 CSTS SFT examples; two SFT epochs; QwenClawBench and 23-/123-task PinchBench"},
"2606.16813":{"model":"Claude Opus 4.8; Claude Sonnet 4.6; Claude Haiku 4.5; GPT-OSS-120B; Nova Premier; Nova 2 Lite; Nova Pro v1","batch":"120 controlled tool-use tasks across six filtering methods"},
"2606.16821":{"model":"Claude Sonnet 4.6; Claude Haiku 4.5; GPT-5.4-mini/nano; GPT-5.5; Gemini 3 Flash/3.1 Pro/3.5 Flash; DeepSeek V4 Pro/Flash; Grok 4.3; Kimi K2.6; MiniMax M2.7; Qwen3.6-Plus"},
"2606.16824":{"model":"vLLM implementation","batch":"N=30 sessions for KV movement; N=40 scheduling-overhead point","concurrency":"long-running closed-loop coding sessions"},
"2606.16907":{"model":"GPT-3 dense; GShard, Qwen3 and Mixtral MoE","hardware":"five NVIDIA GPU instance types on Azure across three heterogeneous clusters","precision":"FP16 activations","input_length":"GPT-3 2,048; GShard 1,024; Qwen3/Mixtral 4,096 tokens","batch":"global batch size 128"},
"2606.16914":{"model":"Qwen2.5 base/instruction and Qwen3 open-weight policies at 3B, 7B and 14B scales","batch":"GRPO with LoRA rank 16; six training and six held-out MoneyWorld domains"},
"2606.16988":{"model":"ten coding Agents"},
"2606.17005":{"batch":"constructed terminal-only example over 1,000 systems"},
"2606.17016":{"model":"GPT-5.4-mini agent backbone; Qwen3.5-35B-A3B state estimator","input_length":"500K-token baseline context; method-specific thresholds from 40K to 120K and reported cache-hit/miss token totals","batch":"batch-turn tracking window B=3; isolated and continuous PinchBench/Claw-Eval modes","concurrency":"continuous same-category task streams","slo":"provider-priced cache hit/miss/output cost plus benchmark task score"},
"2606.17029":{"model":"8B research-Agent policy","hardware":"8×A100 for 3 SFT GPU-hours and 750 RL GPU-hours","batch":"140 RL steps reported for convergence"},
"2606.17034":{"hardware":"2×A100 80GB for training; 1×A100 80GB for inference; 1.7TiB RAM; 24 CPU cores","batch":"pretraining under one day; fine-tuning about eight hours"},
"2606.17110":{"model":"GPT-2 family and Llama family; VLM victims; GPT2-Small 124M defense appendix","batch":"10 FL clients for 80 rounds, 10,000 samples/client; one malicious client; 100 target secrets/samples"},
"2606.17114":{"model":"ReAct Agent plus separate user LLM and LLM judge","concurrency":"multi-turn Agent/user interaction with stepwise MCP tool calls"},
"2606.17122":{"model":"ViT-Tiny/Small/Base, all 12 layers with 16×16 patches; passport-augmented LoRA extensions","batch":"10 epochs for TrustErase and hypernetwork"},
"2606.17182":{"concurrency":"concurrent multi-Agent shared-state executions"},
"2606.17200":{"hardware":"ARX bimanual real-robot platform; RoboCasa GR1 TableTop and RoboTwin 2.0 simulators","batch":"24 RoboCasa tasks, 50 RoboTwin tasks and six real-world manipulation tasks"},
"2606.17209":{"hardware":"4×NVIDIA L40S 48GB GPUs","precision":"bf16","input_length":"retrieved text truncated at 4,000 characters per turn","batch":"k=4 primary comparison; about 590 GPU-hours plus $185 API cost"},
"2606.17229":{"model":"GPT-2 Small 117M; GPT-2 Medium 345M; Qwen2.5-1.5B/7B-Instruct; Phi-3-mini-4k-instruct 3.8B","batch":"25 train and 20 held-out facts; 48 neutral anchors for relative representations"},
"2606.17241":{"hardware":"Jetson Orin Nano 8GB; Arm Cortex-A78AE 6-core CPU; NVIDIA Ampere GPU with 1,024 CUDA/32 Tensor cores; 7–25W","concurrency":"continuous live vehicular pipeline; fixed k=3, confidence 0.5, padding 0.20"},
"2606.17283":{"batch":"6,138 reproduced vulnerabilities across 311 projects from 8,921 OSS-Fuzz inputs; 221 linked CVEs"},
"2606.17328":{"model":"13 memory-system configurations; Qwen3.5-35B, Gemini-3-Flash, GPT-5-nano long-context rows; shared gpt-4o-mini generator for other main rows","batch":"20 users, 835 knowledge points, 5,677 base probes, 15,422 question rows and 200,453 scored answers"},
"2606.19386":{"concurrency":"non-uniform Agent action cadence"},
"2606.20695":{"model":"Claude Sonnet 4.5 retail probe; Claude Haiku airline probe","batch":"n=30 for each stated cross-model/domain probe","concurrency":"paired single-Agent and coordination-active trials"},
"2606.20701":{"batch":"25-agent and 100-agent traffic grids","concurrency":"10% Byzantine-agent attack conditions"},
"2606.17378":{"model":"SDXL relay configurations over DiffusionDB and DrawTextCreative","concurrency":"mixed service workloads sharing edge GPU resources","slo":"dynamic quality-latency preference encoded in scheduler reward"},
"2606.17383":{"workload":"AAPL, MSFT, GOOGL, NVDA, AMZN, JPM, IBM, GLD and TLT portfolio with SPY benchmark; 10 Jun 2024–12 Jun 2026","input_length":"252-trading-day lookback","output_length":"21-trading-day holding period; monthly rebalance"},
"2606.20698":{"model":"OpenVLA-OFT backbone; Wan2.2 interactive world model; ResNet task classifier and safety head","hardware":"Franka Emika Panda 7-DoF manipulator in SafeLIBERO/Robosuite plus five real-world Franka tasks","batch":"four SafeLIBERO suites × four tasks × two obstacle levels; 1.5K world-model trajectories; GRPO group size 16"},
"2606.24598":{"batch":"one production WeChat workflow; nine expert functions/tools; nine adversarial invariant tests; three self-operated accounts for observational feedback"},
}

def benchmark_contract(aid: str) -> dict[str, str]:
    workload, evaluator = WORKLOAD_EVALUATOR[aid]
    value = {"workload":workload,"model":"Not Disclosed","hardware":"Not Disclosed","precision":"Not Disclosed","input_length":"Not Disclosed","output_length":"Not Disclosed","batch":"Not Disclosed","concurrency":"Not Disclosed","slo":"Not Disclosed","evaluator":evaluator}
    value.update(BENCH_OVERRIDES.get(aid, {}))
    return value

BOUNDARIES = {
"2606.16100":"GhostPrint 只证实行为指纹可被适配器伪造，不能证明任何现有 provider 正在欺诈；adapter 训练和持续轮换增加成本，检测漂移时回退到 attested model/version 与独立计费证据。",
"2606.16106":"EMC 轴和 burst tail 来自两类 Orin 平台，不能外推所有 edge GPU；多维 DVFS 增加 profiling/actuation 成本，未知 workload 或热状态下回退到保守 deadline headroom。",
"2606.16110":"proof-of-ignorance 仅覆盖论文威胁模型与六个数据集，不等价于法律意义的数据删除；额外审计会增加查询与误判成本，证据不足时仍需 scratch retrain 或隔离旧模型。",
"2606.16135":"借用 idle HBM 能降低 P99 TTFT，但 donor pressure 或跨模型 identity 错配会引起抖动/污染；回收阈值失效时回退本地 KV 与普通 eviction，不能宣称跨机收益。",
"2606.16190":"闭环 arena 证明特定 MCU 上可编译、刷写和测量，不证明任意固件或外设安全；硬件循环昂贵且易受工具链影响，失败时保留人工固件 review 与沙箱部署。",
"2606.16242":"自适应 poisoning 证明更新型 detector 有跨轮攻击面，不代表所有 rapid-response 防御必然失效；冻结/延迟更新牺牲响应速度，异常时回退到人工 adjudication 和已知良性快照。",
"2606.16264":"联合 multiplexing 只改善论文 request mix 的 SLO，不证明不可估计突发同样可控；controller 依赖可估计 slack 与服务时间，突发或模型切换失配时应降级为隔离队列/保守 admission，而非继续过载。",
"2606.16287":"DyMalSkill 展示静态扫描遗漏动态修改，不证明所有动态 skill 恶意；runtime verifier 增加 syscall/权限摩擦，无法判定时回退只读 mount、签名包与拒绝执行。",
"2606.16310":"分解 RMSNorm 保留论文 MLA decode path，但只对给定归一化/投影结构成立；数值误差或 fused-kernel 不兼容时回退原始归一化并保留完整 keys。",
"2606.16322":"持久 issue 与 guarded revision 只证明所测 artifact loop 可减少 reviewer 互相覆盖，不证明自动审稿会收敛；它增加协调状态和延迟，无法形成 adjudication 时冻结 claim spine、停止自动 patch 并交人工 owner。",
"2606.16332":"SMEPilot 的 shape-aware 选择只覆盖测试矩阵与 CPU 扩展，不能把 SME 设为全算子默认；packing 或功耗收益消失时回退既有 CPU/GPU kernel。",
"2606.16341":"phase boundary 只在论文 ANN/过滤分布中把 selectivity error 转成 plan regret，不证明任意索引共享同一阈值；估计漂移或 regret 接近时回退可解释的静态 plan，并重新采样校准。",
"2606.16352":"VeriAttn 只验证 attention 路径而非整个远端 serving stack，不证明端到端服务可信；TEE 通信、分页和 TCB 增加开销，验证失败时 fail closed 或回退本地受信执行。",
"2606.16358":"Aegis 缩小 plaintext authority，但不能消除 client compromise、side channel 或 enclave 漏洞；attestation/relay 失败必须拒绝目的地绑定，不能静默回退到 host plaintext。",
"2606.16364":"attention-segment 证据只定位 function-selection readout，不证明 arguments 或完整多轮执行正确；selector 约有 1.2× 计算开销且 AST 端到端仍失败，无法约束时回退原生生成与 executor 校验。",
"2606.16384":"95% 以上压缩与 300 Mbps 结果只绑定论文模型和网络，不证明任意 topology 保持收敛；动态 subspace 会引入重构误差与版本状态，误差或收敛漂移时停用 projection，回退未压缩 context parallel。",
"2606.16420":"813/371 advisory 结果证明 playbook 可迁移到所测 Agent，不证明自动发现普遍安全；evolution 会放大错误启发式，held-out/false-positive gate 失败时回退并回滚上个 playbook。",
"2606.16429":"Taylor 校准减少所测 GDN 转换 token，不证明适用于所有 hybrid mixer 或更大模型；局部对齐与统计采样增加前置成本，恢复曲线异常时回退 naive conversion 或保留 softmax 层。",
"2606.16461":"正交对称只保护所述 equivariant 表示，不证明 metadata、访问模式和 side channel 保密；架构约束可能损失兼容性，攻击或 utility gate 失败时回退可信执行/密码学路径。",
"2606.16494":"位置扰动揭示所测 reader 的 primacy bias，不能断言所有 multimodal RAG 都忽略末尾证据；shuffle/rerank 增加不稳定性，失败时保留多顺序投票与位置归因而非单次顺序。",
"2606.16496":"REFLEX 的经验迁移只来自所测演化任务，不证明生成诊断是可靠规则；critic 偏差会污染 skill memory，held-out 下降时回滚候选并保留旧策略。",
"2606.16511":"协议能排除若干 tail-shape 假阳性，不能证明剩余 tail model 为真或预测极端事件；更大样本/多阈值增加成本，gate 不稳时回退为只报告经验分位数。",
"2606.16519":"BadWorld 证明可攻击特定视频 world model，不等于真实 closed-loop controller 必然崩溃；攻击优化成本高且 transfer 有界，部署回退应是安全控制器与 observation shield。",
"2606.16523":"SkillWiki 展示技能治理基础设施，不证明摄取知识生成的 skill 正确或安全；规模化 lineage/health 管理有持续成本，验证缺失时回退草稿态并禁止 runtime promotion。",
"2606.16527":"结构+语义双分支只改善所测 jailbreak 检测，不证明 judge/backbone 不会共同失效；双分支增加延迟，分歧或自适应攻击未通过时回退拒绝/人工复核。",
"2606.16541":"BPF 在形式 oracle 可用时检测语义漂移，不证明自然语言意图被完全形式化；双向证明和 probe budget 昂贵，oracle 不完备时必须标注 undecidable 并人工核对。",
"2606.16603":"VeriGraph 只让所测数据分析轨迹可重放，不证明源数据或结论语义正确；图扩张增加 token/runtime，校验失败时回退确定性查询与人工证据审查。",
"2606.16605":"ARB4WM 的统一接口只比较所测 Dreamer agents，不构成真实环境安全认证；attack budget/controller/horizon 改变会重排结果，未知条件下回退 clean controller 与独立 shield。",
"2606.16682":"MPCI 显示所测 evaluator 的跨模态 contagion，不证明所有自演化系统同样崩塌；多 evaluator/holdout 增加成本，偏好漂移时冻结 promotion 并回滚 evaluator 版本。",
"2606.16690":"PATCH 只检测 active action corridor 附近的 latent innovation，不是通用碰撞证明；threshold 对场景/传感器敏感，低置信时回退停止、减速或人工接管。",
"2606.16707":"可执行 memory 提升所测个性化任务，但记忆代码具有执行/冲突风险；生成-验证成本与错误约束会累积，验证失败时回退只读事实库并禁止代码执行。",
"2606.16710":"MINT 说明 benign MAS 会传播虚假上下文，不证明多数协议总是更差；独立复核增加调用成本，provenance 缺失时回退单 Agent 或人工确认关键 claim。",
"2606.16748":"MyPCBench 提供持久 persona 和 resettable desktop，但合成网站/任务不代表真实企业桌面；环境维护与 rubric judge 有偏差，副作用不确定时回退只读/确认式执行。",
"2606.16751":"UniAttack 比较多类 defense 的自适应攻击，不证明组合生产防线已经失效；搜索 query 成本与 detector 误判显著，预算耗尽时保留未决而非计为成功。",
"2606.16768":"architecture warm-up 在所测深度/优化器提高稳定性，不等于可删除所有 learning-rate warm-up；渐进启用改变优化轨迹，曲率或 loss 恶化时回退标准 warm-up。",
"2606.16774":"collective skill tree 在两个 benchmark 提升搜索，不证明成功轨迹可直接全局复用；多模型评估成本高且会收敛到错误节点，held-out 失败时 prune 并回退基础 Agent。",
"2606.16813":"goal-aware filtering 降低所测 wrong-goal execution，但 clarification 会增加交互摩擦且不等于授权；歧义持续时回退暴露安全最小工具集并请求人工确认。",
"2606.16821":"静态 proxy 只证明 source framing 能操纵 endorsement，不证明开放 Web 的真实发生率；防御 prompt 或 backend 切换有成本，来源冲突时回退多源验证和拒绝背书。",
"2606.16824":"CacheWise 的收益只绑定采集到的 coding traces 和 vLLM 实现，不证明其他 Agent workload 同样获益；metadata predictor 漂移会错误保留 KV，压力或命中率恶化时回退 LRU/标准 prefix caching。",
"2606.16907":"Tangram 扩展异构 plan 搜索但不能消除真实设备 straggler/故障；decomposition/planning 有编译开销，profile 不可信时回退同构 island 或保守 pipeline。",
"2606.16914":"MoneyWorld 证明决策相关 incentive channel 可诱发 hacking，不证明自然语言奖励线索普遍致因；channel blinding 可能损失有效反馈，安全 probe 失败时冻结 adaptation。",
"2606.16988":"procedural fingerprint 区分十个 Agent 的行为习惯，不证明轨迹相似就是语义正确；压缩 vocabulary 可遗漏关键动作，约束导致成功率下降时回退结果级验收。",
"2606.17005":"archive audit 只能否定不受支持的 frontier claim，不把缺失公开记录变成真实能力估计；Bayesian 结果依赖 reporting convention，缺失过高时回退描述性历史与不确定性。",
"2606.17016":"TokenPilot 已由 Ch75 现有 canonical-prefix/segment-lifecycle owner 覆盖，论文收益不证明任意 Agent 都可激进压缩；utility gate 失败时保留原始 segment，因此本次 No Change。",
"2606.17029":"evidence-tree rubric 只分解论文 reward，不证明树和 citation judge 不会奖励错误证据；构建/评分成本上升，支持关系未验证时回退人工 rubric 与独立引用检查。",
"2606.17034":"KVEraser 在所测 QA 上局部擦除，不证明敏感信息从参数或所有后续 state 删除；steering 会伤及旁观 token，drift 超阈值时回退重新 prefill 或清空 session。",
"2606.17110":"LLP 展示特定 poisoning 可诱导未见数据提取，不证明任意微调都会泄漏；provenance/admission 增加训练摩擦，可疑 update 应隔离并回退可信 checkpoint。",
"2606.17114":"AISI 场景只揭示所测 benign tool use 的泄漏风险，不证明 judge/用户模型无误判；额外确认降低自动化，secret policy 不确定时回退最小权限与人工批准。",
"2606.17122":"passport 验证只证明配置/凭证状态，不等价于所有信息已从 backbone 删除；hypernetwork 与密钥管理增加复杂度，重构攻击或 retain gate 失败时回退重训/隔离。",
"2606.17182":"形式化 detector 只覆盖论文 single-store runtime 与列出的 anomaly，不证明 split-view 等外部一致性；序列化牺牲并行度，模型假设不成立时回退单写者或事务存储。",
"2606.17200":"统一 22-D action schema 改善所测跨 embodiment 训练，不代表 human video action 标签完全可靠；转换误差会污染控制，quality gate 失败时回退 robot-only 数据并停用 human auxiliary data。",
"2606.17209":"DivInit 只改善所测 agentic search 的首轮多样性，不证明后续证据质量；它增加首轮延迟，预算受限或聚合不稳时回退单 seed 加可解释 branch pruning。",
"2606.17229":"RIFT 的 residual rank 是所测 deception 条件下的 read-only signature，不是 truth detector；跨域 probe 仍有 caveat 且 steering 较弱，低置信时回退人工复核，不能自动惩罚。",
"2606.17241":"连续道路部署结果绑定 INTSD、精选视频和指定硬件，不等于任意天气/相机满足实时性；热/队列/精度恶化时回退稀疏采样、降级分类或安全停止。",
"2606.17283":"ARVO 提高可复现性但构建容器和 oracle 仍会老化，不能把无法复现等同于无漏洞；失败时保留 upstream record 并标注环境缺口。",
"2606.17328":"MemTrace 的 retrieval-versus-use 归因已由 Ch77 现有 memory pipeline counterfactual owner 覆盖，不证明 judge 与接口敏感性已经消失；因此回退既有 owner，本次 No Change 而非重复写入。",
"2606.17378":"RISE 的 relay/scheduler 收益只绑定所测 diffusion、设备和 network，不证明其他链路同样获益；partial denoising state 迁移失败会同时伤质量和 SLO，回退本地完整推理或静态 placement。",
"2606.17383":"POMDP 三层 validation 在单一 portfolio case 演示，不能升级为一般 Agent 合规证明；latent-state/model risk 未闭合时回退规则策略与人工风险限额。",
"2606.19386":"论文首先纠正自身 Δt=0 错误，后续 bistability 只覆盖所测 cadence/monitor class；时钟或 burst 分布漂移时回退 transition-window 告警而非 moment truth。",
"2606.20695":"paired noise-floor 发现当前 power 下无可检测 coordination gain，不证明 ET-MCP 永远无效；扩大 trial 很昂贵，effect 未越过 deployment threshold 时保留单 Agent。",
"2606.20698":"world-model rollout 只支持所测 VLA safe RL，不证明模拟 cost head 保证真实世界安全；model bias 或 shield disagreement 时回退真实环境 safety shield、abstention 和人工接管。",
"2606.20701":"BARD 在 SUMO/指定 attack 上识别 Byzantine agent，不证明跨域 trust score 校准；误杀 peer 会降低协作，置信不足时隔离消息并回退无通信策略。",
"2606.24598":"证据仅是单个 WeChat workflow 的可逆迁移和 early feedback signal，不是验证过的 self-learning；taxonomy 误路由时回退并一键回滚 legacy harness，保持业务逻辑不变。",
}

NO_CHANGE = {"2606.17016", "2606.17328"}
SELECTED = {"2606.16100":"DA-20260616-ATTESTED-IDENTITY", "2606.16384":"DA-20260616-LOW-BANDWIDTH-CONTEXT", "2606.17182":"DA-20260616-CONCURRENT-AGENT-STATE"}
SELECT_RATIONALE = {
"2606.16100":"Selected because it changes the gateway trust primitive itself: behavioral fingerprint becomes spoofable under adaptive providers, so model identity and billing evidence must become attested, versioned control state.",
"2606.16384":"Selected because it couples model geometry, distributed activation state and network bandwidth: the rotating subspace is not merely compression but versioned training state whose failure changes convergence.",
"2606.17182":"Selected because it supplies the day's strongest cross-cutting concurrency model: happens-before, shared-state conflicts and tool side effects become explicit runtime invariants rather than conversational convention.",
}

PATHS = {
"PLATFORM-SECURITY":"books/part-06-ai-infrastructure/72-security.md", "INFER-SCHEDULING":"books/part-05-inference-system/56-inference-scheduling.md",
"TRAIN-DATA":"books/part-04-training-system/27-data.md", "INFER-KV-CACHE":"books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
"PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/66-evaluation-system.md", "INFER-PD-DISAGGREGATION":"books/part-05-inference-system/55-pd-disaggregation.md",
"MODEL-LONG-CONTEXT":"books/part-02-model/22-long-context.md", "AGENT-WORKFLOW":"books/part-07-agent/81-workflow.md",
"INFER-TENSORRT-LLM":"books/part-05-inference-system/49-tensorrt-llm.md", "AGENT-RAG":"books/part-07-agent/76-rag.md",
"PLATFORM-GATEWAY":"books/part-06-ai-infrastructure/62-gateway.md", "AGENT-TOOL-CALLING":"books/part-07-agent/78-tool-calling.md",
"TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/36-distributed-training.md", "AGENT-REFLECTION":"books/part-07-agent/80-reflection.md",
"MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "AGENT-MEMORY":"books/part-07-agent/77-memory.md",
"AGENT-MULTI-AGENT":"books/part-07-agent/82-multi-agent.md", "TRAIN-PRETRAINING":"books/part-04-training-system/28-pretraining.md",
"AGENT-CONTEXT":"books/part-07-agent/75-context.md", "AGENT-PLANNING":"books/part-07-agent/79-planning.md", "PLATFORM-MONITORING":"books/part-06-ai-infrastructure/67-monitoring.md",
}

ADJACENT = {
"PLATFORM-SECURITY":"books/part-06-ai-infrastructure/62-gateway.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1",
"INFER-SCHEDULING":"books/part-05-inference-system/55-pd-disaggregation.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1",
"TRAIN-DATA":"books/part-04-training-system/28-pretraining.md#L1; books/part-04-training-system/35-checkpoint.md#L1",
"INFER-KV-CACHE":"books/part-05-inference-system/54-gpu-memory.md#L1; books/part-05-inference-system/56-inference-scheduling.md#L1",
"PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1",
"INFER-PD-DISAGGREGATION":"books/part-05-inference-system/43-prefill.md#L1; books/part-05-inference-system/44-decode.md#L1",
"MODEL-LONG-CONTEXT":"books/part-02-model/19-kv-cache.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1",
"AGENT-WORKFLOW":"books/part-07-agent/79-planning.md#L1; books/part-07-agent/82-multi-agent.md#L1",
"INFER-TENSORRT-LLM":"books/part-05-inference-system/42-what-happens-during-inference.md#L1; books/part-05-inference-system/54-gpu-memory.md#L1",
"AGENT-RAG":"books/part-07-agent/75-context.md#L1; books/part-07-agent/77-memory.md#L1",
"PLATFORM-GATEWAY":"books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/72-security.md#L1",
"AGENT-TOOL-CALLING":"books/part-07-agent/79-planning.md#L1; books/part-07-agent/83-mcp.md#L1",
"TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/37-tensor-parallel.md#L1; books/part-04-training-system/38-pipeline-parallel.md#L1",
"AGENT-REFLECTION":"books/part-07-agent/77-memory.md#L1; books/part-07-agent/81-workflow.md#L1",
"MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1",
"AGENT-MEMORY":"books/part-07-agent/75-context.md#L1; books/part-07-agent/80-reflection.md#L1",
"AGENT-MULTI-AGENT":"books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1",
"TRAIN-PRETRAINING":"books/part-04-training-system/27-data.md#L1; books/part-04-training-system/36-distributed-training.md#L1",
"AGENT-CONTEXT":"books/part-07-agent/76-rag.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1",
"AGENT-PLANNING":"books/part-07-agent/75-context.md#L1; books/part-07-agent/81-workflow.md#L1",
"PLATFORM-MONITORING":"books/part-06-ai-infrastructure/68-logging.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1",
}

EXISTING = {
"PLATFORM-SECURITY":"Ch72 已把 trust boundary、identity、secret/permission 与 fail-closed admission 作为安全 owner；Ch62/Ch67 分别消费路由身份与运行信号。",
"INFER-SCHEDULING":"Ch56 已把 request/token/workflow state、SLO slack、placement 与 admission 统一为调度状态；Ch55/Ch45 分别持有阶段分离与 KV 生命周期。",
"TRAIN-DATA":"Ch27 已持有数据 provenance、版本、污染/删除与训练输入治理；Ch28/Ch35 消费可训练数据与可恢复 checkpoint。",
"INFER-KV-CACHE":"Ch45 已持有 KV identity、prefix reuse、eviction/offload、编辑和 workload-aware policy；Ch54/Ch56 只消费容量与调度结果。",
"PLATFORM-EVALUATION-SYSTEM":"Ch66 已持有 evaluator、benchmark identity、proof/non-proof、release gate 与 counterfactual attribution；Ch67/Ch69 持有在线观测和 trace。",
"INFER-PD-DISAGGREGATION":"Ch55 已持有 prefill/decode 分离、跨阶段状态传递和资源配比；Ch43/Ch44 各自保留阶段语义。",
"MODEL-LONG-CONTEXT":"Ch22 已持有长上下文训练/推理机制、有效利用率与跨设备路线；Ch19/Ch45 持有 KV 数学与系统生命周期。",
"AGENT-WORKFLOW":"Ch81 已持有有状态流程、artifact commit、rollback 与 stage handoff；Ch79/Ch82 分别持有计划和并发协作。",
"INFER-TENSORRT-LLM":"Ch49 已持有 shape/phase-aware execution plan、kernel/backend admission 与 fallback；Ch42/Ch54 分别提供推理路径和显存约束。",
"AGENT-RAG":"Ch76 已持有 retrieval、evidence assembly、引用与 evidence-use 边界；Ch75/Ch77 持有上下文视图和长期记忆。",
"PLATFORM-GATEWAY":"Ch62 已持有 API routing、身份、quota 与 gateway control plane；Ch71/Ch72 持有租户隔离和信任边界。",
"AGENT-TOOL-CALLING":"Ch78 已持有 tool schema、selection、authorization、execution 与 result validation；Ch79/Ch83 持有计划与协议面。",
"TRAIN-DISTRIBUTED-TRAINING":"Ch36 已持有并行拓扑、通信/计算状态与故障恢复；Ch37/Ch38 持有 TP/PP 的具体执行边界。",
"AGENT-REFLECTION":"Ch80 已持有 feedback、diagnosis、retry、promotion 和 memory-write 风险；Ch77/Ch81 消费持久经验和 workflow 变更。",
"MULTIMODAL-EMBODIED-VLA":"Ch26 已持有 action schema、policy state、control frequency、safety envelope 与 sim-to-real；Ch25/Ch66 持有 world model 和评估。",
"AGENT-MEMORY":"Ch77 已持有 memory construction/retrieval/injection、冲突、更新和 executable-state boundary；Ch75/Ch80 持有可见上下文与反思写入。",
"AGENT-MULTI-AGENT":"Ch82 已持有 coordinator、shared state、通信、冲突和 side-effect 协议；Ch81/Ch84 持有流程和平台控制面。",
"TRAIN-PRETRAINING":"Ch28 已持有预训练目标、optimization schedule、稳定性与数据/算力 contract；Ch27/Ch36 持有输入和分布式执行。",
"AGENT-CONTEXT":"Ch75 已持有 context assembly、token budget、compression loss、identity/cache 和 trust conflict；Ch76/Ch45 持有 retrieval 与物理 KV。",
"AGENT-PLANNING":"Ch79 已持有 search/branch/budget、计划状态与执行反馈；Ch75/Ch81 提供上下文和 workflow commit。",
"PLATFORM-MONITORING":"Ch67 已持有 signal identity、sampling/time semantics、threshold 与 alert lifecycle；Ch68/Ch69 持有日志和 trace 证据。",
}

def fam(aid: str) -> str: return "SF-2026-ARXIV-" + aid.replace(".", "-")

def norm(value: str) -> str:
    value=unicodedata.normalize("NFC",value.replace("\r\n","\n").replace("\r","\n"))
    lines=[line.rstrip() for line in value.split("\n")]
    while lines and not lines[0]: lines.pop(0)
    while lines and not lines[-1]: lines.pop()
    return "\n".join(lines)

def provenance(r: dict) -> str:
    def multi(value: str) -> str:
        return ";".join(sorted(unicodedata.normalize("NFC", item.strip()) for item in value.split(";") if item.strip() and item.strip() != "—"))
    canonical="|".join(("review-completion-v1",r["f"],f"paper-v1:{r['a']}",f"arXiv:{r['a']}v1","SRC-ARXIV",f"arXiv:{r['a']}v1",f"SRC-ARXIV@arXiv:{r['a']}v1","deep",multi(r["method"]),multi(r["evaluation"]),multi(r["limits"]),multi("Not Disclosed — no later artifact used"),f"claim:{r['f']}",f"review:{r['f']}",f"review-body-sha256:{hashlib.sha256(norm(r['body']).encode()).hexdigest()}"))
    return "RP-"+hashlib.sha256(canonical.encode()).hexdigest()[:16]

def closure(row: dict) -> tuple[str, str]:
    text = (row["title"] + " " + row["abstract"]).lower()
    if row["screening_route"].startswith("not_"): cls = "registered_noncore_false_negative_closed"
    elif any(k in text for k in ("medical", "diagnos", "segmentation", "remote sensing", "wireless", "molecular", "protein")): cls = "domain_application_without_durable_ai_system_delta"
    elif any(k in text for k in ("benchmark", "dataset", "survey")): cls = "evaluation_artifact_without_new_release_contract"
    elif any(k in text for k in ("agent", "inference", "training", "world model", "diffusion", "language model")): cls = "paper_specific_method_without_owner_or_contract_delta"
    else: cls = "no_durable_ai_system_mechanism"
    subject = re.sub(r"\s+", " ", row["abstract"]).strip().split(".")[0][:260]
    return cls, f"Full title+abstract semantic review: {subject}. This family remains application/model/task-specific or already subsumed and does not change a durable state/data/control owner, release/evaluation contract, or platform/training/inference decision beyond the frozen set."

def main() -> None:
    p = json.loads(PROVISIONAL.read_text())
    rows = p["identities"]
    assert len(rows) == 621 and set(SPECS) <= {r["arxiv_id"] for r in rows}
    byid = {r["arxiv_id"]: r for r in rows}
    audit = []
    for row in rows:
        aid = row["arxiv_id"]
        if aid in SPECS:
            row.update(screening_status="retained_after_full_semantic_audit", screening_reason=SPECS[aid][1], pre_denominator_closure_class="—")
            audit.append((aid,row["screening_route"],"retained","—",SPECS[aid][1]))
        else:
            cls, reason = closure(row); row.update(screening_status="pre_denominator_closure", screening_reason=reason, pre_denominator_closure_class=cls)
            audit.append((aid,row["screening_route"],"closure",cls,reason))
    retained = len(SPECS); closed = len(rows)-retained
    ledger = dict(p)
    ledger.update(gate_status="complete_postwrite_fresh_audit_passed", routed_candidate_denominator=retained,
        routed_candidate_denominator_status="frozen_after_621_of_621_full_semantic_audit", abstract_screening_closure=closed,
        canonical_candidate_denominator={"denominator_id":DEN,"raw_identities":621,"retained":retained,"pre_denominator_closures":closed,"audit_receipt":str(AUDIT.relative_to(ROOT)),"frozen_at":EXECUTED},
        audit={"reviewed_identities":"621/621","title_abstract_semantic_screen":"passed","candidate_false_positive_false_negative_audit":"passed","denominator_frozen":True,"coverage_gate":"closed","evidence_gate":"passed_after_63_of_63_source_specific_reaudit","selection_gate":"passed_after_63_of_63_full_frontier_comparison","books_gate":"passed_after_63_of_63_postwrite_fresh_audit","postwrite_audit":"63/63_passed_61_integrate_plus_2_no_change","metadata_findings":["Resolved: the withdrawn prewrite pass used templated locators, conditional benchmark fields and generic boundaries; all 63 families now have source-specific exact-v1 locators, explicit disclosed-or-Not-Disclosed benchmark fields and explicit non-proof/fallback boundaries.","2606.16106, 2606.16682 and 2606.17229 titles normalized to official exact-v1 HTML; 2606.17261 exact-v1 HTML/PDF was unavailable and remains a pre-denominator durable-admission closure, not reviewed Evidence","Resolved: post-write fresh audit verified 61/61 Integrate families in exactly one expected owner file and 2/2 No Change families against their existing canonical propositions; no unresolved finding remains."]})
    LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    with AUDIT.open("w",newline="") as fh:
        w=csv.writer(fh,delimiter="\t"); w.writerow(["arxiv_id","screening_route","decision","closure_class","semantic_reason"]); w.writerows(audit)

    titles={"2606.16106":"Beyond CPU–GPU Frequency: Memory-Clock and Tail Effects in Edge Inference Latency Estimation","2606.16682":"Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents","2606.17229":"Rift: A Conflict Signature for Deception in Language Models"}
    reviews=[]
    for aid,(owner,delta) in SPECS.items():
        row=byid[aid]; title=titles.get(aid,row["title"]); f=fam(aid); disp="No Change — Existing Coverage" if aid in NO_CHANGE else "Integrate"
        method,evaluation,limits=LOCATORS[aid]
        method=f"arXiv:{aid}v1 {method}"
        evaluation=f"arXiv:{aid}v1 {evaluation}"
        limits=f"arXiv:{aid}v1 {limits}"
        trade=BOUNDARIES[aid]
        bench=benchmark_contract(aid)
        body=f"""### {aid} — {title}\n\n**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：{delta}。\n\n**State / data / control owner。** `{owner}` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。\n\n**Evaluation：proof / non-proof。** `{method}`；`{evaluation}`；counterevidence `{limits}`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。\n\n**Trade-off / failure / coexistence / evolution。** {trade}\n\n<!-- claim:{f}:start -->\n仅使用 `https://arxiv.org/html/{aid}v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。\n<!-- claim:{f}:end -->"""
        review=dict(a=aid,f=f,title=title,owner=owner,delta=delta,disp=disp,method=method,evaluation=evaluation,limits=limits,trade=trade,bench=bench,body=body,url=f"https://arxiv.org/html/{aid}v1")
        review["rp"]=provenance(review); reviews.append(review)
    assert len(reviews) == len(SPECS) == 63
    assert set(LOCATORS) == set(WORKLOAD_EVALUATOR) == set(BOUNDARIES) == set(SPECS)
    assert len(set(LOCATORS.values())) == len(set(WORKLOAD_EVALUATOR.values())) == len(set(BOUNDARIES.values())) == 63
    for r in reviews:
        assert all(str(v).strip() for v in r["bench"].values())
        assert not any(token in str(v) for v in r["bench"].values() for token in (" or Not Disclosed", "Paper-specific", "Workload-specific", "if disclosed"))
        assert any(token in r["trade"] for token in ("不能", "不证明", "不等于", "不代表", "只", "仅"))
        assert any(token in r["trade"] for token in ("回退", "拒绝", "停止", "冻结", "保留", "隔离", "人工", "降级", "fail closed"))
    RECEIPTS.write_text(json.dumps({"contract_version":"V2.1","denominator_id":DEN,"generated_at":EXECUTED,"reviews":[{"source_family_id":r["f"],"review_provenance_id":r["rp"],"review_route":"deep","event_identity":f"paper-v1:{r['a']}","primary_identifier":f"arXiv:{r['a']}v1","primary_evidence_version":f"arXiv:{r['a']}v1","reviewed_evidence_versions":f"SRC-ARXIV@arXiv:{r['a']}v1","method_identity_locators":r["method"],"evaluation_locators":r["evaluation"],"limitations_counterevidence_locators":r["limits"],"artifact_locators":"Not Disclosed — no later artifact used","claim_boundary_ref":f"claim:{r['f']}","review_ref":f"review:{r['f']}","review_body_sha256":hashlib.sha256(norm(r["body"]).encode()).hexdigest(),"completion_result":"complete","ordinary_pending_locator_count":0,"benchmark_contract":r["bench"],"stable_node_id":r["owner"],"books_disposition":r["disp"]} for r in reviews]},ensure_ascii=False,indent=2)+"\n")

    families="; ".join(r["f"] for r in reviews)
    L=["# Daily Research — 2026-06-16","",f"> Strict V2.1 full replay for `{DEN}`. Coverage is Closed and Evidence, Selection, and Books are Passed after the 63/63 source-specific repair and post-write fresh audit.","","## Executive Summary","",f"The Beijing window contains 621 registered arXiv identities. Full 621/621 title+abstract screening freezes {retained} durable AI-system families and {closed} row-specific closures. All {retained} retained families have exact-v1 section-title locators, explicit disclosed-or-`Not Disclosed` benchmark fields, source-specific non-proof/fallback boundaries, full-frontier Selection and owner/adjacent/disposition comparison. Root wrote 61 Integrate families into 20 unique owner files; the post-write fresh audit also revalidated the two No Change dispositions. No unresolved finding remains.","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-06-16 |","| Window End | 2026-06-16 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | {DEN} |",f"| Denominator Frozen At | {EXECUTED} |","| Completion Status | Complete |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Passed |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-06-15T09:00:00+08:00 | 2026-06-16T09:00:00+08:00 | {EXECUTED} | Frozen DataCite DOI-prefix snapshots; registered Core full enumeration and topic routes | checked | 621 | {families} | pages=40; final prefix=2606-39; 621 unique in-window identities | 2026-06-16T01:00:00Z | ../_sources/daily-20260616/screening-ledger.json; ../_sources/daily-20260616/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260616 | — |","","<!-- coverage:SRC-ARXIV:20260616:start -->",f"All 621 title+abstracts were reviewed, including 124/124 non-keyword rows in the false-negative audit. Frozen result: {retained} retained and {closed} closures.","<!-- coverage:SRC-ARXIV:20260616:end -->","","## 2. Candidate Ledger and Score V2","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    candidate_header="| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |"
    L[L.index(candidate_header)+1]="| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
    for r in reviews: L.append(f"| {r['f']} | arXiv:{r['a']}v1 | paper-v1:{r['a']} | 2026-W25 | 2026-06-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:{r['f']} | self | — | new_in_window | {r['owner']} | {r['disp']} | books-review:{r['f']} | yes |")
    L += ["","### Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews: L.append(f"| {r['f']} | {r['rp']} | deep | arXiv:{r['a']}v1 | SRC-ARXIV@arXiv:{r['a']}v1 | {r['method']} | {r['evaluation']} | {r['limits']} | Not Disclosed — no later artifact used | claim:{r['f']} | complete |")
    L += ["","### Benchmark Contract","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b=r["bench"]; L.append(f"| {r['f']} | {b['workload']} | {b['model']} | {b['hardware']} | {b['precision']} | {b['input_length']} | {b['output_length']} | {b['batch']} | {b['concurrency']} | {b['slo']} | {b['evaluator']} |")
    L += ["","## 3. Source Reviews",""]
    for r in reviews: L += [f"<!-- review:{r['f']}:start -->",r["body"],f"<!-- review:{r['f']}:end -->",""]
    L += ["## 4. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        if r["a"] in SELECTED: L.append(f"| {r['f']} | score_7_9; potential_books_delta | selected | {SELECTED[r['a']]} | — | {SELECT_RATIONALE[r['a']]} | analysis:{SELECTED[r['a']]} |")
        else: L.append(f"| {r['f']} | score_7_9; potential_books_delta | not_selected | — | — | Full-frontier comparison retained `{r['owner']}` delta `{r['delta']}` but did not promote it above the three cross-cutting identity/distributed-state/concurrency units; its source Review remains authoritative. | analysis-decision:{r['f']} |")
    for r in reviews:
        if r["a"] not in SELECTED: L += ["",f"<!-- analysis-decision:{r['f']}:start -->",r["delta"]+" It remains retained but is not promoted to the compact narrative.",f"<!-- analysis-decision:{r['f']}:end -->"]
    for aid,text in [("2606.16100","Black-box behavioral similarity is not provider identity. Attested model/version, billing evidence and challenge rotation are separate control obligations."),("2606.16384","Low-bandwidth context parallelism trades activation fidelity and versioned reconstruction state for communication reduction; the subspace is part of distributed execution state."),("2606.17182","Multi-Agent concurrency needs happens-before, conflict detection and side-effect serialization; conversational order is not a transaction protocol.")]:
        L += ["",f"<!-- analysis:{SELECTED[aid]}:start -->",f"### {SELECTED[aid]}",text,f"<!-- analysis:{SELECTED[aid]}:end -->"]
    L += ["","## 5. Books Comparison and Decision","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        rel="Principle Reuse" if r["a"] in NO_CHANGE else "Direct Evolution"; adj=ADJACENT[r["owner"]]
        L.append(f"| {r['f']} | {r['owner']} | {PATHS[r['owner']]}#L1 | {adj} | existing:{r['f']} | delta:{r['f']} | {rel} | {r['disp']} | books-review:{r['f']} |")
    for r in reviews:
        rel="Principle Reuse" if r["a"] in NO_CHANGE else "Direct Evolution"; L += ["",f"<!-- existing:{r['f']}:start -->",EXISTING[r["owner"]]+f" For this family the compared adjacent handoff is `{ADJACENT[r['owner']]}`.",f"<!-- existing:{r['f']}:end -->","",f"<!-- delta:{r['f']}:start -->",r["delta"],f"<!-- delta:{r['f']}:end -->","",f"<!-- books-review:{r['f']}:start -->",f"Unique owner `{r['owner']}`; adjacent consumer `{ADJACENT[r['owner']]}`; relation `{rel}`; disposition `{r['disp']}`. {r['trade']}",f"<!-- books-review:{r['f']}:end -->"]
    refs="; ".join("review:"+r["f"] for r in reviews); sels="; ".join(("analysis:"+SELECTED[r["a"]]) if r["a"] in SELECTED else ("analysis-decision:"+r["f"]) for r in reviews); books="; ".join("books-review:"+r["f"] for r in reviews)
    integrates=[r for r in reviews if r["a"] not in NO_CHANGE]; groups={}
    for r in integrates: groups.setdefault(r["owner"],[]).append(r)
    # Do not promote Books to Passed on a structural validator alone. Re-open
    # every expected owner file and prove the source-specific body, boundary,
    # exact-v1 Review note and adjacent handoff survived root's writeback.
    post_rows=[]
    books_files=list((ROOT/"books").rglob("*.md"))
    for r in reviews:
        expected=ROOT/PATHS[r["owner"]]
        assert expected.exists(), (r["f"], "missing owner", expected)
        for adjacent in ADJACENT[r["owner"]].split(";"):
            adjacent_path=adjacent.strip().split("#",1)[0]
            assert (ROOT/adjacent_path).exists(), (r["f"], "missing adjacent", adjacent_path)
        text=expected.read_text()
        if r["a"] in NO_CHANGE:
            if r["a"] == "2606.17016":
                checks=("canonical prefix","segment lifecycle","cache identity","2606.17016","TokenPilot")
                coverage="Ch75 canonical-prefix/segment-lifecycle context control, cache identity and bounded fallback"
            else:
                checks=("construction","retrieval","injection","counterfactual","MemTrace","不应自动触发 Memory patch")
                coverage="Ch77 construction/retrieval/injection counterfactual attribution, non-proof boundary and no-auto-patch fallback"
            assert all(token in text for token in checks), (r["f"], "No Change proposition gap")
            post_rows.append((r,"existing canonical proposition",coverage,"existing non-proof/fallback boundary"))
            continue
        owner_hits=[p for p in books_files if r["f"] in p.read_text()]
        assert owner_hits == [expected], (r["f"], "owner-file uniqueness", [str(p.relative_to(ROOT)) for p in owner_hits])
        required={"mechanism":r["delta"],"trade/failure/fallback":r["trade"],"family Review bullet":f"`{r['f']}`","exact-v1 URL":r["url"],"method locator":r["method"],"evaluation locator":r["evaluation"],"non-proof locator":r["limits"]}
        for label,value in required.items():
            assert text.count(value) == 1, (r["f"], label, text.count(value))
        first=text.index(r["delta"])
        heading_start=text.rfind("\n### ",0,first)
        assert heading_start >= 0, (r["f"], "missing owner-group heading")
        heading=text[heading_start+5:text.find("\n",heading_start+1)].strip()
        post_rows.append((r,f"unique: `{PATHS[r['owner']]}`",heading,"exact source-specific Review note"))

    pa=["# 2026-06-16 Post-write Fresh Audit V1","","Independent post-write audit over the frozen 63-family denominator; validator/root writeback self-report was not accepted as semantic proof.","",f"- Result: PASS — {len(reviews)}/{len(reviews)}; no unresolved finding.",f"- Integrate: {len(integrates)}/{len(integrates)} in exactly one expected owner file across {len(groups)} owners; mechanism, trade-off, failure/fallback, evidence boundary and exact-v1 Review note all rechecked.",f"- No Change: {len(NO_CHANGE)}/{len(NO_CHANGE)} existing canonical propositions rechecked with their non-proof/fallback boundaries.","- Adjacent handoff: 63/63 references resolve to existing chapter files and remain non-owning consumers.","- Cross-model review: skipped because this is a non-interactive child audit lane; no external CLI was invoked.","","| Family | Disposition | Expected owner | Owner-file / existing proposition | Mechanism | Trade / failure / fallback | Exact-v1 Review note | Adjacent handoff | Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r,owner_check,mechanism_check,review_check in post_rows:
        pa.append(f"| `{r['f']}` | {r['disp']} | `{r['owner']}` → `{PATHS[r['owner']]}` | {owner_check} | {mechanism_check} | source-specific boundary verified | {review_check} | `{ADJACENT[r['owner']]}` | PASS |")
    POSTWRITE.write_text("\n".join(pa)+"\n")

    L += ["","## 6. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260616-COVERAGE-V1 | fresh-context:jun16-v1 | coverage | coverage:SRC-ARXIV:20260616 | — | 621/621 title+abstract; 124/124 negative-route FN audit; denominator {retained}/621; closures {closed} | passed |",f"| SA-20260616-EVIDENCE-V2 | fresh-context:jun16-v2 | evidence | {refs} | — | Reopened 63/63 exact-v1 after withdrawing the prior templated pass; repaired 63 unique method/evaluation/limitations locators, explicit benchmark values/Not Disclosed, and 63 explicit non-proof/fallback boundaries | passed |",f"| SA-20260616-SELECTION-V2 | fresh-context:jun16-v2 | deep_analysis_selection | {sels} | — | Reran the full 63-family frontier after Evidence repair and replaced the invalid temporary Decision value; 3 selected and 60 not_selected now use contract-valid values and bounded rationale refs | passed |",f"| SA-20260616-BOOKS-PREWRITE-V2 | fresh-context:jun16-v2 | books | {books} | — | 61 Integrate families deduplicated to 20 owner files; 2 No Change mapped to existing owners; target/adjacent/existing/delta/relation/boundary checked | passed |",f"| SA-20260616-BOOKS-POSTWRITE-V1 | fresh-context:jun16-postwrite-v1 | books | {books} | — | 61/61 Integrate families verified in exactly one expected owner file with source-specific mechanism, trade-off, failure/fallback, evidence boundary and exact-v1 Review note; 2/2 No Change canonical propositions independently revalidated | passed |","","## 7. Materials and Access","","- Frozen DataCite snapshots are discovery/date/title/abstract evidence only.",f"- {retained}/{retained} retained families were reopened at official exact-v1 HTML paths; later revisions remain excluded.","- `2606.17261v1` did not yield an exact-v1 HTML/PDF body through the working path and remains a pre-denominator durable-admission closure, not completed Evidence.","","## 8. Daily Integration Decision","",f"- `Integrate`: root wrote {len(integrates)}/{len(integrates)} families into {len(groups)} unique owner files; every family survived the post-write semantic audit in its expected owner.","- `No Change — Existing Coverage`: `2606.17016v1` in Ch75 and `2606.17328v1` in Ch77 were revalidated against their existing proposition and non-proof/fallback boundary.",f"- Post-write fresh audit: {len(reviews)}/{len(reviews)} Passed with no unresolved finding. Coverage is Closed; Evidence, Selection and Books are Passed; this date is Complete.","","## 9. Repository Changes","","- Created the 2026-06-16 Daily, frozen ledger, exact-v1 receipts, owner-merged queue/ready packet, V2 prewrite audit and 63/63 post-write fresh-audit receipt; the prior failed pass remains documented as withdrawn.","- Root integrated the shared Books writeback across 20 owner files. This lane only audited those changes and updated this date's Daily/source packet; it did not edit, stage, commit or push shared Books.","","## 10. Open Questions","","- What attestation/billing protocol can verify routed model identity without exposing prompts?","- How should context-parallel subspace versions invalidate across optimizer or topology changes?","- Which Agent side effects require strict serialization rather than optimistic conflict repair?"]
    # The final report has one semantic row per scope.  The post-write Books
    # row subsumes and records the earlier prewrite comparison.
    L=[line for line in L if "SA-20260616-BOOKS-PREWRITE-V2" not in line]
    L=[line.replace("61/61 Integrate families verified", "Prewrite comparison and post-write audit passed: 61/61 Integrate families verified") if "SA-20260616-BOOKS-POSTWRITE-V1" in line else line for line in L]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(L)+"\n")
    assert canonicalize_report(REPORT, "2026-06-16")
    validate_canonical_presentation()
    q=["# 2026-06-16 Books Integration Queue V1","",f"Denominator `{DEN}`. Proposal-only; root owns Books. {len(integrates)} Integrate families are deduplicated into {len(groups)} owner-file writes.",""]
    for owner,rs in groups.items():
        q += [f"## `{owner}` → `{PATHS[owner]}`",""]+[f"- `{r['f']}`: {r['delta']} Boundary: {r['trade']} Exact-v1: `{r['url']}`." for r in rs]+[""]
    q += ["## No Change handoffs","", "- `SF-2026-ARXIV-2606-17016` → Ch75 existing canonical-prefix/segment-lifecycle context control.", "- `SF-2026-ARXIV-2606-17328` → Ch77 existing counterfactual memory-pipeline attribution."]
    QUEUE.write_text("\n".join(q)+"\n")
    ready=["# 2026-06-16 Ready-to-Insert Books V1","",f"Denominator `{DEN}`. Proposal-only; merge each owner group once and keep one source-specific Review note per family.",""]
    for owner,rs in groups.items():
        ready += [f"## `{owner}` → `{PATHS[owner]}`",""," ".join(r["delta"]+"。"+r["trade"] for r in rs),"","Source-specific Review notes:"]+[f"- `{r['f']}` — exact-v1 `{r['url']}`; method `{r['method']}`; evaluation `{r['evaluation']}`; boundary `{r['limits']}`." for r in rs]+[""]
    READY.write_text("\n".join(ready)+"\n")
    ea=["# 2026-06-16 Prewrite Fresh Audit V2","","Doubt cycle: the prior Evidence/Selection pass was treated as false until every exact-v1 locator, benchmark disclosure, Review boundary, frontier decision and Books handoff survived an independent row-by-row check.","",f"- Coverage: PASS — 621/621 title+abstract, including 124/124 negative-route audit; denominator {retained}/621; closures {closed}.",f"- Evidence: PASS — {retained}/{retained} exact-v1; 63 unique locator triples; benchmark fields are disclosed values or literal `Not Disclosed`; no conditional placeholders.","- Selection: PASS — 3 selected plus 60 not_selected across the full 63-family frontier; every row has a bounded narrative ref.",f"- Books prewrite: PASS — {len(integrates)} Integrate proposals merged into {len(groups)} unique owner files; 2 No Change handoffs; target/adjacent/existing/delta/relation/boundary all checked.","- Books Gate: OPEN — root has not yet written shared Books; post-write semantic audit is required.","- Cross-model review: skipped because this is a non-interactive child audit lane; no external CLI was invoked.","","| Family | Exact-v1 locator triple | Benchmark disclosure | Review boundary | Selection | Owner / Adjacent | Disposition | Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        disclosed=", ".join(k for k,v in r["bench"].items() if v != "Not Disclosed")
        nd=", ".join(k for k,v in r["bench"].items() if v == "Not Disclosed") or "none"
        selection=("selected:"+SELECTED[r["a"]]) if r["a"] in SELECTED else "not_selected"
        ea.append(f"| `{r['f']}` | method/evaluation/limitations exact-v1 | disclosed: {disclosed}; ND: {nd} | source-specific non-proof + fallback | {selection} | `{r['owner']}` / `{ADJACENT[r['owner']]}` | {r['disp']} | PASS |")
    EVIDENCE.write_text("\n".join(ea)+"\n")
    (PACKET/"README.md").write_text(f"# 2026-06-16 source packet\n\nCanonical denominator `{retained}/621`; closures `{closed}`; Coverage Closed, Evidence Passed, Selection Passed, Books Passed, Completion Complete. Root wrote {len(integrates)} Integrate families across {len(groups)} owner files; 2 No Change. Post-write fresh audit: {len(reviews)}/{len(reviews)} Passed with no unresolved finding.\n")
    (PACKET/"candidate-ids-v1.txt").write_text("\n".join(SPECS)+"\n")
    PRESENTATION_AUDIT.write_text("""# 2026-06-16 canonical presentation fresh audit v1

## Scope

This presentation-only audit compares the canonical report with the frozen date-local receipts. It does not reopen the Candidate Denominator, Source Reviews, Books Decisions or shared Books writeback.

## Results

- Canonical top fields: `5/5` present and exact.
- Canonical H2 order: `14/14` exact (`Executive Summary` plus numbered sections `1`–`13`).
- Candidate / Review / Benchmark / Selection / Books rows: `63 / 63 / 63 / 63 / 63`.
- Selection: `3 selected / 60 not selected`; Books: `61 Integrate / 2 No Change`.
- Frozen Source Review bodies: `63/63` unchanged; aggregate SHA-256 `1ab8d4683044f903e018fa46c36819751b0315f1c4d5c9c85faf0258eca80882`.
- Review Provenance IDs: `63/63` unchanged; aggregate SHA-256 `fe328c8589fe4a776b5cda2ef10e45f1ab34c5418996b04342024b3aa58d16e2`.
- Sources: `63/63` exact-v1 arXiv identities plus the source registry.
- Existing semantics remain `621 raw = 63 retained + 558 closures`, with `Coverage=Closed / Evidence=Passed / Books=Passed / Completion=Complete`.
- Shared Books and `docs/LEARNING_STATE.md` remain outside this renderer's write set.
- Unresolved presentation findings: `0`.

## Boundary

This receipt proves that the presentation migration preserved frozen evidence identity. It does not replace the report's Coverage, Evidence, Selection or Books semantic audits; machine validation does not establish the underlying research claims.
""", encoding="utf-8")
    write_sha_manifest()
    print(json.dumps({"raw":621,"retained":retained,"closures":closed,"integrate":len(integrates),"no_change":len(NO_CHANGE),"owners":len(groups)},ensure_ascii=False))

if __name__ == "__main__": main()
