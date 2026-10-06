# 2025-10-23 首批准入校准包

作者 Cicero，非独立复核。仅 `[2025-10-22T09:00:00+08:00,2025-10-23T09:00:00+08:00)`。本日 fresh 当前合同、ROADMAP 与最新路由已实读；四组主题各页0/max80，提交发现带 UTC10/22 00:00～10/23 00:59，不证明公开时刻。21当前完整题摘，加CL身份带2510.19000～21500前15标题中13相关/含糊题摘及Seed3D题摘，共35家族；月目录不作全文队列。初包32为较早阶段，新增三份见arxiv_supp2.raw，未扩大标题停止位置。

较早包以当前题摘提出潜力；现root FIRST已实际核以下六精确v1，贡献/版本校准通过，不授首公开、评分或正面Evidence。当前版本原件仍保留，不倒灌历史贡献。原件见FETCH.json / supplement.raw，独立实际范围见FIRST_INDEPENDENT_REVIEW.md。

| 家族 | 具体潜在增量 |
| --- | --- |
| [RLBoost 2510.19225](https://arxiv.org/abs/2510.19225) current v3 | rollout与训练资源不同→可抢占rollout资源、pull权重与token级迁移→需核预占恢复和吞吐/成本是否改变资源选择，不把stateless宣传当无损保证 |
| [AdaSPEC 2510.19779](https://arxiv.org/abs/2510.19779) v1 | 全token KL不等接受率目标→参考模型过滤难token蒸馏→需核小draft容量下接受率/质量/端到端差额 |
| [Semantic World Models 2510.19818](https://arxiv.org/abs/2510.19818) v1 | 像素重建目标与规划不一致→预测未来任务语义VQA→可能改变world state表示与规划监督选择 |
| [MoE-Prism 2510.19366v1](https://arxiv.org/abs/2510.19366v1) | expert粗粒度与请求QoS约束→offline neuron partition与online QoS scheduling→可能改变分区粒度/异质请求执行取舍；不沿用current v2的k-aware描述 |
| [CAB 2510.19266](https://arxiv.org/abs/2510.19266) current v4 | 跨架构仅输出蒸馏不足→attention bridge对齐token中间表征与Mamba投影→需核低监督迁移/推理开销边界 |
| [Reflective memory 2510.19897](https://arxiv.org/abs/2510.19897) current v3 | 标签RAG缺任务指导→实例批评/语义记忆及suggestibility差异→可能改变不更新参数的适应条件，不能把后续v3效果授v1 |

四个arXiv分层排除：19986宗教木刻Iconclass使用LLM/RAG改领域分类，未新增检索机制；19364ProTerrain为地形参数相关不确定性与物理轨迹预测，不涉及foundation/world-learning机制；19577gem5 co-pilot为DSE领域DSL/数据库与成本区间搜索，未建立改变LLM执行机制或AI计算设计的证据；19030 Re:Member为三帧采样/WhisperX/情绪语音模块的L2互动probe，未新增memory representation或适应机制。root已实际完整题摘抽检前三项3/4，第四未称独立重读。Google Earth AI另属机构公告，核心遥感/人口/灾害模型融合与专用工具编排按AI for Science边界关闭，不计这四项分母。不得把局部、负面、小模型潜力一概排除。

必要反侧另定点读动态过拒、知识冲突、工具评价、重复终止、合成数据预算、抢占恢复及CUDA代码隐私。日期缺段仍只隔离，不误称无贡献；作者可继续无关初筛，不等待本包，但正面采用必须先校准。
