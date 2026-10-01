# `2609.24976v1` — 触觉由即时条件进入预测环境状态

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.24976)、[精确 v1 全文](https://arxiv.org/html/2609.24976v1)，访问 2026-09-23；官方 09-22 New 公告落入本窗，09-21 投稿标记不单独证明公开。
- 问题与旧方案：视觉 world model + 当前触觉 policy 能在短时接触或触觉足够直接时工作；灵巧手多指接触、遮挡和滑移让动作后果依赖未显式预测的接触演化。
- 机制与状态：各指视觉触觉编码、指身份和手部姿态进入压缩器，触觉 latent 与视频扩散模型共同预测 future contact；action expert 读取预测特征而非只读当前触觉。sensor calibration/timestamp、hand embodiment、压缩映射与 action chunk 属共同 state identity；物理执行及安全回退仍由 controller 拥有。
- 评价合同：六项 Sharpa 视觉触觉手的接触密集任务整体 70.6 对 38.0 的最强异构 baseline 不能独立归因机制；四项同输入/同 expert/同数据/同动作空间的去掉触觉 world modeling 消融为 74.7 对 26.6，支持该系统内预测作用。单 RTX 4090 的 363.0→281.6 ms/chunk 是披露设置，不能当生产 SLO。约 100 个成功示范每任务、未测失败恢复或其他 sensor physics，不能声称通用机器人收益。
- Books Decision：`MULTIMODAL-WORLD-MODELS` Ch25 已将触觉设为独立 provenance，但尚未区分当前 tactile conditioning 与预测 contact evolution；已在触觉段之后补条件分支、代价与旧路共存。V2 评分 2 + 2 + 2 = 6/9；独立写后复核通过。
