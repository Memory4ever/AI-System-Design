# 下一组必要证据：10819 / 10825 / 10833 / 10885

四家族准入已独立校准，119日期交集，采用exact-v1；current abs均v1，无明确withdraw/correction声明（BEIGHTLAST1），10833 ECIR2026 acceptance不单独构成更早正文公开证据。未核代码或复现。支持与直接反侧足够即止；root必要证据与Only处置通过，FlowCache Ch24与10833 Ch76实际正文/邻接/末注已由root非作者POST通过、窄锁释放，不授日级。RLCER保留具体候选与证据、仅报告，现Ch33的outcome-calibrated rubric admission/共适应和成本原则已承载长期判断，具体corr阈值/validfraction recipe不另造缺口。原raw BEIGHTINITIAL/CORE0–3/TAIL0–3/EXTRA0–3按标题顺序，CONFIG3是RLCER必要配置，LAST0是FlowCache直接反侧/runtime，Source L号非物理行。

## [10819 RePO](https://arxiv.org/html/2602.10819v1)

5（2+1+2），所声称on-policy的设计假设反侧深入。§3 Eq5明确rephrased sample来自πθ(.|P(q,k))，而普通组来自πθ(.|q)；先扩G+1、删meta token，然后failure fraction≥ρ时替换最低reward项、以新组GRPO更新。相同θ/nativevocab不使条件分布相同，post-processing还改变sample映射与选择人口，未披露将该proposal严格校正回无k任务策略的ratio；故“strictly preserving on-policy”不能采用。可采用自模型条件rephrase+低reward替换这条有限监督接口，不借Eq11声称正确/无偏gradient。

LUFFY collapse解释集中vocabulary mismatch，但native词表可评分不证明正确归因或全梯度稳定，未有控制唯一vocab/tokenizer因子的消融。SuperGPQA11k单epoch/数学Hard18k与multi-source10k/financial10k不同协议。Qwen2.5Math7B与Qwen4B受限结果，Table4 RePO AIME24/AMC/Minerva仍低base；Table5 Qwen3-8B数学仍低base，不授保持所有generality。金融指标只模型评价，非金融建议。

RL G8/B512/lr1e−6、verl vsLUFFY不同框架；SFT samefinancial data lr1e−5/16k但非相同训练tokens/rollout/compute。avg@4用于AIME/AMC、其他pass@1，financial Qwen3-30BA3B judge/部分1000随机测试；teacher T1/topp1不是learner eval统一配置。hardware/precision/learner完整采样数值、ρδ具体值/额外rephrase成本/训练repeat与不确定性ND，不以entropy平稳证明全概率一致。仅报告：保留新条件proposal与原强on-policy主张的直接反侧，不把成熟生成/替换recipe升为通用无偏或稳定保证；无拟书稿“on-policy保持”采用。原source CORE0 110–139/165–187；TAIL0/EXTRA1 211–264/320–334。

## [10825 FlowCache](https://arxiv.org/html/2602.10825v1)

6（2+2+2），标准并拟具体cache边界差额加深。§3为每个active ARvideo chunk分别累计relativeL1，早m步强制重算、各自超过阈值reset/recompute，其余reuse activation；同一全局denoise时间不等各chunk同phase/cacheage。另将completed-clean KV与active denoising KV分区，满budget后合并新completed状态，再按pooled attention importance−cosine mean redundancy选per-head TopB。reuse与history compression分别改变轨迹/历史，不是exact cache或原模型无损执行。

不采用Theorem1/Corollary1的普遍monotonic必要性。B proof将最优conditional velocity写成已知单endpoint表达，且L402–413用“自然data norm通常更大”、norm interpolation单调与增长较缓直接代替所需导数界；都非已有假设自动推出。C中state不同不保证norm不同、approximately相等分子不保证ratio严格不等1。机制可作为经验chunk控制分支，不将这些strong theorem移入书。D2均值key后内积可以避免全pairmatrix；原设置zero diagonal对归一化key是常数shift，softmax不变，但原Eq20记号不背书已核实现。

同checkpoint MAGI1-4.5Bdistill/SkyReelsV2-1.3B540P，A80080GB，MAGI24frame/chunk/64steps/10chunks；Sky97frame/overlap17/50steps/2chunks。VBench-long和8metricselected VBench*不是同metric；Table1 fast77.93与83.05相比vanilla77.06/83.84有后者退步，非所有quality无损。必要Table2 fixedfast chunkwise无compression77.66→有77.93只是局部VBench；PhysicsIQ Table4 vanilla47.60→chunkreuse43.10→compression39.34，不能称物理质量完全保持。无reuse的独立Table6 8→7/6/5chunks42.84→34.05/31.25/28.45GB，分数47.60→47.55/46.72/47.65，6chunk非±.1。D1声称end-to-end timing但未披露所有测量boundary/precision/batch/concurrency/重复seed与SLO，所列speedup非生产或任意长视频保证；预热/selector/cache存储不免费。

拟Ch24 cache差额：当前1122后denoiser-output approximate reuse与1189 trajectory-conditioned policy已经覆盖一般errorbudget，但尚需核实际正文是否含多activechunk各自phase/累积reuse状态与completed-clean/activeKV压缩分责；只补该接口/预算，不搬争议定理/所有quality或Eq20实现。root实际POST核Ch24正文1180–1203与末注1630，窄整合已通过。source CORE1 123–197；TAIL1 199–240；EXTRA0 368–448；LAST0 449–522。

## [10833 Training-Induced source bias](https://arxiv.org/html/2602.10833v1)

5（2+1+2），实际评价反证深入。samegoldhuman及Llama2rewritten平行corpus，E5/Contriever/AugTriever unsupervised vsMSMARCO与in-domain/LLM rewrittenfinetuning。InfoNCE/4GPU/perdevice16/acc4/effective256/lr1e−5/warm.05，MSMARCO1epoch、SciFact30epoch、NQ从307373采30000pairs3epochs；matchedcorpus条件不是同所有历史预训练。Contriever MSMARCO用现成checkpoint，不能称作者所有stagecontrolledidenticalrun。

Tables3–6具体反侧：unsupervised sourcepreference因dataset/model而变；humanNQfinetune prohuman、humanSciFactmixed；LLMcorpus多数proLLM但AugTQGenNQ仍prohuman（16.1/5.0/3.7）。故不是densearchitecture天生偏LLM，也不是所有SFT/所有synthetic必同方向。重新attachpretrainedBERTLMhead的PRA近chance/42.2/46.1只反驳该retriever-centric masked-perplexity代理与配对relevance一致性，不证明无任何fluency因果或该head是已校准retriever概率。语义等价rewrite沿已有构造假设，不独立保证所有实体/事实不改。完整GPU型号/precision、训练multi-seed/CI、实际online成本ND。

拟Ch76窄gap：actual139–155已分source/serialization身份、readerformatattention与encoderformatadapter，但尚未载retriever训练stage/sourcecorpus本身改变pairedsource ranking preference，以及更新时必须在固定语义pair与querypopulation下验排名/召回，不能用PPL或source名代truth。只一段诊断/一段counter/fallback，非proLLM普遍law；root实际POST核Ch76正文143–170与末注1215，窄整合已通过。source CORE2 105–180；TAIL2 195–243；EXTRA2 244–264。

## [10885 RLCER](https://arxiv.org/html/2602.10885v1)

5（2+1+2），标准、必要eligibility和counter审阅。单policy不同role生成reasoning/rubric，另frozen Qwen3-4Bverifier判satisfaction；同题Nrollouts以GT finalcorrectness z与satisfaction v的corr>.2且std(v)>0筛valid，validrubric权重minmax→CoTreward+outcome，rubricator按validfraction+formatreward更新，roleadvantage分别算。采用具体非饱和/相关eligible predicate，不称criterion因果、真实思考faithfulness或无GT。z全同使corr未定义、emptyvalid/minmax无跨度数值处理未据原披露建立，不写通用零信号实现保证。

Qwen3base4/8B冷启动40k（20kmath/20krubric）DoubaoSeed1.6teacher rejects、5epoch/SFT32768/lr2e−5；verifier另distill同recipe，不是无需额外supervision/训练。DAPOMath17k/PPO、1500steps/B32/N8/mini64/12288response/16384prompt、noKL/actorlr1e−6/critic1e−5/T1/topp1，evaluation16samplesT.7 avgpass@1，3SuperGPQAsubsets各100。图中rubricOnly随机reward反侧与去evolving同baseablate支持局部信息性，但仍用GT validity选择，不能称无正确答案验证；额外role/verifier/curation导致预算不同，§6明确更多训练time，与§5“free-lunch”冲突，不采用免费保证。

Table1 4B SuperGPQASci42.88→41.81、8B Med38.31→36.50退步，AIME24 4B无增；correlation上升可能selection与同policy共适应，未独立建立可靠性或持续selfevolution。hardware/precision/训练seed/CI、verifier校准误报率、全成本ND。Only Report：actual1558–1595已承载rubric provenance、outcome-calibrated admission、共适应与成本；本文corr阈值/validfraction recipe没有新的长期知识差额，不因缺名强行写Books。必要证据与局部结果保留。source CORE3 123–184；TAIL3/EXTRA3 239–301；CONFIG3 302–339。
