# 2602.09438v1 必要审阅（作者准备，Source待独立）

[ACTSC](https://arxiv.org/html/2602.09438v1)，root AB/date通过；2+2+2=6。§3/Alg1–2 L95–213：frozenLLM最后prompt-token FFN activity、MATH easy/hard extremes neuron mean-gap筛选、linear BCE probe，在线单forward不预采答案→easy单sample/hardwindowSC。中等difficulty排除训练，probe标签是题目难度不是该targetmodel可校准错误率或独立truth。原文阈值τ是每新dataset预测均值L205，故“不需任何新数据准备”须限定为不生成预采样答案，仍需目标分布一遍probe/阈值估计；不授陌生singlequery无需校准的普遍控制。

§4 L237–308/T1直接反侧：Qwen2.5Instruct3/7B、Gemma3IT4B，AIME30每年、MATH500；同temp.7/topP.8/cap40，但SC40/AC.95/ESC5allagree、ACT confidence.50停止，采样效率并非只probe因果，预算/停止条件未匹配ablation。Qwen7B AIME2025 16.67→13.33、GemmaAIME2024 13.33→10为实际退化，不授全面等质。MATHprobe train/test划分和feature selection leakage control不明确，seedCI/repeatsND，rare-difficulty误判risk不可从均值accuracy恢复。

Token数不是wallclock或SLO；Qwen7B/AIME2025 offlineDSN138.7s+train5.9s一次144.6s，online P(Hard).59s每query非零，“–prepare”表格不等于没有offline/target-calibration/activation-extract成本。hardware/precision/batch/concurrency未披露，不把87%样本节约映射87%GPU省。科学题只用于原protocolcontext，不采用AIforScience域能力。Source后actualowner拟INFER-SCHEDULING或MODEL-TRANSFORMER-LAYER budgetcontrol，待唯一owner差额；支持候选替代cheapprior足停，无生产guarantee。
