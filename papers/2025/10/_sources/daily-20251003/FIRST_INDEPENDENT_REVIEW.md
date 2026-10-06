# 2025-10-03 首批独立复核

复核者：root / Codex，非作者Huygens。fresh加载本日合同、来源使用说明/每日/arXiv、Prompt、ROADMAP与10月checkpoint，只加载本日材料。窗口 `[2025-10-02T09:00:00+08:00,2025-10-03T09:00:00+08:00)`。

**首批贡献校准及日期隔离通过，不是日级完成。** 实际核五个精确v1原始完整题摘与版本历史：

- [TetriServe](https://arxiv.org/abs/2510.01565v1)：逐denoising step调整sequence parallel度与round packing，面向混合分辨率/期限；不是一般Agent调度，也没有授摘要性能结论。
- [KVComm](https://arxiv.org/abs/2510.03346v1)：按attention importance/Gaussian prior选择层间KV通信介质，与普通相同prefix复用不同；模型匹配/转换与开销效果还需相应证据。
- [AsyPPO](https://arxiv.org/abs/2510.01656v1)：不相交prompt shards的mini-critics及不确定性筛选更新；Asymmetric不是异步策略或stale rollout。
- [Reasoning Boundary Paradox](https://arxiv.org/abs/2510.02230v1)：on-policy取样下负干扰/强者更强，单样本质量与多次覆盖需分开；小模型/局部反侧有贡献潜力，pass256具体结果留待必要评价核验。
- [ToolTweak](https://arxiv.org/abs/2510.02554v1)：provider可改name/description造成选择偏置；摘要选择率不能变成恶意动作成功率，必要威胁/评价反侧仍需审。

提交记录均为10/02，但不能推出首次公开落窗；也不据v2/v3/v4覆盖历史v1。没有评分、正面Evidence或Books权限。原请求范围是本日四主题和有限相关标题导航，不要求全部分类/月/年库存逐项关闭。

代表排除实际核完整题摘：[ImageNet-Think v1](https://arxiv.org/abs/2510.01582v1)是两个teacher的thinking-answer资源，题摘无新的机制/评价反证；[AccurateRAG v1](https://arxiv.org/abs/2510.02243v1)原abs网页失败后实际读作者保存的原官方[exact-v1 Atom](exact-v1.raw)，是处理/微调/评价pipeline与局部QA收益，未辨识新增选择边界；[IoDResearch v1](https://arxiv.org/abs/2510.01553v1)网页失败后实际下载读[原件](ROOT-2510.01553v1.html)，核心目标是私有科学数据FAIR化和科学发现，暂缓范围不能借通用RAG/Agent owner绕过。

这些是三个具名样本，不是全部排除/94题摘已独立复核。其余必要安全/设计反侧核心、官方根因公开时间和十四有限来源仍需日级非作者验收。复核者未读23份核心或授全部原文完成；已有作者原件与边界便于后续只审必要内容。准入为0的日期隔离不等已有覆盖、无事件或无遗漏，不制造Books变化。作者可同步FIRST有效并继续下一日，不必等待整月；DAY通过之前日报保持进行中。
