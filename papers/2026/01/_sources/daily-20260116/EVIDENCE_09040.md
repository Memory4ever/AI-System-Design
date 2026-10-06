# 2601.09040v1 — local video-MAE supervision changes representation depth, not guaranteed efficiency


## 非作者局部终裁

root actual exact-v1必要方法/对照/反侧与Ch28 block-local终裁通过，5分标准OnlyReport；不是泛Existing。
[Exact-v1](https://arxiv.org/html/2601.09040v1), PRIMARY_09040_NECESSARY.md §3.1–3.4/4.1, necessary5 results and6 discussion/limits. Proposed2+1+2=5 standard, pending root final OnlyReport. Global end-to-end gradient→isolated block-local MAE/depth-accessibility comparison→reconsider probe depth and credit-assignment claims; score only the local comparison, not mature BP alternatives.

K blocks use stop-gradient boundaries and a local reconstruction decoder each, same single90% mask across blocks. Sequential K stages each E epochs means K*E data passes versus E per parameter; simultaneous sums local losses with full forward. Extra local decoders/deep supervision differ from end-to-end final-only objective, so outcome cannot uniquely attribute gradient locality. Tiny/Small12layer192/384width3/6heads,150/300epochs,K4/6; localdecoder4layers192width3heads. Tubelet8×16×16,16frame/stride4,UCF101 limited retained videos/128crop; AdamW1e-4 cosine wd.05,3init and3probe fits each not all reported CI.

Blockwise features reach nearby local linear-probe/retrieval quality, early accessibility with late-block saturation/CKA changes; layerwise decodability is not whole capability. Sequential/simultaneous loss/representation differ, no unique optimal granularity. Discussion explicitly additional decoder memory/compute and focus on representation, not efficient learning; modest dataset and no full isolation local supervision vs gradient stop. Hardware/precision/full matched training budget Not Disclosed in necessary source for efficiency and no efficiency claim adopted.

Actual TRAIN-PRETRAINING Ch28 L271–277 already explains global BP→block-local objective/gradient-horizon, memory/readout/coordination tradeoff and evaluation/fallback, but original boundary only CNN/VGG. This video-MAE empirical extension is not exact same evidence and not generic Existing; local saturation/probe population does not establish a new portable training recipe, so proposed OnlyReport with experiment preserved. No Books edit/replication.
