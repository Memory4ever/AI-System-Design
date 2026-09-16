# 2026-05-05 V3 新非作者最终语义终审 — 2026-09-15

**复核者：** `fresh-context:may05_fresh_final_review_round2`

**角色隔离：** 本复核者没有参与本日 36 项 closure 恢复、18 项 root 写回或 Books 正文修改。本轮只检查 2026-05-05，不扩大时间窗口，不修改 Books。

**结论：** **FAIL**。Daily 必须保持 `进行中`。52 项 Applied 的 Books 正文通过语义与位置复核，但三个原 `Blocked` family 的 exact-v1 正文已经可以取得；此外一个 Evidence locator 和 `2605.01771` 的 owner 状态仍不一致。在完成这些定点修复及新的非作者复核前，不能签发 Complete。

## 1. 守恒、恢复与评分

- 原始身份守恒可复算：`1058 = 181 retained + 877 pre-denominator closure`；Source Family 与 arXiv identity 均无重复。
- 定点 closure 重审恢复 36 项：18 项已写入 Books、15 项为 proposition-level `No Change`、3 项原标为 `Blocked / Unverified`。
- 当前 Evidence 账面为 `178 complete + 3 blocked = 181`，其中 `94 deep + 84 standard = 178`。
- 181 项三维评分均可复算，分项处于 0～3，Total 等于三项之和；7～9 分项目均进入 deep review。
- 126 项 `No Change` 均有存在的目标章节、非空现有命题和逐命题比较。36 个恢复项中的 15 个 No Change 已逐项回读其 owner 与命题差异，没有发现仅凭主题相似宣称 Existing Coverage 的项目。

这些检查证明账面结构和已完成判断可复用，但不能覆盖下文已恢复的正文材料和状态冲突。

## 2. 52 项 Applied 与 18 项 root 队列

- 52 项 Applied 均能解析到 ROADMAP 中唯一 Stable Node，且对应 Books 正文至少存在一个可定位的 source-family/semantic-body binding。
- 每项正文 binding 都位于目标章节的二级 `## Review notes` 之前。普通项目正文 marker 为一个；`SF-2026-ARXIV-2605-01771` 使用一对 start/end marker，另一个命中位于 Review notes 的证据记录，不构成第二个正文副本。
- 逐项回读 52 个正文块后，没有发现只有 marker、`已吸收` 标签或论文摘要而缺少机制正文的情况。18 项本轮 root 写回都写出了旧路径或适用条件、约束变化、状态/控制 owner、收益边界、trade-off、failure/fallback 与 exact-v1 证据边界。
- 18 项 root 队列实际结果为 17 个新写入加 1 个复用既有 canonical block；没有遗留 Proposed 项。

因此，**Books 写回正文子 Gate 本身通过**。本轮不要求改写这 52 个正文块。

## 3. `2605.01771` 的 canonical owner 判断

root 拒绝在 Ch69 再写一份，并把最终 owner 改为 `PLATFORM-EVALUATION-SYSTEM`，这个语义判断正确：

- exact-v1 的长期增量是区分 outcome compliance 与 process compliance，并要求 evaluation 观察真实 tool/action trace、环境 affordance 与 effect receipt；它首先改变的是验收合同，而不是通用 trace 存储机制。
- Ch66 已有完整 canonical block，明确写出 textual agreement 只是 sensor、typed action trace 与 environment receipt 才能支持 process-compliance judgment，并同时保留开放环境、过度脚本化和 false reject 的 trade-off。
- Ch69 已承载 route/trace 的记录机制；再次插入相同 process-compliance 结论会制造 owner 重复。

但是状态包仍残留旧 owner：

1. `V3_CANONICAL_LEDGER.json` 与 `V3_EVIDENCE_REVIEWS.json` 的 `score_v2.rationale.system_reach` 仍写影响限定在 `PLATFORM-TRACE`。
2. canonical ledger 的 `internal_design_delta_challenge` 仍以 Ch69 的旧缺口和“现有正文仍缺”描述当前状态。
3. root 队列仍把 `stable_node_id` / `target_chapter_path` 写成 `PLATFORM-TRACE` / Ch69，只通过 `actual_books_path` 和 `writeback_resolution` 暗示改判。

**定点修复：** current owner、评分说明、Books binding 与 resolved queue 字段统一为 `PLATFORM-EVALUATION-SYSTEM` / Ch66；若要保留最初提案，必须显式命名为 `proposed_owner` / `proposed_path`，不能继续让旧字段看起来像当前事实。

## 4. Evidence locator 缺口

`SF-2026-ARXIV-2605-01710` 当前 `method_locators` 为空，`method_evidence` 仅写 `Not Disclosed in an independently titled section.`，但同一份 exact-v1 HTML 实际包含可定位的设计章节：

- `5. Adapting provenance ideas for route receipts`
- `6. What a route receipt records`
- `8. What a receipt should cover`
- `Appendix A: Minimal route receipt JSON Schema`

当前 Books 正文对 route receipt 的状态、控制权、trade-off 和回退写入是合理的，不需要改 Books；但 Evidence 包没有记录支撑该机制的实际位置，未满足“记录实际证据位置与解释”的合同。

**定点修复：** 从上述 exact-v1 章节补齐 method locators 与直接证据，并把 claim boundary 明确收窄为 design/schema proposal 加 fictional case study；不能把它表述为已被生产实验验证。

## 5. 三个 `Blocked` 已可重开

2026-09-15 新复查表明三个原受阻 family 的 exact-v1 正文已可取得：

| Source Family | 可用原始材料 | 本次完整性检查 | 下一步 |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-02196` | `https://arxiv.org/pdf/2605.02196v1` | 845013 bytes；PDF 17 页；完整 `%%EOF`；SHA-256 `9e22e82692ed974b6a11d6a4ae4133a3f2c697f931838dcdf6c7420cd16bae9e` | 按 8/9 deep 读取 Method、evaluation、limitations，重新作 Books 判断 |
| `SF-2026-ARXIV-2605-02206` | `https://arxiv.org/pdf/2605.02206v1` | 1668839 bytes；完整 `%%EOF`；SHA-256 `85359e65a7dbe6dee24d32ea8df6ea2802fdb8b01f6346e92f32a4d156fee5cb` | 按 6/9 standard 完成正文审阅，再作 Books 判断 |
| `SF-2026-ARXIV-2605-02375` | `https://arxiv.org/html/2605.02375v1` 与 `https://arxiv.org/pdf/2605.02375v1` | HTML 557391 bytes；PDF 942415 bytes、25 页、完整 `%%EOF`；HTML SHA-256 `cdeb2cb2c2d8028ba4033284d31a9f8c5ea5229d43e3a640f5121b4fe2c09b3c` | 按 6/9 standard 完成正文审阅，再作 Books 判断 |

因此这三项不能继续作为“正文不可得”的终态保留项。作者应只重开这三个 family，不重扫 1058 个 raw identity；若新的 Books 判断为 Integrate，再交 root 按 owner 串行写入，随后由新的非作者 reviewer 复核。

## 6. README 与 active state 过期

Daily 当前仍写“Proposed 尚待 root 写回”“root 应先按队列写入”和“root 写回尚未完成”，与 18/18 已解决、Applied=52、Proposed=0 相冲突。这些不是历史说明，而是 active 状态，必须改成：root 写回已完成且正文复核通过，当前阻断仅为三个已恢复来源的 Evidence/Books 审阅、`01710` locator、`01771` owner state 以及修复后的新非作者复核。

## 7. Gate 判定

- Window / identity conservation：**PASS**。
- Candidate Denominator 与 36 项恢复账面：**PASS**。
- 当前 181 项评分算术：**PASS**。
- 126 项 No Change comparison：**PASS**。
- 52 项 Applied Books 语义、owner、marker 与 Review notes 位置：**PASS**。
- 18 项 root 写回真实结果：**PASS**。
- `2605.01771` 的 Ch66 canonical owner 决策：**PASS**；active owner state：**FAIL**。
- Evidence completeness：**FAIL**；`2605.01710` 缺实际 method locator，三个原 blocked family 已恢复材料但尚未审阅。
- Active README / JSON consistency：**FAIL**。
- Daily：**Ongoing**。

## 8. 再次验收的最小范围

1. 审阅 `2605.02196v1`、`2605.02206v1`、`2605.02375v1` 的已恢复正文，更新 Review、Books disposition 和汇总计数。
2. 补齐 `2605.01710v1` 的设计章节 locator 与证据边界。
3. 统一 `2605.01771v1` 的 resolved owner/state 字段，并清理 README 的 root-pending 旧状态。
4. 若三项恢复来源产生新的 Integrate，由 root 写入后再复核；否则保留可验证的 No Change / Disputed 结论。
5. 由未参与上述修复与任何新增 Books 写回的新非作者 reviewer，只复核这四个 Evidence 项、`01771` 状态一致性和可能新增的 Books 变化。既有 52 个通过的正文块无需无差别重读。

## 9. 校验边界

- 本轮未修改 Books，未扩大窗口，未 stage、commit 或 push。
- validator、JSON、链接、marker、评分和 scoped diff 的机器检查必须在本审计状态写入后重新运行；机器通过不能覆盖以上语义失败。
- 本轮未增加跨模型复核；独立性来自未参与作者修复或 root 写回的 fresh-context reviewer。
