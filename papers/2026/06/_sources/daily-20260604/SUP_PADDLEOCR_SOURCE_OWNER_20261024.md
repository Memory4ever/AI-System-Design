# PaddleOCR-VL-1.6 03264 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author；R45完整exact-v1题摘/Jun03联合日证/notice已独核通过复用，不第三准入/date。正式2+1+2=5：重要局部的数据干预分支与可复用边界，SystemReach仅数据/监督组件，不按串起CPT-SFT-RL联想升分。为actual长期差额深入受影响内容，不以工作量倒推评分。

[exact-v1 HTML](https://arxiv.org/html/2606.03264v1) HTMLfirst；完整剥标/保mathannotation TEXT80526字元保存[原件](2606.03264v1.fulltext.txt)，无工具truncation。实际必要读§2/3.1–3.5完整机制与Alg1–2、§4.1–4.3.1/4.3.2式5及解释/4.3.3、§5.3/T8。未读全部下游taskcell/各任务reward表格细则、图像像素/代码/数据或训练复现；采用命题不依赖这些细则，支持与直接关键反侧足即停。

## 必要机制与关键反侧

§2继承1.5架构，layout模型PP-DocLayoutV3不变，0.9B中LLM0.3B；不能由参数不变证明实机速度或全部能力保持。新增为model-oriented dataengine及后训，不以OCR应用榜分准入。

§3.2 late8%八checkpoint×16视觉扰动产生128prediction/sample，全trainingpool；8128成对normalizededitdistance取最大128均值作fragility，top1%及任一degeneration入选。这里“region”是模型/数据邻域，不只是图像bbox。声明semantic-invariant的blur/noise/缩放等仍可能改变小字可辨性，输出edit/格式变化不证明真实语义边界或因果不稳定；empirical1%不是普适阈值，成本包含128次全池预测及pair比较。

§3.3内部documentencoder提normalizedfeatures/cosinesimgraph，逐步升threshold分连通分量，选小outliercomponent；encoder/cluster/threshold代理不证明每个低密度即真实语义长尾或更值得训练。未充分披露encoder、阈值/预算/终止资格，不采Alg1为所有pool必终止的可执行recipe。fragile/sparse两者只作internalpool新增样本retrievalseeds，不同于修原标签。

§3.4旧labelqualification专家是QianfanOCR/GLMOCR/MinerU2.5Pro：只要任一expert同原label即retain；全不同原label但至少2expert互同则替换；全不达共识转unresolved。一个支持也可保留错标签，共同偏差不因“独立模型”消失，agreement精确等价/规范化规则未完整给，不补确定性gold判定。持续高confidence错误可能label问题，但不排模型系统偏差/标注歧义，不拿模型错误单独认证label有错。

§3.5新unlabeled/待修复的annotation专家集合换为**PaddleOCRVL1.5/GLMOCR/MinerU2.5Pro**，不同于§3.4，不能合成同一专家协议。至少2同则直接accept，否则ERNIE5初次看三expert生成候选；后续只看当前prediction+上次judge discrepancies，不再次注入expert。候选LaTeX/HTML render成图，由同ERNIE Mjudge对原图/渲染图给δ，空δ即accept，否则Mrefine改，T轮未过转人工请求并附prelabel。render把跨模态比对变同模态比对，但同模型proposal/judge、renderer丢信息和视觉近似均可漏语义错误；空δ不是真值、有限人工请求非全部人核，也不保证迭代必修好。保原图/label/生成与判定/渲染/人工lineage。

§4数据分配：CPT旧SFT+部分pretrain+新增全池16.8M/allparams/1epoch/global1024/maxLR3e-5；SFT包含UACS难例、需renderrefine难例和旧标签已修样本，共7.3M/allparams/1epoch/global1024/maxLR1e-5；串行配方不隔离诊断/labelrepair/数据量单项作用。§4.3.1用SFTpolicy每题16rollouts/T.85/topP.9/topK32，筛maxreward低、mean高、max−mean低、variance低；Score=(max−mean)exp(U+2Vr)，U是1−平均lengthnormalized采样confidence，非校准不确定性或真实可学性/熵定理。每task分开top8K、总49K为原文口径，不补精确六任务总数配方；§4.3.3全参2epochs/LR2e-6/G16/cliphigh.28，动态忽略rewardzeroVariance组。finite采样没成功不等不可学；这里是SFT阶段probe，不认证一直online刷新selector。

§4.3.2式5Validity×Structure×ReferenceSimilarity，format/parseability或canonicalreference匹配与真实图文正确分责；未审各rewardcell不补完整RLrecipe。本PRE不采用该RL选择公式为唯一新机制，也不复制Ch33GRPO原理。

§5.3/T8仅顺序累加stage：94.93→95.62→96.25→96.33，不能从increment断言UOR优于等量uniform/某diagnostic唯一因果/总成本更省，缺UOR组件或equalpreparationbudgetfactorial。TEDS-S在SFT行97.09、邻文97.19不齐，不采该精确值；RLoverall+.08不是单seed显著性保证。未披露trainingseeds/CI、GPU拓扑/precision、完整token/teacher/refinement/采样/时间预算、推理batch/concurrency/SLO，均Not Disclosed。不采用SOTA/参数更小即效率/保原架构即无损结论。

全池多checkpoint/perturbprobe、feature/graph/retrieval、双专家集合、render/ERNIEjudge反复生成及人工、CPT-SFT-RL与独立回归均付费。代理/专家/渲染或实际任务支持失配时保可信原标签、隔离/人工、代表性数据与独立heldout，不由一致性批准自动真值。

## actualowner与最小差额

唯一TRAIN-DATA Ch27。三Bookscontext与ROADMAP职责已加载，本轮actual读Ch27开篇、质量/干预相关330–360及370–418完整局部、1317–1345online selection相关和26/28开篇交接；本family/PaddleOCR/UACS在Ch27检索未见旧owner。此前Ch27已讲字段Error/Missing修复与judge循环，在线policyselector也已有，不能重复这些原则当新差额。尚未承载**将checkpoint/扰动不稳、表征稀疏用于检索扩数据，与旧标签external-support不足用于纠正分开路由**，以及LaTeX/HTML渲染闭环在空δ/轮次/人工fallback中的具体监督资格；只补此分支，不接管VLM表示/GRPO机制。拟2602-13013完整段后/2603-20004完整段前原两段+本人trueH2注，无新授/未写。

完整上锚：

多源 audiovisual captions 的纠正还有一条更细的字段边界：先保留各来源互补覆盖，另存 speaker-aware ASR 与 timestamp anchors，再把合并 caption 拆成 attributes，分别标出 Error 与 Missing，只修受影响字段、保留已核内容。它不同于一个全局 alignment 分数，也不同于每次重新生成整条 caption；format 检查与事实检查仍分开，同一模型同时合并和审校则必须显式保留 judge 循环的风险。[受限数据对照](https://arxiv.org/html/2602.13013v1)显示增加覆盖会伴随 hallucination 上升，局部修复降低漏述不等于所有阶段的 hallucination 单调下降；长 context/stage 变化也不能归因于 attribute editing 一项。原始 caption、ASR/time、字段 verdict 与 rewrite lineage 都需保留，并用独立审计与下游切片验收；锚点冲突、共源错误或修复费用不合算时，回退可信单来源、人工核验或隔离样本，不把“verified”当整池真值。<!-- source-family:SF-2026-ARXIV-2602-13013 -->

拟增两段：

持续错误不应一律转成“再收集更多难例”。可以先把诊断分为不同干预入口：跨邻近 checkpoint 或轻扰动仍不稳定的样本，以及表征空间中稀疏的小邻域，作为检索新增数据的种子；原标签缺少外部支持的样本，则先进入监督修正，而不是继续复制同一错误目标。一条[受限文档数据分支](https://arxiv.org/html/2606.03264v1#S3)据此分开扩分布与修标签。输出差异和特征密度都只是 proposal：扰动可能改变可辨内容，低密度不等于重要长尾，单个专家支持或多模型共识也不能给原标签或替换标签签发真值。

当表格或公式的候选是 HTML、LaTeX 时，还可先渲染成图，再让 judge 比较原图与渲染结果、将具体差异交回修订；有限轮次仍未通过就转人工，并保留最后候选作预标注。这改变了监督检查的接口，不使渲染相似或“未发现差异”成为语义正确证书，同一模型生成和审校仍可能共同漏错。应保存原图/标签、检索与专家来源、每轮候选、renderer、差异和最终准入，分别验新增覆盖、标签质量及下游行为。多 checkpoint/扰动探测、特征检索、专家与 render-refine、人工和后续训练全计费；顺序增加 CPT、SFT、RL 的局部收益不能单独归因于诊断器。资格或净质量不稳时，保留可信原监督、隔离/人工复核与代表性数据回退，不由更高平均解析分数批准全池自动修正。<!-- source-family:SF-2026-ARXIV-2606-03264 -->

完整下锚：

可执行reward的数据修正还要包括“哪些输出应算正确”与“由哪版验证集选择checkpoint”，不只是换一份gold答案。一个query任务可允许任意满足条件的子集、限定结果数量或要求固定排序，若仍用统一set-equality会把合法答案误罚；question、外部条件、schema、gold和grader规则应共同版本化。训练reward上涨也可能与独立已修正heldout表现反向，修training而不核validation仍会选错更新阶段。[受限RLVR数据对照](https://arxiv.org/html/2603.20004v1)同时改变样本人口/题意和训练时长，不证明清洗单一因果或humanparity；模型reviewer、expert blind复核与冲突投票亦不自动全truth。重审、数据库执行、训练和checkpoint回归均计费；语义规则不明、原任务支持被改掉或验证偏置未解时，保raw/corrected lineage、独立审校与原可靠训练/验证manifest，不以verified标签签发部署能力。<!-- source-family:SF-2026-ARXIV-2603-20004 -->

本人trueH2注拟：

- `SF-2026-ARXIV-2606-03264`：Daily2026-06-04补Jun03；exact-v1 §2–3.5/Alg1–2、§4.1–4.3.1/式5概述/4.3.3、§5.3/T8必要，2+1+2=5具体data干预分流差额深入。保8×16代理/专家集合与共识非truth、renderjudge循环/人工fallback、阶段累加非单因果/T8单格口径不采与全费；不授自动全池修正、SOTA/净效率或GRPO普适选择，未核全taskcell/图像/数据代码或复现。待首次PRE/新授/唯一实际POST。

