# 第七包：Ch66两个具体差额、八项实际已有覆盖

仅整体PRE/具体NC提案，尚未SAVE。Books上下文/ROADMAP/Ch65质量与资源公平分界及Ch67监控交接有效层复用，writer本轮实际读取下述完整目标段与直接邻接。必要首读/独核归属照EVIDENCE_WRITER和reader canonical，不写成全为本人第一Methods；均未核代码/复现。仅单一PLATFORM-EVALUATION-SYSTEM Ch66，不锁全章；NC不写marker/注。

## 12587 FUT / 2+2+2=6 / 完整差额提案

actual §2–4/A1.2必要、R54 key独核已成。当前Ch66“从语义等价到蕴含与互斥根”完整两段拆样本兼容与truth，上邻MDN亦只预测teacher语义分布；它们没有把**已估不矛盾率编成措辞训练标签、表达保持与事实保持**分别验收。唯一插位在完整`NLI/parser、采样模型...逻辑图之后仍需外部 evidence、claim verifier 与 policy threshold。`之后、原`### Calibration Slice 必须包含 Language × Model Scale × Estimator Contract`之前。下方完整温度重采样两段也已读，不改其原source-family。

正文：

样本一致性也可以被编译成回答的措辞，而不只输出额外confidence分数：先按同一模型的重复采样估计每个assertion的不矛盾率，将其映射为语言hedge，再以改写或后缀制备监督数据。[受限表达微调](https://arxiv.org/html/2510.12587v1#S3)因此学习的是“怎样表达当前belief”，不是“怎样把belief变真”；原模型一致地答错时，措辞对齐仍可伴事实错误。构造时语义保持的映射，不让有限SFT自动保持全部答案分布，模型/NLI、采样与hedge词表、重写器、checkpoint和评价人口须共同绑定，分别检查表达一致、内容分布变化及外部QA正确性。有限采样的自比TVD只提供噪声参照，不能当全分布不变证书；QA仍可能退步。多次采样、NLI/改写、标签制备、微调与独立事实和语言校准全部付费，不能由部署少一次显式估计忽略准备成本。语义、语言映射或原能力失配时，保留原答案与独立后置不确定性/证据核验，不由更自然的犹豫或坚定措辞批准知识正确、风险校准和发布。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12587 -->`

本人末注：

- `SF-2025-ARXIV-2510-12587` — Herschel，Daily2025-10-16补Oct15；exact-v1 §2–4/A1.2必要，2+2+2=6，belief-consistency→hedge标签→有限SFT与truth保持差额深入。R54采用关键独核；保10采样/单assertion简化、有限judge校准、TVD采样参照及三QA反退/全费，不采全分布无损或正确概率。未核代码/复现；完整PRE/真实SAVE/完整自读/solePOST只本日canonical后到真实层。

## 12697 Judge Debate / 2+2+2=6 / 完整差额提案

actual §4.1/5/6/B2/B4/C必要；旧本日RAW_COUNTER_F决定层复用。这里不采精确理论/无标签在线停止recipe，新增命题仅**跨题有标签正确人数分布的稳定、逐请求可观察状态与停止预算不能互授资格**。当前Ch66 SF2605-29800完整段已保存逐item/judge正确矩阵与共错，后Genii段是群体偏好更新参数，没有承担拟合分布监控的停止权限。

唯一插位在完整`均衡成员偏移也不能使同一题上的错误独立...不由更多成员或低agreement自行授予可靠性。`（SF2605-29800同段marker完整保留）后、完整`群体一致性还可以被写回judge参数...Genii...`前；上方CyclicJudge两完整段与下方Genii完整段/独立marker已实际读，不打断任何源论证。

正文：

对多轮judge，还须声明停止信号来自一题的意见变化，还是一批有标签题目的正确人数分布。一条[受限辩论分支](https://arxiv.org/html/2510.12697v1#S5)在各轮拟合两个Beta-Binomial成分，再以相邻CDF差的连续稳定提出停止；这是指定校准人口、拟合器与阈值的监控接口，不使稳定分布成为正确分布，更不能把需要gold的正确人数直接搬成无标签单请求的自知概率。逐题状态、跨题汇总、标签权限和实际执行的轮次上限须分别保存，未观测的真值不由EM补出。共读历史与共同偏差会破坏条件独立，提前停止也可能损失accuracy；应与固定轮、原多数/最佳单judge及外部gold配对验收，而非只比收敛速度。全部成员/历史调用、校准标签、拟合与阈值选择、独立回归均付费，近似token总数不等墙钟或SLO。标签、分布或成本资格不足时，保留有界固定轮与独立核验/Unknown，不由意见一致或统计稳定批准单题truth、普遍准确率提升和自动发布。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12697 -->`

本人末注：

- `SF-2025-ARXIV-2510-12697` — Herschel，Daily2025-10-16补Oct15；exact-v1 §4.1/5/6/B2/B4/C必要，2+2+2=6，跨题有标签correct-count拟合与逐请求停止资格差额深入。旧本日必要复用，保trueconcept/条件独立假设、准确率反退、3round与表4–8round冲突、近似token及全部费；不采完整证明/无标签在线recipe或净速。未核实现/复现；整体PRE/SAVE/完整自读/solePOST只本日canonical实际层。

## 八项具体NC提案

各项都仍保P及原分数/完整必要反侧，不因“同主题”关闭，不声称本文所有结果已被书覆盖。下述采用命题不包含新的细节算法recipe；若reader发现实际差额则仅重该项。

| 身份/分数/已成必要 | 本次仅采用的论点与实际覆盖 |
| --- | --- |
| 12548 VISaGE，2+1+2=5，writer§3–4/Limitations/B–D、R43key | 只典型性与任务要求冲突、concept与当前instance的gold不能混、命名提示和过滤人口分责，不采MM-SHAP因果/所有模型同向。实际Ch66完整ProtoBias段（SF2601-04946）已明确“符合要求但不典型”vs“典型但违反条件”的反向配对，冻结条件/过滤/独立标签并拒绝prototype替target；上方几何score调节段与下方多reference平均段又将proxy、目标满足和参考人口拆开。此次概念问题与单图问题是该目标合同的具体两人口，不新增可迁移新操作；拟NC。 |
| 12355 Brain–LLM，2+1+2=5，writer§3–5/A1.3/A3/A10、R48key | 只BA ridge/voxelMSE与NWP CE不同目标、归因/扰动资格及随机对照，不采脑计算等价。实际Ch66 GemmaScope2完整两段（SF2025-GOOGLE-GEMMA-SCOPE-2）分activation重建、LMloss、解释firing与任务干预；RFEM完整段（SF2510-06070）明确target梯度新增目标与费用、plausibility/稳定性/行为响应不替faithfulness。已承担目标/读出与归因资格分责；Brain carrier未带来所采用的新人脑机制，拟NC，top词随机替换非matched控制仍在日报保留。 |
| 12463 Wug，2+1+2=5，writerPDF pp6–12、R48key | 只人机参照/模型选择人口和任务难度/资源混杂，不采语言资源单因果或p=.055等价。实际Ch66认知框架完整段（SF2026-GOOGLE-COGNITIVE-FRAMEWORK）要求明确成人参照与相同指令/示例/工具/输出、分布和构念不确定性；固定estimand分析审计完整两段（SF2602-18710）明确过滤/分析选择改变结论、survivor分母不等原总体。它们具体承担排BERT及四语言任务/工具不配平的测量限制，本文不另建立资源→能力机制，拟NC。 |
| 12722 artificial-language，2+1+2=5，writer§3–7/Limitations/B1；key待reader | 只已知词汇下短训长测/语法支持与PPL、最小对和typology不同目标，保Recursive不显著，不采人脑/通用working-memory因果。实际Ch66长度外推完整段（SF2606-07254）要求指定transition holdout、状态与readout分验，明确只排指定模板路径且有限群不授自然语言/无界记忆；认知框架段另冻结构念/参照。当前AL只是另一有限生成支持与输出目标人口，未提出可采的新系统学习算子，拟NC。 |
| 12750 VQArt，2+1+2=5，旧必要+本轮§4；key待reader | 只count更相似distractor使维度比较混难度，metadata/筛选人审不授全图truth，不采art/MoE因果。实际Ch66 option-prior完整段（SF2602-17377）把选项生成器/候选数/语料共同冻结并与含题干/均匀候选配对；MCQ修复完整两段（SF2602-06221）明确换distractor同时变答案唯一性、难度与所需知识，子集排名不隔离构念。实际已经承担该具体反侧，不需按艺术场景新增段，拟NC。 |
| 11852 sarcasm evaluation，2+1+2=5，Cicero R49首次必要 | 只分类、解释相似度与faithful不同目标、有效解析分母，保Listing2参考可见/公式人口未闭，不采架构因果。实际Ch66首段自动prompt优化完整段（SF2610-13287）拆宽parser accuracy、严格consumer拒收、cap截断和多重失败归因；GemmaScope2/RFEM上述完整论证又拆解释可预测/像人/稳定与真实行为faithfulness。这些已承担本次窄采用，CLIP解释得分不是新增truth或解释学习机制，拟NC。 |
| 12608 StyleDecipher，2+1+2=5，旧III+writerIV、R54key | 只改写/离散与连续style-change sensor、来源/阈值资格，不采UMAP或KL为解释因果。实际Ch66来源检测完整段（SF2605-15518）保存原始来源、模型修订过程与最终类别，明确binary/第三类人口、域移阈值与真实作者不同；其后双proxy轨迹两完整段（SF2509-12385）冻结producer/tokenizer/读出与自然人误报/Unknown，不由AUROC授来源取证、cache亦不免首次/新input全费。既有层已承载本次sensor/lineage和阈值合同，本文成熟feature组合不另改变该长期链，拟NC。 |
| 12200 HackWorld，2+2+2=6，writer§2–4/B1、R54key | 只观察/工具invoke/实际读取与终止结果分责，不采p>.1排除视觉瓶颈、flag容差为全漏洞truth或攻防上界。实际Ch66运输/结构/语义/policy/outcome完整分层表与上段HTTP200非真实完成，InteractWeb完整段（SF2604-27419）另拆完整gold、每轮实际信息和最后可执行outcome，UserSWE完整段记录真实工具/双侧测试而非模型声明。实际已承担接口操作/可见信息与最终资格；CTF容器是该受限人口，不新增独立系统机制，拟NC。 |
