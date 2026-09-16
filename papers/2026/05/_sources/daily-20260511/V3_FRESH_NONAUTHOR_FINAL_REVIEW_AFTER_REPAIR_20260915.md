# 2026-05-11 V3 fresh-context 非作者终审（作者修复与 Books 写回之后）

## 结论

**FAIL — Daily 必须保持 `Ongoing`。**

本轮没有重放来源、扩大日期窗口或修改 Books，只审阅当前 V3 冻结分母、Evidence Review、Books queue、两份 root 写回记录、Daily 正文与对应 Books 主体。既有 46 个候选的证据与 Books 落点总体可信，但高风险 closure 挑战发现 12 个明确 false negative，另有 2 个相邻项需要有界重审；3 个已保留候选的 exact-v1 证据位置不准确或不完整。因此当前分母未冻结，不能把报告标记为 Complete。

## 审阅身份与范围

- 审阅者：`/root/may14_fresh_postwrite`，未参与 2026-05-11 的作者修复或 Books 写回。
- 时间窗口：`2026-05-10 09:00:00 +08:00` ～ `2026-05-11 09:00:00 +08:00`，左闭右开。
- 仅使用当前冻结材料：`V3_SCREENING_LEDGER_20260914.json`、`V3_EVIDENCE_REVIEWS_20260914.json`、`V3_BOOKS_WRITEBACK_QUEUE_20260914.json`、两份 `ROOT_BOOKS_WRITEBACK` 记录及当前 Daily/Books。
- 禁止项：未扩展来源、未读取窗口外事件、未重新枚举 arXiv、未修改 Books。

## 已通过的部分

### 来源、窗口与算术

- Daily registry 共 14 个来源，报告中的来源集合与当前注册表一致。
- 826 个原始 identity 的路由算术成立：635 个 official announcement direct + 191 个 ordinary revision。
- 当前 direct 分母算术成立：635 = 46 retained + 589 pre-denominator closure。
- 当前证据处置算术成立：46 = 15 Integrate + 29 No Change + 2 Weekly Only。
- 46 个 retained Source Family 唯一，未发现同一 family 重复计分。

### exact-v1、撤稿与评分

- 44 个 HTML exact-v1 当前可访问，页面标题与记录一致；页面未出现撤稿声明。
- `2605.06760v1`、`2605.07063v1` 为 PDF-only；exact-v1 PDF 可访问，PDF metadata 标题与记录一致。
- 46 项 Score V2 三个分量均在 0–3，Total 算术正确；所有 Total ≥ 7 与所有 Integrate 项均为 deep review。
- 本轮未发现需要因 withdrawn 状态排除的 retained family。

### Books Decision 与正文绑定

- 29 个 `No Change — Existing Coverage` 均给出具体 owner、既有命题与差异说明；对主张、机制与边界做了逐项正文对读，未发现仅靠 marker 或 Review notes 冒充既有覆盖的项目。
- 15 个 Integrate 的 canonical marker 均只出现一次，位于 ROADMAP 指定 owner 文件内，且全部位于章末 `## Review notes` 之前。
- 15 个正文片段均包含可识别的旧基线、约束变化、机制或 state/control owner、代价/失败模式/回退，以及证据边界；最新 5 个 root 写回与先前 10 个写回均通过此检查。
- 本轮没有修改 Books；上述结论只证明当前 15 个写回成立，不补偿分母 false negative。

### retained false-positive 挑战

对 12 个跨 owner、跨 disposition 的 retained family 做 fresh-context 反向挑战：`2605.06673`、`2605.06676`、`2605.06702`、`2605.06755`、`2605.06841`、`2605.06905`、`2605.06946`、`2605.06997`、`2605.07002`、`2605.07209`、`2605.07363`、`2605.08013`。题摘与采用命题均满足当前 contribution gate，未发现明确 false positive。

## 阻断 Complete 的问题

### P0：Candidate Denominator 存在 12 个明确 false negative

以下项目都来自现有 frozen ledger；完整题摘已经明确描述会改变本项目长期机制、state/control ownership 或 evaluation contract 的增量，不得继续以泛化 closure 理由排除：

| arXiv | Source Family | 必须重开的原因 |
| --- | --- | --- |
| `2605.06731` | When Routine Chats Turn Toxic | cross-session state poisoning、memory write authorization drift 与可回滚审计直接改变 Agent Memory / Security 的状态所有权。 |
| `2605.06761` | Weblica | HTTP-level cache/replay 与环境合成改变 Web Agent 训练环境的 identity、可复现性与控制边界。 |
| `2605.06812` | Towards Security-Auditable LLM Agents | 连接静态 capability 与动态 semantic state 的统一图表示，直接改变 Agent 安全审计的数据模型。 |
| `2605.06898` | Self-Programmed Execution | model completion 接管 orchestrator program，harness 退为评价/边界层，属于明确 control ownership 变化。 |
| `2605.06919` | Can LLMs Take Retrieved Information with a Grain of Salt? | retrieved evidence certainty 与回答服从关系改变 RAG evidence authority 与 calibration contract。 |
| `2605.06978` | Group of Skills | 从 flat skill retrieval 变为带 Start/Support/Check/Avoid role 的 typed execution context，改变 Skill/Context contract。 |
| `2605.06992` | Why Does Agentic Safety Fail to Generalize Across Tasks? | 安全执行映射比任务执行更难泛化，直接约束 Agent Evaluation / Security 的 task-generalization contract。 |
| `2605.07660` | Not All Tokens Learn Alike | attention-entropy 暴露 token-level RL signal/gradient heterogeneity，可能改变 post-training credit assignment 的长期判断。 |
| `2605.07686` | The Coupling Tax | reasoning trace 与 final answer 共用输出预算产生结构性干扰，改变 Inference / Evaluation 的 token-budget contract。 |
| `2605.07769` | Coding Agents Don't Know When to Act | action bias、stale issue 与显式 abstention 直接改变 Agent action admission 和成功判定。 |
| `2605.07806` | Beyond Confidence | 多维 self-assessment 取代单一 verbalized confidence，改变 uncertainty/evaluation contract。 |
| `2605.07937` | Ask Early, Ask Late, Ask Right | clarification timing 与不可逆错误传播直接改变长程 Workflow 的控制点。 |

必须为这 12 项恢复候选身份、执行 exact-v1/withdrawal 检查、Score V2、标准/深入证据审阅、Stable Node/相邻章节对读和最终 Books Decision。只有真实 `Integrate` 项才进入新的 root queue；作者不得自行改 Books 或自签终审。

### P0b：2 个相邻高风险 closure 必须有界重审

- `2605.07701` — Guidance Is Not a Hyperparameter：确认 dynamic CFG control 是否改变 diffusion language generation 的长期控制机制，或以 family-specific 理由维持 closure。
- `2605.07986` — Towards Apples to Apples for AI Evaluations：确认 scenario grounding 是否改变 evaluation contract，或以 family-specific 理由维持 closure。

对照项 `2605.07726` — A Scalable Recipe on SuperMUC-NG Phase 2 当前仍可维持 closure：题摘显示的是训练 recipe/实施组合，尚未给出需要重开分母的独立长期机制。除非上述有界重审发现不可分离 family，不得把修复扩成对 589 个 closure 的全量重跑。

### P1：3 个 exact-v1 Evidence locator 需要修正

- `2605.07568v1`：当前把 §2/§3/§4/§5 记为 Method/Evaluation/Limitations/Conclusion，但 exact-v1 实际为 §2 Related Work、§3 Preliminaries、§4 encoder probe、§5 projector/layer analysis、§6 instruction-tuning evaluation、§7 Conclusion，且没有独立 Limitations 标题。
- `2605.07881v1`：§2.1 是硬件背景、§5.1 是 evaluation methodology；采用机制的核心位置在 §3.1–§3.7，实现在 §4.1–§4.5。当前 Method locator 不足以支持 adopted claim。
- `2605.06733v1`：§3 主要是 problem/theory，GLoRA algorithm 位于 §4.1–§4.3；当前 Method locator 不完整。

只需修正 locator 与相应 Daily 摘要，不改变已经通过的 Books 正文，除非重新审阅改变 adopted claim。

## 精确修复与再次验收

1. 只重开上述 12 + 2 个 frozen-ledger Source Family；`2605.07726` 保持 closure 作为对照。
2. 修正 3 个 evidence locator，并重新核对 Daily 中相同描述。
3. 重算 635 direct 的 retained/closure 分母和 15/29/2 disposition 算术，更新 V3 ledger、evidence、Books queue 与 Daily。
4. 对新 `Integrate` 项由 root 按日期与目标文件冲突顺序写 Books；作者不直接写 Books。
5. 由另一位未参与修复/写回的 reviewer 再做一次 bounded fresh-context 终审。只有不存在未决项、报告与正文一致、validator 与 diff check 通过时，才能将 Daily 标记为 Complete。

## 本轮文件影响

- 新增本独立复核记录。
- 更新 2026-05-11 Daily 的缺口与复核结论。
- 未修改 Books，未 stage、commit 或 push。
