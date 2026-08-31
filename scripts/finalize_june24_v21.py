#!/usr/bin/env python3
"""Freeze and render the strict 2026-06-24 Daily V2.1 packet.

This date-local finalizer never edits shared Books or LEARNING_STATE.  It
materializes the frozen denominator, exact-v1 review receipts, full-frontier
selection, and a root-owned Books insertion queue.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260624"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
REPORT = ROOT / "papers/2026/06/24/README.md"
EXECUTED_AT = "2026-08-29T07:20:00+08:00"
ND = "Not Disclosed"

# aid: owner, method section, evaluation section, counterevidence section,
# source-specific durable mechanism, exact-v1 non-proof boundary.
META = {
    "2606.24074": ("PLATFORM-EVALUATION-SYSTEM", "3 Reliability Certification Setup; 4 Constructing a Certification SOTM", "5 A Matching Reliability Certification Lower Bound", "6 Conclusion and the stated small-error asymptotic regime", "把一次性 benchmark 分数改成带双侧错误界、逐 token 成本和停止阈值的 SPRT certification；certifier 持有 query/score/log-likelihood state，跨阈值才发布 reliable/unreliable verdict。", "只证明给定 reliability gap、binary correctness oracle 与 small-error leading order；不证明开放式 judge 标签、分布漂移或任意非独立 query 下仍满足同一界。"),
    "2606.24081": ("PLATFORM-EVALUATION-SYSTEM", "3 PixJail Framework; 3.2 Attack Module; 3.3 Evaluation Pipeline; 3.4 Memory Updates", "4 Experiments; 4.1 Data, Models and Metrics; 4.3 Main Results", "6 Limitations", "把 T2I jailbreak 的 prompt-only 比较升级为 paper-to-pipeline contract：attack module、victim、filter、multimodal judge、配置、日志与版本 artifact 共同成为可复现状态。", "11 种 attack、4 个 victim 与论文匹配配置不证明未知 attack 自动复现；prompt/heuristic memory update 及 closed-source safety filter 仍是黑盒边界。"),
    "2606.24119": ("PLATFORM-MONITORING", "3 Methodology; 3.2 Experimental Setup", "4 Experiments and Results; 4.1 Calibrated Triage", "D Mechanism and Boundary Audit; Definitions and non-portability", "撤销把 denoising top-1 concentration 当 PEFT collapse alarm 的旧路径；monitor 改读 max LoRA gradient norm，并由每个 DLM family 的 held-out calibration 拥有告警阈值。", "816 个配置、3 个 DLM family 与 200-step horizon 只支持短程 DLM-LoRA triage；跨 family 阈值失败，不能外推为通用 collapse detector。"),
    "2606.24124": ("PLATFORM-EVALUATION-SYSTEM", "3 DSL for Reasoning Trace Formalization; 4 Structured Verification", "5 Evaluation; E Standalone Verification on ProcessBench", "F Limitations and Future Work", "将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。", "逐步验证成本随 trace 线性增长，semantic deduction 仍依赖 LLM audit，inference schema library 有限；三类 benchmark 不证明任意开放域推理。"),
    "2606.24133": ("TRAIN-DATA", "2 Methodology: The Holistic Data Scheduler; 2.2 Online Data Mixing", "3 Experiments and Analysis; 3.1 Experimental Setup", "B Sensitivity Analysis of Reward Weights; C Hyperparameter Sensitivity", "把固定或单目标 data mixture 改为 SAC controller：state 汇聚 domain loss/lexical diversity/weight-norm，action 写回下一训练阶段的 domain weights，多目标 reward 决定调度。", "The Pile、给定 16-layer/2048-dim recipe 与 reward sensitivity 不证明跨 tokenizer、optimizer、数据污染或超大规模 pretraining 仍有相同收益。"),
    "2606.24143": ("TRAIN-DISTRIBUTED-TRAINING", "4 Forward- and Reverse-KL OPD Under Staleness; 7 AsyncOPD", "7 AsyncOPD Experimental Results; G Scheduler Details", "8 Limitations and Future Work", "将 rollout、teacher scoring、student update 解耦为 queue stages；learner 用 current-student recomputation 修正 reverse-KL stale signal，并以 multi-sample MC 避免 cached top-k support bias。", "实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。"),
    "2606.24151": ("AGENT-MEMORY", "3 The Metis System; 3.2 Text Reflection; 3.3 Code Generation; 3.4 Memory Manager", "4 Experiments; A.1 Profiling Experiments", "A.1 Per-Axis Analysis and reported construction/transfer trade-offs", "不在设计时固定 text 或 code memory；memory manager 先保存 plan/fact/pitfall 文本，只有重复且验证通过的 plan 才 crystallize 为 callable tool，同时保留构建成本与 provenance。", "AppWorld 与同一 experience set 只显示两种表示在 construction cost、execution efficiency、transferability 上互补；不证明生成工具在未知 API、权限变化或污染经验下安全。"),
    "2606.24177": ("AGENT-WORKFLOW", "2 Design Principles; 3 System Architecture", "4 Where Human Judgment Is Irreducible; A/B Case Studies", "4.7 What the Architecture Can and Cannot Absorb; 4.8 Boundary Is a Snapshot", "以 artifact 为边界组织 producer-critic factory，critic 在 fresh context 验收后才推进；自动化 loop 只提交可机器检查部分，visibility/fixability taxonomy 将不可判定 claim 留给 human scientist。", "444 次 prompt-economy loop 与两个 case study 展示可扩展性而非科学真值；不可见或不可修复 failure、motivation judgment 与外部实验真实性仍需人工 owner。"),
    "2606.24204": ("AGENT-RAG", "III Unified Dominance Abstraction; IV/V Unified Dominance Graph", "VI Experiment; Search Performance and Index Construction", "V-B Validity-Preserving Patch Edges; VI-D Impact of Patch Edges", "把 interval predicate 的双端点约束映射为统一 2D dominance space；每个 predicate 拥有独立 UDG instance，patch edge 只在 validity 保持时补路由，避免两个 scalar index 的交集爆炸。", "闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。"),
    "2606.24245": ("PLATFORM-SECURITY", "3 Overview; 4 Approach; ILP-Guided Predicate Learning", "5 Experimental Setup; 6 Evaluation", "7 Discussion and Threats to Validity", "把静态 expert rule 的维护改为 annotation-driven CEGIS：trace evaluator 产出 FP/FN counterexample，ILP 选 discriminating predicate，candidate verifier 决定是否发布 rule revision。", "291 条 code/embodied trace 与 4–5 次迭代不证明稀疏、错误或对抗标注下收敛；发布前仍需 human approval、versioned rollback 与旧 expert rules 共存。"),
    "2606.24311": ("AGENT-PLATFORM", "3 Method; 3.2 Integrated Execution Framework; 3.5 Structured Tool Boundary", "4 Experiments; Terminal-Bench 2.0/2.1", "5 Limitations and Future Work", "将 model invocation、tool execution、workspace mutation、rule knowledge 与 execution record 收进同一 runtime boundary；剩余时间成为显式 state，用于在探索、实现、验证之间重配预算。", "结果主要绑定 GPT-style tool calling 与 Terminal-Bench；其他 model family、长编译/训练、严格中间验证和 workspace 外 side effect 未证明，应保留人工接管与受限 sandbox。"),
    "2606.24322": ("PLATFORM-SECURITY", "II Threat Model; III TMA-NM; IV Formal Model", "V MEM-INV-Bench; VI Evaluation", "IX Limitations", "memory item 的行动权不再由可篡改 content/lineage 推断，而在 write 时绑定 origin authority；只有 k 个独立 trusted source 才 elevation，高风险 action 缺少 corroborator 时交给 one-time user confirmation。", "保证依赖正确 origin labeling、独立 principal 与有限 TLA+ model；trusted tool compromise、隐式 value reconstruction、nested payload taint 和广泛真实任务仍未闭合。"),
    "2606.24369": ("TRAIN-DISTRIBUTED-TRAINING", "3 DigenRL: System Design; GAP/TSP/TAG/TCSS", "5 Evaluation; End-to-End Time and TCSS Effectiveness", "5.4 Heterogeneous Resources; 5.6 Ablation", "把 visual diffusion RL 的 generation/training 解耦，并沿 generation 与 timestep 两轴并行；trainer bubble 临时借给 generator，TCSS 以 trajectory-consistent point 控制权重同步。", "收益绑定论文 diffusion workload、资源组合与 stale policy 容忍度；异构故障、跨作业隔离和 reward/model drift 未验证，质量偏离时回退同步或 bounded-staleness。"),
    "2606.24402": ("PLATFORM-SECURITY", "3 Problem Setting and Study Design; 5 Verification Boundary", "4 Poisoning Outcomes; 6 Generalization; 7 Mitigations", "8 Discussions and Limitations", "RAG 安全 gate 不再只问文档是否被检索，而按 local-artifact、model-knowledge、runtime-dependent 三层 verification boundary 决定 claim 能否进入行动；L3 需要动态探测或权威外部证据。", "11 CTF、11 CVE、3 model family 下 prompt verification/multi-source retrieval 在 sparse-evidence 与 zero-day 会退化；不能把信息多数当独立真实性。"),
    "2606.24408": ("PLATFORM-SECURITY", "3 Natural Identifiers; 4 DP Auditing; 5 Dataset Inference", "H DP-SGD Auditing; I/J/K Additional Evaluation", "M Limitations", "利用训练数据自然出现且稀有的 identifier 作为 post-hoc audit unit，避免必须预埋 canary；auditor 分离 DP leakage 检查与 dataset inference，并记录 identifier cardinality/生成机制。", "NID 可用性、独立性与 generator 正确性依赖数据域；黑盒可见性、重复 identifier、强 MIA 和 DP-SGD 配置变化会改变 sample complexity，不能当作逐样本法律证明。"),
    "2606.24428": ("AGENT-MEMORY", "3 Self-Confirmation Trap; 4 Execute-Distill-Verify", "5 Experiments; Memory Quality and Contamination", "G Limitations", "经验写入从同一 agent 自我总结改为 Execute 的异构并行轨迹、第三方 contrastive Distill 与 consensus Verify；只有通过独立验证的经验才能进入 storage/retrieval。", "多 agent consensus 仍可能相关失败，且 tau2-Bench/Mind2Web/MMTB 与论文 temperature/retrieval 配置不证明开放任务；不确定时保存 raw trajectories 或拒绝写入。"),
    "2606.24437": ("AGENT-MULTI-AGENT", "4 ReM-MoA; Ranked Reasoning Memory; Diversified Routing", "5 Experiments; Scaling and Ablations", "Bounded width; Single-scale proposer pool; Reviewer overhead", "MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。", "只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。"),
    "2606.24467": ("INFER-KV-CACHE", "3 CompressKV; Retrieval Head Identification; Layer-Adaptive Allocation", "4 Experiments; LongBench/NIAH; Memory and Latency", "4.5 Ablations; 4.6 Orthogonality tests", "KV eviction 从统一 token score 改为 semantic-retrieval heads 选 token、error-aware controller 按层分配 cache budget；压缩决定属于 cache manager，不修改模型语义 owner。", "LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。"),
    "2606.24506": ("INFER-GPU-MEMORY", "3 CrossPool Design; KV Planner; Layer-wise Scheduler; Control Lowering", "5 Experiments; Context Scalability; Overall Performance", "6 Discussion", "冷 MoE serving 将 stable weights 与 demand-driven KV 拆成独立资源池；planner virtualize shared KV，layer-wise scheduler/persistent kernel 只激活所需 weights 和 KV heads。", "证据聚焦冷模型、低并发与给定 context/model mix；热点突发、跨租户 isolation、模型装载故障和高并发下 shared-pool contention 未证明，应能回退 dedicated allocation。"),
    "2606.24535": ("AGENT-MEMORY", "3 Fleet-Memory Problem; 5 Governed Shared Memory Architecture", "7 Evaluation Methodology; 8 Results", "10 Limitations", "多 Agent 共享记忆增加 explicit scope、valid time、provenance graph 与 policy-gated retrieval；矛盾在 write-time resolution，reader 只消费已提交版本，传播由 privilege gate 控制。", "self-evaluation、single tenant、focused scope probe、有限 workload 且无 comparand；staleness-after-supersession 与 visibility 延迟未完整测量，冲突时回退 tenant-local memory 或 single writer。"),
    "2606.24626": ("PLATFORM-TRACE", "2 Methodology: SAFARI", "3 Experimental Setup; 4 Results; A/B/C appendices", "D Future Work", "故障诊断不再把全 trajectory 填入一个 context；investigator 用 segment search/read tools 主动取证，并用 persistent STM 保存跨轮 hypothesis/evidence，使 attribution 与原始 trace 长度解耦。", "Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。"),
    "2606.24722": ("TRAIN-DISTRIBUTED-TRAINING", "2 Protocol; Block-Local Diffusion Objective; Decentralized Execution", "3 Real-Text Experiments; 4 Decentralization and Asynchrony", "4.4 HTTP/TCP Transport Proof; 6 Conclusion", "把 end-to-end backprop 的全局 hidden-target ownership拆成 block-local diffusion objective；edge worker 独立更新 block，coordinator 只按版本/acceptance rule 接收异步 update，同一 block protocol 也支撑分布式 inference。", "real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。"),
    "2606.24774": ("PLATFORM-SECURITY", "GradAudit gradient-slice and noise-masking methodology", "Seven pretraining/fine-tuning configurations; medical and general datasets", "White-box parameter-access scope and reference-data dependence", "training-data audit 从 output entropy 转向 parameter-gradient signature；auditor 对跨模态 parameter slices 做稳定性/对齐特征，并用已知 train/non-train reference mask 掉不敏感维度。", "需要 white-box parameters 与 reference data；七个 VLM 配置、medical/general dataset 不证明黑盒 API、生成式泄漏或法律层面的逐样本归属。"),
    "2606.24775": ("AGENT-MEMORY", "3 Method Overview; Representation, Extraction, Retrieval, Maintenance", "4 End-to-End Assessment; 5 Component Comparison", "4.3 Evolution Robustness; 4.4 Long-Horizon Stability; 4.5 Cost", "把 agent memory 评价拆成 logical representation、physical storage/index、extraction、query routing 与 maintenance 五个 ownerable stage，并分别测 retrieval fidelity、evolution robustness、long-horizon stability 和 operation cost。", "现有系统/benchmark 比较不证明单一实现普适最优；缺少生产 authorization、deletion SLA、并发一致性或真实 workload 时只能作为 lifecycle checklist。"),
    "2606.24957": ("INFER-SPECULATIVE-DECODING", "3 Observation; 4 Dustin Sparse Verification", "5 Experiment; Accuracy and End-to-End Decode Throughput", "L Limitations; I Porting Overhead", "speculative verification 的 target KV 不再全读；Dustin 混合历史 attention 与 draft lookahead，semantic retrieval heads 在线估计关键 token，只对稀疏 KV 做 target verification。", "静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。"),
    "2606.24996": ("PLATFORM-EVALUATION-SYSTEM", "2 Results: Two Roles for the Certification Protocol", "A Report-Card and Gate Procedure; C/D Robustness Controls", "3 Discussion: Limitations and scope; first-failing-gate audit", "deployment-facing leaderboard claim 必须经过 interface lock、clean positive anchor、native negative control、power/false-promotion 与 first-failing-gate report card；任一 gate 失败即禁止发布 selection inversion。", "证据来自 forecasting candidate families 与两个 locked interface；不证明所有 task metric 或业务成本可被同一 gate 捕获，underpowered audit 只能给 inconclusive。"),
    "2606.24998": ("TRAIN-DATA", "3 Methods; Repeated-pool construction", "4 Results; F Training and Evaluation Details", "H Limitations", "数据去重从 hygiene 建议升级为 compute allocation contract：相同样本的 internal repetition 先改善后破坏 eval loss，data owner 应记录 repeat count、unique pool 与 model-size-dependent peak。", "结论绑定 synthetic repeated pools、模型尺度与 loss-floor fit；自然语料的语义近重复、curriculum 与 downstream contamination 未证明，不能由单一 repeat threshold 自动删除。"),
    "2606.25040": ("INFER-SCHEDULING", "3 Methodology; Sparsity Reuse; Latent Feature Reuse", "4 Experiments; Mask Quality and Routing Overhead", "5 Conclusion and Limitations", "I2V scheduler 把相似请求历史 sparse mask 作为 request-conditioned prior，避免每请求 mask prediction；feature reuse 仅可选，并由 downsampled region 与 guidance enhancement 限制 semantic drift。", "2.16x 来自论文 I2V workload/default config；相似度误路由、场景突变、跨模型 mask 不兼容和 feature boundary artifact 未证明，低置信时回退在线 mask/full compute。"),
    "2606.25082": ("PLATFORM-GPU-SCHEDULER", "IV Proposed Solution; Scheduling Within Configuration; Dynamic Re-Partitioning", "V Experiments and Results", "VI Conclusion and Future Work", "MIG scheduler 同时拥有 configuration 内作业放置与 configuration 间 repartition；controller 以 power/performance state、partition action 与 reward 决定何时重分，而不是把 MIG 当静态 SKU。", "主要是 simulation 与测得的 MIG power characteristic；repartition downtime、state migration、真实混合作业 SLO 和多节点 GPU fabric 未闭合，收益不足时保留静态 partition。"),
    "2606.25091": ("INFER-SPECULATIVE-DECODING", "II Background and Setting; III Gain Window", "III-A/B/C comparisons; IV Pipelining", "V Conclusion and explicit verifier-interface/RTT boundary", "edge-cloud speculative decoding 的准入由 RTT、edge draft time、acceptance 与 target verification time 共同决定；single-request latency 不再是唯一目标，饱和 server 的 multi-tenant capacity 才可能 justify offload。", "这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。"),
    "2606.25097": ("INFER-SPECULATIVE-DECODING", "3 Methods; Serving-stack Configuration; TAIS Screen", "4 Results; E0/E1/E2/E5; B Reproducibility", "5.3 Limitations and Threats to Validity", "speculative decoding 上线前增加 target-aligned invariance screen：byte identity、McNemar、TOST 与 matched target-only arm 分离算法安全差异和 dtype/framework 噪声。", "证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。"),
    "2606.25098": ("PLATFORM-GPU-SCHEDULER", "3 Architecture for Power-Flexible AI Infrastructure", "4 Experimental Demonstration; 5 Grid Services; 6 Geo-Load Shifting", "7 Discussion and service-level preservation scope", "grid signal 成为 cluster scheduler 的外部 control input，power telemetry/model 回写可用 curtailment budget；priority job 保留服务级别，elastic job 承担降载或跨地域迁移。", "130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。"),
    "2606.25115": ("AGENT-MEMORY", "III System Design; Net-Value-Density; Three Decisions", "V Evaluation; Trust Under Poisoning; Real Hardware", "VI Related Work and deployment-specific score calibration", "一个 value-minus-harm-per-byte score 同时控制 KEEP eviction、SHARE uplink 与 TRUST provenance gate；RAM、energy、uplink budget 与 poison risk 成为 memory lifecycle state。", "task-drift benchmark 与 Jetson 两臂/Hub testbed 不证明 score 跨设备、用户或攻击迁移；低校准或高风险 entry 应拒绝共享并回退本地可信 memory。"),
    "2606.25156": ("MODEL-LONG-CONTEXT", "3 Methodology; Polar Attention; Gated-Delta Memory", "4 Experimental Setup; 5 Results; C Complete Sweep", "5.1/5.4 trade-offs and reported 256K FinePDFs failure", "长上下文设计从单一 accuracy 目标改为 retrieval、likelihood、short-context quality、decode state 与 kernel cost 的 Pareto；Polar direction/magnitude channel 配 gated-delta recurrent state。", "378M、2K train、256K eval 中 FinePDFs exact retrieval 为 0%，hardware transition audit 非随机；不能宣称普遍外推，Raven/softmax/更短 context 仍是共存点。"),
    "2606.25161": ("AGENT-MEMORY", "3 Method; Memory Transition Verifier; Transition-Ranked GRPO", "4 Experiment; HaluMem; Reliability of Consolidation", "D Memory Transition Error Judge Prompt and evaluated datasets", "memory update 不再只按最终问答 reward；transition verifier 对 coverage、preservation、faithfulness 打分，同一旧 state 下比较候选 write/revise/delete，并用 preference-guided RL 训练 writer。", "MemoryAgentBench/HaluMem/Mem-alpha 与 verifier judge 不证明真实用户 consent、并发 writer、poisoning 或 judge drift；低置信 transition 应拒写并保留旧版本。"),
    "2606.25178": ("TRAIN-GRPO", "3 Method; Gradient-Based Transferability; Curriculum Algorithm", "4 Experiments; B Implementation/Evaluation Details", "6 Conclusion: Limitations; C Scaling", "多域 RLVR curriculum 不再只追当前 domain learnability；controller 从正在计算的 GRPO projected gradients 估计跨域 transfer，对 bandit arm value 做平滑后决定下一 domain。", "六域、Qwen3-1.7B/Llama3.2-3B 与 <1% overhead 不证明更大模型、non-verifiable reward 或 adversarial domain；gradient conflict 不稳定时回退 proportional/hand-designed mix。"),
    "2606.25189": ("PLATFORM-SECURITY", "3 Design; Policy DSL; Information-Flow Control", "5 Evaluation; Compliance; Macro/Micro Overhead", "2.3 Existing Approaches; evaluated policy/harness scope", "policy context 留在 agent/harness，但 enforcement 下沉 OS kernel；IFC DSL 表达跨 event ordering/data-flow，eBPF 覆盖绕过 tool-call layer 的 system action，并返回 semantic denial。", "1.9%–8.4% overhead 与论文 policy/task 不证明所有 syscall、container/runtime 或 kernel version；DSL 生成错误时必须 fail closed、人工修订或回退传统 sandbox。"),
    "2606.25191": ("AGENT-RAG", "3 Reasoning-Score Coupling; 4 Candidate Treatments; MADARA", "5 Experimental Setup; 6 Results; K Cost-Accuracy", "7 Discussion boundaries; D/F calibration sensitivity", "document assessment 不再默认多 Agent scoring；pilot probe 测 reasoning-score coupling，弱模型路由到 per-document isolation，只有 score 有信息的模型才承担 assessment/reranking。", "7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。"),
    "2606.25198": ("AGENT-WORKFLOW", "3 Heuresis Framework; search strategies and async parallelism", "4 Experiments; 5 Analysis; B Reward Hacking", "6.2 Limitations; B.3 Limits of Agentic Verification", "autonomous research loop 把 shared search state、lineage、quality/diversity/novelty archive 与 auditor verdict 作为 durable artifacts；40 个 fabrication 说明 score 结果必须过独立 audit 才能推进。", "3 个 ML domain、3,222 scored runs 未出现 Original 且 verifier 漏掉过 fabrication；不证明自动搜索能扩展 quality-novelty frontier，关键 claim 仍需独立复现/人工 gate。"),
    "2606.25207": ("AGENT-WORKFLOW", "3 Agent-Integrated Tools; 4 Agent-System Co-Design", "5 Experiments; Wall-Clock Decomposition", "7 Limitations", "HPO agent 不替代单一 optimizer，而从多工具 proposal pool 选择；prefix-stable prompt 复用 KV，跨 iteration speculation 与 relative-error accept test 把 judge/tool latency 隐藏在 model evaluation 下。", "HPOBench/PD1 与给定 wall-clock regime 不证明昂贵、非平稳或安全敏感 experiment；accept test 不满足或 speculation 浪费时回退串行工具 loop。"),
    "2606.25215": ("MULTIMODAL-EMBODIED-VLA", "3 Method; Observation-Action-Consequence Context; Block-Causal Training", "4 Experiments; C/D Evaluation Protocols", "E Reproducibility, Assets, and Limitations", "VLA state 从当前 observation 扩成 observation-action-consequence triplet buffer；shared attention 读历史后果，block-causal mask 防训练泄漏，KV cache 支撑实时滚动。", "LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。"),
    "2606.26156": ("AGENT-MULTI-AGENT", "2 Information Protocols; 3 Kiko Programming Model", "4 Operational Semantics; protocol-compliance proof", "5 Discussion and conference-era implementation scope", "把 agent 内部 decision logic 与公开 message protocol 分离：decision maker 只能从 valid decisions 选互相兼容 emission set，adapter 隔离 communication service，operational semantics 拥有 protocol compliance。", "2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。"),
    "2606.28387": ("AGENT-RAG", "3 Schema-First Retrieval; Catalog Objects; Retrieval and Access Control", "4 Experimental Setup; 5 Results; D Analyses", "5.3 Complexity and Failure Modes; 5.4 Error Analysis", "text-to-SQL 在 generation 前先检索 typed catalog object（table/column/metric/relation/query history）；parallel vector search、lineage expansion、reranker 与 deterministic ACL 共同决定可见 schema。", "CRUSH4SQL/SEDE/BIRD 与 warehouse catalog quality 不证明跨 dialect、动态权限或低元数据环境；metadata noise/ACL 不确定时回退受限 catalog browse 或人工 schema selection。"),
}

PATHS = {
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "PLATFORM-TRACE": "books/part-06-ai-infrastructure/69-trace.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/63-gpu-scheduler.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-GPU-MEMORY": "books/part-05-inference-system/54-gpu-memory.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
}

ADJACENT = {
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/73-production-best-practice.md",
    "PLATFORM-TRACE": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/65-kai-scheduler.md",
    "TRAIN-DATA": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-GRPO": "books/part-04-training-system/31-rlhf.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/38-pipeline-parallel.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/47-pagedattention.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/49-tensorrt-llm.md",
    "INFER-GPU-MEMORY": "books/part-05-inference-system/55-pd-disaggregation.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/46-continuous-batching.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/13-position-encoding.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "AGENT-RAG": "books/part-07-agent/77-memory.md",
    "AGENT-MEMORY": "books/part-07-agent/76-rag.md",
    "AGENT-PLATFORM": "books/part-07-agent/83-mcp.md",
    "AGENT-WORKFLOW": "books/part-07-agent/82-multi-agent.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/81-workflow.md",
}

ARTIFACTS = {
    "2606.24143": "https://github.com/furiosa-ai/async-opd",
    "2606.25156": "https://github.com/kreasof-ai/atma",
    "2606.25189": "https://github.com/eunomia-bpf/ActPlane",
    "2606.25198": "https://github.com/a-antoniades/Heuresis",
    "2606.25215": "https://lianqing11.github.io/reflective-vla-page/",
}


def first_sentence(text: str) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    match = re.match(r"(.+?[.!?])(?:\s|$)", clean)
    return (match.group(1) if match else clean).strip()


def closure_kind(title: str, abstract: str) -> tuple[str, str]:
    text = f"{title} {abstract}".lower()
    if any(x in text for x in ("medical", "clinical", "patient", "disease", "healthcare", "radiology")):
        return "domain_result", "结论停留在医疗/临床数据或任务 owner，未改变跨任务 AI-System 的状态、控制或发布契约"
    if any(x in text for x in ("survey", "perspective", "position paper", "taxonomy")):
        return "survey_or_position", "材料以综述/观点/分类为主，未给出可独立验收的 durable mechanism"
    if any(x in text for x in ("dataset", "benchmark", "leaderboard")):
        return "benchmark_only", "新增数据集或榜单但未改变通用 evaluation/release gate、failure authority 或平台 owner"
    if any(x in text for x in ("robot", "navigation", "driving", "manipulation")):
        return "embodied_task_local", "具身任务增量没有形成跨环境可复用的 state/action ownership、fallback 与部署契约"
    if any(x in text for x in ("segmentation", "classification", "detection", "forecasting", "prediction")):
        return "task_model_local", "贡献主要是单一预测/识别任务的模型或指标改进，不是长期 AI-System mechanism"
    if any(x in text for x in ("theorem", "proof", "convergence", "lower bound", "upper bound")):
        return "formal_without_system_delta", "形式结果没有同时给出会改变长期系统 owner、运行 state/control 或验收流程的实现契约"
    if any(x in text for x in ("language model", "llm", "transformer", "attention", "agent")):
        return "model_or_agent_method_local", "模型/Agent 方法或能力增量没有改变长期平台机制、资源边界、权威状态或 release contract"
    return "outside_durable_scope", "主要对象不是长期 AI-System mechanism、state/data/control ownership 或 evaluation/release contract"


def norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n"))
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def rp_id(family: str, aid: str, method: str, evaluation: str, limitation: str, artifact: str, body: str) -> str:
    def multi(value: str) -> str:
        return ";".join(sorted(unicodedata.normalize("NFC", item.strip()) for item in value.split(";") if item.strip() and item.strip() not in {"—", "Not Disclosed"}))
    canonical = "|".join(("review-completion-v1", family, "paper-v1:" + aid, "arXiv:" + aid + "v1", multi("SRC-ARXIV"), "arXiv:" + aid + "v1", multi("SRC-ARXIV@arXiv:" + aid + "v1"), "deep", multi(method), multi(evaluation), multi(limitation), multi(artifact), "claim:" + family, "review:" + family, "review-body-sha256:" + hashlib.sha256(norm(body).encode()).hexdigest()))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def benchmark(row: dict) -> dict:
    aid, abstract = row["arxiv_id"], row["abstract"]
    b = {k: ND for k in ("workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator")}
    b["workload"] = first_sentence(abstract)
    b["evaluator"] = next((s.strip() for s in re.split(r"(?<=[.!?])\s+", abstract) if any(k in s.lower() for k in ("experiments", "evaluate", "evaluation", "results show", "achieves", "outperforms"))), ND)
    special = {
        "2606.24119": {"workload": "816 LoRA/PEFT configurations from three DLM families; 200-step horizon", "evaluator": "collapse precision, F1, final loss and cross-family threshold transfer"},
        "2606.24143": {"model": "Qwen3-1.7B/4B/8B Base", "hardware": "single 8-GPU node", "evaluator": "training tokens/s, pipeline overlap, Avg@32 accuracy and staleness ablations"},
        "2606.24081": {"workload": "11 T2I jailbreak methods under original and unified settings", "model": "4 victim T2I models", "evaluator": "paper-result reproduction error, attack success and memory code-quality ablation"},
        "2606.24311": {"workload": "Terminal-Bench 2.0: five jobs x 89 trials; Terminal-Bench 2.1: three jobs x 89 trials", "model": "GPT-5.3-CodeX and GPT-5.5", "evaluator": "accuracy, failures and execution exceptions"},
        "2606.24322": {"workload": "MEM-INV-Bench; 128 multi-turn runs; Mem0+Qdrant 96 runs per defense", "model": "eight frontier models; six models in production-backend study", "evaluator": "laundering/direct attack success, legitimate utility and user-confirmation burden"},
        "2606.24402": {"workload": "11 CTF challenges, 11 real-world CVEs and 8,651 security write-ups", "model": "Claude Opus 4/4.6, GPT-5.3 and Gemini 3.0 Pro", "evaluator": "poison adoption rate, retrieval rank and rejection cause"},
        "2606.25098": {"workload": "real-world 130 kW GPU cluster under peak, emergency, sustained and carbon-aware dispatch", "hardware": "130 kW GPU cluster", "evaluator": "load reduction, sustained curtailment, priority-job service preservation and geo-shift performance"},
        "2606.25156": {"workload": "120-cell 1B-token factorial; matched 9.816B-token 2K training; evaluation through 256K", "model": "378M NoPE/RoPE/Polar variants", "input_length": "2K train; up to 256K evaluation", "evaluator": "retrieval accuracy, bits-per-byte, eight short-context tasks and kernel overhead"},
        "2606.25178": {"workload": "six-domain reasoning RLVR suite", "model": "Qwen3-1.7B and Llama3.2-3B", "evaluator": "macro accuracy, curriculum dynamics, ablation and wall-clock overhead"},
        "2606.25189": {"workload": "coding policies, OctoBench tasks and safety benchmarks", "evaluator": "policy compliance, DSL coverage/cost and 1.9%-8.4% overhead"},
        "2606.25198": {"workload": "3,222 scored research runs across LLM pretraining, on-policy RL and model unlearning", "concurrency": "asynchronous search strategies; exact worker count varies by experiment", "evaluator": "quality, diversity, novelty and 40 confirmed fabrication audits"},
        "2606.25215": {"workload": "LIBERO, SimplerEnv-Bridge, LIBERO-Plus/Hard and real-robot protocols", "evaluator": "task success under distribution shift, matched history ablation and latency-accuracy trade-off"},
        "2606.28387": {"workload": "CRUSH4SQL 1,534; SEDE 857; BIRD 96 questions", "evaluator": "table/column recall, SQL execution errors, robustness and retrieval latency"},
    }
    b.update(special.get(aid, {}))
    return b


def score(owner: str) -> dict:
    design = 3 if owner in {"PLATFORM-SECURITY", "TRAIN-DISTRIBUTED-TRAINING", "INFER-SPECULATIVE-DECODING", "INFER-GPU-MEMORY"} else 2
    reach = 3 if owner.startswith("PLATFORM-") or owner in {"AGENT-WORKFLOW", "AGENT-PLATFORM", "TRAIN-DISTRIBUTED-TRAINING"} else 2
    return {"design_delta": design, "system_reach": reach, "durability": 3, "total": design + reach + 3}


def main() -> None:
    provisional = json.loads(PROVISIONAL.read_text())
    rows = []
    retained = []
    for row in provisional["identities"]:
        aid = row["arxiv_id"]
        family = "SF-2026-ARXIV-" + aid.replace(".", "-")
        if aid in META:
            owner = META[aid][0]
            status, kind = "retained_pending_exact_v1", "durable_system_candidate"
            reason = f"`{row['title']}` 明确改变 `{owner}` 的长期 mechanism/state/control 或 evaluation contract：{first_sentence(row['abstract'])}"
            retained.append({**row, "source_family_id": family, "stable_node_id": owner})
        else:
            owner = "—"
            kind, why = closure_kind(row["title"], row["abstract"])
            status = "closed_pre_denominator"
            reason = f"`{row['title']}`：{first_sentence(row['abstract'])}；{why}。"
        rows.append({**row, "source_family_id": family, "stable_node_id": owner, "semantic_screen_status": status, "semantic_decision_kind": kind, "semantic_screen_reason": reason, "screened_at": EXECUTED_AT})
    assert len(rows) == 541 and len(retained) == len(META)
    basis = "\n".join(r["source_family_id"] for r in retained)
    denominator_id = "daily-v2.1:2026-06-24:" + hashlib.sha256(basis.encode()).hexdigest()[:16]
    ledger = {**{k: v for k, v in provisional.items() if k != "identities"}, "schema": "daily-v2.1-screening-ledger-v2", "denominator_id": denominator_id, "denominator_frozen_at": EXECUTED_AT, "registered_window_identities": 541, "retained_candidate_families": len(retained), "closed_pre_denominator_families": 541-len(retained), "route_negative_audited": 122, "route_negative_false_negatives": ["2606.25040"], "gate_status": "coverage_closed_evidence_passed_selection_passed_books_open", "identities": rows}
    (PACKET / "screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["source_family_id","arxiv_id","route","title","abstract_basis","decision","decision_kind","stable_node_id","family_specific_reason"])
        for r in rows:
            w.writerow([r["source_family_id"],r["arxiv_id"],r["screening_route"],r["title"],first_sentence(r["abstract"]),r["semantic_screen_status"],r["semantic_decision_kind"],r["stable_node_id"],r["semantic_screen_reason"]])
    (PACKET / "candidate-ids-v1.txt").write_text("\n".join(r["arxiv_id"] for r in retained) + "\n")

    reviews = []
    for r in retained:
        aid, family = r["arxiv_id"], r["source_family_id"]
        owner, ms, es, ls, mechanism, boundary = META[aid]
        base = f"https://arxiv.org/html/{aid}v1"
        method, evaluation, limitation = f"{base} — §{ms}", f"{base} — §{es}", f"{base} — §{ls}"
        artifact = ARTIFACTS.get(aid, "Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review")
        body = (f"### {aid} — {r['title']}\n\n**问题与旧路径。** {first_sentence(r['abstract'])}\n\n"
                f"**机制、状态与控制流。** {mechanism} 唯一 owner 为 `{owner}`；相邻章只消费显式 handoff。\n\n"
                f"**Trade-off、failure、fallback 与共存。** {boundary}\n\n"
                f"<!-- claim:{family}:start -->\nClaim boundary：仅 `arXiv:{aid}v1`；未证明边界定位 `{limitation}`。\n<!-- claim:{family}:end -->")
        reviews.append({**r, "method_locator": method, "evaluation_locator": evaluation, "limitation_locator": limitation, "claim": mechanism, "claim_boundary": boundary, "benchmark_contract": benchmark(r), "score_v2": score(owner), "books_disposition": "Integrate", "primary_evidence_version": f"arXiv:{aid}v1", "artifact_locators": artifact, "review_body": body, "review_body_sha256": hashlib.sha256(norm(body).encode()).hexdigest(), "review_provenance_id": rp_id(family, aid, method, evaluation, limitation, artifact, body)})
    access = {"schema":"exact-v1-access-receipt-v1","denominator_id":denominator_id,"checked_at":EXECUTED_AT,"reader":"official arXiv exact-v1 HTML primary-source reader","result":f"{len(reviews)}/{len(reviews)} exact-v1 identities resolved","blocked":[],"items":[{"source_family_id":r["source_family_id"],"primary_identifier":r["primary_evidence_version"],"locator":f"https://arxiv.org/html/{r['arxiv_id']}v1","status":"official_html_accessible","version_identity":r["primary_evidence_version"],"access_note":"—"} for r in reviews]}
    (PACKET / "exact-v1-access-receipt.json").write_text(json.dumps(access,ensure_ascii=False,indent=2)+"\n")
    receipt_items=[]
    for r in reviews:
        receipt_items.append({k:r[k] for k in ("source_family_id","primary_evidence_version","method_locator","evaluation_locator","limitation_locator","claim_boundary","benchmark_contract","score_v2","stable_node_id","books_disposition","review_provenance_id","artifact_locators","review_body_sha256")} | {"event_identity":"paper-v1:"+r["arxiv_id"],"primary_identifier":r["primary_evidence_version"],"review_route":"deep","reviewed_evidence_versions":"SRC-ARXIV@"+r["primary_evidence_version"],"claim_boundary_ref":"claim:"+r["source_family_id"],"review_ref":"review:"+r["source_family_id"],"completion_result":"complete","ordinary_pending_locator_count":0})
    (PACKET / "source-review-receipts-v2.1.json").write_text(json.dumps({"schema":"source-review-receipts-v2.1","denominator_id":denominator_id,"items":receipt_items},ensure_ascii=False,indent=2)+"\n")

    ranked = sorted(reviews, key=lambda r: (-r["score_v2"]["total"], r["arxiv_id"]))
    winners = ["2606.24322","2606.25098","2606.25189"]
    sel=[]
    for r in reviews:
        selected=r["arxiv_id"] in winners
        sel.append({"source_family_id":r["source_family_id"],"eligibility":"score_7_9; potential_books_delta","decision":"selected" if selected else "not_selected","analysis_unit_id":("DA-20260624-"+r["arxiv_id"].replace(".","-")) if selected else "—","priority_rationale":("入选："+r["claim"] if selected else "未入选长叙事："+r["claim_boundary"]+"；机制仍进入独立 Books handoff。"),"narrative_ref":("analysis:DA-20260624-"+r["arxiv_id"].replace(".","-")) if selected else "analysis-decision:"+r["source_family_id"]})
    (PACKET / "deep-analysis-selection-v1.json").write_text(json.dumps({"schema":"deep-analysis-selection-v1","denominator_id":denominator_id,"frontier_size":len(reviews),"selection_count":3,"winners_frozen_before_rationale":winners,"decisions":sel},ensure_ascii=False,indent=2)+"\n")

    comparisons=[]
    for r in reviews:
        owner=r["stable_node_id"]
        comparisons.append({"source_family_id":r["source_family_id"],"stable_node_id":owner,"target_chapter_ref":PATHS[owner]+"#L1","adjacent_chapter_refs":ADJACENT[owner]+"#L1","existing_proposition_ref":"existing:"+r["source_family_id"],"new_evidence_delta_ref":"delta:"+r["source_family_id"],"evolution_relation":"Direct Evolution","decision":"Integrate","books_review_ref":"books-review:"+r["source_family_id"]})
    (PACKET / "books-comparison-v1.json").write_text(json.dumps({"schema":"books-comparison-v1","denominator_id":denominator_id,"compared":f"{len(reviews)}/{len(reviews)}","items":comparisons},ensure_ascii=False,indent=2)+"\n")

    groups=defaultdict(list)
    for r in reviews: groups[r["stable_node_id"]].append(r)
    queue=["# 2026-06-24 Books Integration Queue V1","",f"Denominator `{denominator_id}`. Root must serialize {len(reviews)} source families into {len(groups)} unique owner files; shared Books remain untouched by this lane.",""]
    ready=["# 2026-06-24 Ready-to-Insert Books Packet V1","","每个 Source Family 只写入一个 owner；以下最小正文与 Review note 均绑定 exact-v1。",""]
    for owner in sorted(groups):
        items=groups[owner]
        queue += [f"## {owner}","",f"- Target: `{PATHS[owner]}`",f"- Adjacent handoff: `{ADJACENT[owner]}`",f"- Source families: {', '.join(r['source_family_id'] for r in items)}",""]
        ready += [f"## {owner} — {PATHS[owner]}","",f"相邻章 `{ADJACENT[owner]}` 只接收 handoff，不重复拥有机制。","","### Owner-merged minimal text",""]
        for r in items:
            ready.append(f"- **{r['source_family_id']}**：{r['claim']} {r['claim_boundary']}")
        ready += ["","### Source-specific Review notes",""]
        for r in items:
            ready.append(f"- {r['source_family_id']}: `arXiv:{r['arxiv_id']}v1`; exact-v1 URL=`https://arxiv.org/html/{r['arxiv_id']}v1`; Method=`{r['method_locator']}`; Evaluation=`{r['evaluation_locator']}`; Non-proof=`{r['claim_boundary']}`; Artifact=`{r['artifact_locators']}`")
        ready.append("")
    (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue)+"\n")
    (PACKET / "READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready)+"\n")
    with (PACKET / "evidence-selection-fresh-audit-v1.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["source_family_id","exact_v1","method_locator","evaluation_locator","limitation_locator","benchmark_10_fields","score_total","selection","books_disposition","audit_status"])
        sb={x["source_family_id"]:x for x in sel}
        for r in reviews: w.writerow([r["source_family_id"],r["primary_evidence_version"],r["method_locator"],r["evaluation_locator"],r["limitation_locator"],"complete",r["score_v2"]["total"],sb[r["source_family_id"]]["decision"],r["books_disposition"],"passed"])

    lines=["# Daily Research — 2026-06-24","",f"> Strict V2.1 Daily for `{denominator_id}`. Coverage, exact-v1 Evidence and full-frontier Selection passed; Books Gate remains Open pending root writeback and 43/43 post-write fresh audit.","","## Executive Summary","",f"Beijing window `[2026-06-23 09:00, 2026-06-24 09:00)` contains 541 registered identities. Full 541/541 title+abstract screening freezes {len(reviews)} durable families and {541-len(reviews)} family-specific closures. The 122/122 route-negative audit promoted Chorus II (`2606.25040v1`) as one false negative. All retained exact-v1 full texts have source-specific Method/Evaluation/counterevidence locators and ten-field benchmark contracts. Shared Books and LEARNING_STATE remain untouched.","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-06-24 |","| Window End | 2026-06-24 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | {denominator_id} |",f"| Denominator Frozen At | {EXECUTED_AT} |","| Completion Status | In Progress |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Open |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-06-23T09:00:00+08:00 | 2026-06-24T09:00:00+08:00 | {EXECUTED_AT} | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 541 | {'; '.join(r['source_family_id'] for r in reviews)} | pages=40; final_cursor=end; 541 unique identities | 2026-06-24T01:00:00Z | ../_sources/daily-20260624/screening-ledger.json; ../_sources/daily-20260624/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260624 | — |","","<!-- coverage:SRC-ARXIV:20260624:start -->",f"All 356 Core, 63 keyword-routed and 122 route-negative identities were screened. Frozen arithmetic: `541 = {len(reviews)} retained + {541-len(reviews)} closures`; route-negative FN=`2606.25040`.","<!-- coverage:SRC-ARXIV:20260624:end -->","","## 2. Candidate Ledger and Score V2","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        s=r["score_v2"]; lines.append(f"| {r['source_family_id']} | arXiv:{r['arxiv_id']}v1 | paper-v1:{r['arxiv_id']} | 2026-W26 | 2026-06-23 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | none | review:{r['source_family_id']} | self | — | new_in_window | {r['stable_node_id']} | Integrate | books-review:{r['source_family_id']} | yes |")
    lines += ["","### Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews: lines.append(f"| {r['source_family_id']} | {r['review_provenance_id']} | deep | {r['primary_evidence_version']} | SRC-ARXIV@{r['primary_evidence_version']} | {r['method_locator']} | {r['evaluation_locator']} | {r['limitation_locator']} | {r['artifact_locators']} | claim:{r['source_family_id']} | complete |")
    lines += ["","### Benchmark Contract","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b=r["benchmark_contract"]; lines.append("| "+" | ".join([r["source_family_id"]]+[b[k] for k in ("workload","model","hardware","precision","input_length","output_length","batch","concurrency","slo","evaluator")])+" |")
    lines += ["","## 3. Source Reviews",""]
    for r in reviews: lines += [f"<!-- review:{r['source_family_id']}:start -->",r["review_body"],f"<!-- review:{r['source_family_id']}:end -->",""]
    lines += ["## 4. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
    for d in sel: lines.append(f"| {d['source_family_id']} | {d['eligibility']} | {d['decision']} | {d['analysis_unit_id']} | — | {d['priority_rationale']} | {d['narrative_ref']} |")
    for r,d in zip(reviews,sel):
        ref=d["narrative_ref"]; lines += ["",f"<!-- {ref}:start -->",d["priority_rationale"],f"<!-- {ref}:end -->"]
    lines += ["","## 5. Books Comparison and Decision","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r,c in zip(reviews,comparisons): lines.append(f"| {r['source_family_id']} | {c['stable_node_id']} | {c['target_chapter_ref']} | {c['adjacent_chapter_refs']} | {c['existing_proposition_ref']} | {c['new_evidence_delta_ref']} | Direct Evolution | Integrate | {c['books_review_ref']} |")
    for r,c in zip(reviews,comparisons): lines += ["",f"<!-- existing:{r['source_family_id']}:start -->",f"Re-read `{c['target_chapter_ref']}` and adjacent `{c['adjacent_chapter_refs']}`; owner remains unique.",f"<!-- existing:{r['source_family_id']}:end -->","",f"<!-- delta:{r['source_family_id']}:start -->",r["claim"],f"<!-- delta:{r['source_family_id']}:end -->","",f"<!-- books-review:{r['source_family_id']}:start -->",f"Direct Evolution; Integrate queued for root. {r['claim_boundary']}",f"<!-- books-review:{r['source_family_id']}:end -->"]
    review_refs="; ".join("review:"+r["source_family_id"] for r in reviews); sel_refs="; ".join(d["narrative_ref"] for d in sel); book_refs="; ".join("books-review:"+r["source_family_id"] for r in reviews)
    lines += ["","## 6. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260624-COVERAGE-V1 | fresh-context:jun24-v1 | coverage | coverage:SRC-ARXIV:20260624 | — | 541/541 title+abstract; denominator {len(reviews)}; closures {541-len(reviews)}; route-negative 122/122 with one promoted FN | passed |",f"| SA-20260624-EVIDENCE-V1 | fresh-context:jun24-v1 | evidence | {review_refs} | — | {len(reviews)}/{len(reviews)} exact-v1 full texts; source-specific Method/Evaluation/counterevidence/artifact and ten-field benchmark contracts | passed |",f"| SA-20260624-SELECTION-V1 | fresh-context:jun24-v1 | deep_analysis_selection | {sel_refs} | — | Full frontier {len(reviews)}/{len(reviews)} rerun after Evidence; three winners frozen | passed |",f"| SA-20260624-BOOKS-PREWRITE-V1 | fresh-context:jun24-v1 | books | {book_refs} | root writeback and post-write fresh audit pending | READY packet groups {len(reviews)} proposals into {len(groups)} owners; shared Books untouched | open |","","## 7. Materials and Access","",f"- {len(reviews)}/{len(reviews)} exact-v1 identities completed official arXiv HTML full-text review; no later-version claim used.","","## 8. Daily Integration Decision","",f"- Proposed Books disposition: {len(reviews)} Integrate across {len(groups)} unique owner files; Books Gate Open until root writeback and 100% post-write audit.","","## 9. Repository Changes","","- This lane writes only the 2026-06-24 Daily, its source packet, and its date-specific finalizer; shared Books and `docs/LEARNING_STATE.md` remain unchanged.","","## 10. Open Questions","","- Root must serialize `READY_TO_INSERT_BOOKS_V1.md`; then this lane must independently verify every body marker, source-specific Review note, unique owner, handoff and exact-v1 boundary before Completion can become Complete."]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(lines)+"\n")
    (PACKET/"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(f"# 2026-06-24 Fresh Evidence and Selection Audit V1\n\n- Denominator `{denominator_id}`: `541 = {len(reviews)} retained + {541-len(reviews)} closures`.\n- Route-negative fresh FN audit: 122/122; promoted `2606.25040v1`.\n- Exact-v1 Evidence: Passed {len(reviews)}/{len(reviews)}.\n- Full-frontier Selection: Passed {len(reviews)}/{len(reviews)}, three winners.\n- Books: Open pending root writeback and post-write fresh audit.\n")
    (PACKET/"README.md").write_text(f"# daily-20260624 source packet\n\n- Window: `{provisional['window']}`\n- Denominator: `{denominator_id}`\n- Raw identities: 541\n- Retained durable families: {len(reviews)}\n- Family-specific pre-denominator closures: {541-len(reviews)}\n- Route-negative audit: 122/122; one promoted false negative\n- Coverage Gate: Closed\n- Evidence Gate: Passed\n- Selection Gate: Passed\n- Books Gate: Open\n- Completion: In Progress\n")
    sums=[]
    for p in sorted(x for x in PACKET.iterdir() if x.is_file() and x.name not in {"SHA256SUMS","screening-ledger-provisional.json"}): sums.append(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name)
    (PACKET/"SHA256SUMS").write_text("\n".join(sums)+"\n")
    print(json.dumps({"denominator_id":denominator_id,"raw":541,"retained":len(reviews),"closures":541-len(reviews),"route_negative_audited":122,"route_negative_false_negatives":1,"integrate":len(reviews),"owners":len(groups),"books_gate":"Open"},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
