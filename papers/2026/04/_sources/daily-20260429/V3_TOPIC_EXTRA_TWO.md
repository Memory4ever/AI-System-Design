# 04/29 arXiv 主题查漏的两个额外完整题摘

本批两篇均在本日官方 arXiv 公告窄 ID 链内，由 `cs.AI` 安全／多模态主题标题补检发现，不在旧 446 代理库存或旧 retained60 中。已读官方 exact-v1 的完整标题、摘要；对 `24983` 只为判明威胁模型再定点读 §4.1 算法输入/输出，不继续全附件。此处是作者侧贡献初筛，不把 v1 submitted/DOI created 独自当首公开，不计正式候选、分数或 Books。

| 身份 | 作者侧处理 | 必须保留的接口与证据边界 |
| --- | --- | --- |
| [2604.24983v1 Adaptive Prompt Embedding Optimization for LLM Jailbreaking](https://arxiv.org/html/2604.24983v1) | **潜在安全审阅**：相对附加离散 suffix，直接优化原 prompt token 的连续 embeddings 是新的白盒攻击面；即使 nearest-token projection 保留原可见字符串，模型实际消费的 `E*` 仍改变，因此文本检查与 embedding-level input check 不是同一防线。 | §4.1 Algorithm 1 输入 token 序列与目标 continuation、迭代优化 `E`，返回的是**优化后的 embedding**，不是可向普通 text-only API 直接发送的原字符串；若只发送投影后未变化的 token，不能推有同等效果。“prompt 表面隐形”只在攻击者能把 `E*` 注入模型输入的白盒路径成立，不证明一般用户消息具此权限。后续核 ASR-Judge 与 matched attack budget、Ch72 的模型输入信任边界，再定是否足以留在项目候选。 |
| [2604.24987v1 Assessing Y-Axis Influence](https://arxiv.org/abs/2604.24987v1) | **具名前关闭**：五个多模态模型的 chart-to-table 任务上，y-axis 主刻度位数、数量、范围、数值格式和 legend 数量影响结果，额外提示 y-axis 信息能提高部分模型表现；这揭示该任务的数据分布/格式敏感性，但题摘没有把已知的图表编码切片原则改成新的视觉表示、评价权责或发布保证。 | 关闭不是因“只一任务”硬拒，而是相对本书已需按输入可见证据、格式和任务切片评价的现有约束，这组局部指标未给非同义机制或反向结论。若必要原文对同等数值信息但不同 y-axis 绘制做受控反证，改变 Ch23/66 的具体证据条件，再定点重开；不把提示改善解释成模型内部数值理解已修复。 |

本批 `1 潜在＋1 具名前闭`。按已具名且不重复的身份，作者侧**最小**完整题摘集合由 `104＝73＋31` 暂增为 `106＝74 潜在＋32 具名前闭`，另两个机构事件潜在；来源、日期、准入复核和正式 denominator 仍未冻结。
