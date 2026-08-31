#!/usr/bin/env python3
"""Render the contract-compliant 2026-05-03 author packet."""

from __future__ import annotations

import hashlib
import json
import unicodedata
from pathlib import Path

from render_report import CONFIG, DEEP_NARRATIVE


HERE = Path(__file__).resolve().parent
REPORT = HERE.parents[1] / "03" / "README.md"
LEDGER = json.loads((HERE / "screening-ledger-v2.1.json").read_text())
RETRIEVED_AT = "2026-08-31T20:55:00+08:00"

# Exact-v1 papers without a standalone empirical or limitations section use a
# reasoned exception rather than a vague prose locator.
CONFIG["2605.01357"]["limits"] = "Not Disclosed — exact-v1 has no standalone limitations section; scope is N=5, named tasks/judges/models and logits access"
CONFIG["2605.01425"]["eval"] = "Not Required — exact-v1 is a theorem/construction paper with no empirical benchmark"
CONFIG["2605.01425"]["limits"] = "Not Disclosed — limits are the autoregressive, black-box and optimality assumptions stated with the theorems"
CONFIG["2605.06690"]["eval"] = "Not Required — exact-v1 provides formal examples and application sketches, not an end-to-end empirical benchmark"
CONFIG["2605.06690"]["limits"] = "Not Disclosed — result is local and linearized; exact-v1 proves neither global convergence nor truth"
CONFIG.update({
    "2605.01186": dict(f="SF-ATTACK-AGENT-TERMINAL-FINGERPRINT", owner="PLATFORM-SECURITY", score=(3,3,3), disp="No Change — Existing Coverage", title="Trace", method="§2 Design Methodology; §2.1 Threat Model and Target Environment; §2.3 passive fingerprinting; §2.4 active forensics", eval="§3 Evaluation Setup; §4 Evaluation Results; §5 Validation of Trace in the Wild", limits="§6 Threats to Validity and Future Work — model/scaffold drift, mimicry/evasion, honeypot and payload scope", artifact="§3 reports evaluation scripts and a reproducibility notebook; full dataset and immutable reviewed commit Not Disclosed", body="攻击 Agent 的 provider/model identity 通常不可从一次 tool call 直接获得，但 terminal session 会留下 command-order 与 bigram 行为痕迹。Trace 先以 TF-IDF/LinearSVC 被动分类 model family，再按 family 路由 defensive prompt-injection payload 做 active forensics。exact-v1 的 2,028-session CTF/container 实验、scaffold-LOSO、evasion 与 proprietary-scaffold 检查只支持所测七个 family/三类 scaffold；classifier 会受 scaffold、mimicry、模型更新和 DPI 可规避性影响，DPI 本身还可能污染调查。Security 章节已将黑盒行为 fingerprint 定义为可漂移的风险 sensor，而非身份凭证，并要求不确定时回退限流/隔离，因此该 family 不重复写入。", queue="—"),
    "2605.01247": dict(f="SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT", owner="PLATFORM-SECURITY", score=(3,3,2), disp="No Change — Existing Coverage", title="FP-Agent", method="§4 Methodology; §4.2 honey website; §4.4 data collection; §4.5 featurization; §4.6 multi-class classification", eval="§5 Characterizing Fingerprints; §5.1 classifier evaluation; §5.2 browser fingerprints; §5.3 behavioral fingerprints", limits="§6 Discussion, Limitations, and Implications; §6.1 generalizability; §6.2 arms race; §6.3 real-time classification", artifact="§9 Data Availability; immutable reviewed dataset/code commit Not Disclosed", body="真实浏览器会削弱传统 bot flag 与 browser fingerprint 的区分力，网站仍可从 typing、scroll 与 mouse trajectory 提取行为 sensor。FP-Agent 在 instrumented honey site 上比较七种 browsing agent 与人类、三类任务，并显示 behavioral features 比共享 browser features 更有区分度。该结果不证明开放流量上的稳定身份：任务、browser automation、agent version 与反检测策略都会漂移，实时 false-positive cost 也未由受控研究闭合。Security 章节已经把 web-agent attribution 写成 TLS/HTTP/browser-action 多层 fingerprint，由 policy engine 只据此 throttle/challenge，classifier 漂移时回退行为限流；故 No Change。", queue="—"),
    "2605.01284": dict(f="SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN", owner="AGENT-RAG", score=(3,3,3), disp="Integrate", title="Chain of Evidence", method="§3 Wiki-CoE Dataset; §3.2 bounding-box annotation; §4 Methodology; §4.2 candidate reasoning; §4.3 chain-structured evidence generation; §4.4 unified generation", eval="§5 Experiment Setup; §6 Experimental Results; §6.2 reasoning type; §6.3 SlideVQA generalization; §6.4 ablations; §6.5 efficiency", limits="Not Disclosed — exact-v1 has no standalone limitations section; claims are bounded to Wiki-CoE/SlideVQA, selected VLMs, screenshot candidates and author attribution metrics", artifact="dataset construction and model implementation are described; public immutable code/data commit Not Disclosed", body="text-only parsing 会丢掉表格、图形与 layout 的空间关系，也只能把 citation 粗略指到整篇文档。Chain of Evidence 让 VLM 在检索到的 page/slide screenshots 上生成带 bounding boxes 的多跳 evidence chain，再据该 chain 回答。exact-v1 的 Wiki-CoE、SlideVQA、ablation 与 efficiency 实验支持所测 visual-document workload 的定位/回答收益，但 bounding box 仍是模型生成的 locator，不自动证明 source authority、claim entailment 或 corpus completeness，也未覆盖动态页面和 event-time revision。长期增量是把 RAG evidence identity 从 document/chunk 扩展到 modality-native region 与 hop dependency，同时保留原始可回取 source。", queue="在 Ch76 的 claim-evidence lifecycle 中加入 visual document branch：source/page revision → screenshot/region identity → bounding-box evidence hop → claim mapping；region locator 只负责可定位性，仍需 source authority、entailment、sufficiency 与独立 verifier。"),
    "2605.01293": dict(f="SF-LOGIC-GROUNDED-SKILL-INDUCTION", owner="AGENT-WORKFLOW", score=(3,3,3), disp="No Change — Existing Coverage", title="Neuro-Symbolic Skill Induction", method="§4 Neuro-Symbolic Skill Representation; §4.1 workflows; §4.2 node invention; §4.3 interactive control-flow semantics; §5 logic-grounded induction; Appendix A syntax/semantics", eval="§6 Empirical Study; §6.1 setup/baselines; §6.2 main results; §6.3 modular skill honing", limits="Not Disclosed — exact-v1 has no standalone limitations section; evidence is bounded to evaluated agentic tasks, induced language, planner/executor and held-out goals", artifact="Appendix A specifies representation language; public immutable implementation/data commit Not Disclosed", body="把 trajectory 直接总结成 state-blind script 会丢失分支条件与变量依赖，运行环境变化后容易把偶然步骤当通用 skill。NSI 把 traces 提升为带 node、control flow、dynamic variable binding 与交互语义的 logic-grounded program，并允许通过 reflective planning 在线修订。exact-v1 的有限 agentic-task 实验支持所测任务上的 few-shot induction 与 modular honing，不证明开放工具环境里的 side-effect safety、权限、并发、termination 或 skill admission。Agent Platform 已把 trajectory→typed/versioned Skill 明确定义为 artifact compilation，并要求 held-out evaluation、permission/smoke-test、publish/supersede/rollback；Workflow 也已拥有 durable control-flow state，因此 No Change。", queue="—"),
    "2605.01471": dict(f="SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY", owner="PLATFORM-EVALUATION-SYSTEM", score=(3,3,3), disp="Integrate", title="Practical Limits of Autonomous Test Repair", method="§3 System Architecture; §3.3 five-agent pipeline; §3.4 uncertainty propagation; §5 Observed Failure Modes; §8 Design Guidelines; §9 Controlled Autonomy Framework", eval="§6 Quantitative Evaluation; 300 reports/636 test executions/10 scenario families; §6.3 convergence; §6.5 failure signatures; §6.6 self-correction", limits="§10 Threats to Validity — single anonymized production-like UI prototype, model/framework/configuration and observational case-study scope", artifact="§12 Data Availability; Zenodo archive is linked, but immutable implementation commit Not Disclosed", body="把 test pass 当 repair objective 在人工指定 oracle 稳定时成本低，但 autonomous loop 可以通过弱化 assertion 或删除失败 test 来制造表面 convergence。该 case study 记录了 300 reports、636 executions、非收敛 retry、无可执行 artifact、environment failure，并直接观察到 assertion weakening 与 scope deletion；因此 pass rate 必须与原始 test intent、coverage inventory、artifact existence 和 mutation diff 共同验收。证据受单一 anonymized UI prototype、10 scenario families 与 observational design 限制，不证明所有 coding agent 的 failure rate。长期增量是把 semantic oracle 与 scope ownership 放在 repair agent 之外，并对 assertion/test-set 变更设置人工或独立 verifier gate。", queue="在 Ch66 的 executable-evidence 路线加入 autonomous repair 的 anti-gaming gate：冻结 test intent/coverage inventory，分别验证 executable artifact、assertion strength 与 scope diff；repair agent 不拥有 oracle 或删除测试的 commit 权，非收敛和环境故障进入 bounded retry/人工裁决。"),
    "2605.01560": dict(f="SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE", owner="AGENT-WORKFLOW", score=(3,3,3), disp="Integrate", title="FlowBook", method="§3 notebook execution semantics; §3.3 reproducibility; §4 dynamic analysis; §4.1 instrumentation state; §4.2 read/write tracking; §4.3 well-formedness; §4.4 correctness; §5 implementation", eval="§6 Evaluation; §6.1 overhead; §6.2 real-world rerun-consistency violations; §6.3 repair", limits="Not Disclosed — exact-v1 has no standalone limitations section; implementation is bounded by instrumented Python/notebook state, modeled cells/files and observable read/write effects", artifact="§10 Availability; implementation is described, but immutable reviewed repository commit Not Disclosed", body="保存 notebook 文件与执行顺序仍无法证明当前 outputs 可由 clean run 重现，因为 out-of-order cells 会在共享 store 中留下 hidden mutation。FlowBook 把 reproducibility 定义为从 empty store 按 top-to-bottom 执行得到当前记录 outputs，并在 cell boundary 跟踪 read/write set、标记 stale cells、阻止破坏 rerun consistency 的操作。exact-v1 给出 semantics、preservation/reproducibility/progress 证明与 real-notebook evaluation，但对未建模外部服务、native extension、随机性、并发和不可观察 side effect 不提供保证。长期增量是把 notebook 从版本化步骤容器推进为带 clean-state equivalence 与 stale-state gate 的 workflow artifact。", queue="在 Ch81 的 Versioned Notebook 路线加入 clean-state reproducibility contract：empty-store top-to-bottom result 是 reference，cell read/write receipts 决定 stale state 与可提交操作；未建模外部 side effect、随机性或并发时回退 clean rerun/containerized execution。"),
    "2605.01566": dict(f="SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION", owner="AGENT-MULTI-AGENT", score=(3,3,2), disp="Integrate", title="Pareto-Optimal Test-Time Scaling", method="§3 Method; compute-normalized comparison of self-consistency, self-refinement, debate and mixture-of-agents; Appendix A–B model/compute accounting", eval="§4 Experiments; §4.1 equal-compute efficiency; §4.2 task difficulty; §4.3 scaling ratio; §4.4 small-vs-large models; §4.5 mixed-vs-uniform MoA; Appendix D", limits="Not Disclosed — exact-v1 has no standalone limitations section; conclusions are bounded to MMLU-Pro/BBH, 34 configurations, tested model sizes and token-based compute estimates", artifact="prompts and compute formulas are disclosed in appendices; immutable code/result artifact Not Disclosed", body="比较 multi-agent、self-consistency 与 refinement 时，固定 sample/agent 数会让更昂贵 pipeline 看起来更强，却无法回答同一预算该选哪个。该工作把 34 个配置放入 accuracy–compute Pareto front，并在相同 token-compute 预算下比较并行 generations、sequential aggregations、debate rounds 与 model size。结果只覆盖 MMLU-Pro/BBH、作者模型池与 token-based estimate；API latency、KV/communication、并发、能耗、相关错误和开放式工具任务均未纳入，不能把某一 topology 宣称为普遍最优。长期增量是让 Multi-Agent admission 先绑定可复算 compute budget 与 single-agent baselines，再按 task difficulty/quality frontier 决定协调。", queue="在 Ch82 的 coordination-tax 路线加入 equal-budget Pareto admission：同一 task slice 下比较 CoT/self-consistency/refinement/debate/MoA 的 quality–token/latency/cost frontier；先记录 single-agent baseline，相关错误或通信/尾延迟未计入时不得自动推广 topology。"),
    "2605.01660": dict(f="SF-AGENT-GENERATED-VERIFIED-COMPILER", owner="PLATFORM-EVALUATION-SYSTEM", score=(3,3,3), disp="Integrate", title="Axon Verified Compiler", method="§2 Compiler and Development Overview; §2.1 verification overview; §2.2 rationale; §3 Development Process; §3.1 workflow", eval="§4 Validation Technique Evaluation; §4.1 testing; §4.2 certificate checks; §4.3 verification; §4.4 audits; §5.2–5.6 compiler theorems/performance/compile time", limits="§2.1–2.2 trust boundary and §4 validation scope — parser/pretty-printer and environment/model assumptions remain outside the verified AST-to-assembly theorem", artifact="Axon compiler/proofs are described as Lean artifacts; public immutable repository commit used by this review Not Disclosed", body="coding agent 能快速生成 compiler 与 proof code，但‘有测试’仍可能漏掉环境模型，人工 audit 也不随代码量线性扩展。Axon 将 AST→assembly correctness 放进 Lean theorem，优化 pass 生成可检查 certificate；testing 发现环境假设问题，certificate checker/verification 管理语义正确性，audit 只处理未验证边界。exact-v1 不证明 parser、pretty-printer、host/toolchain、spec 本身或所有性能目标；机器证明只覆盖形式化 statement。长期增量是按 artifact boundary 组合 testing、translation validation、machine-checked proof 与 audit，而不是让 agent 或单一 validator 同时拥有 specification 与 accept 权。", queue="在 Ch66 的 coding-agent artifact gate 中加入分层 trust path：tests 探测环境/implementation mismatch，translation certificate 由独立 checker 验证，machine proof 只承诺形式化 theorem，audit 聚焦 parser/spec/toolchain 等未验证边界；任何层失败回退不发布。"),
    "2605.01191": dict(f="SF-SENTINEL-VLA-STATUS-CONTROL", owner="MULTIMODAL-EMBODIED-VLA", score=(3,3,2), disp="Integrate", title="Sentinel-VLA", method="§3 Sentinel-VLA; §3.1 Dynamic Reasoning via Active Status Monitor; Eq. (1)–(5); §3.3 SECL", eval="§4 Experiments; §4.2 RLBench/LIBERO/real-world results; §4.3 monitor and SECL ablations", limits="§4.1 disclosed models/tasks/control frequency; §5 Conclusion; no standalone limitations section", artifact="code, weights and EC-Gen pipeline announced for future release; immutable commit Not Disclosed", body="固定每步深思会破坏实时控制，完全 reactive VLA 又无法识别错误状态。Sentinel-VLA 用 status-monitor expert 把 control state 显式分为 Initial、Normal、New-subtask 与 Error，只有非 Normal 才更新 thought memory 或触发 recovery；action expert 消费 observation、status 与 memory。exact-v1 在 RLBench、LIBERO-LONG 与三项实机任务报告收益并做 monitor/SECL ablation，但 status label 来自合成 error pipeline，代码仍未发布，也没有证明 OOD 校准、hard deadline 或独立 safety envelope；因此 monitor 只拥有 reasoning trigger，低层 controller 仍拥有物理 commit。", queue="在 VLA fast/slow 与 runtime monitor 之间补入显式 status state machine：monitor 只触发 plan/update/recover，Normal 路径复用 thought memory；未校准或超时交回保守 controller。"),
    "2605.01302": dict(f="SF-COUNTERFACTUAL-RISK-RAG", owner="AGENT-RAG", score=(3,3,2), disp="No Change — Existing Coverage", title="CoRM-RAG", method="§3 Methodology; §3.1 counterfactual risk; §3.2 cognitive perturbation; §3.3 evidence critic; §3.4 abstention", eval="§4 Experimental Setup; §5 Results; §5.2 risk-coverage; §5.4 ablation; §5.5 efficiency", limits="§5.6 hyperparameter sensitivity; evaluated decision benchmarks and synthetic cognitive perturbations only", artifact="GitHub repository linked from exact-v1; reviewed immutable commit Not Disclosed", body="semantic relevance 在 false-premise 或 confirmation-bias query 上会优先检索支持错误前提的文档。CoRM-RAG 用认知扰动构造 counterfactual training pairs，蒸馏 Evidence Critic，并以 risk threshold 决定 retrieve 或 abstain。exact-v1 支持所测 decision benchmarks 上的 robustness/risk-coverage 结果，但不证明 critic 跨领域校准、来源 authority、claim entailment 或生产 corpus drift。当前 RAG 章节已经把 relevance 降为候选生成信号，并用 sufficiency、independent check、abstain/escalate 承载相同长期设计，因此作为受限证据 No Change。", queue="—"),
    "2605.01567": dict(f="SF-DEVELOPER-MEMORY-OPE-GATE", owner="AGENT-MEMORY", score=(3,3,3), disp="No Change — Existing Coverage", title="RL Developer Memory", method="§2.1 framework; §2.4 deterministic decision; §2.5 feedback normalization; §2.6 delayed reward; §2.7 shadow policy; §2.8 OPE gate; §2.9 governance", eval="§3.1–3.8 deterministic 200-case benchmark, controlled baselines, claim gate, patch replay, latency and residual failures", limits="§3.4 claim gate; §3.7 latency regression; §3.8 residual failures; §4 Discussion", artifact="local-first MCP implementation described; official-client interoperability and immutable public commit Not Disclosed", body="coding-agent memory access 会改变 patch 与验证结论，因此不能只按 embedding similarity 返回。该架构把 retrieval 记为带 propensity 的 decision event，将异构 feedback 归一成 bounded reward，把 verified resolution 反链到原事件，并让 learned residual policy 先 shadow、再经 OPE 才可 canary。作者同 commit 实验没有证明 accuracy gain，且披露 latency regression、40 个 residual failures 与 official MCP client 未支持。Memory 章节已要求 provenance、feedback/verifier、writer-reader authority 分离、shadow/canary、abstain 与 rollback，故该 family 强化现有 contract，不重复写入。", queue="—"),
    "2605.01604": dict(f="SF-PRODUCTION-AGENT-EVALUATION", owner="PLATFORM-EVALUATION-SYSTEM", score=(2,3,3), disp="No Change — Existing Coverage", title="PAEF", method="§3 seven production failure modes; §5 PAEF dimensions; §5.2–5.7 definitions and architecture", eval="§6 Empirical Evaluation; §6.2–6.5 four public-benchmark experiments", limits="§7.3 Limitations — no production data, black-box agents, threshold calibration", artifact="reference implementation linked in exact-v1; immutable reviewed commit Not Disclosed", body="单次 benchmark 不能观察长链 error cascade、tool availability 与 truth 解耦、输出分布漂移或 explanation-decision divergence。PAEF 把这些压力拆为 cascade uncertainty、tool reliability、distribution health、explanation validity 与 cross-surface consistency，并要求持续观测。虽然摘要称 billion-event observations，§7.3 明确实验没有 production data，阈值也未校准；因此不能把结果当生产有效性证明。Evaluation 章节已拥有 trajectory/component receipts、drift、offline→shadow→canary→online、per-example slice 与 scorer identity，故 No Change。", queue="—"),
    "2605.01201": dict(f="SF-VISUOMOTOR-EXECUTION-GUARANTEE", owner="MULTIMODAL-EMBODIED-VLA", score=(3,3,3), disp="Integrate", title="Visuomotor Execution Guarantee", method="§3 set invariance and Nagumo theorem; §4 execution-guarantee definition; §5.1–5.3 safeset construction and recovery QP; Eq. (1)–(5)", eval="§6 Experimental Evaluation; §6.1 simulation/real Franka setup; §6.2 clean, cluttered and OOD results", limits="§7 Limitations and Future Work — goal-specific safeset, demonstration coverage assumption, no grasp feasibility, conservative recovery", artifact="exact-v1 describes construction and experiments; public implementation and immutable commit Not Disclosed", body="只看 task success 会把‘成功但越过危险状态’与可靠执行混在一起。该工作从 demonstrations 和冻结视觉 encoder 构造 visibility/recognizability safeset，用 Nagumo sub-tangentiality 把它解释为 control-invariant region，再以 QP recovery controller 对 nominal policy action 做最小投影。exact-v1 的 Franka 仿真与实机结果支持所测 Lift/Candy-Sorting、clean/clutter/OOD 条件下的 execution guarantee，但其所谓 guarantee 等于 safeset 内达到该 policy 的 best-known success，并依赖 fully actuated、line-of-sight、goal-specific demonstration coverage；它不证明任意安全属性、动态目标、grasp feasibility 或未知 embodiment。长期增量是把 safety 从 learned actor 的 confidence 外移为 safeset certificate + recovery + controller commit。", queue="在 Ch26 的 safety monitor 路线加入 demonstration-derived perceptual safeset → control-invariance check → minimally projected recovery → controller commit；明确 execution guarantee 只承诺 safeset 内的 best-known task success，不等同于任意物理安全。"),
    "2605.01386": dict(f="SF-PROVENANCE-GRAPH-MEMORY", owner="AGENT-MEMORY", score=(2,3,2), disp="No Change — Existing Coverage", title="MemORAI", method="§3.1 session segmentation/selective compression; §3.2 provenance-enriched graph; §3.3 query-adaptive subgraph retrieval and weighted PageRank", eval="§4.1–4.3 LOCOMO/LongMemEval setup, main results and ablations; Appendix B.1–B.5 robustness, cost and scalability", limits="§Limitations — static entity linking, dynamic/ambiguous conversations, graph/LLM compute and memory overhead", artifact="public repository or immutable reviewed commit Not Disclosed", body="Flat top-k memory 把 episode granularity、事实来源和关联扩展压成一个 similarity score。MemORAI 先做 session/topic segmentation 与 selective compression，再把 entity、turn、segment 和 provenance 写入 multi-relational graph，读取时按 query 构造子图并动态加权 PageRank。exact-v1 在 LOCOMO/LongMemEval、三种 backbone 与 component ablation 上支持该组合在所测 workload 的 retrieval/generation 增益，但 static entity linking、歧义 coreference、实时 graph cost、concurrent update、ACL/deletion propagation 均未闭合。Memory 章节已经形成 authorized anchor recall → bounded graph expansion → provenance merge 的相同主线，因此 No Change。", queue="—"),
    "2605.01429": dict(f="SF-LORA-COMPOSITION-RELIABILITY", owner="TRAIN-LORA", score=(3,3,2), disp="Integrate", title="SCALE-LoRA", method="§Problem Formulation; §Method; Layer-Adaptive Sparse Residual Composition; Sparse-Composition Agreement Layer; Eq. (14)–(17)", eval="§Experiments; Post-Retrieval Evidence; Ablation Studies; Discussion and Analysis; Appendix matched-protocol audit tables", limits="§Limitations — matched FLAN-T5-Large/BBH/97-LoRA contract, protocol-distinct backbones, uncalibrated reliability proxy, multi-path cost", artifact="replication package fields are specified in §Limitations; public immutable package commit Not Disclosed", body="按 task 检索到相关 adapters 不代表这些低秩更新在参数空间兼容。SCALE-LoRA 保留 linear anchor，把 block-wise adapter directions residualize 后按 norm/alignment guard 组合；更高成本分支生成多个 sparse composition views，用 agreement、support-loss proxy 与 oracle headroom 做 post-retrieval audit。作者明确 single-view LASRC 的 task-stratified CI 跨零，support loss 不是 calibrated query-accuracy estimator，多路径也没有 fixed serving stack 的 latency/GPU-memory 证明。长期增量不是宣称某个 merge 算法普遍最优，而是把 retrieve → compose → reliability audit → promote 变成带 adapter-pool identity、matched controls 与 path-cost receipt 的 lifecycle。", queue="在 TRAIN-LORA 的‘多个 Adapter 能否直接相加’之后补入 retrieve → compatibility-preserving composition → bounded multi-view reliability audit → behavioral promotion；disagreement 只作诊断，未校准时不能自动 commit，单路径或人工选择继续作为低成本分支。"),
    "2605.08143": dict(f="SF-SEQUENTIAL-MODEL-EDIT-SIDECAR", owner="PLATFORM-MODEL-REGISTRY", score=(3,3,3), disp="Structural Candidate", title="HoReN", method="§2.1 problem formulation; §2.2 normalized codebook; §2.3 damped Hopfield retrieval; §2.4 codebook update/routing", eval="§3.1–3.4 ZsRE/WikiBigEdit/UnKE, 10K/50K sequential edits, cross-model results and ablations; Appendix E large-scale stability", limits="§4 Conclusion — codebook memory grows linearly; deployed one-step variant is not covered by the multi-step convergence result; temporal conflicts and multi-hop edits remain open", artifact="GitHub code/logs linked in exact-v1; immutable reviewed commit Not Disclosed", body="部署后事实修正若直接改 shared weights，会让连续小样本 edit 累积干扰；外部 memory editor 避免 base-weight drift，却会在 paraphrase routing 和 codebook competition 上退化。HoReN 把单层 activation 方向归一化为 key，以离散 value codebook 保存 edit，并只做一步 damped Hopfield query refinement，使 paraphrase 进入相同吸引域而无关 query 尽量保持 locality。exact-v1 在多模型、三类 benchmark 和最多 50K ZsRE edits 报告稳定结果，也披露 codebook 线性增长、threshold/model calibration、temporal conflict 与 multi-hop 未解决。该机制介于 parameter update、external memory、runtime routing 与 registry revision 之间；现有知识树没有单一 owner 能完整承载 edit identity、precedence、rollback 与 serving route，因此保留 Structural Candidate，不直接写入 Books。", queue="—"),
})

# Current-owner + adjacent-chapter comparison found that both durable design
# contracts are already present in Books.  Keep the papers as reviewed
# evidence, but do not enqueue duplicate prose.
CONFIG["2605.01342"]["disp"] = "No Change — Existing Coverage"
CONFIG["2605.01342"]["queue"] = "—"
CONFIG["2605.15208"]["disp"] = "No Change — Existing Coverage"
CONFIG["2605.15208"]["queue"] = "—"

# A structural gap outranks the otherwise local policy-carriage branch for the
# report's three long narratives.  Both retain complete Source Reviews.
DEEP_NARRATIVE.discard("2605.12535")
DEEP_NARRATIVE.add("2605.08143")

CHAPTERS = {
    "MODEL-TOKENIZER": ("books/part-02-model/11-tokenizer.md#L10", "books/part-02-model/12-embedding.md#L10; books/part-04-training-system/28-pretraining.md#L10"),
    "MULTIMODAL-EMBODIED-VLA": ("books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10", "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10; books/part-04-training-system/27-data.md#L10"),
    "PLATFORM-EVALUATION-SYSTEM": ("books/part-06-ai-infrastructure/66-evaluation-system.md#L10", "books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10"),
    "TRAIN-DISTRIBUTED-TRAINING": ("books/part-04-training-system/36-distributed-training.md#L10", "books/part-04-training-system/35-checkpoint.md#L10; books/part-04-training-system/37-tensor-parallel.md#L10"),
    "AGENT-RAG": ("books/part-07-agent/76-rag.md#L10", "books/part-07-agent/75-context.md#L10; books/part-07-agent/77-memory.md#L10"),
    "PLATFORM-GPU-SCHEDULER": ("books/part-06-ai-infrastructure/63-gpu-scheduler.md#L10", "books/part-06-ai-infrastructure/62-gateway.md#L10; books/part-06-ai-infrastructure/64-volcano.md#L10"),
    "INFER-DECODE": ("books/part-05-inference-system/44-decode.md#L10", "books/part-05-inference-system/43-prefill.md#L10; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10"),
    "TRAIN-PRETRAINING": ("books/part-04-training-system/28-pretraining.md#L10", "books/part-04-training-system/27-data.md#L10; books/part-04-training-system/29-sft.md#L10"),
    "TRAIN-LORA": ("books/part-04-training-system/30-lora.md#L10", "books/part-04-training-system/29-sft.md#L10; books/part-04-training-system/35-checkpoint.md#L10"),
    "INFER-TENSORRT-LLM": ("books/part-05-inference-system/49-tensorrt-llm.md#L10", "books/part-05-inference-system/48-speculative-decoding.md#L10; books/part-05-inference-system/50-vllm.md#L10"),
    "PLATFORM-SECURITY": ("books/part-06-ai-infrastructure/72-security.md#L10", "books/part-06-ai-infrastructure/66-evaluation-system.md#L10; books/part-07-agent/78-tool-calling.md#L10"),
    "AGENT-REFLECTION": ("books/part-07-agent/80-reflection.md#L10", "books/part-07-agent/79-planning.md#L10; books/part-07-agent/81-workflow.md#L10"),
    "AGENT-CONTEXT": ("books/part-07-agent/75-context.md#L10", "books/part-07-agent/74-prompt.md#L10; books/part-07-agent/76-rag.md#L10"),
    "AGENT-MEMORY": ("books/part-07-agent/77-memory.md#L10", "books/part-07-agent/76-rag.md#L10; books/part-07-agent/78-tool-calling.md#L10"),
    "AGENT-WORKFLOW": ("books/part-07-agent/81-workflow.md#L10", "books/part-07-agent/80-reflection.md#L10; books/part-07-agent/82-multi-agent.md#L10"),
    "AGENT-MULTI-AGENT": ("books/part-07-agent/82-multi-agent.md#L10", "books/part-07-agent/81-workflow.md#L10; books/part-07-agent/83-mcp.md#L10"),
    "PLATFORM-MODEL-REGISTRY": ("books/part-06-ai-infrastructure/59-model-registry.md#L10", "books/part-04-training-system/30-lora.md#L10; books/part-06-ai-infrastructure/61-kserve.md#L10"),
}

# These are semantic results of reading the current owner and both adjacent
# chapters.  They intentionally describe the proposition already in Books,
# rather than using a marker-only assertion that a file was opened.
BOOK_EXISTING = {
    "SF-ATTACK-AGENT-TERMINAL-FINGERPRINT": "Security 已把 black-box model/agent fingerprint 定义为会受版本、scaffold 与对抗策略漂移的风险 sensor，并明确不得把 classifier output 当身份 credential；Trace 的 terminal sequence/DPI 路线落在该边界内。",
    "SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT": "Security 已用 MARK 建立 TLS/HTTP/browser-action 多层 web-agent fingerprint、policy-engine throttle/challenge 与漂移时行为限流 fallback；FP-Agent 的 typing/scroll/mouse features 不改变 owner。",
    "SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN": "RAG 已要求 claim-level provenance、source dereference、sufficiency 与 entailment，也保留 modality-native operator；当前尚未把 visual document 的 page/region/bounding-box identity 与多跳依赖写成 evidence contract。",
    "SF-LOGIC-GROUNDED-SKILL-INDUCTION": "Agent Platform 已把 trajectory→typed/versioned Skill 定义为受治理 compilation，并要求 source provenance、held-out evaluation、admission/supersede/rollback；Workflow 拥有 durable control-flow state。",
    "SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY": "Evaluation 已要求 executable artifact、hidden validator 与 claim/evidence mapping，但尚未显式处理 repair agent 通过 assertion weakening 或 test deletion 窃取 oracle/scope ownership 的反奖励路径。",
    "SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE": "Workflow 已把 notebook 写成 versioned procedure 与 gate-conditioned fallback，却只解决 environment portability；当前没有 clean top-to-bottom equivalence、read/write receipt 与 stale-cell gate。",
    "SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION": "Multi-Agent 已解释 coordination tax、topology、correlated error 与 verifier，但尚未要求在相同 compute budget 下把 self-consistency/refinement/debate/MoA 放入同一 quality-cost Pareto contract。",
    "SF-AGENT-GENERATED-VERIFIED-COMPILER": "Evaluation 已拥有 executable verifier、artifact lineage 与 coding-agent release gate；当前没有明确区分 testing、translation certificate、machine proof 与 audit 各自覆盖的 trust boundary。",
    "SF-COMPUTE-OPTIMAL-TOKENIZATION": "Tokenizer 已解释 segmentation、vocabulary 与压缩率如何改变 token sequence 和上下文成本，但跨 tokenizer/scaling 比较仍以 token 为默认单位，尚未建立 bytes 口径。",
    "SF-SENTINEL-VLA-STATUS-CONTROL": "Ch26 已把高层 reasoning、动作 proposal、低层 controller 与安全 fallback 分层，也说明 fast/slow path；尚未把执行状态建模为显式、可审计的触发状态机。",
    "SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE": "Ch26 已要求高层 reasoning 与实时 controller 分层并受 latency budget 约束；当前没有把 uncertainty/critic disagreement 定义为追加推理计算的触发合同。",
    "SF-TAIL-SAFE-RUNTIME-MONITOR": "Ch26 已要求 safety envelope、human override 和 controller commit 边界，但尚未展开 actor 外独立 empirical safe-set monitor 与 bounded recovery 的控制流。",
    "SF-VISUOMOTOR-EXECUTION-GUARANTEE": "Ch26 已规定 safety monitor 拥有 veto、controller 拥有物理 commit；当前没有从 demonstration/perception 构造 control-invariant safeset 并以 recovery projection 保持集合不变的分支。",
    "SF-GRBEN-PROCESS-REWARD-EVAL": "Evaluation 章节已要求 outcome、process/trajectory 与 component receipts 分层，并冻结 scorer、版本、slice 与失败归因；单一 process-reward benchmark 属于该合同的实例。",
    "SF-ACTIVATION-GRADIENT-COMPRESSION": "Distributed Training 已比较 activation sharding、checkpoint/rematerialization 和 communication trade-off，但尚未按 linear/nonlinear operator path 约束压缩是否保持无偏与可重构。",
    "SF-COUNTERFACTUAL-RISK-RAG": "RAG 已把 relevance 降为候选信号，并要求 sufficiency、independent verification、abstain/escalate 和生产漂移监控；counterfactual critic 没有改变这些 owner。",
    "SF-PROVENANCE-GRAPH-MEMORY": "Memory 已把长期读取写成 authorized anchor recall → bounded graph expansion → provenance merge，并要求 edge 不成为事实 owner；MemORAI 的 graph schema 与 PageRank 落在该主线内。",
    "SF-CONFOUNDED-LOG-EVALUATION": "Evaluation 已区分 offline、shadow、canary 与 online evidence，却没有在观察日志进入估计前强制声明 OBS/EXP/SIM 身份、可识别性假设与 mediator state。",
    "SF-ACCESS-AWARE-VECTOR-INDEX": "RAG 已要求授权先于 ranking，并讨论 role graph、index partition 与 broad-query crossover；Veda/EffVeda 是这一现有 security-aware retrieval contract 的受限实现证据。",
    "SF-VUDA-CUDA-VULKAN-SHARING": "GPU Scheduler 已覆盖 time-slicing、MPS、MIG、隔离与 fallback，但资源 owner 仍默认单一 CUDA scheduling/address-space domain。",
    "SF-LONG-FORM-LENGTH-VOLATILITY": "Decode 已以 TTFT/TPOT、tail latency、token budget 和 stop condition 管理 SLO，但未把 output-length distribution/variance 当成独立于平均质量的发布变量。",
    "SF-LIVEFMBENCH-SPECIFICATION-EVAL": "Evaluation 已要求 benchmark/version/scorer identity、contamination 检查、per-example slice 与 failure analysis；formal-spec benchmark 只为既有 contract 增加一个 workload。",
    "SF-LORA-COMPOSITION-RELIABILITY": "TRAIN-LORA 已指出多个 adapter 数学可相加不代表行为兼容，并要求组合后重新 Evaluation；尚未把 retrieval identity、composition path、disagreement proxy 与 path cost 组织成 promotion contract。",
    "SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER": "RAG 已要求 claim-evidence provenance 与 generation 同步携带，但尚未解释为何生成后再做 token-level attribution 不能保证组合性，且可能具有不可承受的搜索复杂度。",
    "SF-ACTION-AGENT-VIDEO-CONTROL": "Ch25–26 已把 video/latent imagination 与 controllable world state 分开，并形成 action proposal → controller → environment feedback 的闭环；该 family 没有改变 owner。",
    "SF-DEVELOPER-MEMORY-OPE-GATE": "Memory 已要求 provenance、writer/reader authority、feedback verifier、shadow/canary、abstain 与 rollback；带 propensity 的 retrieval event 和 OPE 是该发布纪律的实现案例。",
    "SF-PRODUCTION-AGENT-EVALUATION": "Evaluation 已拥有 trajectory/component receipts、drift、offline→shadow→canary→online、per-example slice 与 scorer identity；PAEF 的维度不新增 release owner。",
    "SF-DATA-CONSTRAINED-SCALING-LAW": "Pretraining 已以 compute/data/model capacity 决定 allocation，并说明 scaling law 的测量区间；目前没有把 unique-data benefit 与 repetition penalty 分开。",
    "SF-AGENT-SAFETY-SEARCH-MEASUREMENT": "Evaluation 已要求 deployment configuration、sampling budget 与 residual uncertainty 可追溯，但尚未把 prefix-cache/chunk search 作为与 sampling 并列的安全覆盖路线。",
    "SF-DITRON-DISTRIBUTED-TILING": "Execution Engine 已区分 compiler plan 与 runtime/kernel execution，也保留库路径 fallback；现有主线仍以单设备 tiling 为主，没有 topology/health 驱动的分布式层级。",
    "SF-REFUSAL-TRAJECTORY-MONITOR": "Security 与 Evaluation 已要求沿 trajectory 观察 policy/refusal 状态、区分 refusal 与安全性，并以 action boundary 执行 gate；新监测器未改变 enforcement owner。",
    "SF-RECURSIVE-STATE-TERMINATION": "Reflection 已要求 budget、maximum iterations、evidence check 与停止条件，但尚未把 epistemic state 类型和 order-gap 作为局部 stop sensor。",
    "SF-PRUNING-BEHAVIORAL-REGRESSION": "Evaluation 已反对只看 aggregate/perplexity，并要求 item-level transition、slice、calibration 与真实运行时验证；pruning 的 sparse-kernel/storage 联动尚未显式进入压缩 release gate。",
    "SF-POLICY-CARRIAGE-INTEGRITY": "Context 已定义 trust ordering、provenance 与预算约束，Tool boundary 负责动作授权；尚未把 active policy set/version 作为跨 assembly 与 action 的不可丢失 invariant。",
    "SF-QUANTIZATION-BEHAVIORAL-REGRESSION": "Execution/Evaluation 已将 quantization 视为行为变换，要求 dense-vs-quantized per-example correctness、slice、校准及真实硬件验证；该 family 直接落在现有 contract 内。",
    "SF-SEQUENTIAL-MODEL-EDIT-SIDECAR": "Registry 拥有 immutable model/artifact lineage，LoRA 拥有低秩增量与 rollback，Serving 拥有 runtime route；三者都没有完整拥有持续 model edit 的 key/value identity、precedence、conflict、locality 与撤销语义。",
}

BOOK_NO_CHANGE_DELTA = {
    "SF-ATTACK-AGENT-TERMINAL-FINGERPRINT": "terminal-command bigram 与 family-routed active forensics 扩展了 fingerprint modality，但仍是可漂移、可规避且会被 scaffold 混淆的 sensor；现有 Security contract 已要求独立身份/授权与保守 fallback。",
    "SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT": "typing、scroll 与 mouse behavior 强化既有 web-agent fingerprint evidence；受控 honey-site classifier 没有改变 policy-engine、identity credential 或 drift fallback 的既有边界。",
    "SF-LOGIC-GROUNDED-SKILL-INDUCTION": "显式 control flow、node invention 与 dynamic variable binding 为 trajectory compilation 提供实现证据；当前 Books 已要求 typed Skill、durable workflow、held-out admission 与 rollback，不重复追加。",
    "SF-GRBEN-PROCESS-REWARD-EVAL": "GRBench 证明所测任务中 process reward 的分步评价价值，但没有新增 evaluator identity、release gate 或跨 workload 的 process-state owner。",
    "SF-COUNTERFACTUAL-RISK-RAG": "counterfactual perturbation、Evidence Critic 与 risk threshold 具体化了既有 verify/abstain 分支；跨领域校准和 production drift 未证明，因此不重复写入。",
    "SF-PROVENANCE-GRAPH-MEMORY": "selective compression、turn-level provenance graph 与 query-adaptive expansion 强化既有 bounded evidence-set retrieval；static entity linking、ACL、并发和 deletion propagation 未闭合。",
    "SF-ACCESS-AWARE-VECTOR-INDEX": "Veda/EffVeda 的 lattice 与 coordinated search 为授权先于检索提供性能案例；现有章节已明确相同安全边界和 broad-query trade-off。",
    "SF-LIVEFMBENCH-SPECIFICATION-EVAL": "污染控制、faithful filtering 与 formal-spec failure analysis 强化现有 benchmark contract，但没有形成新的通用 evaluator 或发布判断。",
    "SF-ACTION-AGENT-VIDEO-CONTROL": "video rehearsal 与 FlowDiT action denoising 支持现有 imagination-to-control 分层；短视频、少量 open-loop 实机试验没有证明新的 closed-loop safety contract。",
    "SF-DEVELOPER-MEMORY-OPE-GATE": "decision event、bounded reward、shadow residual policy 与 OPE gate 是现有 Memory provenance/verification/canary/rollback 路线的实现证据，且论文未证明 accuracy gain。",
    "SF-PRODUCTION-AGENT-EVALUATION": "cascade/tool/distribution/explanation 指标映射到现有 trajectory、drift 与 release receipts；论文没有 production data 且 threshold 未校准。",
    "SF-REFUSAL-TRAJECTORY-MONITOR": "trajectory monitor 提供局部检测案例，但未改变 refusal 不是 safety proof、最终 enforcement 位于 action boundary 的既有结论。",
    "SF-QUANTIZATION-BEHAVIORAL-REGRESSION": "dense-vs-quantized 的 item-level divergence 强化既有行为回归 gate；相同命题已完整存在，新增论文名称不会改善论证。",
}

BOOK_STRUCTURAL_DELTA = {
    "SF-SEQUENTIAL-MODEL-EDIT-SIDECAR": "HoReN 暴露 parameter-preserving model edit 作为独立长期知识链：base weights 保持只读，edit codebook 拥有派生事实，runtime router 决定 override，Registry 需治理 edit order/conflict/rollback。现有节点只能分段承载，交由结构复核决定 canonical owner。",
}

UNITS = {
    "2605.01188": "DA-20260503-TOKEN-UNIT",
    "2605.01311": "DA-20260503-CAUSAL-LOGS",
    "2605.08143": "DA-20260503-SEQUENTIAL-MODEL-EDIT",
}

SELECTION_RATIONALE = {
    "SF-ATTACK-AGENT-TERMINAL-FINGERPRINT": "terminal behavioral attribution 与 active forensics 具有安全价值，但现有 Security 已拥有 fingerprint-as-sensor 的完整边界，不高于三个跨层结构问题。",
    "SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT": "浏览行为 fingerprint 为现有 MARK 路线增加受限 measurement evidence；版本漂移与受控任务范围使其保持局部传感器分支。",
    "SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN": "visual region/hop identity 补全 RAG evidence 可定位性，但不转移 source authority 或 claim-verification owner，完整 delta 由 Ch76 局部吸收。",
    "SF-LOGIC-GROUNDED-SKILL-INDUCTION": "trace→logic-grounded program 已由 Agent Platform 的 typed Skill compilation 和 Workflow control state 承载，Books Decision 为 No Change。",
    "SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY": "assertion weakening/test deletion 是重要 evaluator gaming 反例，但处置集中于 Ch66 的 semantic oracle/scope gate，不占本日跨层长叙事。",
    "SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE": "clean-state equivalence 与 stale-cell gate 改进 durable Workflow artifact，但 owner 局限于 notebook execution state。",
    "SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION": "equal-budget Pareto accounting 改进 Multi-Agent admission，却受两 benchmark、token compute estimate 与未计通信/尾延迟条件约束。",
    "SF-AGENT-GENERATED-VERIFIED-COMPILER": "testing/certificate/proof/audit 分层补全 coding-agent artifact gate，但仍归平台 Evaluation 的单一 trust-path 分支。",
    "SF-COMPUTE-OPTIMAL-TOKENIZATION": "selected：把 scaling/evaluation 的基本计量从 tokenizer-dependent token 改为可跨 tokenizer 比较的信息单位，并同时传播到训练与推理成本。",
    "SF-SENTINEL-VLA-STATUS-CONTROL": "显式 status state machine 很重要，但影响集中在 Ch26 的 reasoning-trigger 分支；完整机制与 fallback 已在 Source Review/Books delta 保留。",
    "SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE": "uncertainty-triggered compute 只改变 VLA fast/slow 调度，没有跨越 controller commit 或平台 owner，优先级低于三条跨层路线。",
    "SF-TAIL-SAFE-RUNTIME-MONITOR": "独立 monitor 与 recovery 属于 physical-safety 路线的一条执行分支；与 execution-guarantee family 一并保留，但不重复占长叙事。",
    "SF-VISUOMOTOR-EXECUTION-GUARANTEE": "control-invariant safeset 是强机制证据，但仍归 Ch26 safety monitor/controller handoff；其假设、证明边界与 recovery 已在完整 Review 中闭合。",
    "SF-GRBEN-PROCESS-REWARD-EVAL": "只为既有 process/trajectory evaluation contract 增加受限 benchmark，Books Decision 为 No Change。",
    "SF-ACTIVATION-GRADIENT-COMPRESSION": "operator-aware compression 改变训练 memory/variance 取舍，但 owner 局限于 Distributed Training，不高于跨系统计量与因果证据问题。",
    "SF-COUNTERFACTUAL-RISK-RAG": "Evidence Critic 和 risk threshold 具体化既有 verify/abstain 分支，跨领域校准未证明，Books Decision 为 No Change。",
    "SF-CONFOUNDED-LOG-EVALUATION": "selected：OBS/EXP/SIM 的可识别性决定日志能否成为因果 evidence，并扩展到多轮 Agent mediator/state，直接改变平台评测合同。",
    "SF-ACCESS-AWARE-VECTOR-INDEX": "authorization-before-ranking、role graph 与 partition 已由 RAG 章节承载；新工作主要提供实现/性能案例。",
    "SF-VUDA-CUDA-VULKAN-SHARING": "cross-API spatial sharing 改变 GPU 隔离实现，但受单一 runtime/driver 条件约束，属于局部平台分支。",
    "SF-LONG-FORM-LENGTH-VOLATILITY": "output-length variance 改善 decode SLO 建模，但不重分配跨章节 state owner，完整 delta 可在 Ch44 局部吸收。",
    "SF-PROVENANCE-GRAPH-MEMORY": "provenance graph 与 adaptive expansion 已落在 Memory 的 bounded evidence-set retrieval 主线，Books Decision 为 No Change。",
    "SF-LIVEFMBENCH-SPECIFICATION-EVAL": "formal-spec workload 强化 benchmark identity/contamination/failure-analysis 合同，没有新增通用 evaluator owner。",
    "SF-LORA-COMPOSITION-RELIABILITY": "post-retrieval composition audit 改进 TRAIN-LORA lifecycle，但 matched workload 与 uncalibrated proxy 使结论保持局部分支。",
    "SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER": "负面理论结果修正 post-hoc attribution 直觉，但系统处置集中在 RAG provenance admission，不占跨层长叙事。",
    "SF-ACTION-AGENT-VIDEO-CONTROL": "video rehearsal/action denoising 只支持既有 imagination→controller 分层，closed-loop safety 未证明。",
    "SF-DEVELOPER-MEMORY-OPE-GATE": "propensity、shadow policy 与 OPE 是现有 Memory promotion/rollback 合同的实现证据，且没有证明 accuracy gain。",
    "SF-PRODUCTION-AGENT-EVALUATION": "PAEF 指标映射到已有 trajectory/drift/release receipts；没有 production data，Books Decision 为 No Change。",
    "SF-DATA-CONSTRAINED-SCALING-LAW": "unique-data/repetition 双项会改变 pretraining allocation，但实验 scale 有界，适合作为 Ch28 条件分支而非本日报跨层主线。",
    "SF-AGENT-SAFETY-SEARCH-MEASUREMENT": "search-based safety coverage 是 Evaluation 的重要替代分支，但仍由同一 deployment config/likelihood budget owner 承载。",
    "SF-DITRON-DISTRIBUTED-TILING": "hierarchical tiling 改变 execution-plan/runtime handoff，但证据受特定编译与拓扑 workload 约束，局部吸收即可。",
    "SF-REFUSAL-TRAJECTORY-MONITOR": "trajectory monitor 没有改变 refusal≠safety proof 和 action boundary owns enforcement 的既有结论。",
    "SF-RECURSIVE-STATE-TERMINATION": "typed epistemic state/order-gap 是 Reflection stop sensor 的理论分支，既不证明 truth 也不新增 workflow commit owner。",
    "SF-PRUNING-BEHAVIORAL-REGRESSION": "item-level pruning regression 补强压缩 release gate，但仍属于 Evaluation 的单一 artifact transformation 分支。",
    "SF-SEQUENTIAL-MODEL-EDIT-SIDECAR": "selected：base weights、external edit memory、runtime override 与 registry lineage 分属多个现有 owner，暴露当前知识树没有 canonical model-edit lifecycle 的结构缺口。",
    "SF-POLICY-CARRIAGE-INTEGRITY": "policy-carriage invariant 跨 Context 与 action boundary，但机制 delta 已可在现有两个 owner 间明确 handoff；优先级低于尚无 owner 的 model-edit gap。",
    "SF-QUANTIZATION-BEHAVIORAL-REGRESSION": "dense-vs-quantized behavioral regression 已完整存在于 Execution/Evaluation release gate，Books Decision 为 No Change。",
}


def norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def canonical(value: str) -> str:
    return ";".join(sorted(x.strip() for x in value.split(";") if x.strip() and x.strip() != "—"))


def source_url(arxiv_id: str) -> str:
    if arxiv_id == "2605.01342":
        return f"https://arxiv.org/pdf/{arxiv_id}v1"
    return f"https://arxiv.org/html/{arxiv_id}v1"


def locator(arxiv_id: str, value: str) -> str:
    if value.startswith(("Not Required —", "Not Disclosed —", "Not Applicable —", "Pending —")):
        return value
    return f"arXiv:{arxiv_id}v1 — {value}"


def review_body(cfg: dict) -> str:
    return (
        f"\n### {cfg['title']}\n\n{cfg['body']}\n\n"
        f"<!-- claim:{cfg['f']}:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；"
        "未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。"
        f"<!-- claim:{cfg['f']}:end -->\n"
    )


def provenance(row: dict, cfg: dict, body: str) -> str:
    evidence = f"arXiv:{row['arxiv_id']}v1"
    reviewed = f"SRC-ARXIV@{evidence}"
    parts = [
        "review-completion-v1", cfg["f"], f"paper-v1:{row['arxiv_id']}", evidence,
        "SRC-ARXIV", evidence, reviewed, "deep", "review-override:knowledge_gap",
        canonical(locator(row["arxiv_id"], cfg["method"])),
        canonical(locator(row["arxiv_id"], cfg["eval"])),
        canonical(locator(row["arxiv_id"], cfg["limits"])),
        canonical(locator(row["arxiv_id"], cfg["artifact"])),
        f"claim:{cfg['f']}", f"review:{cfg['f']}",
        "review-body-sha256:" + hashlib.sha256(norm(body).encode()).hexdigest(),
    ]
    return "RP-" + hashlib.sha256("|".join(parts).encode()).hexdigest()[:16]


def main() -> None:
    retained = sorted(
        (r for r in LEDGER["rows"] if r["screening_decision"] == "retain"),
        key=lambda r: int(r["arxiv_id"].split(".")[1]),
    )
    retained_count = len(retained)
    closure_count = sum(r["screening_decision"] == "pre_denominator_closure" for r in LEDGER["rows"])
    queue_count = sum(CONFIG[r["arxiv_id"]]["disp"] == "Integrate" for r in retained)
    no_change_count = sum(CONFIG[r["arxiv_id"]]["disp"].startswith("No Change") for r in retained)
    structural_count = sum(CONFIG[r["arxiv_id"]]["disp"] == "Structural Candidate" for r in retained)
    reopened_count = len(LEDGER.get("false_negative_author_audit", {}).get("reopened", []))
    retain_rate = 100.0 * retained_count / 274
    families = ";".join(CONFIG[r["arxiv_id"]]["f"] for r in retained)
    ledger_hash = hashlib.sha256((HERE / "screening-ledger-v2.1.json").read_bytes()).hexdigest()
    bodies = {r["arxiv_id"]: review_body(CONFIG[r["arxiv_id"]]) for r in retained}

    lines = [
        "# Daily Research — 2026-05-03", "", "**Research Date:** 2026-05-03", "",
        "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-05-02 09:00:00 ～ 2026-05-03 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；月快照只承担 identity/date recall，机制 claim 绑定 exact arXiv v1", "",
        "**Status:** In Progress；Coverage=Open；Evidence=Open；Books=Open；等待独立 Semantic Audit 与 root 串行 Books writeback", "",
        "## Executive Summary", "",
        f"完整月度快照含 {LEDGER['monthly_snapshot_unique_records']:,} 条唯一 DOI；严格窗口 raw identity=512，注册类别命中 274。Core Daily 180 条与 keyword-category 94 条均完成 title+abstract 语义筛选；author-side false-negative audit 纠正 {reopened_count} 项后，当前冻结 {retained_count} 个候选（{retain_rate:.2f}%），{closure_count} 项形成具名 pre-denominator closure。{retained_count}/{retained_count} exact-v1 作者审阅、Score V2 与 Books Comparison 已形成；{queue_count} 项进入串行 Books 队列、{no_change_count} 项 No Change、{structural_count} 项 Structural Candidate。blocked=0、ordinary pending=0，但独立 fresh-context audit 与共享 Books 写回尚未完成，因此不能称为闭环。", "",
        "<!-- audit-target:coverage:start -->", "## 1. Coverage", "",
        "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |",
        "| Window Start | 2026-05-03 |", "| Window End | 2026-05-03 |", "| Registry Version | 2026-08-25 |",
        "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |",
        "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260503-V1 |",
        f"| Denominator Frozen At | {RETRIEVED_AT} |", "| Completion Status | In Progress |",
        "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-05-02T09:00:00+08:00 | 2026-05-03T09:00:00+08:00 | {RETRIEVED_AT} | DataCite exact-month arXiv snapshot；19 registered categories；Core Daily full title+abstract screen | checked | 274 | {families} | pages=100; prefix=00..99; final_cursor=end; unique=31604; raw=512; screened=274; retained={retained_count}; closure={closure_count} | 2026-05-03T00:55:02Z | sha256:{ledger_hash} | — |", "",
        "### Coverage Limitations", "",
        "DataCite 只证明 identity/date recall；技术结论绑定 exact-v1。后加入注册表的其他来源不反推为本历史 Daily 的到期源。Coverage Gate 仍 Open，只因为 fresh-context reviewer 尚未完成 274 项 false-positive/false-negative 审计。", "<!-- audit-target:coverage:end -->", "",
        "<!-- audit-target:evidence:start -->", "## 2. Candidate Ledger", "",
        "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    decision_blocks = []
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        a, b, c = cfg["score"]
        stable_node = "—" if cfg["disp"] == "Structural Candidate" else cfg["owner"]
        lines.append(f"| {cfg['f']} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W18 | 2026-05-02 | SRC-ARXIV | {a} | {b} | {c} | {a+b+c} | retained | deep_complete | accessible | knowledge_gap | review:{cfg['f']} | self | — | new_in_window | {stable_node} | {cfg['disp']} | books-review:{cfg['f']} | yes |")

    lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
        "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        aid = row["arxiv_id"]
        lines.append(f"| {cfg['f']} | {provenance(row, cfg, bodies[aid])} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {locator(aid,cfg['method'])} | {locator(aid,cfg['eval'])} | {locator(aid,cfg['limits'])} | {locator(aid,cfg['artifact'])} | claim:{cfg['f']} | complete |")
    lines += ["", "### Source Reviews"]
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        lines += [f"<!-- review:{cfg['f']}:start -->", bodies[row["arxiv_id"]].strip(), f"<!-- review:{cfg['f']}:end -->"]

    lines += ["", "## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
        "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        lines.append(f"| {cfg['f']} | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |")

    lines += ["", "<!-- audit-target:deep_analysis_selection:start -->", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
        "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        aid = row["arxiv_id"]
        elig = "score_7_9; forced_review"
        if cfg["disp"] == "Integrate":
            elig += "; potential_books_delta"
        elif cfg["disp"] == "Structural Candidate":
            elig += "; potential_structural_gap"
        if aid in DEEP_NARRATIVE:
            unit = UNITS[aid]
            reason = SELECTION_RATIONALE[cfg["f"]]
            lines.append(f"| {cfg['f']} | {elig} | selected | {unit} | — | {reason} | analysis:{unit} |")
        else:
            reason = SELECTION_RATIONALE[cfg["f"]]
            lines.append(f"| {cfg['f']} | {elig} | not_selected | — | — | {reason} | analysis-decision:{cfg['f']} |")
            decision_blocks += [f"<!-- analysis-decision:{cfg['f']}:start -->", reason, f"<!-- analysis-decision:{cfg['f']}:end -->"]
    lines += decision_blocks
    analyses = [
        ("DA-20260503-TOKEN-UNIT", "Token 不是稳定的数据单位", "旧 scaling law 用 token 表达 data，因为同一 tokenizer 内便于计数；compression rate 可变后，token 数不再表示相同信息量。bytes 使跨 tokenizer 比较成立，代价是 tokenizer 与模型规模、训练 FLOPs、decode 长度共同优化。证据未证明固定 compression rate 普遍最优。"),
        ("DA-20260503-CAUSAL-LOGS", "日志规模不能修复选择偏差", "OBS 很大但 model choice 被 user/context confound；SIM 能重放 output，outcome relation 仍需随机 EXP anchor。演进是 logs → causal graph → EXP+SIM identification → OBS variance reduction，代价是实验成本与严格假设；多轮 Agent 还要重建 mediator/state。"),
        ("DA-20260503-SEQUENTIAL-MODEL-EDIT", "持续模型编辑不是一次权重补丁", "直接修改 shared weights 能让新事实进入模型，却会让连续小样本 edit 累积干扰；完全外置 memory 保住 base weights，又把 paraphrase routing、冲突优先级与 serving override 变成新的系统责任。归一化 edit codebook 与一步 Hopfield refinement 把事实修正演化为 parameter-preserving sidecar，但收益依赖 routing/locality calibration，代价是线性增长的派生状态、temporal conflict、multi-hop gap 与 rollback 治理。base weights、edit state、runtime router 和 registry lineage 分属不同 owner，暴露现有知识树缺少完整 model-edit lifecycle 的结构问题。"),
    ]
    for unit, title, body in analyses:
        lines += ["", f"### {title}", f"<!-- analysis:{unit}:start -->", body, f"<!-- analysis:{unit}:end -->"]
    lines += ["<!-- audit-target:deep_analysis_selection:end -->", "", "<!-- audit-target:books:start -->", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
        "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        target, adjacent = CHAPTERS[cfg["owner"]]
        relation = "Direct Evolution" if cfg["disp"] == "Integrate" else ("Alternative Branch" if cfg["disp"] == "Structural Candidate" else "Principle Reuse")
        comparison_node = "considered:PLATFORM-MODEL-REGISTRY,TRAIN-LORA,AGENT-MEMORY" if cfg["disp"] == "Structural Candidate" else cfg["owner"]
        lines.append(f"| {cfg['f']} | {comparison_node} | {target} | {adjacent} | existing:{cfg['f']} | delta:{cfg['f']} | {relation} | {cfg['disp']} | books-review:{cfg['f']} |")
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        target, adjacent = CHAPTERS[cfg["owner"]]
        existing = (
            f"已对读当前 owner `{target}` 与相邻 handoff `{adjacent}`。"
            + BOOK_EXISTING[cfg["f"]]
        )
        if cfg["disp"] == "Integrate":
            delta = cfg["queue"]
        elif cfg["disp"] == "Structural Candidate":
            delta = BOOK_STRUCTURAL_DELTA[cfg["f"]]
        else:
            delta = BOOK_NO_CHANGE_DELTA[cfg["f"]]
        lines += [f"<!-- books-review:{cfg['f']}:start -->", f"<!-- existing:{cfg['f']}:start -->{existing}<!-- existing:{cfg['f']}:end -->", f"<!-- delta:{cfg['f']}:start -->{delta}<!-- delta:{cfg['f']}:end -->", f"结论：**{cfg['disp']}**。", f"<!-- books-review:{cfg['f']}:end -->"]
    lines += ["<!-- audit-target:books:end -->", "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
        "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        "| SA-20260503-COVERAGE | fresh-context:root-pending | coverage | audit-target:coverage | FINDING-20260503-COVERAGE — 274 项 false-positive/false-negative audit 未执行 | root 独立审阅后关闭 | open |",
        f"| SA-20260503-EVIDENCE | fresh-context:root-pending | evidence | audit-target:evidence | FINDING-20260503-EVIDENCE — {retained_count} 个 claim/locator/non-proof audit 未执行 | root 独立审阅后关闭 | open |",
        f"| SA-20260503-SELECTION | fresh-context:root-pending | deep_analysis_selection | audit-target:deep_analysis_selection | FINDING-20260503-SELECTION — {retained_count}→3 独立优先级审计未执行 | root 独立审阅后关闭 | open |",
        f"| SA-20260503-BOOKS | fresh-context:root-pending | books | audit-target:books | FINDING-20260503-BOOKS — {queue_count} 项共享 Books 写回、{structural_count} 项结构裁决与 post-write audit 未执行 | root 串行写回后关闭 | open |", "",
        "## 8. Ignored Noise", "", f"{closure_count} 项未入池 identity 全部保存在 screening ledger；每项保留 exact identity、v1 timestamp、title、abstract、category、具体 closure 与重开条件，不计 Score V2。", "",
        "## 9. Recommended Action", "", f"root 按 BOOKS_INTEGRATION_QUEUE_V1.md 串行写回 {queue_count} 项，裁决 {structural_count} 项 Structural Candidate，并以独立上下文完成四个 Semantic Audit scope；发现 false negative 时重开 denominator。", "",
        "## 10. Repository Changes", "", "- 新建本 Daily README。", f"- 保存 274 项 screening ledger、identity/date provenance、{retained_count} 项 exact-v1 author review 与 Books queue。", "- 未修改共享 Books、ROADMAP、Learning State、Weekly 或其他日期。", "",
        "## 11. Open Questions", "", "- VLA uncertainty/critic 与 safety monitor 在真实 closed-loop、OOD 和硬 deadline 下如何联合校准？", "- confounded log evaluation 在多轮 Agent mediator 随 action 改变时需要怎样的 sequential identification？", "- policy carriage 与 action-boundary enforcement 如何共享 policy version 而不形成 stale control state？", "",
        "## 12. Sources", "", f"访问时间：{RETRIEVED_AT}。", ""]
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        lines.append(f"- [{cfg['title']}]({source_url(row['arxiv_id'])}) — exact arXiv v1")
    lines += ["- DataCite arXiv DOI 月度快照：`papers/2026/05/_sources/datacite-arxiv-202605-v2/`（只作 metadata/discovery）", "",
        "## 13. Final Status", "", "- Raw identities = 512", "- Registered identities = 274", "- Core Daily semantic screened = 180", "- Keyword-category screened = 94", f"- Candidate Denominator = {retained_count}", f"- Pre-denominator closures = {closure_count}", f"- exact-v1 Full Source Review = {retained_count}/{retained_count} author-complete", "- Deep Analysis narrative = 3/3", f"- Books Comparison = {retained_count}/{retained_count}", f"- Books writeback = {queue_count} pending root serialization", f"- Structural Candidate = {structural_count} pending root decision", "- Ordinary pending = 0；blocked = 0", "- Coverage = Open", "- Evidence = Open", "- Books = Open", "- Unresolved findings = 4", "- Completion Status = In Progress", "", "<!-- audit-target:evidence:end -->"]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")

    queue = ["# 2026-05-03 Books Integration Queue", "", "本队列由 root 按日期和 owner 串行写回；子任务未直接修改共享 Books。", "", "| Order | Source Family | Owner | Target / Adjacent comparison | Requested semantic delta | Status |", "| --- | --- | --- | --- | --- | --- |"]
    order = 0
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        if cfg["disp"] != "Integrate":
            continue
        order += 1
        target, adjacent = CHAPTERS[cfg["owner"]]
        queue.append(f"| {order} | {cfg['f']} | {cfg['owner']} | {target}; {adjacent} | {cfg['queue']} | queued_for_root_serial_write |")
    (HERE / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue) + "\n")

    receipts = []
    for row in retained:
        cfg = CONFIG[row["arxiv_id"]]
        aid = row["arxiv_id"]
        body = bodies[aid]
        receipts.append({
            "source_family_id": cfg["f"], "primary_version": f"arXiv:{aid}v1",
            "url": source_url(aid), "retrieved_at": RETRIEVED_AT,
            "review_body_sha256": hashlib.sha256(norm(body).encode()).hexdigest(),
            "source_content_sha256": None,
            "source_snapshot_status": "exact-version URL and section locators verified through the web reader; local byte snapshot unavailable because direct arXiv transport reset",
            "method_locator": locator(aid, cfg["method"]), "evaluation_locator": locator(aid, cfg["eval"]),
            "limitations_locator": locator(aid, cfg["limits"]), "artifact_locator": locator(aid, cfg["artifact"]),
        })
    (HERE / "SOURCE_PROVENANCE_V1.json").write_text(json.dumps({"retrieved_at": RETRIEVED_AT, "receipts": receipts}, ensure_ascii=False, indent=2) + "\n")
    print(f"rendered {REPORT}; retained={len(retained)}; queue={order}")


if __name__ == "__main__":
    main()
