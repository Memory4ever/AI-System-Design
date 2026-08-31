# 2026-05-09 Exact-v1 Materials Request — Resolved

状态：`Closed`

恢复日期：`2026-09-01`

open requests：`0`

ordinary pending：`0`

原 17 项请求均按 official arXiv exact-v1 的 `HTML → PDF → e-print/source → author repo/project page` 路径重新执行；没有用后续 revision 替代 v1。16 项由 official v1 HTML 直接完成，`SF-2026-ARXIV-2605-08267` 的 HTML 全量读取在恢复时出现 SSL timeout，但 official v1 PDF 与 e-print source 均返回 HTTP 200，足以完成 identity、Method、Evaluation、Limitations、artifact 与 claim-boundary 核验。

| Request ID | Source Family | HTML v1 | PDF v1 | e-print/source v1 | Artifact / project page | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
| MR-20260509-2605.07111 | SF-2026-ARXIV-2605-07111 | 200；readable | not needed after readable HTML | not needed | immutable event-time repo commit Not Disclosed | closed；No Change |
| MR-20260509-2605.07134 | SF-2026-ARXIV-2605-07134 | 200；readable | not needed after readable HTML | not needed | `https://github.com/kwondu/region4web`；exact-v1 commit Not Disclosed | closed；No Change |
| MR-20260509-2605.07180 | SF-2026-ARXIV-2605-07180 | 200；readable | not needed after readable HTML | not needed | related `https://github.com/MiroMindAI/MiroFlow`；paper-specific immutable commit Not Disclosed | closed；No Change |
| MR-20260509-2605.07514 | SF-2026-ARXIV-2605-07514 | 200；readable | not needed after readable HTML | not needed | upstream references only；paper-specific artifact Not Disclosed | closed；No Change |
| MR-20260509-2605.07547 | SF-2026-ARXIV-2605-07547 | 200；readable | not needed after readable HTML | not needed | immutable event-time repo commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08267 | SF-2026-ARXIV-2605-08267 | initial probe 200；full-body retry SSL timeout | 200；297366 bytes；SHA256 `ae34cdb3df4654d3613ca8a04d80fcf71a34e09cf431d3067b9571945b936263` | 200；gzip source 11988 bytes；SHA256 `0b121fdad7ab193b95956ae6daa0b235970bd9e89c6f3bdcc71154692fe5002d` | source includes `execution_envelope_admission.tex`；external repo Not Disclosed | closed；No Change |
| MR-20260509-2605.08268 | SF-2026-ARXIV-2605-08268 | 200；readable | not needed after readable HTML | not needed | immutable event-time repo commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08271 | SF-2026-ARXIV-2605-08271 | 200；readable | not needed after readable HTML | not needed | `https://github.com/lijiazheng0917/MAGIC-video`；exact-v1 commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08314 | SF-2026-ARXIV-2605-08314 | 200；readable | not needed after readable HTML | not needed | `https://github.com/Zishan-Shao/FlashSVD`；exact-v1 commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08363 | SF-2026-ARXIV-2605-08363 | 200；readable | not needed after readable HTML | not needed | `https://github.com/lunal-dev/kettle`；exact-v1 commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08368 | SF-2026-ARXIV-2605-08368 | 200；readable | not needed after readable HTML | not needed | immutable event-time repo commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08399 | SF-2026-ARXIV-2605-08399 | 200；readable | not needed after readable HTML | not needed | immutable event-time repo commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08432 | SF-2026-ARXIV-2605-08432 | 200；readable | not needed after readable HTML | not needed | `https://github.com/ZhanliangAaronWang/Sem-ECE`；exact-v1 commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08504 | SF-2026-ARXIV-2605-08504 | 200；readable | not needed after readable HTML | not needed | author-linked repo present；paper-specific immutable commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08505 | SF-2026-ARXIV-2605-08505 | 200；readable | not needed after readable HTML | not needed | immutable event-time repo commit Not Disclosed | closed；No Change |
| MR-20260509-2605.08565 | SF-2026-ARXIV-2605-08565 | 200；readable | not needed after readable HTML | not needed | `https://github.com/clee1994/finer_is_better`；exact-v1 commit Not Disclosed | closed；No Change |
| MR-20260509-2606.27379 | SF-2026-ARXIV-2606-27379 | 200；readable | not needed after readable HTML | not needed | position/evaluation-contract paper；code artifact Not Disclosed | closed；Integrate；waiting for root serial Books writeback |

## Gate effect

- Coverage remains `Closed`.
- Evidence is `Passed`: 83/83 candidate Source Reviews are complete.
- Books is `Open`: only `SF-2026-ARXIV-2606-27379` remains in the date-local root-serialized queue.
- This recovery lane did not modify shared Books.
