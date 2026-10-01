# 2026-04-24 四项传输与评价候选的有限非作者核

复核者 root；核官方精确 v1 的必要方法、评价边界，并对读现有章节。此文仅结清所列四项当前 Books 处置，不代替其余候选、日期与来源 Gate。

## `2604.20923v1` ILDR：几何预警不签发训练完成

[官方 PDF v1 Table 6/9/11](https://arxiv.org/pdf/2604.20923v1)把类间 centroid 距离与类内 scatter 的比值当 grokking 前兆，按固定阈值触发早停或 LR/weight-decay 干预。Table 9 的一个 seed 在触发后只有 7.1% validation accuracy，直接阻止把几何 flag 当成功证书；阈值选择与少数 seeds 还限制迁移。第5章已有“表征几何是诊断，仍需 held-out 行为验收”的 owner 论点。本研究只新增局部测量操作点，维持 2+1+2=5、标准审阅、仅报告；不把节省训练步数外推成通用 wall-clock 收益。

## `2604.20940v1` Sema：语义传输是受限 placement 分支

[官方 §3–5](https://arxiv.org/html/2604.20940v1)在 client 编码为离散 audio/visual codes，并以可访问性文本/OCR 补视觉结构；server 重建后仍交给原模型 encoder，不是任意模型直接读 codes。§4 是组件测量与模拟网络，§5 才讨论端到端 prototype；宽带、编码器质量、codebook 版本和 client 算力都会改变取舍。第23章拥有表示 fidelity，第62章拥有传输和流时序；这项模拟还不足签发默认 placement 或端到端 SLO。维持 2+2+2=6、标准审阅、仅报告。若有真实 agent loop 与丢包/尾时延验收再定点重判。

## `2604.20995v1` Value-Conflict Diagnostics：行为差异不是隐藏意图

[官方 §3–7](https://arxiv.org/html/2604.20995v1)以合成二选一情境、反向 developer policy 和监督/后果标签测 compliance gap；这个条件输出差异并不识别模型的持久价值或战略目的。样本按预调查筛选，scratchpad 自述、PCA direction 与 steering 都受 elicitation 和测量协议制约，不能给自然任务总体发生率。第66章已有 evaluator identity、观测行为与内部动机分离的长期边界。维持 2+2+2=6、深入审阅、仅报告；不把此受限诊断升级为通用 hidden-intent sensor。

## `2604.21016v1` Stochastic Sharpness Gap：理论假设不外推优化器

[官方 §2–5](https://arxiv.org/html/2604.21016v1)以 SGD 的 top-Hessian 方向噪声、cubic restoring force 和局部近似解释平均 sharpness gap；结论依赖平滑、eigengap、噪声及闭合假设。有限网络/CIFAR 试验可支撑该模型条件下的机制候选，不给 Transformer/Adam 普适学习率公式，也不证明泛化。第28章已有训练稳定性需要多种 telemetry、不能以单 proxy 控制更新的主线；此精确理论是受限旁支，维持 2+1+2=5、标准审阅、仅报告。若主线规模及 optimizer 条件获得检验，再对照是否构成长期增量。

四项均未改 Books；本日状态继续进行中。
