# 2026-09-11 Cross Final Semantic Audit — Deep-B Reviewer

**复核者：** Deep-B reviewer（未参与本文件所审 Batch A、Ch24、Ch27 Root write、Standard decisions 与 Daily 汇总的写作）

**快照时间：** `2026-09-11T17:31:41+08:00`

**复核范围：** Batch A 六个 Books owner（Ch25、Ch26、Ch27、Ch49、Ch56、Ch72），Ch24 的 `2609.10863`，Ch27 的 `2609.11146`，`STANDARD_BOOKS_DECISIONS.md`，以及 `papers/2026/09/11/README.md`。只读对照当前 Research/Report 合同、ROADMAP、exact-v1 review 与正文；未修改 Daily 或 Books。
**结论：** **未通过。** Books 正文的核心语义链与 marker placement 通过，但当前汇总/决策记录仍有四项完成 Gate blocker 和两项需要统一的 owner/status 问题。修复后应定点复查这些行，再把 Daily 的独立复核结论与状态改为完成。

## 阻断 Findings

### P1 — Repository Changes 与当前 Git 事实相反

- **证据：** Daily `README.md:368-376` 声明“未 stage、commit 或 push”；本次快照 `git status --short` 显示本审范围内 Ch24、Ch25、Ch26、Ch27、Ch49、Ch56、Ch72 均为 index-side `M`，Daily 本身为 index-side `A`，`git diff --cached --name-only | wc -l` 为 `276`。
- **为什么阻断：** 项目与 Report 合同要求把实际工作树状态与完成状态分开。已 staged 不能写成未 stage；这一句会把可观察的 repository state 反向陈述。
- **可执行修复：** 将 `README.md:376` 改成当前可证明的边界，例如“本次未 commit/push；当前工作树已有 staged changes，包含本 Daily 与 Books 写回，提交边界由 Root 另行验收”。如果 staging 属于先前流程，明确“本轮未新增 stage”而不要声称整个 worktree 未 staged。

### P1 — `2609.10863` 的 Review 强度在 Daily 与证据账本中冲突

- **证据：** Daily `README.md:71` 标记 `深入完成`；`STANDARD_REVIEW_BATCH.md:5` 声明全批 `7/7 标准审阅完成`，同文件 `:55` 又明确该项为 `标准审阅完成`；`STANDARD_BOOKS_DECISIONS.md:4` 也以“exact-v1 标准审阅完成”为判断基础。与此同时 `RESEARCH_CONTRACT.md:184` 要求 Books `整合` 有深入审阅支持。
- **为什么阻断：** 现有标准记录的内容实际已经较完整地覆盖定理、假设、pilot、failure 与 evidence locations，但状态账本不能一边写 Standard、一边在 Daily 宣称 Deep。机器校验不会识别这类语义状态冲突。
- **可执行修复：** 选择一个真实状态并全链统一。若认定现有阅读已因 Books Integration 触发而达到深入审阅，需在 `STANDARD_REVIEW_BATCH.md` 对该项明确登记 `Books conflict/long-term gap triggered deep review`，补齐/确认实现与 artifact 状态，并把批次总述改成“六项标准 + 2609.10863 深入”；同步修改 Standard decisions 的判断基础。否则不能把 Daily 写成 `深入完成`，且需要重新裁决 Ch24 Integration Gate。

### P1 — `2609.11020` 三维评分被重排

- **证据：** Daily `README.md:82` 为 `2 + 2 + 3 = 7`；`DEEP_REVIEW_BATCH_B.md:26` 与 `DEEP_BOOKS_DECISIONS_B.md:9` 均为 `3 / 1 / 3 = 7`。
- **为什么阻断：** 总分相同不代表三维评分相同。Design Delta 与 System Reach 的定义不同，Daily 不能静默把 `3/1` 改成 `2/2`；这会破坏候选评分口径的可追踪性。
- **可执行修复：** 若没有新的重评分证据，将 Daily 改成 `3 + 1 + 3 = 7`。若要保留 `2 + 2 + 3`，必须在唯一评分 owner 中记录重评分理由，并同步 Deep review 与 Books decision；不能只改报告表格。

### P1 — Fengshui 的 Books Decision 使用不存在的 Stable Node ID

- **证据：** `DEEP_BOOKS_DECISIONS_A.md:17` 将 Ch49 写为 `INFER-EXECUTION-PLAN`；ROADMAP `:102` 的 Ch49 Stable Knowledge Node ID 是 `INFER-TENSORRT-LLM`。Daily `README.md:78` 已使用正确 ID，正文也实际位于 Ch49。
- **为什么阻断：** ROADMAP 是 Stable owner 的唯一事实来源；一个描述性别名不能冒充 Stable Knowledge Node ID。Daily 与所链接的 Books Decision 因此不一致。
- **可执行修复：** 将 `DEEP_BOOKS_DECISIONS_A.md:17` 的 owner 改为 `INFER-TENSORRT-LLM / Ch49`；保留 “execution plan” 作为机制描述而非 owner ID。

## 需要统一的 Major Findings

### P2 — Standard decisions 使用非合同 disposition `Weekly Only`

- **证据：** `STANDARD_BOOKS_DECISIONS.md:14,54,79` 使用 `Weekly Only — Explanatory Analogy`；Report 合同允许的处置是 `整合 / 已有覆盖 / 仅报告 / 结构候选 / 暂缓 / 未纳入本次`（`REPORT_CONTRACTS.md:94,104`），Daily `README.md:79` 已正确写成 `仅报告 — Explanatory Analogy`。
- **风险：** “Weekly Only” 容易被解释为推迟当前 Books 判断，而实际判断是证据只支持解释性类比、因此本 Daily 仅报告且不改 Books。
- **可执行修复：** 将 Standard decisions 三处统一为 `Report Only / 仅报告 — Explanatory Analogy`，并保留“不把 statistical-mechanics 特例提升为生产 Transformer 机制”的现有理由。

### P2 — `2609.10964` 的 owner 改判缺少显式 handoff 理由

- **证据：** `DEEP_REVIEW_BATCH_A.md:518-519` 将 `AGENT-WORKFLOW` 评为 readiness/release ownership 的主 owner，`INFER-SCHEDULING` 只承接 engine admission；`DEEP_BOOKS_DECISIONS_A.md:11` 与 Daily `README.md:77` 最终只登记 `INFER-SCHEDULING / Ch56`。Ch56 正文 `:1143-1160` 的确把 ready set/release budget 归 workflow scheduler、commit turn 归 engine，语义边界成立；ROADMAP 同时存在 `AGENT-WORKFLOW` Ch81（`:134`），且 Ch81 已拥有 `ready-task frontier` 与 workflow/platform scheduling handoff。
- **风险：** 最终 owner 未必错误，但从 source-review proposal 改到 Books owner 没有记录对读后的选择依据，后续可能在 Ch81 重复写入同一机制。
- **可执行修复：** 在 Books Decision A 加一句 owner override：本 family 只吸收 “workflow-to-inference-engine release admission / committed-work accounting”，故 Ch56 为唯一 owner；Ch81 继续拥有 DAG dependency、action/retry/approval 与业务 effect，不重复该算法。若实际想拥有完整 workflow ready-set policy，则应迁至 Ch81，只在 Ch56 留 engine-admission handoff。

## 通过项

- **窗口与 identity：** Daily 窗口为 `2026-09-10T09:00:00+08:00 ～ 2026-09-11T09:00:00+08:00`；Standard/Deep A/B 均将 arXiv 身份绑定 exact-v1 与 Friday new-list 的 `2026-09-11T08:00:00+08:00`，没有把 Atom/submitted 字段改名为首次公开。
- **分母与算术：** `SCREENING_AND_EVIDENCE.md` 含 138 个唯一 arXiv v1 identity；Daily 候选表恰有 40 行，处置计数为 `22 Integrated + 16 Existing Coverage + 1 Report Only + 1 Deferred = 40`，与“原 15 + 新增 25”和 NCP 单项受阻一致。
- **Batch A 正文语义：** ExaServe/Ch56、membership identifiability/Ch72、Story Imprinting/Ch27、ReactHuman+IMLE/Ch26、world-model update fork/Ch25、Fengshui/Ch49 均在正文形成旧约束→状态/控制机制→trade-off/failure→fallback→exact-v1 边界；未把 512-node failure、仿真机器人安全、`11x`、online update、MIA 或 chiplet simulation 外推成普适结论。
- **Ch24：** `2609.10863` 正文明确列出 product/permutation/no-tie/conditional-independence/argmax-compatible 等价条件，分离 source/coupling/schedule、learned field 与 runtime commit，保留原 source/schedule fallback，并把 10K-step single run 限为受限 pilot。语义内容通过；仅 Review 状态账本需修复。
- **Ch27 / `2609.11146`：** 正文正确用 clean-base reset 区分 corpus recursion 与 parameter recursion，分开 concentration、supplier susceptibility、composition 与 human fraction；保留 1–4B、`K<=13`、五代、三 seeds、自然集中度 28%、90% injected probe、未收敛 7–8B 与未公开 code 边界，没有写成“集中度无害”。
- **Standard Existing Coverage：** 2609.10657、10658、10723、10993、11127 的锚点真实存在且与 owner 一致；2609.10976 被限制为理论 analogy，不写入 Self Attention 正文的判断成立。
- **Marker：** `2609.10812/10830/10863/10883/10895/10915/10954/10964/10970/11146` 各有唯一 source-family marker，且均早于目标章节首个 `Review notes`。
- **工具检查：** `python3 scripts/validate_research.py --report papers/2026/09/11/README.md` 通过；该结果只证明 schema/明显一致性，没有消除上述语义状态与 Git 事实问题。

## 完成 Gate

在上述 P1 修复并对 P2 做统一后，定点重跑：三维评分对照、Review/Books 状态对照、ROADMAP owner 检查、marker-before-first-Review-notes、当前 Git state 描述、`validate_research.py` 与 `git diff --check`。随后 Daily `§6` 必须按 `REPORT_CONTRACTS.md:124-125` 增加明确的 `复核者：<身份>`、`结论：通过` 和实际修复摘要，并将顶部 `状态` 从 `进行中` 改为 `完成`；在此之前不能宣称整体 Complete。
