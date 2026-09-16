# 2026-05-13 V3 有界六项返修后的独立写后终审

**检查时间：** 2026-09-15T16:33:30+08:00  
**复核者：** fresh non-author reviewer `/root/may13_bounded6_fresh_final`  
**Review Provenance ID：** `daily-20260513-v3-fresh-nonauthor-postwrite-after-bounded-six-20260915`  
**结论：** **未通过；Daily 保持 `Ongoing`**

本 reviewer 未参与六项作者返修和 root Books 写作。本轮不扩日期窗口、来源清单或身份池，不修改 Books；只核验冻结账本、六项修复、当前 Books 正文、状态守恒，并在冻结 closure/candidate 中执行有界 false-negative / false-positive challenge。Cross-model review skipped：本轮是非交互式子任务，未取得单独外部模型授权。

## 1. 冻结范围与账目

- 时间窗保持 `2026-05-12T09:00:00+08:00` ～ `2026-05-13T09:00:00+08:00`，左闭右开。
- `838 = (151 retained + 496 pre-denominator closure + 0 withdrawn) official-owner route + 191 revision/non-owner-route isolation`，实际 rows 与声明一致。
- 151 个 retained Source Family 唯一；`candidate_ids` 也是 151 个唯一身份。
- retained、Evidence Review 与 Books comparison 的 Source Family 集合完全一致，均为 151 项。
- 151 项 Evidence Review 为 117 个 deep、34 个 standard；全部 `accessible`，Method、Evaluation、Limitations、Artifact/claim boundary 字段齐备。
- 14 个 Daily 来源均在 README 中有窗口依据。OpenAI、Qwen、Moonshot 与 Xiaomi Blog 的历史入口无法稳定回溯时，报告已明确隔离该来源限制，没有把空响应写成零命中；这四项限制不支持“全站无遗漏”，也没有被用来扩张 arXiv 分母。

上述机械账目通过不代表 Candidate Denominator 正确；第 3 节的语义挑战仍发现漏收。

## 2. 六项返修与 Books 写回：通过

### 2.1 exact-v1、撤回、评分与 owner

六个 exact-v1 HTML 均可访问，页面标题与 arXiv 身份一致，本次检查未观察到官方 withdrawal banner：

| arXiv | V3 Score | Review | Stable owner | 结论 |
| --- | ---: | --- | --- | --- |
| `2605.10974v1` | 2+2+3=7 | deep | `PLATFORM-EVALUATION-SYSTEM` | score-box softmax 的 interval-only 信息上限与进一步收紧所需结构被准确限定 |
| `2605.11317v1` | 3+2+3=8 | deep | `INFER-REQUEST-LIFECYCLE` | session-local surrogate 的切换、漂移检测与 rollback 属于请求生命周期状态 |
| `2605.11905v1` | 2+2+2=6 | standard | `TRAIN-DATA` | supervision unit 由 open-goal transition 划分，并与 rollout search unit 对齐 |
| `2605.11931v1` | 2+2+2=6 | standard | `TRAIN-SFT` | partial-correct prefix reuse 与 visual-attention sensor 改变 self-improvement 数据回路 |
| `2605.12201v1` | 3+2+3=8 | deep | `PLATFORM-EVALUATION-SYSTEM` | partial-program prediction set、multiple testing 与 selective execution 构成结构化风险合同 |
| `2605.12446v1` | 3+2+3=8 | deep | `PLATFORM-EVALUATION-SYSTEM` | answer generation 与 verbalized confidence 解耦，排序 sensor 不拥有事实 truth |

`2605.12446` 沿用既有 title-based Source Family ID `SF-ORCE-ORDER-AWARE-ALIGNMENT-OF-VERBALIZED-CONFIDENCE-IN-LARGE-LANGUAGE-MO`；它不是缺失 binding，也没有与其他 family 重复。

### 2.2 正文语义与位置

六项均只有一对 `semantic-body-binding:<Source Family>:start/end`，位于 canonical owner 的首个 `## Review notes` 前。正文不是论文摘要或空 marker，并均能定位以下链条：

- 旧基线为何合理；
- workload/状态约束发生了什么变化；
- proposal、sensor、verifier、runtime 或 release gate 分别拥有什么状态和控制权；
- 新增计算、校准、漂移、错误归因、状态版本或 verification 成本；
- 明确 failure mode、保守 fallback 与旧路径继续成立的条件；
- exact-v1 的模型、任务、硬件、搜索预算或统计假设边界，以及未证明的生产/跨模型结论。

因此六项作者返修和 root 写回本身通过独立写后复核，不能再次退回 `No Change` 或 closure。

## 3. 有界 false-negative challenge：未通过

从 496 个冻结 closure 中选取 10 个高风险样本，覆盖 Transformer/optimizer、Agent state/action、multi-model communication、RAG/security、memory evaluation 与多模态 terminal evaluation；只读账本中的完整题摘与具体排除理由，不扩来源或身份池。`2605.11059`、`2605.11172`、`2605.12419`、`2605.10966` 的现有 closure 在本轮可维持窄边界；以下 6 项却明确满足当前合同的贡献入口：

1. **`2605.11136` — EVOCHAMBER**：它不是把单 Agent 方法复制 N 次，而是把可变状态分成个体 context/memory、team composition/collaboration structure 与 population fork/merge/prune/seed，并用非对称知识路由维持 specialization。该增量直接改变 `AGENT-MULTI-AGENT` 的持久状态与 lifecycle owner。
2. **`2605.11167` — The Bicameral Model**：它把多模型/工具协作从文本序列化改为同步 hidden-state coupling、translation interface 与 learned suppression gate。连续通信 channel、锁步执行和 gate authority 是模型/多 Agent 接口的设计分支，不能以“局部模型变体”关闭。
3. **`2605.11169` — OLIVIA**：它在 ReAct Agent 的 action-selection interface 增加 contextual-bandit decision layer、显式 uncertainty 与在线 action-feedback update，且保留 frozen reasoning state。这改变 action proposal 与 deployment-time adaptation 的控制边界，应重开 `AGENT-TOOL-CALLING` / `AGENT-WORKFLOW` owner 对读。
4. **`2605.11225` — PIVOT**：它把 trajectory 作为可执行、可检查、可演化的状态，经过 PLAN→INSPECT→EVOLVE→VERIFY 与 monotonic acceptance 闭环修复 plan-execution gap。现有“局部感知/表示”排除理由与摘要机制不匹配，应重开 `AGENT-PLANNING`。
5. **`2605.11996` — BadSKP**：KG-derived soft prompt 构成独立于文本的 graph-conditioned channel；攻击直接操纵 graph-to-prompt interface，暴露 semantic anchoring 从防御机制转为攻击面的条件。它改变 RAG/soft-prompt trust boundary，应重开 `PLATFORM-SECURITY` 并对 `AGENT-RAG` handoff。
6. **`2605.12477` — MEME**：该评价把 persistent memory 从单实体更新扩展到 multi-entity cascade、absence 与 deletion，并显示多类 memory system 在 dependency reasoning 上失效。它不是仅增加任务条目，而是揭示静态 retrieval 评分无法证明 evolving-memory correctness，应重开 `PLATFORM-EVALUATION-SYSTEM` / `AGENT-MEMORY` 对读。

这六项当前仍处于 `pre_denominator_closure`，没有 V3 score、exact-v1 Evidence Review 或 Books Decision，因此 151/496 不是最终分母。

## 4. 有界 false-positive challenge：通过

对 10 个 retained 样本 `2605.10959`、`2605.10991`、`2605.10993`、`2605.11003`、`2605.11195`、`2605.11217`、`2605.11403`、`2605.11547`、`2605.12396`、`2605.12500` 重新比较题摘、准入理由、V3 分数与处置。它们均提出可定位的机制、状态/控制边界、评价条件或反例；低分/No Change 不等于误收，本轮未发现需要退回分母前的 false positive。

## 5. 状态同步仍未闭合

六项 root 写回已在当前 Books 存在且通过第 2 节复核，但活跃状态仍保留写前值：

- `v3-active-ledger.json` 的六项 `integration_disposition` 仍为 `Integrate — Root write required`；
- `v3-books-comparison.json` 仍声明 `requires_root_write_count=6`，六项 comparison 也仍为 root write required；
- `v3-root-writeback-queue.json` 的六个 item 已写 `root_serial_write_applied_pending_fresh_review`，但顶层仍为 `pending_root_count=6 / root_applied_count=71`；
- README 候选表仍把六项写作“待 root”，与文件开头及当前 Books 不一致。

这些字段应在下一轮和新重开的六项一起从实际 rows 重算；不能用正文 marker 反向替代状态守恒。

## 6. 精确返修范围与 Gate

下一轮只处理以下增量，不重新枚举日期、来源、191 个 isolation 或已经通过的 151 项：

1. 将第 3 节六项从 closure 重开，完成 exact-v1 identity/withdrawal、相应深度 Evidence Review、V3 score、Stable owner 和 Books comparison；
2. root 只对最终判为 `Integrate` 且当前正文没有真实承载的增量串行写入 Books；
3. 从实际 rows 重算 retained/closure、Evidence/Books 集合和 queue 状态，并把已通过的本轮六项同步为 applied + post-write review passed；
4. 新的 non-author reviewer 只复核这六个重开项、必要新增写回和状态守恒。

当前 Gate：

- Coverage source/window boundary：**通过，带四个已隔离的历史入口限制**；
- Candidate Denominator：**未通过，存在 6 个 false negative**；
- Evidence：**现有 151 项通过，新增 6 项尚未审阅**；
- Books：**本轮六项写回通过；新增 6 项尚未作最终 Books Decision**；
- 状态一致性：**未通过**；
- 独立终审：**未通过**。

`scripts/validate_research.py --report papers/2026/05/13/README.md` 与本轮 scoped `git diff --check` 均通过；它们只证明格式和可判定一致性，不能覆盖上述语义漏收与状态冲突。本 reviewer 未修改 Books，未 stage、commit 或 push。
