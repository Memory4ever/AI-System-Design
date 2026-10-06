# 2602.09541v1 必要审阅（作者准备，Source待独立）

[Scalpel](https://arxiv.org/html/2602.09541v1)，Feb11/root AB已核；2+1+2=5。旧head固定纠正direction对多簇activation过粗→offline trusted/perturbed activation GMM、component coupling→online局部direction与membership scaling，改变steering分支，非直接真实事实validator。

scalpeloutline §3.2–3.4 L84–168：trusted来自validimageQA、hallucinated来自扰image/box但保持QA，标签是受控corruptionproxy非所有natural hallucinations。每head独立GMM、OT LP coupling后取row最大j*，运行时argmaxH component并加αbase×maxposterior×(μT−μH)，并未执行完整stochasticSchrödinger bridge；不能把理论distributionmapping授runtime最优/保持semantictruth。c是H内部相对component置信，不是“当前token真hallucination”概率，始终可对factualactivation施加纠正，需要反侧边界。Probe1500trusted/corrupt筛topk，有label/fit成本，不是zero-training。

scalpelconfig/eval §4 L180–225/T1–3：LLaVA1.5/Qwen2.5VL7B、balancedPOPE27k、COCO/AOKVQA/GQA binaryyesno，MME部分能力。ICT实际reimplementation，可比但未列训练fixture分离、hyperparametersearch、seedCI，no natural-freegeneration可靠性结论。T2singlemoduleAOKpopular等有相对ICT退化，objectremoval能改善个别color/reasoning，组合不是每partial必然安全；GMM1–32/tuningretention也需独立validation。没有matchedofflinecalibration/latency/MFU/存储/GPU/precision/batch/SLO测量，headposterior/lookup/vectoradd非0计算，不能采用“without added computational cost”。只保留组件条件steering与需要独立facts验收的边界；actualowner拟MULTIMODAL-REPRESENTATION/MODEL-MULTI-HEAD-ATTENTION，Source后再定位唯一owner。
