# 2026-05-05 V3 作者修复审计

**状态：** 作者侧可执行修复与 root LEAP trace reconciliation 已完成；Daily 继续保持进行中，等待新非作者复核。

## 守恒变化

- 修复前：1058 raw = 101 retain + 957 closure。
- 修复后：1058 raw = 123 retain + 935 closure。
- 本轮从 closure 恢复 22 个 family；另将 `2605.02187v1` 合并为现有 semantic family alias，没有增加候选数。
- Evidence：Deep 56、Standard 65、Blocked 2。
- Books：Applied 24、No Change 97、Blocked 2。

## 恢复项

| arXiv v1 | Canonical Source Family | Score | Owner | 作者侧 Books 处置 |
| --- | --- | --- | --- | --- |
| `2605.01058v1` | `SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT` | 7 | `INFER-TENSORRT-LLM` | `Integrate Applied — body marker and root-corrected trace verified; independent review pending` |
| `2605.01293v1` | `SF-NEURO-SYMBOLIC-TRACE-TO-SKILL-COMPILATION` | 7 | `AGENT-PLATFORM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.01386v1` | `SF-MEMORAI-PROVENANCE-AWARE-GRAPH-MEMORY` | 7 | `AGENT-MEMORY` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.01394v1` | `SF-LIVEFMBENCH-FAITHFULNESS-GATE` | 8 | `PLATFORM-EVALUATION-SYSTEM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.01567v1` | `SF-RL-DEVELOPER-MEMORY-OPE-GATE` | 8 | `AGENT-MEMORY` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.01604v1` | `SF-PRODUCTION-AGENT-CONTINUOUS-EVALUATION` | 7 | `PLATFORM-EVALUATION-SYSTEM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.01688v1` | `SF-GRAVITY-GENERATION-TIME-STRUCTURED-ANCHORS` | 7 | `AGENT-MEMORY` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.01758v1` | `SF-FORESIGHT-LOCALIZED-MULTIAGENT-RECOVERY` | 8 | `PLATFORM-SECURITY` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.01847v1` | `SF-NEUROSTATE-COMMITMENT-INTEGRITY` | 7 | `AGENT-MEMORY` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02050v1` | `SF-AI-EVALUATION-RCT-CONTRACT` | 7 | `PLATFORM-EVALUATION-SYSTEM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02122v1` | `SF-STABLEVAL-DISAGREEMENT-AWARE-RANKING` | 8 | `PLATFORM-EVALUATION-SYSTEM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02125v1` | `SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING` | 9 | `TRAIN-DISTRIBUTED-TRAINING` | `Integrate Applied — body marker verified; independent review pending` |
| `2605.02168v1` | `SF-UNBALANCED-MULTIAGENT-COMPUTE-OWNERSHIP` | 7 | `AGENT-MULTI-AGENT` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02179v1` | `SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET` | 9 | `INFER-SCHEDULING` | `Integrate Applied — body marker verified; independent review pending` |
| `2605.02195v1` | `SF-CODE-EVAL-PIPELINE-FALSE-FAILURES` | 9 | `PLATFORM-EVALUATION-SYSTEM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02199v1` | `SF-MEMAUDIT-EXACT-PACKAGE-ORACLE` | 8 | `AGENT-MEMORY` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02209v1` | `SF-SUBMODULAR-BENCHMARK-SELECTION` | 9 | `PLATFORM-EVALUATION-SYSTEM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02307v1` | `SF-SOTOPIA-TOM-INFORMATION-FLOW-EVALUATION` | 7 | `AGENT-MULTI-AGENT` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02363v1` | `SF-STRUCTURED-OUTPUT-TYPED-VALIDATION` | 8 | `PLATFORM-EVALUATION-SYSTEM` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02391v1` | `SF-DP-RUNTIME-MONITORING` | 8 | `PLATFORM-MONITORING` | `Integrate Applied — body marker verified; independent review pending` |
| `2605.02584v1` | `SF-AGENTIC-TOOL-SEQUENCE-PROCEDURE-BOUNDARY` | 7 | `AGENT-WORKFLOW` | `No Change — Existing Coverage (author proposition comparison; independent review required)` |
| `2605.02626v1` | `SF-GRADIENT-GATED-DPO` | 8 | `TRAIN-DPO` | `Integrate Applied — body marker verified; independent review pending` |

## Alias 与日期归属

- `2605.02187v1` 的 generic identity `SF-2026-ARXIV-2605-02187` 只作为 alias；canonical family 是 `SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE`。Books 中已有唯一正文 marker，因此处置为 Applied，不重复计分或写正文。
- `2605.01058v1` 的 canonical family 是 `SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT`。Books 正文已存在；root 已把 trace 从 `2026-05-02` 修正为本日 owner receipt 对应的 `2026-05-05`，没有重写机制正文。
- 独立复核指出的 `2605.03190v1` 属于 2026-05-06，本轮没有把它加入 05-05 分母，也没有修改其他日期或 Books。

## 受影响 closure 理由簇复查

本轮不是按关键词扩池，而是只重开已证实错误理由影响的四个簇。恢复项必须改变 training/runtime interface、跨时间控制状态、evaluation identity 或 Agent state/control ownership。

- training/runtime co-design：恢复 LEAP、FedQueue 与 Gate-DPO。`2605.01214` 仍关闭，因为它是 marginal-token-allocation 立场文，未给出可核验实现或实验机制。
- time-coupled serving/monitoring：恢复 AEGIS 与 DP Runtime Monitoring；前者把跨时隙 deadline-risk budget 变为调度状态，后者把 temporal sensitivity 与 privacy barrier 变为监控发布合同，二者都不能被一次性 latency/metrics 论点替代。
- evaluation identity：恢复 LiveFMBench、production agent continuous evaluation、STABLEVAL、code-eval false failures、RCT contract、MEMAUDIT、benchmark subset admission 与 structured-output typed validation。`2605.02443` 仍关闭：其 composite metric 与 72-config 局部结果没有建立可迁移的 release authority。
- Agent state/control：恢复 trace-to-skill、OPE-gated developer memory、MemORAI、generation-time structured anchors、localized multi-agent recovery、commitment integrity、planner role ownership、SOTOPIA information flow 与 deterministic procedure boundary。`2605.02163` 仍关闭：AST+RAG+Reflexion 的文档维护组合案例未改变现有 workflow owner 或新的跨系统 contract。
- 本轮恢复证明旧的泛化 closure 理由不安全；`V3_CANONICAL_LEDGER.json` 已为恢复项保存具体反证卡，其余 closure 仍保留原始题摘与 family-specific 理由，供新非作者分层抽样。

## Withdrawal、Evidence 与 Books 边界

- 23 个本轮恢复/alias family 的 exact-v1 页面未观察到 withdrawn notice；该检查记录为作者侧访问事实，不替代新非作者复核。
- 作者没有把摘要当全文：已有 packet 项复用 `exact-v1-review-packet.json` 的 Method/Evaluation/Limitations 定位；新增项重新打开 exact-v1 HTML，记录机制、评测与不能外推的边界。
- 97 个 No Change 均已增加具体 Books proposition locator 与短比较，见 `V3_PROPOSITION_BOOKS_COMPARISON.md`。章节名相似不再构成充分证明。
- 作者本轮不写 Books。root 已完成 LEAP trace 的 owner-date 纠正且未重写机制正文；当前还必须执行新非作者最终复核。
