# 2026-05-25 fresh non-author V3 repair queue

状态：**Ongoing / final review failed**。本队列只重开下列 2026-05-25 项，不扩来源、不扩窗口、不全量重扫，不由 reviewer 编辑共享 Books。

## 1. Owner batch

`official-owner-batch-evidence-v3.json` 只给出 announcement cadence 与作者断言的 ID 区间；其指向的旧 receipt 对 97 项仍把 DataCite initial-created day 写成 owner proxy。补 `2605.22823/22824/23904/23905` 的 primary official batch/boundary locator，证明 `2605.22824..2605.23904` 的 announcement membership。若不能证明，把 97 项隔离为 owner-day ambiguous，不能把 DataCite created time 当正面归属。

## 2. Screening false negatives

下列 20 项的 title + full abstract 已经明确给出跨任务可迁移的长期机制，不能保留 generic closure；逐项恢复候选、评分、exact-v1 Evidence 与 Books Decision：

| arXiv | 建议 owner | 题摘已经暴露的 durable delta |
| --- | --- | --- |
| 2605.22864 | PLATFORM-EVALUATION-SYSTEM | 用跨层 trajectory geometry 而非单点 MSP 读取 selective-abstention uncertainty。 |
| 2605.22879 | AGENT-CONTEXT | token/byte budget 下维护 trace graph、append-only history、summary+suffix compaction 与引用计数。 |
| 2605.22885 | AGENT-TOOL-CALLING | formal proof checker + expert iteration + structure-aware scaffold 形成可验证 proof-optimization loop。 |
| 2605.22939 | TRAIN-SFT | DLM 在 diffusion timestep 上按 token learnability 调整 SFT 目标。 |
| 2605.23074 | INFER-DECODE | 只在局部不确定状态按 reflection-marker type 调整 decoding path。 |
| 2605.23099 | AGENT-MULTI-AGENT | 以 debate outcome 更新 posterior-style correctness 并增量构造 communication graph。 |
| 2605.23175 | PLATFORM-SECURITY | key-conditioned watermark generation/detection 明确改变 provider/user ownership contract。 |
| 2605.23180 | AGENT-PROMPT | 单次 forward 的 demonstration likelihood 作为 test-time prompt-embedding zeroth-order optimization signal。 |
| 2605.23189 | PLATFORM-EVALUATION-SYSTEM | 将 score variability 写入 empirical-Bayes conformal nonconformity，同时保留 coverage contract。 |
| 2605.23244 | TRAIN-DPO | reference-free convex preference optimization 改变 alignment compute/state contract。 |
| 2605.23259 | MODEL-TRANSFORMER-LAYER | multi-stream gated residual 在不增加通信的条件下控制 activation growth。 |
| 2605.23344 | INFER-DECODE | uncertainty gate 只在需要时启用 localized visual contrastive branch。 |
| 2605.23382 | TRAIN-RLHF | generic/personal preference reward decoupling、user anchor 与 skill graph 构成个性化 Agent RL state。 |
| 2605.23384 | TRAIN-RLHF | knowledge/regulation 两类 process reward 把 credit 从终态扩展到 reasoning trajectory。 |
| 2605.23398 | TRAIN-DPO | iterative DPO 的 policy trajectory 通过 learned model merging 构造 reference，抑制噪声累积。 |
| 2605.23522 | MULTIMODAL-GENERATIVE-PARADIGMS | SDE exploration schedule 与小步数离散化共同成为 flow-model RL policy identity。 |
| 2605.23753 | AGENT-RAG | dense/entity seed + RL graph expansion 将 KG retrieval 写成有预算的局部决策序列。 |
| 2605.23833 | Structural Candidate / inference compiler owner | dataflow ISA、on-chip memory/parallelism control 与两阶段 compiler search 构成 DNN accelerator execution contract。 |
| 2605.23871 | TRAIN-PRETRAINING | regularized Muon 的 mirror/prox 与 momentum dual state 提供明确 optimizer-state 理论边界。 |
| 2605.23885 | TRAIN-DATA | pretraining corpus 的 bilingual lexical intervention 改变跨语言 transfer 的数据控制面。 |

同理由的 bounded reopen 集合（先过 title + full abstract 贡献判定，只有通过才读 exact-v1）：`2605.23171, 2605.23226, 2605.23315, 2605.23381, 2605.23458, 2605.23497, 2605.23556, 2605.23591, 2605.23595, 2605.23605, 2605.23610, 2605.23645, 2605.23668, 2605.23719, 2605.23780, 2605.23825, 2605.23826, 2605.23889, 2605.23892, 2605.23902, 2605.23903`。

## 3. Evidence

- `2605.22850`：替换 `section Section identity in frozen exact-v1 receipt`；method/evaluation/non-proof 必须有真实 exact-v1 locator。
- `2605.22873`：limitations locator 改为 current exact-v1 `§5 Limitations and Future Work`，不是 `§11`。
- `2605.22967`：两项 compute trade-off 位于 current exact-v1 `§6 Limitations`，不是 `§5`。
- `2605.23476`：把 topic label 改为可重放的 `§§II-III` 理论与 `§IV` numerical validation locator，并写清 proof-of-concept non-proof boundary。
- `2605.22834`、`2605.23857`：当前独立 reviewer 无法取得可重放 exact-v1 body；核心摘要命题可暂存，但不得把完整 boundary 视为已独立通过。只重开这两项材料。
- `2605.23491`：terminal isolation 通过；继续 Deferred，不进 Books。fresh HTML 为 internal error、fresh PDF 为 connection reset；材料到达后只核 Method、四 benchmark、ablation/common-mode failure、limitations。

## 4. Books

Root 新写 5 项的 marker 均唯一成对且在 `## Review notes` 前；`22873/22967/23476` 正文语义通过，`22834/23857` 只等待 independent exact-v1 boundary replay，不要求先改正文。

Root 另需串行修复两个旧 Applied binding，不改变命题内容：

1. `2605.22949` → `books/part-05-inference-system/56-inference-scheduling.md`：把 marker 从 2606.19376 段之后移回 2605.22949 的 online-calibration 段，最好改成唯一 paired start/end marker。
2. `2605.23893` → `books/part-02-model/21-moe.md`：把 marker 从 2609.08690 activation-ratio 段之后移回 Complete-muE 的 dense↔MoE hyperparameter-transfer 段，最好改成唯一 paired start/end marker。

53 个 No Change 中，以下 37 项没有 proposition-level existing locator；不能用 owner headings 或 owner-wide summary 代替具体命题比较：

- headings-only：`22882, 22891, 22894, 22896, 22905, 23055, 23057, 23058, 23066, 23067, 23071`
- generic owner summary：`23157, 23168, 23200, 23215, 23218, 23220, 23258, 23262, 23294, 23311, 23348, 23362, 23414, 23454, 23493, 23574, 23590, 23628, 23640, 23657, 23701, 23723, 23764, 23856, 23899, 23904`

每项补现有正文 heading/anchor 或逐字 span，再说明为何新机制不移动 owner、state/control、trade-off、failure/fallback；若比较失败，改为 Integrate 并生成 root queue。

## 5. Institution source receipt

Meta 与 Xiaomi 隔离正确，继续不支持 no-hit。其余正面 `已检查` 项为每个 source 补官方 checked URL、相邻 dated item 的 URL/date；OpenAI 两条 raw event URL 已在 screening ledger，可复用。不要把普通 GitHub commits/PRs 扩入 denominator。

修复后重新冻结 raw/retained/closure/withdrawn、Evidence、score 与 Books 恒等式，运行 validator、JSON、marker uniqueness、算术与 scoped diff-check；仍需另一位 fresh non-author 终审，repair author 不自签 Complete。
