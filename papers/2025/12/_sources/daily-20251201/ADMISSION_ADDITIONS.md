# 12/01 增补潜在准入与待判断项

观察时间：2026-10-02T17:41:02+08:00。全部完整精确 v1 题摘已打开，均无本窗 first-public 证明；不是确定候选或评分清单。网页当前版本史未见撤回标记，不代表完整版本史核验。

| 原始身份 | 原有约束 → 原文增量 → 可能改变的选择 | 日期与下一证据 |
| --- | --- | --- |
| [SIMPLE 2512.00719v1](https://arxiv.org/abs/2512.00719v1) | TP/PP 的末级采样仍在同步关键路径 → CPU决策面与推理重叠、按序列/批而非词表切分，截断优先和热词表拒绝采样 → 要重新考虑采样执行放置与分布正确性，不能只按GPU算子速度判断。潜在准入，不因摘要缺配置排除；拟实现owner INFER-SCHEDULING，分布语义邻接 MODEL-SAMPLING | submission Nov30 04:15:34 UTC。需原始公开、采样等价性/拒绝纠正、端到端配置及尾延迟证据；摘要吞吐/延迟宣传数字未采用 |
| [VLASH 2512.01031v1](https://arxiv.org/abs/2512.01031v1) | 异步VLA推理期间机器人继续运动，观察与执行时间错位 → 用上一动作块前推执行时状态再预测 → 异步执行不能仅看推理延迟，须检查预测状态误差与反应延迟。潜在准入；拟owner MULTIMODAL-EMBODIED-VLA | submission Nov30 18:59:24 UTC。官方题摘链接 mit-han-lab/vlash；需原始仓库/项目发布日期和精确v1机制、对照与失效条件，不用2026v2 |
| [Catch Me If You Can 2512.00552v1](https://arxiv.org/abs/2512.00552v1) | 答案正确率可掩盖过程关系不一致 → 正反向、传递性、反事实和扰动四轴诊断，Qwen3-0.6B/MenatQA局部反证 → 判断推理质量要区分答案与关系保持。潜在准入；拟owner PLATFORM-EVALUATION-SYSTEM | submission Nov29 16:47:01 UTC。需首公开和协议/分母，不能从一个小模型外推全部 reasoning model“假装推理”；OpenReview后续发表线索不授予首公开 |
| [Advancing Academic Chatbots 2512.00991v1](https://arxiv.org/abs/2512.00991v1) | 文本QA评价不覆盖幻灯片布局/风格 → 原型对读GraphRAG/hybrid、human与LLM judge，摘要报告局部GraphRAG负结果及视觉缺陷 → 可能修正评价或检索选择，但若只有不可比原型排名则不够准入 | submission Nov30 17:25:23 UTC。贡献含糊需定点核心方法与评价协议；不按应用领域直接关闭，尚未决定准入 |

发现为具体主题限定窗口查询，非全类库存。日期不确定不降分或删除贡献；若日期恢复确认窗外，路由真实日期而非复制到12/01。
