# CGC 2603.16440：必要中心桥与安全隔离拟稿

作者 resume_mar18；仅03-19补03-18，2+1+2=5只给SAE feature-density预算/PTP桥，中心理论须深入。HTML404，实际[精确v1 PDF](https://arxiv.org/pdf/2603.16440v1)§3–6/Definitions1–5/Theorems1–2/Table1与直接限制已读；本地SUP_CGC_16440v1.pdf原件，web截图失败后实际渲染p6/p10视觉回对保留比例约束/初始化式及Table1/图2。未遍参考文献/代码或复现，不因小模型/负面结果排除。

## 支持与决定性争议

§3用每head SAE activation的breadth、频率entropy与跨semantic输入Jaccard几何均值构成density，§4用于非均匀retention/搜索边界，是具体可核提案。但Definition2的p_f是每token激活频率，TopK k=25时总和通常25而非1；未额外归一不能直接称Shannon分布entropy或用logF作[0,1]归一保证。Thm1将feature activation高entropy直接推出decoder方向铺开/结构冗余较低；activation频率本身不指定decoder列角度、复制/尺度或剪除权重到功能的映射，§6.1自己承认非紧等价且self-repair未闭合。不能从统计量定义推出随机删权重下feature destruction单调。

§4.2–4.3视觉实核ξ为retention，约束ξ≤ρmax与拒绝超过ceiling只限制最多保留，不强制高density最少保留；本宣称capability protection保证需要有效budget语义/可行性，而不是作者擅自替换不等式。初始化式与实际固定global size的归一亦未给完整可行性/repair说明。Thm2额外采用高density convex/低density concave的D(r)曲率，Thm1未证明这些条件；不同函数的凸凹与密度排序不能直接用一个Jensen式推出任意nonconstant density严格更好，更不能从CGC-L传到未实测CGC-F/所有压缩轴。§4.4跨quantization/rank保证与§6.1明确不解决quantization/outlier关系并存，不择一删除反证。

GPT2-Medium355M/24×16heads、singleT4，128×512 WikiText103 train用于384 SAEs，64→512/k25/5epochs/Adam2e-4；test32×512 nonoverlap，50%head output-projection retention，不是全模型减半。Table1 dense26.68/uniform27.57/CGC27.87/inverted27.86，实验未证推理能力更好；§6.2却说该表展示reasoning差异，没有reasoning结果支持。与Wanda Spearman−.054/384head仅低rank关联，不证明统计独立或与所有其他importance正交；individual ablation Pearson−.066 p.20/Spearman−.077 p.13未显著且不证“GPT2能力均一”或SAE密度已正确。浅SAE/PPL/规模诊断只hypothesis，后续大模型收益未测。完整precision/library/runtime、repeat seeds/CI、SAE/搜索墙钟与部署I/O/batch/concurrency/SLO ND。

## actual owner / 本次拟终态

实际Ch49 525–552完整敏感度/entropy proxy→齐次结构→protected set及796–830性能测量合同，Ch48/50开篇已读；soleINFER-TENSORRT-LLM拥有artifact/校准评分/保护预算分责。现文已有proxy非能力与保护集分责，但不假NC承载CGC新density理论或消除中心错误，也不绕争议仅写一般PPL不够。拟中心安全终态隔离：保5分候选、不EX、不降分、不Books、不授正面Evidence/Coverage/PTP/capability/服务保证，待非作者独核。

一次精确请求：归一后的density定义/decoder几何与剪除映射假设；retention上下界/global-budget可行性修正；足以成立单调/严格改善的证明或有效限定反例处理；matched-size、独立capability评价与受限cost对照。勘误/可检推导与最小评价可替代全部artifact，到达仅重开该family，不扩完整引用史/新来源发现。
