# 2601.09195v1 — probability-gated supervision does not classify semantic importance

Exact [v1](https://arxiv.org/html/2601.09195v1); PRIMARY_09195_NECESSARY.md §4–6, AppendixA/B decisive proof/config. Proposed2+1+2=5. SFT single-reference incidental expressions→stopgradient p_target>tau loss mask→reconsider which teacher-forced positions receive supervision, not delete inputcontext.

Gemini3pro marks core/trivial; Qwen3-4BBase probabilities show different distributions with p1e-6, but different marginaldistributions do not certify individual lowp as trivial. Core longtail facts may lowp. Training mask detachedprobabilitystrict>tau; Eq5 averages by totalT notretainedcount, so maskratio also changesgradient scale. Lowp tokens remain in teacherforcing prefix. No matchedlossmass/semanticlabelmask/rare-factbudget controls in necessarysource. §6.1 knowledge-intensiveGPQA declines as threshold increases, authors attribute rareentities; do not adopt highp=logic-only or negligiblelowpvalue.

Theorem1 requires localfullrowrankJ/sigma_min>=gamma; proof supports lowerbound gamma(1-p), not actual monotone gradientnorm ordering across tokens/contexts with differentJ, nor semantic correctness or interference. No falseclaimtheorem itself disproved; isolate prose stronger than bound.

2000highrewardInfinityInstruct,5base modelsQwen0.6/4/14B,OLMo7B,Llama8B;8H20,perdevicebatch1accum4,length8192,1epoch; maintrainingLR/precision/seeds/CI/fullwallclock ND. Evaluate GPQA/GSM8K/MATH/AIME/IFEval;32generationAIME/8others are decoding samples not training seeds. Qwen/OLMo temp.7topP.8topK20;Llama.6/.9;maxAIME32768/others8192. Table1 ProFit Qwen4GSM87.55<DFT87.83,0.6GSM59.78<DFT62.42,14BAIME16.56<DFT17.29,LlamaGPQA21.4<SFT23.3,OLMoGSM78.25<SFT78.43. Aggregateimprovement notalltasksemanticguarantee;singleLoRA/rank curvesnot universalintrinsicdimension. SubsequentGRPO onlyQwen0.6/32H20/DeepScaleR,initdifference not isolatedlearninglaw.

Actual Ch29 L98–132 has response mask/provenance and IG-selected spans but not student-confidence token-gating/totalT denominator as alternative. Potential TRAIN-SFT minimal two paragraphs: dynamic confidence proposal notsemanticowner, rarefacts/maskratio and qualitycontrols, ordinaryverifiedCEfallback. Rootactual necessaryevidence/owner must decide realgap versus OnlyReport; not automaticBooks or reliance on theorem for coreidentification.
# 当前终态收据

root非作者实际必要primary/具体owner终裁通过：深入完成，整合：[TRAIN-SFT Ch29](../../../../books/part-04-training-system/29-sft.md)，IG选段后两段，POST通过。§4–6/Table1/A/B核到confidence gate与全历史分开；不授高p必core或实际梯度全序，低p实体与总T maskrate、预算/质量切片保留。Ch29 L132/134与末注1224实际写入，root必要源/owner及前后交接非作者POST通过。 日级未授，未复现实验。
