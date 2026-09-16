# 2026-05-22 Daily V3 fresh non-author final semantic review — R2

**Reviewer:** fresh non-author reviewer（未参与 2026-05-22 author repair 或 root Books 写回）

**Reviewed at:** 2026-09-16T12:25:16+08:00

**Gate:** **FAIL — 保持 Ongoing**

## 结论

当前 owner batch、身份集合与账面投影可以机械复算，46 个 Applied binding 的成对 marker、正文位置与 owner 路径也通过检查；本轮新写入的 9 个 binding 经逐项复核，采用命题、证据边界、trade-off、failure mode 与 fallback 均成立，无需撤回或改写。

但 final semantic Gate 仍不能通过：419 个 `continued_closure` 中至少有 3 个由当前保存的 title + full abstract 即可确认需要重开；245 个 Evidence 记录中有 70 个没有显式 `adopted_proposition`，其中 14 个仍缺 current `problem`、`mechanism` 与 `review_status` 投影；145 个 `No Change` 中有 70 个只给出章级主题概述，没有指出 `## Review notes` 之前承载该论文采用命题的具体正文位置与命题。历史 receipt、账面相等与 marker 存在不能替代这些当前语义证据。

因此 `667 = 245 retained + 422 closure`、`245 = 191 deep + 54 standard` 与 `245 = 46 Applied + 145 No Change + 54 Report Only` 只能视为当前 author projection，不能登记为最终 canonical closure。

## Owner、窗口与身份集合

- 窗口：PASS。官方 announcement time 为 `2026-05-22T08:00:00+08:00`，处于 `[2026-05-21T09:00:00+08:00, 2026-05-22T09:00:00+08:00)`。
- owner batch：PASS。`official-owner-batch-evidence-v3.json` 覆盖 `2605.21490..2605.22823`，667 个 covered-category identity 唯一且全部位于该范围；513 个 same-day OAI direct 与 154 个 later-revision recovery 合计 667。
- 当前集合算术：PASS，但只证明文件自洽。`667 = 245 + 422 + 0`；retained identity 与 Evidence、Books comparison identity 集合一致。
- source-local reservation：Meta 与 Tencent Hunyuan 的外部材料问题继续隔离；它们没有被用作正面 no-hit 证据，也不是本轮 FAIL 原因。

## Denominator false-negative challenge

以下三项当前均标为 `continued_closure`，但保存的完整摘要已提供足以重开 contribution admission 的机制信号。重开只表示进入 exact-v1、评分、Evidence 与 Books comparison，不预判最终 Integrate。

| arXiv | 当前摘要中的 durable delta | 建议 owner / 需要核验的边界 |
| --- | --- | --- |
| `2605.21573` | Lens 将训练 compute 差异归因于 dense captions、multi-resolution/aspect-ratio batching、semantic VAE 与 encoder/post-training/distillation 组合，而非只有较小参数量或单一 benchmark 分数。 | `MULTIMODAL-GENERATIVE-PARADIGMS` / `TRAIN-PRETRAINING`；exact-v1 必须拆分哪些组件真正改变 compute-quality contract，哪些只是模型配方。 |
| `2605.21776` | PromptNCE 通过显式 `OTHER` 选项把候选间相对排序改成对条件概率/PMI 的估计，改变 prompt-based probability elicitation 与 calibration contract。 | `PLATFORM-EVALUATION-SYSTEM` / prompt owner；核验概率恢复假设、候选集依赖与跨数据集边界。 |
| `2605.22202` | 论文不是单纯资产：它跨 25 个模型、五个 MTEB task 验证 neighborhood overlap 与 ICA magnitude 同 task performance 的相关性，提出 representation geometry diagnostic。 | `WORLDVIEW-REPRESENTATION` / `MODEL-EMBEDDING`；核验相关性、预测能力与训练目标之间不能外推为因果。 |

这三项已足以推翻“419 continued closure 均可终结”的结论。返修应按同一 closure reason/class 做 bounded sibling challenge，不能只把三个 ID 加入 hard-coded retained list 后结束。

## Evidence projection challenge

- `exact-v1-evidence-v3.json` 有 245 个唯一记录。
- 其中 **70** 个没有显式 `adopted_proposition`。55 个保留了 current `problem`/`mechanism`，但仍无法从结构化记录区分“论文声称什么”和“本项目采用什么”。
- 另有 **14** 个同时没有 current `problem`、`mechanism`、`adopted_proposition` 与 `review_status`；这些记录仍依赖旧 replay packet，不能直接计入当前 `deep complete`。
- `2605.21516` 使用另一套 legacy 字段（`problem_and_changed_constraint`、`mechanism_and_ownership`），但同样没有显式 `adopted_proposition`，且 locator 投影不完整。它可以复用原始证据，不能在未规范化当前投影时被历史 receipt 自动判定为 complete。

修复不要求重复下载可验证的 exact-v1；可以复用已核验 artifact，但必须把当前采用命题、Evidence Level、具体 Method/Evaluation/Non-proof locator 与边界投影完整。

## Books comparison challenge

- 46 个 `Applied`：marker 唯一性、owner 路径、正文位置均 PASS。
- 37 个既有 binding：沿用此前逐项写后复核结果，本轮没有发现新的语义冲突。
- 9 个新 binding：`2605.21751`、`2605.21770`、`2605.21849`、`2605.21933`、`2605.22060`、`2605.22211`、`2605.22644`、`2605.22723`、`2605.22733` 均逐项 PASS。它们位于 owner chapter 的 `## Review notes` 前，且正文明确保留采用命题、非证明边界、收益/代价、failure mode 与 fallback/coexistence。
- 145 个 `No Change` 中 **70** 个的 `existing_proposition` 只是“当前 Chxx 已覆盖……”的章级主题概述，没有给出具体正文 heading/anchor/excerpt。主题相似不能证明现有正文已经承载该 source family 的采用命题，因此这些项必须补做 current-body comparison；若确实已有覆盖，记录具体命题与位置，否则改为 Integrate 或 Report Only。

## 精确剩余 Gate

1. 重开 `2605.21573`、`2605.21776`、`2605.22202`，并按其原 closure class 做 bounded sibling false-negative challenge。
2. 对新增 retained 完成 official exact-v1、V2 score、Evidence、owner 与 Books comparison；同步 retained/closure 算术。
3. 为 70 个缺失项补齐显式 adopted proposition；其中 14 个同步补齐 current review status 与 Method/Evaluation/Non-proof 投影。
4. 对 70 个泛化 `No Change` 补做 current-body anchor/proposition 对读，不能以章节主题或 marker 代替覆盖证明。
5. 同步 README、screening/evidence/books JSON 后，再交给另一位未参与返修的人做 fresh final semantic Gate；在此之前状态保持 Ongoing。

## 本轮校验结论

- JSON parse / identity uniqueness / retained-evidence-books set equality：PASS。
- `667 = 245 + 422 + 0`、`245 = 191 + 54`、`245 = 46 + 145 + 54`：PASS（仅机械投影）。
- 46 组 paired marker uniqueness / owner path / pre-Review-notes position：PASS。
- 9 个新 Books binding 独立语义复核：PASS。
- Candidate denominator semantic Gate：FAIL。
- Evidence current projection Gate：FAIL。
- No Change current-body comparison Gate：FAIL。
- Final disposition：**Ongoing**；本轮没有修改 Books。
