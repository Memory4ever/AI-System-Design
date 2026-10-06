# 2601.09159v1 — partition collision codes replace the retrieval metric

Exact [v1](https://arxiv.org/html/2601.09159v1), PRIMARY_09159_NECESSARY.md §3/4/Table1–2/Limitations, decisive C2/C3/C4, E2/F1–2 config. Proposed2+2+2=6; concrete representation/index interface gap pending root. FP dense retrieval cost→data-derived random partitions and compact leaf indices/collision-count ranking→reconsider retraining-free representation, index compatibility and quality budget. Not inference-model quantization.

Same embedding model maps corpus/query; iForest random features/splits gives t indices, storedceil(log2 psi) per tree, compare equal leaf counts; no training optimizer. Online query still pays base encoder plus mapping, not all computation eliminated. IKE-VD distance-to-anchors more expensive. IVF coarse candidates still chosen originaldense kmeans; HNSW replaces distance with collision metric. This changes similarity function, not lossless storage preservingcosine. Partition artifacts/corpus distribution, query mapping and index revision must move together (engineering inference).

CPU dualXeonGold6330 56physical112threads503GiBRAM in-memory allthreads; two4096D LLM2VecMistral7B/Qwen3embedding8B, sixtextdatasets (1Msubsettwo). Table1 separates Other construction/corpusmapping vs allquery Search; searchtime avg10consecutive runs, §4.2 10random seeds, otherexperimentsone seed. Precision basevectorsFP32 incompressionreference, fullqueryencoder timing/concurrency/CI endtoend ND. CSR comparison includesmapping+similarity, fixedcodelength4kbytes, not trainingcost fully matched. ψ2–16 validationtuned per dataset; Touche30% testsplit validation/70%test and FEVERorigvalidation; t4096typical, no crossmodalguarantee. Main nDCG counter HotpotQwen76.85→75.41/Touche76.41→73.35; optimalVD can beatIKE, no universalwinningdesign.

Theoretical subclaims not adopted: C2 uniform Voronoi cell mass asserted overrandom anchor process does not certify fixedpartition uniformoccupancy; C3 mean half mass per split does not imply equal probability leaves of unequaldepth or exactψleaves underheightlimit; C4 declaresTheta iid for fixedquerypair then later strict positive covariance order from shareddata/additionalrandomness, and independent dimensions do not force identical collision probabilities acrosscoordinates. No demonstrated guarantee relevance-lossless, bitindependentorstrictcorrelationhierarchy. Reopen these only with explicit randomexperiment/leafbalance and proof, not entireappendix mandatory.

Current Ch76 L299–329 distinguishes encoderweight PTQ,scoremargin and geometry metrics but not compactrandompartition collision codes tied tocorpus/index. Potential AGENT-RAG 1–2paragraphs only learned-free transformation,changedmetric/artifact/cost/qualityregression+densefallback. Rootdecidegap/lock; mathematical guarantees isolated, no code run.

## 当前实际写后收据

6分具体gap深入，Ch76 L338/340 与 L1451末注，root实际330–347及邻接/末注非作者POST通过，锁释放；整合终态，不授附录概率保证或日级。
