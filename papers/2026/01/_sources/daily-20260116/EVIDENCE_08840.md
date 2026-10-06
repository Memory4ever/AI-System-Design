# 2601.08840v1 — entity editing 的一致性与邻近损伤

[精确 HTML](https://arxiv.org/html/2601.08840v1)，实际§IV方法、§V-A/B RWKU、§V-D样本/token/order消融、§V-E consistency weight与§VI限制。2+1+2=5；隐状态更新一致性是可核替代，不把成熟MEMIT闭式更新/整体unlearning原则计入新增。root实际原源与Ch72实体擦除/retain现owner复核通过：标准完成、仅报告。新的局部consistency候选机制保留日报；无λ=0与matched selection消融，不能归因新增长期擦除结论，亦不是已有主题吞掉新增机制。不改Books，日级Gate未授。

MLP参数更新采用R Kf^T(KrKr^T+KfKf^T)^-1；retain covariance来自100kWiki样本，实体一跳facts+模板+paraphrase，last subject token取key并以95%能量SVD选子集。主要增量Eq7把第j个modified hidden state拉向前j-1样本均值，配null-answer NLL residual优化；是激活一致性正则，不是严格参数擦除/全局认证。分层残差δ/(L-ell+1)沿MEMIT方式传播。j=1空均值实现未说明。

RWKU100实体/ToFU20实体分别单实体编辑，100/20个不同模型求均值，不是一次批量擦除。Llama3/3.1 Instruct8B，编辑配置正文两A10040GB但成本段称单40GB，baseline full tune另两80GB/3.1训练4A80080GB；precision/运行时/repeats(除四次order)/置信区间NotDisclosed，不能授统一端到端效率。λcons=.05。

TableI Llama3 forget-all15.9对MEMIT26.6，但neighbor72.2低于MEMIT76.4；3.1 neighbor64.7也低于MEMIT72.2。MIA/FM/RM为其各自protocol输出，不是直接隐私保证。Mean混合forget、neighbor、utility及MIA异尺度，不以排行榜综合分替代分项。TableVIII只对.01–.2 positive λ，缺λ=0 matched消融，PCA聚簇和案例不隔离一致性机制因果；四种order小范围波动，不普遍order-invariant。TableVI LST对LT部分QA反而差，all/neighbor局部取舍。样本20–100提升forget同时损neighbor是重要反侧；不能照录“全面保留/精确擦除”。局部拟采用可核一致性路径和分项损伤，不采用永久forgetting/security或普遍优于训练的方法保证。
