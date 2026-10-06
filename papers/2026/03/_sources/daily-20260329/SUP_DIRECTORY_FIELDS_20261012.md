# 03-29补充：本轮有限目录原字段

本轮2026-10-12实际原始请求。只保存title/identity/date及分页停止字段，不保存content、signed cover或无关全文。目录日期不自动等firstpublic。API路径及参数与本日V3_DIRECTORY_FIELDS一致；Hunyuan publicAt/publishedAt/display三字段全部无March，有限9/9不授全历史无遗漏。Seed type1 token20→40跨03-28下/上界后停，type2 token0 has_more=false但14/19差额仍隔离。

## Hunyuan POST renderType0 pageNum1 pageSize20

```text
code=0 total=9 rows=9
{"id":100116,"title":"When Do Larger Batches Help Scale LLM Reinforcement Learning?","publicAt":1790150728,"publishedAt":1789707529,"displayPublishTime":1790006400}
{"id":100100,"title":"Introducing Hy4 preview","publicAt":1787896874,"publishedAt":1787896672,"displayPublishTime":1787846400}
{"id":100091,"title":"From LR to ELR: A Better Heuristic for Pretraining Dynamics","publicAt":1787231073,"publishedAt":1785989409,"displayPublishTime":1785945600}
{"id":100087,"title":"Hyra: A simple yet effective scaffold for general discovery","publicAt":1784563044,"publishedAt":1784111171,"displayPublishTime":1784599200}
{"id":100064,"title":"Introducing Hy3","publicAt":1783348861,"publishedAt":1783319811,"displayPublishTime":1783440000}
{"id":100039,"title":"Real life is where context gets hard","publicAt":1777554399,"publishedAt":1777227059,"displayPublishTime":1777532400}
{"id":100061,"title":"Hy3 preview: The First Step in Rebuilding the Hy model","publicAt":1783313906,"publishedAt":1782369407,"displayPublishTime":1776873600}
{"id":100015,"title":"Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping","publicAt":1770971763,"publishedAt":1770971763,"displayPublishTime":1770971763}
{"id":100025,"title":"Learning from context is harder than we thought","publicAt":1770112927,"publishedAt":1770090898,"displayPublishTime":1770090898}
```

## Seed type2 token0

```text
{"next_page_token":"","has_more":false,"total":19,"BaseResp":{"StatusMessage":"success","StatusCode":0}}
1939 | 2026-02-11T16:00:00Z | Seedance 2.0 Official Launch
1806 | 2026-02-12T16:00:00Z | Deeper Thinking, More Accurate Generation | Introducing Seedream 5.0 Lite
1801 | 2026-02-13T16:00:00Z | Seed 2.0 Official Launch
2155 | 2026-02-15T16:00:00Z | Dola-Seed-2.0-Preview Model Release on Arena
1202 | 2026-03-31T16:00:00Z | ByteDance Seed 2027 Foundation Model Campus Recruitment is Now Open (Internships Included)
1798 | 2026-04-08T16:00:00Z | Introducing Seed Full-Duplex Speech LLM: Attentive Listening, Robust Interference Suppression, Enabling More Natural Interaction
2132 | 2026-04-22T16:00:00Z | Seed3D 2.0 Released: Higher Precision and Greater Usability
2152 | 2026-06-18T16:00:00Z | Seed-2.1-Preview Model Release on Arena
1949 | 2026-06-23T00:02:42Z | Seed2.1 Officially Released: Advancing AI Productivity
1950 | 2026-07-06T16:00:00Z | EdgeBench: Measuring Real-World Environment Learning and Discovering a New Scaling Law
2159 | 2026-07-07T16:00:00Z | Beyond Generation, It Understands Design | Introducing Seedream 5.0 Pro
1788 | 2026-07-19T16:00:00Z | From Speech to Audio Creation | Introducing the Seed Audio 1.0 Audio Creation Model
1970 | 2026-07-30T16:00:00Z | One-take Creation, Flexible Referencing: Introducing Seedance 2.5
2186 | 2026-08-04T16:00:00Z | SeedRealtime Audio-Visual Full-Duplex LLM Released: Toward Omni-Modal Natural Interaction
```

## Seed type1 token20

```text
{"next_page_token":"40","has_more":true,"total":82,"BaseResp":{"StatusMessage":"success","StatusCode":0}}
1992 | 2026-02-25T12:00:00Z | veScale-FSDP: Flexible and High-Performance FSDP at Scale
1412 | 2026-02-26T16:00:00Z | CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation
1420 | 2026-02-26T16:00:00Z | Steerable Instruction Following Coding Data Synthesis with Actor-Parametric Schema Co-Evolution
1411 | 2026-02-28T16:00:00Z | How RL Unlocks the Aha Moment in Geometric Interleaved Reasoning
1607 | 2026-02-28T16:00:00Z | Learn Hard Problems During RL with Reference Guided Fine-tuning
1644 | 2026-03-01T16:00:00Z | Anatomy of the Modality Gap: Dissecting the Internal States of End-to-End Speech LLMs
1664 | 2026-03-01T16:00:00Z | On the Residual Scaling of Looped Transformers: Stability and Transferability
1424 | 2026-03-11T16:00:00Z | Permutation invariant multi-scale full quantum neural network wavefunction
1414 | 2026-03-14T16:00:00Z | Disentangling Tensor Network States with Deep Neural Network
1426 | 2026-03-15T16:00:00Z | Mixture-of-Depths Attention
1661 | 2026-03-19T16:00:00Z |  FlexTrain: Scalable Hybrid-Parallel Training with Elastic Resource Utilization and Consistent Accuracy
1407 | 2026-03-20T16:00:00Z | Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression
1337 | 2026-03-22T16:00:00Z | Development and large-scale benchmarks of a protein-ligand absolute binding free energy toolkit
1334 | 2026-03-23T16:00:00Z | SIMART: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM
1428 | 2026-03-23T16:00:00Z | UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation
1606 | 2026-03-24T16:00:00Z | TopoMesh: High-Fidelity Mesh Autoencoding via Topological Unification
1335 | 2026-03-25T16:00:00Z | Towards Generalizable Robotic Data Flywheel: High-Dimensional Factorization and Composition
1336 | 2026-03-25T16:00:00Z | Hessian-informed machine learning interatomic potential towards bridging theory and experiments
```

## Seed type1 token40

```text
{"next_page_token":"60","has_more":true,"total":82,"BaseResp":{"StatusMessage":"success","StatusCode":0}}
1994 | 2026-03-31T12:00:00Z | GPU Accelerated Minimal Auxiliary Basis Approach TDDFT for Large Organic Molecules
1430 | 2026-04-07T16:00:00Z | Not all tokens contribute equally to diffusion learning
1650 | 2026-04-08T16:00:00Z | Topological invariant of periodic many body wavefunction from charge pumping simulation
1657 | 2026-04-09T16:00:00Z | Nexus: Same Pretraining Loss, Better Downstream Generalization via Common Minima
1586 | 2026-04-10T16:00:00Z | Protenix-v2: Broadening the Reach of Structure Prediction and Biomolecular Design
1670 | 2026-04-12T16:00:00Z | Continuous Adversarial Flow Models
1589 | 2026-04-14T16:00:00Z | Seedance 2.0: Advancing Video Generation for World Complexity
1652 | 2026-04-15T16:00:00Z | LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories
1635 | 2026-04-19T16:00:00Z | Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence
1443 | 2026-04-21T16:00:00Z | Seed3D 2.0: Advancing High-Fidelity Simulation-Ready 3D Content Generation
1669 | 2026-04-22T16:00:00Z | Context Unrolling in Omni Models
1605 | 2026-04-25T16:00:00Z | MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production
1637 | 2026-04-29T16:00:00Z | Leveraging Verifier-Based Reinforcement Learning in Image Editing
1654 | 2026-04-30T16:00:00Z | End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer
1665 | 2026-04-30T16:00:00Z | CARD: Coarse-to-fine Autoregressive Modeling with Radix-based Decomposition for Transferable Free Energy Estimation
1639 | 2026-05-03T16:00:00Z | Video Generation with Predictive Latents
1587 | 2026-05-05T16:00:00Z | Agentic Discovery of Exchange-Correlation Density Functionals
1629 | 2026-05-06T16:00:00Z | Continuous Latent Diffusion Language Model
1631 | 2026-05-06T16:00:00Z | TDDFT Gradients and Nonadiabatic Couplings with Minimal Auxiliary Basis Set Approximation for Fewest-Switches Surface Hopping Dynamics
1667 | 2026-05-09T16:00:00Z | Towards Robust Sequential Decomposition for Complex Image Editing
```

## Anthropic当前March publishedOn

```text
bytes 282283
nvestigation, code inspection, finding bugs, code examination\",\"name\":\"Object CodeMagnifier\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-31T22:17:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"how-australia-u
g\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":{\"backgroundColor\":null,\"illustration\":null},\"publishedOn\":\"2026-03-24T10:41:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"economic-index-
1000x1000.svg\",\"width\":1000},\"keywords\":\"Head, nodes\",\"name\":\"Node-Head-Constellation\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-23T23:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"introducing-ant
361111949b32136a308ef35b6864-1000x1000.svg\",\"width\":1000},\"name\":\"Object Hourglass Cosmic\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-23T23:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"long-running-Cl
th\":1000},\"keywords\":\"Hero illustration: Hand HeadNodeThink\",\"name\":\"Hand HeadNodeThink\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-23T23:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"vibe-physics\"}
g\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":{\"backgroundColor\":null,\"illustration\":null},\"publishedOn\":\"2026-03-13T10:15:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"diff-tool\"},\"
puting, technology, work computer, office setup, computer interface\",\"name\":\"Object Desktop\",\"type\":\"hero\"}},\"publishedOn\":\"2026-03-06T10:30:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"mozilla-firefox
ies\":[{\"_key\":\"research\",\"_type\":\"tag\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":null,\"publishedOn\":\"2026-03-06T00:00:00.000Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"exploit\"},\"su
g\",\"label\":\"Research\",\"value\":\"research\"}],\"illustration\":{\"backgroundColor\":null,\"illustration\":null},\"publishedOn\":\"2026-03-05T19:59:21.508Z\",\"slug\":{\"_type\":\"slug\",\"current\":\"labor-market-im
```

