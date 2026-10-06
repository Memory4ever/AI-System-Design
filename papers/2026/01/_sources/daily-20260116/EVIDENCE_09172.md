# 2601.09172v1 — worst-tail weighting is not a KL-radius certificate

Exact [v1](https://arxiv.org/html/2601.09172v1); necessary source saved PRIMARY_09172_NECESSARY.md §4.1–4.3, §5/Table1–3, §5.3 and Appendix B decisive percentile. Proposed2+1+2=5: uniform forgetting can hide heterogeneous residual→batch top-loss group or exp-loss weights alter forget objective→consider residual-tail weighting separately from average progress. Base-method loss is a difficulty proxy, not verified per-sample erasure.

§4.2.1 assigns all mass to top50% worst-loss samples; this need not remain inside the original fixed KL-radius ball. §4.2.2 Eq9–12 gives fixed-beta penalized log-sum-exp; constrained KL sup would require appropriate dual minimization/radius relation, absent from fixed-beta recipe. Retain loss unchanged; negligible retain-DRO effect in local NPO tests does not prove naturally balanced retain distributions. Preserve actual alternative mechanism, do not adopt exact-radius robust guarantee or synchronized forgetting proof.

Llama2-7B/8A800; LR1e-5/2e-5/5e-5/1e-4, batch8/16/32, beta1/2/5/10, retainlambda.25/.5/1/2 hypersearch. Steps/precision/seed repetition/CI/heldout selection budget/full timing ND in necessary core. TOFU synthetic200authors1/5/10%, MUSE books/news entangled; FQ KS truth-ratio reference versus MU aggregate probability/ROUGE/TR, not universal erasure or privacy. Sorting O(nlogn) is not full training wallclock proof.

Direct countercontrols: Table1 NPO+GEM.7634>.6842 worse, SatImp DV ES.4522>.2041/fluency.7588<.8272. Table2 SimNPO G News VM.4193>.3829 worse; DV Books retain KM.5393<.5969 and PL magnitude can overshoot zero. Table3 NPO+G MinK.5056>.4912 worse. Appendix B 25/50/75/100% nonmonotonic, no universal50% optimum; local other-metric improvement not all-method superiority.

Actual Ch72 unlearning body2555–2601 distinguishes target/reference, gradient core-set selection and separate parameter/behavior releases, but does not express training-time worst-tail forget-loss weighting. Potential PLATFORM-SECURITY minimal gap immediately around core-set branch: selection of subset versus adaptive objective weighting, different loss semantics, tail/retain/recovery validation and baseline fallback. No universal deletion or exact-DRO recipe; root necessary source/owner decision pending, no write.
# 当前终态收据

root非作者实际必要primary/具体owner终裁通过：深入完成，整合：[PLATFORM-SECURITY Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，core-set后两段，POST通过。§4–5/Table1–3及B核到tail-weight不等subset选择；固定温度/截断不授给定KL半径保证或50%普遍最佳，retain/恢复/攻击反侧保留。Ch72 L2569/2571与末注4085实际写入，root必要源/owner及前后交接非作者POST通过。 日级未授，未复现实验。
