# 2026-04-24：HAT-VTR 的准入与日期反查

复核日：2026-09-29；独立复核者 root。原题摘回放收据已将 `2604.20851` 判为 `pre-denominator closure`，但后续正式日报误将它列为 5 分“仅报告”。本次重新打开[arXiv exact-v1 正文](https://arxiv.org/html/2604.20851v1)、[官方版本页](https://arxiv.org/abs/2604.20851)及[ICLR 正式出版页](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ed9f00cb7dd5fbdc2175d55e2fdf1b05-Abstract-Conference.html)，只复核决定本项目准入与日报归属的必要信息。

- 问题、机制、边界：这项工作评估视频—文本检索在视频扰动下的 query shift，并用最近 query–gallery score memory 调整排序、用 LN 测试时更新改善视频检索。作者也报告部分低 hubness 场景中直接 rerank 可与训练相当或更好。这是视频检索领域的受限 operating point；未提供改变本项目 LLM 检索证据身份、RAG 答案支持、模型生命周期或 AI Infra 决策的可迁移新合同。不能仅因 Ch76 有检索章节、或出现 memory/robustness 术语而准入。
- 日期：官方版本页显示 v1 `Submitted 2026-02-15T05:57:44Z`，但 2604 ID 与本日 OAI/处理记录指向较晚的 arXiv 批次；Submitted 不是 first-public。ICLR 正式出版页证实同一家族的会议版本，尚无可用的逐时公开日志。因此不把 2 月 Submitted 或 4 月 OAI 元数据冒充首发时刻，也不把它硬记为本日新候选。若未来需追该领域，须另核 OpenReview/会议版本的早期可得时间。
- 处置：保留原必要方法、限制与非作者审读证据，但正式日报中转为具名前分母关闭；不评分、不作“仅报告”候选、不进入 Books。重开条件是出现与本书大模型检索或平台评价合同直接相连、且相对既有 Ch76 命题有明确设计差异的证据；单独重发或引用量不够。

这是单族纠错，不自动把其它视频/检索候选一并关闭。原来源回放收据保留其先前 `closure` 判断；本笔记解释为何正式稿应与之统一。
