# 必要证据与具体owner差额：10079 / 09853

原源均exact-v1 HTML，未复现。root独立必要原源→owner待核，尚未写Books。

## Sparse-RL — 2601.10079v1

[原文](https://arxiv.org/html/2601.10079v1)，`2601.10079v1-primary.txt`实际§3/4.1–4.3(90–152)、5setup414–434、5.2/5.3及5.5/Limitations434–515、AppendixE714–745。拟3+2+3=8，只采新增稀疏sampler mismatch分解/拒收接口，非成熟importance/clipping再计贡献。

同θold不同KVview即不同sampler；ρ=πlearner/πdenseold，ξ=πdenseold/πsparsesampler逐token同prefix概率比。任何ξ<1e-4令全response梯度为零，ξ放在clipρ外。ξ低是相对概率不一致，**不是数学support为零、逻辑错误、hallucination或reward真值**。AppendixE只证明同prefix ratio乘法相消和所定义surrogate求导；没有恢复sparse采来的prefix distribution，response拒收又改变人口，clipping/groupadvantage仍在，故不采“完整dense RL无偏/只保留逻辑valid”。可保留受测稳定化和各比值/阈值/view/policy identity分责。

Setup：slime、SimpleRL-Zoo hard~8k GSM8K/MATH、400steps~1.5epoch、binaryverifier、G8、temperature1/top-p1/maxresponse4096、global1024/update256、LR1e-6/KL1e-4/KV512、4H20HGX141GB。四个模型Llama3.2-1B-Instruct/Qwen2.5-1.5/3/7B，两compressorR-KV/SnapKV。七benchmark中AIME24/AMC23Avg32，其他作者误称“six”但实际五个Pass1，不能混成同采样预算。MainQwen3B42.8vsdense43.4、7B51.4vs53.1，不是完全无损；35.1–53.3%“Toks saving”是KVretained token代理，不是含dense scoring/拒收/训练state的GPUmemory或总吞吐。512budget局部有效、128退化；rejectavg0.07与clipavg0.0005仅Qwen3B动态，不授通用稳定阈值。未给reject/reweight分别消融，也无独立重复/CI或完整端到端时间曲线，不能独立归因全部收益两component。有限math/verifiablebinary不外推open-endedreward。代价包括denseoldteacher-forcing/scoring、拒收浪费、ratiovariance、压缩mapping与view记录；不稳回退dense/freshrollout。

日期原SubmittedJan15T05:12:03Z(v1)、UpdatedJan16T01:21:31Z(v1)、created02:46:40Z/registered02:46:41Z；正常cohort公告+registered秒精度上界条件BJT[Jan16 09:00,10:46:42)。v2不采；无已发现先行正文，后续反证定点重开。

Owner `TRAIN-GRPO` Ch33。实际body705–719已有compressed-observation view与decision probability分账，但它是学习省略决策，不是KV稀疏rollout；2143–2157已有stale-policy与numericaldrift/prompt-leveladmission，**缺同权重sparse sampler/denseold/learner三分布及response min-ratio gate/token外clip权重**。拟AsynchronousRL节，在2157后两短段，接机制总结，ratio条件与理论不采用旁置。首段18符号与PPO/DPO交接已核，待root授Ch33窄锁。

## MedRedFlag — 2601.09853v1

[原文](https://arxiv.org/html/2601.09853v1)，`2601.09853v1-primary.txt`实际§3.1–3.4/4.1–4.4/5.1–5.2/6及Limitations/Ethics103–278。拟2+2+2=6，具体安全evaluationblindspot深入，不采取临床建议或一般患者真值。

MedRedQA51k2013–2022公开RedditQA→33,090contextfilter→GPT5stagedquestion/implicitansweredquestion/misconception提取→1103redirection，original top-votedphysician非全gold。300flagged审7false，60notflagged1missing是分层条件错误率，不是populationFPR/FNR证明；同作者医师造rule/审，医学判断可错、用户自主/合法前提误拒保留。

100testquestions，GPT5Aug7/Opus4.5Nov1/Llama3.3-70B/MedGemma27b，supportedtemperature0；分别判“explicitly addresses any misconception”与“仍给criterion请求信息”。GPT5baseline88%address却73%accommodate；oracleassumptions nearlyalladdress仍Opus33%accommodate。这里oracle从clinician原答而来、不是线上输入，也不认证premise detection perfect truth，只隔离identify与responsebehavior。JudgeGPT5，110address/55accommodatelabel与twoauthorphysicians93%concordance是小样本一致，不能外推全域truth/causality。RAGtop5MedRAG与先identify方法减少部分accommodate但不充分，RAGaddress可退；不宣称新的可用安全RLobjective。Potentialtrainingmemorization/publiccorpus、preprocessingcontextmissing、only100/qual10/noactualclinicaloutcome/部署hardware并发SLO NotDisclosed。核心长期delta是不得让免责声明/识错掩盖仍提供错误前提要求的actionable信息，必须分别标注检测和回答承接。

日期SubmittedJan14T20:23:02Z(v1)，UpdatedJan16T01:04:55Z(v1)，created02:41:01Z/registered02:41:02Z；正常公告+register条件BJT[Jan16 09:00,10:41:03)，不采v2/v3。

Owner `PLATFORM-EVALUATION-SYSTEM` Ch66。实际974–996reliabilityprofile、4011clean-twinreview、4141failuredecomposition已有多维/误拒，但**不承载premise addressed与requestedinformationaccommodated同时为真、oracle知前提仍不redirect的特定interface**。拟974privacyfairness之前两短段，测量方向/authorjudge/医师不是全真值/误拒反侧在机制旁；不写成医疗应用节。Ch66首尾与Ch65/67交接前批已核、未变化复用；需窄锁，顺便把PVNI末note待验改rootPOST通过（原正文不重审）。
