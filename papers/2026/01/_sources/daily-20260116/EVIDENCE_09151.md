# 2601.09151v1 — generated pairwise logits are a new estimate, not exact Shapley truth

Exact [v1](https://arxiv.org/html/2601.09151v1), PRIMARY_09151_NECESSARY.md §3/4 relevant interface and evaluation limitations,5, C2. Proposed2+1+2=5 standard OnlyReport pending root. Direct verbal probability noisy→query paired factor coalitions and sum estimated logit changes→reconsider explicit factor aggregation/cost. No clinical/financial application benefit adopted.

PRISM samples random factor order background K times per factor; same prompt asks with/without factor probabilities, logit differences averaged, adds base logit and sigmoid. Tabular variant batches pairs and imputes a reference case; extracted factors requested nonoverlap/complete but LLM summaries do not establish it. Shapley additive identity applies deterministic single function defined consistently on coalitions; context-dependent generated paired estimates need not form that f, and a separately prior-derived phi0 changes reconstructed target. No exact reconstruction/calibration/cause assertion. Reference-specific attribution ≠ causal feature contribution.

Actual evaluation mostly tabular risk and medical/finance tasks; only reusable generation-estimator design examined here, no high-stakes guidance or application adoption. GPT4.1mini/Gemini2.5Pro and one GPT4.1 unstructured example; K10 per tabular feature, K5 apple; query countsΘ(mK), TabularΘ(m) requests stillΘ(mK) instances. Timings92.7/330s are historical nonbatched API-specific, not general latency/SLO; model precision/hardware/concurrency/seed/CI ND. Probability of event plotted against magnitude of price change is not calibration identity. Factor extraction10 repeats are not all training/evaluation seeds.

C2 quantile reliability reweights balanced split with original dataset prevalence proxy; population unknown. No guarantee real deployment class-conditional distribution invariant or arbitrary dynamic recalibration; monotone binned curve not every-individual correctness. Table3 MIMIC PRISM AUROC below best direct baseline, do not adopt authors consistently-superior claim. Source note phi0 does not change ranking but F1 under fixed threshold can change; no fixed-threshold invariance asserted here.

Current Ch66 L132–154 separates task/calibration release and exchangeability; generic principles covered, not this generated Shapley implementation. Proposed OnlyReport because no independently validated portable reliability contract; preserves new local estimator/counterevidence, not vague Existing. No Books/replication.

## 当前独立终裁收据

root实际method/evaluation/C2与当前Ch66核：5分标准完成、OnlyReport通过。不是泛Existing，不授精确真概率Shapley/因果或未知prevalence/conditional-shift部署calibration，无高风险领域收益采用。
