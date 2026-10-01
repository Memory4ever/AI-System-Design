# 04/22 四项仅报告候选的有限非作者审阅

复核者 apr01，非本日报作者。分两次定点重开 `2604.19015v1`、`2604.18966v1`、`2604.19149v1`、`2604.19234v1` 的必要官方原文并对读当前 owner；不复现实验，不核本日十四来源、首公开日期、其它候选或整日 Gate，也不改 Books/正式日报。

## 2604.19015v1 FedProxy — 受限保护机制，仅报告 PASS

[官方 exact-v1](https://arxiv.org/html/2604.19015v1) §4.1–4.3、Alg.1、§5.2–5.3 与 [Ch30](../../../../../books/part-04-training-system/30-lora.md) adapter 组合/同坐标合并、[Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) federated communication 实际论点对读。原方法以公共数据压缩同源 LLM 为层可映射 proxy，客户端更新 proxy，server 汇合 task vectors 与逐维冲突，再直接用 proxy 对应层覆盖原 LLM；不是 decode-time logits 混合。Eq.6 是 `|cos|` 权重，反向更新也可提高该量；Eq.7 的 `C` 越高表示符号越冲突，而 §4.2.2 把高 `C` 称“consensus”与公式不一致，不能照录这个文字解释。§5.3.3 明确 IP 仅降低基座直接暴露，不是密码或信息论保护；有限 7B/客户端/QA-GLUE、通信与 client 更新成本不等同预算。现有 Ch30/36 已要求 merge 坐标、组合后行为、通信与隐私边界，但未逐字写这套 proxy 算法；该受限组合可在 Daily 留下正反证据，不足以新增一个可推广的 IP/隐私保证或发布控制决策。维持 `2+2+2=6`、安全相关深入审阅、Books `仅报告`，不得改写为整个 privacy/IP trilemma 已解决。作者证据中“§5 为 LoRA 更新，Alg.1 抽象训练 φ 不等全参”的澄清也与原文一致。

## 2604.18966v1 TabGRAA — 受限目标与反馈分工，仅报告 PASS

[官方 exact-v1](https://arxiv.org/html/2604.18966v1) §3.2–3.6/Eq.5–10、§5.4/Table 7 与 [Ch34](../../../../../books/part-04-training-system/34-dpo.md) pair/reference/margin、[Ch31](../../../../../books/part-04-training-system/31-rlhf.md) 独立 scorer/反馈分工对读。高/低两组各先平均 policy/reference log-ratio，再取两均值差进入 sigmoid，两侧保持梯度；不是逐 pair DPO loss 简单平均，也不等同 GRPO reward normalization。质量 scorer 可从真实表格训练；训练模型未直接把每条 real row 放进这项 loss，不推出全系统没有访问真实数据或具形式 privacy。Table 7 中部分结构保真低于 baseline，MIA AUC 近 0.5 不覆盖所有攻击；固定 reference 亦非硬 KL/单调改善证明。现有 Ch34/31 已把 preference signal、reference、反馈代理与实际行为/数据真值分权，但未主张 TabGRAA 此组损失公式已存在；论文给出 tabular 合成的局部 operating point 与反例，暂不改变本书一般 LLM post-training 的目标选择。维持 `2+1+2=5` 标准审阅、Books `仅报告`，不因只在 tabular 研究就硬拒，也不因新公式强行写书。

前两项仅证明上述实际阅读范围内的处置，不签候选分母、日期/来源覆盖或整日完成。

## 2604.19149v1 Self-Reading — 受限相关性和筛选干预，仅报告 PASS

[官方 exact-v1](https://arxiv.org/html/2604.19149v1) §3.1–3.2/Table 1–2、§4.2–4.4/Eqs. 1–8、§5.6 的 Same Pool 对照与 [Ch5「从可读出到机制」](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)实际论点对读。answer→reasoning attention 的 centroid 前移与 anchor 集中确是可测的局部几何；但随机 200 例中有正确而非该模式 12 例、错误而有该模式 3 例，不能将它作为正确性的充要条件或内部确定性真值。Steering vector 的两组分别来自正确池的高 SRQ 80% 和错误池的低 SRQ 80%，故正确性、trace 内容和 reading pattern 一起改变；Same Pool 只控制候选池大小，不能把增益唯一归因于“模型因果使用了某段推理”。原文确做 answer/reason 阶段干预并报告受限任务收益，不能反过来说它只是静态可视化。

Ch5 已把 attention/readout、局部干预与下游行为分成不同证据级别；本篇的 SRQ/CAA 是该边界内的局部筛选与 steering operating point，尚未提供会改变书稿长期 controller 选择的独立因果合同。维持 `2+1+2=5` 标准审阅、Books `仅报告`；保留 white-box attention、外部语义标注、activation steering 与数据选择成本，不声称普适跨任务、跨模型的可靠性。此判断不是说 Ch5 已写出 SRQ 算法。

## 2604.19234v1 OTCA — 时间代理与多目标权重分离，仅报告 PASS

[官方 exact-v1](https://arxiv.org/html/2604.19234v1) §3.1–3.4/Eqs. 8、11、13–15、§4.2/4.4 Tables 1、4 与 [Ch33「Typed Credit」](../../../../../books/part-04-training-system/33-grpo.md)、[Ch31 多目标 reward](../../../../../books/part-04-training-system/31-rlhf.md)实际论点对读。打印公式 `Ã_t^i = w_t^i Σ_k c_k^i A_k^i` 的 `c_k^i` 没有时间下标；它是相邻 latent 对最终 latent 相似度变化所得的时间代理，乘样本级目标混合，而不是每个 reward objective 拥有独立的 timestep causal credit。Eq. 11 的固定样本标量优化可以在所给形式下成立，不能从中推出跨样本、clip 后全参数更新的 Pareto 或无偏因果保证；Eq. 13 的 exploration bias 也改变原 min-norm 目标。Table 1 的 Aesthetic 6.6028 低于 DanceGRPO 6.8917；Table 4 的 Full ImageReward 1.1998 低于 TCD-only 1.2618，MOCA-only Aesthetic 6.2120 低于 base 6.2508，不能写成每目标均受益。

Ch33 已将 denoising 内部 step proxy 与真实 outcome/credit 分权，Ch31 不把多目标标量混合当成各目标都改善。论文提供 FLUX/Wan 视觉生成的受限可分离权重配方和反向切片，未把时间相似度升格为可迁移的真实过程贡献；维持 `2+2+2=6`、因过程归因保证作深入审阅、Books `仅报告`。这不否定作者所测视觉指标改善，也不冒称现有章节已有这套公式。

新增两项仍只签上述单篇必要原文、实际 owner 与处置边界；不签其日期归属、04/22 其余候选、来源覆盖或整日 Gate。
