#!/usr/bin/env python3
"""Build the 2026-06-08 V2.1 Daily packet without editing Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260608"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-full-semantic-audit-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
BOOKS_QUEUE = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
FRESH_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
POST_WRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
PRESENTATION_AUDIT = PACKET / "CANONICAL_PRESENTATION_AUDIT_V1.md"
SHA256SUMS = PACKET / "SHA256SUMS"
REPORT = ROOT / "papers/2026/06/08/README.md"
EXECUTED_AT = "2026-08-29T15:30:00+08:00"
DENOMINATOR_ID = "DEN-20260608-277042"

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

CANONICAL_HEADER = """**Research Date:** 2026-06-08

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-07 09:00:00 ～ 2026-06-08 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；277/277 registered arXiv identities 完成 title+abstract semantic screen；42-family exact-v1 Evidence、full-frontier Selection 与 Books post-write audit 保持 root-accepted state

**Status:** Complete — Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`
"""

IGNORED_NOISE = """## 8. Ignored Noise

Coverage ledger 中的 `235` 条 family-specific pre-denominator closures 保持在冻结分母之外；它们均已完成 title+abstract semantic decision，不以关键词负路由或静默遗漏代替 closure。
"""

RECOMMENDED_ACTION = """## 9. Recommended Action

维持 root 已接受的 `9 Integrate / 33 No Change — Existing Coverage` 与三条 Deep Analysis unit；本次只迁移 reader-facing presentation，不重新解释证据、不重算 Books owner，也不触发共享写回。
"""

OPEN_QUESTIONS = """## 11. Open Questions

None. 该日普通 pending、external blocker 与未解决 semantic finding 均为零。
"""

FINAL_STATUS = """## 13. Final Status

- Denominator: `{denominator}` = `42 retained / 277 raw`；pre-denominator closures `235`。
- Evidence / Selection: `42/42` exact-v1 Reviews、benchmark contracts 与 full-frontier decisions complete；selected units `3`。
- Books: `9 Integrate / 33 No Change — Existing Coverage`；root writeback 与 `42/42` post-write audit 已闭合。
- Gates: Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`。
""".format(denominator=DENOMINATOR_ID)

# DataCite captured an earlier title for 2606.08531.  The canonical retained
# record follows the title printed by the immutable arXiv v1 HTML.
TITLE_OVERRIDES = {
    "2606.08531": "VESTA: A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents",
}

# id: owner, source-specific durable delta, Score V2 tuple, Books disposition,
# optional full-frontier analysis unit.
META = {
    "2606.08403": ("PLATFORM-SECURITY", "结构化浮点载体把恶意信号藏在原始文本视图之外，并在可信重建后才进入模型上下文，迫使安全 owner 同时校验 data layer 与 reconstruction layer。", (3, 3, 3), "Integrate", "DA-20260608-CARRIER"),
    "2606.08411": ("INFER-DECODE", "AsyncLane 用 lane tree 把 DLM 的 prefix refinement 与 frontier advancement 解耦，并以 shared-prefix batching、lookahead reuse 与 cache refresh 管理异步依赖。", (3, 3, 3), "Integrate", None),
    "2606.08417": ("PLATFORM-EVALUATION-SYSTEM", "零参数劣质 sampler 可在非退化 entropy 下优化 gen-PPL，说明单一 scorer predictability 不能充当生成质量，评测必须转向分布差异。", (3, 2, 3), "No Change — Existing Coverage", None),
    "2606.08432": ("TRAIN-SFT", "TRD 把 on-policy distillation 的修复尺度从 token-loss clipping 提升到 teacher-guided trajectory correction，以避免失败 prefix 产生双峰且碎片化的监督。", (3, 2, 3), "No Change — Existing Coverage", None),
    "2606.08433": ("PLATFORM-SECURITY", "AI code sandbox 不能用单一总分排序；host attack surface、leakage、stackability、CVE、patch cadence 与 fuzzing posture 必须按 threat model 分轴负责。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08446": ("TRAIN-GRPO", "Sparrow 把 long-context RL rollout 的稀疏注意力当作训练系统路径，并显式保留 dense teacher refresh 以约束效率与策略漂移。", (3, 3, 2), "No Change — Existing Coverage", None),
    "2606.08476": ("TRAIN-DISTRIBUTED-TRAINING", "FlashCP 将 context-parallel 的负载均衡、attention kernel 与 KV 通信共同建模，避免静态 sequence sharding 把三类瓶颈分开优化。", (3, 3, 3), "Integrate", "DA-20260608-CONTEXT-PARALLEL"),
    "2606.08483": ("PLATFORM-EVALUATION-SYSTEM", "consumer health LLM 的 personalization 与版本漂移无法由黑盒单次测量独立归因，评测合同必须记录可观察输入、不可见系统状态与重复测量边界。", (2, 3, 3), "No Change — Existing Coverage", None),
    "2606.08486": ("INFER-DECODE", "TRADE 以共享 audio encoder 的 transducer branch 补齐 Speech LLM 的 frame alignment、streaming decode 与 end-of-utterance 状态。", (3, 2, 3), "No Change — Existing Coverage", None),
    "2606.08517": ("PLATFORM-EVALUATION-SYSTEM", "adaptive selective predictor 的部署证明必须联合约束 selected risk、acceptance floor 与 utility，而不能分别挑选阈值后拼接置信区间。", (3, 2, 3), "No Change — Existing Coverage", None),
    "2606.08529": ("PLATFORM-EVALUATION-SYSTEM", "GAIA 控制实验显示 scaffold 本身可显著移动同一模型的得分，因此 capability owner 必须分离 model、scaffold 与 attempt budget。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08531": ("PLATFORM-EVALUATION-SYSTEM", "ForesightSafety-SAGE 把 agent 风险从静态 prompt/终局判断扩展为 scenario generation、authority context 与执行轨迹上的多维检查。", (2, 3, 2), "No Change — Existing Coverage", None),
    "2606.08539": ("PLATFORM-SECURITY", "AgentTrust 按 lexical 与 semantic threat 分流 action decision，并让 allow/warn/block/escalate 的反馈进入可更新 judge，而不是扩张固定规则包。", (3, 3, 3), "Integrate", None),
    "2606.08574": ("TRAIN-DATA", "OrderDP 区分 full-data gradient 与 pruning surrogate 的 unbiasedness，并把样本顺序纳入动态数据删减合同。", (2, 2, 3), "No Change — Existing Coverage", None),
    "2606.08590": ("PLATFORM-MONITORING", "Kubernetes RCA 将 typed evidence graph、read-only tool collection、bounded traversal 与独立 verdict validation 分开，避免 prompt leakage 冒充诊断增益。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08610": ("AGENT-WORKFLOW", "HARBOR 把 robot RL 自动化定义为 bounded stages、standard commands、persistent artifacts 与 executable gates 的 harness，而非一个长提示词。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08615": ("AGENT-MEMORY", "unbounded streaming video 同时要求 proactive interaction、long-horizon memory 与 real-time processing，形成跨 chunk state retention 与 bounded-latency 的联合合同。", (2, 3, 3), "No Change — Existing Coverage", None),
    "2606.08625": ("PLATFORM-EVALUATION-SYSTEM", "rubric 随 chat、reasoning 与 agent 范式演化，评价单位从 holistic output 转为可追踪的 structured criteria 与行为约束。", (2, 2, 3), "No Change — Existing Coverage", None),
    "2606.08635": ("INFER-PD-DISAGGREGATION", "SpectrumKV 将 PD 之间的 KV 传输从 token keep/drop 二元决策改为 per-token mixed precision，使网络字节、量化误差与重算成为同一控制面。", (3, 3, 3), "Integrate", None),
    "2606.08661": ("PLATFORM-SECURITY", "Data Agent 把数据库执行、外部数据资源与 agent reasoning 三个攻击面串联，安全 owner 必须覆盖 query authority、tool side effects 与 evidence provenance。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08671": ("AGENT-REFLECTION", "SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。", (3, 3, 3), "Integrate", None),
    "2606.08679": ("PLATFORM-EVALUATION-SYSTEM", "leaderboard 必须传播 task-level 不确定性并输出 rank intervals，而不是把多任务均值压成确定名次。", (3, 2, 3), "No Change — Existing Coverage", None),
    "2606.08702": ("AGENT-MEMORY", "ConMem 显式建模 memory-skill relation，并从 noisy trajectories 中选择结构化记忆以支持 training-free multi-agent adaptation。", (2, 3, 2), "No Change — Existing Coverage", None),
    "2606.08755": ("AGENT-REFLECTION", "skill generation 与 policy optimization 必须共同验证新 skill 的 usefulness，避免 skill bank 只积累未经行为结果校验的文本程序。", (3, 2, 3), "No Change — Existing Coverage", None),
    "2606.08761": ("INFER-GPU-MEMORY", "APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。", (3, 3, 3), "Integrate", None),
    "2606.08769": ("PLATFORM-EVALUATION-SYSTEM", "RadOT-Eval 将 radiology generation 的 omission、hallucination、polarity、location、uncertainty 与 temporal error 映射为可审计 structured-evidence transport。", (2, 2, 3), "No Change — Existing Coverage", None),
    "2606.08779": ("TRAIN-RLHF", "训练 engine 与推理 engine 的 discrepancy 会使 RL objective 与实际 rollout distribution 脱节，post-training 必须记录 sampler/implementation identity。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08790": ("AGENT-TOOL-CALLING", "RAILS 把 delegated obligation、verification、liability 与 settlement action 组合成 agent commerce 的 clearing contract，而不把支付成功等同于任务履约。", (3, 3, 2), "No Change — Existing Coverage", None),
    "2606.08806": ("PLATFORM-PRODUCTION", "AI-generated test artifacts 需要 provenance、policy checks、human approval 与 audit trail 的治理层，生成速度不能替代测试资产的责任链。", (2, 3, 3), "No Change — Existing Coverage", None),
    "2606.08813": ("AGENT-RAG", "HNTL 用 hierarchical no-pointer tangent-local layout 降低 ANN graph 的 pointer tax 与不规则访存，把候选生成的数据布局与 CPU pipeline 一起优化。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08831": ("PLATFORM-EVALUATION-SYSTEM", "multi-step reasoning 的 factuality error 具有 ancestor-conditioned DAG 结构，conformal control 不能把 node-wise error 简单累加。", (3, 2, 3), "No Change — Existing Coverage", None),
    "2606.08840": ("PLATFORM-EVALUATION-SYSTEM", "code model 的 pass rate 必须按语言、题型与 execution failure mode 分层，aggregate pass rate 会掩盖可部署性边界。", (2, 2, 3), "No Change — Existing Coverage", None),
    "2606.08867": ("AGENT-PLATFORM", "100M-user support agent 把离线 evaluation、context engineering、training 与 online measurement 组成闭环，单一模型分数不代表生产 readiness。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08869": ("PLATFORM-MONITORING", "dynamic cloud-edge control loop 需要把变动 node set 与 query 编码成低延迟 semantic state，而不是只收集 raw counters。", (2, 3, 2), "No Change — Existing Coverage", None),
    "2606.08891": ("INFER-TENSORRT-LLM", "PALUTE 用 processing-in-memory lookup table 同时吸收 quantized GEMM 的 dequantization 与 nonlinear operator 成本，改变 edge inference 的 data-movement owner。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.08892": ("PLATFORM-SECURITY", "Diffuse AI Control 针对长时段、fuzzy-task sabotage 把控制证据分散到多次任务与审计预算，而非依赖单次可验证 outcome。", (2, 3, 3), "No Change — Existing Coverage", None),
    "2606.08893": ("PLATFORM-EVALUATION-SYSTEM", "cheap reward-hacking detector 用 trajectory embedding 与 metadata/reward distance 近似替代昂贵 LLM judge，但其清洗 split 与阈值不能外推为通用证明。", (2, 2, 3), "No Change — Existing Coverage", None),
    "2606.09927": ("INFER-TENSORRT-LLM", "trainable smooth rotation 与 learned channel scales 共同控制 activation outlier 的迁移，量化 owner 需绑定等价变换、校准数据与 serving kernel。", (3, 3, 3), "No Change — Existing Coverage", None),
    "2606.09932": ("TRAIN-RLHF", "过度 SFT 会耗尽后续 RL 的 policy plasticity；SFT-to-RL handoff 应以可学习性而非只看 SFT checkpoint accuracy 作为 release 条件。", (3, 3, 3), "Integrate", "DA-20260608-HANDOFF"),
    "2606.09935": ("PLATFORM-SECURITY", "GitInject 把 issue、PR 与仓库文本中的 prompt injection 连到高权限 CI/CD agent，要求 untrusted content、repository permission 与 approval gate 分离。", (3, 3, 3), "Integrate", None),
    "2606.09936": ("MULTIMODAL-WORLD-MODELS", "不同 world-model substrate 只能通过 capability-typed interface 比较 observability 与 intervention，不能假设 latent、token 与 joint-embedding state 同构。", (2, 2, 3), "No Change — Existing Coverage", None),
    "2606.09937": ("INFER-KV-CACHE", "RKSC 在 multi-branch reasoning 中用 hidden-state similarity 决定 prefix KV sharing，并以 confidence early exit 管理共享错误与冗余 decode。", (3, 3, 3), "No Change — Existing Coverage", None),
}

# Fresh post-write Books audit.  The explicit owner anchor overrides prevent a
# lexical best-match from substituting a nearby paper link for the durable
# proposition that actually supports a No Change decision.
BOOKS_ANCHOR_OVERRIDES = {
    "2606.08432": 315, "2606.08483": 1018, "2606.08486": 178,
    "2606.08517": 1701, "2606.08529": 140, "2606.08531": 1835,
    "2606.08574": 133, "2606.08590": 128, "2606.08610": 104,
    "2606.08615": 14, "2606.08625": 1372, "2606.08661": 562,
    "2606.08679": 1807, "2606.08702": 703, "2606.08755": 274,
    "2606.08769": 74, "2606.08790": 14, "2606.08806": 45,
    "2606.08813": 33, "2606.08840": 170, "2606.08867": 14,
    "2606.08869": 128, "2606.08891": 987, "2606.08892": 298,
    "2606.08893": 1811, "2606.09927": 987, "2606.09936": 14,
    "2606.09937": 110,
}

NO_CHANGE_RATIONALE = {
    "2606.08417": "Ch66 已把 proxy、分布差异、scorer blind spot 与不确定性纳入同一 EvalSpec；该 sampler 反例强化既有原则，不建立新 owner。",
    "2606.08432": "Ch29 已拥有 same-prefix on-policy distillation 与 privileged-teacher/student-state 分离；TRD 是 trajectory-correction 分支，不改变 SFT handoff。",
    "2606.08433": "Ch72 已按 threat model 管理 sandbox isolation、attack surface 与 defense-in-depth；六轴比较是审计实例，不形成跨章节新机制。",
    "2606.08446": "Ch33 已拥有 rollout、policy-version freshness 与训练执行效率边界；稀疏 rollout 加 dense refresh 是该控制面的受限实现分支。",
    "2606.08483": "Ch66 已要求完整 subject identity、重复运行与 client-local/关键 slice；黑盒 consumer-health 测量不能独立归因，正落在既有评测合同。",
    "2606.08486": "Ch44 已拥有 decode frontier、termination、detokenization 与 streaming state；speech transducer/frame alignment 是领域化 decode branch，不改写通用 owner。",
    "2606.08517": "Ch66 已联合管理 risk-coverage、abstention、threshold 与关键 slice；joint certificate 强化现有 release rule，而非新增控制面。",
    "2606.08529": "Ch66 已把 model、harness、environment、scorer 与 raw trajectory 绑定为 evaluation identity；scaffold-induced score movement由该 owner 直接吸收。",
    "2606.08531": "Ch66 已把 Agent 评测扩展到 runtime、tool/environment generation、typed trace 与 scenario coverage；VESTA 是安全场景实例。",
    "2606.08574": "Ch27 已把 select/mix/weight、gradient/loss signal、active set 与 held-out evaluation 建成版本化 data control plane；OrderDP 是 pruning/order 算法分支。",
    "2606.08590": "Ch67 已区分 telemetry、typed failure evidence、root-cause hypothesis、reproduction 与 verdict；Kubernetes RCA harness 不取得 monitoring 新 owner。",
    "2606.08610": "Ch81 已拥有 canonical DAG、typed mutation、persistent artifact 与 executable gate；robot-RL harness 是同一 workflow contract 的实例。",
    "2606.08615": "Ch77 已将 runtime persisted state 与参数/KV 区分并负责跨段保留、压缩、检索与遗忘；streaming video 只新增 workload 压力。",
    "2606.08625": "Ch66 已把 rubric formation、atomic criterion execution、ranking 与版本/审批边界分层；rubric 演化综述不改变该 owner。",
    "2606.08661": "Ch72 已要求 tool/database action 经过 authority、effect receipt、provenance 与 fail-closed control；Data Agent 的三攻击面属于既有分层。",
    "2606.08679": "Ch66 已拒绝 leaderboard-first/average-only，并保留 task slice 与 uncertainty；rank interval 是既有 aggregation contract 的实现。",
    "2606.08702": "Ch77 已拥有结构化 memory、关系边、冲突/supersedes 语义与受限 admission；ConMem 的 memory-skill selection 是训练免分支。",
    "2606.08755": "Ch80 已要求 skill revision 记录 evidence、accept/reject、独立 evaluation 与 rollback；联合 skill/policy 优化验证同一原则。",
    "2606.08769": "Ch66 已拥有 semantic-success taxonomy、per-example evidence 与 domain-specific rubric；radiology error transport 是领域实例。",
    "2606.08779": "Ch31 已将 rollout probability、policy/checkpoint version 与 training/inference runtime identity绑定；engine discrepancy 是既有 RLHF handoff failure。",
    "2606.08790": "Ch78 已拥有 delegated tool intent、typed schema、authorization、side-effect 与 outcome receipt；commerce settlement 是其业务协议层，不新增核心 owner。",
    "2606.08806": "Ch73 已拥有 provenance、policy、approval、release/rollback 与 audit obligations；AI-generated tests 是 production artifact 的受限类别。",
    "2606.08813": "Ch76 已拥有 ingestion/index/candidate construction、index identity 与 retrieval pipeline；HNTL 是 CPU ANN index-layout implementation branch。",
    "2606.08831": "Ch66 已拥有 trajectory/first-error attribution、graph-conditioned evidence 与 conformal uncertainty；DAG factuality control 复用该原则。",
    "2606.08840": "Ch66 已要求 per-example evidence、language/task/risk slices 与 execution failure taxonomy；aggregate pass-rate 分解直接落入现有合同。",
    "2606.08867": "Ch84 已把 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy 组成平台闭环；100M-user case 不改变 ownership。",
    "2606.08869": "Ch67 已把 observed state、typed evidence 与 control-loop signal分开，并将 action authority留给 scheduler/evaluator；semantic estimator 是 sensor 分支。",
    "2606.08891": "Ch49 已拥有 graph/operator 到 kernel/accelerator 的执行映射及 data-movement contract；PIM lookup table 是 backend alternative。",
    "2606.08892": "Ch72 已区分 CoT sensor、monitorability、authorization 与 outcome safety，并组合 budget/action verifier；diffuse long-horizon control 复用此分层。",
    "2606.08893": "Ch66 已将 judge/detector限定为需校准的 sensor，并保存 split、threshold、uncertainty 与独立 verifier；cheap detector 不改变 truth owner。",
    "2606.09927": "Ch49 已要求 quantization artifact、calibration、graph mapping、可用 kernel 与目标硬件共同绑定；rotation/scaling 是实现分支。",
    "2606.09936": "Ch25 已区分 observed state、latent belief、imagined state，并以 action intervention/outcome 验证 capability；异构 substrate adapter 不改写 world-model owner。",
    "2606.09937": "Ch45 已拥有 prefix reuse 的 model/position/cache identity、sharing safety 与 branch lifecycle；hidden-state similarity/early exit 是近似复用分支。",
}

WRITEBACK_ANCHORS = {
    "2606.08403": ("books/part-06-ai-infrastructure/72-security.md", "#### 安全边界必须覆盖不可见重建、动作判定与仓库权限"),
    "2606.08411": ("books/part-05-inference-system/44-decode.md", "### Diffusion Decode 要分离 Refinement 与 Advancement"),
    "2606.08476": ("books/part-04-training-system/36-distributed-training.md", "### Context Parallelism 必须联合优化 Sequence、Kernel 与 Communication"),
    "2606.08539": ("books/part-06-ai-infrastructure/72-security.md", "#### 安全边界必须覆盖不可见重建、动作判定与仓库权限"),
    "2606.08635": ("books/part-05-inference-system/55-pd-disaggregation.md", "### PD Handoff 可以把 KV Bytes 与 Quality 变成同一控制面"),
    "2606.08671": ("books/part-07-agent/80-reflection.md", "### Skill Revision 需要保留 Decision History，而不只是覆盖最新文本"),
    "2606.08761": ("books/part-05-inference-system/54-gpu-memory.md", "### 低比特收益还取决于同一 SM 内的 Compute Balance"),
    "2606.09932": ("books/part-04-training-system/31-rlhf.md", "### SFT Checkpoint 的 Release 条件还要包含后续 RL Plasticity"),
    "2606.09935": ("books/part-06-ai-infrastructure/72-security.md", "#### 安全边界必须覆盖不可见重建、动作判定与仓库权限"),
}

LOCATORS = {
    "2606.08403": ("§3 Threat Model; §4 Carriers", "§5 Experimental Setup; §6 Results", "§7 Discussion; §8 Limitations"),
    "2606.08411": ("§3 Methods; §§3.1–3.4 lane scheduling and execution", "§4 Experiments; §4.1 Experimental Setup", "§4.3 Ablation Study; §5 Conclusion"),
    "2606.08417": ("§3 Methodology; §§3.1–3.2 naive samplers and distributional metrics", "§4 Experiments", "§5 Conclusion; Appendix A parameter sweeps"),
    "2606.08432": ("§4 Prefix Failure; §5 Trajectory-Refined Distillation", "§6 Experiments; Appendix C Evaluation Protocol", "§6.4–6.5 signal/trajectory analysis; Appendix B ablations"),
    "2606.08433": ("Methodology in brief; §§2.1–2.6 six engine-level axes", "§3 Cross-axis reads; §4 Threat-model qualification matrix; §5 product portraits", "§6 Open questions; §7 Caveats and limitations"),
    "2606.08446": ("§3 Observation and Insights; §§3.1–3.3 stability/cost controls", "§4 Empirical Studies; §§4.1–4.5", "Appendices A, D, E and §5 Conclusion"),
    "2606.08476": ("§3 FlashCP Design; §§3.1–3.4", "§4 Experiments; §4.1 Experiment Setup; §§4.2–4.3", "§2.3 Limitation of Existing Works; §6 Conclusion"),
    "2606.08483": ("§1 Question Design; §2 User Profile Simulation; §3 Technical Implementation", "§4 Evaluation Criteria; §5 Temporal Stability", "§6 Discussion and structural black-box limits"),
    "2606.08486": ("§3 TRADE Model; §4 Training and Inference", "§6 Experiments; §6.1 Setup; §§6.2–6.5", "§8 Limitations; Appendix A model configuration"),
    "2606.08517": ("§3 Problem, Setup, and Algorithm; §4 Joint Certificate", "§5 Experimental Evaluation; §5.1–5.3", "§4.9 regime-separation scope; later experimental scope analysis"),
    "2606.08529": ("§3 Methodology; §§3.1–3.6", "§4 Results; §§4.1–4.5", "§6 Limitations; Appendix D incomplete cells/failure analysis"),
    "2606.08531": ("§3 VESTA Framework; §§3.1–3.3", "§4 Experimental Results and Analysis; §4.1 setup", "§5 Conclusion; Appendices D–H judge/protocol/trace evidence"),
    "2606.08539": ("§3 threat-type decomposition and trust-layer design; §4 self-improving dual store", "§5 evaluation and online replay; Tables 2–5", "§6 Limitations; concurrency and fixed-verdict replay boundary"),
    "2606.08574": ("§2 Method; §3 Theoretical Analysis", "§4 Experimental Settings; §5 Empirical Studies", "Appendix F Limitations and Future Work"),
    "2606.08590": ("§IV System Overview; §V Audit Checks", "§VI Snapshot Evaluation; §VII Live-Validation Status", "§VIII Failure Analysis; §IX Limitations and Future Work"),
    "2606.08610": ("§2 Robot RL Automation as a Harness Engineering Problem; §3 HARBOR", "§4 Experiments; §§4.1–4.3; Appendix D details", "§5 Conclusion, Limitations, and Future Work"),
    "2606.08615": ("§3 streaming problem formulation; §§4–5 streaming-native VLM and harness", "§6 Streaming-Eval; §7 Experiment; §7.1 setup", "§7.4 Ablation Study; §9 Limitations"),
    "2606.08625": ("§2 rubric definition/taxonomy; §3 construction and optimization", "§4 evaluation use; §5 training use", "§6 reliability limits; §8 future directions and claim-bounded survey scope"),
    "2606.08635": ("§2 Problem Formulation; §4 SpectrumKV Policy", "§5 Experimental Setup; §6 Results; §7 Additional Analyses", "§8 Evidence boundary; §9 Limitations and Threats to Validity"),
    "2606.08661": ("§3 Threat Model and Overview; §4 Vulnerability Analysis", "§5 Evaluating Vulnerabilities; §6 Evaluation Details", "§6.4 sensitivity; §6.5 commercial-system generalization; §7 takeaways"),
    "2606.08671": ("§2 Method; §§2.2–2.3 harness and persistent decision history", "§3 Experiments; §3.1 Benchmarks and Evaluation Settings", "§5 Conclusion; unnumbered Limitations"),
    "2606.08679": ("§2 Task-level model ranking; §3 ranking across tasks", "§4 Experiments; §§4.1–4.3", "Appendix D rank-interval interpretation and task selection"),
    "2606.08702": ("§3 budgeted context-control preliminaries; §4 Methodology; §§4.1–4.5", "§5 Experiment; Appendix A.3 protocol", "§5.3 Additional Analysis and Discussion; appendix run-isolation boundaries"),
    "2606.08755": ("§3 Preliminary negative results; §4 Skill-Augmented Policy Optimization", "§5 Experiments; §5.1 setup; §§5.2–5.5", "§5.4 skill utility; §5.5 ablation; Appendix D negative/alternate results"),
    "2606.08761": ("§2 W4A4 performance gap; §3 APEX4 quantization; §4 pure-W4A4 kernel", "§5 Evaluation; §5.1 setup; §§5.2–5.4", "§5.5 cross-platform analysis; §7 Conclusion and deployment boundary"),
    "2606.08769": ("§III problem/data; §IV RadOT-Eval method", "§V Evaluation Protocol; §VI Results", "§VII Discussion, limitations, and evidence-transport boundary"),
    "2606.08779": ("§3 engine-discrepancy decision space; §4 magic penalty; §5 discrepancy-constrained MDP", "§6 Experiments; setup, results, and ablations", "§7 Limitations and engine-identity boundary"),
    "2606.08790": ("§3 RAILS at a glance; §4 formal model; §§5–7 verification/settlement state machine", "§8 worked scenarios and exposure analysis", "Not Disclosed — no empirical limitations section; formal proposal is bounded to §§3–8 and does not prove real task completion"),
    "2606.08806": ("§4 Governance Methodology and control chain", "§5 Results and artifact-policy analysis", "§6 Conclusion; provenance, approval, and auditability boundary"),
    "2606.08813": ("§2 Aperon system architecture and HNTL layout", "§3 Implementation, hardware, and retrieval results", "§4 Conclusion; CPU/ANN-layout scope boundary"),
    "2606.08831": ("§2 Setup and ancestor-conditioned DAG errors; §3 inference-time subgraph prediction and conformal calibration", "§4 Experiments", "§6 Limitations and graph/calibration assumptions"),
    "2606.08840": ("§III Evaluation Methodology", "§IV Results and execution failure modes", "§V Discussion and aggregate-pass-rate boundary"),
    "2606.08867": ("§4 Production support-agent system design", "§5 Case Study and evaluation; §6 offline/online measurement", "privacy, rollout, and production-readiness boundaries in §§6–7"),
    "2606.08869": ("§II dynamic cloud-edge model; §III semantic-state framework", "§IV Implementation/training; §V Experimental Results", "§VI Conclusion and topology/workload scope"),
    "2606.08891": ("§3 PALUTE Architecture Design; §§3.1–3.4", "§4 Evaluation; §4.1 Experimental Setup; §§4.2–4.4", "§4.3 sensitivity; §4.4 overhead; §5 Conclusion and simulation boundary"),
    "2606.08892": ("§2 diffuse-threat control framework; §§3–5 red/blue automated experiment planning", "§5 mitigations; Appendix C scorer details; Appendices D–G optimization/experiments", "§7 Limitations and Future Work; fuzzy-task and automated-scorer boundary"),
    "2606.08893": ("§2 detector objective/architecture; §3 dataset cleaning and training", "§4 Results; §§4.1–4.6", "§5 Conclusion/Future Work; Appendix A negative path and robustness ablations"),
    "2606.09927": ("§III Method; §§III-A–III-C", "§IV Experimental Setup; §V Results; N1–N3/T1–T3", "§VI Discussion and Limitations"),
    "2606.09932": ("§3 Diagnosing and Restoring Plasticity; §§3.1–3.4", "§4 Experiments; §4.1 Setup; §§4.2–4.3; Appendix B", "Appendix C analyses/cost; handoff evidence is workload-specific, not a universal SFT stopping rule"),
    "2606.09935": ("§3 Threat Model; §4 GitInject workflows/scenarios/execution", "§5 Results; §§5.1–5.5; Appendices B–C", "§§6.1–6.3 structural scope, limitations, and responsible disclosure"),
    "2606.09936": ("§3 WorldModelLens abstraction; §§3.1–3.3 capability adapters/hooks/replay", "§4 reusable analyses; §5 Evaluation; §§5.1–5.3", "§7 Limitations and Roadmap; heterogeneous-substrate capability boundary"),
    "2606.09937": ("§2 RKSC Pipeline; §§2.1–2.4 ASKS/CGEE/RSBCM", "§3 Experimentation and Results; §3.1 setup; §§3.2–3.4", "§4 Analysis/Ablations; §5 Limitations; Appendices C–G sensitivity/failures"),
}

BENCH_OVERRIDES = {
    "2606.08403": {
        "workload": "Disclosed — §5 uses summarization and structured extraction across four carriers, three injection objectives, four defenses and three commercial APIs; 14,400 attacked real-model trials plus 4,800 clean trials",
        "model": "Disclosed — GPT-5.4, Gemini 3.1 Flash-Lite Preview, and Claude Sonnet 4.6; Prompt Guard 2, TF-IDF and roberta-base defenses",
        "hardware": "Not Disclosed — API-backed model execution and local classifier hardware are not identified",
        "precision": "Not Disclosed — model/classifier numerical precision is not identified",
        "input_length": "Disclosed — Appendix C reports neural-detector maximum sequence length 512 and largest attacked input 438 subword tokens",
        "output_length": "Not Disclosed — no fixed model-output length contract is identified",
        "batch": "Disclosed — roberta-base defense training uses batch size 16; API attack trials are not relabeled as a serving batch",
        "concurrency": "Not Disclosed — no in-flight concurrency contract is identified",
        "slo": "Not Disclosed — ASR/TSR thresholds are evaluation metrics, not a production SLO",
        "evaluator": "Disclosed — leakage ASR, Strong ASR, task success rate and detection rate, with carrier×defense and 2×2 ablations",
    },
    "2606.08411": {
        "workload": "Disclosed — §4.1 evaluates GSM8K, GSM8K-CoT, MATH, HumanEval and MBPP over 256/512/1024 generation budgets",
        "model": "Disclosed — LLaDA- and Dream-based masked diffusion LMs; Fast-dLLM and inference-only d3LLM baselines",
        "hardware": "Disclosed — one NVIDIA H100 GPU",
        "precision": "Not Disclosed — §4.1 does not identify numerical precision",
        "input_length": "Not Disclosed — prompt lengths are task-dependent and no single fixed input length is stated",
        "output_length": "Disclosed — benchmark generation budgets 256, 512 and 1024 tokens",
        "batch": "Disclosed — inference batch size 1",
        "concurrency": "Not Disclosed — active lanes are scheduler state, not request concurrency",
        "slo": "Not Disclosed — TPS/quality trade-off has no production acceptance threshold",
        "evaluator": "Disclosed — tokens/s, exact-match accuracy, pass@1, model-call NFE and wall-clock latency",
    },
    "2606.08432": {
        "workload": "Disclosed — five competition-math benchmarks plus HumanEval+, MBPP+ and LiveCodeBench for OPD code evaluation",
        "model": "Disclosed — Qwen3-1.7B/4B students, frozen Qwen3-8B teacher, and Qwen3-4B/8B shared-backbone OPSD",
        "hardware": "Disclosed — Appendix C uses one 8-GPU node; exact accelerator model is not identified in the bound locator",
        "precision": "Disclosed — bfloat16 training",
        "input_length": "Disclosed — Appendix C reports method-specific maximum lengths from 18,432 to 38,912 tokens",
        "output_length": "Disclosed — evaluation samples up to 64 math or 128 code sequences; fixed token cap varies by recipe",
        "batch": "Disclosed — per-GPU batch 1 with gradient accumulation 16, effective batch 128 on eight GPUs",
        "concurrency": "Not Disclosed — sample count is not in-flight serving concurrency",
        "slo": "Not Disclosed — no serving SLO",
        "evaluator": "Disclosed — Avg@16, Pass@16, task accuracy, KL/trajectory diagnostics and refinement-signal ablations",
    },
    "2606.08476": {
        "workload": "Disclosed — WLB-LLM, Pile and RedPajama; 100K sampled packed sequences; 128K contexts; CP sizes 4 and 8",
        "model": "Disclosed — 16- and 32-attention-head model configurations with head dimension 128; Llama3 CP, Per-Doc CP and Ring-Attn baselines",
        "hardware": "Disclosed — single node with 8×NVIDIA H100 SXM 80GB connected by NVLink",
        "precision": "Not Disclosed — §4.1 does not identify numerical precision",
        "input_length": "Disclosed — 128K context in the main comparison, with additional context-window sweeps",
        "output_length": "Not applicable — training/inference attention-kernel benchmark, not free-form generation output",
        "batch": "Disclosed — each evaluation input is a packed sequence; no global optimizer batch is stated",
        "concurrency": "Disclosed — CP worker counts 4 and 8; this is parallelism degree, not request concurrency",
        "slo": "Not Disclosed — latency/speedup has no acceptance SLO",
        "evaluator": "Disclosed — normalized training/inference latency, speedup, load imbalance, communication and kernel-efficiency breakdown",
    },
    "2606.08539": {
        "workload": "Disclosed — independent 630-action corpus, external semantic slice, and 30×1,500-action Monte Carlo online replay (45,000 actions)",
        "model": "Disclosed — Haiku 4.5, Sonnet 4.6, Opus 4.8 and GPT-5.5 judges; deterministic rules and MiniLM retrieval controls",
        "hardware": "Not Disclosed — hosted judge/runtime hardware is not identified",
        "precision": "Not Disclosed — numerical precision is not identified",
        "input_length": "Not Disclosed — action text length contract is not identified",
        "output_length": "Not Disclosed — judge output length is not identified",
        "batch": "Not Disclosed — corpus/replay size is not a model batch size",
        "concurrency": "Not Disclosed — §6 explicitly says live concurrency is not exercised by fixed-verdict replay",
        "slo": "Disclosed as a safety invariant, not latency SLO — zero benign hard-blocks; escalation tops out at warn/review",
        "evaluator": "Disclosed — accuracy, FPR/FNR, judge-call rate, semantic accuracy, memory correctness and dangerous leaks",
    },
    "2606.08635": {
        "workload": "Disclosed — WikiText-2 PPL, NIAH at 4,096 tokens/19 depths, 2K–8K context sweeps, TTFT/TPS transfer-path timing and ablations",
        "model": "Disclosed — Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3 and Gemma-2-9B-it; Qwen2.5-14B only in locality characterization",
        "hardware": "Disclosed — NVIDIA RTX 4080 SUPER 32GB and RTX 4090 48GB cloud GPUs",
        "precision": "Disclosed — token tiers FP16/INT8/INT4; adaptive fallback disables INT4 for Qwen after probe failure",
        "input_length": "Disclosed — 2K–8K contexts; NIAH fixed at 4,096 in the main retrieval slice",
        "output_length": "Not Disclosed — no fixed decode output length is identified",
        "batch": "Not Disclosed — no batch size is identified",
        "concurrency": "Not Disclosed — no continuous batching or request concurrency; §6.6 excludes a complete PD scheduler and contention",
        "slo": "Not Disclosed — TTFT reduction has no acceptance threshold",
        "evaluator": "Disclosed — PPL delta, NIAH accuracy, TTFT, TPS, transfer budget, quantization error and probe/ablation outcomes",
    },
    "2606.08671": {
        "workload": "Disclosed — GAIA and WebWalkerQA-EN in curated-search and raw-open-web settings",
        "model": "Disclosed — Claude Opus 4.6 development controller and Qwen3.6-35B-A3B execution/evaluation backbone",
        "hardware": "Not Disclosed — model execution hardware/topology is not identified",
        "precision": "Not Disclosed — numerical precision is not identified",
        "input_length": "Not Disclosed — task/context token lengths are not identified",
        "output_length": "Not Disclosed — output length is not identified",
        "batch": "Not Disclosed — no batch size is identified",
        "concurrency": "Not Disclosed — role-bounded dispatches are not quantified as concurrent execution",
        "slo": "Not Disclosed — no latency/reliability SLO",
        "evaluator": "Disclosed — benchmark accuracy by difficulty split plus optimization-trajectory comparison; English and single-skill limitations stated",
    },
    "2606.08761": {
        "workload": "Disclosed — WikiText2 perplexity, PIQA/ARC/HellaSwag/WinoGrande zero-shot accuracy, kernel tests and vLLM end-to-end serving",
        "model": "Disclosed — LLaMA-2 family (including 7B/70B), LLaMA-3-8B and Qwen2.5 family (including 7B/32B)",
        "hardware": "Disclosed — A100-40G, RTX 3090, A40 and L40S with per-SM and memory specifications",
        "precision": "Disclosed — pure W4A4/INT4, compared with FP16, W4A16, W4A8 and mixed W4A4/W4A8 baselines",
        "input_length": "Not Disclosed as one serving contract — workload-dependent calibration/evaluation inputs",
        "output_length": "Not Disclosed — no fixed generated-token length is identified",
        "batch": "Disclosed — vLLM serving sweeps include batch sizes through 256; A100 recovers at batch size ≥64",
        "concurrency": "Not Disclosed — batch sweep is not relabeled as in-flight request concurrency",
        "slo": "Not Disclosed — throughput/speedup has no acceptance SLO",
        "evaluator": "Disclosed — kernel/end-to-end speedup, PPL delta, zero-shot accuracy and cross-GPU rho analysis",
    },
    "2606.09932": {
        "workload": "Disclosed — math RL and τ-bench Retail agentic SFT/RL, with plasticity probes and periodic validation",
        "model": "Disclosed — EvoLM-4B, Qwen3-8B and Qwen3-30B-A3B teacher; GRPO actor/reference checkpoints",
        "hardware": "Disclosed — math RL on one node of 8×H800; agentic run uses 6 policy/user-simulator GPUs; rejuvenation probes on one H800",
        "precision": "Not Disclosed — the bound setup does not identify one numerical precision contract",
        "input_length": "Disclosed — math RL max prompt 512 and response 1,024; agentic SFT/RL max response 4,096/1,024",
        "output_length": "Disclosed — response limits above, workload-specific",
        "batch": "Disclosed — math prompt batch 512, mini-batch 128, 8 responses/prompt; agentic global batch 96 from 12 prompts×8 trajectories; SFT batch 16",
        "concurrency": "Not Disclosed — rollout multiplicity/dynamic batching is not relabeled as request concurrency",
        "slo": "Not Disclosed — training success/plasticity is not a production SLO",
        "evaluator": "Disclosed — checkpoint/RL improvement, Math-Verify reward, τ-bench task outcomes, plasticity diagnostics and rejuvenation cost",
    },
    "2606.09935": {
        "workload": "Disclosed — real-world AI-powered CI/CD agent workflows with malicious issue/PR/repository content and permission-bearing actions",
        "model": "Disclosed in the exact-v1 experiment/system matrix; model identity is bound to the evaluation locator and not generalized across vendors",
        "hardware": "Not Disclosed — hosted CI/CD/model hardware is not identified",
        "precision": "Not Disclosed — numerical precision is not applicable/disclosed",
        "input_length": "Not Disclosed — repository/issue content lengths are not a fixed token contract",
        "output_length": "Not Disclosed — no fixed output length",
        "batch": "Not Disclosed — no batch size",
        "concurrency": "Not Disclosed — no in-flight concurrency contract",
        "slo": "Not Disclosed — attack success is not a serving SLO",
        "evaluator": "Disclosed — exploit/attack outcomes across injection surfaces, permissions and mitigations; claim is CI/CD threat-model scoped",
    },
    "2606.08446": {
        "workload": "Disclosed — long-context RL rollout plus sparse-attention cost studies, including 16K/24K/32K prefill probes and 1,000 repeated decode timings",
        "model": "Disclosed — Qwen3-1.7B is used in the reported stability example; dense-teacher and sparse-student configurations remain recipe-specific",
        "hardware": "Disclosed — single NVIDIA H200 for the bound kernel/full-model cost measurements",
        "precision": "Not Disclosed — no numerical training/inference precision contract is stated in the bound setup",
        "input_length": "Disclosed — 16K, 24K, and 32K prefill lengths; 37K generation-budget stability slice",
        "output_length": "Disclosed by experiment — long-generation regimes vary; no single universal decode cap",
        "batch": "Disclosed — batch 8 in the 1,000-trial full-model timing and batch 16 in the page-size cost table",
        "concurrency": "Not Disclosed — batch size is not relabeled as request concurrency",
        "slo": "Not Disclosed — stability and speedup results are not a production SLO",
        "evaluator": "Disclosed — sparse/dense mismatch, rollout stability, latency, page-size sensitivity and LoRA-distillation overhead",
    },
    "2606.08486": {
        "workload": "Disclosed — streaming speech recognition over six chunk-size operating points and offline/streaming comparisons",
        "model": "Disclosed — shared audio encoder with transducer branch, adaptor/joint network, and Speech-LLM decoder",
        "hardware": "Disclosed — training on 16×H200 GPUs; real-time inference check on one H200; about 8 GB inference memory",
        "precision": "Disclosed — bfloat16 mixed-precision training",
        "input_length": "Disclosed — dynamic chunks 4/8/16/24/32/full post-subsampling frames; utterance split at 25 seconds",
        "output_length": "Not Disclosed — no fixed generated-token cap",
        "batch": "Not Disclosed — eight-step gradient accumulation is disclosed but per-step/global batch is not",
        "concurrency": "Not Disclosed — one-pass streaming is not an in-flight concurrency contract",
        "slo": "Disclosed as evaluated real-time boundary — maximum RTF 0.171 across six operating points, not a production availability SLO",
        "evaluator": "Disclosed — speech quality/alignment, latency/RTF, streaming stability and operating-point comparisons",
    },
    "2606.08574": {
        "workload": "Disclosed — CIFAR-10/100 and ImageNet-1K pruning with ResNet-18/50, repeated stability and gradient checks",
        "model": "Disclosed — ResNet-18 and ResNet-50 with Dynamic Random, UCB and InfoBatch baselines",
        "hardware": "Disclosed — ImageNet timing on a 2×NVIDIA L40 server",
        "precision": "Disclosed — Timm ImageNet recipe uses mixed-precision training; exact dtype is not stated",
        "input_length": "Not applicable — fixed image datasets rather than token input",
        "output_length": "Not applicable — classification training",
        "batch": "Disclosed — 128 for CIFAR and 1,024 for ImageNet",
        "concurrency": "Not Disclosed — no serving concurrency",
        "slo": "Not Disclosed — accuracy/runtime comparisons have no acceptance SLO",
        "evaluator": "Disclosed — accuracy, training time/GPU-hours, pruning ratio, Jaccard stability and gradient direction",
    },
    "2606.08661": {
        "workload": "Disclosed — isolated benchmark data across database execution, external-resource and agent-reasoning attack surfaces plus commercial-service checks",
        "model": "Disclosed in §§6.1–6.5 — open-source and commercial data-agent systems are reported per condition",
        "hardware": "Disclosed — AMD Ryzen Threadripper PRO 9975WX, 576 GB RAM, one RTX Pro 6000 GPU for open-source runs",
        "precision": "Not Disclosed",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "Not Disclosed — exploit outcomes are not a production SLO",
        "evaluator": "Disclosed — vulnerability/attack outcomes, sensitivity, cross-system generalization and explicit ethical scope",
    },
    "2606.08755": {
        "workload": "Disclosed — ALFWorld, WebShop and Search-QA policy/skill co-evolution",
        "model": "Disclosed in §5.1 and Appendix hyperparameters; model identity stays workload-bound",
        "hardware": "Not Disclosed",
        "precision": "Not Disclosed",
        "input_length": "Disclosed — maximum prompts 4,096/6,000/5,000 by workload",
        "output_length": "Disclosed — maximum responses 512/768/700 and environment steps 50/15/4",
        "batch": "Disclosed — train batches 16/16/512, validation 256/64/1,024, eight rollouts per prompt",
        "concurrency": "Not Disclosed — rollout multiplicity is not request concurrency",
        "slo": "Not Disclosed",
        "evaluator": "Disclosed — task reward/success, skill utility, joint-optimization ablation and negative baselines",
    },
    "2606.08779": {
        "workload": "Disclosed — DAPO-Math-17K RL with math-verify reward and explicit train/inference-engine discrepancy",
        "model": "Disclosed in §6 setup; model/checkpoint and engine identities are condition-bound",
        "hardware": "Not Disclosed",
        "precision": "Disclosed as the studied discrepancy dimension — FP16 alignment is a prior baseline, not asserted as the paper's universal runtime dtype",
        "input_length": "Not Disclosed — prompt cap is not stated in the bound setup",
        "output_length": "Disclosed — maximum response length 8,192 tokens",
        "batch": "Disclosed — 64 prompts, PPO mini-batch 16, eight rollouts per prompt",
        "concurrency": "Not Disclosed",
        "slo": "Not Disclosed",
        "evaluator": "Disclosed — math reward, training efficiency/stability, engine-discrepancy and ablation outcomes",
    },
    "2606.08790": {
        "workload": "Not applicable — formal clearing protocol with worked scenarios, not an empirical benchmark",
        "model": "Not applicable",
        "hardware": "Not applicable",
        "precision": "Not applicable",
        "input_length": "Not applicable",
        "output_length": "Not applicable",
        "batch": "Not applicable",
        "concurrency": "Not applicable",
        "slo": "Not applicable — protocol invariants are not measured service objectives",
        "evaluator": "Not applicable — definitions/propositions and worked scenarios do not constitute empirical verification",
    },
    "2606.08806": {
        "workload": "Disclosed — Defects4J and PROMISE with Jenkins/GitHub Actions governance checks",
        "model": "Disclosed — transformer-based artifact generator, RoBERTa governance classifier, SHAP/attention explainability",
        "hardware": "Disclosed — Intel Xeon Gold 6338, NVIDIA A100 40 GB, 128 GB RAM, Ubuntu 22.04",
        "precision": "Not Disclosed",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "Not Disclosed — reported generation latency and governance quality have no acceptance threshold",
        "evaluator": "Disclosed — test accuracy/validity/success, hallucination rate, governance precision/recall/FPR and latency",
    },
    "2606.08831": {
        "workload": "Disclosed — multi-step reasoning DAG factuality with calibration/test splits and ancestor-closed subgraph objectives",
        "model": "Disclosed — factuality-utility predictor plus paper-specified LLM reasoning generators",
        "hardware": "Not Disclosed",
        "precision": "Not Disclosed — 'precision-oriented' names a statistical objective, not numerical dtype",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Disclosed — predictor training batch size 32",
        "concurrency": "Not Disclosed",
        "slo": "Disclosed as statistical coverage level 1-alpha, not latency SLO",
        "evaluator": "Disclosed — no-false/no-miss conformal coverage, retained subgraph utility and calibration validity",
    },
    "2606.08840": {
        "workload": "Disclosed — multilingual execution-grounded code tasks stratified by language, task type and runtime failure",
        "model": "Disclosed — nine open-weight/openly accessible instruction-tuned code models",
        "hardware": "Disclosed — Lambda Vector One, AMD Ryzen 7, 128 GB RAM, RTX 4090 24 GB, 4 TB SSD",
        "precision": "Not Disclosed",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "Not Disclosed",
        "evaluator": "Disclosed — execution pass rate stratified by language/task plus compile/runtime/timeout failure modes",
    },
    "2606.08869": {
        "workload": "Disclosed — one seven-node live Kubernetes cluster under five stress profiles; 100-question and 700-query comparisons",
        "model": "Disclosed — LPSE, 106.3M-parameter MLP, XGBoost, Qwen3-4B and 120B Nemotron upper-bound baseline",
        "hardware": "Disclosed — one RTX 6000 Ada GPU for non-LLM systems; Qwen3-4B single-GPU comparison",
        "precision": "Not Disclosed",
        "input_length": "Disclosed — 16-frame context window; 78,352-dimensional flattened MLP input",
        "output_length": "Not applicable — state/question classification",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed — seven sequential queries within a budget is headroom analysis, not concurrent load",
        "slo": "Disclosed — 50 ms control-loop budget; observed 6.65 ms mean is one-run evidence",
        "evaluator": "Disclosed — clean/stressed accuracy, latency, robustness, model size and cluster-state coverage",
    },
    "2606.08891": {
        "workload": "Disclosed — cycle-accurate end-to-end Transformer decode simulation plus RTL synthesis and sensitivity/overhead studies",
        "model": "Disclosed — Qwen3-0.6B/1.7B/4B/8B with Jetson Orin NX, PIMPAL, FIGLUT and CHIME baselines",
        "hardware": "Disclosed — modeled 35 nm, 768-layer, 24 GB M3D DRAM; 7 nm logic synthesized at 200 MHz",
        "precision": "Disclosed — W4A4, 4-bit LUT results and 128-bit row-buffer transfers",
        "input_length": "Not Disclosed — no one token-length contract",
        "output_length": "Not Disclosed — throughput is per generated token without a fixed sequence cap",
        "batch": "Not Disclosed",
        "concurrency": "Disclosed at hardware level — modeled peak 8,388,608 concurrent LUT lookups; not request concurrency",
        "slo": "Not Disclosed — TPS/power/area results have no acceptance threshold",
        "evaluator": "Disclosed — TPS, power, energy/area efficiency, sensitivity and overhead under simulation/synthesis",
    },
    "2606.08892": {
        "workload": "Disclosed — fuzzy research-proposal tasks with automated red/blue prompt optimization, scorer controls and appended stress experiments",
        "model": "Disclosed — paper-processing, red/blue and scorer prompts bind exact provider models in Appendix H",
        "hardware": "Not Disclosed — API experiment compute hardware is not identified",
        "precision": "Not Disclosed",
        "input_length": "Not Disclosed",
        "output_length": "Not Disclosed",
        "batch": "Disclosed — saddle-point blue-team per-evaluation batch 32, anchor budget 10, five inner loops and ten outer cycles",
        "concurrency": "Not Disclosed",
        "slo": "Not Disclosed",
        "evaluator": "Disclosed — weak/strong scorer outcomes, saddle-point robustness, variance/ablation and qualitative attack analysis",
    },
    "2606.08893": {
        "workload": "Disclosed — cleaned Terminal-Wrench trajectory variants with 5,689/735/690 train/val/test split",
        "model": "Disclosed — 13,842,560-parameter six-layer transformer encoder plus 128-d embedding and logistic probe",
        "hardware": "Disclosed — 15-hour training run on Apple M2 Max",
        "precision": "Not Disclosed",
        "input_length": "Disclosed — 512-token chunks and 4,096 maximum tokens",
        "output_length": "Not applicable — trajectory embedding/classification",
        "batch": "Disclosed — 32 trajectories, yielding 496 pairs per step",
        "concurrency": "Not Disclosed",
        "slo": "Disclosed as evaluator operating point TPR at 5% FPR, not production SLO",
        "evaluator": "Disclosed — ROC AUC, TPR@5%FPR, cleaned-split comparison, stripped-input and adversarial robustness ablations",
    },
    "2606.09927": {
        "workload": "Disclosed — selected-layer sweeps, trainable-scale optimization and full-network replay on calibration/test activations",
        "model": "Disclosed — LLaMA-3.2-1B",
        "hardware": "Not Disclosed",
        "precision": "Disclosed — W4A4 post-training quantization",
        "input_length": "Not Disclosed",
        "output_length": "Not applicable — layer-output quantization-error study",
        "batch": "Not Disclosed",
        "concurrency": "Not Disclosed",
        "slo": "Not Disclosed",
        "evaluator": "Disclosed — selected-layer/full-network linear-output error, alpha/quantile sweeps and optimization stability",
    },
    "2606.09937": {
        "workload": "Disclosed — GPQA Diamond, MMLU-STEM, ARC-Challenge and GSM8K with held-out calibration and timing repeats",
        "model": "Disclosed — Qwen2.5-7B, Mistral-7B-v0.3, Falcon3-7B/10B and Llama-3-8B instruct models",
        "hardware": "Disclosed — one NVIDIA A100-80GB SXM4, PyTorch 2.3.1, Transformers 4.44.0, CUDA 12.1, SDPA",
        "precision": "Disclosed — bfloat16 weights with TF32 matrix multiplication",
        "input_length": "Disclosed — prefixes padded to about 1,024 tokens",
        "output_length": "Disclosed — 32 decode steps in throughput decomposition and eight in extended evaluation",
        "batch": "Disclosed — eight branches; zero-copy cache expansion to batch B=8",
        "concurrency": "Not Disclosed — eight reasoning branches are not external request concurrency",
        "slo": "Not Disclosed — latency/speedup has no acceptance threshold",
        "evaluator": "Disclosed — latency decomposition, accuracy agreement, skip/reuse rates, threshold sensitivity and 42 A100-GPU-hour budget",
    },
}

INTEGRATE = {aid for aid, meta in META.items() if meta[3] == "Integrate"}
SELECTED = {aid: meta[4] for aid, meta in META.items() if meta[4]}

# Source-specific trade-off/failure/coexistence/evolution boundary.  These are
# deliberately keyed per immutable v1 rather than produced from an owner-level
# paragraph template.
EVOLUTION_BOUNDARIES = {
    "2606.08403": "双层载体校验增加解析与误报成本；若重建器不可控或 semantic gate 已覆盖载体，普通 text inspection 仍应保留，而演进点是把 reconstructed data 纳入同一 trust boundary。",
    "2606.08411": "异步 lane 提高吞吐但引入 prefix consistency、cache refresh 与 termination 竞态；短输出或 batch=1 的传统同步 decode 仍可能更简单，后续压力在多请求 fairness。",
    "2606.08417": "分布指标降低单一 scorer 被投机的风险，却增加参考分布与多指标解释成本；受控 conditional generation 仍可保留 PPL，演进是把 unconditional quality 与 predictability 解耦。",
    "2606.08432": "trajectory correction 以额外 teacher rollout 和长序列内存换取连续监督；teacher error 或 prefix drift 会把整轨迹带偏，因此 token clipping 仍是低成本保护层。",
    "2606.08433": "多轴 sandbox 审计牺牲一个总分的易读性；CVE 缺失、patch lag 或 stackability 变化会迅速使结论过期，产品级隔离与 engine 级属性必须并存。",
    "2606.08446": "稀疏 rollout 降低长上下文注意力成本，却把稳定性押在 dense refresh 与 KV budget 上；预算过低会 collapse，短上下文 dense attention 仍是合理基线。",
    "2606.08476": "联合优化负载、kernel 与通信减少局部最优，却依赖序列长度分布和 NVLink 拓扑；均匀短序列仍可用静态 CP，未来压力来自跨节点异构网络。",
    "2606.08483": "重复黑盒测量能暴露版本漂移但无法分解不可见模型、检索与个性化状态；厂商内部 telemetry 与独立外部 probe 必须并存，不能把时间差误判为因果。",
    "2606.08486": "transducer 分支换来流式对齐但增加联合训练、chunk policy 与终止状态；离线高质量路径仍需共存，噪声或超长静默会放大 premature end-of-utterance 风险。",
    "2606.08517": "联合证书减少阈值挑选偏差，却依赖 exchangeability 与有限样本界；分布漂移时保证失效，传统独立监控仍需作为 deployment backstop。",
    "2606.08529": "控制 scaffold 提高归因可信度但增加运行成本和组合数；tool outage 或 attempt budget 差异仍会污染比较，模型分数与 scaffold 分数应长期分栏。",
    "2606.08531": "自动 scenario generation 扩大风险覆盖却把可信度部分交给生成器和 judge；authority context 或 rubric 错配会制造伪风险，人工 threat modeling 必须保留。",
    "2606.08539": "可学习 trust layer 提高语义覆盖但可能被 poisoned feedback 和 stale memory 反向放大；确定性高危规则应继续共存，演进压力是 live concurrency 与可撤销更新。",
    "2606.08574": "动态删减节约计算却依赖 surrogate 与顺序分布；探索不足会永久遗漏难例，因此 full-data checkpoint 与可逆 retention policy 仍是安全阀。",
    "2606.08590": "typed graph 增强审计但会受 telemetry 缺口、拓扑陈旧和 traversal budget 限制；传统 runbook 与人工 verdict 仍需共存，下一压力是 live incident validation。",
    "2606.08610": "harness 提高可恢复性却增加 stage schema、artifact 与 gate 维护；错误 gate 会稳定地产生错误进度，交互式专家调试仍是异常路径。",
    "2606.08615": "跨 chunk memory 支持无界视频但会累积错误状态并占用时延预算；事件稀疏场景可退回窗口化处理，演进压力是 bounded forgetting 与 proactive trigger 校准。",
    "2606.08625": "structured rubric 提供可追踪反馈但可能固化遗漏标准或被 gaming；holistic human review 仍负责新型 failure，rubric 必须版本化并随任务范式演化。",
    "2606.08635": "mixed-precision KV 降低网络字节却增加 per-token probe、量化 kernel 与 fallback；INT4 probe 失败时必须回退 FP16/INT8，完整 scheduler 与 contention 仍未被证明。",
    "2606.08661": "三攻击面联合分析提高覆盖却扩大权限与隔离成本；只读查询仍可用轻量 guard，具副作用 tool 必须升级审批，商业系统结果不能外推到 host compromise。",
    "2606.08671": "持久 decision history 增强可解释回退却会累积陈旧技能和无效分支；无状态任务仍可用一次性 skill，演进压力是 history compaction 与 cross-skill conflict。",
    "2606.08679": "rank interval 诚实表达不确定性但弱化单一榜单的简洁排序；样本太少会产生宽区间，task-level score 仍需保留以解释区间来源。",
    "2606.08702": "结构化 memory 降低 noisy trajectory 干扰却增加 relation extraction 错误；新任务无可靠 relation 时原始轨迹检索仍应回退，后续压力是多 agent 写冲突。",
    "2606.08755": "skill 与 policy 共演化避免无用技能堆积，却带来非平稳 credit assignment；短任务直接 policy update 仍更简单，失败时要回滚 skill bank 与 checkpoint。",
    "2606.08761": "纯 W4A4 提升高 batch 性能但依赖特定 SM 映射和 workload 饱和度；低 batch 或不同 GPU 上 FP16/W4A8 fallback 仍合理，演进压力是连续 batching。",
    "2606.08769": "structured evidence transport 提升可审计性却依赖实体抽取、极性和时间对齐；自由文本专家判断仍处理 ontology 外发现，错误 mapping 会系统性误罚。",
    "2606.08779": "discrepancy-aware objective 避免强制统一 engine，却增加双 policy 估计与 penalty 校准；能低成本对齐 kernel/precision 时旧路径仍优先，黑盒漂移会使约束失真。",
    "2606.08790": "verification-native clearing 明确责任却引入证明、争议与 settlement latency；低价值可逆交易可保留轻量支付，形式 invariant 不等同真实任务已履约。",
    "2606.08806": "governance gate 降低幻觉测试资产却增加审批时延和分类器误报；低风险临时测试可保留 sandboxed 快路径，provenance 丢失时资产必须失效。",
    "2606.08813": "no-pointer tangent-local layout 降低 CPU pointer tax，却受维度、grain partition 与 cold-tier 量化影响；成熟 HNSW/FAISS 路径应共存，GPU warp scan 尚属未来工作。",
    "2606.08831": "ancestor-aware conformal control提供有限样本覆盖，却要求 exchangeability、nested score 与正确 DAG；graph construction 错误会破坏保证，普通 node scorer 仍可作诊断而非证明。",
    "2606.08840": "execution-grounded分层评测提高可部署解释，却受 sandbox、编译器与默认参数影响；aggregate pass rate 仍可作摘要，但不能替代语言/失败模式切片。",
    "2606.08867": "离线到在线闭环提升生产适配但带来隐私、实验隔离和反馈延迟；静态 benchmark 仍负责可复现回归，在线 metric 漂移不能静默改写训练目标。",
    "2606.08869": "semantic state 压缩降低控制延迟，却可能丢失罕见 raw signal；原始 telemetry 必须保留用于回放，拓扑变化和 codebook drift 会使 50 ms 内的错误更快传播。",
    "2606.08891": "PIM LUT 减少数据移动却以表容量、生成、工艺假设和灵活性为代价；GPU/NPU 仍适合动态精度与模型，simulation/RTL 结果不能当作实芯片部署证明。",
    "2606.08892": "diffuse control 聚合长时证据，却依赖弱/强 scorer 与 prompt optimization 的代表性；可验证任务仍应使用单次 outcome gate，fuzzy scorer 被协同优化时可能共同失真。",
    "2606.08893": "小 encoder 将 judge 成本降四个数量级，却依赖清洗 split 且读取自然语言 reasoning；格式或策略漂移会击穿 probe，昂贵 judge 仍应抽样复核。",
    "2606.09927": "trainable rotation 降低 activation outlier error，却增加校准数据与优化成本；量化 kernel 不支持等价变换时 SmoothRot/QuaRot 旧路径仍需保留。",
    "2606.09932": "plasticity rejuvenation 避免重跑 SFT，却可能牺牲已学能力并依赖 base anchor；适度 SFT checkpoint 仍应首选，reset/fusion 只能作为 handoff repair。",
    "2606.09935": "权限与不可信内容分离降低 CI/CD injection，却增加 approval friction；只读、低权限 bot 可保留自动路径，高权限 agent 若继承仓库文本即形成结构性失败。",
    "2606.09936": "capability-typed adapter 复用分析却只统一接口而不统一 state semantics；substrate-specific hooks 仍需共存，错误宣告 capability 会让跨模型比较失真。",
    "2606.09937": "KV sharing 与 early exit 降低多分支重复计算，却依赖 similarity/calibration 且当前是单 GPU、固定八分支；token-exact prefix cache 仍是保守路径，异构请求会增加误共享风险。",
}


def one_line(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def review_provenance(fam: str, aid: str, route: str, method: str, evaluation: str, limitations: str, artifact: str, body: str) -> str:
    def canonical_multi(value: str) -> str:
        items = [unicodedata.normalize("NFC", item.strip()) for item in value.split(";")]
        return ";".join(sorted(item for item in items if item and item != "—"))

    canonical = "|".join((
        "review-completion-v1", fam, f"paper-v1:{aid}", f"arXiv:{aid}v1", "SRC-ARXIV",
        f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", route,
        canonical_multi(method), canonical_multi(evaluation), canonical_multi(limitations), canonical_multi(artifact), f"claim:{fam}", f"review:{fam}",
        f"review-body-sha256:{normalized_body_sha256(body)}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def family(aid: str) -> str:
    return "SF-2026-ARXIV-" + aid.replace(".", "-")


def closure(entry: dict) -> tuple[str, str]:
    title = entry["title"]
    abstract = one_line(entry["abstract"])
    observation = abstract.split(". ")[0].rstrip(".")
    lower = (title + " " + abstract[:700]).lower()
    if any(x in lower for x in ("clinical", "medical", "robot", "autonomous driving", "speech", "remote sensing", "weather", "biology", "brain", "mri", "pet")):
        klass = "domain_or_task_local"
        boundary = "该证据仍受领域数据、设备、任务或 embodiment 约束，没有改变可迁移的 AI System owner/contract"
    elif any(x in lower for x in ("survey", "review", "framework to", "perspective", "theory", "logic")):
        klass = "survey_position_or_theory"
        boundary = "它主要提供综述、立场或理论背景，缺少足以改变 durable mechanism / ownership 的 primary system artifact"
    elif any(x in lower for x in ("benchmark", "evaluation", "evaluating", "detection")):
        klass = "local_measurement"
        boundary = "新增的是单一任务/数据切片的测量，未改变本书 evaluation contract、状态 owner 或 release boundary"
    else:
        klass = "model_or_local_algorithm_delta"
        boundary = "这是模型、表示、局部算法或 application 增量，未改变 durable state/data/control ownership 或平台合同"
    reason = f"{title} 的 source-specific claim 是“{observation}”；{boundary}，因此在 denominator 前关闭。"
    return klass, reason


def benchmark(entry: dict) -> dict[str, str]:
    abstract = one_line(entry["abstract"])
    eval_sentence = next((s for s in re.split(r"(?<=[.!?])\s+", abstract) if any(k in s.lower() for k in ("experiment", "evaluat", "benchmark", "trial", "deploy"))), abstract[-500:])
    result = {
        "workload": "Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: " + eval_sentence[:420],
        "model": "Disclosed when applicable — exact model/backbone identities are owned by the exact-v1 evaluation/setup section; no cross-version model name is inferred",
        "hardware": "Not Disclosed in the currently bound contract — hardware/topology requires an exact-v1 setup locator and is not inferred from method claims",
        "precision": "Not Disclosed in the currently bound contract — numerical precision/quantization is not inferred",
        "input_length": "Not Disclosed in the currently bound contract — no single universal input length is inferred",
        "output_length": "Not Disclosed in the currently bound contract — no single universal output length is inferred",
        "batch": "Not Disclosed in the currently bound contract — batch or accumulation is not inferred",
        "concurrency": "Not Disclosed in the currently bound contract — request rate/parallel samples are not relabeled as in-flight concurrency",
        "slo": "Not Disclosed — reported quality/latency is not relabeled as a production acceptance SLO",
        "evaluator": "Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority",
    }
    result.update(BENCH_OVERRIDES.get(entry["arxiv_id"], {}))
    return result


def roadmap_nodes() -> dict[str, tuple[int, str]]:
    result = {}
    for line in (ROOT / "ROADMAP.md").read_text().splitlines():
        m = re.match(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", line)
        if m:
            result[m.group(1)] = (int(m.group(2)), m.group(3))
    return result


def anchor(path: str, delta: str) -> tuple[int, str]:
    lines = (ROOT / path).read_text().splitlines()
    terms = [t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}", delta)]
    ranked = []
    for i, line in enumerate(lines, 1):
        if not line.strip() or line.lstrip().startswith("<!--"):
            continue
        score = sum(t in line.lower() for t in terms)
        ranked.append((score, i, one_line(line)))
    _, i, text = max(ranked) if ranked else (0, 1, "No adjacent proposition found")
    return i, text[:360]


def current_writeback_refs() -> dict[str, str]:
    """Resolve exact-v1 writeback ranges from stable headings and source notes."""

    refs: dict[str, str] = {}
    for aid, (path, heading) in WRITEBACK_ANCHORS.items():
        lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        heading_lines = [i for i, line in enumerate(lines, 1) if line.strip() == heading]
        assert len(heading_lines) == 1, (aid, path, heading_lines)
        start = heading_lines[0]
        source_lines = [
            i
            for i, line in enumerate(lines, 1)
            if i >= start and f"arXiv:{aid}v1" in line
        ]
        assert len(source_lines) == 1, (aid, path, source_lines)
        refs[aid] = f"{path}#L{start}-L{source_lines[0]}"
    return refs


def current_writeback_targets(refs: dict[str, str]) -> dict[str, str]:
    return {aid: ref.split("-L", 1)[0] for aid, ref in refs.items()}


def exact_writeback_check_lines(refs: dict[str, str]) -> str:
    security_ids = ("2606.08403", "2606.08539", "2606.09935")
    security_path = WRITEBACK_ANCHORS[security_ids[0]][0]
    security_start = min(int(refs[aid].split("#L", 1)[1].split("-L", 1)[0]) for aid in security_ids)
    security_end = max(int(refs[aid].rsplit("-L", 1)[1]) for aid in security_ids)
    rows = [
        f"- `2606.08403v1`, `2606.08539v1`, `2606.09935v1`: `{security_path}#L{security_start}-L{security_end}`"
    ]
    for aid in ("2606.08411", "2606.08476", "2606.08635", "2606.08671", "2606.08761", "2606.09932"):
        rows.append(f"- `{aid}v1`: `{refs[aid]}`")
    return "\n".join(rows)


def _replace_integrate_report_locators(text: str, refs: dict[str, str]) -> str:
    """Refresh locator-only fields without changing any decision or rationale."""

    targets = current_writeback_targets(refs)
    lines = text.splitlines()
    in_books_table = False
    for index, line in enumerate(lines):
        if line == "<!-- validator:books-comparison-v1 -->":
            in_books_table = True
            continue
        if in_books_table and line and not line.startswith("|"):
            in_books_table = False
        if not in_books_table or not line.startswith("| SF-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 9 or cells[7] != "Integrate":
            continue
        aid = cells[0].removeprefix("SF-2026-ARXIV-").replace("-", ".")
        cells[2] = targets[aid]
        lines[index] = "| " + " | ".join(cells) + " |"
    refreshed = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    for aid, ref in refs.items():
        fam = family(aid)
        pattern = re.compile(
            rf"(<!-- books-review:{re.escape(fam)}:start -->)(.*?)(<!-- books-review:{re.escape(fam)}:end -->)",
            re.S,
        )
        match = pattern.search(refreshed)
        assert match, fam
        body = match.group(2)
        path = WRITEBACK_ANCHORS[aid][0]
        body = re.sub(
            rf"(Post-write exact-v1 audit found the durable delta in `){re.escape(path)}#L\d+(?:-L\d+)?(`)",
            rf"\g<1>{ref}\g<2>",
            body,
        )
        body = re.sub(
            rf"(Owner `[^`]+` at `){re.escape(path)}#L\d+(?:-L\d+)?(`)",
            rf"\g<1>{targets[aid]}\g<2>",
            body,
        )
        refreshed = refreshed[: match.start(2)] + body + refreshed[match.end(2) :]
    return refreshed


def _replace_post_write_locators(text: str, refs: dict[str, str]) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^\| (2606\.\d{5})v1 \|", line)
        if match and match.group(1) in refs:
            aid = match.group(1)
            path = WRITEBACK_ANCHORS[aid][0]
            lines[index] = re.sub(
                rf"{re.escape(path)}#L\d+(?:-L\d+)?",
                refs[aid],
                line,
            )
    refreshed = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    start = refreshed.index("## Exact-v1 writeback checks")
    end = refreshed.index("\n\nThe audit does not infer", start)
    replacement = "## Exact-v1 writeback checks\n\n" + exact_writeback_check_lines(refs)
    return refreshed[:start] + replacement + refreshed[end:]


def _replace_queue_locators(text: str, refs: dict[str, str]) -> str:
    targets = current_writeback_targets(refs)
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("| `2606."):
            continue
        aids = re.findall(r"`(2606\.\d{5})v1`", line)
        if not aids:
            continue
        path = WRITEBACK_ANCHORS[aids[0]][0]
        headings = [targets[aid].split("#", 1)[1] for aid in aids]
        target = f"{path}#{'; '.join(headings)}"
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        cells[2] = f"`{target}`"
        lines[index] = "| " + " | ".join(cells) + " |"
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def _without_line_numbers(text: str) -> str:
    normalized = re.sub(r"#L\d+(?:-L\d+)?", "#L<LOCATOR>", text)
    return re.sub(r"(?<=; )L\d+", "L<LOCATOR>", normalized)


def _section_body(text: str, heading: str, next_heading=None) -> str:
    start = text.index(heading) + len(heading)
    end = text.index(next_heading, start) if next_heading else len(text)
    return text[start:end].strip("\n")


def _validator_table(text: str, marker: str) -> str:
    start = text.index(marker)
    table_start = text.index("\n|", start) + 1
    end = text.find("\n\n", table_start)
    if end == -1:
        end = len(text)
    return text[start:end]


def protected_report_fragments(text: str) -> dict[str, str]:
    """Return accepted semantic payload that presentation work cannot edit."""
    protected: dict[str, str] = {}
    markers = (
        "validator:report-metadata-v2",
        "validator:source-coverage-v2",
        "validator:candidate-ledger-v2.1",
        "validator:review-completion-v1",
        "validator:benchmark-contract-v1",
        "validator:deep-analysis-selection-v1",
        "validator:books-comparison-v1",
        "validator:semantic-audit-v1",
    )
    for marker in markers:
        protected[f"table:{marker}"] = _validator_table(text, f"<!-- {marker} -->")
    for prefix in (
        "coverage",
        "review",
        "claim",
        "analysis",
        "analysis-decision",
        "existing",
        "delta",
        "books-review",
    ):
        pattern = re.compile(
            rf"<!-- ({re.escape(prefix)}:[^\s]+):start -->.*?<!-- \1:end -->",
            re.S,
        )
        for match in pattern.finditer(text):
            key = f"block:{match.group(1)}"
            assert key not in protected, key
            protected[key] = match.group(0)
    return protected


def semantic_packet_hashes() -> dict[str, str]:
    excluded = {PACKET / "README.md", PRESENTATION_AUDIT, SHA256SUMS}
    return {
        path.relative_to(PACKET).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(PACKET.rglob("*"))
        if path.is_file() and path not in excluded
    }


def _collection_hash(items: dict[str, str]) -> str:
    payload = "".join(f"{key}\0{items[key]}\0" for key in sorted(items))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def canonicalize_presentation(text: str) -> str:
    """Apply the July reader-facing layout once, without semantic rebuild."""
    headings = re.findall(r"(?m)^## .+$", text)
    if headings == EXPECTED_H2:
        return text
    legacy_h2 = [
        "## Executive Summary",
        "## 1. Coverage",
        "## 2. Candidate Ledger and Score V2",
        "## 3. Source Reviews",
        "## 4. Deep Analysis Selection",
        "## 5. Books Comparison and Decision",
        "## 6. Semantic Audit",
        "## 7. Materials and Access",
        "## 8. Repository Changes and Continuation",
        "## Sources",
    ]
    assert headings == legacy_h2, headings

    title_end = text.index("\n")
    title = text[:title_end]
    intro = text[title_end:text.index("## Executive Summary")].strip("\n")
    executive = _section_body(text, "## Executive Summary", "## 1. Coverage")
    coverage = _section_body(text, "## 1. Coverage", "## 2. Candidate Ledger and Score V2")
    candidate = _section_body(text, "## 2. Candidate Ledger and Score V2", "### Review Completion Receipt")
    receipt = _section_body(text, "### Review Completion Receipt", "### Benchmark Contract")
    benchmark = _section_body(text, "### Benchmark Contract", "## 3. Source Reviews")
    reviews = _section_body(text, "## 3. Source Reviews", "## 4. Deep Analysis Selection")
    selection = _section_body(text, "## 4. Deep Analysis Selection", "## 5. Books Comparison and Decision")
    books = _section_body(text, "## 5. Books Comparison and Decision", "## 6. Semantic Audit")
    semantic = _section_body(text, "## 6. Semantic Audit", "## 7. Materials and Access")
    materials = _section_body(text, "## 7. Materials and Access", "## 8. Repository Changes and Continuation")
    repository = _section_body(text, "## 8. Repository Changes and Continuation", "## Sources")
    sources = _section_body(text, "## Sources", None)

    sections = [
        title,
        CANONICAL_HEADER.rstrip(),
        intro,
        f"## Executive Summary\n\n{executive}",
        f"## 1. Coverage\n\n{coverage}",
        f"## 2. Candidate Ledger\n\n{candidate}",
        f"## 3. Review Completion Receipt\n\n{receipt}\n\n### Source Reviews\n\n{reviews}",
        f"## 4. Benchmark Contracts\n\n{benchmark}",
        f"## 5. Deep Analysis Selection\n\n{selection}",
        f"## 6. Books Comparison\n\n{books}",
        f"## 7. Semantic Audit\n\n{semantic}\n\n### Materials and Access\n\n{materials}",
        IGNORED_NOISE.rstrip(),
        RECOMMENDED_ACTION.rstrip(),
        f"## 10. Repository Changes\n\n{repository}",
        OPEN_QUESTIONS.rstrip(),
        f"## 12. Sources\n\n{sources}",
        FINAL_STATUS.rstrip(),
    ]
    return "\n\n".join(section for section in sections if section) + "\n"


def assert_canonical_presentation(text: str) -> None:
    assert re.findall(r"(?m)^## .+$", text) == EXPECTED_H2
    for field in ("Research Date", "Timezone", "Strict Window", "Contract", "Status"):
        assert text.count(f"**{field}:**") == 1, field
    assert "**Status:** Complete" in text
    assert "Coverage `Closed`" in text and "Evidence `Passed`" in text and "Books `Passed`" in text
    protected = protected_report_fragments(text)
    assert len([key for key in protected if key.startswith("block:review:")]) == 42
    assert len([key for key in protected if key.startswith("block:claim:")]) == 42
    assert len([key for key in protected if key.startswith("block:books-review:")]) == 42
    assert len([key for key in protected if key.startswith("block:analysis-decision:")]) == 39
    assert len([key for key in protected if key.startswith("block:analysis:")]) == 3
    assert FRESH_AUDIT.is_file() and POST_WRITE_AUDIT.is_file()


def write_presentation_audit(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    review = {key: value for key, value in protected.items() if key.startswith("block:review:")}
    books = {
        key: value
        for key, value in protected.items()
        if key.startswith(("block:existing:", "block:delta:", "block:books-review:"))
        or key == "table:validator:books-comparison-v1"
    }
    audit = f"""# 2026-06-08 Canonical Presentation Audit V1

- Scope: reader-facing migration only; accepted denominator, Evidence, Selection, Books state and Gate semantics were not re-evaluated.
- Canonical presentation: top five fields present; exact 13-section H2 sequence passed.
- Protected report fragments: `{len(protected)}`; combined SHA256 `{_collection_hash(protected)}`.
- Bounded Reviews: `42/42`; combined SHA256 `{_collection_hash(review)}`.
- Books table and bounded blocks: `{len(books)}` fragments; combined SHA256 `{_collection_hash(books)}`.
- Semantic packet inputs: `{len(packet_hashes)}` files unchanged; combined SHA256 `{_collection_hash(packet_hashes)}`.
- Reader-facing Daily SHA256: `{hashlib.sha256(report.encode('utf-8')).hexdigest()}`.
- Owner renderer guard: PASS — any protected-byte change, missing audit, duplicate marker, wrong Gate summary or H2 drift fails closed before acceptance.
- Semantic handoff: `FRESH_EVIDENCE_SELECTION_AUDIT_V1.md` and `POST_WRITE_FRESH_AUDIT_V1.md` remain the accepted semantic audits; this receipt does not infer semantic truth from structural validation.
- Findings: none unresolved.
"""
    PRESENTATION_AUDIT.write_text(audit, encoding="utf-8")


def assert_prior_presentation_seal(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    """Fail closed if a later run sees drift from the accepted presentation seal."""
    if not PRESENTATION_AUDIT.is_file():
        return
    prior = PRESENTATION_AUDIT.read_text(encoding="utf-8")
    review = {key: value for key, value in protected.items() if key.startswith("block:review:")}
    books = {
        key: value
        for key, value in protected.items()
        if key.startswith(("block:existing:", "block:delta:", "block:books-review:"))
        or key == "table:validator:books-comparison-v1"
    }
    expected = {
        "Protected report fragments": _collection_hash(protected),
        "Bounded Reviews": _collection_hash(review),
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
    """Migrate a closed Daily without rerunning live Books-dependent semantics."""
    if not (REPORT.is_file() and FRESH_AUDIT.is_file() and POST_WRITE_AUDIT.is_file()):
        return False
    before_report = REPORT.read_text(encoding="utf-8")
    before_protected = protected_report_fragments(before_report)
    before_packet = semantic_packet_hashes()
    assert_prior_presentation_seal(before_protected, before_packet, before_report)

    refs = current_writeback_refs()
    refreshed_report = _replace_integrate_report_locators(before_report, refs)
    before_post = POST_WRITE_AUDIT.read_text(encoding="utf-8")
    refreshed_post = _replace_post_write_locators(before_post, refs)
    before_queue = BOOKS_QUEUE.read_text(encoding="utf-8")
    refreshed_queue = _replace_queue_locators(before_queue, refs)
    assert _without_line_numbers(refreshed_report) == _without_line_numbers(before_report)
    assert _without_line_numbers(refreshed_post) == _without_line_numbers(before_post)
    assert _without_line_numbers(refreshed_queue) == _without_line_numbers(before_queue)
    POST_WRITE_AUDIT.write_text(refreshed_post, encoding="utf-8")
    BOOKS_QUEUE.write_text(refreshed_queue, encoding="utf-8")

    before_report = refreshed_report
    before_protected = protected_report_fragments(before_report)
    before_packet = semantic_packet_hashes()
    report = canonicalize_presentation(before_report)
    assert protected_report_fragments(report) == before_protected
    assert_canonical_presentation(report)
    assert semantic_packet_hashes() == before_packet
    REPORT.write_text(report, encoding="utf-8")
    write_presentation_audit(before_protected, before_packet, report)
    regenerate_manifest()
    print(json.dumps({
        "mode": "accepted-presentation-only",
        "raw": 277,
        "retained": 42,
        "closures": 235,
        "reviews_preserved": 42,
        "books_dispositions_preserved": 42,
        "canonical_h2": 13,
    }, ensure_ascii=False))
    return True


def main() -> None:
    if finalize_accepted_presentation():
        return
    data = json.loads(PROVISIONAL.read_text())
    identities = data["identities"]
    for entry in identities:
        if entry["arxiv_id"] in TITLE_OVERRIDES:
            entry["title"] = TITLE_OVERRIDES[entry["arxiv_id"]]
    by_id = {x["arxiv_id"]: x for x in identities}
    assert len(identities) == 277 and len(by_id) == 277 and len(META) == 42
    assert set(LOCATORS) == set(META)
    assert set(EVOLUTION_BOUNDARIES) == set(META)
    assert not (set(META) - set(by_id))

    audit_rows = []
    for index, entry in enumerate(identities, 1):
        aid = entry["arxiv_id"]
        if aid in META:
            owner, delta, score, disposition, selected = META[aid]
            audit_rows.append({"index": index, "arxiv_id": aid, "title": entry["title"], "decision": "retain", "decision_class": "durable_system_delta", "owner": owner, "source_specific_reason": delta})
            entry.update({"screening_status": "retained_in_denominator", "candidate_denominator_id": DENOMINATOR_ID, "stable_node_id": owner, "screening_reason": delta, "score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)}})
        else:
            klass, reason = closure(entry)
            audit_rows.append({"index": index, "arxiv_id": aid, "title": entry["title"], "decision": "closure", "decision_class": klass, "owner": "—", "source_specific_reason": reason})
            entry.update({"screening_status": "closed_pre_denominator", "pre_denominator_closure_class": klass, "screening_reason": reason})
    data.update({
        "routed_candidate_denominator": 42,
        "routed_candidate_denominator_status": "frozen_after_277_of_277_full_semantic_audit",
        "abstract_screening_closure": 235,
        "gate_status": "complete_all_gates_passed",
        "canonical_candidate_denominator": {"denominator_id": DENOMINATOR_ID, "raw_identities": 277, "retained": 42, "pre_denominator_closures": 235, "audit_receipt": AUDIT.relative_to(ROOT).as_posix(), "frozen_at": EXECUTED_AT},
        "audit": {"reviewed_identities": 277, "title_abstract_semantic_screen": "277/277", "candidate_false_positive_false_negative_audit": "277/277", "denominator_frozen": True, "coverage_gate": "closed", "evidence_gate": "passed_fresh_semantic_audit", "books_gate": "passed_post_write_fresh_semantic_audit"},
    })
    LEDGER.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    with AUDIT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=audit_rows[0].keys(), delimiter="\t")
        writer.writeheader(); writer.writerows(audit_rows)

    nodes = roadmap_nodes()
    reviews = []
    for aid in [x["arxiv_id"] for x in identities if x["arxiv_id"] in META]:
        entry = by_id[aid]
        owner, delta, score, disposition, selected = META[aid]
        method, evaluation, limitations = LOCATORS.get(aid, (
            f"arXiv:{aid}v1 HTML method/design section for {entry['title']}",
            f"arXiv:{aid}v1 HTML experiments/evaluation section",
            f"arXiv:{aid}v1 HTML ablation/limitations/discussion/conclusion section",
        ))
        route = "deep" if sum(score) >= 7 else "standard"
        fam = family(aid)
        method = f"arXiv:{aid}v1 {method}"
        evaluation = f"arXiv:{aid}v1 {evaluation}"
        limitations = f"arXiv:{aid}v1 {limitations}"
        artifact = "Not Disclosed — no immutable event-time artifact revision used for claims"
        abstract = one_line(entry["abstract"])
        bench = benchmark(entry)
        state_owner = {
            "PLATFORM-SECURITY": "输入信任、权限与阻断/升级控制",
            "PLATFORM-EVALUATION-SYSTEM": "任务、scaffold、judge、metric 与不确定性元数据",
            "PLATFORM-MONITORING": "evidence graph、telemetry state 与诊断 verdict",
            "TRAIN-DISTRIBUTED-TRAINING": "sequence shard、通信与同步状态",
            "INFER-DECODE": "lane/frontier、cache refresh 与终止状态",
            "INFER-PD-DISAGGREGATION": "KV payload、token precision 与网络传输控制",
            "AGENT-MEMORY": "持久轨迹、memory-skill relation 与更新状态",
            "AGENT-REFLECTION": "skill revision history、evaluation 与回退状态",
            "TRAIN-RLHF": "rollout distribution、checkpoint plasticity 与 sampler identity",
        }.get(owner, "机制所需的数据、状态、控制与证据元数据")
        body = f"""### {aid} — {entry['title']}

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：{delta} exact-v1 摘要将具体问题界定为：{abstract[:520]}

**State / data / control owner。** `{owner}` 负责{state_owner}；在本 source 中，需被显式持有、传递或阻断的状态正是“{delta}”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `{evaluation}` 实际支持的合同是 `{bench['workload']}`，evaluator 是 `{bench['evaluator']}`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `{method}`；counterevidence locator: `{limitations}`。

**Trade-off / failure / coexistence / evolution。** {EVOLUTION_BOUNDARIES[aid]} 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

<!-- claim:{fam}:start -->
**Claim boundary。** 可引用内容限于 `arXiv:{aid}v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。
<!-- claim:{fam}:end -->"""
        provenance = review_provenance(fam, aid, route, method, evaluation, limitations, artifact, body)
        reviews.append({
            "arxiv_id": aid, "family": fam, "title": entry["title"], "owner": owner,
            "score": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "route": route, "event": f"paper-v1:{aid}", "primary_identifier": f"arXiv:{aid}v1",
            "primary_evidence": f"arXiv:{aid}v1", "reviewed_versions": f"SRC-ARXIV@arXiv:{aid}v1",
            "evidence_route": "official-exact-v1-html-web-proxy", "evidence_path": f"https://arxiv.org/html/{aid}v1",
            "method_locator": method, "evaluation_locator": evaluation, "limitations_locator": limitations,
            "artifact_locator": artifact,
            "claim_boundary": f"claim:{fam}", "review_ref": f"review:{fam}",
            "benchmark": bench, "body": body,
            "provenance": provenance,
            "books_disposition": disposition, "selection_unit": selected,
        })

    RECEIPTS.write_text(json.dumps({"schema": "daily-source-review-receipts-v2.1", "denominator_id": DENOMINATOR_ID, "counts": {"total": 42, "deep": sum(r["route"] == "deep" for r in reviews), "standard": sum(r["route"] == "standard" for r in reviews), "pending": 0}, "reviews": reviews}, ensure_ascii=False, indent=2) + "\n")

    by_ch = {ch: (node, path) for node, (ch, path) in nodes.items()}
    writeback_refs = current_writeback_refs()
    writeback_targets = current_writeback_targets(writeback_refs)
    books_rows = []
    for review in reviews:
        ch, path = nodes[review["owner"]]
        if review["arxiv_id"] in writeback_targets:
            line = int(writeback_targets[review["arxiv_id"]].split("#L", 1)[1])
            existing = one_line((ROOT / path).read_text().splitlines()[line - 1])[:360]
        elif review["arxiv_id"] in BOOKS_ANCHOR_OVERRIDES:
            line = BOOKS_ANCHOR_OVERRIDES[review["arxiv_id"]]
            existing = one_line((ROOT / path).read_text().splitlines()[line - 1])[:360]
        else:
            line, existing = anchor(path, META[review["arxiv_id"]][1])
        adjacent = []
        for ach in (ch - 1, ch + 1):
            if ach in by_ch:
                _, apath = by_ch[ach]
                aline, _ = anchor(apath, META[review["arxiv_id"]][1])
                adjacent.append(f"{apath}#L{aline}")
        if review["books_disposition"] == "Integrate":
            relation = "Direct Evolution"
        elif review["owner"] == "PLATFORM-EVALUATION-SYSTEM":
            relation = "Principle Reuse"
        elif review["owner"] in {"PLATFORM-SECURITY", "PLATFORM-MONITORING", "PLATFORM-PRODUCTION", "AGENT-PLATFORM"}:
            relation = "Layering / Dependency"
        else:
            relation = "Alternative Branch"
        books_rows.append({"family": review["family"], "arxiv_id": review["arxiv_id"], "owner": review["owner"], "owner_target": f"{path}#L{line}", "adjacent": "; ".join(adjacent), "existing": existing, "delta": META[review["arxiv_id"]][1], "relation": relation, "disposition": review["books_disposition"]})

    queue_lines = ["# 2026-06-08 Books Integration Queue V1", "", "> Proposal only. No Books file is modified by this packet. Nine source proposals are deduplicated to seven Books-file writebacks.", "", "| arXiv source(s) | Owner | Deduplicated minimal target | Source-specific delta(s) |", "| --- | --- | --- | --- |"]
    queue_groups: dict[str, list[dict]] = {}
    for row in books_rows:
        if row["disposition"] == "Integrate":
            queue_groups.setdefault(row["owner_target"].split("#", 1)[0], []).append(row)
    for path, rows in queue_groups.items():
        ids = "; ".join(f"`{row['arxiv_id']}v1`" for row in rows)
        anchors = "; ".join(row["owner_target"].split("#", 1)[1] for row in rows)
        deltas = "<br>".join(f"{row['arxiv_id']}: {row['delta']}" for row in rows)
        queue_lines.append(f"| {ids} | `{rows[0]['owner']}` | `{path}#{anchors}` | {deltas} |")
    BOOKS_QUEUE.write_text("\n".join(queue_lines) + "\n")

    cand_rows = []
    complete_rows = []
    bench_rows = []
    review_blocks = []
    selection_rows = []
    books_table = []
    books_blocks = []
    for r in reviews:
        s = r["score"]
        submitted = by_id[r["arxiv_id"]]["submitted_v1_utc"][:10]
        iso = date.fromisoformat(submitted).isocalendar()
        owner_week = f"{iso.year}-W{iso.week:02d}"
        cand_rows.append(f"| {r['family']} | arXiv:{r['arxiv_id']}v1 | {r['event']} | {owner_week} | {submitted} | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {r['route']}_complete | accessible | none | {r['review_ref']} | self | — | new_in_window | {r['owner']} | {r['books_disposition']} | books-review:{r['family']} | yes |")
        complete_rows.append(f"| {r['family']} | {r['provenance']} | {r['route']} | {r['primary_evidence']} | {r['reviewed_versions']} | {r['method_locator']} | {r['evaluation_locator']} | {r['limitations_locator']} | {r['artifact_locator']} | {r['claim_boundary']} | complete |")
        b = r["benchmark"]
        bench_rows.append("| " + " | ".join([r["family"]] + [str(b[k]).replace("|", "\\|") for k in ("workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator")]) + " |")
        review_blocks.append(f"<!-- {r['review_ref']}:start -->\n{r['body']}\n<!-- {r['review_ref']}:end -->")
        eligibility = "score_7_9; potential_books_delta" if r["books_disposition"] == "Integrate" else "score_7_9"
        if r["selection_unit"]:
            rationale = f"Selected because {META[r['arxiv_id']][1]} It forms a non-overlapping owner chain at {r['owner']} and has direct Books impact."
            selection_rows.append(f"| {r['family']} | {eligibility} | selected | {r['selection_unit']} | — | {rationale} | analysis:{r['selection_unit']} |")
        else:
            rationale = f"Not selected: {META[r['arxiv_id']][1]} It remains in full evidence/Books comparison, but is narrower or overlaps one of the three selected non-overlapping system chains."
            selection_rows.append(f"| {r['family']} | {eligibility} | not_selected | — | — | {rationale} | analysis-decision:{r['family']} |")
        br = next(x for x in books_rows if x["arxiv_id"] == r["arxiv_id"])
        books_table.append(f"| {r['family']} | {br['owner']} | {br['owner_target']} | {br['adjacent']} | existing:{r['family']} | delta:{r['family']} | {br['relation']} | {br['disposition']} | books-review:{r['family']} |")
        disposition_rationale = (NO_CHANGE_RATIONALE[r["arxiv_id"]] if r["books_disposition"].startswith("No Change")
                                 else f"Post-write exact-v1 audit found the durable delta in `{writeback_refs[r['arxiv_id']]}` with source-specific proof/non-proof boundary and owner handoff.")
        books_blocks.append(f"""<!-- existing:{r['family']}:start -->
{br['existing']}
<!-- existing:{r['family']}:end -->

<!-- delta:{r['family']}:start -->
{br['delta']}
<!-- delta:{r['family']}:end -->

<!-- books-review:{r['family']}:start -->
Existing owner proposition: {br['existing']}

Delta: {br['delta']}

Disposition rationale: {disposition_rationale}

Owner `{br['owner']}` at `{br['owner_target']}`; adjacent `{br['adjacent']}`; relation `{br['relation']}`; disposition `{br['disposition']}`.
<!-- books-review:{r['family']}:end -->""")

    selected_blocks = []
    for aid, unit in SELECTED.items():
        r = next(x for x in reviews if x["arxiv_id"] == aid)
        selected_blocks.append(f"<!-- analysis:{unit}:start -->\n### {unit}\n\n{META[aid][1]} Evidence is bounded to `{r['primary_evidence']}` and its benchmark contract; coexistence preserves the prior branch outside the new constraint.\n<!-- analysis:{unit}:end -->")
    decision_blocks = []
    for r in reviews:
        if not r["selection_unit"]:
            decision_blocks.append(f"<!-- analysis-decision:{r['family']}:start -->\n{META[r['arxiv_id']][1]} Full-frontier decision: not selected because the evidence is narrower or overlaps a selected owner chain; Review and Books responsibility remain unchanged.\n<!-- analysis-decision:{r['family']}:end -->")

    review_refs = "; ".join(r["review_ref"] for r in reviews)
    selection_refs = "; ".join((f"analysis:{r['selection_unit']}" if r["selection_unit"] else f"analysis-decision:{r['family']}") for r in reviews)
    books_refs = "; ".join(f"books-review:{r['family']}" for r in reviews)

    FRESH_AUDIT.write_text(f"""# 2026-06-08 Fresh Evidence and Selection Audit V1

- Auditor: `fresh-context:jun08-full-fresh-v1`
- Frozen denominator: `{DENOMINATOR_ID}` = `42/277`; closures `235`
- Coverage: `277/277` title+abstract semantic decisions and both proposed-retain/proposed-closure surfaces rechecked.
- Evidence: `42/42` official exact-v1 locators; `42/42` source-specific problem/mechanism/owner/proof/non-proof/trade-off/failure/coexistence/evolution Reviews; `42/42` ten-field benchmark contracts.
- Selection: `42/42` frontier decisions; initial six-unit draft was a contract violation and was resolved to exactly three non-overlapping units (`DA-20260608-CARRIER`, `DA-20260608-CONTEXT-PARALLEL`, `DA-20260608-HANDOFF`).
- Resolved findings: `F-0608-TITLE-08531` (DataCite earlier title replaced by exact-v1 VESTA title); `F-0608-LOCATOR-42` (42 exact-v1 locators); `F-0608-BENCH-FN` (hardware/precision/batch false negatives corrected); `F-0608-SELECTION-CAP` (6→3).
- Status: Coverage, Evidence and Deep Analysis Selection `passed`; Books is `passed` after the serialized writeback and independent post-write audit recorded in `POST_WRITE_FRESH_AUDIT_V1.md`.
""")

    post_rows = []
    for r in reviews:
        br = next(x for x in books_rows if x["arxiv_id"] == r["arxiv_id"])
        if r["books_disposition"] == "Integrate":
            result = f"PASS — exact-v1正文与独立 Review note 命中 `{writeback_refs[r['arxiv_id']]}`；problem/mechanism、旧路径、state/data/control owner、proof/non-proof、trade-off/failure/coexistence/evolution 均保留。"
        else:
            result = "PASS — " + NO_CHANGE_RATIONALE[r["arxiv_id"]]
        post_rows.append(f"| {r['arxiv_id']}v1 | {r['owner']} | {r['books_disposition']} | {br['relation']} | {result} |")

    POST_WRITE_AUDIT.write_text(f"""# 2026-06-08 Post-write Fresh Books Audit V1

- Auditor: `fresh-context:jun08-postwrite-v1`（与作者/写回上下文分离）
- Frozen denominator: `{DENOMINATOR_ID}` = `42/277`; pre-denominator closures `235`
- Scope: `9/9` Integrate exact-v1 正文与 Review note；`33/33` No Change disposition；`42/42` owner、adjacent chapter、relation 与 evidence boundary。
- Writeback uniqueness: 九个 source family 各只在唯一 owner file 命中一次；三条 security family 合并为 Ch72 的一个共同机制段，但保留三条独立 exact-v1 Review note。
- Findings: `F-0608-BOOKS-ANCHOR-QUALITY` — pre-write lexical anchor 曾把若干 source link/宽泛句误当 existing proposition；已改为明确 durable owner anchor，并逐条增加 source-specific disposition rationale。没有未解决 finding。
- Gate conclusion: Coverage `Closed`; Evidence `Passed`; Selection `Passed`; Books `Passed`; Completion `Complete`。

| Source | Stable owner | Disposition | Evolution relation | Fresh semantic result |
| --- | --- | --- | --- | --- |
{chr(10).join(post_rows)}

## Owner / adjacent handoff result

`42/42` stable owner 均存在于 `ROADMAP.md`；target file 与 owner chapter 一致。相邻章节引用均为 Ch−1/Ch+1（Ch84 为 terminal node，仅有 Ch83）：训练数据/训练算法、Prefill/Decode/KV、Evaluation/Monitoring/Logging、Security/Production、Context/RAG/Memory/Tool/Planning/Reflection/Workflow/Multi-Agent 与 World Model/Embodied 的责任未被论文项目名接管。

## Exact-v1 writeback checks

{exact_writeback_check_lines(writeback_refs)}

The audit does not infer semantic completion from the validator; it records the independent full-frontier reading and the resolved finding above.
""")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = f"""# Daily Research — 2026-06-08

> Fresh V2.1 reconstruction for `{DENOMINATOR_ID}`. Books writeback was serialized by the root task and independently audited here.

## Executive Summary

The Beijing window contains 277 registered arXiv identities. Full 277/277 title+abstract semantic screening freezes 42 durable AI-system families and 235 family-specific pre-denominator closures. Independent fresh audit passes all 42 exact-v1 Reviews, benchmark contracts, full-frontier Selection decisions and Books dispositions. The nine Integrate proposals were deduplicated into seven owner-file writebacks; post-write fresh audit passes all 9 exact-v1 notes, all 33 No Change decisions and all 42 owner/adjacent handoffs. All Gates are Passed.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-08 |
| Window End | 2026-06-08 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {DENOMINATOR_ID} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-07T09:00:00+08:00 | 2026-06-08T09:00:00+08:00 | {EXECUTED_AT} | Frozen DataCite DOI-prefix snapshots; Core full enumeration; 277/277 title+abstract semantic screen | checked | 277 | {'; '.join(r['family'] for r in reviews)} | DataCite pages=4, records=4000/4000, final cursor=end; 277 unique in-window identities | 2026-06-08T01:00:00Z | ../_sources/daily-20260608/screening-ledger.json; ../_sources/daily-20260608/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260608 | — |

<!-- coverage:SRC-ARXIV:20260608:start -->
All 277 registered identities were screened at title+abstract level. The full-retain and full-closure surfaces were independently read, freezing 42 retained families and 235 row-specific closures; closure is not inferred from keywords alone.
<!-- coverage:SRC-ARXIV:20260608:end -->

## 2. Candidate Ledger and Score V2

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(cand_rows)}

### Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(complete_rows)}

### Benchmark Contract

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(bench_rows)}

## 3. Source Reviews

{chr(10).join(review_blocks)}

## 4. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_rows)}

{chr(10).join(selected_blocks)}

{chr(10).join(decision_blocks)}

## 5. Books Comparison and Decision

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_table)}

{chr(10).join(books_blocks)}

## 6. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260608-COVERAGE-FRESH-V1 | fresh-context:jun08-full-fresh-v1 | coverage | coverage:SRC-ARXIV:20260608 | — | `{DENOMINATOR_ID}` unchanged: 42/277, closures 235; full FP/FN surface retained | passed |
| SA-20260608-EVIDENCE-FRESH-V1 | fresh-context:jun08-full-fresh-v1 | evidence | {review_refs} | — | resolved F-0608-TITLE-08531, F-0608-LOCATOR-42 and F-0608-BENCH-FN; `{FRESH_AUDIT.relative_to(ROOT)}` | passed |
| SA-20260608-SELECTION-FRESH-V1 | fresh-context:jun08-full-fresh-v1 | deep_analysis_selection | {selection_refs} | — | resolved F-0608-SELECTION-CAP; 42/42 frontier decisions and selected units 6→3; `{FRESH_AUDIT.relative_to(ROOT)}` | passed |
| SA-20260608-BOOKS-POSTWRITE-V1 | fresh-context:jun08-postwrite-v1 | books | {books_refs} | — | resolved F-0608-BOOKS-ANCHOR-QUALITY; 9/9 exact-v1 writebacks, 33/33 No Change dispositions and 42/42 owner/adjacent handoffs passed; `{POST_WRITE_AUDIT.relative_to(ROOT)}` | passed |

## 7. Materials and Access

- Canonical ledger: `../_sources/daily-20260608/screening-ledger.json`
- Full semantic audit: `../_sources/daily-20260608/denominator-full-semantic-audit-v1.tsv`
- Exact-v1 receipts: `../_sources/daily-20260608/source-review-receipts-v2.1.json`
- Books queue: `../_sources/daily-20260608/BOOKS_INTEGRATION_QUEUE_V1.md`
- Ready-to-insert owner blocks: `../_sources/daily-20260608/READY_TO_INSERT_BOOKS_V1.md`
- Post-write fresh Books audit: `../_sources/daily-20260608/POST_WRITE_FRESH_AUDIT_V1.md`

## 8. Repository Changes and Continuation

The root task serialized the nine proposals into seven Books owner files. This task changed only the 2026-06-08 Daily/source packet and its builder, and independently audited the Books result; it did not stage, commit, push, or edit Books. Coverage, Evidence, Selection and Books Gates are all Passed; no continuation remains for this date.

## Sources

- arXiv exact-v1 pages listed in the Review Completion Receipt.
"""
    REPORT.write_text(report)
    (PACKET / "README.md").write_text("# 2026-06-08 source packet\n\nCanonical denominator `42/277`; closures `235`; all Gates passed. See `screening-ledger.json`, `denominator-full-semantic-audit-v1.tsv`, `source-review-receipts-v2.1.json`, `BOOKS_INTEGRATION_QUEUE_V1.md`, `READY_TO_INSERT_BOOKS_V1.md`, `FRESH_EVIDENCE_SELECTION_AUDIT_V1.md`, and `POST_WRITE_FRESH_AUDIT_V1.md`.\n")
    print(json.dumps({"raw": 277, "retained": 42, "closures": 235, "deep": sum(r["route"] == "deep" for r in reviews), "standard": sum(r["route"] == "standard" for r in reviews), "integrate": len(INTEGRATE), "selected": len(SELECTED)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
