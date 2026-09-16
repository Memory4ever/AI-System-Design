# 2026-05-14 V3 Round5 False-negative Author Repair

**作者上下文：** `/root/may13_bounded_author_round5`  
**状态：** `AUTHOR REPAIR COMPLETE — NOT FINAL SIGN-OFF`  
**边界：** 只处理 fresh non-author review 点名的 6 个 ID；未重新枚举、未扩日期/来源/候选范围、未编辑 Books。

## 返修结果

| arXiv | exact-v1 | withdrawal | Score V3 | Owner | 作者处置 |
| --- | --- | --- | --- | --- | --- |
| 2605.12863 | accessible | no | 3+3+3=9 | `PLATFORM-SECURITY` | Integrate — Root Writeback Pending |
| 2605.12879 | accessible | no | 3+2+3=8 | `MODEL-SELF-ATTENTION` | Integrate — Root Writeback Pending |
| 2605.12913 | accessible | no | 3+3+3=9 | `TRAIN-SFT` | Integrate — Root Writeback Pending |
| 2605.13228 | accessible | no | 2+2+3=7 | `AGENT-TOOL-CALLING` | Integrate — Root Writeback Pending |
| 2605.13316 | accessible | no | 3+2+3=8 | `MULTIMODAL-EMBODIED-VLA` | Integrate — Root Writeback Pending |
| 2605.13821 | accessible | no | 3+3+3=9 | `AGENT-PLATFORM` | No Change — Existing Coverage |

6/6 均重新读取题名与完整摘要，并打开 `arxiv.org/html/<id>v1`。6/6 完成身份、v1、withdrawal、Method/实现、Evaluation、limitations/counterevidence、artifact 与 Stable Node/相邻正文对读；0 blocked，0 withdrawn。

## 分母与证据账本

- Active inventory 未变化：714。
- 修复前：`714 = 118 retained + 596 closure + 0 withdrawn`。
- 修复后：`714 = 124 retained + 590 closure + 0 withdrawn`。
- 加 2 个官方 Source Family 后 Candidate Denominator：120 → 126。
- Exact-v1 evidence：118 → 124；deep=120，standard=4，accessible=124，withdrawn=0。
- Books comparison：124；既有 root applied=78；本轮 pending=5；No Change=41。
- `screening-outcomes-v3.json` 是当前 714 active inventory 的唯一分母权威。`screening-ledger-final.json` 含旧 745-record 抓取 checkpoint，现已明确标记 non-canonical，并仅同步六项语义状态，不能参与当前分母算术。

## Evidence-boundary Challenge

- `2605.12863`：没有把 well-typed 写成业务正确；保留 runtime check、EDSL/checker TCB 与跨语言 non-proof。
- `2605.12879`：没有把迭代消除写成 sparse/subquadratic；保留 dense QK/value、calibration shift 与 causal-mask gap。
- `2605.12913`：没有把 software-agent benchmark 外推所有 Agent；保留 teacher cost/bias、OpenHands scope 与 context overflow。
- `2605.13228`：没有把 heterogeneous full-system baseline 当机制因果证明；保留 resolver loop、typed failure、budget 与 high-risk action boundary。
- `2605.13316`：没有把作者所称 lossless 外推真实机器人安全；明确 Tesla A40、模型、sampler、模拟任务和 50-episode contract，artifact 仅核验 repository identity。
- `2605.13821`：没有为新论文名强行写 Books；对读 Ch84 的具体机制锚点后以 `No Change` 关闭。

## 输出与下一步

- 新 root queue：`root-books-writeback-queue-round5.json`，5 项。
- 可直接吸收的中文主线：`ROOT_BOOKS_SYNTHESIS_ROUND5_20260915.md`。
- root 必须依 owner/日期顺序修改共享 Books；作者不修改 Books。
- 写回后必须由新的 fresh non-author context 检查 marker 唯一性、正文位置、owner、语义完整性、exact-v1 boundary 与 README 状态；通过前保持 Ongoing。
