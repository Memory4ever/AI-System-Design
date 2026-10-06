# 2601.08951v1 — predictive annotator harm versus normative safety

[精确HTML](https://arxiv.org/html/2601.08951v1)，实际§2/3、§5/Table1、Limits与E.1评价定义/E.2必要段PRIMARY_08951_CORE.md。2+1+2=5：新增是disagreement-rich harm人口中个体/aggregate predictor与profile/kshot的具体反侧，不把成熟价值多元原则、demographic correlation或安全愿景计分。拟标准完成/Existing当前Ch66:2546–2561和2948–2952，待root实际原源+owner复核；不授日期或日级Gate。

AIR5692 seed经DeepSeekV3-0324每条11harm-level变体→62612，SafetyAnalyst/KALEIDO提取features，geneticalgorithm10000iter按目标oversample .4–.6且每seed最多2→150prompt；100US Prolific参与者各评全部150，15000ratings，English prompt-level judgments。标签0–100，人口非现实任务流量，不测model response造成的harm。feature/trait回归是observational association，不识别trait因果或安全policy正当性，不能用synthetic0–1等级当客观harm真值。

固定100promptalignment/50test split；individual本人rating vsaggregate mean训练，然后按各annotator test MAE→平均，预测不同目标与真正安全行为分开。kshot examples与LLM inferred natural-languageprofile不同表示/成本，不是人格groundtruth。temperature GPTprofile.15、SafetyAnalyst harmtree.6、test GPT4.1/WildGuard0；别的所有生成配置/hardware/precision/重跑与CI构造范围NotDisclosed于必要段。WildGuard yes/no logprob归一化probability与binaryclass在continuousrating MAE下不是同type评分。Table1同时有refusal/completion（Qwen8B completion65.6%、部分Claude refusal>0）但MAE如何处理未完成/拒答未在必要eval定义给出，不采用跨产品精确胜负；Table3与Table1 GPT4.1 kshot数字不一不拼合。以统计分数最优为安全release依据未成立。

具体Existing：Ch66:2546–2561明确预测个体/群体标签分布与规范rubric两个目标、annotator/cohort身份、majority压分歧和描述性预测不作安全判决；2948–2952保存annotator/policy/slice并分operational ambiguity/value pluralism。root已实际必要primary与该owner核验通过标准5 Existing；原normalSubmitted/registered完整字段及条件区间另见DATE_NORMAL_FIVE.md，不由Updated独立授日期。本篇新个人化实验只在日报保留，不冒称它的新数字已在书稿，不把‘主题已有’作贡献排除。未运行代码/复现，也不采用U.S./English结果为全球公平或生产安全保证。
