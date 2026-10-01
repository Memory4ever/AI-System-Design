# `2609.22894v1` — Coreset 节省须计入扫描与训练总时间

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.22894)、[精确 v1 全文](https://arxiv.org/html/2609.22894v1)，访问 2026-09-23；官方 09-22 New 公告落入本窗；v1 内的 09-19 投稿标记不证明更早公开。
- 问题与旧方案：固定子集比例下比较 top-1 accuracy 有利于隔离选择质量，适合研究算法本身；但“训练更少样本”不能在系统预算里免除选择前必须扫描、算特征和排名的时间。
- 机制与状态：评估 owner 将 selector 的固定全量扫描、选取、下游训练放进同一 wall-clock 预算，并与分层随机/全数据压缩 schedule 对比。subset identity、选择器实现、数据/模型/seed、schedule 和复用次数是实验合同；只有复用时才能摊销前置选择成本。训练 owner 仍选择是否使用 subset，selector score 不直接拥有验证权。
- 证据边界：作者的 CIFAR-10、Tiny ImageNet、ImageNet-1K 等图像分类、ResNet-18 为主、部分 ViT-Tiny/ResNet-50，三 seed 主格；ImageNet 搜索部分单 seed，绝对准确率使用 test peak 且无独立 validation，不能把“复杂选择无效”推广为 LLM、动态剪枝或数据蒸馏结论。论文披露并更正 35 项 Tiny ImageNet batch-size 缺陷，结果以修订后的 exact-v1 为准。
- Books Decision：`TRAIN-DATA` Ch27 原讨论 recipe search 的额外训练与 probe 成本，但缺少一次性全量扫描与完整训练同预算的判据，已在该论证之后补充旧方法共存与适用范围。V2 评分 2 + 2 + 2 = 6/9；写后独立复核通过。
