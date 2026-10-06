# 2601.09097v1 — reusable solver is an artifact, not a per-query proof

Exact [v1](https://arxiv.org/html/2601.09097v1), selected PRIMARY_09097_NECESSARY.md §3.1–3.4/4/5/6/Limitations, B1/B2, decisive C1/C2 and E cost definition. Proposed2+2+2=6. Long repeated reasoning/per-query code→single-example domain schema and compiled combination/filter/delivery functions→reconsider parameter extraction versus solver regeneration. Unique owner candidate AGENT-PLANNING, not code-name-based integration.

Planning/Solution agents derive combination versus constraint parameters and output shape from one query/GT answer. Optimization rewrites schema; generators make enumerate/filter/render functions; refinement checks inclusion of known solution, returned solution identity and rendered answer against that one example. At inference InputAgent only extracts parameter values using one-shot schema, no new solver code. A prompt forbidding hard-coded example values is not a proof of full-domain completeness or generalization. Deterministic runtime checks only encoded constraints; extraction omissions/misinterpretations remain critical failure channel.

Five proprietary exact revisions in B1 (GPT4o/5/o3/Gemini1.5/2.5), stronger thinking enabled, temp0 where settable. TravelPlanner closed deterministic constraints explicitly normalized for all baselines; Trip Planning half sampled per complexity for expensive baselines but Direct/CoT/SCOPE full elsewhere; not merge populations. D2 gold exact-plan success distinct TravelPlanner commonsense/hard micro/macro. No hardware/precision/concurrency/repeated CI or deployment SLO guarantee (ND in necessary evidence). E counts inference tokens/reasoning/API+tools wallclock, but no demonstrated amortization of offline schema/code/refinement preparation over future query count. Prices historical not current recommendation.

Ablation Table2: no-refinement TravelPlanner93.1 equals full93.1 despite prose every-component-essential; formalization removal leaves Meeting100, other slices harmed. No-optimization TravelPlanner at most100000 sampled candidates, not same exhaustive budget, so cannot isolate optimization alone. Appendix F says query parameter errors, one-shot overgeneralization and long structured outputs. Solver is domain-tied; new domain needs schema redefinition. Do not adopt universal exhaustive search or no-overfit guarantee.

Actual Ch79 L149–164 feasibility/execution-conformance separates solver from executor, but not single-example schema→reusable solver with per-query extraction-only path and artifact lifecycle. Proposed minimal gap after solver tradeoff: compiled domain/parameter interface, heldout validation, version/cost/invalid extraction fallback; no general safety or permanent reuse. Root source/owner/lock pending, no Books write or code replication.

## 当前独立终裁收据

root实际核 Ch79 L159–173/末注515–520，非作者POST通过，锁释放。6=2+2+2，深入完成、实际整合；单例不授完备/无过拟合，离线成本及建模遗漏仍隔离。
