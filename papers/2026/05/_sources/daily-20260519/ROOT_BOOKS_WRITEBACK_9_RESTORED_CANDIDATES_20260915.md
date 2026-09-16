# 2026-05-19 Root Books Writeback Audit

## Scope

本次只落实作者冻结队列中的 9 个 `Integrate`，不改写其余 163 个候选的 Evidence 或 Books Decision。写入顺序按报告日期执行，所有内容进入既有 Stable Knowledge Node 的论证主线，不建立论文列表式附录。

## Applied bindings

| Source Family | Stable Node | Owner file | Binding |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-16345` | `TRAIN-SFT` | `books/part-04-training-system/29-sft.md` | `semantic-body-binding:SF-2026-ARXIV-2605-16345` |
| `SF-2026-ARXIV-2605-16579` | `MULTIMODAL-GENERATIVE-PARADIGMS` | `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` | `semantic-body-binding:SF-2026-ARXIV-2605-16579` |
| `SF-2026-ARXIV-2605-17093` | `TRAIN-SFT` | `books/part-04-training-system/29-sft.md` | `semantic-body-binding:SF-2026-ARXIV-2605-17093` |
| `SF-2026-ARXIV-2605-17432` | `TRAIN-LORA` | `books/part-04-training-system/30-lora.md` | `semantic-body-binding:SF-2026-ARXIV-2605-17432` |
| `SF-2026-ARXIV-2605-17447` | `MODEL-SELF-ATTENTION` | `books/part-02-model/14-self-attention.md` | `semantic-body-binding:SF-2026-ARXIV-2605-17447` |
| `SF-2026-ARXIV-2605-17887` | `MODEL-SELF-ATTENTION` | `books/part-02-model/14-self-attention.md` | `semantic-body-binding:SF-2026-ARXIV-2605-17887` |
| `SF-2026-ARXIV-2605-18309` | `TRAIN-SFT` | `books/part-04-training-system/29-sft.md` | `semantic-body-binding:SF-2026-ARXIV-2605-18309` |
| `SF-2026-ARXIV-2605-18359` | `MODEL-SELF-ATTENTION` | `books/part-02-model/14-self-attention.md` | `semantic-body-binding:SF-2026-ARXIV-2605-18359` |
| `SF-2026-ARXIV-2605-18753` | `MODEL-SELF-ATTENTION` | `books/part-02-model/14-self-attention.md` | `semantic-body-binding:SF-2026-ARXIV-2605-18753` |

## Root checks

- 每个 Source Family 在全书恰有一个 owner file，且 start/end marker 各一个。
- 新正文均位于章内 `Review notes` 之前；是否准确保留机制、边界与 fallback 仍由 fresh non-author 复核，而不是由 root 自签。
- 同一章节内的多个增量按机制关系合并到已有推理链，没有用论文名称充当章节结构。
- `scripts/validate_research.py --report papers/2026/05/19/README.md` 通过。
- 上述 Books 与 date-local 文件的 `git diff --check` 通过。

## Fresh-review repairs

fresh non-author 首轮顺读发现三项真实语义缺陷，root 已定点修复，未扩大到其他章节：

- `2605.16345`：由“样本准入”纠正为训练与推理共享的显式 goal-conditioned interface，并补回 threshold-indexed sample-goal expansion；准入只是数据构造的一部分。
- `2605.17432`：纠正“接触 private data 前冻结”的错误；DP synthetic generation 已消耗 `(ε_syn, δ_syn)`，selection 只是该 artifact 的 post-processing，最终私有微调继续消耗 `(ε_ft, δ_ft)`，两阶段预算必须组合。
- `2605.18309`：把“停训后自然 rebound”纠正为 reverse fine-tuning 后通过 re-exposure / re-alignment training 出现的能力恢复；论文不支持 time-only 自发反弹。

三项修复已由同一 fresh non-author reviewer 重新顺读并通过验收；结果见 `V3_FRESH_NONAUTHOR_FINAL_GATE_REVIEW_20260915.md`。

## Remaining gate

该记录本身只证明 root 写入已完成，不构成作者自签；其后 fresh non-author 已对 36 项 affected set、Evidence/Books 算术、9 个新正文及相邻交接完成独立复核并通过。05-19 当前没有剩余可执行 Gate。
