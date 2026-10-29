# 22075v1标准审阅与仅报告提案

首批准入/公开日期root校准通过，评分2+1+2=5不改。作者实际读[exact-v1](https://arxiv.org/html/2603.22075v1) §3/Table1–2、§4.1～4.3/Tables3–4、§5.1～5.4，必要sampler配置及八项限制。采用局部实测配置证据，不采用摘要sole-variable因果。

两模型同TinyStories50M/20K steps/batch32/seq512/H10080GB、共享layer/model width等；AR123.6M、MDLM162.7M（31.6%更多）且CE目标不同不可比较val loss。单seed AR在14K best后overfit、MDLM20K仍未plateau，仅说明该pair每步训练throughput接近，不推相同质量总成本。1K个128token输出：AR nucleus p0.9/T0.8，MDLM100step/temperature1.2→0.5/repetition1.3；参数与sampler差异使prefix diversity不能唯一归因范式。无downstream QA/分类或更多数据、规模、seed；不把自报fluency/creative-vs-code类别外推成系统选择保证。训练precision Not Disclosed；输出128、training batch32，生产concurrency/SLO不适用，未核代码或复现。

Books适用docs/ROADMAP/LS已读，MULTIMODAL-GENERATIVE-PARADIGMS 当前Ch24 masked generation第482～496的每轮预测/保守与激进schedule及第50～63的训练/额外head成本与非唯一归因边界已实际比较，Ch23/25开篇交接已读。不是认定主题相似即已有覆盖；本新增局部pair不能分离范式因果，未支持把AR/MDLM通用收敛速度或任务用途改写为长期法则。拟仅报告保留具体小规模验证和混杂，不制造Books diff，不自授独核完成。

普通下一步：root非作者标准Source/仅报告决定一次有限复核；通过后正式同步日报§3/§4。不请求Books写锁。

## root非作者有限Source与处置裁

实际独读v1§3/Table1–2/两目标与采样、§4/Table3–4、§5.4八限制。参数数、temperature/核采样/repetition配置不同且单seed，足以排除“范式为唯一变量”的强因果；Distinct4亦非MDLM全面占优，val loss绝对值不跨目标比较。作者报告的局部训练/输出观察保留，不外推代码/翻译用途或同质量总训练成本。实际Ch24基础masked schedule及表示—生成/成本边界已读：没有必要用该受限pair把通用结论改写为范式普遍律。原5分不因不写书降低；必要标准Source与仅报告有限PASS，Books0，不借主题已有覆盖冒称本实验普遍有效。尚未授整日DAY或代码复现。
