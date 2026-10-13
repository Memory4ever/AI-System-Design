# 03-19 补03-18：首批准入校准待独核

仅本日日报作者 resume_mar18。四主题 API 原查询/分页在 SUP_API_*.json，分别97/136/50/118命中，跨组256唯一标题。标题浏览只作窄主题补检，不是256完整题摘/必须Evidence队列。以下10项已实际完整读精确v1题摘；current header/Comments另存 SUP_FIRST_CURRENT_HEADER_20261011.json，未见withdraw或具体勘误/纠错说明；普通版本变更不触发全历史diff。

前3完整题摘在 SUP_FIRST_AB_RAW_20261011.txt；16039/16590/16666/16871/15773/15909题摘在各SUP_AB_*_20261011.json；15954实际完整题摘读于官方v1，正文如下。首9日期原字段见 SUP_FIRST_DATES_20261011.json：v1 Submitted均UTC03/16T18:05之后至03/17T18之前；DataCite findable/registered均UTC03/18T02:16–02:42（Mobile v1Updated03/23不误当firstpublic）。官方availability明确ID/DOI只在announcement时分配、提交后可能延迟，普通Monday14→Tuesday14 ET最早Tuesday20；本批最早BJT03/18，findable日期作已公开上界的限定推断也BJT03/18。拟日级03/18，不补造精确公开时刻、不把Submitted或Updated直接当公开；仍请root独立裁决此夹证口径及是否有具体更早正文信号。日期确认前不是确定候选。

| ID | 原约束 → 题摘实际增量 → 待核设计选择 | 初步准入 |
| --- | --- | --- |
| 2603.15854v1 FlashSampling | LM-head后logits HBM流量/额外kernel → tile内Gumbel+局部argmax/层次categorical精确分解 → exact采样能否作为matmul epilogue而不是近似后处理 | 拟入；核精确性条件/TP边界/端到端代价，不采用up-to数字 |
| 2603.15953v1 HAT | 固定vocab/换语言适应与序列容量 → bytes→word encoder、旧Llama去embedding/head保backbone、decoder cross-attend回bytes → tokenizer与预训练backbone迁移的边界 | 拟入；不是模型品牌/通用byte-level介绍 |
| 2603.15965v1 MoLoRA | 逐序列单adapter不能同序列多模态/多专业 → 按vocab或learned gate逐token路由独训LoRA → 组合专家是否无需联合重训及N对KN的确切任务假设 | 拟入；最优/胜大模型中央claim需反证，不先采用 |
| 2603.16039v1 Residual Duality | sequence自适应混合而depth固定累加 → depth causal-read局部operator与ShortSWA双轴对偶但系统不对称 → 算子等价是否不授cache/kernel代价等价 | 拟入（设计边界）；不因观点/小稿排除，需实际可证推导与硬件边界 |
| 2603.15954v1 MobileLLM-Flash | resource-constrained hardware需实际latency而不是只FLOPs → hardware-loop latency模型+继承pruned权重、联合结构/attention-skipping的staged Pareto → 端侧设计为何不用特制attention/kernel | 拟入；核搜索/continued-pretrain预算与runtime条件 |
| 2603.16590v1 BATQuant | integer rotation迁MXFP4跨block传outlier/bimodal → granularity内affine、GPK分解、block clipping → 正交/global混合可否破坏block scaling | 拟入；核归因及nonorthogonal变换可折叠代价 |
| 2603.16666v1 Fast-WAM | 训练video与推理imagination混在一起 → 保video cotrain但去testfuture受控variants → world表示训练收益不必等于test-time rollout必要 | 拟入（反证）；核各variant/闭环/latency范围，不采用普遍无须想象 |
| 2603.16871v1 WorldCam | abstract action难精确控制/长程一致 → Lie-algebra action积累camera pose＋pose索引回取历史 → 统一几何状态如何同时约束控制与revisit | 拟入；核pose误差/生成与真实观测区别 |
| 2603.15773v1 Morphemes | 假定tokenizer形态对齐能决定generation → 七Arabic/multilingual模型的对齐非必要亦非充分证据 → token粒度与productive generation的因果混杂 | 拟入（局部反证）；不是一般Arabic应用提高指标，核任务/预训练混杂 |
| 2603.15909v1 Psychometrics | prompt设计与网络psychometric reduction在BigFive量表生成 → adaptive prompting改善该领域结构效度/冗余 → 未识别改变模型机制/训练/系统选择的可迁移增量 | 拟排除贡献；完整题摘非因领域/没开源，temperature反例只此psychometric实验；不另追不影响关闭的日期 |

代表标题范围外：2603.15840 Scientific Decision-Making、2603.16002 Radiology Report Annotation、2603.15932 CT synthesis，明确AI-for-Science/领域已有AI应用，未见具体纠错信号时标题范围关闭；未称完整题摘。15909为完整题摘代表负侧，不把所有domain应用统一批量关闭。首批仍待独校，未评分/Source/Books；入口过宽部分已收窄到上述模型/推理/训练/世界机制，不顺序遍历256。

15954必要题摘机制已在上表保留；完整题摘实际读于 https://arxiv.org/abs/2603.15954v1 ，不将全文照抄为本报告论证。
