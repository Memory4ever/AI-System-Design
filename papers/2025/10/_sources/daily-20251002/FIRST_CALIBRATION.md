# 2025-10-02 首批准入小包（作者，待 root 独立校准）

窗口：2025-10-01T09:00:00+08:00 ～ 2025-10-02T09:00:00+08:00。
正文权限：完整 v1 题摘实际读取；以下不是 Evidence 完成，也不是已确证当窗候选。
原件：[精确 v1 Atom](exact-v1.raw)；查询参数、执行时间与响应身份见 [receipt](exact-v1.receipt.json)。

| 身份 | 原有约束 → 实际潜力 → 可能改变的选择 | 处置 / 校准请求 |
| --- | --- | --- |
| [GUI-KV 2510.00536v1](https://arxiv.org/abs/2510.00536v1) | 图像历史缓存预算紧张 → 空间 saliency 与跨帧 key 子空间冗余评分，且观察 GUI 各层高稀疏 → GUI 负载能否采用统一层预算，而不照搬自然图像方案 | 潜力；当前尚缺官方 first-public 落窗依据。不得照录 FLOPs/准确率为已验证收益。拟 owner INFER-KV-CACHE，交接 MULTIMODAL-REPRESENTATION。 |
| [PAL-UI 2510.00413v1](https://arxiv.org/abs/2510.00413v1) | 摘要/截断丢失后续所需视觉细节 → 双层摘要加可回取原截图的工具，8.6K 训练样本 → 以主动视觉历史检索替代不可逆纯摘要 | 潜力；日期隔离。拟 owner AGENT-MEMORY，交接 AGENT-CONTEXT/PLANNING；不把通用检索原理算新增。 |
| [M2PO 2510.01161v1](https://arxiv.org/abs/2510.01161v1) | 异步 RL rollout staleness 导致训练崩溃 → 限制 importance weights 的二阶矩，仅抑制极端离群权重 → 调整 off-policy 更新而不全量废弃陈旧数据 | 潜力；日期隔离。拟 owner TRAIN-PPO，交接 TRAIN-GRPO/分布式执行；256-update 数字仅作者摘要，未核 core。 |
| [The Transformer Cookbook 2510.00368v1](https://arxiv.org/abs/2510.00368v1) | 参数编码算法文献分散 → 整理已有算术和路由 construction recipes → 提供阅读参考 | 本次贡献排除：题摘明确为已知构造的统一整理，没有具体新假设、反证或设计边界；不因“理论”排除，独立复核可指定新增 construction 作为重开依据。 |
| [Priming Vulnerability 2510.00565v1](https://arxiv.org/abs/2510.00565v1) | DLM 安全不能只沿用 AR 输出评估 → 中间 denoising step 肯定 token 注入可改变后续轨迹，训练污染中间态防御 → 重新考虑中间态威胁模型 | 安全潜力；即使日期隔离也要有限核关键原 core，不能作为无增量关闭。 |
| [Exposing the Cracks 2510.00829v1](https://arxiv.org/abs/2510.00829v1) | reasoning 被认为能抵抗检索噪声 → 低资源 idiom 翻译更易受噪声损伤，LRM 可能 rationalize 错上下文 → 需区分 clean/noisy 质量代价 | 反侧潜力；不得因局部翻译负载、小模型或 RAG 已有主题而排除。日期隔离。 |

独立校准者：待 root 分配。未收到校准前，不开展这些项的正面 Evidence/Books 采用。
继续本日无关初筛和必要安全/反侧有限 core，不等待 root。
