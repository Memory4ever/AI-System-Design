# 尾部定点筛选

检查：2026-10-04T08:55:00+08:00。本文件仅保存本日实际读取的筛选理由，不继承其他 Daily / Weekly 的去重或评分。

## Google GIST

[Introducing GIST: The next stage in smart sampling](https://research.google/blog/introducing-gist-the-next-stage-in-smart-sampling/)：官方博客日期 January 23, 2026，未核时区；已读完整核心方法、理论保证、ImageNet 单次采样说明及所链原论文完整题摘。

[GIST: Greedy Independent Set Thresholding for Max-Min Diversification with Submodular Utility](https://arxiv.org/abs/2405.18754v3)：v1 `Wed, 29 May 2024 04:39:24 UTC`；v2 `Mon, 10 Feb 2025 21:17:29 UTC`；v3 `Mon, 20 Oct 2025 13:56:47 UTC`；NeurIPS 2025。原题摘已有联合 monotone-submodular utility 与 min-distance diversity 的目标、threshold 系列独立集的 bicriteria greedy、1/2 approximation、0.5584 hardness、ImageNet single-shot sampling 实验。博客解释的这些贡献与原题摘一致，未读到新增机制、评价条件、修正或安全/纠错信号。关闭的是本次博客增量，不是算法长期价值；未声称以前已经有效审阅或 Books 已有覆盖。不需要为了这个贡献关闭理由追博客精确时刻，不评分、不进入本窗候选。

## Kimi CLI release notes

原源：[MoonshotAI/kimi-cli CHANGELOG](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/CHANGELOG.md)，本次只读 `0.87 (2026-01-25)` 至 `0.84 (2026-01-22)` 的邻接区段；日字段未含时区和小时。v0.87 增加 skills 搜索目录与媒体生成/处理提示，修复 HTML 块渲染和 macOS 图片粘贴；v0.86 修复 binary builds。v0.85 列出落盘粘贴图像、content-hash 去重、历史媒体展示、ReadMediaFile 路径标识、MP4 识别、slash 命令 Ctrl-C、shlex 无效语法、MCP stderr 展示污染，以及连接关闭/Ctrl-C 时 pending requests 的 graceful cleanup。

已读到完整实际变更，不因修复标签关闭。缓存/路径标识是现有持久化与追踪惯例的具体应用；这段 release 没有提供不同设计的约束、兼容性/安全变化、可改变既有判断的验证或新状态/恢复语义。Wire cleanup 不被提升为 exactly-once、重连续跑、取消远端已提交副作用等保证，也没有原文证据指向这些保证发生变化。当前按局部实现变更关闭；若原源新增具体正确性/安全或协议状态改变说明，仅重开受影响项。无需追三个日字段的精确时区来维持明确贡献关闭。

## FUDLR 日期边界

[Towards Fair Large Language Model-based Recommender Systems without Costly Retraining](https://arxiv.org/abs/2601.17492v1)：完整题摘及当前官方版本页已读。v1 `Sat, 24 Jan 2026 15:40:52 UTC`；v2 `Sun, 1 Feb 2026 13:36:40 UTC`，版本变化本身不授重要修订。原文通过 bias-agnostic mask 识别待遗忘样本，再估计/移除其参数影响；这是可能有价值的机制，未以推荐领域或局部实验拒绝。

Submitted 不等于公开。按实际官方周末排程不可能是本窗标准公告批；本次未发现更早独立公开的具体线索。不从提交字段授精确其他 Daily，也不把它列为本窗确定候选。若发现原正文更早公开记录，定点核首公开窗口，再执行贡献与必要证据审阅；本次不采用其公平性/效率主张。
