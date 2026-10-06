# 11/14 新方向：训练时稀疏 circuit 校准 ready

作者Planck；不重复首批SIMA2/cyber/API准入。新增原源：[Understanding neural networks through sparse circuits](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/)，官方核心实际读完，raw-web-07；完整论文题摘及身份raw-web-08。Books实际写入0。

## 日期与版本权限

本日新抓官方RSS raw-openai-rss.xml 中该项 `pubDate=Thu, 13 Nov 2025 10:00:00 GMT`，对应BJT13 18:00，完全落窗；网页显示November13 2025。采用权限是发布方RSS的公开事件时间，不是arXiv submitted。该RSS另有GPT5.1API午夜字段，本项不是同一午夜字段，不将二者混用。原HTML请求403已存raw-sparse-blog.html.request.json，403正文不是文章元数据。

当前Read paper链接指向[Weight-sparse transformers have interpretable circuits](https://arxiv.org/abs/2511.13653v1)，v1 submitted=`Mon,17 Nov2025 18:02:06 UTC`。故该精确arXiv版本不能静默当Nov13首次公开正文；只作当前家族身份和全文恢复线索。Nov13原技术稿链接/内容是否相同仍需有限恢复；若采用超出Blog核心的定量/算法细节，必须先解决。没有把这篇论文提前归属或用提交时间替代公开时间。

## 准入命题及评分

事后把dense模型拆出可读feature/circuit，仍受混叠与解释faithfulness限制 → 作者直接在GPT2-like language model训练时约束绝大多数weights为零，再对手工algorithmic tasks剪枝出可运行小circuit → 解释性可作为训练架构的另一设计轴，而不仅是训练后诊断。拟评分 **2+1+2=5**；不是借“因果干预重要”成熟原则计Durability3。

官方核心对照与反侧：固定sparse模型size时增加稀疏度损害capability但提高所定义interpretability；扩大模型size可移动该局部前沿。quote-type例子报告留下小circuit仍能做任务、删除fewedges失败；variable-binding只部分可解释。手工简单任务、小于frontier模型、大部分计算尚未解释、训练效率成本、dense deployment仍更有效率，均是原文直接限制。没有把对这套tasks的最小circuit等同唯一真实算法、开放LLM安全保证或通用稀疏推理加速。训练预算匹配、任务挑选、剪枝评价及不确定性仍是必要后续审阅；没有因Blog未列完整实验配置关闭潜在贡献。

## 具体owner差额与当前Books建议

实际重读项目context/学习方法/写作指南，ROADMAP及Ch4/5/6；Ch5重点定点读177–240行、330–350行。owner=`WORLDVIEW-REPRESENTATION`，[Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)现有“分布式表示与Superposition”实际承载容量/解释难度取舍、“从可读出到机制”承载行为、读出、干预的证据阶梯，后文另有sufficiency/necessity与basis条件。因而不建议重复新增“probe不等causal”原则。

可讨论的真实差额是**把稀疏连接约束放在训练形成表示的阶段**，与现有sparse decomposition这一事后证据手段分开；整合位置若证据成立，是Superposition容量取舍后、证据阶梯前的替代训练分支，保留size/sparsity/capability局部前沿及训练成本。不因本章没有论文名称授长期缺口。当前建议 **暂缓整合、报告可继续**：现有博客足以校准这个新机制方向，但精确原稿的task/剪枝/预算尚未核，不申请root直接写Books。仅报告或现有具体覆盖也可有效。

请root独立核：RSS时间采用权限；Nov17v1与Nov13原报告隔离；这条训练设计增量是否足够准入；方法与反侧支持的最小命题。root可先核单项，不需等本日arXiv集合。

后续状态：以上为初筛时快照。root 已在 [FIRST_INDEPENDENT_REVIEW](FIRST_INDEPENDENT_REVIEW.md) 实际通过日期和准入；Blog 有限命题、当前 owner 具体覆盖与建议差额现交 [SPARSE_EVIDENCE_OWNER_READY](SPARSE_EVIDENCE_OWNER_READY.md)。不再因可选原稿未恢复将整个家族暂缓；超出 Blog 的定量/算法细节仍隔离。共享 Books 尚未写入，最终处置与 POST 待独立协调。
