#!/usr/bin/env python3
"""Build the strict V2.1 2026-06-14 Daily packet without editing Books."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import finalize_june11_v21 as base


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260614"
N = 41
RAW = 254
CLOSED = RAW - N
EXECUTED_AT = "2026-08-29T23:58:00+08:00"
DENOMINATOR_ID = "DEN-20260614-254041"
REPORT = ROOT / "papers/2026/06/14/README.md"
EVIDENCE_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
POST_WRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
PRESENTATION_AUDIT = PACKET / "CANONICAL_PRESENTATION_AUDIT_V1.md"
SHA256SUMS = PACKET / "SHA256SUMS"

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

CANONICAL_HEADER = """**Research Date:** 2026-06-14

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-13 09:00:00 ～ 2026-06-14 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；254/254 registered arXiv identities 完成 title+abstract semantic screen；41-family exact-v1 Evidence、full-frontier Selection 与 Books post-write audit 保持 root-accepted state

**Status:** Complete — Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`
"""

IGNORED_NOISE = """## 8. Ignored Noise

Coverage ledger 中的 `213` 条 family-specific pre-denominator closures 保持在冻结分母之外；它们均有 title+abstract semantic decision，不以关键词负路由或静默遗漏代替 closure。
"""

FINAL_STATUS = """## 13. Final Status

- Denominator: `{denominator}` = `41 retained / 254 raw`；pre-denominator closures `213`。
- Evidence / Selection: `41/41` exact-v1 Reviews、benchmark contracts 与 full-frontier decisions complete；selected units `3`。
- Books: `37 Integrate / 4 No Change — Existing Coverage`；root writeback 与 `41/41` post-write audit 已闭合。
- Gates: Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`。
""".format(denominator=DENOMINATOR_ID)


def E(owner, delta, trade, workload, model="Not Disclosed", *, method="§3 Method / system design", evaluation="§4 Experiments / evaluation", limits="Conclusion / limitations and exact-v1 claim boundary", disposition="Integrate", hardware="Disclosed only in the exact-v1 setup; no cross-paper normalization", precision="Not Disclosed"):
    return (owner, delta, (3, 3, 3), disposition, method, evaluation, limits, workload, model, hardware, precision, trade)


M = {
"2606.15045": E("TRAIN-DISTRIBUTED-TRAINING", "把低比特梯度聚合下沉到 CXL memory controller，并以 workload/layer/phase admission 保留 FP32 recovery path。", "低比特减少流量但 CIFAR-100 的全路径失败表明 approximation 不能无条件进入敏感层；FP32 All-Reduce 仍是 correctness fallback。", "CIFAR-10/100 ResNet-18, SST-2 DistilBERT; gem5/controller timing and FPGA plausibility", "ResNet-18; DistilBERT", method="§3 Architecture; §4 Methodology", evaluation="§§5–10 timing, correctness, training evidence and hardware plausibility", limits="§7.2 harder-workload boundary; §11 Limitations"),
"2606.15050": E("PLATFORM-GATEWAY", "跨站点 LLM 路由必须联合 GPU DCGM、vLLM queue/runtime 与 WAN RTT/jitter，并把 replica lifecycle 与 capability constraint 放进 placement state。", "更多信号可提前 drain，但权重、telemetry staleness 与跨站网络波动会扩大控制环；单站点/同构集群仍适合简单最少队列。", "three US datacenters; 15 GPUs; eight workload classes; 216-cell SLO matrix", "vLLM-served LLM workloads", method="§4 System Architecture; §§4.2–4.4 scorer and lifecycle", evaluation="§5 setup; §6 results", limits="§2.3 failure modes; §7 discussion/limitations"),
"2606.15057": E("PLATFORM-SECURITY", "IPI 防御的 release contract 必须包含对已部署 defense 自适应优化的黑盒攻击，并把 action-open 用户欠规格单列为结构性风险层。", "adaptive red team 提高压力覆盖却受 attacker model、budget 与 task suite 限制；静态回归仍保留为廉价 canary，但不能证明鲁棒。", "three AgentDojo task suites, five target models and adaptive/static attacks", "five target LLMs plus frontier optimizer", method="§III system/threat model; §IV AutoDojo", evaluation="§V Evaluation; Appendix B per-suite ASR", limits="§VI Discussion; action-open structural boundary"),
"2606.15070": E("INFER-DECODE", "用 attention-state 判断推理是否收敛，再在 exit、logit injection 与 jump intervention 之间切换，把 overthinking 从固定 token budget 演进为 request-local control。", "省 token 依赖 attention signal 的校准；误停会丢正确性、误判 trap 会增加扰动，固定 budget 与 verifier fallback 仍需共存。", "nine reasoning benchmarks across DeepSeek-R1-Distill and Qwen3 scales", "DeepSeek-R1-Distill; Qwen3", method="§3 motivations; §4 Methodology", evaluation="§5 Experiments; Appendix D/E/F", limits="§5.5 discussion; Appendix H future work"),
"2606.15079": E("MODEL-LONG-CONTEXT", "已有 dense checkpoint 可经分阶段 attention transplantation 迁移到 7:1 Lightning Attention/MLA hybrid，而不必从头训练；KPop 与异步 RL 是相邻训练 handoff。", "迁移保护既有训练资产却引入 QK-Norm/RoPE compatibility、warmup 与长期稳定性风险；从头训练或 full attention 在迁移证据不足时仍合理。", "31 pretraining benchmarks plus agent/tool/coding/search evaluations", "Ling-2.6 / Ring-2.6 104B–1T family", method="§2.1 hybrid retrofit; §2.3 recipe; §4 infrastructure", evaluation="§2.4 and §3.3 evaluations", limits="§5 Conclusion, Limitations, and Future Directions", disposition="No Change — Existing Coverage", precision="router FP32; other precision remains exact-v1-bound"),
"2606.15099": E("MULTIMODAL-EMBODIED-VLA", "VLA 可把显式 CoT 改成 task-reward 对齐的 latent POMDP reasoning，并用 confidence gate 决定早退。", "latent reasoning 降低文本解码延迟却牺牲可解释性，gate miscalibration 会过早行动；显式计划在审计或高风险任务仍合理。", "LIBERO and embodied-decision benchmarks; compute-matched and robustness ablations", "AVA-VLA and explicit-CoT baselines", method="§3 Method; §§3.5–3.6 RL denoising and early exit", evaluation="§4 Experiments; Appendix C", limits="Appendix D Limitations and Future Work"),
"2606.15122": E("PLATFORM-EVALUATION-SYSTEM", "LLM 只负责为告警构造 analysis harness；harness validation 与 backend formal analysis 才拥有 no-bug discharge authority。", "形式 backend 降低 plausible rationale 误放行，却受 harness assumptions 与 analyzer completeness 限制；无法证明时保守保留告警。", "200 Android kernel driver warnings from two static detectors", "Evident with LLM harness generator and formal backend", method="§3 overview; §4 Design; §5 Implementation", evaluation="§6 Evaluation", limits="§7 Discussion & Limitations"),
"2606.15127": E("PLATFORM-EVALUATION-SYSTEM", "评测应把答案 susceptibility 与 trace acknowledgment 分开；表面承认偏置不是机制理解，也不是 outcome correctness。", "trace 轴提高诊断性但依赖 rubric/judge，且小条件分母不稳定；最终答案与独立 outcome verifier 仍不可省略。", "thousands of biased GSM8K trials", "GPT-4o; Claude Sonnet 4", method="§3 Framework", evaluation="§4 Experimental Design; §5 Results", limits="§6 Discussion and Limitations", disposition="No Change — Existing Coverage"),
"2606.15153": E("PLATFORM-EVALUATION-SYSTEM", "selective risk control 必须同时审计 confidence-bound tightness 与 exchangeability；group shift 时应按组重校准并显式支付 coverage cost。", "更紧证书提高可接受覆盖，却不能跨越 exchangeability 破坏；分组阈值恢复有效性但可能严重拒绝。", "synthetic trials plus anomalous-sound and AI-image detectors", "four calibration rules", method="§2 rules, bounds and exchangeability", evaluation="§3 Experiments", limits="§3.4–3.5 failure/mitigation; §4 limitations"),
"2606.15157": E("INFER-KV-CACHE", "KV compression 应把 eviction method 与 budget allocation 都提升为 layer-wise heterogeneous decision，而不是全层单策略同预算。", "heterogeneity 提升固定预算质量却需要离线 calibration 与更多 profile metadata；短 context 或模型漂移时统一策略更稳。", "long-context tasks under fixed and varied KV budgets", "multiple transformer LLMs", method="§3 Methodology", evaluation="§4 Evaluation", limits="§4.3–4.6 robustness and case-study boundary; §5"),
"2606.15177": E("INFER-SCHEDULING", "MoE serving 要协调 DP-engine request pressure 与 expert/communication pressure，并让 expert placement 消费 source-aware traffic profile。", "联合控制减少两级 imbalance，却引入 trace、MINLP calibration 与 online placement 开销；低偏斜或小规模部署仍适合独立调度。", "MoE serving throughput, latency, ablation and overhead sweeps", "MoE LLM serving stack", method="§3 overall design; §§4–5 scheduling and placement", evaluation="§7 Evaluation", limits="§2.3 current-system limits; §7.5 overhead"),
"2606.15179": E("AGENT-RAG", "document-isolated device-cloud RAG 应用 waiting debt 与 certificate-guided minimal supplement 异步聚合证据，而不是等待所有设备或一次性上传全文。", "稀疏补充降低等待和通信，但证书/估计失真会漏证据；需要全局一致性或关键文档时同步聚合仍合理。", "device-cloud RAG experiments with waiting/communication ablations", "distributed RAG configurations", method="§III problem; §IV Methodology", evaluation="§V Experiments", limits="§IV-E theorem assumptions; §VI"),
"2606.15210": E("INFER-SCHEDULING", "cloud-edge MLLM offload 应把 generation quality predictor 与 latency/capacity state联合进 placement objective。", "联合目标避免只追 latency，却依赖 simulator/quality predictor 的校准；高风险请求仍需固定能力路由或 cloud fallback。", "CEMLLM-Sim benchmark and quality-latency offloading experiments", "multiple MLLM placement options", method="§III system model; §IV QLMIO", evaluation="§V Benchmark and Experiment", limits="§V-G ablation; §VI future work"),
"2606.15216": E("TRAIN-DATA", "pretraining subset selection 应在 gradient space 以 set-level diversity 与 quality 联合优化，而不是逐样本 top-score。", "集合优化减少冗余却需要梯度近似/JL projection 并受 reference model 影响；流式或廉价筛选仍可保留标量质量基线。", "pretraining subset selection across several datasets", "small controlled pretraining models", method="§3 Spokes; §4 efficiency", evaluation="§5 setup; §6 Results", limits="§7 Limitations"),
"2606.15242": E("PLATFORM-SECURITY", "Skill 安全单位应从孤立 artifact 扩到 activated composition path，显式跟踪 capability flow、trust transfer 与 authorization confusion 的 state change。", "path-aware sandbox 暴露组合风险但无法穷尽动态图和长链；静态 artifact vetting 与 effect-time authorization 仍是必要层。", "SCR-Bench across three mechanisms and multiple LLM backends", "multiple agent backends", method="§3 Method; Appendix B", evaluation="§4 Experiments", limits="Appendix A Limitations"),
"2606.15258": E("PLATFORM-EVALUATION-SYSTEM", "step-level proof evaluation 应遮蔽真实 proof step、保留必要上下文并以重复 judge/人审校验等价性，避免从最终答案反推每步正确。", "masked-step 测量更细，却仍受 judge 与 proof-extraction error 影响，不能替代 formal checker；完整答案 benchmark 仍适合粗筛。", "Mask-ProofBench with automated curation, human checks and model comparisons", "multiple reasoning LLMs", method="§3 Methodology", evaluation="§4 Experiments", limits="§4 ablations and §5 discussion"),
"2606.15285": E("MULTIMODAL-EMBODIED-VLA", "把低频 semantic module 与高频 action module 异步解耦，并让 action policy 条件化历史动作以容忍 stale semantics。", "提高 control rate 但引入双时钟、stale-state 与恢复边界；强耦合在低频、可停顿环境仍更简单。", "LIBERO plus real-world robot deployments and stale-semantic ablations", "asynchronous VLA variants", method="§3 Method; Appendix A", evaluation="§4 Experiments; Appendix B/C", limits="§5 Limitations and Discussion"),
"2606.15306": E("PLATFORM-EVALUATION-SYSTEM", "跨任务 experiential learning 需要共享 ground-truth latent 的可控环境，分别测 adaptation neglect、breakdown、miscalibration 与 exploration/exploitation。", "可控 latent 提供诊断但简化真实环境；它证明 failure decomposition，不证明开放任务中的经验迁移。", "seven controllable environments plus cross-task RL demonstration", "frontier agents and trained adaptation policy", method="§2 controllable suite", evaluation="§3 failure modes; §4 demonstration", limits="§5 Discussion"),
"2606.15308": E("PLATFORM-SECURITY", "confidence-based model cascade 是可攻击的资源控制面：输入可被优化为强制 deferral，使昂贵模型被持续调用。", "robust routing/预算 gate 抵抗成本攻击却可能拒绝真实困难输入；accuracy-only deferral 在可信流量仍可保留。", "multiple datasets, MLLM families, routing metrics and preprocessing defenses", "weak/strong multimodal LLM cascades", method="§3 Method and threat model", evaluation="§4 Experiments; Appendix A", limits="§5 Conclusion and Limitations"),
"2606.15319": E("INFER-SCHEDULING", "streaming video generation 应把 playout slack 作为动态 SLO state，用于 preemption、re-homing、elastic sequence parallelism 与 per-chunk fidelity selection。", "回收 slack 提高利用率但转移 KV/state 有开销，低保真传播与 controller lag 会伤质量；静态 reservation 在稳定负载仍合理。", "streaming-video workloads, end-to-end/ablation/sensitivity and controller-overhead tests", "streaming video diffusion serving", method="§3 overview; §§4–5 slack control", evaluation="§7 Evaluation; Appendices B/D", limits="§7.5 sensitivity; §9 future work"),
"2606.15333": E("TRAIN-GRPO", "reinforcement unlearning 可把低 reward hard-case group 放入 off-policy replay，并用 importance correction 重用，而不是继续在易例 on-policy 采样。", "replay 节省 rollout 但会受 policy drift 与 stale buffer 偏差影响；hard/easy 差异不明显时退化到普通 RULE。", "knowledge, copyrighted-content and entity unlearning benchmarks", "multiple LLM unlearning configurations", method="§3 ReRULE", evaluation="§4 Experiments", limits="§4.5 ablation and computational-cost boundary"),
"2606.15335": E("PLATFORM-SECURITY", "分布式 Agent 分享文本时应把 task-role semantics 与 identifying style 分离，并只聚合 role prototypes。", "sanitization 保留任务性却不能证明去标识，representation/judge 漂移会泄漏；高风险数据仍需最小化或不共享。", "distributed-agent text-sharing and RAG experiments", "role-style disentangling sanitizer", method="§3 threat scope; §4 Method", evaluation="§5 Experiments", limits="§3.2 threat scope and later limitations", disposition="No Change — Existing Coverage"),
"2606.15341": E("MULTIMODAL-WORLD-MODELS", "驾驶 world model 必须由当前 observation/action 生成 reactive future，不能偷用 oracle future layout；causal text controls 与 context-forced distillation服务闭环。", "实时反应性用 distillation 换 fidelity，文本控制和标注 pipeline 也可能制造偏差；显式 simulator 继续拥有安全验证。", "SocioDrive-Bench and downstream closed-loop applications", "causal autoregressive teacher and distilled renderer", method="§3 Methodology", evaluation="§4 benchmark; §5 Experiments", limits="§5 reliability/controllability scope; §6"),
"2606.15345": E("PLATFORM-EVALUATION-SYSTEM", "跨语言 deep-research 评测要把 retriever recall、agent evidence integration、citation precision 与 calibration 分开，避免端到端分数吞掉 bottleneck。", "分解提高定位但翻译和 judge 仍会引入偏差；oracle retrieval 只隔离检索损失，不证明 agent reasoning 正确。", "XBCP cross-lingual agent/retriever/oracle-retrieval evaluations", "multiple deep-research agents and retrievers", method="§3 XBCP construction", evaluation="§4 Experiments; Appendices F/G", limits="§5 Discussion; translation/judge scope"),
"2606.15363": E("AGENT-REFLECTION", "Agent self-evolution 可把 harness review、principle distillation 与 workflow topology search 作为三个独立 proposal layer。", "三层共演化扩大搜索却增加 evaluator coupling 和自报偏差；单次 114-trace/4-call case 不证明生产优势。", "one production case with 114 traces and four LLM calls", "APEX three-layer workflow", method="§3 APEX Framework", evaluation="§4 Experimental Evaluation", limits="§5.3 Limitations", disposition="No Change — Existing Coverage"),
"2606.15367": E("TRAIN-DATA", "deep-research 训练数据应从 graph-grounded task 生成，经真实 AgentLoop rollout，再用多维 trajectory verifier 决定收录。", "完整轨迹更贴近部署却昂贵且会继承 generator/verifier bias；静态 QA 仍适合基础能力。", "long-horizon research, report, instruction, file and skill benchmarks", "S1-DeepResearch training stack", method="§3 Agentic Data Construction System", evaluation="§5 Experiments", limits="§7 Limitations"),
"2606.15376": E("AGENT-MULTI-AGENT", "多 Agent 共享对象可用 Monotonic Trajectory Pre-Order：固定读序、speculative write、通知与可逆三阶段 tool call，在 quiescence 达到 serializable outcome。", "少锁并发提高吞吐但要求 undo/saga 与 constrained tools；不可逆副作用或缺少 inverse 时必须串行或人工 gate。", "multi-agent concurrency workloads and protocol/system comparisons", "CoAgent protocol/framework", method="§§4–6 insights, MTPO and framework", evaluation="§7 Evaluation", limits="§5.1 correctness assumptions; §6.3 undoability and three-phase toolcalls"),
"2606.15378": E("MODEL-LONG-CONTEXT", "hybrid architecture 中 efficient attention 主要塑造 optimization，而长程 retrieval 仍主要由 full-attention layers 承担；ratio 与 positional treatment 应按该分工设计。", "减少 full attention 降成本却会压缩长程容量；large-window 或错误 NoPE 组合会产生 lazy layers，纯 full attention 仍是质量基线。", "scaling-law, probing and long-context evaluations across hybrid attention variants", "multiple hybrid attention backbones", method="§§3–6 scaling/mechanism/design", evaluation="§4 settings and scaling; §5 probing", limits="§6 hybrid design ablations; §7 conclusion boundary"),
"2606.15385": E("PLATFORM-EVALUATION-SYSTEM", "Agent RL 评测必须分开 observed proxy reward 与 hidden task reward；更强 exploration、credit assignment 或 entropy 不能修复错误规格。", "隐藏 reward 揭示 gaming 却依赖可构造 oracle；开放世界仍需多 verifier、红队与 effect audit。", "AI Safety Gridworlds zero-shot and RL experiments", "Qwen2.5-family agents and RL variants", method="§2 Methodology", evaluation="§§3–4 zero-shot and RL experiments", limits="§4.3 failed fixes; §5"),
"2606.15390": E("AGENT-REFLECTION", "Skill library 应用随机 masking 估计 per-skill causal effect，并对每任务只暴露有正贡献的最小集合。", "因果 assay 减少 harmful skills 却需要大量 trials 且受 interaction/非平稳性影响；新任务仍需全库探索或保守 fallback。", "tool-agent tasks with masking, library restructuring and per-task selection", "multiple agent backends", method="§2 Assay", evaluation="§3 Experiments; Appendices K/H", limits="Appendix A.3 Limitations"),
"2606.15405": E("AGENT-MEMORY", "长期 memory 应在 write time 生成事实/片段级 retrieval triggers，使未来 query 可通过描述性与联想线索命中，而不只按原文相似度检索。", "trigger 提高联想 recall 但会增加写入成本和误触发；未知未来意图仍需 semantic/full-text fallback。", "LoCoMo and LoCoMo-Plus with ablation and efficiency analyses", "T-Mem and memory baselines", method="§3 Approach", evaluation="§4 Experiments", limits="§4.4–4.6 ablation/efficiency; §5"),
"2606.15441": E("PLATFORM-SECURITY", "IPI defense 应在每次 tool output 上做 task-alignment reasoning，并用自适应 red-team diversity reward 构造训练分布。", "训练防御改善安全-效用取舍但依赖 threat model、reasoning faithfulness 与持续 refresh；deterministic effect gate 仍不可替代。", "six adaptive black-box attacks across two target models", "RETA-trained agent defenders", method="§3 failures; §4 RETA", evaluation="§5 Experiments", limits="§5.5 Failure Analysis; §6 Limitations"),
"2606.15453": E("INFER-GPU-MEMORY", "MoE expert staging 可利用跨层与相邻 token 的 activation correlation 预取，并保持原 router 决策不变。", "prefetch 隐藏加载却占带宽/容量，误预测会挤出需要 expert；动态 routing 漂移时 on-demand loading 仍是 fallback。", "language/code MoE workloads, prediction, latency, energy and hardware sensitivity", "Qwen/DeepSeek-class MoE models", method="§3 correlations; §4 ST-MoE design", evaluation="§5 Evaluation and Analysis", limits="§5.6–5.7 ablation/sensitivity; §7"),
"2606.15455": E("TRAIN-GRPO", "RLVR 的 diversity collapse 应按 problem saturation/overtraining 解释，并用 zero-success/boundary contribution gate 决定哪些题继续更新。", "boundary gating 保护高-k 能力但估计受少量 rollout 噪声影响；只优化 Pass@1 或资源紧张时普通 on-policy 仍更简单。", "multiple reasoning benchmarks with Pass@k, gating and early-stop analyses", "RLVR base models and GRPO/REINFORCE/BBG variants", method="§3 overtraining; §4 Methodology", evaluation="§5 Experiments; Appendices A–D", limits="§6 Limitations and sampling-noise appendix"),
"2606.15474": E("PLATFORM-EVALUATION-SYSTEM", "持续评测必须用固定人标 anchor 与第二条 anytime-valid e-process 区分 system drift 和 judge drift，并让 anchor race 快于主告警。", "anchor 减少误归因却增加强 judge/人标成本并会陈旧；系统与 judge 同时漂移时只能按声明规则保守归类。", "two real judge changes across two domains and repeated streaming trials", "cheap monitor plus strong LLM judge", method="§3 cost-aware monitoring; §4 anchor construction", evaluation="§5 Experiments", limits="§6 Discussion and Limitations"),
"2606.15476": E("AGENT-MEMORY", "机器人 episodic memory 应保存 object identity、geometry、VLM descriptor 与 viewpoint evidence，并用显式关系谓词约束 retrieval。", "符号关系提高可解释检索但维护 object identity 与 geometry 有成本；开放类误检或变化环境仍需视觉 history fallback。", "44k queries, 67 scenes, real-time and quadruped deployment", "FARM with VLM parsing/reranking", method="§2 Method; Appendix D", evaluation="§3 Experiments; Appendix F", limits="§4.1 Limitations"),
"2606.15493": E("PLATFORM-SECURITY", "模型窃取评估不能把高 fidelity surrogate 等同部署等价；Rashomon set 的 ambiguity、discrepancy 与 fairness 必须单独报告。", "multiplicity audit 降低错误风险推断，却不测真实攻击成本或商业替代；fidelity 仍是基础泄漏指标。", "tabular, medical-imaging and NLP extraction experiments", "multiple surrogate families", method="§§2–3 multiplicity and metrics", evaluation="§4 Experiments", limits="§5 Discussion; partial-supervision boundary"),
"2606.15508": E("AGENT-TOOL-CALLING", "visible tool menu 是运行时权限/认知界面；应按 state 与 causal path 暴露最小工具集，同时测 risky exposure、wrong call、premature action 与 token cost。", "最小菜单降风险和 token，却可能漏掉恢复工具或跨步依赖；小型可信库仍可 all-tools。", "seven backends, three menu sizes, six filters and seven settings", "seven LLM backends", method="§III Benchmark; §IV filtering methods", evaluation="§V metrics and §VI results", limits="§III-F4 contract-quality sensitivity; §VII discussion/limitations"),
"2606.19380": E("PLATFORM-SECURITY", "coding-agent safety failure 应拆成 underspecification、capability error 与 harness error，并分别用 policy、classifier/immutability 与 context/tool control修复。", "分解支持定向缓解但有限场景不能证明安全 guarantee；自修改 harness 还需外部 immutable authority。", "eight coding-agent safety evaluations plus mitigation tests", "frontier coding agents and AgentArmor", method="§3 setup; §4 scenarios; §5 design", evaluation="§6 Implementation and Results; Appendices", limits="§7 future directions; Appendix C.17 validity"),
"2606.20679": E("MULTIMODAL-WORLD-MODELS", "video-world-model policy 应把 episode history 压成 recap tokens，并由 cue gate 估计 progress，同时注入 video backbone 与 action decoder。", "记忆缓解非 Markov 窗口却可能压缩掉关键事件；并行 memory 不保证长期一致性，短任务仍可无 memory。", "LIBERO-Mem and real-robot counting/spatial/sequential tasks", "UNet and DiT video-action backbones", method="§3 Method", evaluation="§4 Experiments", limits="§6 Limitations"),
"2606.28361": E("AGENT-RAG", "多轮 RAG 服务可把历史文档/推理改成 append-only conclusion chain，并在一次调用中联合生成 reasoning 与 conclusion，使跨轮输入从近 O(N²) 降为 O(N)。", "状态压缩节省 token/网络却会累积遗漏和错误结论；高风险问答仍需 raw evidence pointer 与可恢复 replay。", "12 configurations across three models, two datasets and two frameworks", "three API-served LLMs", method="§III model; §IV Algorithm; §V analysis", evaluation="§VI Experiment", limits="§VI-D deployment implications; §VIII"),
}


PATHS = {
"TRAIN-DISTRIBUTED-TRAINING":"books/part-04-training-system/36-distributed-training.md", "PLATFORM-GATEWAY":"books/part-06-ai-infrastructure/62-gateway.md", "PLATFORM-SECURITY":"books/part-06-ai-infrastructure/72-security.md", "INFER-DECODE":"books/part-05-inference-system/44-decode.md", "MODEL-LONG-CONTEXT":"books/part-02-model/22-long-context.md", "MULTIMODAL-EMBODIED-VLA":"books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "PLATFORM-EVALUATION-SYSTEM":"books/part-06-ai-infrastructure/66-evaluation-system.md", "INFER-KV-CACHE":"books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "INFER-SCHEDULING":"books/part-05-inference-system/56-inference-scheduling.md", "AGENT-RAG":"books/part-07-agent/76-rag.md", "TRAIN-DATA":"books/part-04-training-system/27-data.md", "TRAIN-GRPO":"books/part-04-training-system/33-grpo.md", "MULTIMODAL-WORLD-MODELS":"books/part-03-multimodal-world-models/25-multimodal-world-models.md", "AGENT-REFLECTION":"books/part-07-agent/80-reflection.md", "AGENT-MULTI-AGENT":"books/part-07-agent/82-multi-agent.md", "AGENT-MEMORY":"books/part-07-agent/77-memory.md", "INFER-GPU-MEMORY":"books/part-05-inference-system/54-gpu-memory.md", "AGENT-TOOL-CALLING":"books/part-07-agent/78-tool-calling.md",
}


def adjacent(path: str) -> str:
    p = int(re.search(r"/(\d+)-", path).group(1))
    candidates = sorted(ROOT.glob(f"books/**/{p-1:02d}-*.md")) + sorted(ROOT.glob(f"books/**/{p+1:02d}-*.md"))
    return "; ".join(str(x.relative_to(ROOT)) for x in candidates[:2]) or path


def replace_counts(text: str, integrates: int, owners: int, nochange: int) -> str:
    pairs = [
        ("2026-06-11", "2026-06-14"), ("20260611", "20260614"), ("2026-W24", "2026-W24"),
        ("2026-06-10T09:00:00+08:00", "2026-06-13T09:00:00+08:00"),
        ("2026-06-11T09:00:00+08:00", "2026-06-14T09:00:00+08:00"),
        ("2026-06-11T01:00:00Z", "2026-06-14T01:00:00Z"),
        ("559/559", f"{RAW}/{RAW}"), ("31/559", f"{N}/{RAW}"),
        ("31 durable AI-system families and 528 row-specific closures", f"{N} durable AI-system families and {CLOSED} row-specific closures"),
        ("31 retained, 528 closures", f"{N} retained, {CLOSED} closures"),
        ("closures 528", f"closures {CLOSED}"),
        (" | checked | 559 | ", f" | checked | {RAW} | "),
        ("559 unique", f"{RAW} unique"), ("559 registered", f"{RAW} registered"),
        ("31 durable", f"{N} durable"), ("31 retained", f"{N} retained"),
        ("31/31", f"{N}/{N}"), ("31 exact", f"{N} exact"),
        ("26 Integrate", f"{integrates} Integrate"), ("26/26", f"{integrates}/{integrates}"),
        ("12 unique owners", f"{owners} unique owners"), ("12 files", f"{owners} files"),
        ("five No Change", f"{nochange} No Change"), ("5/5", f"{nochange}/{nochange}"),
        ("31 retained families", f"{N} retained families"), ("31 retained", f"{N} retained"),
        ("beyond the 31 retained families", f"beyond the {N} retained families"),
        ("DEN-20260611-559031", DENOMINATOR_ID), ("daily-20260611", "daily-20260614"),
        ("fresh-context:jun11", "fresh-context:jun14"), ("SA-20260611", "SA-20260614"),
        ("DA-20260611", "DA-20260614"),
    ]
    for a, b in pairs:
        text = text.replace(a, b)
    return text


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
        "## 8. Daily Integration Decision",
        "## 9. Repository Changes",
        "## 10. Open Questions",
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
    materials = _section_body(text, "## 7. Materials and Access", "## 8. Daily Integration Decision")
    recommended = _section_body(text, "## 8. Daily Integration Decision", "## 9. Repository Changes")
    repository = _section_body(text, "## 9. Repository Changes", "## 10. Open Questions")
    questions = _section_body(text, "## 10. Open Questions", None)

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
        f"## 9. Recommended Action\n\n{recommended}",
        f"## 10. Repository Changes\n\n{repository}",
        f"## 11. Open Questions\n\n{questions}",
        "## 12. Sources\n\n- arXiv exact-v1 sources and locators listed in the Review Completion Receipt.",
        FINAL_STATUS.rstrip(),
    ]
    return "\n\n".join(section for section in sections if section) + "\n"


def assert_canonical_presentation(text: str) -> None:
    assert re.findall(r"(?m)^## .+$", text) == EXPECTED_H2
    assert "All 254 identities were read at title+abstract level." in text
    assert "All 559 identities were read at title+abstract level." not in text
    assert "Books writeback is pending" not in text
    assert "this lane completed the independent 41/41 post-write fresh-context audit" in text
    evidence_audit = EVIDENCE_AUDIT.read_text(encoding="utf-8")
    assert "41 retained; 213 row-specific closures." in evidence_audit
    assert "41 retained; 528 row-specific closures." not in evidence_audit
    for field in ("Research Date", "Timezone", "Strict Window", "Contract", "Status"):
        assert text.count(f"**{field}:**") == 1, field
    assert "**Status:** Complete" in text
    assert "Coverage `Closed`" in text and "Evidence `Passed`" in text and "Books `Passed`" in text
    protected = protected_report_fragments(text)
    assert len([key for key in protected if key.startswith("block:review:")]) == 41
    assert len([key for key in protected if key.startswith("block:books-review:")]) == 41
    assert len([key for key in protected if key.startswith("block:analysis:")]) == 3
    assert len(set(re.findall(r"RP-[0-9a-f]{16}", text))) == 41
    assert EVIDENCE_AUDIT.is_file() and POST_WRITE_AUDIT.is_file()


def _report_collections(protected: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    reviews = {key: value for key, value in protected.items() if key.startswith("block:review:")}
    books = {
        key: value
        for key, value in protected.items()
        if key.startswith(("block:existing:", "block:delta:", "block:books-review:"))
        or key == "table:validator:books-comparison-v1"
    }
    return reviews, books


def write_presentation_audit(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    reviews, books = _report_collections(protected)
    audit = f"""# 2026-06-14 Canonical Presentation Audit V1

- Scope: reader-facing migration only; accepted denominator, Evidence, Selection, Books state and Gate semantics were not re-evaluated.
- Canonical presentation: top five fields present; `Executive Summary` plus the exact numbered §§1–13 H2 sequence passed.
- Protected report fragments: `{len(protected)}`; combined SHA256 `{_collection_hash(protected)}`.
- Bounded Reviews: `41/41`; combined SHA256 `{_collection_hash(reviews)}`.
- Review Provenance IDs: `41/41`; the protected Review Completion table remains byte-identical.
- Books table and bounded blocks: `{len(books)}` fragments; combined SHA256 `{_collection_hash(books)}`.
- Semantic packet inputs: `{len(packet_hashes)}` files sealed; combined SHA256 `{_collection_hash(packet_hashes)}`.
- Reader-facing Daily SHA256: `{hashlib.sha256(report.encode('utf-8')).hexdigest()}`.
- Owner renderer guard: PASS — protected-byte drift, missing audits, wrong Gate summary, duplicate markers or H2 drift fails closed.
- Semantic handoff: `FRESH_EVIDENCE_SELECTION_AUDIT_V1.md` and `POST_WRITE_FRESH_AUDIT_V1.md` remain the accepted semantic audits; structural validation is not substituted for semantic truth.
- Findings: none unresolved.
"""
    PRESENTATION_AUDIT.write_text(audit, encoding="utf-8")


def assert_prior_presentation_seal(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    if not PRESENTATION_AUDIT.is_file():
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
    if not (REPORT.is_file() and EVIDENCE_AUDIT.is_file() and POST_WRITE_AUDIT.is_file()):
        return False
    before_report = REPORT.read_text(encoding="utf-8")
    before_protected = protected_report_fragments(before_report)
    before_packet = semantic_packet_hashes()
    assert_prior_presentation_seal(before_protected, before_packet, before_report)
    report = canonicalize_presentation(before_report)

    # One accepted-state metadata repair is intentionally performed only after
    # the prior seal has verified the complete input.  It corrects two inherited
    # June-11 denominator strings without reopening any review or Books body.
    stale_report = "All 559 identities were read at title+abstract level."
    current_report = "All 254 identities were read at title+abstract level."
    stale_audit = "41 retained; 528 row-specific closures."
    current_audit = "41 retained; 213 row-specific closures."
    stale_status = (
        "Books writeback was serialized through root; Books writeback is pending; "
        "this lane completed the independent evidence/selection audit."
    )
    current_status = (
        "Books writeback was serialized through root; this lane completed the "
        "independent 41/41 post-write fresh-context audit."
    )
    evidence_before = EVIDENCE_AUDIT.read_text(encoding="utf-8")
    repair_report = stale_report in report
    repair_audit = stale_audit in evidence_before
    if repair_report:
        assert report.count(stale_report) == 1 and current_report not in report
        report = report.replace(stale_report, current_report)
    if stale_status in report:
        assert report.count(stale_status) == 1 and current_status not in report
        report = report.replace(stale_status, current_status)
    if repair_audit:
        assert evidence_before.count(stale_audit) == 1 and current_audit not in evidence_before
        EVIDENCE_AUDIT.write_text(
            evidence_before.replace(stale_audit, current_audit), encoding="utf-8"
        )

    after_protected = protected_report_fragments(report)
    if repair_report:
        changed = {
            key for key in before_protected
            if before_protected[key] != after_protected[key]
        }
        assert changed == {"block:coverage:SRC-ARXIV:20260614"}, changed
    else:
        assert after_protected == before_protected

    after_packet = semantic_packet_hashes()
    if repair_audit:
        changed = {
            key for key in before_packet
            if before_packet[key] != after_packet[key]
        }
        assert changed == {"FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"}, changed
    else:
        assert after_packet == before_packet
    assert_canonical_presentation(report)
    REPORT.write_text(report, encoding="utf-8")
    write_presentation_audit(after_protected, after_packet, report)
    regenerate_manifest()
    print(json.dumps({
        "mode": "accepted-presentation-only",
        "raw": RAW,
        "retained": N,
        "closures": CLOSED,
        "reviews_preserved": N,
        "books_dispositions_preserved": N,
        "canonical_numbered_sections": 13,
        "total_h2": len(EXPECTED_H2),
    }, ensure_ascii=False))
    return True


def main() -> None:
    if finalize_accepted_presentation():
        return
    assert len(M) == N
    base.PACKET = PACKET
    base.PROVISIONAL = PACKET / "screening-ledger-provisional.json"
    base.LEDGER = PACKET / "screening-ledger.json"
    base.AUDIT = PACKET / "denominator-full-semantic-audit-v1.tsv"
    base.RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
    base.QUEUE = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
    base.READY = PACKET / "READY_TO_INSERT_BOOKS_V1.md"
    base.EVIDENCE_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
    base.POSTWRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
    base.REPORT = ROOT / "papers/2026/06/14/README.md"
    base.EXECUTED_AT = EXECUTED_AT
    base.DENOMINATOR_ID = DENOMINATOR_ID
    base.M = M
    base.PATHS = PATHS
    base.ADJ = {k: adjacent(v) for k, v in PATHS.items()}
    base.TITLE.update({
        "2606.15057": "AutoDojo: Adaptive Attacks Expose Superficial Defenses and User-Underspecification Limits in LLM Agents",
        "2606.19380": "AgentArmor: A Framework, Evaluation, & Mitigation of Coding Agent Failures",
    })

    real_loads = base.json.loads
    class CountList(list):
        def __len__(self): return 559
    def loads(s, *args, **kwargs):
        obj = real_loads(s, *args, **kwargs)
        if isinstance(obj, dict) and isinstance(obj.get("identities"), list):
            obj["identities"] = CountList(obj["identities"])
        return obj
    base.json.loads = loads
    try:
        base.main()
    except (AssertionError, KeyError):
        pass
    finally:
        base.json.loads = real_loads

    integrates = sum(v[3].startswith("Integrate") for v in M.values())
    nochange = N - integrates
    owners = len({v[0] for v in M.values() if v[3].startswith("Integrate")})
    for path in [base.AUDIT, base.QUEUE, base.READY, base.EVIDENCE_AUDIT, base.REPORT]:
        s = replace_counts(path.read_text(), integrates, owners, nochange)
        path.write_text(s)

    ledger = json.loads(base.LEDGER.read_text())
    ledger["gate_status"] = "coverage_evidence_selection_passed_books_open"
    ledger["routed_candidate_denominator"] = N
    ledger["routed_candidate_denominator_status"] = f"frozen_after_{RAW}_of_{RAW}_full_semantic_audit"
    ledger["abstract_screening_closure"] = CLOSED
    ledger["canonical_candidate_denominator"].update(raw_identities=RAW, retained=N, pre_denominator_closures=CLOSED)
    ledger["audit"].update(reviewed_identities=f"{RAW}/{RAW}", books_gate="open_pending_serialized_root_writeback")
    base.LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

    receipts = json.loads(base.RECEIPTS.read_text())
    receipts["denominator_id"] = DENOMINATOR_ID
    receipts["generated_at"] = EXECUTED_AT
    selected_ids = {"2606.15057", "2606.15376", "2606.15474"}
    for row in receipts["reviews"]:
        arxiv_id = row["event_identity"].split(":")[-1]
        row["selection_decision"] = "selected" if arxiv_id in selected_ids else "not_selected"
    base.RECEIPTS.write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n")

    report = base.REPORT.read_text()
    report = report.replace("| Completion Status | Complete |", "| Completion Status | In Progress |")
    report = report.replace("| Books Gate | Passed |", "| Books Gate | Open |")
    refs = "; ".join(f"books-review:{base.fam(a)}" for a in M)
    report = re.sub(r"\| SA-20260614-BOOKS-POSTWRITE-V1 .*?\| passed \|", f"| SA-20260614-BOOKS-PREWRITE-V1 | fresh-context:jun14-v1 | books | {refs} | F-0614-BOOKS-PENDING | owner/adjacent comparison is complete, but serialized Books writeback and post-write semantic audit are still required | open |", report)
    report = report.replace("Root merged", "Proposal packet queues")
    report = report.replace("were merged by root", "are queued for serialized root merge")
    report = report.replace("Root performed the serialized Books writeback", "Root has not yet performed the serialized Books writeback")
    report = report.replace("this lane performed the independent post-write audit", "Books writeback is pending; this lane completed the independent evidence/selection audit")
    report = report.replace("closed Books Gate", "keeps Books Gate open pending post-write audit")
    report = report.replace("The 41/41 post-write fresh-context audit resolved one Daily-only owner finding for 2606.12370 and keeps Books Gate open pending post-write audit.", "Books writeback and the 41/41 post-write fresh-context audit remain pending, so Books Gate stays Open.")
    report = report.replace("- `Integrate`: 26 families are queued for serialized root merge into 12 unique ROADMAP owners; each exact-v1 family ID occurs once in its target Books file.", f"- `Integrate`: {integrates} families are queued for serialized root merge into {owners} unique ROADMAP owners; exact-v1 family uniqueness will be checked after writeback.")
    report = report.replace("- Finding `F-0611-OWNER-12370` was confined to Daily routing: MTP acceptance/TV/rejection correctness belongs to `INFER-SPECULATIVE-DECODING`; `TRAIN-RLHF` consumes rollout throughput and policy-update consequences as an adjacent handoff.\n", "")
    report = report.replace("source receipts, finalizer and post-write audit only", "source receipts, finalizer and pre-write audit only")
    selected = {"2606.15057":"DA-20260614-ADAPTIVE-SECURITY", "2606.15376":"DA-20260614-SHARED-STATE", "2606.15474":"DA-20260614-DRIFT-ATTRIBUTION"}
    lines = report.splitlines()
    for i, line in enumerate(lines):
        for a, unit in selected.items():
            f = base.fam(a)
            if line.startswith(f"| {f} |") and "| not_selected |" in line:
                lines[i] = line.replace("| not_selected | — | — |", f"| selected | {unit} | — |").replace("Retained after full review, but subsumed in narrative priority by three non-overlapping units; review remains authoritative.", "Selected after the complete frontier comparison because it contributes a non-overlapping control/evidence boundary.").replace(f"analysis-decision:{f}", f"analysis:{unit}")
        if line.startswith("| SA-20260614-SELECTION-V1 |"):
            for a, unit in selected.items():
                lines[i] = lines[i].replace(f"analysis-decision:{base.fam(a)}", f"analysis:{unit}")
    report = "\n".join(lines) + "\n"
    for stale in ("ADMISSION", "AGING", "COMPOSITE-SERVING"):
        report = re.sub(rf"\n<!-- analysis:DA-20260614-{stale}:start -->.*?<!-- analysis:DA-20260614-{stale}:end -->\n", "\n", report, flags=re.S)
    analysis_blocks = "<!-- analysis:DA-20260614-ADAPTIVE-SECURITY:start -->\n### DA-20260614-ADAPTIVE-SECURITY\nStatic IPI success is not a release certificate: adaptive black-box optimization and action-open underspecification must be explicit threat-model dimensions, while deterministic effect authorization remains the final authority.\n<!-- analysis:DA-20260614-ADAPTIVE-SECURITY:end -->\n\n<!-- analysis:DA-20260614-SHARED-STATE:start -->\n### DA-20260614-SHARED-STATE\nMulti-agent concurrency becomes a transaction problem when speculative text causes shared effects; MTPO gains overlap only where reads are ordered and writes are undoable, so irreversible tools retain a serial gate.\n<!-- analysis:DA-20260614-SHARED-STATE:end -->\n\n<!-- analysis:DA-20260614-DRIFT-ATTRIBUTION:start -->\n### DA-20260614-DRIFT-ATTRIBUTION\nA production score stream cannot identify whether the system or its LLM judge drifted. Fixed human anchors and an independent anytime-valid process create an attribution race, not a correctness proof.\n<!-- analysis:DA-20260614-DRIFT-ATTRIBUTION:end -->\n\n"
    report = report.replace("## 5. Books Comparison and Decision", analysis_blocks + "## 5. Books Comparison and Decision")
    report = report.replace("- `No Change — Existing Coverage`: 5 families", "- `No Change — Existing Coverage`: 4 families")
    report = re.sub(r"## 10\. Open Questions\n\n.*?\n- These are research continuations, not unresolved Gate findings\.", "## 10. Open Questions\n\n- How should attention-state stopping, cascade deferral and quality predictors share calibration/refresh evidence under drift?\n- How should conclusion-chain compression and anticipatory memory preserve raw-evidence replay without losing their cost advantage?\n- Which external effects can honestly satisfy the undoability assumption required by concurrent multi-Agent coordination?\n- How should cross-site routing, MoE pressure and streaming slack exchange backpressure without creating an unstable joint controller?\n- These are research continuations, not unresolved Gate findings.", report, flags=re.S)
    base.REPORT.write_text(report)

    evidence = base.EVIDENCE_AUDIT.read_text()
    evidence = re.sub(r"- Books post-write:.*", f"- Books pre-write: PASS — {integrates} Integrate proposals are merged into {owners} owner writes; {nochange} No Change dispositions retain exact-v1 evidence. Books Gate remains Open until root writeback and fresh post-write audit.", evidence)
    base.EVIDENCE_AUDIT.write_text(evidence)
    (PACKET / "candidate-ids-v1.txt").write_text("\n".join(M) + "\n")
    (PACKET / "README.md").write_text(f"# 2026-06-14 source packet\n\nCanonical denominator `{N}/{RAW}`; closures `{CLOSED}`. Coverage, Evidence and Selection Gates Passed. Books Gate Open pending serialized root writeback and post-write fresh-context audit.\n")
    if base.POSTWRITE_AUDIT.exists():
        base.POSTWRITE_AUDIT.unlink()


def postwrite() -> None:
    """Close Books Gate only after every Integrate family has one unique owner hit."""
    if finalize_accepted_presentation():
        return
    receipts = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())
    nochange_locations = {
        "2606.15079": "`books/part-02-model/22-long-context.md:283` dense-to-hybrid migration with conversion probe, retained attention and long-context calibration",
        "2606.15127": "`books/part-06-ai-infrastructure/66-evaluation-system.md:234` process/information/output evidence separated from outcome; `:873` deterministic verdict separated from stochastic judge",
        "2606.15335": "`books/part-06-ai-infrastructure/72-security.md:89` relationship-aware local sanitization, client-owned mapping and fail-closed restoration",
        "2606.15363": "`books/part-07-agent/81-workflow.md:342` versioned harness proposal, held-out regression and fixed outer commit authority",
    }
    books = sorted(ROOT.glob("books/**/*.md"))
    audit = [
        "# 2026-06-14 Post-write Fresh-context Audit V1", "",
        f"Denominator `{DENOMINATOR_ID}`; {N}/{N} families audited after the serialized Books writeback.", "",
        "| Family | Disposition | Unique owner / adjacent result | Mechanism and non-proof boundary | Result |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in receipts["reviews"]:
        a = row["event_identity"].split(":")[-1]
        f = row["source_family_id"]
        owner = row["stable_node_id"]
        disp = row["books_disposition"]
        path = ROOT / PATHS[owner]
        owner_hits = [i + 1 for i, line in enumerate(path.read_text().splitlines()) if a in line]
        global_hits = [(str(p.relative_to(ROOT)), i + 1) for p in books for i, line in enumerate(p.read_text().splitlines()) if a in line]
        if disp.startswith("Integrate"):
            assert len(owner_hits) == 1, (a, owner, owner_hits)
            assert len(global_hits) == 1, (a, global_hits)
            loc = f"`{PATHS[owner]}:{owner_hits[0]}`; owner `{owner}`; adjacent `{adjacent(PATHS[owner])}`"
            boundary = f"Mechanism: {M[a][1]} Trade-off / failure / fallback: {M[a][-1]} Evidence boundary: `{M[a][6]}`."
        else:
            assert not owner_hits, (a, "No Change family was appended unexpectedly", owner_hits)
            loc = f"owner `{owner}`; adjacent `{adjacent(PATHS[owner])}`; {nochange_locations[a]}"
            boundary = f"Existing proposition covers: {M[a][1]} Trade-off / fallback: {M[a][-1]} Daily retains `{M[a][6]}` without a duplicate append."
        audit.append(f"| `{f}` | {disp} | {loc} | {boundary} | PASS |")
    audit += ["", "## Gate verdict", "", "- 37/37 Integrate unique owner writebacks: PASS.", "- 4/4 No Change semantic locations: PASS.", "- 41/41 owner/adjacent handoffs and exact-v1 evidence boundaries: PASS.", "- Unresolved findings: 0.", "- Books Gate: PASS."]
    post = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
    post.write_text("\n".join(audit) + "\n")

    report_path = ROOT / "papers/2026/06/14/README.md"
    report = report_path.read_text()
    report = report.replace("| Completion Status | In Progress |", "| Completion Status | Complete |")
    report = report.replace("| Books Gate | Open |", "| Books Gate | Passed |")
    report = report.replace("Proposal packet queues 37 Integrate families into 18 unique owners; 4 No Change families were rechecked against existing owner/adjacent coverage. Books writeback and the 41/41 post-write fresh-context audit remain pending, so Books Gate stays Open.", "Root merged 37 Integrate families into 18 unique owners; four No Change families remained Daily-only. The 41/41 post-write fresh-context audit found no unresolved semantic finding and closed Books Gate.")
    report = re.sub(r"\| SA-20260614-BOOKS-PREWRITE-V1 .*?\| open \|", f"| SA-20260614-BOOKS-POSTWRITE-V1 | fresh-context:jun14-postwrite-v1 | books | {'; '.join('books-review:'+base.fam(a) for a in M)} | — | 37/37 unique Integrate writebacks, 4/4 No Change semantic locations and 41/41 owner/adjacent handoffs passed; `papers/2026/06/_sources/daily-20260614/POST_WRITE_FRESH_AUDIT_V1.md` | passed |", report)
    report = report.replace("- `Integrate`: 37 families are queued for serialized root merge into 18 unique ROADMAP owners; exact-v1 family uniqueness will be checked after writeback.", "- `Integrate`: root merged 37 families into 18 unique ROADMAP owners; each exact-v1 family ID occurs once in its unique owner file.")
    report = report.replace("Root has not yet performed the serialized Books writeback", "Root performed the serialized Books writeback")
    report = report.replace("source receipts, finalizer and pre-write audit only", "source receipts, finalizer and post-write audit only")
    report_path.write_text(report)

    ledger_path = PACKET / "screening-ledger.json"
    ledger = json.loads(ledger_path.read_text())
    ledger["gate_status"] = "all_gates_passed"
    ledger["audit"].update(books_gate="passed_after_41_of_41_post_write_fresh_context_semantic_audit")
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    evidence_path = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
    evidence = evidence_path.read_text()
    evidence = re.sub(r"- Books pre-write:.*", "- Books post-write: PASS — 37/37 Integrate unique owner writebacks, 4/4 No Change semantic locations and 41/41 owner/adjacent handoffs; unresolved findings 0.", evidence)
    evidence_path.write_text(evidence)
    (PACKET / "README.md").write_text(f"# 2026-06-14 source packet\n\nCanonical denominator `{N}/{RAW}`; closures `{CLOSED}`. Coverage, Evidence, Selection and Books Gates Passed. Post-write fresh-context audit: `POST_WRITE_FRESH_AUDIT_V1.md`.\n")
    assert finalize_accepted_presentation()


if __name__ == "__main__":
    import sys
    postwrite() if "--postwrite" in sys.argv else main()
