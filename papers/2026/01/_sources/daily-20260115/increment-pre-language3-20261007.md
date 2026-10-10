# 三项已校准语言/表示潜力的必要审阅

作者supp_jan15；原52不动。已独立准入校准，当前只核本篇必要命题，不将216题名库存或全部潜力升全文队列。精确v1原件在language-core0–4；日期原字段在increment-dates47，普通公告/正式ID上下界方法复用，直接更早正文信号轻核。08181已获root必要证据/actual owner Existing通过；08146已获root必要证据/PRE与actual Ch29:415、397–430邻接/自身1357 POST通过，窄锁释放；08545待独立PRE。当前无Books锁。

## 08181 TabPFN Through The Looking Glass — 2+1+2=5，标准完成，具体Existing通过

精确§3.1–3.5/§4实际读：TabPFNv2样本/feature两轴attention，独立context-fit的系数probe低train accuracy；将多个关系合进一个context并附switch后（probe不看switch token）才较好读出，作者§3.2承认可能dataset-specific signature而非普遍系数编码。中层a·b与answer可预测、native output alignment更迟，不等于内部必按该算法算，也不允许由probe最早层直接裁去后层。复杂MLP probe退步不是线性唯一性证书。正文系数公式两处重复x与口述x/y不一致，不采用具体公式recipe。只有toy additive/multiplicative；没有activation patching/ablation，作者列futurework。sample/seed/训练probe协议、硬件/precision/batch/concurrency/SLO Not Disclosed；数字曲线仅该局部，不复现，不授全部contexts无共表示定理。abs仅v1，无更早完整项目链接。

实际PLATFORM-EVALUATION-SYSTEM Ch66:2206–2229完整邻接承载probe有预测信息≠因果必要或自动干预权，3049–3063完整邻接承载estimand/identification/反证压力与无法识别时降级，跨reference不可机械要求同低层head。采用本稿的context依赖及probe/native output分账不改这些已有判断；拟具体NoChange—Existing，不为toy case新增段。

## 08146 Mechanisms are Transferable — 2+1+2=5，缺口深入完成；Ch29实际POST通过

精确§3–6/§8/A与D.1–3：label-balanced mean是in-distribution估计不是faithful counterfactual；directional margin/projection选proxy任务head，grad masking只更新选head+LayerNorm，其他参数冻，不是全forward prune或唯一因果机制保证。有限Qwen2.5-0.5B/NusaX与XNLI、一token标签、4seeds，50正确样本/均值、poolA competence+mean+discovery共用，poolB第二阶段heldout；共享pool排名较稳不证明免泄漏。难transfer倾向Circuit、易transfer可NearZero；弱English50-sample XNLI更深scope可退步，源task需先形成，不是学习任务替代。Source retention只单源局部accuracy非所有能力；Table4把Circuit/NearZero中更好的test表现报CT summary，不能当预先选定policy泛化。D.1 mean ablation另验faithfulness，mean是参考不是中性真值，增depth/ratio收益有饱和或退步。5epochs/128tokens/lr5e-5/batch16；hardware/precision/concurrency/SLO与总discovery+训练墙钟Not Disclosed，不以.23–.66%trainable参数推同幅总加速/显存下降。abs有后续v2–4但当前无撤回/纠错提示，不遍历未来全文；本次只v1。

actual TRAIN-SFT Ch29:398–419完整邻接有reference支持注入与sparsecarrier联合训练、事后circuit非因果必要；尚非**先学会proxy任务→选择更新原decision heads或同数量NearZero heads→受初始target competence约束的plasticity scope**这一选择。拟在sparsecarrier前用一段条件分支，保小数据模型与低competence反侧、LayerNorm并非仅head、筛选/训练总成本与普通full/adapter共存；若actual其它段已有同命题则Existing，不因paper新名必增。确认长期差额后再深入具体命题/授锁，当前不写Books。

上述CT-SFT差额已按root窄锁写入Ch29正文415，保留LayerNorm、proxy competence/条件scope、test择优及总discovery/train成本。root实际完整397–430邻接与自身1357末注POST通过；上段保留原提案供恢复，不再是待写状态。

## 08545 Learner-Tailored Program Repair — 2+1+2=5，标准必要完成；实际owner差额待独立PRE

精确method Eq1–14/主Tables1–4与Appendix设置/指标：同题、同user时序错误→后来passing pair中保diff一致>.65，edit向量h_fixed−h_bug加当前embedding以选参考；failed generated patch进入下一次retrieval query/search scoring，测试只是限定fixture而非完整semantic oracle。code/diff+LLM bug说明与iteration一起增益，不单因果；Eq10的h_cw记法不统一不采用精确solver。407tests/306users/65problems来自ACPR test按GPT4o三次repair成功率>1/3排简单例，CodeNet同problemID retrieval274349条，不授OOD所有repair。T0.2生成、top5、GPT4omini T0 judge；A80080GB两卡仅open模型，precision/batch/concurrency/SLO/完整tokens调用费/seed Not Disclosed。iter3比base多calls，未matched总budget。

Bug explanation只为passing-code计分（Appendix L341），故更好B-F1混合repair pass gate与说明内容；189GPT4o输出/1390pairs两人独立、第一作者协调，point agreement93.02但sample67.72/11.12indeterminate，不授所有explanation正确。reference注释与生成/judge可能同源，不授完全机制解释。直接repo README只有artifact配置/执行说明，未见更早dated完整稿信号；没有执行其中docker/代码。actual AGENT-RAG Ch76:730–764/1169–1199已读，已有查询改写/工具反馈与迭代验收，但未明确失败patch的edit方向成为下一轮reference检索proposal；拟在反馈检索邻接补一个有测试边界/总调用成本的条件分支，不把passing tests授语义正确，等待独立源/actual owner PRE与窄锁。
