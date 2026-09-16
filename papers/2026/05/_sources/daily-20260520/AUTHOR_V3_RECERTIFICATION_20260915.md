# 2026-05-20 V3 作者重认证

- 严格窗口：`[2026-05-19T09:00:00+08:00, 2026-05-20T09:00:00+08:00)`。
- 14 个 Daily 来源均已处理；13 个机构来源有 2 个 Google AI 日期级原始事件，均按 ROADMAP 的 AI for Science 排除项在候选分母前关闭，机构 retained=0。
- arXiv owner 只使用 2026-05-20 08:00+08 的官方 announcement batch；covered-category inventory=575。DataCite created/updated、v1 submission 与 current OAI datestamp 只作 identity/revision 佐证。
- 旧 V2.1 的 727 identity / 75 candidate / Complete 不再拥有当前状态；其中 152 个 revision/其他 owner identity 被排除。
- 作者语义筛选先恢复 `2605.18792`、`2605.18796`、`2605.18824` 三个旧粗筛假阴性，并重认 `2605.18899` 为领域性 closure；随后对 15 个高风险/次级 closure 做 title + full abstract 的有界重审，并在需要时核到 exact-v1。该挑战恢复 11 项：`2605.18813`、`2605.18822`、`2605.18841`、`2605.18857`、`2605.18882`、`2605.19095`、`2605.19220`、`2605.19250`、`2605.19317`、`2605.19322`、`2605.19577`；`2605.18810`、`2605.18999`、`2605.19260`、`2605.19619` 保持 closure，并分别留下非模板理由。
- base owner receipt 的 575 条逐项状态由 `18 closure + 1 pre_denominator_closed + 504 pre_denominator_closure + 52 retained` 构成；三个 closure spelling 先归一化，再应用合计 14 个显式 override，得到 arXiv 算术：`575 = 66 retained + 509 pre-denominator closure + 0 withdrawn`。全日算术：`577 = 66 retained + 511 pre-denominator closure + 0 withdrawn`。
- Evidence：66/66 exact-v1，`66 deep + 0 standard`，评分分布 `8 score7 + 47 score8 + 11 score9`；blocked=0，materials=0。仅复用 identity/version/claim 未变的旧审阅正文，不复用旧 Gate；11 个新恢复项另有可定位的 Method、Evaluation、non-proof boundary 与 adopted claim。
- Books 作者判断：`27 prior Applied + 33 No Change + 6 Integrate + 0 Structural Candidate`。root 已串行写回 6 个 Integrate；当前 33 个正文 binding 均已存在。作者侧只机械确认 27 个既有与 6 个新 marker 全局唯一、锚点顺序正确且位于首个 `## Review notes` 前；33 个 No Change 均绑定当前正文命题。6 项 queue 包含 target path、唯一 marker、正文锚点、采用命题、证据边界、trade-off、failure、fallback 与 exact-v1 locator。
- 作者没有修改共享 Books；6 个 root action 标记为 applied pending fresh non-author post-write semantic review。
- 状态：owner、screening、evidence 与 root writeback 的机械 Gate 通过；Books post-write fresh Gate 未过，Daily 保持 Ongoing，不得由本文件自签 Complete。

## 待 fresh-context 非作者挑战

1. announcement owner 与 09:00 cutoff；575 个 arXiv identity、152 个排除 identity 及 withdrawn=0。
2. 509 个 arXiv closure 与 2 个机构 scope closure 的 false-positive/false-negative challenge；15 个指定高风险项的作者有界重审结果仍须独立挑战。
3. 66 个 exact-v1 review 的 Method、Evaluation、Counterevidence/Limitations、Artifact 与 adopted-claim boundary。
4. 27 个既有 Applied 与 root 写入后的 6 个新 Integrate 正文是否真实承载 old baseline、changed constraint、state/control、evidence boundary、trade-off、failure、fallback；33 个 No Change 是否有充分现有命题。

Cross-model skipped：本文件是作者侧重认证；最终复核必须由独立 fresh-context reviewer 完成。
