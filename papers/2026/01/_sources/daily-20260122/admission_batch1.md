# 新批独立准入请求 1

原题、作者、完整exact-v1摘要与身份历史：[abs_batch1.txt](./abs_batch1.txt)。本表只请求准入校准；日期尚待final-ID上界核验，非已入选池，评分与审阅完成数尚未冻结。小模型或局部反证不因规模关闭；以下每项delta若成立改变的是具体选择。

| arXiv | 原约束 → 原文实际增量 → 改变选择 | 作者准入判断 |
| --- | --- | --- |
| 2601.12033 | 平均精度保持不能代表跨语言安全/公平保持 → 静动态量化差异与critical-weight保护 → 应分别验证跨语言风险而非仅平均task质量 | 继续必要证据，安全边界 |
| 2601.12145 | 固定稀疏阈值随context长度产生更多偶然attention边 → 行极值/长度相关阈值提供恒定伪边界 → 阈值应随长度校准，需保留统计假设 | 准入 |
| 2601.12212 | 固定draft-tree参数不适合变化acceptance状态 → target hidden-state条件的RL树动作及多步持久策略 → draft拓扑可按context预算选择 | 准入 |
| 2601.12430 | VLM yes-bias常归因视觉证据薄弱 → system-prompt attention与因果重分配 → 修正应区分prompt attention竞争与视觉编码问题 | 准入局部反证 |
| 2601.12698 | LLM直接kernel改写成本/随机性高 → 模板级语义重构后配置搜索 → 是否新增长期边界仍不清楚；autotune+template本身成熟 | 定点关键对照再定，不因收益数字准入 |
| 2601.12809 | 空间relation失败常归因layout泛化 → 1D CLIP受控label/layout多样性及position-token梯度干预 → 增加layout数据未必修复关系表示，需保留toy范围 | 准入局部机制 |
| 2601.13020 | continual MoE中router和expert共同漂移 → activation-subspace rank stabilization → 固定capacity应稳定激活子空间而不只单独稳定参数 | 准入 |
| 2601.13345 | occupancy不是GPU能耗/时延的充分配置指标 → PTX静态估计约束搜索Pareto候选 → block配置可先静态筛选但需限定预测误差 | 准入 |
| 2601.13631 | 细粒度KV稀疏性与块I/O不一致 → contiguous访问及跨层预测prefetch → cache压缩要同时优化读放大，不能只数留下token | 准入 |
| 2601.13684 | 每head统一budget忽略时变异质与重复 → 动态head预算、代表状态monitor与异步CPU取回 → offload/pruning预算需要同时衡量变化和冗余 | 准入 |
| 2601.13707 | 双前向contrastive grounding增加decode成本 → 单前向vision-language/language-only attention及正交修正 → 相同校正目标可不必复制前向 | 准入，收益归因待核 |
| 2601.14152 | MCQA prompt顺序通常视为格式选择 → CQO/QOC的causal mask使option无法看到context并产生>14pp差异 → 评价顺序是计算图条件，不能当等价格式 | 准入局部反证 |
| 2601.11865 | 跨tokenizer无法直接对齐teacher/student preference token概率 → char-span对齐及teacher-reference校正 → DPO蒸馏可按公共字符边界对齐但需保持importance条件 | 准入 |
| 2601.12269 | ToM改进常需要后训练 → annealed sequence power MCMC无训练采样替代 → 局部任务可改变inference分布而非模型权重，额外计算须核 | 准入局部替代 |

## 分层代表排除/未决（题摘在同一原文件）

- 2601.11908 PPA：negative constraints前置规划；摘要描述的是成熟proactive-vs-reactive规划recipe，未指出新的失效边界。拟关闭而非因Agent主题关闭；若正文定点显示不可由成熟约束解释的局部机制再重开。
- 2601.11956 DoublyCal：proxy KG证据置信度与black-box reasoning confidence组合；不同信息源联合校准是成熟原则，摘要未显示新增稳定有效性条件。拟关闭，不以owner关联代替贡献。
- 2601.11979 PICL：entropy/semantic confusion触发demo检索；选择性检索与动态ICL组合仍为成熟recipe，摘要未指出改变检索设计判断的证据。拟关闭。
- 2601.12040 PREGU：entropy触发、局部latent soft-search；选择性额外计算组合本身不足；摘要称不同latent-space framework但实际增量含糊，需最小核心决定准入，不能按阅读成本排除。
- 2601.14112 ExpNet：跨task/token learned importance attribution；完整摘要没有改变attribution有效性或开销边界的明确证据。拟关闭，不因单组件局部研究关闭。
- 2601.14327 Layer-adaptive Expert Pruning：摘要有可能机制，但final-ID可能属于下一公告批；先核日期，不能用Jan20 submit或后来的Yuan标题直接列本窗。

根复核请优先核真实增量/排除理由是否相同误因；独立题摘校准通过不替代必要证据审阅。
