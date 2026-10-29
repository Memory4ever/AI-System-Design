# 2604.00725v1：局部质量/资源对照，作者必要Source

[精确v1](https://arxiv.org/html/2604.00725v1)已实际读§3/4与§5 Tables4–7的决定性范围，未取June v2。题摘潜力经root纠正保留：同训SSM/Transformer在length、paragraph上的质量成本差额，不因OCR领域标签EX。

拟2+1+2=5，标准必要对照完成，不授普适复杂度结论。DAN与Mamba共享CNN，训练/validation paragraph伪标签由ROVER权重5/3/3构建，976 manually corrected test；主要仅1–10lines/≤1000chars。Antiqua line MambaAR/DAN均1.83CER但53.3/156.5ms；Fraktur及CTC/VAN分支不支持统一优越。Paragraph Mamba6.07CER vs DAN5.24（退0.83个百分点），195.6 vs401.2ms；VAN6.42CER/17.2ms又是更便宜对照。

100→1000chars Mamba memory2.865→3.622GB、DAN0.676→1.551GB；1.26×vs2.30×较小增长**不等于更小绝对memory**，Mamba14.1M vs DAN7.1M又非参数matched。仅4个有限长度的peak memory测量不能认证O(n²)定律，不能把KV-cache内存一般改说二次；原Table7该理论概括不采用。A100局部latency/throughput不具完整batch/precision/concurrency/SLO，少CER/较快不授所有部署更好。

准入对象为有限architectural comparison的quality-cost条件，拟仅报告（不是‘SSM已有主题所以NC’）：未新增通用SSM机制或超出小OCR对照的资源规律，当前所需长期判断已有canonical局部quality/absolute-vs-growth分账，新增numbers不移入通用章节。若root判实际主线新边界必须Books，须先定位唯一owner和具体缺口，不自动类比长上下文。

日期双向链及匹配arxiv.content注册字段已存SUP_DATACITE_BOUNDS：不改变原报告日期。

## 非作者必要原证复核

root实际核§4共享CNN/伪标签人口及Tables6/7完整quality/resource反侧，接受2+1+2=5标准完成、仅报告：6.07vs5.24的质量退步，VAN更快；1.26vs2.30增长非更小absolute，14.1vs7.1M非parameter matched，四长度不认证KV一般二次。准入为有限architecture取舍，不按OCR标签EX；无通用新SSM mechanism或长期缺口，因此仅报告而非主题NC。本项无Books写入，不追v2或其余附件。本回执不授DAY。
