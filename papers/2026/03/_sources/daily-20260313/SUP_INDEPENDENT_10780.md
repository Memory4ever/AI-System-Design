# 10780：分组退化reference必要Source/owner/PRE独核

复核者：mar13_admission_review，非准备者、非Books writer。仅2026-03-13补充Mar12北京时间自然日，AGENTS/current合同与本日停点已恢复；完整题摘准入与Mar12 arXiv事件日独核复用，不由CVPR接受信号或Submitted制造新的公开日期结论。不扩来源、旧版、全图或全文proof，不授DAY。

## 实际原件与范围

实际读[准备包](./SUP_EVIDENCE_10780_HANDOFF.md)，回[精确v1官方HTML](./SUP_HANDOFF7_SOURCE_10780.raw)及提取文本：§3–5 Eq2–11、§6 Tables1–4全部主对照/§6.3.1–4直接消融及结论；AppB必要Algorithm2与ProcessToken代码局部；C.1实际metric定义及C.3模型参数/FLUX配置。不是摘要或准备者判断替代原证。身份为 *Guiding Diffusion Models with Semantically Degraded Conditions*，Shilong Han、Yuming Zhang、Hongxia Wang，arXiv2603.10780v1；[GET结果](./SUP_HANDOFF7_FETCH_RESULT.json)对应https://arxiv.org/html/2603.10780v1，200/517252 bytes，2026-10-10T04:33:38.138082Z。实际复读[完整精确abs](./SUP_ABS3_10780.txt)的身份、题摘与Comments/history；不授所有版本“无纠错”全网保证。

实际顺读[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)265–313对应完整局部，truncated输出中的Sparse Guidance/EMA部分另取280–301恢复完整。还实际核Ch23表示identity入口与Ch25 World Model入口，唯一owner为ROADMAP的`MULTIMODAL-GENERATIVE-PARADIGMS`，不把encoded-condition存在误说为world state，也不新增结构。没有目视Fig2/5/6所有图像，不采用未核曲线幅度。

## 方法与采用资格

Eq5仍是`D(c)+(w−1)[D(c)−D(c_deg)]`两支差分，不是新增外推定律。实际新增是负条件的保留范围：encoded text positions分成content与context-aggregating（受测padding/special）两组，R∈[0,2]通过Eq9映射为`r_content=min(R,1)`、`r_context=max(R−1,0)`；组内按rank选择替换数。Eq10–11保留原位置，选中状态用对应empty-branch状态混合替换，不删sequence或让所有条件全空。R=1只退化全部content、保留聚合组，因此无需组内重要性排名。

非边界预算可从指定denoiser block的attention关系计算排名；主文允许first-step mask缓存复用，Algorithm2明确首次CalculateImportance、后续ProcessToken与两支求值。不是每步语义实时重判，也不是仅在静态text encoder重新生成无条件prompt。AppB正文/伪码与代码中的mask为keep/degrade互补约定；没有据此认证唯一逐行可执行实现，未运行代码或核部署接口。两段PRE不采用这项执行保证。

Eq6 principal-angle和Eq7 projected-energy诊断所依赖的是跨COCO prompt预测的SVD近似子空间，不是已经获知真实data manifold法空间；近正交与common-mode解释不提供任意迭代无干扰、语义保真或law保持证明。受限分组实现和直接消融可独立于该强几何解释采用。

## 全部主对照与直接反侧

主评价5000 COCO2017 captions及GenAI-Bench，SD3/3.5、FLUX1、QwenImage。实际完整Table1–2支持有限多项改善，但Qwen Aesthetic2.54低于CFG2.57，FLUX收益较小，不能授全质量支配、通用精准语义或所有模型泛化。C.1 CLIP为ViT-B32，Aesthetic为predictor，VQA是clip-flant5-xxl在固定yes/no模板下的yes概率，不是独立composition/事实真值。

Table3固定R=1.1：stratified WPR的FID33.89/CLIP31.98/Aesthetic5.68/VQA92.21，与stratified random的34.17/32.02/5.68/92.27接近，后者部分指标更好；不分组与reverse/random主行退步只支持此人口中的分组选择，不证明PageRank是必要模块或新理论。CFG*改用退化条件作正支、CLIP代理下降只支持剩余条件改变，不能唯一识别语义分量。

实际Table4也是R=1.1/SD3/block1：CFG5.456s、first-step CDG5.655s（+3.6%）、每步WPR8.031s（+47.2%）。不能贴给默认R=1、所有模型或完整SLO；R1跳过WPR也仍有原两denoiser支、empty-state/hook/调参与生成费用。C.3 SD3.5用block2而SD3/FLUX用block1，各scale不同；FLUX512²/28steps不是原1024²/50steps配置，PAG/SEG关闭CFG以各自scale比较，不冒认所有方法同调用人口。

## 评分、真实差额与PRE裁决

**2+1+2=5成立**：同一prompt的content/context-aggregating分组退化负条件接口与局部分组反证为新增（2）；有限backbone/代理评价负载（1）；条件布局、替换预算与排名/缓存/求值费用的稳定分责可复用（2）。不借CFG、SVD、PageRank成熟方法或强manifold宣传加分。

实际Ch24已承载capacity gap、velocity EMA历史、MMD参考人口、安全keyword/prototype和pooled modulation；这些既有论点没有直接承载同一条件内部先content、后聚合状态的保留范围。故此处有真实长期gap，不因都叫guidance便NC。拟在Sparse Guidance完整段后/velocity EMA完整两段前，保留capacity与history两种旧reference的合理性。

**准备包逐字两段PRE通过，无必改机制句。** 第一段准确分组empty状态替换、默认边界无需排名、其他预算指定denoiser层attention且可复用首步排名；第二段准确隔离SVD子空间proxy、WPR非必要、质量反退与费用/退化布局兼容及保守回退。没有自签真实manifold、语义无损、取消全部训练unconditional接口或通用免费SLO。源链接/marker与spacing规范可由writer按既有格式补，不改采用命题。

结论：受限Source、5分、actual唯一owner差额与两段PRE通过，支持受限整合；尚未实际写入，不能授POST或Books完成。仅本人独核文件，不共享写，不stage、commit、push。
