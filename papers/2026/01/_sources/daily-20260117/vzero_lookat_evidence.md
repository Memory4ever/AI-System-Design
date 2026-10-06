# V-Zero 与 LOOKAT：必要证据及待 root 处置

不把已缓存正文当全附件已读。两项 root 已实际完整 AB 准入；以下必要原段已作者实际读，未核代码或复现。

## V-Zero — 2601.10094v1

exact [HTML](https://arxiv.org/html/2601.10094v1)；缓存 `2601.10094v1-primary.txt`。actual §3 L104–160、§4.1–4.4 L239–308、§6 L311–314、A.1–A.3 L526–538（前段 Table1 数字亦已读）。正常 Submitted Jan15T05:47:43Z，Updated Jan16T01:22:37Z 不当 public；created 02:47:02Z、registered 02:47:03Z 原秒精度。正常公告及无已知先行全文条件下 BJT Jan16 [09:00:00,10:47:04) 完全落窗。

2+2+2=6；具体自生成课程/伪标签与 verifier 差额深入。两同起点 VLM policy：Questioner 同次生成 image MCQ+direct answer；冻结 Solver 10 次 CoT 投票给 modal answer/confidence c。相同 direct/modal 时 min(c,1−c)，不同时 0.5c；格式门只验四选项与 tags。Solver 只收 confidence 0.3–0.8，并奖励新 rollout 匹配自身 modal pseudo-label。这不是独立 RLVR 真值；一致错答案/同源 hallucination 仍可高 c，故“reward naturally prevents hacking”“divergence corrects intuition”不采用。问题与答案同生成也不是 matched 同模型同问题控制，不能认定偏差仅来自 reasoning。

§4 Table2 freezingQuestioner、single uncertainty、去confidencefilter各有局部对照；7B 两迭代平均49.9→51.9，3B第一轮43.2→43.9后43.8是直接反侧；不归因普遍容量law或无限单调改善。7B对supervisedGRPO humanlabels+twoepochs未匹配总compute，同source训练图像不等预算一致；Qwen3VL32B题目难度judge、Qwen3VL8B answer extraction 不认证标签。本文A.1从约9K选4K纯image，主文约9K是来源库而非确定训练量。训练4×A80080GB另2GPU托管feedbacksolver，B64、LR1e−6、T1、Questioner G4/Solver G5、m10、KL.01、输出2048/4096、FSDPoffload，约9h/iteration作者数据；precision/seed数/完整eval runtime未披露，不采总成本优势。

实际owner `TRAIN-GRPO` Ch33 L1496–1504 已承载 coevolving curriculum/proposal≠solver≠verifier与targetguide反侧，却没有 direct-vs-majority reward 两支及无externaltruth时confidencegate的明确责任。Ch32尾/Ch34首及Ch33首实际读过。拟原一般自博弈分责之后、targetguide之前两段：新增双track提案与filteredpseudo-label更新接口；相邻同源错误、MCQ/format不认证、3B退步及rollout/judge/9h成本，保留fixedverified题库和外部verifier退路。请 root 必要源/owner 独立核后决定是否授窄锁。

## LOOKAT — 2601.10155v1

exact [HTML](https://arxiv.org/html/2601.10155v1)；缓存 `2601.10155v1-primary.txt`。actual §3 L111–190/Alg1、§3.6 L192–200、§4.1–4.2 L201–240、§4.3–5.2 L291–411。Submitted Jan15T07:54:07Z、Updated Jan16T01:27:37Z，created 02:48:31Z、registered 02:48:32Z；同上述正常cohort条件 BJT Jan16 [09:00:00,10:48:33) 完全落窗。

2+2+2=6；key-only PQ score consumer 与高精度 V 具体接口gap深入，但中心质量/性能headline未成立。calibration K-means将 d head拆m子空间/256centroid，cache每key持m uint8 indices，query计算各子空间q·centroid表，再sum indexed score、softmax、FP16 V aggregate。这确实不必逐key显式重建向量，但表构造要256d乘加/每query（原文效率行 m256 省掉d/m），LUT/state/codebook bytes、encoding及FP16 V仍需预算。原文“scalar dequant读取same DRAM所以zero speedup”不能采用：压缩字节与register重构不是相同DRAM流量；本文未测真实kernel/edge端到端。

排序保持≠softmax等值。即使所有score次序相同，score间距变化可改变attention/output；§3.6未给scoremargin/query/data分布假设或完整proof，从PQ MSE跳rank bigO，最后声称实验导出，不能授rankbound或质量certificate。Alg1的近似内积只是对量化后key的精确消费，未认证原key。GPT2第一层12head/d64，三种textsample128–512，3sample误差棒不是多seed模型能力；Table3 L64→1024 KL1.039→8.291/cos.999→.903直接退化；同budget Table4 INT8/INT4cos1/.987高于PQ .947/.953，故并非全Pareto。cosine .957不是95.7%任务质量，keys64x不是totalKV64x（valuesFP16）；Table2codebook字节与256×64×FP16应有开销口径缺口，不采用表中精确总存储。hardware/precision除FP16存储外/完整任务/PPL/decode/arrival/SLO未披露。

实际owner `INFER-KV-CACHE` Ch45 L660–666有量化→losslesscodec再解码及K/V消费差别，L1514对key centroid选择+低ranklogit补偿，但没有PQ码本q-LUT直接消费keys。Ch49 L943–945有weight/activation LUT，不代替KVkey consumer；不双owner复制。已实际Ch45首/44尾/46首与上述owner正文。拟 L662之后、mixedblock之前两段，只采用码本indices→querytable→softmax/highprecisionV接口与成立条件，明确保序非权重保证、V/codebook/calibration/表构造成本、有限firstlayerproxy与更长退化，保原量化/fullKV。不把作者缺proof补成新理论；若 root 判中心争议阻断长期采用则安全NoBooks，不伪装完整质量或速度。请 root 定点裁决。
