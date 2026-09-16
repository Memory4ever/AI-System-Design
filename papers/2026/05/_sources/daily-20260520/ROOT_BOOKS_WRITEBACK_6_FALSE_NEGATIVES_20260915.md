# 2026-05-20 Root Books Writeback Audit

## Scope

本次只落实作者在 bounded false-negative challenge 后冻结的 6 个新 `Integrate`。其余 60 个候选的 Evidence 与 Books Decision 不在本次写回中重判；共享 Books 按报告日期串行修改。

## Applied bindings

| Source Family | Stable Node | Owner file | Binding |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-18813` | `MULTIMODAL-WORLD-MODELS` | `books/part-03-multimodal-world-models/25-multimodal-world-models.md` | `semantic-body-binding:SF-2026-ARXIV-2605-18813` |
| `SF-2026-ARXIV-2605-18841` | `PLATFORM-SECURITY` | `books/part-06-ai-infrastructure/72-security.md` | `semantic-body-binding:SF-2026-ARXIV-2605-18841` |
| `SF-2026-ARXIV-2605-18882` | `AGENT-TOOL-CALLING` | `books/part-07-agent/78-tool-calling.md` | `semantic-body-binding:SF-2026-ARXIV-2605-18882` |
| `SF-2026-ARXIV-2605-19095` | `TRAIN-PRETRAINING` | `books/part-04-training-system/28-pretraining.md` | `semantic-body-binding:SF-2026-ARXIV-2605-19095` |
| `SF-2026-ARXIV-2605-19250` | `MULTIMODAL-REPRESENTATION` | `books/part-03-multimodal-world-models/23-multimodal-representation.md` | `semantic-body-binding:SF-2026-ARXIV-2605-19250` |
| `SF-2026-ARXIV-2605-19577` | `TRAIN-GRPO` | `books/part-04-training-system/33-grpo.md` | `semantic-body-binding:SF-2026-ARXIV-2605-19577` |

## Root checks

- 每个 binding 的 start/end marker 各一个，且只出现于唯一 owner file。
- 新正文均位于章内首个 `## Review notes` 前，并与既有段落形成“旧方案边界 → 约束变化 → 机制 → 代价与 fallback”的连续关系。
- 写入没有把权重记忆、learned shield、tool-call sensor、schedule-free optimizer、head intervention 或跨任务 reward normalization 外推为普遍成立的系统结论。
- `scripts/validate_research.py --report papers/2026/05/20/README.md` 与 scoped `git diff --check` 需在作者文件冻结后再次执行。

## Remaining gate

Root 写入不等于 Books Gate 通过。fresh non-author 仍需挑战 575 个 announcement identities 的分母、66 个 Evidence、33 个 Applied binding、33 个 No Change，并顺读 6 个新正文及相邻交接；只有该复核通过后，05-20 才能标记 `Complete`。
