# 04/27 首批独立准入口径校准

2026-09-28；复核者 root。只重新打开下列官方 exact-v1 身份页的完整题摘，检查首批独立工作的误收/漏收风险；不称全文、日期、所有来源或日级 Gate 已完成。重要修订仍须使用本窗 v1 正文，不能沿用后发 v2/v3 摘要。

| 身份 | 仅准入判断 |
| --- | --- |
| [2604.22074v1](https://arxiv.org/abs/2604.22074v1) | 继续：RLVR 提高任务正确率与 reasoning token 的 Causal Importance / Sufficiency 可分离，直接挑战用 outcome reward 当 reasoning faithfulness 的评价合同；后续需核 CIR/SR 操作定义及受限模型/题集。 |
| [2604.22167v1](https://arxiv.org/abs/2604.22167v1) | 继续：通过 unsafe proposal model 的 importance sampling 衡量低概率 harmful output，与只挑危险输入或平均拒答不同；后续核权重支持、方差与风险事件定义。 |
| [2604.22127v1](https://arxiv.org/abs/2604.22127v1) | 继续：sequential / parallel hybrid 两种拓扑下 recurrent backbone LoRA 的正反转，可能改变适配位置选择；后续核预算与任务对照，不从两模型概括全部 hybrid。 |
| [2604.22273v1](https://arxiv.org/abs/2604.22273v1) | 继续但留风险：ECR/EIR 与初始准确率联合决定继续自纠错是否有益的受限 Markov 诊断，不能把单次提示词干预外推成生产控制保证；exact-v1 与后发摘要必须分开。 |
| [2604.22430v1](https://arxiv.org/abs/2604.22430v1) | 暂支持贡献前关闭：MPS/MIG 的一般 GPU 空间共置对照，没有在题摘中隔离大模型训练或推理的负载、KV/collective/租户约束；有限最佳/最差数字不能直接改本书 AI 平台策略。不是因系统会议或 GPU 主题而入选。 |
| [2604.21999v1](https://arxiv.org/abs/2604.21999v1) | **定点重审**：单块 Universal Transformer/Sudoku 虽窄，memory-token 下限/过量 attention dilution 和 ACT 初始化导致提前 halting 的对照可能直接解释深度状态的训练边界。不能仅以 Sudoku/小模型关闭；核实际 Ch5/Ch6/Part II 是否已有该非平凡取舍。 |
| [2604.22128v1](https://arxiv.org/abs/2604.22128v1) | **定点重审**：Dyck 受控实验里 residual probe 可读而 top-of-stack attention 干预显著影响长距正确率，可能新增 probe 与实际使用分离的具体反证。若 Ch5 已有同命题，需要判断新受控条件是否改变证据强度，而非靠章节对应直接收/排。 |
| [2604.22565v1](https://arxiv.org/abs/2604.22565v1) | **定点重审**：冻结 Solver、原上下文不重写，只训练 evidence emphasis actor 标注关键 span，可能改变 RAG/context 的信息保真与预算分工；需核相对压缩/重写的同预算对照，不能由转移宣传直接入选。 |

三项“定点重审”只需标题摘要、当前命题及决定准入的必要对照，不进入全文队列；作者若维持关闭须给具体已覆盖/不改变选择的理由，若恢复仍须 exact-v1 evidence、日期、独立处置及 Books 判断。

作者据此定点对读后回报：21999 恢复为候选（Ch17 的 ACT 初始 halt prior 与 scratch slots 联合校准有窄缺口）；22128 在 Ch66 已有 probe 可读与因果使用分责下具体前闭，不因 Dyck 小任务而一概排除；22565 保留候选，但 Ch75 已有 full-source→span tags→frozen Solver 责任边界，Books 暂为已有覆盖。上述是准入/owner 工作判定，仍需各自的必要 exact-v1 证据和日期、全日日级 Gate，不能由此宣称 04/27 Complete。
