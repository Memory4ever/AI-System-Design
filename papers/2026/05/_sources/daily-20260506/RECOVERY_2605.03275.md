# arXiv:2605.03275v1 Full-text Recovery Receipt

- Source family: `SF-2026-ARXIV-2605-03275`
- Primary identity: `arXiv:2605.03275v1`
- First public: `2026-05-05T02:04:10Z`
- Recovery route: ResearchGate public full-text mirror carrying the exact title, both authors, `10.48550/arXiv.2605.03275`, `CC BY 4.0`, and the manuscript label `May 2026 • Draft for arXiv / KDD 2026 ADS Track`.
- Retrieved: `2026-09-01` (Asia/Shanghai)
- URLs:
  - https://arxiv.org/abs/2605.03275v1
  - https://www.researchgate.net/publication/404476862_Beyond_Similarity_Search_A_Unified_Data_Layer_for_Production_RAG_Systems

## Identity reconciliation

The mirror title, author list, arXiv DOI, abstract and manuscript month match the official arXiv v1 identity. It is used only to recover the inaccessible body; the official arXiv record remains the authority for first-public date and version identity.

## Method and state ownership

The paper contrasts a split vector-store / metadata-store / cache path with a unified PostgreSQL 16 + pgvector 0.6.0 path. In the unified path, document, embedding, metadata and access policy share one transaction and query planner. The durable systems claim is therefore about ownership: freshness and authorization are enforced before retrieval result admission, rather than repaired by application-side joins or post-filtering.

## Evaluation contract

- Corpus: 50,000 documents, 128-dimensional embeddings, 20 tenants, 5 categories, uniformly distributed across 180 days.
- Repetitions: 200 queries per query type; p50, p95 and p99 reported.
- Runtime: PostgreSQL 16, pgvector 0.6.0, HNSW.
- Comparison: Stack A simulates split-system coordination by separating PostgreSQL tables and merging results in application code; it is not an actual Pinecone, Qdrant or Milvus deployment.
- Reported evidence: pure-similarity latency is nearly equal in the controlled setup; constrained queries favor the unified path. The paper also reports a measured synchronization window and a tenant-leakage simulation under an application-filter bug.

## Limitations and claim boundary

The 50k-document experiment is intentionally small and controlled. Because the split baseline is simulated inside PostgreSQL, the headline percentages cannot be generalized to a particular external vector database, different hardware, production concurrency, billion-scale corpora or an undisclosed SLO. The paper itself preserves the coexistence boundary: specialized ANN systems remain reasonable for large, mostly pure-similarity workloads; a hybrid hot/warm/cold design is proposed for larger deployments.

## Books decision

`No Change — Existing Coverage` at `AGENT-RAG`. Chapter 76 already owns the durable conclusion: ACL/tenant policy must be applied before candidate admission, freshness requires atomic publication/version semantics, and specialized versus unified retrieval storage is a workload-dependent trade-off. Adding this paper as another named case would duplicate the existing reasoning without changing the design conclusion.
