# `2609.24788v1` — 双向视频编辑条件迁到因果流

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.24788)、[精确 v1 全文](https://arxiv.org/html/2609.24788v1)，访问 2026-09-23；官方 09-22 New 公告落本窗，09-21 投稿标记不替代公开事件。
- 问题与旧方案：整段双向视频扩散允许 future frame 参与去噪与编辑，质量路径明确但无法在直播时看到未来；从头训练流式编辑模型成本高，也放弃既有编辑控制能力。
- 机制与状态：冻结预训练双向及流式因果 backbone，额外控制分支对源帧使用时间独立的二维 attention，避免未来条件泄漏；双向与因果 feature space 不一致时，以 SVD 识别 backbone 转换的主导更新方向，将控制优化限制到其正交方向。控制分支只负责 edit condition，因果 backbone 负责历史 KV 与输出提交。该正交近似需验证，不能保证任意 backbone 无干扰。
- 评价边界：作者视频编辑任务的单 H100 15 FPS 是该实现和输入设置，未给生产并发或 tail-SLO；零样本迁移依赖具体冻结 backbones、条件任务与对齐质量，帧独立控制可能损害跨帧条件表达。离线质量优先仍可使用双向编辑，真正流式需求若迁移失败仍可能须重训因果版本。
- Books Decision：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 已比较双向扩散与流式提交，但未讲**编辑控制分支**跨两类 backbone 的因果兼容性，已在 diffusion serving 与 scheduling 过渡处补约束、代价和共存。V2 评分 2 + 1 + 2 = 5/9；独立书稿审阅已通过。
