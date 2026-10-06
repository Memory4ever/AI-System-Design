# Batch7 — 必要证据与处置（root九项实际复核通过）

当前终态：八项仅报告、Depth Delusion整项争议/暂缓，均已root实际原源复核通过；下面原“尚待/提议”保留提交过程，不是当前状态。21494仅保留局部经验预算/质量，formal accuracy/cost未采用；20994中心parameter identity冲突整项隔离，不用小规模观察替换中心准入。无新增Books差额，不授日级完成。

精确版本均为2601.*v1；日期沿用本日DATES逐项批次/上下界，非submitted=公开。原完整题摘AB_BATCH7与必要原文保持分工；本批作者已读所列方法、直接对照及反侧，非全附件/运行复现。各项评分2+1+2=5（不计成熟组合、宣传规模或访问状态）。root独立证据复核尚待。

## 2601.21343 — Self-Improving Pretraining

[原文](https://arxiv.org/html/2601.21343v1) §3–6/Table6；[核心](CORE_STANDARD_21343v1.txt)，[讨论](CORE_SUPP_21343v1.txt)。自然prefix后选原suffix/rewrite/本policy rollout，固定post-trained judge给偏好，onlineDPO/RFNLL更新；早期rollout弱、后期被选率升，不能当judge与rewrite成本免费。继续训练Llama2标称1.4B（具体checkpoint lineage未披露）、64GPU型号ND，batch256/16rollouts/2000steps/max2048/LR5e-6；scratch21ksteps/1rollout并非同预算。judge8BGRPO和70B生成/过滤另计。gptoss120B也用于训练质量标签和评价，8个judge sampling seeds非8次policy训练。Table6 unjudged-rollout SFT安全99.5却quality2/.2、标准任务29.5，是safe collapse反例；高quality组合并非所有安全指标更高，pivot节约成本又损quality。scratch32.4相对anchor分低于50，非达到base质量。§6明确慢于NTP，未建立数据墙突破或training efficiency。仅报告：TRAIN-PRETRAINING保留局部训练目标/评价authority与cost counter；不把该judge闭环配方化为通用自改进保证或冒称精确算法已有覆盖。

## 2601.21725 — Procedural Pretraining

[原文](https://arxiv.org/html/2601.21725v1) §3–6/讨论/E1/E3；[核心](CORE_STANDARD_21725v1.txt)，[参数](CORE_SUPP_params_21725v1.txt)，[限制](CORE_SUPP_21725v1.txt)。先抽象程序任务再语义训练，pair任务只算output loss，语义阶段重新初始化embedding并全参数训练。结构打乱保留token频率仍破坏收益，layer-weight shuffle、attention entropy regularizer不足复现；attention/MLP迁移随任务分化，非所有程序通用。额外T1 tokens带来后续token equivalence，非total iso-compute。Wikitext/Java/CodeParrot局部收益、Sort跨domain不总有效；组件拼装需两份预训练成本，proof-of-concept4任务非任意merging。小任务10seeds、multiplication3seeds不授所有语义训练重复；E1 fixed LR/procedural bs64与E3 C4 bs32 seq2048/CodeParrot bs48 seq1024/Math exactaccuracy不同协议。硬件/precision及语义重复ND，未采用未核更大scale附录数字。仅报告：TRAIN-PRETRAINING；局部结构/组件可迁移是实际受控增量，具体程序配比与受限architecture未建立跨任务长期最优recipe，不为名称造Books差额。

## 2601.21698 — Curriculum Training

[原文](https://arxiv.org/html/2601.21698v1) 方法/Table1/规模及HMM分析/A1；[核心](CORE_STANDARD_21698v1.txt)，[KL定义](CORE_SUPP_21698v1.txt)。固定ThePile样本只重排AoA/frequency/VV，20/60/300Btokens、Pythia14M–410M；1B只Random/VV。linguistic proxy非理想loss难度，强凸/光滑/无偏有界方差且hard subset高方差近最优的假设不构成LLM普遍定理。小模型有益，410M课程47.5–47.9<随机51，1B50.1<50.5，具体BLiMP能力亦反退。多数single seed1234，3seeds仅14/31M；共享拟合5-state HMM不独立证明phase causal identity。所谓singular entropy定义实际KL(p||uniform)=logr−Shannon entropy，高值是集中而非Shannon entropy升高。A100 GPUhours披露部分规模，precision/batch数值未在必要正文披露。仅报告：TRAIN-DATA；保留尺度依赖和probe边界，future phase-adaptive curriculum尚未实现，不当新训练政策或全规模规则。

## 2601.21695 — AtPatch

[原文](https://arxiv.org/html/2601.21695v1) §3–5/Table2/4/ablation/overhead；[核心](CORE_STANDARD_21695v1.txt)。安全变更影响内容加深实际读：debugpair由逆trigger搜索/保护属性翻转和nearest Hamming clean构造，column标签仍代理而非真实因果。mean-head attention→CNNMLP detector、50epochs/AdamW1e-4/threshold.1校准；victim权重不变不等于零训练，benign均值替换flagged column并row-rescale绑定ref/model/inputshape。Eq8正指数比率最小化未写−log与Eq11epsilon导致严格normalization条件不清，不采其数学保障。六小型ViT/表格模型加BERTIMDB是受测范围，非foundation generative保证。Table2部分ASR别方法更低/clean accuracy下降；Table4平衡map FPR .02–.099要考虑base rate。额外.8ms flag/.1ms clean对base.5ms即160%/20%，不是零开销。硬件型号/precision/batch/seedsND于必要段；同debug/eval/hardware声称非复现。MNIST→Fashion只是local OOD；adaptive attack仍future。仅报告：PLATFORM-SECURITY；保留受限runtime intervention与可靠性缺口，不导入一般backdoor防护承诺，不称已有AtPatch算法正文。

## 2601.21204 — Embedding Scaling versus MoE

[原文](https://arxiv.org/html/2601.21204v1) §3–6；[核心](CORE_STANDARD_21204v1.txt)，[相邻设计](CORE_SUPP_21204_5_3_Empirical_Comparisonv1.txt)、[模型](CORE_SUPP_21204_6_1_Model_Informationv1.txt)、[执行](CORE_SUPP_21204_6_4_Fast_Inference_with_Optimized_Kernelsv1.txt)。既有n-gram hash+projection非准入，增量是same-parameter MoE-vs-embedding/sparsity边界及受测hash碰撞反例。activated280M/790M/1.3B、300Btokens，expert ratio过大才出现local差异，阈值不通用；width/depth也不总同activated预算。多项式hash在近整数vocab倍数即使prime仍碰撞峰，证据只100seq/受测vocab范围，不推广任意hash。N≥3/K≥2及norm/init反侧是local recipe；fast draft linear/earlyreject仍探索非实现。LongCat68.5B/2.9–4.5Bactive/31.4BnGram/11T+1.5T+SFT，vanilla不同activated cost非isocompute。8H80080/ISL4K/OSL1K/batch-variable与Eagle3+EP+SBO+fusion+PDL联合路径，不独立归因embedding；50%指kernel而非完整服务，precision variant format、concurrency/SLO/seedsND。仅报告提议：MODEL-EMBEDDING；受测hash与容量/执行分账有具体增量，但单hash算式/局部sweetspot未建立通用新接口，不以规模或名称造gap。root可复核此长期处置，不冒称具体算法已有覆盖。

## 2601.20994 — Depth Delusion

[原文](https://arxiv.org/html/2601.20994v1) §3–5/Table3/§4.6/4.8；[核心](CORE_STANDARD_20994v1.txt)。PDF exact-v1 p1/5/6/7实际恢复（22页，p1水印v1）：原PDF题名Depth Delusion，HTML题名Extended Theory dissertation差异不改ID。拟合loss ansatz的Dcrit W^.44与2.43logW仅局部近似，不是统一理论；capacity exponentCI[-.21,.65]，D*.12/W*.34不授普遍optimal scaling。固定LR3e-4/WD.1/clip1/preLN/RoPE/GELU/seq1024/bs256/single seed42；1000step gradient非训练causal证明，SE来自末10%tokens非独立runCI，训练token CE非自动heldout。**中心争议**：同7B损失2.417/2.298，§4.6写64L7.08B>32L6.92B而§4.8写64L6.38B<32L6.86B，PDFp6两处仍同时存在；5.30e21 vs5.89e21亦非同FLOPs。保留小规模非单调结果，但中心人口/parameter identity和architecture归因不能由窄化标签消除。争议/暂缓提议：WORLDVIEW-SCALING-LAW，不采用中心0.12结构归因、最优幂律或production规模保证，不进Books。需作者统一checkpoint/参数/FLOPs/训练-eval split及matched train identity后只重开该命题，非访问受阻、不降分EX。

## 2601.21590 — Scalable Power Sampling

[原文](https://arxiv.org/html/2601.21590v1) §3–6/C1；[核心](CORE_STANDARD_21590v1.txt)，[实现评价配置](CORE_SUPP_21590v1.txt)。轨迹p^α的nexttoken需future partition ζ而非local temperature；MC ζ unbiased≠ratio unbiased，jackknife只在条件下消leading O(1/M) bias。实际TopK8/M8/192block horizon/max3072/α4，finite candidate/horizon已不等exact global distribution；likelihood非correctness。PLAN/GUESS toy有受控差异，真实7B四family/MATH500/HE164/GPQA198；QwenMath和DeepMath多项低于GRPO，不普遍取代RL，α过高也退。C1singleGPU型号ND/vLLM.6.3/seed0，batchND；2.5–3.5×慢于standard generation，up10×相对特定MCMC非通用E2E加速。output均长~700非length distributionmatched，额外inference与RL训练预算不能自动同成本。仅报告：MODEL-SAMPLING；保留局部global-vs-local取舍与approximation/cost，无精确target或训练替代承诺。

## 2601.21522 — Restart and Discard

[原文](https://arxiv.org/html/2601.21522v1) 方法/HE评估/limits；[核心](CORE_STANDARD_21522v1.txt)，[限制](CORE_SUPP_21522v1.txt)。coverage@attempt/cost而非单attempt成功率；IID fixed p、perfect verifier、无switch/unitattemptcost条件下无限fresh pool τ1最小mean，有限池将随机剩余时间换mean是approximation。已解discard、未解后验难度转移非生产fair scheduling。HE164每题100sample矩阵后100reshuffle realizations，不是100模型训练或独立APIreplicate；Groq三LLM/temp.8/同prompt、USD为作者历史价不是当前价，verification成本/时间未计，hardware/precision/concurrency/SLO ND。高coverage大模型仍解small不能解题，相关attempts/falsepositive verifier在limits而非已解决。仅报告：PLATFORM-COST；受限coverage allocation区别明确，不采Outcome-as-Service/refund或成本普适最优，具体政策不改平台通用cost ownership。

## 2601.21494 — Prefix Consensus

[原文](https://arxiv.org/html/2601.21494v1) §3–5/Table2/4/A；[核心](CORE_STANDARD_21494v1.txt)，[参数](CORE_SUPP_21494v1.txt)。短prefix TFIDF/Agglomerative dominant cluster→Kcontinuations→majority，以分支早期可区分压预算。MI>0不证明dominant=correct，不能采accuracy保证；成本式Nlp+K(lf−lp)、K=κN实际κ越大省越少，与文字/命题sketch反向，formal保证未采用。QWQ AIME25 N51−10pp、DSQ24−6.7pp、GPQA局部反退，不声称accuracy无损；10次sampling非trainingseeds。TFIDF5–11ms vsdense220ms只cluster overhead，非完整prefill/cache/continuationcost验证。AppA4L40S48G/temp.6/top-p.9/max32K，precision/batch/concurrency/KV复用/TP ND；main全dominant vsApp预算子集要具体state binding。仅报告提议：AGENT-PLANNING；采用局部经验预算/质量反侧，数学accuracy/cost保证子命题明确未采用，若root判中心保障不能分开则终态争议而不删证据。具体cluster recipe不变成新长期规划保证。
