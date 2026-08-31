# 2026-05-11 Stable Marker 与 Report Truth 修复计划

## 审计结论

- 审计时间：2026-09-01（Asia/Shanghai）
- 审计范围：最终 canonical Books queue、27 项 pre-write challenge、当前 Books、`ROADMAP.md`、05-11 README 的 Candidate Ledger / Books Comparison，以及相关 date-local structured artifacts。
- 最终 canonical Books 集合：6 项 `Integrate`、20 项 `No Change — Existing Coverage`、1 项 `Weekly Only — Context`。
- 六项 `Integrate` 的机制正文均真实存在于 canonical owner，owner/path 与 `ROADMAP.md` 一致，exact-v1 claim/non-proof boundary 仍成立；未发现 semantic gap。
- 六项稳定 `<!-- source-family:... -->` marker 在全体 Books 中均为 0 次，因此六项全部属于 **marker-only repair**，不得重复追加或重写机制正文。
- README 与若干上游 artifact 仍保留 pre-write provisional truth：27 项被标为 `Integrate`。这与 `books-prewrite-independent-challenge.json`、`books-writeback-queue-reconciled.json` 和 `post-write-semantic-audit.json` 的 canonical truth 冲突。当前 `Complete / Books Passed` 状态不能替代字段级一致性修复。

## Canonical Truth 与快照

| Artifact | Role | SHA-256 |
| --- | --- | --- |
| `books-prewrite-independent-challenge.json` | 27 项最终 disposition map | `8d2fac1ba701ae8ea84dd6d4e8507bae24b700bff55f162671c3ae954ce12f05` |
| `books-writeback-queue-reconciled.json` | 6 项 writeback + 21 项 closed 的 canonical queue | `96c854a2827169bd0143d805f676a349b07a1e964ae126753b052893784f2ec3` |
| `post-write-semantic-audit.json` | 6/6 写回语义验收 | `5f19266909ab79d4e1a18d3b7dcad6133ad477294ba85b78a517510a2990f6d8` |
| `papers/2026/05/11/README.md` | 待修复 report snapshot | `c5b16e5ce736de3d60e0d7ae2a23bcee2ec0b4f267e5ea8becd04d500e86db0a` |
| `ROADMAP.md` | Stable Node / owner path truth | `fd3a80ec1e49db9a7eb61e3d3c836d39bbfb38530d5b5830517b5eec18bb53e0` |

以上 hash 只绑定本次只读审计看到的工作树快照；执行修复前若文件变化，必须重新定位 anchor，不能盲用旧行号。

## 六项 Marker Binding

### 1. When2Tool

- Source Family：`SF-LLM-AGENTS-ALREADY-KNOW-WHEN-TO-CALL-TOOLS-EVEN-WITHOUT-REASONING`
- Primary：`arXiv:2605.09252v1`
- Owner：`AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md`
- Canonical H2：`Tool Necessity 与 Execution Admission 是两个 Gate`
- 当前机制：把 tool necessity（knowledge / computation / execution-reliability boundary）与 execution admission 分成两个 Gate；模型只决定是否进入工具路径，不获得执行权；不确定时走 catalog、clarify 或 abstain。
- Exact-v1 boundary：Method=`§2 benchmark; §4 probe; §5 Probe&Prefill`；Evaluation=`§3 failure analysis; §5.2–5.3; Appendices B–H`；Limitations=`§7; Appendix F overhead/OOD`。证据不证明开放环境中的通用边界检测或执行安全。
- 唯一 anchor：含 `纯文本回答无法满足任务 contract。调用前应先按三类压力判断` 且同段含 `[受限证据：arXiv:2605.09252v1]` 的段落。
- 修复：在该段之前插入 `<!-- source-family:SF-LLM-AGENTS-ALREADY-KNOW-WHEN-TO-CALL-TOOLS-EVEN-WITHOUT-REASONING -->`。
- 当前 marker count：0；目标 count：1；repair class：`marker-only`。

### 2. Self-evolving Agent capability preservation

- Source Family：`SF-DO-SELF-EVOLVING-AGENTS-FORGET-CAPABILITY-DEGRADATION-AND-PRESERVATION-I`
- Primary：`arXiv:2605.09315v1`
- Owner：`AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md`
- Canonical H2：`Self-evolution 必须按 Capability Vector 发布，而不是按新任务分数发布`
- 当前机制：把新任务增益与旧能力 preservation replay 分成两个 promotion evidence object，按 workflow/skill/model/memory channel 保留 lineage、回滚与 policy acceptance。
- Exact-v1 boundary：Method=`§3 capability erosion; §4 CPE`；Evaluation=`§5 four-channel experiments`；Limitations=`task/model/evolution-loop scope`。证据不证明固定 replay suite 能覆盖未来任务或能力可强制单调。
- 唯一 anchor：含 `Promotion Gate 应冻结一组 capability vector` 且同段含 `[受限证据：arXiv:2605.09315v1]` 的段落。
- 修复：在该段之前插入 `<!-- source-family:SF-DO-SELF-EVOLVING-AGENTS-FORGET-CAPABILITY-DEGRADATION-AND-PRESERVATION-I -->`。
- 当前 marker count：0；目标 count：1；repair class：`marker-only`。

### 3. SimWorld Studio

- Source Family：`SF-SIMWORLD-STUDIO-AUTOMATIC-ENVIRONMENT-GENERATION-WITH-EVOLVING-CODING-AG`
- Primary：`arXiv:2605.09423v1`
- Owner：`MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- Canonical H2/H3：`Research Outlook` → `生成环境本身也是版本化训练状态`
- 当前机制：环境生成器、seed、asset、curriculum parent、validator 和 policy revision 共同成为版本化训练状态；coding Agent 只有 proposal 权，simulator validator 与 curriculum controller 分别拥有校验和纳入训练的控制权。
- Exact-v1 boundary：Method=`§2; §2.1 SimCoder; §2.2 Adaptive Curriculum`；Evaluation=`§3; §3.1–§3.3`；Limitations=`Appendix A; Unreal/Gym navigation/generated-environment scope`。证据不授予 sim-to-real authority。
- 唯一 anchor：含 `因此生成环境不能只是临时脚本输出` 且同段含 `[受限证据：arXiv:2605.09423v1]` 的段落。
- 修复：在该段之前插入 `<!-- source-family:SF-SIMWORLD-STUDIO-AUTOMATIC-ENVIRONMENT-GENERATION-WITH-EVOLVING-CODING-AG -->`。
- 当前 marker count：0；目标 count：1；repair class：`marker-only`。

### 4. MonitoringBench

- Source Family：`SF-MONITORINGBENCH-SEMI-AUTOMATED-RED-TEAMING-FOR-AGENT-MONITORING`
- Primary：`arXiv:2605.09684v1`
- Owner：`PLATFORM-MONITORING` → `books/part-06-ai-infrastructure/67-monitoring.md`
- Canonical H2/H3：`Monitor 也需要独立的 Red-team Loop` → `被观测者会适应 Monitor，固定暴露策略会产生共同盲区`
- 当前机制：red-team generator 搜索绕过 monitor 的 hard negatives，environment verifier/judge 独立确认；monitor 只拥有 observation，最终停止权属于独立 policy owner。
- Exact-v1 boundary：Method=`§3 MonitoringBench threat/monitor task construction`；Evaluation=`§4 semi-automated red-team evaluation`；Limitations=`monitor/model/judge/attack-distribution scope`。证据不证明未知攻击覆盖率。
- 唯一 anchor：含 `每轮结果必须绑定 attack generator` 且同段含 `[受限证据：arXiv:2605.09684v1]` 的段落。
- 修复：在该段之前插入 `<!-- source-family:SF-MONITORINGBENCH-SEMI-AUTOMATED-RED-TEAMING-FOR-AGENT-MONITORING -->`。不要移动现有的 2605.15257 / 2605.15377 markers。
- 当前 marker count：0；目标 count：1；repair class：`marker-only`。

### 5. Causal state binding

- Source Family：`SF-CAUSAL-STATE-BINDING-PREDICTS-ACTION-CONTROL-IN-LANGUAGE-AGENTS`
- Primary：`arXiv:2605.09692v1`
- Owner：`PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Canonical H2：`Action Control 需要 Sensitivity 与 Invariance 双臂证据`
- 当前机制：用 decisive-state sensitivity 与 irrelevant-cue invariance 两类 matched intervention 共同验收 action control，无法构造可信干预时降级为 observational association。
- Exact-v1 boundary：Method=`§2–§3 structured-control lesion/intervention design`；Evaluation=`§4–§5 seven-corpus/open-weight/matched-interface results`；Limitations=`§6–§7`。双臂通过只证明披露任务中的结构耦合，不证明内在 agency 或开放环境迁移。
- 唯一 anchor：含 `EvalSpec 需要冻结 event/state schema` 且同段含 `[受限证据：arXiv:2605.09692v1]` 的段落。
- 修复：在该段之前插入 `<!-- source-family:SF-CAUSAL-STATE-BINDING-PREDICTS-ACTION-CONTROL-IN-LANGUAGE-AGENTS -->`。
- 当前 marker count：0；目标 count：1；repair class：`marker-only`。

### 6. RubricRefine

- Source Family：`SF-RUBRICREFINE-IMPROVING-TOOL-USE-AGENT-RELIABILITY-WITH-TRAINING-FREE-PRE`
- Primary：`arXiv:2605.09730v1`
- Owner：`AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md`
- Canonical H2：`Tool Necessity 与 Execution Admission 是两个 Gate`
- 当前机制：task/registry/state/side-effect-aware rubric 在执行前校验 candidate program；repair 只生成新 proposal，executor 在硬约束通过后才获得 authorize 权。
- Exact-v1 boundary：Method=`§3; §3.2 Pre-Execution Algorithm`；Evaluation=`§4; §4.3–§4.5`；Limitations=`§6; M3ToolEval/API-Bank/generated-rubric calibration scope`。证据不证明远端工具诚实或 rubric 覆盖未建模约束。
- 唯一 anchor：含 `候选 program 还应在执行前依据当前 task` 且同段含 `[受限证据：arXiv:2605.09730v1]` 的段落。
- 修复：在该段之前插入 `<!-- source-family:SF-RUBRICREFINE-IMPROVING-TOOL-USE-AGENT-RELIABILITY-WITH-TRAINING-FREE-PRE -->`。
- 当前 marker count：0；目标 count：1；repair class：`marker-only`。

## README 与 Structured Artifact 真值修复

### 已确认的漂移

1. `README.md` 的 `## 2. Candidate Ledger`：上述 27 个 pre-write challenged family 仍全部显示 `Integrate`；canonical 应为 6 / 20 / 1。
2. `README.md` 的 `## 6. Books Comparison`：27 行比较表仍全部显示 `Integrate`，且对应 27 个 author-lane narrative block 仍写 `Decision=Integrate`；canonical 应为 6 / 20 / 1。
3. `books-comparison.json`：53 项中仍为 `Integrate=27, No Change=26`；应按本计划的 disposition map 改为 `Integrate=6, No Change=46, Weekly Only=1`。
4. `screening-ledger-final.json`：Candidate Denominator 的 `integration_disposition` 仍保留 provisional `Integrate=27`；Evidence/Score/Review 字段不变，只同步 Books disposition 为 canonical 6 / 20 / 1（全体 53 汇总为 `Integrate=6, No Change=46, Weekly Only=1`）。
5. `semantic-independent-audit.json` 的 `final.integrate=27` 与 `books_prewrite.final_integrate=27` 是较早阶段快照。不能覆写或改名其原始 coverage/evidence audit 字段；应追加 `books_final_reconciliation` overlay（6 / 20 / 1）及 reconciliation ref，明确旧 `final` 只代表当次 audit 的 provisional pre-write 输出。
6. README 末尾 Final Status、Gate 表以及 `books-writeback-queue-reconciled.json` / `post-write-semantic-audit.json` 已正确记录六项；修复不得倒退这些通过状态。

### Canonical disposition map（27/27）

| Source Family | Primary | Canonical Books disposition | Owner |
| --- | --- | --- | --- |
| SF-LLM-AGENTS-ALREADY-KNOW-WHEN-TO-CALL-TOOLS-EVEN-WITHOUT-REASONING | arXiv:2605.09252v1 | Integrate | AGENT-TOOL-CALLING |
| SF-EQUIMEM-CALIBRATING-SHARED-MEMORY-IN-MULTI-AGENT-DEBATE-VIA-GAME-THEORET | arXiv:2605.09278v1 | No Change — Existing Coverage | AGENT-MEMORY |
| SF-DO-SELF-EVOLVING-AGENTS-FORGET-CAPABILITY-DEGRADATION-AND-PRESERVATION-I | arXiv:2605.09315v1 | Integrate | AGENT-PLATFORM |
| SF-TEST-TIME-SPECULATION | arXiv:2605.09329v1 | No Change — Existing Coverage | INFER-SPECULATIVE-DECODING |
| SF-SKILLMAS-SKILL-CO-EVOLUTION-WITH-LLM-BASED-MULTI-AGENT-SYSTEM | arXiv:2605.09341v1 | No Change — Existing Coverage | AGENT-MULTI-AGENT |
| SF-SKILL-R1-AGENT-SKILL-EVOLUTION-VIA-REINFORCEMENT-LEARNING | arXiv:2605.09359v1 | No Change — Existing Coverage | AGENT-PLATFORM |
| SF-FROM-DETECTION-TO-RECOVERY-OPERATIONAL-ANALYSIS-ON-LLM-PRE-TRAINING-WITH | arXiv:2605.09370v1 | No Change — Existing Coverage | TRAIN-DISTRIBUTED-TRAINING |
| SF-NEXUS-CONTINUAL-LEARNING-OF-SYMBOLIC-CONSTRAINTS-FOR-SAFE-AND-ROBUST-EMB | arXiv:2605.09387v1 | No Change — Existing Coverage | MULTIMODAL-EMBODIED-VLA |
| SF-SIMWORLD-STUDIO-AUTOMATIC-ENVIRONMENT-GENERATION-WITH-EVOLVING-CODING-AG | arXiv:2605.09423v1 | Integrate | MULTIMODAL-EMBODIED-VLA |
| SF-SWIFT-PROMPT-ADAPTIVE-MEMORY-FOR-EFFICIENT-INTERACTIVE-LONG-VIDEO-GENERA | arXiv:2605.09442v1 | No Change — Existing Coverage | MULTIMODAL-GENERATIVE-PARADIGMS |
| SF-NOT-ALL-THOUGHTS-NEED-HBM-SEMANTICS-AWARE-MEMORY-HIERARCHY-FOR-LLM-REASO | arXiv:2605.09490v1 | No Change — Existing Coverage | INFER-GPU-MEMORY |
| SF-TRUST-ME-IMPORT-THIS-DEPENDENCY-STEERING-ATTACKS-VIA-MALICIOUS-AGENT-SKI | arXiv:2605.09594v1 | No Change — Existing Coverage | AGENT-PLATFORM |
| SF-WORKSPACE-OPTIMIZATION-HOW-TO-TRAIN-YOUR-AGENT | arXiv:2605.09650v1 | No Change — Existing Coverage | AGENT-PLATFORM |
| SF-FORCING-KV-HYBRID-KV-CACHE-COMPRESSION-FOR-EFFICIENT-AUTOREGRESSIVE-VIDE | arXiv:2605.09681v1 | No Change — Existing Coverage | MULTIMODAL-GENERATIVE-PARADIGMS |
| SF-MONITORINGBENCH-SEMI-AUTOMATED-RED-TEAMING-FOR-AGENT-MONITORING | arXiv:2605.09684v1 | Integrate | PLATFORM-MONITORING |
| SF-CAUSAL-STATE-BINDING-PREDICTS-ACTION-CONTROL-IN-LANGUAGE-AGENTS | arXiv:2605.09692v1 | Integrate | PLATFORM-EVALUATION-SYSTEM |
| SF-CALIBRATE-DON-T-CURATE-LABEL-EFFICIENT-ESTIMATION-FROM-NOISY-LLM-JUDGES | arXiv:2605.09702v1 | No Change — Existing Coverage | PLATFORM-EVALUATION-SYSTEM |
| SF-RUBRICREFINE-IMPROVING-TOOL-USE-AGENT-RELIABILITY-WITH-TRAINING-FREE-PRE | arXiv:2605.09730v1 | Integrate | AGENT-TOOL-CALLING |
| SF-KV-RM-REGULARIZING-KV-CACHE-MOVEMENT-FOR-STATIC-GRAPH-LLM-SERVING | arXiv:2605.09735v1 | No Change — Existing Coverage | INFER-KV-CACHE |
| SF-DYSTRUCT-DYNAMICALLY-STRUCTURED-DIFFUSION-LANGUAGE-MODEL-DECODING-VIA-BA | arXiv:2605.09820v1 | No Change — Existing Coverage | MULTIMODAL-GENERATIVE-PARADIGMS |
| SF-ORACLE-POISONING-CORRUPTING-KNOWLEDGE-GRAPHS-TO-WEAPONISE-AI-AGENT-REASO | arXiv:2605.09822v1 | No Change — Existing Coverage | AGENT-RAG |
| SF-PRETRAINING-LARGE-LANGUAGE-MODELS-WITH-MXFP4-ON-NATIVE-FP4-HARDWARE | arXiv:2605.09825v1 | No Change — Existing Coverage | TRAIN-PRETRAINING |
| SF-DISAGMOE-COMPUTATION-COMMUNICATION-OVERLAPPED-MOE-TRAINING-VIA-DISAGGREG | arXiv:2605.11005v1 | No Change — Existing Coverage | TRAIN-PIPELINE-PARALLEL |
| SF-AGENTSHIELD-DECEPTION-BASED-COMPROMISE-DETECTION-FOR-TOOL-USING-LLM-AGEN | arXiv:2605.11026v1 | No Change — Existing Coverage | PLATFORM-SECURITY |
| SF-FRAGBENCH-CROSS-SESSION-ATTACKS-HIDDEN-IN-BENIGN-LOOKING-FRAGMENTS | arXiv:2605.11029v1 | No Change — Existing Coverage | PLATFORM-SECURITY |
| SF-PORTABLE-AGENT-MEMORY-A-PROTOCOL-FOR-CRYPTOGRAPHICALLY-VERIFIED-MEMORY-T | arXiv:2605.11032v1 | No Change — Existing Coverage | AGENT-MEMORY |
| SF-WHAT-HAPPENS-BEFORE-DECODING-PREFILL-DETERMINES-GUI-GROUNDING-IN-VLMS | arXiv:2605.12549v1 | Weekly Only — Context | INFER-PREFILL |

## 执行顺序与验收

1. 先以 canonical disposition map 重渲染 `books-comparison.json`、`screening-ledger-final.json` 和 README 的 Candidate Ledger / Books Comparison / narrative decisions；不得改变 identity、Score V2、Evidence、Access、Review 或 owner 字段。
2. 对 `semantic-independent-audit.json` 保留原阶段事实与既有 schema 字段，追加 reconciliation overlay/ref 来消除“final=27”的阶段歧义；不要改名旧字段，也不要伪造其原审计当时尚未执行的结论。
3. 再按六个 unique anchors 只插 marker；同一 H2 中的 When2Tool / RubricRefine 必须分别绑定各自段落，不得共用模糊 section-level marker。
4. 重新运行 27-ID disposition invariant：README Candidate Ledger、README Books Comparison 表、README narrative、`books-comparison.json`、`screening-ledger-final.json` 必须逐 ID 等于 canonical map。
5. 重新运行 marker invariant：六个 canonical marker 在全体 Books 中各出现且仅出现 1 次；每个 marker 后的首个受限证据段必须含对应 exact-v1 ID，并位于 owner chapter 首个 exact H2 `## Review notes` 之前。
6. 校验 `ROADMAP.md` 的 node/path 映射、目标 H2/H3 存在、anchor 唯一、无新增第二 owner、Markdown、report validator 与 `git diff --check`。

## Scope Safety

本文件是只读审计产物。本轮未修改共享 Books、05-11 README、canonical queue、ROADMAP 或其他日期；后续执行者必须在当前工作树上使用 scoped patch，并保留并行任务的既有修改。

## 2026-09-01 执行 Checkpoint

- Report truth repair：已应用。README Candidate Ledger、Books Comparison table、27 个 narrative decision 与 `books-comparison.json` 已统一为 canonical 6 / 20 / 1。
- Historical phase preservation：已应用。`screening-ledger-final.json` 与 `semantic-independent-audit.json` 的旧阶段字段保持原值，只追加 `books_final_reconciliation` overlay。
- Coverage receipt：已重绑修改后的 `screening-ledger-final.json` SHA-256：`065887a6a3d7ef859b3d7f616663405b7aa919d93260d5084c4398fe30e6828d`。
- Weekly Only audit：已把 2605.12549 的 per-family Review Ref 加入 passed Books Semantic Audit；其 disposition 保持 `Weekly Only — Context`，未写入 Books。
- Marker repair：仍未执行；六项 marker count 仍应由后续 Books 串行 writer 按本计划修复，并接受独立 post-write 检查。
- Validation：report validator、27/27 disposition/owner/queue invariant 与 scoped `git diff --check` 均通过。

Cross-model skipped: non-interactive context.
