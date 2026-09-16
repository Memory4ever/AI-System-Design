# 2026-05-20 Root Books Writeback：Fresh Review 恢复项

**状态：** 三项共享 Books 写回已由 root 串行完成，等待非作者复核者执行写后语义验收。

## 写回范围

- `arXiv:2605.18810v1` → `INFER-SPECULATIVE-DECODING`：补入 parallel block drafter 的 accepted-length credit assignment；明确 loss owner 与 verifier accept/commit owner 分离，并保留固定 CE/KL fallback。
- `arXiv:2605.18999v1` → `TRAIN-PRETRAINING`：补入 normalized direction 与 step-radius certificate 的分权；绑定 optimizer/checkpoint state、理论条件与 fixed-scale fallback。
- `arXiv:2605.19619v1` → `TRAIN-PRETRAINING`：补入 singular-gap 条件分支、branch identity 与恢复语义；显式隔离论文 Introduction 中与 abstract、Table 1、定理冲突的 typo。

## 证据与边界

写回采用 `root-books-writeback-queue-v3.json` 中的 exact-v1 Method、Evaluation 与 non-proof locators。正文没有把作者有限模型、硬件或 benchmark 结果外推为生产结论；每项均保留代价、failure mode、旧路径适用条件和回退方案。

## 待验收

非作者复核者须重新检查：机制命题是否准确、marker 是否唯一成对、owner 是否正确、是否位于 Review notes 前、与相邻段落是否连贯，以及日报的 Candidate/Evidence/Books 集合与算术是否同步。完成这些检查前，2026-05-20 仍不得标记 Complete。
