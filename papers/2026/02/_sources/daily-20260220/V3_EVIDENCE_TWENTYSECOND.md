# 02/20 第二十二有限证据包：GCM / ECS / Retrieval Collapse

三条query潜力的必要精确v1正文/匹配评价/直接限制完成。官方v1事件页轻核无可见撤回/纠错，16080有Apr1v2，16113仅v1，16136只用本次v1；不借后版、不遍历版本史。复用既已root独核official announcement→same-ID DOI桥，lower2026-02-19T09:00:00+08:00，Registered+1sec uppers16080 **10:37:47**、16113 **10:38:33**、16136 **10:39:07**；不把注册等同公告精确点。

## 2602.16080v1 — Surgical Activation Steering via Generative Causal Mediation

**2+2+2=6；安全/因果localization反側深入，拟仅报告，待root核。**

实际§2 109–166、setup167–201、judge409–428、evaluation430–464。50paired/basecontrast greedy长回答，经auxiliaryjudge检查概念；patch head output以patched状态下contrast vs original sequence logratio排序，attribution为一阶近似(2forward+1backward)，knockout不读contrast；localizer与后续mean/diffmean/ReFT控制分开。该定义operational“indirecteffect”不是已核自然语言单概念唯一完整mediation，changingbomb/flower同时换语义任务，更不证明定位必要。

三10–14B instructionmodels，α1–10与12headfraction×5localizers×3steerings×3task/model；held-in用同50提议/评价，810k不是独立样本人口。selectedmethod转100prompts×3seeds/dataset，sycophancy仅10–30%transfer，refusal40–80、verse20–80。Llama70Bjudge最大concept/relevance/fluency才成功，human0.82–.95只有限校准，judge/selection仍可偏；不授相同意义或安全。headknockout劣random/probe、ReFTlocalization优势小、allheads可同样控制是关键反侧，不能称surgery必需。hypers120均值、16,200重复设置非independentinferential样本；runtime硬件/precision/并发/SLO与完整tuning费用未充分，2F1B非全链加速。

actual PLATFORM-EVALUATION-SYSTEM Ch66:2999–3020已有patchartifact仅diagnostic、matchedbaseline/replacement改变命题和原record/版本；此longsequence localizer是局部控制配方，实际未建立多概念必要性/跨域安全的新长期条件。不把既有“probe非causal”借分当此篇新原则，也不声称整个GCM已覆盖。保留长form/sparse局部观察与globalsteering反侧，拟Only，不以局部hparam效果强写新机制。

## 2602.16113v1 — Evolutionary Context Search for Automated Skill Acquisition

**2+2+2=6；静态任务context utility搜索接口缺口深入，拟Ch75窄整合，待PRE/具体锁。**

实际§3 123–249、setup256–286、transfer335–345、skill386–392、ablation515–523/cost525–547。把source/insight/skill组成unitpool，population32、elite60%、mutation.1、crossover超量random子集，Gemini3Pro refinement只检查冲突非外证；每context10devsample单rolloutfitness，多轮复用dev不能当holdouttruth或已知globaloptimum。Backend5generation/85docs，airline10generation/60insights，max10units；cost段统一10/320只是较大设置，非所有任务同预算。CuTe20operators8–12OpInfo cases、三次平均；airline9runs且Passk是allk成功非anypass；traintraj→insight来源并不是新事实。必要正文未足够披露dev/test如何完全排重与全部search/label/refinement预算，不授“少材料模型无关”。

sameunitcount random/RAG/fullcontext对照及fitness/mutation移除反退，refinement code0.461/.458近无效而airline明显，支持taskfitness不同于similarity，不证明全部算子必要或任意corpus省。Flash-evolved转Sonnet/DeepSeek两holdoutmodel局部正例，DeepSeek7×plain低基率、airline近Full非任意modelagnostic；skills75全部0.283低plain.306、筛选.310仍低rawsource.461反側。staticprefix可缓存是工程可能，实际“RAG无法缓存/省prefill/TTFT”无部署测量，dynamic也可共享prefix，不采用。hardware/precision/并发/SLO/CI与整个成本未披露，320fitness还每次10任务及refiner调用。

actual AGENT-CONTEXT Ch75:579–583有generic optimizer/acquisition/provenance/overfit边界，仍未解释**稳定任务族的离线taskfitness组合搜索→版本化静态可复用context**，区别query-specific retrieval与训练generator。拟在该标题前补一段条件分支：可核dev下从sourceunits组合，用实际task结果而非相似度选配，冻结task/model/pool/search/heldout后为后续同族调用复用；mutation/refinement不授truth，payoffline复核/调用费、额外cachedprefix仅possible。域漂移/新知识/heldout失效回原检索或fixedassembly，不把context替代参数学习普遍化。此为实际接口增量非structural。

## 2602.16136v1 — Retrieval Collapses When AI Pollutes the Web

**2+2+2=6；安全/质量测量盲区深入，拟Ch76窄整合，待PRE/具体锁。**

actual§3 72–112/Table1、§4 212–234/directlimits244–246。MSMARCO1000queries，Google每query10文→原10k（未认证全部human），GPT5nano每query20SEO由随机原文aggregate/IDF优化，Abuse独立生成再换实体/数值。每round加一文到固定10，20roundpool66.7%；独立两scenario不是证明SEO自然演化为Abuse的时序因果。BM25 vsGPT5nanoranker，同nanoanswer，GPT5minijudge原/生成facts及AA与MSMARCO reference一致，较大judge不自动independenttruth/upperbound，未充分人工校准/seedCI。

PCRpool/ECRtop10/CCR显式引用/AA分开，CCR不是隐藏“实际用证据”。SEO ECR放大但AA稳定只是受测分母盲区，synthetic比例不等实际来源多样性或人类facts消失；原10k本已有SEO/currentwebrange，paraphrase继承原事实。同一model生成/重排/回答/judgefamily相关；AbuseLLMrankerECR近0不授全攻击可靠，BM25AA68→66局部；防御perplexity/provenancegraph/agentfingerprinting只建议未实测，不写已实现gate。真实大规模web、adaptiveattack、ranking费用/hardware/tokenlen/precision/concurrency/SLO NotDisclosed。

actual AGENT-RAG Ch76:162–164有配对human/rewrites与train/ranking来源偏置，818–821有counterfactualsupport/answertruth，仍未给**pool composition→retrieved exposure→explicit citation→answeraccuracy**四测量人口分账。拟source-ranking段后补窄接口：质量稳定不能认证来源结构稳定，固定query/pool/注入/原sourceidentity，分别报告poolshare/topkshare/citation与final质量；origin非truth，citation非hiddenuse，simresults非必两阶段生态定律。额外生成/来源标注/审计rerank费用、生产漂移未验，稳定可信小语料继续ordinaryretrieval+人工审计，不以合成标签全部屏蔽或承诺安全。

## 批次状态

尚待root必要source/actual owner处置独核。两拟写只在具体Ch75/76锁后，16080不写。普通队列不改成外部hold以结束；本日仍非完成，无stage/commit/push。

**后续独核结果：** root 必要源/actual owner PRE通过，16080 Only6终态保局部localizer不写必要性；16113/16136 各6分差额深入，实际 Ch75:579/570–593邻接/末注749 与 Ch76:166/156–177邻接/末注1531 已 root POST通过，锁释放。四人口明确是评价接口非新理论、防御未实测。README同步84=50POST+12争议+5Existing+17Only，普通12；无日级冻结或验收。
