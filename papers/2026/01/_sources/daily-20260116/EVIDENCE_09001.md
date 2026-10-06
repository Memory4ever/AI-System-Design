# 2601.09001v1 — decoding entropy profile is a calibrated slice sensor, not continuous correctness truth

[Exact HTML](https://arxiv.org/html/2601.09001v1)，必要原段PRIMARY_09001_NECESSARY.md（§2、4、5、RQ1–4、§9/C.1–4）。拟2+1+2=5：无标签流量不易估计slice accuracy→top20 decoding logprob轨迹11统计+监督probability head→核其可否在外域均值聚合取代持续标注；不借通用安全/跨生命周期原则抬分。标准必要源已读，拟OnlyReport，待root实际复核。

§2 top20 entropy用截断mass的−Σp logp，未重归一化，不等full-vocabulary entropy；§4 max/mean/std/quantiles/skew/kurt/SEA11维→classifier Pcorrect，再对target slice求均值。均值只有目标人口校准成立才表示accuracy，不由source classifier calibration自动授domain-shift有效。§5十STEM推理benchmark为模型系统mechanism的测试负载，零shotCoT/去MC选项freeform；Grok4.1FastReasoning带reference作binaryvalidator，手查100条97%agreement不是所有labels为人类gold。源model-size标签有3.6/3.8B冲突，不作规模归因。

九模型、385 benchmark training groups/model，三classifier×balance×isotonic等41,580configs，CV只在traininggroup、5fold以ROCAUC选超参，test benchmark disjoint。C.3具体classifier grid，C.4 logistic balanced/RF balanced_subsample/MLP oversampling，不混为同人口样本分布。AEE是aggregate error，Spearman是ranking，两者不同；不能用rank强当绝对可靠。RQ1 extremes组合常更好但非所有模型；RQ2 Table4 SEA/MTP等在部分模型ρ高于classifier（Qwen3-8B .93/.95 vs .76），不采用“alwaysasgood”宣传；RQ3训练组balance与AEE的U形只是group间相关，域/难度/样本量混杂，.4–.6非通用界；更多group降低median/IQR是该协议观察。RQ4校准效应有限，balance会harm，不授11features总最佳。

C.1披露vLLM无system统一prompt；C.2preprocess去specialtokens后Grokbinaryschema。实际temp/长度上限/hardware/precision/seed与classifier选择总成本在必要source Not Disclosed，不采用榜单数值或近零成本。§9 prompt/decoding/posttraining改变entropy可不改变实际能力，旧model需重标/校准；连续online monitor/真实漂移率与policy release未实测。

Books拟OnlyReport：实际Ch66:2437 superviseduncertainty sensor的代表性label、domain-shift/availability、calibration与riskcoverage已承载成熟合同，Ch67:137–139把quality scorer与runtime error/aggregation分开。它们不含本篇11统计/均值实验，不冒称Existing此实现。新局部sensor可作监测候选，但未控制decoder/length变化或证明continuous目标域校准，原simple UQ亦有更强ranking，不能把实现升级为新的无需标注accuracy/SLO gate；局部评价反侧留日报，不强制改书。未复现实验/代码。

root实际§2/4、385训练组/CV/校准、RQ2对照/RQ4/§9与Ch66/Ch67具体owner终裁通过：5分标准完成、OnlyReport。top20截断mass非全词表，source isotonic不授online drift；Books实际写入0。
