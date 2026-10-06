# 首批准入校准请求 — 2025-07-11

来源为独立运行的 arXiv API 主题查询。完整原始题摘在 `discovery.json` 及 `model.raw`、`systems.raw`、`multimodal.raw`；`published` 是提交字段，不当作公开时间。目前只作拟选，待官方公告日期确认，不先宣称落窗。未拿旧 Weekly/Daily 候选反推。

## 拟选

- [2507.07400v1](https://arxiv.org/abs/2507.07400v1)，KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows。完整题摘位于 `discovery.json` systems/agents 同 ID（仅一个家族）。旧约束：LRU 不能预见 workflow 后续执行，会逐出即将重用的 prefix KV；原文增量：Agent Step Graph 的 steps-to-execution 驱动 KV-node eviction，next-step CPU→GPU prefetch；可能改变的选择：已知 workflow 控制流可用于 cache policy，而非仅以 recency 管理。机制准入，不用 speedup 独立准入。拟 owner INFER-KV-CACHE，交接 AGENT-WORKFLOW。
- [2507.07562v1](https://arxiv.org/abs/2507.07562v1)，The Synergy Dilemma of Long-CoT SFT and RL: Investigating Post-Training Techniques for Reasoning VLMs。完整题摘位于 `discovery.json` multimodal 同 ID。原约束：语言模型中 SFT→RL 常被期待协同；原文增量：不同难度、回答长度的取舍及多种组合策略未叠加的负结果；可能改变的选择：VLM 后训练不能仅因语言模型的经验默认叠加收益。局部负结果值得证据核验，不因不是新框架排除。拟 owner TRAIN-SFT，交接 TRAIN-GRPO/MULTIMODAL-REPRESENTATION。

## 代表关闭

- [2507.07201v1](https://arxiv.org/abs/2507.07201v1)，MODA: A Unified 3D Diffusion Framework for Multi-Task Target-Aware Molecular Generation。标题明确分子生成/药物领域，AI for Science 当前暂缓；不以 diffusion 一词映射 Ch24 重新引入。

## 未决而不硬关

- 2507.08045 Krul 的当前 API 是 v2；机制有潜在贡献，但 v1 和公开日期尚未核得，不能将当前摘要当作当窗精确版本。定点恢复，不缩池。
- 2507.07223 通信/分离式内存报告：摘要提出 CXL-over-XLink 与层级内存，不能仅以“硬件综述”关闭；需要正文确认实际新证据和适用边界。

请 root 独立检查：入口是否过宽；两项拟选准入链是否成立；Science 关闭理由；当前版本/日期未决隔离是否恰当。公开日期与正文在后续批次审。
