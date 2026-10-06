# 2601.09076v1 — local ZO head frees client backprop, while formal estimator normalization is unresolved


## 非作者局部终裁

root actual Ch36 L1589/1591、L2038末注及前后 POST通过，锁释放。6分gap深入、整合终裁；方程子命题仍隔离。
[Exact-v1](https://arxiv.org/html/2601.09076v1), PRIMARY_09076_NECESSARY.md III-B/IV, V assumptions/conditional low-rank, VI LM/cost/aux-head controls and AppB minimum. Proposed2+2+2=6 standard, concrete split-training gap pending root; score client/server update protocol, not headline fullaccuracy/unbiased/globalconvergence.

Client trains front+auxiliary local head with zeroth-order one base/one perturbed forward; send smashed activations everyk localupdates, server first-order sequential SFLV2 trains tail, front/auxheads federated-average while server tail noaverage. Auxiliary target decouples local gradient from server backward; this is more than substituting ZO into unchanged full backprop. Costs include auxiliary capacity/multiple evaluations, server work and periodic aggregation.

LM GPT2small/medium,E2E3clients,split3/6blocks;aux1/3Transformer blocks+unembedding initialized from server start,allcomponentsLoRAr8/basefrozen. Author48GBRTXA6000NVL label, ResnetCIFAR controls are different workload. TableIII GPT2medium4.03GB vsSplitLoRA4.59 vsCSE9.09 and FLOPs5.26/5.68/9.48 are local client-resource points, not full training walltime; fixed communication rounds/volume not matched totalforward/latency/auxcapacity. VI-Caux0–3blocks compares fixedround quality/capacity. Precision/sequence length/concurrency/CI/full totalcost Not Disclosed for broad efficiency claim, not adopted. AppB Hessian rank is Resnet empirical, not direct LMtest.

Central theory not adopted: Eq2 uses d*u finite-difference factor while u described Gaussian or uniformball; Def1 normalizes Gaussian direction to unitsphere yet calledGaussian smoothed; Eq4 drops d. For linear f and uniformunitsphere E[uuT]=I/d, Eq4 returns gradient/d whereas Eq2d corrects it. Spherical boundary averaging and ball smoothing are also not same. Thus no coherent distribution/normalization permits borrowing unbiased/convergence bound as written. Reopen formal claim only exactdistribution+normalization+smoothedobjective correction, not allappendices. Conditional Lsmooth/boundedgradient/variance/client-outputdrift and loweffectiveHessianκ assumptions remain stated, not general guarantees.

Actual Ch36 L1581–1589 splitfine-tuning explains frozen front+activationcompression/server reconstruction, but not trainable front via localaux ZO/serverFO handoff; Ch29 ZOadapterquery estimation is separate owner. Potential unique TRAIN-DISTRIBUTED-TRAINING gap limitedconcept2paragraphs aftersplit section beforehandoff, no Eq2/4 recipe/theory adopted; include activation/privacy/aux+forwardcost and central/FO fallback. Root must review source/core normalization and minimal gap before write; not proposed entire sourceDisputed just because unused formal claim conflicted. No artifact run.
