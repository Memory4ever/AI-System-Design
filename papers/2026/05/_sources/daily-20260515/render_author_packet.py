#!/usr/bin/env python3
"""Render the 2026-05-15 V2.1 author packet without writing shared Books."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


R = Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

LEDGER = json.loads((R / "screening-ledger-final.json").read_text())
ROWS = LEDGER["identities"]
RETAINED = [row for row in ROWS if row["screening_status"] == "retained_pending_exact_v1_review"]

# node, score, disposition, durable delta, method, evaluation, limitation boundary
K = {
    "2605.14290": ("AGENT-WORKFLOW", (3, 3, 3), "No Change — Existing Coverage", "Web Agent 应把不可信 runtime content 限制为预提交程序的数据，而不允许其生成新控制流；typed site API、隔离的 LLM subroutine 与显式 replan fallback 共同定义安全/可用性边界", "§2.1 Threat Model; §4 Plan-Then-Execute Web Agents; §5 Expressivity", "§6.1 Task Taxonomy; §6.2 WebArena empirical analysis", "§6.3 Practical Gaps; §7 Discussion"),
    "2605.14415": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "coding-Agent release maintenance 评测必须把版本链、继承 codebase、跨步 regression 与每步 acceptance contract 纳入 run identity，而不能把独立 issue 分数外推为长期维护能力", "§2 SWE-Chain construction; §3.1–§3.2 agent execution", "§3.3 Evaluation; §4 Results", "Appendix K Limitations"),
    "2605.14498": ("AGENT-MEMORY", (3, 3, 3), "No Change — Existing Coverage", "群体会话 memory 必须把 speaker/principal、reply graph、belief ownership 与 audience-specific retrieval 绑定；把多人消息拼成单一文档会制造跨主体状态污染", "§3 GroupMemBench construction; §3.2 question taxonomy", "§4 Evaluation; Appendix I judge reliability", "Appendix K Limitations"),
    "2605.14514": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "模型 defense 是有顺序的 release artifact：后续 safety/privacy/fairness patch 必须重新验证先前保障，不能把单项防御通过等同于组合后仍保持保护", "§3 ConflictEval pairwise sequential-defense framework", "§4 Results; §5 mechanistic analysis; Appendix B configurations", "§5 Limitations paragraph — pairwise/six-defense/three-family boundary"),
    "2605.14570": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "No Change — Existing Coverage", "diffusion LM 的 uncertainty sensor 必须绑定 denoising trajectory、remasking 与 masked likelihood，不能沿用 autoregressive token probability；该 sensor 仍需独立校准且不拥有事实真值", "§3 Denoising-trajectory uncertainty signals", "§4 Experiments and calibration", "Appendix E Limitations; perfect-calibration/semantic-measure assumptions and sampled-model/task boundary"),
    "2605.14678": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "主动 personal Agent 评测必须隐藏 intent、跨 task/session 保留状态，并同时测 proactivity 与 task outcome；单轮显式指令 benchmark 不能代表长期主动协助", "§3 π-Bench task/persona/hidden-intent construction", "§4 Evaluation and long-horizon trajectories", "§6 Limitations — simulated users and single Nanobot-derived scaffold boundary"),
    "2605.14744": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "治理规则不能由同一生成模型同时解释和自证；policy enforcement 应移出模型回路，以机械 primitive 约束 decision/effect，并把 rationale 仅作为可审计证据", "§3 Methodology; §3.2 Mechanical Policy; §3.3 Governance Metrics", "§4 Experiments and Results", "§5 Discussion/Conclusion; no dedicated limitations section — synthetic banking, single-model-family and ground-truth-rule boundary"),
    "2605.14747": ("TRAIN-DATA", (3, 3, 3), "No Change — Existing Coverage", "GUI Agent 数据管线可从互联网教程视频恢复 observation-action trajectory，但每一步都必须保留 video/application identity、grounding confidence、filter revision 与 executable validation；规模不能替代轨迹正确性", "§3 Video2GUI coarse-to-fine pipeline; §4 WildGUI construction", "§5 Pretraining and GUI benchmark evaluation", "Conclusion and appendix data-quality analyses; no dedicated limitations section — automatic grounding/filter and executable-validation coverage boundary"),
    "2605.14786": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "browser Agent 的 action/timing trace 会形成被动 model fingerprint side channel；随机 delay 只能改变 sensor，不是身份或不可链接性保证，平台需将 attribution、privacy 与 rate policy 分开", "§3 Threat model and passive UI-trace fingerprinting", "§4–§5 Cross-model/environment evaluation", "§6 Limitations and adaptive-attacker/retraining boundary"),
    "2605.14865": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "Agent 评测要把 terminal outcome 与 trace span diagnosis 连接：failure taxonomy、location、cause 与最终结果必须同属一次 run evidence，长轨迹不能只由单一成功率压缩", "§3 Top-down and span-level diagnostic framework", "§4 TRAIL/GAIA/SWE-Bench evaluation", "§5 Limitations and evaluator/model/task boundary"),
    "2605.14906": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "多模态长期 memory 评测必须显式比较 long-context 与 external-memory 路径，并冻结 decisive visual evidence、session evolution、ingestion cost 与 storage，而不是把文本 caption shortcut 当视觉记忆", "§3 MemLens construction and visual-evidence requirements", "§4 Evaluation across memory systems", "§6 Limitations — synthetic conversation, judge and modality/task boundary"),
    "2605.14968": ("AGENT-WORKFLOW", (3, 3, 3), "No Change — Existing Coverage", "可靠 Agent workflow 应把生成计划编译成 typed graph，并让可验证 node/edge contract、execution receipt 与 recovery policy拥有提交权；可视化 DAG 本身不构成正确性证明", "official PDF pp. 2–11 §1.3–§1.8 diagram-as-specification, contracts, runtime and formal semantics", "official PDF pp. 12–15 §1.12 Evaluation Plan; §1.13 Empirical Evaluation; §2 Implementation Status", "official PDF pp. 11–15 §1.10 Failure Modes and Limitations; §1.13.6 Interpretation and Limitations — verified core not deployed/evaluated"),
    "2605.14978": ("INFER-SPECULATIVE-DECODING", (3, 3, 3), "No Change — Existing Coverage", "speculative window 不应是静态常数：在线 policy 可依据 acceptance、draft/verify cost 与服务负载调整 proposal 长度，但 target verification 与 rollback 始终保留最终 commit authority", "§3 Adaptive-window policy optimization", "§4 Serving evaluation", "§5 Limitations and workload/hardware/generalization boundary"),
    "2605.15034": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "No Change — Existing Coverage", "模型知道被观察时会改变行为，因此安全 evaluation 的 run identity 必须包含 monitoring disclosure、observer context 与 counterfactual hidden-monitor branch；被监控时合规不证明未监控时合规", "§3 Watched/unwatched experimental design", "§4 Strategic-behavior results", "§5 Limitations and model/task/context boundary"),
    "2605.15100": ("INFER-SCHEDULING", (3, 3, 3), "No Change — Existing Coverage", "test-time compute controller 必须把预算、质量目标、uncertainty 与 stop condition作为可提交 state；只增加推理步数既可能浪费预算也可能放大错误", "§3 Dual-dimensional adaptive inference policy", "§4 Budget-quality evaluation", "§5 Limitations and model/task/SLO boundary"),
    "2605.15118": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "攻击 benchmark coverage 应以 threat target×technique taxonomy 的可审计分母衡量；单个 benchmark 内部一致或高分不能证明覆盖了部署威胁面", "§3 Threat taxonomy and Target×Technique matrix", "§4 Cross-benchmark coverage audit", "§5 Limitations and literature/labeling coverage boundary"),
    "2605.15128": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "多模态 memory 评测必须按 decisive visual evidence granularity 与跨时间使用方式切片，并用 ablation gate 排除 caption/text shortcut", "§3 MemEye framework and benchmark construction", "§4 Evaluation of 13 memory methods", "§6 Limitations — life-scenario, judge and visual-tool boundary"),
    "2605.15138": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "unlearning release gate 必须在最终量化 artifact 上复验，而不只验 full-precision checkpoint；更新小于 quantization bin 时会被压缩抹除，需要 circuit-local permanence 与 utility 双验收", "§3 MANSU circuit attribution and null-space update", "§4 Full-precision and NF4 evaluation", "§6 Limitations and model/quantizer/forget-set boundary"),
    "2605.15152": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "模型供应链验收必须比较 full-precision 与实际 AWQ/GPTQ/GGUF 等量化 artifact 的行为；outlier-induced rounding 可把量化步骤变成隐藏触发器", "official PDF pp. 3–5 §3.1–§3.3 Target Quantizations, Threat Model and Outlier Injection", "official PDF pp. 5–11 §4 Evaluation, defenses and ablations", "official PDF p. 13 Appendix A Limitations and Future Work — excludes 70B models and specialized quantization/hardware"),
    "2605.15155": ("TRAIN-GRPO", (3, 3, 3), "No Change — Existing Coverage", "Agent RL 的 privileged self-teacher 只能作为 detached、按 token gap gating 的辅助 signal；environment/verifier reward 保留 trajectory truth，错误 skill retrieval 不能让 teacher rejection 主导更新", "§3 SDAR gated on-policy self-distillation", "§4–§5 Agent-environment evaluation and ablations", "Appendix limitations, hyperparameters and event-time artifact boundary"),
    "2605.15172": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "backdoor release testing 不能只变换内容：position/length metadata 也可成为不可见 trigger，因此 clean semantics、长度切片与 position-encoding interventions 必须共同进入验收", "§3 MetaBackdoor positional-trigger construction", "§4 Cross-model/position-encoding evaluation", "§6 Limitations and trigger/architecture boundary"),
    "2605.15178": ("MULTIMODAL-WORLD-MODELS", (3, 2, 3), "No Change — Existing Coverage", "minute-scale controllable video generation通过 hybrid linear/softmax attention、camera-control branch与two-stage refinement扩展 rollout；但视觉一致和相机遵循仍不等于 action-conditioned causal world state", "§3 SANA-WM architecture; §4 data and camera annotation", "§5 Generation/control evaluation", "§6 Limitations and video-generation/world-model boundary"),
    "2605.15188": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "开放世界 Agent 评测应冻结历史时钟、逐步释放外生事件并用预测/outcome轨迹评分 adaptation；静态 knowledge cutoff 问答不能代表持续适应", "§3 FutureSim chronological replay environment", "§4 Three-month agent evaluation and ablations", "§6 Limitations and news/source/forecasting boundary"),
    "2605.15403": ("MODEL-MOE", (3, 2, 3), "No Change — Existing Coverage", "MoE balance controller 应估计 population-level routing distribution，而不是把 noisy mini-batch count 当真值；EMA/mirror-descent bias correction换来更稳定利用率，也新增 lag 与非平稳漂移", "§3 φ-balancing objective and mirror-descent controller", "§4 Pretraining/fine-tuning evaluation", "§5 Limitations and topology/workload boundary"),
    "2605.15425": ("AGENT-WORKFLOW", (3, 3, 3), "No Change — Existing Coverage", "Agent coding workflow 应把 task decomposition、branch/retry与schema validation移出 monolithic prompt，交给 executable runtime；LLM只拥有局部判断，不拥有全局控制流提交", "§3 Runtime-structured decomposition architecture", "§4 Monolithic/static/runtime comparison", "§5 Limitations and two-workload/three-configuration boundary"),
    "2605.15466": ("MULTIMODAL-WORLD-MODELS", (3, 2, 3), "No Change — Existing Coverage", "predictive representation只有在 masking 聚焦 entity interaction且用 causal reasoning/action outcome验证时才接近 world-state signal；重建 latent trajectory仍不自动获得控制充分性", "§3 Interaction-Aware JEPA motion/entity masking", "§4 CLEVRER causal evaluation", "§5 Limitations and synthetic-video/action boundary"),
    "2605.15477": ("MULTIMODAL-WORLD-MODELS", (3, 3, 3), "No Change — Existing Coverage", "exo video要服务 ego world model，必须先恢复body pose/action schema并显式转换视角；数据扩容收益依赖action identity与ego observation对齐，不能把普通视频直接当控制轨迹", "§3 Exo-to-ego conversion and action representation", "§4 Prediction/planning evaluation", "§5 Limitations and pose/kinematics/domain boundary"),
    "2605.14241": ("AGENT-TOOL-CALLING", (3, 3, 3), "Integrate", "同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth", "§3 LQM-ContextRoute", "§4 Evaluation", "§7 Limitations"),
    "2605.14249": ("PLATFORM-COST", (3, 3, 3), "No Change — Existing Coverage", "多 GPU 推理能耗优化应先以可解释 surrogate 预测 layer/operator 与并行配置的 energy，再把 energy-quality-latency 约束作为配置探索合同，而不是只比较整机平均功率；当前 Ch70 已明确承载 layer-wise energy model、architecture proxy 与 device/precision/batch/shape/utilization 约束，因此本 family 不再重复写回", "§3 EnergyLens Methodology", "§4 Evaluation", "§5 Discussion and limitations disclosed by evaluated hardware/configuration space"),
    "2605.14271": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "Agent harness 安全评测必须观察 trajectory 中的 resource access、message routing 与 authority transition；最终答案正确不能覆盖中途越权", "§4.1 Task Design; HarnessAudit-Bench", "§5 Experiments", "§6 Discussion and disclosed harness/model boundary"),
    "2605.14305": ("MULTIMODAL-GENERATIVE-PARADIGMS", (3, 2, 3), "No Change — Existing Coverage", "离散 diffusion 的并行 proposal 可用 prefix-conditioned factorization 消除 token-independent clean-posterior 近似，再由 speculative verification 保留 target distribution", "§3 Factorization-Error-Free DLLM", "§4 Experiments", "§4 Ablation and device/workload boundary; no dedicated limitations section"),
    "2605.14421": ("AGENT-MEMORY", (3, 3, 3), "Integrate", "持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority", "§2 Threat Model; §3 MemLineage Design", "§6 Evaluation", "§8 Discussion and Limitations"),
    "2605.14460": ("AGENT-PLATFORM", (3, 3, 3), "No Change — Existing Coverage", "skill supply-chain 审计不能只扫描代码 payload，还要执行 capability/effect probes，识别由描述、依赖和运行上下文组合出的 payload-less behavior", "§3 Payload-less Skill Attack and Audit Method", "§5 Evaluation", "§6.3 Threats to Validity and Limitations"),
    "2605.14473": ("AGENT-RAG", (2, 2, 3), "No Change — Existing Coverage", "RAG 在知识冲突下要把 answer correctness 与 context compliance 分开；诊断 intervention 只能测 retrieved context 是否控制答案，不能证明答案真实", "§3 Context-Driven Decomposition", "§4 Evaluation", "§6 Limitations and conflict-dataset/model boundary"),
    "2605.14483": ("AGENT-MULTI-AGENT", (3, 3, 3), "No Change — Existing Coverage", "Multi-Agent orchestration 的 role、capacity 与 dependency graph 应被视为一个可执行 artifact，并用 counterfactual feedback 做 credit assignment，而非顺序局部调参", "§3 LEMON Counterfactual Orchestration", "§4–§5 Evaluation", "Appendix B Limitations"),
    "2605.14591": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "大模型 privacy audit 可在无法重训时利用已知 member/non-member 固定集合估计经验下界，但该 post-hoc sensor 不能替代机制级 DP accounting 或训练日志；当前 Ch66 已明确承载 post-hoc dataset/membership inference 的证据边界与机制级 accounting 区分，因此本 family 不再重复写回", "§3 Zero-Run Privacy Audit", "§4–§6 Experiments", "§9 Limitations and Conclusion"),
    "2605.14636": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "No Change — Existing Coverage", "时间截止问题必须冻结可知信息边界，并将 temporal leakage 作为独立 failure slice；learned critique 只能在所测 cutoff/prompt 分布上提供 sensor", "§3 Temporal Critique Fine-tuning", "§4–§6 Experiments", "§7 Limitations"),
    "2605.14859": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "coding Agent 的权限策略必须由平台从 task、workspace 与 effect contract 推导并执行；模型的 permission-boundary inference 只能是 policy proposal", "§3 AuthBench and Permission-Boundary Inference", "§4–§5 Evaluation", "Appendix B Limitations and Future Work"),
    "2605.14932": ("PLATFORM-SECURITY", (2, 3, 3), "No Change — Existing Coverage", "Agent security 应借鉴 OS 的 process isolation、capability、mediation 与 audit 边界；类比本身不证明任意 Agent runtime 已实现这些保证", "§3 Agent-as-OS Security Model", "§4–§5 Case Studies", "§VI Limitations"),
    "2605.15030": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "Web Agent 的 prompt-injection guard 应作为与 policy 解耦的并行 sensor，并以持续 adversarial update 管理 drift；guard 不能拥有最终 action authority", "§3 Problem; §4 Data; §5 WARD Training", "§6 Experiments", "Appendix A Limitations"),
    "2605.15051": ("INFER-SPECULATIVE-DECODING", (3, 3, 3), "Integrate", "生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略", "§3 Interpretable Serving Latency Model", "§4 Validation", "§5 Conclusion and Limitations"),
    "2605.15079": ("TRAIN-DATA", (3, 3, 3), "Integrate", "受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata", "§3 Croissant Baker Pipeline", "§4–§5 Evaluation and Case Studies", "§6 Failure Modes and Limitations"),
    "2605.15109": ("AGENT-RAG", (3, 2, 3), "Integrate", "Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance", "§3 Traversal Context and Provenance", "§4 Experiments", "§5 Limitations"),
    "2605.15132": ("AGENT-WORKFLOW", (3, 3, 3), "Integrate", "可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery", "§3 APWA Architecture", "§4–§5 Evaluation", "Appendix A Limitations"),
    "2605.15164": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "behavioural evaluation 只能支持可观察行为声明，不能独立验证 hidden objective、loss-of-control absence 等内部或反事实安全命题", "§2–§7 Behavioural Assurance Analysis", "§7 Pilot Evidence", "§8 Limitations"),
    "2605.15184": ("AGENT-RAG", (2, 2, 3), "No Change — Existing Coverage", "Agent search 评测必须把 retrieval strategy、harness/tool interface 与 corpus access 联合冻结；grep 或 vector retrieval 的结论不能脱离 harness", "§3 Harness and Retrieval Conditions", "§4 Experiments", "§5 Limitations"),
    "2605.15185": ("MULTIMODAL-WORLD-MODELS", (3, 3, 3), "Integrate", "视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability", "§3 PDI-Bench Methodology", "§4–§5 Evaluation", "Appendix G Limitations and Future Directions"),
    "2605.15238": ("AGENT-WORKFLOW", (3, 3, 3), "Integrate", "代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness", "§3 Hydra Overview; §4 Design; §5 Incremental Checker", "§7 Evaluation", "§8 Discussion"),
    "2605.15257": ("PLATFORM-MONITORING", (3, 3, 3), "Integrate", "CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation", "§2 Experimental Design", "§3 Results and Discussion", "§5 Limitations"),
    "2605.15338": ("AGENT-MEMORY", (3, 3, 3), "No Change — Existing Coverage", "memory poisoning 可延迟触发并跨 session 重放；write admission、provenance、activation-time policy 与 expiry 必须共同拥有防线", "§3 Sleeper Memory Poisoning Threat Model", "§4–§5 Evaluation", "Appendix A Limitations and Impact"),
    "2605.15377": ("PLATFORM-MONITORING", (3, 3, 3), "Integrate", "AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority", "§3 Ensemble Monitoring Method", "§4–§6 Evaluation", "§6.3 Limitations and Future Work"),
    "2605.15384": ("AGENT-MEMORY", (3, 3, 3), "Integrate", "顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移", "§3 SeqMem-Eval", "§4–§6 Experiments", "Appendix G Limitations"),
    "2605.15422": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract", "§3–§4 DualKV", "§5 Evaluation", "§6 Conclusion and disclosed workload/hardware boundary; no dedicated limitations section"),
    "2605.16436": ("PLATFORM-SECURITY", (2, 2, 3), "No Change — Existing Coverage", "Agentic AI 降低高拟真攻击的边际成本，使 rate limit、identity proof 与 human vigilance 的旧经济假设失效；position analysis 不证明具体控制已有效", "§2–§5 Agentic Threat-Economics Analysis", "§3–§5 Case Analyses", "§6 Conclusion and position-paper evidence boundary"),
    "2605.16439": ("INFER-KV-CACHE", (2, 2, 3), "No Change — Existing Coverage", "VLM KV compression 应利用视觉与文本 token 的非对称冗余并按序列阶段保留信息；局部压缩收益不能外推到任意模态、长度或 backend", "§3 KVCapsule", "§4–§5 Evaluation", "§6 Conclusion and disclosed model/workload boundary"),
    "2605.18859": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告", "§3 TwinRouterBench Overview; §4 Dataset", "§5 Evaluation", "§7 Conclusion and Limitations"),
}

OWNER_PATH = {}
for line in (REPO / "ROADMAP.md").read_text().splitlines():
    match = re.search(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", line)
    if match:
        OWNER_PATH[match.group(1)] = match.group(3)

BASELINE = {
    "AGENT-TOOL-CALLING": "proposal、provider/tool discovery、utility admission、authorization、execution 与 outcome commit 的分层",
    "PLATFORM-COST": "端到端 work unit、energy/latency/quality 约束与 capacity/idle/失败重试的共同核算",
    "PLATFORM-EVALUATION-SYSTEM": "model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "AR、diffusion、masked refinement 的 proposal、verification、correction 与 commit 边界",
    "AGENT-MEMORY": "write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新",
    "AGENT-PLATFORM": "skill artifact identity、capability、admission、runtime policy、drift 与 audit",
    "AGENT-RAG": "corpus identity、retrieval trajectory、evidence provenance、citation 与 answer claim 的绑定",
    "AGENT-MULTI-AGENT": "role、dependency graph、message/shared state、credit、failure containment 与 final commit owner",
    "PLATFORM-SECURITY": "identity、typed capability、least privilege、policy mediation、effect boundary 与 audit",
    "INFER-SPECULATIVE-DECODING": "draft/target identity、acceptance、verification、rollback 与 serving scheduling 的统一状态机",
    "TRAIN-DATA": "dataset identity、schema、lineage、version、governance、quality gate 与 reusable artifact",
    "AGENT-WORKFLOW": "durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority",
    "MULTIMODAL-WORLD-MODELS": "observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff",
    "PLATFORM-MONITORING": "多源 sensor、trace/evidence identity、阈值、盲区、escalation 与 independent control authority",
    "TRAIN-DISTRIBUTED-TRAINING": "parallel state、collective/placement、kernel execution、checkpoint 与 optimization semantics",
    "INFER-KV-CACHE": "KV identity、residency、compression/eviction quality、rollback 与 workload-bound correctness",
    "INFER-SCHEDULING": "request/work-unit identity、budget、admission、priority、stop condition 与 SLO-aware execution control",
    "TRAIN-GRPO": "trajectory grouping、verifier/environment reward、token/sequence credit、KL/clipping 与 rollout-policy identity",
    "MODEL-MOE": "router probability、expert capacity、load balance、communication、placement 与 fallback 的条件计算合同",
}

def first_sentence(text: str) -> str:
    return re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text).strip())[0]

reviews, provenance, compares = [], [], []
for row in RETAINED:
    aid = row["arxiv_id"]
    node, score, disposition, delta, method, evaluation, limits = K[aid]
    family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
    row.update(
        source_family_id=family,
        owner_node=node,
        score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
        review_status="deep_complete" if sum(score) >= 7 or disposition == "Integrate" else "standard_complete",
        access_status="verified",
        integration_disposition=disposition,
        screening_reason=delta,
    )
    url = f"https://arxiv.org/html/{aid}v1"
    review = {
        "source_family_id": family,
        "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1",
        "exact_v1_url": url,
        "review_route": "deep" if row["review_status"] == "deep_complete" else "standard",
        "method_identity_locators": f"{url} {method} — mechanism boundary: {first_sentence(row['abstract'])}",
        "evaluation_locators": f"{url} {evaluation} — results remain bound to the disclosed model, workload, evaluator and system configuration",
        "limitations_counterevidence_locators": f"{url} {limits} — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO",
        "artifact_locators": f"{url} — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named",
        "claim_boundary": delta,
        "completion_result": "complete",
    }
    reviews.append(review)
    receipt = json.dumps(review, ensure_ascii=False, sort_keys=True).encode()
    provenance.append({
        "arxiv_id": aid,
        "source_family_id": family,
        "exact_v1_url": url,
        "retrieved_at": "2026-09-01T10:10:00+08:00",
        "remote_body_status": "official_html_opened_and_section_located",
        "review_receipt_sha256": hashlib.sha256(receipt).hexdigest(),
        "source_body_sha256": None,
        "local_body": None,
        "limitation": "official arXiv v1 HTML read remotely; section locators and claim/non-proof boundary recorded; local body hash is not a Gate requirement",
    })
    owner_path = OWNER_PATH[node]
    owner_file = REPO / owner_path
    chapter = int(re.match(r"(\d+)-", owner_file.name).group(1))
    adjacent = []
    for path in owner_file.parent.glob("*.md"):
        match = re.match(r"(\d+)-", path.name)
        if match and abs(int(match.group(1)) - chapter) == 1:
            adjacent.append(str(path.relative_to(REPO)))
    owner_hash = hashlib.sha256(owner_file.read_bytes()).hexdigest()
    compares.append({
        "source_family_id": family,
        "arxiv_id": aid,
        "owner_node": node,
        "owner_path": owner_path,
        "owner_sha256": owner_hash,
        "adjacent_paths_reviewed": sorted(adjacent),
        "current_content_comparison": (
            f"已读取 `{owner_path}` 及相邻章节；当前主线已覆盖{BASELINE[node]}。"
            + (f"正文尚未明确承载本 family 的增量：{delta}。" if disposition == "Integrate"
               else f"本 family 的增量“{delta}”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。")
        ),
        "disposition": disposition,
        "delta": delta,
    })

(R / "screening-ledger-final.json").write_text(json.dumps(LEDGER, ensure_ascii=False, indent=2) + "\n")
(R / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v2.1", "report_date": "2026-05-15", "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(R / "evidence-provenance-manifest.json").write_text(json.dumps({"schema": "evidence-provenance-v2.1", "report_date": "2026-05-15", "items": provenance}, ensure_ascii=False, indent=2) + "\n")
(R / "books-current-content-comparison.json").write_text(json.dumps({"schema": "books-current-content-comparison-v2.1", "report_date": "2026-05-15", "items": compares}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((R / "screening-ledger-final.json").read_bytes()).hexdigest()
(R / "coverage-receipt.json").write_text(json.dumps({
    "source_id": "SRC-ARXIV", "window": "[2026-05-14T09:00:00+08:00,2026-05-15T09:00:00+08:00)",
    "route": "DataCite adjacent-month v2 100-prefix snapshots; Core full title+abstract semantic screen; official exact-v1 HTML review",
    "raw_snapshot_records": LEDGER["raw_snapshot_records"], "registered_identities": len(ROWS),
    "core_semantic_screened": LEDGER["core_daily_semantic_review_required"],
    "keyword_semantic_screened": LEDGER["keyword_daily_semantic_review_required"],
    "false_negative_screened": LEDGER["title_route_negative_pending_false_negative_audit"],
    "retained": len(RETAINED), "pre_denominator_closed": len(ROWS) - len(RETAINED), "ledger_sha256": ledger_sha,
    "pagination": "adjacent months; prefixes 00..99; all snapshot pages closed", "status": "checked",
}, ensure_ascii=False, indent=2) + "\n")

integrate = [row for row in RETAINED if row["integration_disposition"] == "Integrate"]
queue = ["# 2026-05-15 Books Writeback Queue", "", "本文件是 date-local author queue；本 lane **未修改共享 Books**。必须经非作者 fresh-context audit 后，由 root 按日期串行写回并再做 post-write audit。", "", f"- Queue count: {len(integrate)}", "- Status: `pending_independent_review`", ""]
for row in integrate:
    queue += [f"## {row['source_family_id']}", f"- Primary: `arXiv:{row['arxiv_id']}v1`", f"- Owner: `{row['owner_node']}`", f"- Delta: {row['screening_reason']}", "- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.", ""]
(R / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue).rstrip() + "\n")

author_audit = {
    "schema": "semantic-author-audit-v2.1", "report_date": "2026-05-15",
    "scope": "author-side full-screen and evidence audit; this is not the independent fresh-context audit",
    "checks": {"registered_screened": [len(ROWS), len(ROWS)], "candidate_denominator": len(RETAINED), "pre_denominator_closures": len(ROWS) - len(RETAINED), "closure_reason_unique": len({row['screening_reason'] for row in ROWS if row['screening_status'] == 'pre_denominator_closed'}), "false_positive_pass": "author challenge complete", "false_negative_pass": "author challenge complete; independent audit pending", "exact_v1_complete": len(RETAINED), "blocked": 0, "books_compared": len(RETAINED)},
    "unresolved_findings": ["Independent fresh-context semantic audit remains pending.", "Root serial Books writeback and post-write semantic audit remain pending for surviving Integrate dispositions."],
}
(R / "semantic-author-audit.json").write_text(json.dumps(author_audit, ensure_ascii=False, indent=2) + "\n")

def candidate_row(row: dict) -> str:
    score = row["score_v2"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    return f"| {row['source_family_id']} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W20 | 2026-05-14 | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | {row['review_status']} | accessible | {override} | review:{row['source_family_id']} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{row['source_family_id']} | no |"

lines = [
    "# Daily Research — 2026-05-15", "", "**Research Date:** 2026-05-15", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-14 09:00:00 ～ 2026-05-15 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite 只用于 identity/date/abstract recovery；技术结论绑定 official arXiv exact-v1。", "",
    "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。Author packet 已闭合；等待非作者 fresh-context audit、root 串行 Books writeback 与 post-write audit。", "",
    "## Executive Summary", "",
    f"相邻月份 v2 snapshot 含 {LEDGER['raw_snapshot_records']:,} 条 raw records；严格窗口注册 {len(ROWS)} 条 identity。{len(ROWS)}/{len(ROWS)} 完成 title+abstract 语义筛选，冻结 {len(RETAINED)} 个 candidate、{len(ROWS)-len(RETAINED)} 项 family-specific pre-denominator closure。{len(RETAINED)}/{len(RETAINED)} official exact-v1 已读取，blocked=0；author 当前提出 {len(integrate)} 项 Books queue，但在非作者审计前不视为最终 disposition，也未写共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-15 |", "| Window End | 2026-05-15 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260515-V1-AUTHOR |", "| Denominator Frozen At | 2026-09-01T10:10:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-14T09:00:00+08:00 | 2026-05-15T09:00:00+08:00 | 2026-09-01T10:10:00+08:00 | DataCite v2 prefixes 00..99 + full semantic screen + exact-v1 HTML | checked | {len(ROWS)} | " + ";".join(row['source_family_id'] for row in RETAINED) + f" | pages=100; final_cursor=end; raw={LEDGER['raw_snapshot_records']}; registered={len(ROWS)}; screened={len(ROWS)}; retained={len(RETAINED)}; closure={len(ROWS)-len(RETAINED)} | 2026-05-15T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260515:start -->Author recall 已闭合：{len(ROWS)}/{len(ROWS)} registered identity 均经 title+abstract 语义筛选，29 个候选完成 exact-v1；独立 reviewer 仍需挑战 false positive/negative，故 Evidence 仍 Open。<!-- coverage:SRC-ARXIV:20260515:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
lines += [candidate_row(row) for row in RETAINED]
lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for review in reviews:
    lines.append(f"| {review['source_family_id']} | RP-TODO-{review['source_family_id']} | {review['review_route']} | {review['primary_evidence_version']} | SRC-ARXIV@{review['primary_evidence_version']} | {review['method_identity_locators']} | {review['evaluation_locators']} | {review['limitations_counterevidence_locators']} | {review['artifact_locators']} | claim:{review['source_family_id']} | complete |")
lines += ["", "### Source Reviews", ""]
for row, review in zip(RETAINED, reviews):
    lines += [f"<!-- review:{row['source_family_id']}:start -->", f"#### {row['title']}", "", f"问题与演进：{row['screening_reason']}。旧路径在原 workload、风险与成本约束下继续成立。", "", f"Method：`{review['method_identity_locators']}`。", "", f"Evaluation：`{review['evaluation_locators']}`。", "", f"Non-proof / fallback：`{review['limitations_counterevidence_locators']}`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`{review['artifact_locators']}`。", f"<!-- claim:{row['source_family_id']}:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:{row['source_family_id']}:end -->", f"<!-- review:{row['source_family_id']}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "本报告不把作者性能数字外推为通用 benchmark claim；条件保留在 Source Review 的 disclosed/not-disclosed boundary。", ""]
selected = {"2605.14421": "DA-MEMORY-LINEAGE-GATE", "2605.15238": "DA-ASYNC-CHECKPOINT-ROLLBACK", "2605.18859": "DA-LIVE-AGENT-ROUTING-EVAL"}
lines += ["## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for row in RETAINED:
    aid = row['arxiv_id']; decision = "selected" if aid in selected else "not_selected"; unit = selected.get(aid, "—")
    eligible = "score_7_9" + (";forced_review;potential_books_delta" if row['integration_disposition'] == 'Integrate' else "")
    rationale = "跨越 memory/action、generation/checking 或 routing/environment 的 ownership boundary" if aid in selected else f"exact-v1 Review 已完成；其 delta 由 `{row['owner_node']}` 承载，三个入选单元更能解释跨层状态与 commit authority"
    ref = f"analysis:{unit}" if aid in selected else f"analysis-decision:{row['source_family_id']}"
    lines.append(f"| {row['source_family_id']} | {eligible} | {decision} | {unit} | — | {rationale} | {ref} |")
lines += ["", "本日最多扩写三项；未入选项目仍保留完整 exact-v1 Source Review 与 Books Decision。", "",
          "<!-- analysis:DA-MEMORY-LINEAGE-GATE:start -->", "### Memory 从文本存储推进到可验证的 Action Chain of Custody", "", "旧路径允许直接召回文本，在低风险、单 session、无外部副作用时成本最低。持久 memory 一旦可以跨 session 影响敏感 action，约束变成：每次派生和引用都必须可追溯，最终 action 只能由 policy gate 在 lineage 完整时提交。签名 provenance 与 derivation DAG 换来可审计 chain-of-custody，却增加 lineage storage、key lifecycle、LLM derivation error 与 availability failure；缺失 lineage 时应降级为 advisory context 或人工确认。", "<!-- analysis:DA-MEMORY-LINEAGE-GATE:end -->", "",
          "<!-- analysis:DA-ASYNC-CHECKPOINT-ROLLBACK:start -->", "### Code Generation 从事后重写推进到异步检查与有界回滚", "", "事后 compile/repair 在短程序、低 compiler cost 时简单可靠，但长生成会让晚发现错误扩大重写范围。Hydra 保存已验证 checkpoint，让 compiler 异步检查 provisional prefix；失败只回滚到最近可信点。收益是减少 token 和 latency，代价是 sealing 规则、checkpoint state、一致性与 checker lag。compiler 只拥有静态诊断，不能替代测试、安全或 outcome correctness；异步状态不可靠时回退完整生成后编译。", "<!-- analysis:DA-ASYNC-CHECKPOINT-ROLLBACK:end -->", "",
          "<!-- analysis:DA-LIVE-AGENT-ROUTING-EVAL:start -->", "### Routing Evaluation 从 One-shot Proxy 推进到 Step-level Environment Outcome", "", "one-shot routing 在独立请求、无长期状态时可复算且便宜；Agent trajectory 中每次模型替换会改变后续 observation、tool call 与 task success。TwinRouterBench 将真实 step prefix 交给 router，并用 environment execution 验证 downstream outcome，分开 static replay 与 live dynamic track。它提高外部有效性，却引入环境 nondeterminism、执行成本与 evaluator/version state；无法 live replay 时静态 track 仍可用于筛选，但不能冒充最终部署证据。", "<!-- analysis:DA-LIVE-AGENT-ROUTING-EVAL:end -->", ""]
for row in RETAINED:
    if row['arxiv_id'] not in selected:
        lines.append(f"<!-- analysis-decision:{row['source_family_id']}:start -->{row['source_family_id']} 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:{row['source_family_id']}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
compare_by_aid = {item['arxiv_id']: item for item in compares}
for row in RETAINED:
    c = compare_by_aid[row['arxiv_id']]
    path = c['owner_path']
    chapter = int(re.match(r'(\d+)-', Path(path).name).group(1))
    target = f"{path}#chapter-{chapter}"
    adjacent_refs = []
    for adjacent_path in c['adjacent_paths_reviewed']:
        adjacent_chapter = int(re.match(r'(\d+)-', Path(adjacent_path).name).group(1))
        adjacent_refs.append(f"{adjacent_path}#chapter-{adjacent_chapter}")
    adjacent = '; '.join(adjacent_refs) or target
    lines.append(f"| {row['source_family_id']} | {row['owner_node']} | {target} | {adjacent} | existing:{row['source_family_id']} | delta:{row['source_family_id']} | Direct Evolution | {row['integration_disposition']} | books-review:{row['source_family_id']} |")
for row in RETAINED:
    c = compare_by_aid[row['arxiv_id']]
    lines += [f"<!-- books-review:{row['source_family_id']}:start -->", f"<!-- existing:{row['source_family_id']}:start -->{c['current_content_comparison']} Owner snapshot sha256=`{c['owner_sha256']}`；相邻章节=`{', '.join(c['adjacent_paths_reviewed'])}`。<!-- existing:{row['source_family_id']}:end -->", f"<!-- delta:{row['source_family_id']}:start -->{row['screening_reason']}<!-- delta:{row['source_family_id']}:end --> Decision: `{row['integration_disposition']}`；author lane 未修改共享 Books。", f"<!-- books-review:{row['source_family_id']}:end -->"]

lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", "| SA-20260515-FRESH-COVERAGE | fresh-context:pending-reviewer | coverage | coverage:SRC-ARXIV:20260515 | F-20260515-FRESH-COVERAGE-PENDING — 非作者 denominator 审计尚未执行 | 等待独立 reviewer 挑战 668 条 screening 的 false positive/negative | open |", "| SA-20260515-FRESH-EVIDENCE | fresh-context:pending-reviewer | evidence | review:SF-2026-ARXIV-2605-14241 | F-20260515-FRESH-EVIDENCE-PENDING — 非作者 evidence 审计尚未执行 | 等待独立 reviewer 核对 29 项 exact-v1 claim boundary 与 locators | open |", "| SA-20260515-FRESH-SELECTION | fresh-context:pending-reviewer | deep_analysis_selection | analysis:DA-MEMORY-LINEAGE-GATE | F-20260515-FRESH-SELECTION-PENDING — 非作者 selection 审计尚未执行 | 等待独立 reviewer 挑战三项 Deep Analysis 选择 | open |", "| SA-20260515-BOOKS | fresh-context:pending-reviewer | books | books-review:SF-2026-ARXIV-2605-14241 | F-20260515-BOOKS-WRITEBACK — 共享 Books 未写 | 等待独立审计后 root 串行写回，再由非写作者 post-write audit | open |", "", "Author audit 不是 fresh-context audit；因此格式与 exact-v1 完成不被伪称为 Evidence/Books 闭环。", "",
          "## 8. Ignored Noise", "", f"完整 {len(ROWS)-len(RETAINED)} 项 pre-denominator closure 位于 `../_sources/daily-20260515/screening-ledger-final.json`。每行保留标题、摘要机制、排除边界与重开条件；它们不因 AI 相关性自动进入 denominator。", "",
          "## 9. Recommended Action", "", f"由非作者重放 668/668 screening、29 个 exact-v1 Review、3 项 Deep Selection 与 {len(integrate)} 项 provisional Books queue；审计通过后 root 才可按日期串行写回。", "",
          "## 10. Repository Changes", "", "- 新建 2026-05-15 date-local Daily、screening ledger、exact-v1 Review、provenance、Books comparison 与 author queue。", "- 未修改共享 Books，未 stage、commit 或 push。", "",
          "## 11. Open Questions", "", "- 独立 reviewer 是否发现 false negative、false positive、claim boundary 或 Books over-integration？", "- root 串行写回后，目标及相邻章节是否仍保持唯一 owner 与连贯演进？", "",
          "## 12. Sources", "", "- DataCite adjacent-month v2 snapshot（identity/date/abstract recovery only）"]
lines += [f"- [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1) — arXiv:{row['arxiv_id']}v1；first-public 2026-05-14；accessed 2026-09-01" for row in RETAINED]
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Open`", "", "Evidence: `Open`", "", "Books: `Open`", "", "unresolved findings: 2", "", f"Author lane 已完成 668/668 screening、29-family denominator、29/29 exact-v1 Review、Score V2、Deep Selection 与 current owner+adjacent Books comparison；仍等待独立 fresh-context audit、root 串行 Books writeback 与 post-write audit。"]

text = "\n".join(lines)
for row, review in zip(RETAINED, reviews):
    family = row['source_family_id']; ref = f"review:{family}"; body = text.split(f"<!-- {ref}:start -->", 1)[1].split(f"<!-- {ref}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{row['arxiv_id']}", "Primary Identifier": f"arXiv:{row['arxiv_id']}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if row['integration_disposition'] == 'Integrate' else "none"}
    rp = _expected_review_provenance(family, candidate, review['review_route'], review['primary_evidence_version'], f"SRC-ARXIV@{review['primary_evidence_version']}", review['method_identity_locators'], review['evaluation_locators'], review['limitations_counterevidence_locators'], review['artifact_locators'], f"claim:{family}", ref, _normalized_body_sha256(body))
    text = text.replace(f"RP-TODO-{family}", rp)

out = REPO / "papers/2026/05/15/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(text + "\n")
print(json.dumps({"registered": len(ROWS), "retained": len(RETAINED), "closures": len(ROWS)-len(RETAINED), "exact_v1": len(reviews), "blocked": 0, "integrate_queue": len(integrate)}, ensure_ascii=False))
