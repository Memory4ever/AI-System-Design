# Recovery Receipt — arXiv:2605.17193v1

- Recovered at: `2026-09-01T14:56:00+08:00`
- Former request: `MR-2605-17193-V1`
- Required identity: `arXiv:2605.17193v1`, first submitted `2026-05-16T23:29:42Z`
- Result: `recovered_exact_v1`

## Official identity and status

The official abs page `https://arxiv.org/abs/2605.17193v1` returned HTTP 200. It identifies the title, four authors, v1 submission history, an official PDF link and the arXiv nonexclusive-distribution license. It does not mark the paper withdrawn or removed.

- Abs response bytes: `40,604`
- Abs SHA-256: `c4b1aaa3faf4c2e73eebe28d3bb18e8ea056f579d536e6820d909720a7a7805b`

## Exact-v1 body recovery

The official HTML route returned HTTP 404. The official PDF route advertised `Content-Length: 4,076,663` and byte-range support. Because long responses were repeatedly truncated, the PDF was recovered through contiguous official byte ranges, reassembled in order, and parsed successfully as a 64-page PDF.

- Exact-v1 PDF: `https://arxiv.org/pdf/2605.17193v1`
- Response bytes: `4,076,663`
- PDF SHA-256: `edde49ce22de86ac25ad4d676f9003afec5c11513bee35438ca8db965322abe7`
- Parsed pages: `64`
- HTML route: `https://arxiv.org/html/2605.17193v1` — HTTP 404, not used for technical claims

## Full-text review locators

- Method / identity: main-text `Methods`; Supplementary Note 1 §§1.1–1.8; Supplementary Notes 2–3 intervention definitions.
- Evaluation: main-text `Results` subsections `Semantic Collapse in Extended Open-Ended Simulations`, `Semantic Collapse Resists Intervention`, and `Diagnosing Mechanisms of Semantic Collapse`; Supplementary Note 3 §3.7 statistical analysis.
- Counterevidence / limitations: main-text `Discussion`; Supplementary Note 3 §3.7 states that the regression does not itself warrant mechanistic or causal interpretation; Supplementary Note 5 calls the theoretical analogies heuristic rather than established properties and bounds early-to-late prediction as predictive regularity, not a recovered channel theory.
- Artifact: an immutable code or data commit used by this review is `Not Disclosed` in exact-v1.

## Claim boundary

The exact-v1 supports semantic contraction in the authors' closed-loop, text-only multi-LLM simulations across the disclosed model families, rounds, interventions and embedding/statistical protocol. It does not prove that every multi-agent architecture collapses, that externally grounded or tool-mediated systems cannot renew evidence, that the proposed recursive-channel explanation is causal, or that the reported embedding metric is a universal measure of knowledge novelty.

Current Books comparison found that `AGENT-MULTI-AGENT` already owns correlated consensus, evidence-independence, same-model convergence, coordination cost and single-agent / independent-verifier fallback. The recovered paper strengthens that existing boundary but does not add a distinct durable mechanism, so the final disposition is `No Change — Existing Coverage` and no Books writeback is required.
