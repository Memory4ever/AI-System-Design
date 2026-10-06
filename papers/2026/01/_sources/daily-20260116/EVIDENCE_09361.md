# 2601.09361v1 — masked spectral initialization is not a persistent update constraint

Exact [v1](https://arxiv.org/html/2601.09361v1), PRIMARY_09361_NECESSARY.md §3–5/Table1–4/limits. Proposed2+1+2=5: SFTspectral initialization may miss RLVR update regime→union bottom-entry masks in originalW/rankrApprox thenSVD lowrankinitialize+subtractscaledBAfromfrozenresidual→consider initialization prior versus actualtrainableconstraint. Standardmechanism plus actualguarantee counter; no formalproof appended.

Eq6/7 bottomrho quantile on entries (not Hessianeigenvalues) union mask WGeo; Eq1–5initializeBAfromWGeo and Wres=W-alpha/r B0A0, so initialfunctionexact algebra matchesW. Subsequent unconstrainedA/B updates canrotate/change entries outsideinitialmask orhead directions; frozenWres doesn'tguarantee parametererasure/pretrainedfeaturepreservation/safetrustregion. Entry-smallnotcurvatureproof, WGeospectrumconstructedfrompretrainedviewnotlearnedRLupdatein§5.1,lowrankstructureobservationalnotgeneraltheorem. Eq10 ||ΔWvk||/||ΔW||F notexactcosangleforarbitraryrank; notopology/knowledgefidelityfromNSSsingularshift. Localinitmethodstillvalidnotdeletedforoverclaim.

Qwen3-8BBase/Llama3.1-8BInstruct DeepMath103k GRPO rank16rho.2; ablationsQwen3-4BBaseGSM8Kdifferentpopulation. Table1QwenAIME25Geo21.67<Full22.08/MATH78<78.4/GPQA37.92<MiLoRA38.26;LlamaMATH61.9<Full62.4. Table2periteration185s vs231 and VRAM68.43%vs95.73%, absolutehardwarecapacity/precision/batch/context/rollout concurrency/SLO/preprocessSVD/trainingsteps/offlinecost/seeds/CI ND readscope; ratiosrelativebutnotfullE2E. SearchLRstress5e−5notmatchedper-methodoptimizedcurve; coincidenceKL/rewardcollapse notuniquecause. Table3usesnew4Bconfignotsame8Bmechanismpopulation. No code/replication.

CurrentCh30actual98–117 zero-init/functioninheritance and matchedLR/capacity/searchconstraints do not implement unionmaskSVD method. Proposed OnlyReport limitedinitialization witness: no persistentconstraint/retentionmechanism established beyond existingfactorparameterization; incompletebudget/controls can't support general safe-RLVR recipe. NotgenericExisting. If root sees real durableinitgap may retain narrowly initialization-only, not guaranteedgeometry. Root finalpending noBookslock.
# ROOT终裁

root实际Eq1–8/Table1–3与Ch30初始化/LR段核，5=2+1+2标准完成/OnlyReport FINAL通过；中心geometry preservation/safe RLVR未采用，mask与Wres只构造初始view/function而后续BA可离开。重开限实际持续约束与matched几何/初始化训练对照，局部数字留报告，非泛Existing。

