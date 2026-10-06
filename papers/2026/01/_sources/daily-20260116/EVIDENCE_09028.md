# 2601.09028v1 — document-quality features cross into decoder attention


## 非作者局部终裁

root actual Ch76 L424/426、L1445末注及前后 POST通过，锁释放。6分gap深入、整合终裁；不代表日级完成。
[Exact-v1](https://arxiv.org/html/2601.09028v1), PRIMARY_09028_NECESSARY.md §3.2–3.4,4.1–4.4,5.2–5.5 and AppD minimum. Proposed2+2+2=6 for retriever/ranker/QPP→decoder interface, not generic confidence or robustness; necessary source read, concrete owner gap pending root.

E5 cosine, reranker final-token score and QPP “relevant” score become per-document indicators, query/instruction weight1, repeated to token matrix to modulate QK^T; decoder attention parameters finetuned on answer NLL. Indicator is relevance proxy not truth/authority probability. Eq3 multiplication semantics, Eq2 L×L vs AppD h×h and complexity O(nh) wording conflict; negative scores/max normalization/missing denominator have no complete robust recipe in necessary core. Scaling a negative logit by <1 can increase relative weight, so no monotonic rejection claim or exact formula adoption.

Robust training replaces second half of top10 with5 relevant/3 partially/2 irrelevant and shuffles. Same Qwen2.5-3B, Wikipedia2018/E5 top10, NQ+Hotpot1epoch, fixed five noise samples across methods; five samples are not five independent train seeds. Normal originaltop10; noisy same5/3/2 construction; extreme all sampled irrelevant (not natural domain-shift proof). Table2 explicit guidance improves local results over VanillaSFT but aggregate features can harm NQ/Pop; robust-noise-only beats full OpenDecoder on extreme Pop (25.61 vs24.96). §5.3 more indicators can interfere on simple QA. Full gains combine indicator attention and noise-training interventions; no unique-cause claim. Ordering/top-k effects vary.

AppD negligible extra attention overhead does not include online reranker/QPP or full end-to-end retrieval/generation/training cost; precision/hardware/concurrency/CI Not Disclosed in necessary core for universal performance. No code run.

Actual Ch76 L132–153 quality/position-aware packing and L389–449 reranking/context packing select what reaches reader; L580–602 RARG uses relevance as corpus interaction prior, not decoder QK feature interface. Potential unique AGENT-RAG gap is passing declared relevance features into trained attention, with learned/proxy/version/cost identity and ordinary packing fallback. Formula ambiguity forbids precise recipe, yet source concrete interface/local ablation may support limited concept. Need root actual comparison/decision, no write yet.
