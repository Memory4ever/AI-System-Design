# 2601.09026v1 — approximate layer solve is not ordinary pipeline scheduling


## 非作者局部终裁

root actual Ch38 L43/45、L443末注及前后 POST通过，锁释放。6分gap深入、整合终裁；不代表日级完成。
[Exact-v1](https://arxiv.org/html/2601.09026v1), selected raw PRIMARY_09026_NECESSARY.md: §3.1–3.2.3/4.1–4.2, buffer-layer Appendix B and minimum setup C. Proposed2+2+2=6, standard source read and concrete alternative-branch gap deepening; root source/owner decision pending. Depth dependency→MGRIT approximate layer solve/gradient error control→reconsider exact microbatch pipeline versus iteration-controlled depth parallelism. No score for borrowed parallelism principles.

Residual Transformer is interpreted as forward Euler; standard h=1 versus neural-ODE middle h=1/L changes architecture, with first/last serial buffers h=1. This is not a drop-in equivalent execution for arbitrary pretrained Transformer. Fine/coarse FCF relaxation, restriction of residuals and coarse serial correction/interpolation connect locally parallel depth updates; GPU-aware MPI communicates partition boundaries. Coarse correction is still serial and solver iterations cost communication/compute.

Forward/backward approximation biases gradients. §4.1 parallel-only training stagnates/diverges on tested BERT/GPT/ViT regimes; increased solve accuracy or serial exact forward/backward later restores progress. Adaptive residual-ratio test periodically increases iterations or switches to serial; source prose switching direction contradicts surrounding figure/method, so use algorithm intent and not that isolated typo. Figure4 min/max three BERT seeds is not uncertainty for every speed/result. Small two-GPU configuration can be slower due to numerical/communication overhead; deeper/granular configurations change tradeoff. Figure9 GPU-scaled batch16/32/64 is not a constant-global-batch speedup. No universal speed/accuracy equivalence adopted.

Setup: BERT/GPT/ViT for MC/MT/classification; Jean Zay V100 nodes and Singra A10080GB; TorchBraid/PyTorch, GPU-aware MPI; dropout mask must be consistent across fine/coarse solves, reset per training iteration rather than every layer evaluation. Necessary source does not fully bind precision/concurrency/CI or matched full training budget for universal cost claim (Not Disclosed). No code executed.

Actual Ch38 L18–72 holds exact layer partition/microbatch dependencies and gradient accumulation; no MGRIT/inexact layer-solve branch. Proposed unique TRAIN-PIPELINE-PARALLEL minimal two paragraphs after “只有Layer Partition” before microbatch: preserve exact PP as baseline; distinguish numerical relaxation changing activation/gradient semantics, accuracy/serial fallback, architecture/residual and total communication cost. Root must decide supported gap/lock, not automatic write.
