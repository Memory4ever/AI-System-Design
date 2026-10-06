# 2601.09093v1 — trace-quality heuristic meets KV admission pressure


## 非作者当前处置

root actual必要source/owner、实际两段/邻接/末注POST通过，锁释放；具体gap深入并实际整合，不授日级Gate。
[Exact-v1](https://arxiv.org/html/2601.09093v1), PRIMARY_09093_NECESSARY.md §4/5.1,5.3.3–4/limits,A1–2/B1/AppDminimum. Proposed2+2+2=6 standard concrete scheduler/qualityhandoffgapdeepening, rootreviewpending. Trace-count/lowtoken heuristics missKVwaiting→step-endhiddenMLP andmemorysaturationcancellowesttrace→reconsider whichtrace tokeep underactualcachepressure; no truecorrectnesssignal guarantee.

Lastlayerstep-endtoken containsdouble-newline; allsteps inheritfinalanswer correctness pseudolabel. Pertrace5kpositive/5knegative butnegative-longerstepsweightedBCE,notactualstepvalidity supervision. MeanaccumulatedMLPscore ranksactivepaths, memorycannotallocate nextdecode cancellowest+freeKV; completedtracefinalscoreweightedvote. SourceAlg1activeT becomesempty yetWeightedVote(T) bookkeeping ambiguous; useprosecompletedoutputsconcept notexactalgorithmcopy. Cancellationchangessamplingpopulation,unscorednewtrace/no“double-newline”state not fullyspecified.

ThreeQwen4B/DS8B/Phi14B,4math/GPQAbench,N64,target-specific64HMMT2012–23solutions/prob→10ktraintraces,LABELviaQwenmathnumeric/SymPy;newtestyears2024/25. GH20096GBmodifiedvLLM,same modeldecodingB1(.6/.95/top20/64kQwenDS;.8/.95/top50/32kPhi). Precision/concurrency/independenttrainruns/CI/totaldatasetcollector/scorertrainingcost Not Disclosed; same64traces not matchedtotalcomputewhen pruning. SCordinaryvotevsSTEPweightedvote mixaggregation/scorer/trigger,notfullfactorialisolation. Table1QwenAIME STEP88.3<DeepConf90 andDSGPQA68.2<68.7; canmoretokensbutlesslatency throughwaiting so noallbest/alwayslessdecodeclaim.

§5.3.3DS8B/HMMT25N64 localwait0whiledecode1024>slim983,notallservingqueueseliminated. §5.3.4claimsN32but.9accuracy73.3matchesmainN64 andotherpopulationunclear;budget0.5–.9mean±1.8 isacrosssettingsnotCI/repetitions, notmemory-insensitivity guarantee. AppD scorerFLOPs<1e-6omits hiddenstateexposure/kernel/storage/synchronization/fullcollectortraining,notendtoendnegligibleoverhead. Limitsweaklabeldomainshift/servingcouplingexplicit.

ActualCh56 L241–245negativeMCTSexit dependsmonotoneupper; L665–671riskvoteuppercoversunfinishedvotes. Neither permits memory-pressure heuristiccancel basedhiddenqualitywithoutguarantee. PotentialuniqueINFER-SCHEDULINGgap2shortparagraphs underTTSnegativeexit: memorypressure asresource trigger,MLPonlyrankingproposalnotcausalstepquality,releaseKV/trackedcompletedvoting/cancellationpopulation,cost andordinarySC/preemptionfallback. Need root actualdifference andlock; notCh54/66doubleowner. Noartifactrun/productionSLO.
