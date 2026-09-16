# 2026-05-22 Root Books Writeback Audit

## Scope

作者侧 V3 对账只冻结了 3 个真正缺失的长期命题，root 按日期顺序写入同一 canonical owner `PLATFORM-EVALUATION-SYSTEM`。其余候选不在本次共享 Books 写回中重判。

## Applied bindings

| Source Family | 语义增量 | Binding |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-21492` | 相关特征与 Rashomon set 下，单 checkpoint attribution 不能同时宣称 faithful、跨重训稳定且组内完整；EvalRun 保存 seed/model ensemble/correlation/attribution identity，并披露 tie 与牺牲性质。 | `semantic-body-binding:SF-2026-ARXIV-2605-21492` |
| `SF-2026-ARXIV-2605-21515` | prompt program 的少量 pass 不能继承 symbolic program 的二峰先验；release confidence 绑定 artifact kind、LLM/temperature、task distribution、直接证据和版本化 prior。 | `semantic-body-binding:SF-2026-ARXIV-2605-21515` |
| `SF-2026-ARXIV-2605-22714` | 复用同一 Judge conversation 时，历史 verdict polarity 是 evaluation state；默认 fresh context，必须 batching 时保存并平衡 history，并以 clean twin 校准。 | `semantic-body-binding:SF-2026-ARXIV-2605-22714` |

三项均写入 `books/part-06-ai-infrastructure/66-evaluation-system.md` 的既有演进链，位于首个 `## Review notes` 前；正文保留证据边界、trade-off、failure 与 fallback，未把作者 benchmark 或厂商式 headline 外推为通用保证。

## Remaining gate

Root 写入只完成 Books implementation。fresh non-author 仍需独立挑战 05-22 的窗口 owner、候选分母、Evidence、No Change 与三项实际正文；受阻材料必须隔离且不得支持正面结论。全部通过后才可标记日报完成。
