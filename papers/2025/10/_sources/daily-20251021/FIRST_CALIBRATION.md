# 2025-10-21 首批准入请求

窗口 BJT 10/20 09:00～10/21 09:00。当前完整题摘独立初筛 66 家族；不是确定首公开家族，尚不评分/采用，作者不自审。

全部拟入选首批：

- DistCA 2510.18121v1：长上下文 attention 平方计算使 colocated DP/PP 不均衡 → 无参数核心 attention 按 token 任务解耦到独立 device pool，并动态 rebatch → 是否要改变训练 stage 放置边界；不能以 512 H200 的数字授普遍优势。
- ReXMoE 2510.17483v1：层内 expert pool 限制容量/组合 → 相邻层复用专家、渐进扩大 routing pool → 固定预算下 expert dimensionality 与路由多样性的关系。
- StreamingThinker 2510.17238 当前 v3：完整输入后才开始 reasoning → 保序 attention/position 及并行 KV → 是否可在信息未齐时合法并行编码/推理；须恢复 v1，当前摘要不得覆盖历史版本。
- SpecAgent 2510.17925 当前 v2：实时检索预算受限且现 benchmark 有未来信息泄漏 → 索引时预取 speculative context、无泄漏评价 → 是否应区分合法预计算和 oracle future context。
- Query augmentation 2510.17139 当前 v3：未控制训练成本的 prompting/RL 比较 → compute-aware 对照及 pseudo-document policy → 是否需修改“RL rewriting 必更优”的选择；负面结果保留，不因新方法/小改动排除。
- SafeSearch 2510.17017 当前 v4：最终拒绝不阻止检索过程 unsafe query → query-level reward 加安全/utility 目标 → 安全验收是否要覆盖中间搜索动作而非只最终输出。

上述 published 字段是 submitted，不是 first-public。外部日期/精确历史版本仍隔离，首包不等 Evidence 通过。必要反侧原版将定点读取。

代表排除：Batch Distillation 18075 是化工数据、MambaX prostate MRI 17529 与 battery 17414 是领域应用；MAPF17382 是非 LLM 路径规划；consumer18155 是营销模拟应用；nightlights21791 是暂缓的遥感数据融合。须抽检这些具体理由，不能按标题词匹配扩大排除。

Google 相册官方核心与 DeepSeek-OCR 完整题摘已本日独立读取，但日期只有标签/提交，暂不算本窗候选；MiMo 路由已按官方标题定点恢复2510.11370v1，必要core/历史版本边界见SCREENING，不以目录10/21赋首公开。等待 root 非作者校准，继续无关初筛/有限来源，不等余下四日。
