# 2026-06-03 V3 Evidence batch 01

本批覆盖从旧 generic closure 恢复的 8 个 Candidate。题摘只负责准入；以下 Method、Evaluation、Limitations/non-proof locator 来自官方 exact-v1 HTML，`2606.02755v1` 因 HTML 不可用而使用官方 exact-v1 PDF。Books comparison 逐项读取当前 owner 正文；“已有覆盖”指正文机制已存在，不由旧 trace 或旧 `Complete` 授权。

## Candidate evidence 与 Books comparison

### 2606.02581v1 — Cost-Aware Query Routing in RAG

- Evidence：Method=`§III Problem Formulation；§IV System Architecture；§V-A～V-D query signals、strategy bundles、utility 与 token billing`；Evaluation=`§VI、§VII-A～VII-H`；Limitations=`§IX；Appendix B`。
- 结论边界：论文只在 15 句技术 corpus、28 个 query、手工 priors 与禁用 exploration 的 reference harness 上证明 router 会在 bundle 间选择；character/word-count complexity 与 billed tokens 相关很弱，不能外推 learned online routing 或生产最优。
- Books：**Existing / `AGENT-RAG`**。当前正文已经把 retrieval depth、compression、verification、stop、token/latency/cost 与 evidence sufficiency 组成联合 policy，并保留固定检索计划 fallback；本篇没有增加新的 ownership。

### 2606.02606v1 — ReLoRA

- Evidence：Method=`§III-A～III-C adaptive initialization 与 scheduled regularization`；Evaluation=`§IV-A～IV-E`；Limitations=`§VI-C～VI-D`。
- 结论边界：两阶段 adapter re-adaptation 与 Bayesian initialization 只在六项任务、三个 model family 与三个 update source 上支持 time-to-readiness/quality 结果；offline evaluation 不证明 production drift、全量 adapter fleet 或任意 backbone compatibility。
- Books：**Existing / `TRAIN-LORA` + `PLATFORM-MODEL-REGISTRY`**。当前正文已要求 adapter 绑定 base revision、objective、quantization/runtime compatibility，并在 base 漂移后重新验收；兼容性不明时回退旧 adapter/base 配对或重训。

### 2606.02755v1 — Acceptance-Test-Driven Evaluation Protocols for Business-Centric LLM Systems

- Evidence：官方 `arXiv:2606.02755v1` exact-v1 PDF；Method=`requirements-to-acceptance-test protocol 与 pass/fail aggregation`；Evaluation=`business-centric case workflow and executable checks`；Limitations=`结论与讨论中的场景/需求覆盖边界`。官方 HTML 返回 404，不使用 later version 或二手摘要补洞。
- 结论边界：把 stakeholder requirement 编译为 executable acceptance test 能改善业务可解释性，但有限案例不证明 requirement 完备、test oracle 正确或能替代独立 outcome/release owner。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。当前正文已有 EvalSpec、requirement→evaluator artifact、non-vacuous/meta-evaluation admission 与独立 release authority；本篇是该合同的业务案例。

### 2606.02822v1 — Which Defense Closes Which Threat?

- Evidence：Method=`§3.1 engine；§3.2 defense lattice；§3.3 locked probe corpus；§3.6 adversarial paraphrasing`；Evaluation=`§4.1～§4.5`；Limitations=`§5.2 cross-cutting mitigation；§5.3 Threats to validity`。
- 结论边界：四容器、17 probes 与 deterministic stubs 支持 defense-family attribution；degenerate CI、paraphrase brittleness 与单个 real-LLM proxy 不证明 OWASP coverage 完备或生产防御有效。
- Books：**Existing / `PLATFORM-SECURITY` + `PLATFORM-EVALUATION-SYSTEM`**。正文已要求按 threat family、decision boundary、operating point、false positive/negative 与 mutation slice 报告，不能让总覆盖率替代可归因证据。

### 2606.02835v1 — Thinking Past the Answer

- Evidence：Method=`§2 reasoning sufficiency；§3.1 prefix-level trajectory evaluation`；Evaluation=`§3.2、§4.1；Appendix B`；Limitations=`Appendix D`。
- 结论边界：oracle optimal prefix 揭示“首次正确后继续推理而转错”，但答案抽取、verifiable-output benchmark 与 model-dependent difficulty 限制了部署性；论文明确 oracle stopping 不是可直接部署 controller。
- Books：**Existing / `INFER-SCHEDULING` + `PLATFORM-EVALUATION-SYSTEM`**。当前正文已把 reasoning budget、stopping sensor、answer verification 与 release slice 分开，sensor 不能拥有 commit；本篇不改变这一 ownership。

### 2606.02875v1 — Handoff Debt

- Evidence：Method=`§2.1～§2.3 handoff debt/state；§3 context formats；§4.1～§4.4`；Evaluation=`§5.1～§5.5；§6`；Limitations=`§Limitations 的 runtime、predecessor diversity、single-run、task-pool、validation coverage`。
- 结论边界：75 个 SWE-bench Verified source task 产生的 deterministic handoff points 支持 structured notes 降低 successor rediscovery；不证明跨 runtime、人工交接、多轮 predecessor 或未覆盖验证器同样成立。
- Books：**Existing / `AGENT-WORKFLOW`**。正文已要求 handoff artifact 保存 scope、evidence、provenance、authority、prerequisite、fallback 与 execution consequence，并由 successor verifier accept/reject；changed files、validation、uncertainty 与 rollback risk 是同一 contract 的字段化实例。

### 2606.02907v1 — Linear Probes Detect Task Format, Not Reasoning Mode

- Evidence：Method=`§3.1～§3.6 residual format analysis、trace-mode agreement 与 random-direction controls`；Evaluation=`§4；§5.1～§5.4`；Limitations=`§7；Appendix D～J`。
- 结论边界：Qwen3-14B、三个 multiple-choice source 与特定 hidden layer 上，完美 probe separation 被 format/source/length confound 消解；这否定该实验的 reasoning-mode 解释，不证明所有 representation probes 无效。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。当前正文已把 representation probe 限定为 diagnostic sensor，要求 format-controlled counterfactual、random baseline 与 causal intervention；不得直接承担 release gate。

### 2606.02955v1 — Fast-dLLM++

- Evidence：Method=`§3 Fréchet Profile Decoding`；Evaluation=`§5 与 §5.1`；Limitations=`§6；Appendix C calibration-robust certificates`。
- 结论边界：full sorted confidence profile 与 Fréchet bounds 能在所测 LLaDA/Dream、cache regime 与 benchmark 上扩大可提交候选集；marginal-only certificate、dependence approximation 与 calibration 不能证明任意 diffusion LM 的 exact joint correctness 或生产吞吐。
- Books：**Existing / `INFER-SPECULATIVE-DECODING`**。当前正文已经分离 confidence proposal、authoritative verification、ordered token/KV commit 与 fallback，并覆盖 masked diffusion 的 factorization mismatch；本篇只提供受限 selector 实例。

## Batch result

- Evidence complete：8/8。
- Books：8 `Existing`，0 `Integrated`，0 `Only report`，0 `Deferred`。
- exact-v1 blocker：0；`2606.02755v1` 使用官方 PDF，未把 HTML 404 误记为 source blocker。
