# 2601.09000v1 — WSD geometry has a two-model counterexample to Transformer exclusivity

[Exact HTML](https://arxiv.org/html/2601.09000v1)，必要原段PRIMARY_09000_NECESSARY.md（§3、4、Appendix A架构）。拟2+1+2=5：Transformer特有WSD解释→160M decoder-LM与334k CNN的局部相似路径/曲率观察→收窄架构特有归因；不把“Universal”或成熟schedule取舍计增量。标准必要证据完成，拟OnlyReport，待root实际源/owner终裁。

§3 LM约3B SlimPajama tokens、batch256/seq2048；CNN CIFAR10/batch128。作者Setup写Adam，主几何解释写AdamW，未擅自消除配置矛盾。80%stable→decay checkpoint插值有局部凸valley，cooldown末最大Hessian eigen增加，PCA仅解释约40%variance，阶段方向/早cooldown Hessian加权norm差不等唯一river-valley因果。Weak-Quasi-Convexity只在warmup后采样的一组iterates检验；更新与negative gradient的cosine大多正，不能把AdamW推广为SGD，或从有限轨迹授全domain凸性/任何架构通用收敛定理。

作者两架构局部结果足以反驳“只有Transformer能见到这些WSD现象”，但两模型不证明全部架构/规模/数据及普适optimizer解释；小CNN不能完美拟合本身也限制overparameterization叙事。AppA仅架构参数，可选artifact未运行；hardware、precision、full optimizer hyperparameters、重复seeds/CI及matched端到端吞吐 Not Disclosed于必要core，不采用加速/普适定律数字。

Books拟OnlyReport：实际TRAIN-PRETRAINING Ch28:687–703已将schedule与optimizer/batch/model/token预算、returned-estimator和cooldown相关证据分开，不声称Transformer专属、也不声称decay必然导致遗忘。新增实验为特定LM/CNN上几何的局部解释性验证，未给可承载新控制分支/普遍保证；保留日报作为反排他性证据，不假称书中已有本篇PCA/Hessian实验、不泛Existing吞掉新验证。未写Books、未复现实验。

root实际必要原源与具体owner终裁：5分标准完成、仅报告通过；受测iterate弱准凸/PCA不授普遍几何或新WSD方案。无Books写入。
