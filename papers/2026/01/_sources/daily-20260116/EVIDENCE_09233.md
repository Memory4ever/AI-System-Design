# 当前独立终裁

root实际最低必要原源复核通过：争议；暂缓：最优初始化bridge未由实际目标支持；无Books。Algo1 base/GT soft-target不等B1 future-soft-Q oracle，E实际RL KL0且人口/评估配置不同，不能采用中心最优初始化bridge。root实际必要原源终裁中心争议隔离，保留局部实测；重开精确同目标future分布/初始化条件与matched控制，不全附件。 本次局部处置不授日级Gate；未运行代码/复现。

# 2601.09233v1 — practical soft targets do not inherit the global post-training optimum

Exact [v1](https://arxiv.org/html/2601.09233v1), PRIMARY_09233_NECESSARY.md §3–4/Tables1–3/limits, AppB/E/Cnecessary smoothing. Proposed2+2+2=6 centerDisputed/暂缓 pendingroot. SFTonehot narrows exploration→base-prior softtarget boostedGTlogitfinitebeta→test compatible initialpolicy forsubsequentRL, not global-optimum guarantee.

Eq3/4 Gibbs solution valid unrestrictedsequencepolicywithbaseKL support/objective; Eq5–7 bridge assumes positiveRLKLpenalty/currentSFTreference andexactRLoptimum. ActualE2KLcoefficient0 andnorm_adv_by_stdFalse does not implement this penalizedobjective, grouprelativeadvantage isn'tsameKLreference. Eq9writesnegativeKLminimization whileAlg1/10minpositiveCE; don't silentlyfixoradopt exactrecipe asconsistenttheory.

AppB exacttokenconditionalrequires allfuture expectedexp reward/softQ. B2 replacesadvantage withGTbeta/rest0 underoracleuniquehighrewardmanifold andnegligible recovery; this is approximation, sparsefinalreward alone doesn't implyeachGTtokenrewardbeta. B3telescopes exactsoftQratio notAlg1boosted-tokenapprox. Finiteβheuristic cannotthereforeinheritglobal optimum ofsequenceobjective. Preserve implementedbaseforward→GTlogit+β→softmax→studentfullvocabCE localmechanism; noglobaloptimality/safety/structural-knowledge guarantee.

DeepMathdisjoint10kSFT/10kRL/1kvalidation,DeepSeekR1solutions,twoQwen2.5-7B/Llama3.1-8B,8H200,AdamW.9/.95decay.01,SFTLR1e-5batch128max8192,noWarmup,checkpoint6thepoch viaheldoutloss; main‘oneepochall’vsE6thSFT differs. Llamauniformsmoothingextra,defaultotherbaselineconfig; no matchedsmoothing-onlycontrol read. RL1epochGRPOgroup8LR1e-6clip.2,max8192,temp1,batch128mini64. Precision/rep-trainingseedCI/fullbaseforward/trainingcost/concurrency ND. evaltemp.6,max8192,4decodingrunsnottrainingrep; E3LlamaAIMEpass@32 whiletableslabelaveragepass@1, do notaggregateAIMEasmatchedmetric. OmitunifiedbaselineLlama duepoorperformance; no inferredscore.

Additional C actual: smoothing lambda.01 is applied to base-prior before logit boost, so practical Llama target not raw base Gibbs. C gives within-GIFT with/without smoothing comparison but not a matched smoothing-only ordinary-SFT control, and Qwen smoothing marginally hurts; no all-architecture stable prior theorem.

Table1QwenGIFT Olympiad46.96<PSFT48.04/LUFFY47.04;preRLpass1GIFT38.92<SFT39.79;Table2Qwen64.10<ReLIFT64.55 withindividualMMLU/ARC reversals;Table3LlamaSFT-stageKL.5909>.5893. No allbest/causalpriorpreservation fromgeometry. Fixedbeta variesmodel,temperaturesearch+baseforwardcost notfree.

CurrentCh29 softtargets/teacherlineage andmask don'timplementthisspecificGibbsheuristic, but centeroptimal-initbridge notvalid foractualtraining; do not writeBooks onguarantee orforceExisting. 6centerDisputedretainlocalexperiments, rootfinalpending. Reopen exacttokenobjective/errorbound plusactualmatchingRLKLprotocol/smoothing andmatchedmetric/cost controls; not allreferences/experimentsmandatory.
