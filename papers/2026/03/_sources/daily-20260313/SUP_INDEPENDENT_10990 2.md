# 2603.10990v1：必要Source、5分与具体NC独核

仅03-13既有Daily补充03-12北京时间自然日；非准备者 mar13_admission_review。实际恢复重读AGENTS/current Research/Report/Prompt、Sources使用说明/Daily与arXiv范围、ROADMAP及本日停点；LS最新相关段只作路由，不以旧51数字替代现Report。保留原窗口/候选/§4，不载入异日候选；仅own本文件。

## 身份与实际原件

实际读[准备包](./SUP_EVIDENCE_10990.md)、[完整v1题摘/history](./SUP_ABS3_10990.txt)、[精确v1原响应](./SUP_CORE_10990.raw)、[manifest结果](./SUP_CORE_10990_MANIFEST_RESULT.json)及具名[CVF单篇原响应](./SUP_VENUE_10990_CVF.raw)。arXiv URL `https://arxiv.org/html/2603.10990v1`，GET200/238409B/2026-10-10T04:06:24.305872Z；Too Vivid to Be Real? Benchmarking and Calibrating Generative Color Fidelity、八作者对应。CVF同题/八作者/pp37258–37267、链接2603.10990，Bib June2026只支持该会议身份，不当first-public或否认更早稿；所恢复单篇无具名早dated original release。既有准入与DATE3 Mar12日级arXiv夹证有效复用，Submitted/Updated不作公开日，当前题摘唯一v1无可见撤回/纠错。没有扫会议库/作者史。

实际必要原件§1定向probe论证、§3数据/人工锚点、§4 Eq2–7、§5 Eq8–12、§6/完整Tables1–5、§7、Supplement A（完整Tables6/7与pair人口）、C、D及Limitations。只读相关正文/caption，没有图像像素、代码复现或全部图库/旧版diff。

## Source采用资格与直接反侧

- **新增命题可保留**：偏好或语义分数不能签现实风格的色彩目标→对同一真实照片作saturation-scaling定向探针，另以CFG强度制造有序监督、人类色彩目标作锚点→评价应分别验审美/语义/特定色彩目标并冻结标签制造器、条件人口与独立校准，不让own scorer给优化后的输出自行签保真。图1只支持作者所报定向证据，不核曲线精确幅度或生产T2I过饱和唯一训练因果。
- **人口真实但不是全真值**：189490 filtered real photos、12类别，6 CFG variants=7.5/10/15/20/25/30；real最佳、CFG越大rank越差是监督预置，不认证逐例相同语义或客观色彩真值。Table6 train160000真实/1120000总图、test29490/206430；§3约190K/1.33M是全库口径，Supplement“train over1.1M synthetic”不能混入总图口径。Table7类别比例5.3–11.3%，不采“均匀分布”字面保证。人工6690图/超过20000ratings、每图三trained annotators；§3.3 average Spearman>.85是报告的inter-rater consistency，**不是qualification阈值**（已回准备者最小纠正）。人类目标包含sharpness/illumination/saturation/overall color realism，仍是限定感知目标。
- **排序recipe隔离**：Eq6包含j=i项0.5而标签rank1…K，精确rank口径需协调；不因此否定已报告局部经验或编造代码失败。Table4 same dataset/backbone/lr/epochs的pairwise76.2/74.8、visual-only77.1/74.3对full83.6/80.1支持该配方局部比较，不授soft-rank普遍必要。
- **评价结果具名保留**：Table1 SynPairs83.6/RealSyn80.1对HPS57.5/58.3；Table2人类相关Spearman84.9/Pearson85.4/Kendall71.4对HPS74.4/76.0/62.8。Supplement A每subset5000pairs、SynPairs相邻CFG、RealSyn固定最低CFG7.5；§6说random counterpart，二者不能补成同协议。制造标签表现及人类相关均不授全目标objective oracle或跨域绝对可靠。
- **采样新机制不签执行保证**：Eq8 normalized embeddings dot-product/κ经softmax，Eq9文本token平均后归一化/upsample，Eq10以s0[1−λ(1−t/T)a′]调guidance。语义agreement map并未由定义证明为色彩错误定位；§5/C的generated-image具体输入和更新时机未精确给出。每步重算noise不证明每步重跑CFM；不采用闭环定位、精确部署recipe、任意diffusion兼容或免费/no-loss保证。
- **直接反侧与费用**：Table3三模型的FID/CLIP/Δsat/CFM有限方向有效；Δsat参考真实整体平均.33不等每prompt色彩真值，CFM又用于refinement，不是独立放行。Table5 temporal-only18.0/25.9/.18/−1.3明显差于baseline13.3/28.2/.15/4.9；spatial-only13.2/28.2/.12/6.8，full13.0/28.2/.07/6.9。Table3 full FID13.1与Table5 13.0分别保留，不補同配置。H20、one epoch/batch32/lr2e−6、448/τ.1/κ10披露，不授完整CFG扫描/训练搜索/encoder调用、λ选择、steps、端到端时账与SLO；未量化费用保持Not Disclosed。Limitations明确仅CFG制造失真不能代表全部color defects。

## 评分、实际owner与终态

**Source受限通过；2+1+2=5通过。** Design2只给这篇定向目标错配probe/条件评价边界，Reach1仅生成评价组件，Durability2为真实制造标签/人工锚点与优化judge资格；不借成熟CFG/Goodhart原则或会议声望抬分。标准必要审阅并对具体评价反侧定点加深已完成，不改潜力为EX或以已有主题降分。

**具体已有覆盖/Books0通过，限定为本次采用的评价资格，非新实验已被吸收。** 实际顺读唯一owner `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)121–148完整邻接，具体131错误proxy目标、133参考encoder/人口/scorer身份与独立人工锚、135MOS代理非事实概率、137定向反配对制造规则/filter/judge/人类锚及非全部标签真值、139条件对象/归一化/judge校准；这些共同承载所采用的目标分账、标签制造与评价权限，不只是同属“评价”。另577–611完整局部中控制预算非实际总费用、有限样本风险依代表人口/无污染/scorer关系，承载本次费用/外推资格。

新CFM/CFR公式与数字未在现章吸收；由于定位/刷新/精确recipe和普遍fidelity未获此原文支撑，本次不将其当长期执行合同写入Ch24或假装由Ch66主题覆盖它们。采用边界已有真实owner，本次不需要PRE/POST/改书；若未来拟采用独立色彩定位/新采样执行机制，须定点恢复map输入/刷新、held-out独立标签与完整费用，而非全论文证明或全网先稿排除。

本文件只授本ID受限Source/评分/具体NC，不授formal同步、性能或安全保证、DAY；没有共享Books/Report/State/mainledger改动或stage/commit/push。
