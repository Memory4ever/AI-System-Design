# 2601.09085v1 — greedy diversity-reward changes group credit, but adaptive scale claim and peak-cost aggregate are not universal


## 当前独立终裁收据

root实际必要source/owner与 Ch33 两段/邻接/末注POST通过；L557/2693再次定点确认 λ 无需手调并非尺度无关，其他 embedding/reward 配置未消失。6分深入、实际整合，锁释放；不否定无需手调λ这一事实，不采用scale-invariant/无配置成本保证。
[Exact-v1](https://arxiv.org/html/2601.09085v1), PRIMARY_09085_NECESSARY.md §3/Alg1,4/Table1,5.3 and B1–5/7. Proposed2+1+2=5 standard, actual reward-contract conflict/gap deeper, root decisionpending. Redundantgrouptrajectories→MMRgreedyrewardadjustment beforegroupadvantage ratherthansampling/removing→reconsider credit object andwholetrainingcost.

Normalizejina-small embeddings,choosehighestrewardfirst withunchangedr, thenrankrestbyλr−(1−λ)maxcosselected anduse selectiontimeadjustedscoreasreward. Allresponsesretained. λ=sigmoid(std rawreward). Raw-scales matter: rescaler→cr changesstd andλ, boundedrange doesNOT scaleinvariant. Evenequalallcorrectorallwronggroupscanreceive differingadjustedrewards fromdiversity, henceobjective no longerpurecorrectnessonly; nouniversalno-signalfilter equivalence, diversity≠semanticvalidity. Firstleaderunscaled vsrestλscaled differscommonaffineweighting.

DSdistillQwen1.5/7B,Llama8B,largerLoRAr64α128,bf16,AdamW1e-6,6responses,temp.7,length3584,prompt512,vLLMbf16prefixcachememory.7,seed2025; effectivebatch48/perdevice6×accum8 mayomitdevicefactor, don'tassertglobalbatchformula. Same500stepsGRPO/DR/evalevery50;DAPOdynamic200/eval10 versusnoDS500/eval10then50. Table1peakcheckpointselectedtestaverage across5bench,notprespecifiedsamequalitystop/heldoutbestselector; lastsamplefewerstepsnotactualearlystopprotocol.

2H10080GBtrain/1A10040GBeval. Actual1.5GRPOpeakstep100both,4.08→4.13hrs slightlyworse;otherqualitysliceslower. Headline70.2%timeaverage combinesDAPOdynamicremoval andMMRreward,not isolatedMMRgain;strongsameNoDSbaseline exists but doesn'tgiveallregimes win. Samegroupsemanticpreprocess addsO(G²)/embeddingwork; traininglog inclusion/eval/selectioncost andrepseedCI Not Disclosed in necessarycore. Adaptiveλvsfixed only1.5localTable2notuniversalparameterfree. No leaderboardheadline/scaleinvariantclaim/code execution.

ActualCh33 L543–551 declaresgroupunique/mixedoutcome samplercontract; L1999–2001 saturationadmission differs from rewardreweighting allresponses; L1458explorationreward isGUIcontinuousdistinct notspecificgreedyMMR. PotentialgapTRAIN-GRPO1–2paragraph rewardobjective change/scaleversion/qualitycost control, orOnlyReport ifsameuncontrolledselectorcostcannotjustifynewstable recipe. Need root actual minimal source/ownerdecision; no forcedBooksdiff.
