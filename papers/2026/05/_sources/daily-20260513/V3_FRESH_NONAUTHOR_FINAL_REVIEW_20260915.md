# 2026-05-13 V3 Fresh Non-author Final Review

**检查时间：** 2026-09-15T15:52:21+08:00  
**复核者：** fresh non-author reviewer `/root/may17_v3_recert`  
**Review Provenance ID：** `daily-20260513-v3-fresh-nonauthor-final-review-20260915`  
**结论：** **未通过；Daily 保持 `Ongoing`**

## 1. 冻结范围与方法

本轮不扩日期窗口、不重新枚举来源、不修改 Books，只复核 Round 5 已冻结的 838 个身份及 root 已完成的写回：

- 647 个 official-owner-day identity：148 retained、499 pre-denominator closure；
- 191 个 revision/non-owner-route isolation；
- 20 个 Round 5 重开的 false negative；
- 6 个作者保留的 borderline closure；
- 148 个候选的 Evidence、V3 Score、Owner 与 Books comparison；
- 62 个 `No Change — Existing Coverage`；
- 71 个 Books queue item，其中 26 个是 Round 5 新写入或边界修订。

对身份、精确版本、采用命题和证据边界未变化的 128 个旧候选复用已有 exact-v1 审阅，并重新检查其状态、评分、owner 与正文处置；对 20 个 Round 5 重开项重新取得 exact-v1 HTML，核对标题、方法/评价/限制定位及 withdrawal 状态。对 71 个 Books item 逐项比较 queue 的 semantic delta 与 canonical owner 中实际正文，不以 marker 或 `Review notes` 充当语义覆盖。

## 2. 通过项

### 2.1 身份、Evidence 与计数

- `v3-active-evidence.json` 与 `v3-books-comparison.json` 均为 148 个唯一 Source Family，集合完全一致。
- 148 项均有 Evidence Review 与 Books comparison：116 项深入审阅，32 项标准审阅；没有 `Review Pending` 或不可访问候选。
- 20 个 Round 5 重开项的 exact-v1 HTML 全部可访问、标题与身份一致；未观察到论文撤回。`2605.12120` 正文中的 “withdrawn drugs” 是数据集语义，不是 arXiv withdrawal banner。
- 20 项审阅均具体覆盖问题、机制与状态归属、evaluation contract、限制、trade-off/failure/fallback 和 exact-v1 不外推边界，不是摘要模板。
- 191 个 isolation 未被误计入 05-13 候选，也未被本轮改动。

### 2.2 Books queue 与 Round 5 写回

- 71 个 queue Source Family 唯一，全部能在登记的 canonical owner 找到正文 binding；没有跨 owner 重复写入。
- 26 个 Round 5 项全部已实际落入 Books：20 个新增 synthesis、6 个 evidence-boundary repair；26/26 binding 唯一，且均位于 canonical `## Review notes` 之前。
- 26 项正文均保留旧方案、约束变化、机制及 state/control owner、trade-off、failure/fallback 与 exact-v1 证据边界；没有只追加论文摘要或 marker。
- 62 个 `No Change` 中 59 项能绑定真实正文命题。4 个 comparison 使用描述性定位而非标题锚点，其中 `2605.11403`、`2605.11547`、`2605.11730`、`2605.12500` 的正文语义均实际存在，不构成失败。

## 3. 未通过项

### 3.1 三个 pre-denominator closure 仍是假阴性

Round 5 对下列材料使用了合同不存在的额外门槛，例如必须改变 optimizer/checkpoint/distributed runtime、必须跨 workload，或必须影响 Agent commit/recovery。当前研究合同允许范围内的局部证据在确实改变具体设计选择时准入，并要求保持局部证据边界，不能用“未跨 workload”本身关闭。

1. **`2605.11905` — Segment-Level Learning for LLM-Based Theorem Proving**
   - 旧选择是 step-level tactic supervision 与 whole-proof supervision：前者信号密但切碎证明结构，后者保留全局结构但端到端生成复杂。
   - 材料把 supervision unit 改为局部连贯 proof segment，并在训练与短 rollout 中使用同一粒度；这会改变 training-data construction 与 search handoff，而不是只有一个任务分数。
   - 必须重开候选，优先评估 `TRAIN-DATA` 作为 canonical owner，并对 `TRAIN-SFT`/推理搜索作短 handoff；结论仍只限 Lean theorem-proving workload。

2. **`2605.11931` — VISTA**
   - 旧 self-improvement 路径会过采简单样本并依赖语言先验；材料用 partial-correct prefix resampling 和 vision-aware attention score 改变数据 admission 与 post-training signal。
   - 摘要已披露 SFT 与 preference-learning 两个训练分支、多个 MLLM 和任务，不能再以“未跨 workload”关闭；它仍不证明 attention score 是视觉真值。
   - 必须重开候选，优先评估 `TRAIN-SFT`，并对 preference branch 与 `MULTIMODAL-REPRESENTATION` 保留 handoff。

3. **`2605.12201` — RisCoSet**
   - 旧 PAC prediction set 依赖强 monotonicity 和单标签假设，不能表达代码生成中的多个有效输出；材料用 multiple-hypothesis testing 生成带风险控制的 partial-program prediction set。
   - 这改变了生成式代码输出的 uncertainty/evaluation contract；“只在特定 Agent task”不是关闭理由。
   - 必须重开候选，优先评估 `PLATFORM-EVALUATION-SYSTEM`，并将保证严格限制在论文假设、风险定义和受测 code-generation setting。

上述三项尚未进入候选表、评分、Evidence Review 或 Books comparison。因此当前正确账目不是最终冻结分母；不得在修复前沿用 `148 retained / 499 closure` 声称 Gate 闭合。

### 3.2 三个 `No Change` 没有被现有正文真实承载

以下 comparison 只绑定了宽泛章节标题，正文没有覆盖 adopted delta，违反“已有覆盖必须指出实际承载该结论的论点”：

1. **`2605.10974` — Vertex-Softmax**
   - 登记锚点“从目标到证据，而不是从指标到目标”没有承载 score-box 上 tight sound softmax bound、interval-only 的最优性边界，以及进一步收紧需要 score correlation 或 score-value coupling 的结论。
   - 重新比较 `PLATFORM-EVALUATION-SYSTEM`；若无更精确现有命题，应改为 `Integrate`。

2. **`2605.11317` — SOMA**
   - 登记锚点“请求状态机”没有承载由 session 早期 turn 估计 local response manifold、适配小 surrogate、后续切换与回退的机制。
   - 重新比较 `INFER-REQUEST-LIFECYCLE`；若无更精确现有命题，应改为 `Integrate`。

3. **`2605.12446` — ORCE**
   - 登记锚点“从目标到证据，而不是从指标到目标”没有承载 decoupled verbalized-confidence generation、order-aware reward/calibration 及其有限样本和 reference drift 边界。
   - 重新比较 `PLATFORM-EVALUATION-SYSTEM`；若无更精确现有命题，应改为 `Integrate`。

这三项已经完成候选 Evidence Review，但 Books Gate 尚未成立；不能只修 marker，必须由 root 按现有正文重新作语义判断并在需要时写入正文。

### 3.3 活跃状态文件未同步实际结果

| 文件 | 当前不一致 | 必须修复 |
| --- | --- | --- |
| `v3-active-ledger.json` | `counts` 和实际 rows 为 148/499，但 `candidate_ids` 仍为 128，`arithmetic` 仍写 128/519 | 重开上述 3 项后，从实际 rows 重算 candidate IDs、计数与算式 |
| `v3-books-comparison.json` | 20 项仍写 `Root write required`，6 项仍写 `boundary repair required`；总体状态仍称 root 待写 | 在 3 个错误 NoChange 重裁后，同步所有实际 writeback 状态 |
| `v3-root-writeback-queue.json` | `pending_root_count=26`、`root_applied_count=45`，20/6 item status 仍为 pending/repair；同时 summary 又写 `51/51 applied` | 以实际 71 项和后续新增 queue 为唯一状态重算，消除相互矛盾字段 |
| `v3-round5-root-books-synthesis-repair-queue.json` | 6 个 boundary item 仍保留 repair-required 状态，而 root 记录称已完成 | 同步为 applied，并保留 fresh-review 结果 |
| `README.md` | 候选表仍把 3 个错误 NoChange 写成已有覆盖，且叙述仍称下一步只剩 fresh review | 完成有界修复后同步候选表、Evidence/Books 段与最终账目 |

## 4. 有界返修范围

下一轮只需处理本审计指出的增量，不得重新枚举窗口或推倒已通过工作：

1. 将 `2605.11905`、`2605.11931`、`2605.12201` 从 closure 重开，完成 V3 评分、相应深度的 exact-v1 Evidence Review、owner/Books comparison；
2. 重新比较 `2605.10974`、`2605.11317`、`2605.12446` 的真实正文覆盖，必要时形成 root Books synthesis；
3. root 完成必要写入后，同步上述四个 JSON 和 README；
4. 由新的 non-author reviewer 只复核这 6 项、状态守恒与新增写入。已经通过的 145 个候选/closure 判断、59 个 NoChange、71 个既有 queue binding、20 个 Round 5 exact-v1 review 和 191 个 isolation 不重开。

## 5. Gate 决定

- Coverage Gate：**未通过**。三项 false negative 使 Candidate Denominator 尚未冻结。
- Evidence Gate：**局部未通过**。现有 148 项通过，但三项新候选尚未审阅与评分。
- Books Gate：**未通过**。三个 `No Change` 需重裁，且新候选可能产生额外写回。
- Independent Review：**未通过**。

因此 2026-05-13 必须保持 `Ongoing`。修复范围已精确收敛，不需要用户补材料，也不需要重跑其他日期。
