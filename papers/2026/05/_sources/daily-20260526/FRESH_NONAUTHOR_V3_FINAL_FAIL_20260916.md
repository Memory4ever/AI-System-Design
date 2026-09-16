# 2026-05-26 V3 Fresh Non-Author Final Gate — FAIL

- Review date: `2026-09-16`
- Reviewer role: fresh non-author final reviewer
- Independence statement: 本审阅者此前未参与 `2026-05-26` 的作者筛选、date-local repair 或共享 Books 写回；此前仅在其他日期的 owner 调查中只读引用过本日材料。本轮未修改作者账本、Evidence、Books comparison 或共享 Books。
- Gate result: **FAIL — keep `papers/2026/05/26/README.md` Ongoing**

## 决定性缺陷：MiniMax identity 跨日双计

`minimax:sparse-token-forgetting` / `SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING` 不能归属 2026-05-26。

1. MiniMax 官方技术页的 JSON-LD 是 `datePublished=2026-05-27T00:00:00Z`，换算为 `2026-05-27T08:00:00+08:00`。
2. 该时间不在本日报窗口 `[2026-05-25T09:00:00+08:00, 2026-05-26T09:00:00+08:00)` 内；当前 05-26 账本使用的 `2026-05-26T00:30:00+08:00` 没有官方 `datePublished` 支持。
3. 2026-05-27 的 current V3 owner receipt、screening、Evidence 与 Books comparison 已经以同一 identity 和同一 source-family marker 收录该事件，公开时间正确记为 `2026-05-27T08:00:00+08:00`。因此 05-26 当前投影构成 exact identity/owner-date 双计，而不是允许跨日复用的独立事件。

该缺陷直接破坏 Coverage Closed、candidate denominator、Evidence denominator 与 Books action projection；机械校验通过不能覆盖 owner 错误。

## 修复后的精确投影

只移除这一项、其余 263 个 arXiv owner identity 与 178 个 closure 不变时，05-26 必须重冻为：

- raw/denominator：`263 = 85 retained + 178 pre-denominator closure + 0 withdrawn`；owner 组成仅为 `263 arXiv official-announcement identities + 0 institutional event`。
- Evidence：`85 = 73 deep complete + 12 standard complete + 0 blocked`。
- score：`{6: 12, 7: 9, 8: 49, 9: 15}`。
- Books：`85 = 30 Applied + 7 Integrate + 41 No Change + 5 Structural Candidate + 2 Report Only`。
- 05-26 实际 Books binding/action 投影：`16`，不是 `17`；05-26 post-write passed count 也只能是 `16`。

MiniMax 当前 disposition 是 `Applied`、Evidence route 是 `deep`、score 是 `8`，所以它分别从 Applied、deep 与 score-8 桶中减一；closure、standard、blocked、Integrate、No Change、Structural Candidate 与 Report Only 均不变。

## 精确返修队列

作者必须只在 05-26 date-local 投影中移除该 identity，并同步下列 current-authoritative artifacts：

1. `papers/2026/05/26/README.md`：删除 MiniMax source-row 的当日正面命中、候选表/Review 段与 05-26 Books action 声明；同步结论、来源、Evidence、score、Books、缺口与复核算术。
2. `official-owner-batch-evidence-v3.json`：从 `institution_events` 删除该事件，并将 `raw_count`、`dedup_count` 改为 `263`。
3. `source-coverage-v3.json`：保留来源检查事实，但明确官方 `datePublished` 属 05-27，05-26 为 `0 raw`，不得继续写 `00:30 BJT`。
4. `screening-outcomes-v3.json`：删除 retained item，冻结 `263/85/178/0` 与 263-item set。
5. `evidence-review-v3.json`：删除该 Evidence item，冻结 `85/73/12/0` 与 score distribution `12/9/49/15`。
6. `books-comparison-v3.json`：删除该 Applied item，冻结 `85 = 30+7+41+5+2`。
7. `root-books-writeback-queue-v3.json`：从 05-26 action set 删除该 family，冻结 `item_count=16`、`postwrite_semantic_review_passed_count=16`；不得把同一 family 继续算作 05-26 root action。
8. `author-adversarial-audit-v3.json`、`DATE_LOCAL_REPAIR_CHECKPOINT_20260916.md` 与 `render_v3_current_recertification.py`：同步 owner、screening、Evidence、Books 与 marker/action 算术，移除旧 `00:30 BJT` 归属断言。

共享 `books/part-04-training-system/29-sft.md` 中已经存在的 semantic binding **不应删除或重复写入**：同一 family 已由 05-27 正确拥有，05-27 Books comparison 也将现有正文判为 `Applied`。修复的是 05-26 的归属与投影，不是长期命题本身。

## 第二个缺陷：7 个 queue-declared marker 不存在

当前 17 个 action 的 paired `semantic-body-binding:<SF>:start/end` 都各出现一次、顺序正确且位于主 `## Review notes` 前；但 `root-books-writeback-queue-v3.json` 为每项声明的 `binding_marker` 是独立的 `<!-- source-family:<SF> -->`。全局实查只有 `10/17` 个该 marker 存在，下列 7 项计数为 0：

| source family | target path | 正文 heading |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-24322` | `books/part-03-multimodal-world-models/25-multimodal-world-models.md` | `Probe 可以暴露物理方向，但不能接管环境真值` |
| `SF-2026-ARXIV-2605-24366` | `books/part-07-agent/76-rag.md` | `Structured Retrieval 是可撤销的中间表示，不是新的事实源` |
| `SF-2026-ARXIV-2605-24545` | `books/part-06-ai-infrastructure/72-security.md` | `Unlearning 的目标应是 Unique Memorization，而不是盲目删除共享能力` |
| `SF-2026-ARXIV-2605-24549` | `books/part-04-training-system/30-lora.md` | `低秩更新还可以避开 Skill-critical Subspace，但 Probe 不是能力真值` |
| `SF-2026-ARXIV-2605-24696` | `books/part-06-ai-infrastructure/67-monitoring.md` | `Streaming Threshold 必须由风险预算派生，而不是离线固定` |
| `SF-2026-ARXIV-2605-24718` | `books/part-02-model/11-tokenizer.md` | `Fertility 是 Language × Domain 的成本与可达性合同` |
| `SF-2026-ARXIV-2605-24737` | `books/part-06-ai-infrastructure/67-monitoring.md` | `Compliance Signal 可以持续运行，但 Judge Disagreement 必须升级` |

因此 queue/current checkpoint 的“17/17 binding marker 全局唯一”断言不成立。root 应在每个既有 paired block 的 `:end` 后、`## Review notes` 前补入 queue 已声明的唯一 `source-family` marker，或在合同明确只认 paired marker 时把 queue 的 `binding_marker` 改为真实存在且可验证的 paired marker；不得同时保留“声明独立 marker”与“正文不存在”的状态。05-26 owner 修正会把 MiniMax action 移出本日集合，因此未修 marker 时修后集合会是 `16/16` paired marker 通过、独立 `source-family` marker 仅 `9/16` 通过；完成这 7 项 root 修复后应为 `16/16`。

## 当前机械检查与未签 Gate

- 当前未修包的 23 个 JSON 均可解析，原有算术机械自洽；17/17 paired `semantic-body-binding` 唯一、有序且位于各目标章主 `## Review notes` 前，但 queue 声明的独立 `source-family` marker 只有 `10/17` 存在。validator 通过只证明报告接口一致，不能证明 owner 或 queue locator 正确。
- 05-26 report validator、date-local/current Books scoped unstaged/staged diff-check 与本 checkpoint 的 no-index whitespace check 均无格式错误。
- 41 个 No Change、5 个 Structural Candidate、2 个 Report Only、其余 16 个 05-26 binding 以及 178 个 closure 的最终语义 PASS 本轮不签署。owner/date Gate 已确定失败，作者完成上述有界修复后，仍须由另一名 fresh non-author reviewer 对修后集合执行最终 FP/FN、Evidence 与 Books Gate。
- 本审阅者只签发 FAIL checkpoint，不把 README 改为 Complete，也不修改共享 Books。

## Gate 结论

当前 `264=86+178` 包含一个已由官方 JSON-LD 证明属于 05-27、且已在 05-27 收录的 identity。2026-05-26 不满足 exact owner/window 与 identity conservation，因此必须保持 **Ongoing**；修复后的预期基线是 `263 raw / 85 retained / 178 closure / 0 withdrawn`，不是 Complete。

## Bounded repair resolution

本 checkpoint 签发后，reviewer 已转为 bounded repair author：

- MiniMax 已从 05-26 raw、retained、Evidence、Books 与 action 投影移除；当前 date-local 基线已重冻为 `263/85/178/0`、Evidence `73/12/0`、score `12/9/49/15`、Books `30/7/41/5/2`、actions `16`。
- Ch29 semantic binding 未删除，由 05-27 owner 保留。
- 7 个缺失 `source-family` marker 已转入 `root-books-writeback-queue-v3.json` 的 marker-only queue；repair author 未修改共享 Books。
- owner/date finding 已修复，但 marker-only root action 与另一名 fresh non-author 最终复核仍未完成，因此 README 继续保持 **Ongoing**。
