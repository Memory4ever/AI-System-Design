# 2025-12-27 非作者复核

复核者：主线程，独立于报告作者 Feynman。
窗口：[2025-12-26T09:00:00+08:00, 2025-12-27T09:00:00+08:00)。

实际阅读 README、SCAN 与 ADMISSION。14 源有限原始邻接按本日比较；62 项查询、失败主题替代和月列表不能冒称当天公告池或唯一候选总数。Seed 双类型、DeepMind 正确历史页与 Alignment 恢复部分不再广泛隔离；未恢复部分仍按源/时段隔离。

## 实际原文检查

独立打开并读完整 exact v1 题摘：[代码依赖](https://arxiv.org/abs/2512.22387v1)、[LoRA replay](https://arxiv.org/abs/2512.22337v1)、[多漏洞](https://arxiv.org/abs/2512.22306v1)、[版权](https://arxiv.org/abs/2512.21871v1)、[分词反证](https://arxiv.org/abs/2512.21933v1)、[scaling 动力学](https://arxiv.org/abs/2512.22088v1)、[Nightjar](https://arxiv.org/abs/2512.22420v1)、[FUSCO](https://arxiv.org/abs/2512.22036v1)、[Agent2World](https://arxiv.org/abs/2512.22336v1)、[Aerial World Model](https://arxiv.org/abs/2512.21887v1)，及下面两项最初关闭材料。Meta AdvGame 的独立完整题摘审阅复用本轮 26 日原文阅读，精确身份、命题未变，不继承 26 日窗口结论。

安全与设计反证保留：clean environment 与 claimed/working/runtime dependency 分开；小量 LoRA 不保证无遗忘；单漏洞检测不等于高密度漏洞；识别 notice 不等于遵从或法律合规；分词统计相关不授因果；kernel 近似不授通用 scaling 定律。未评分或采用安全、性能、理论保证。

Nightjar exact v1 题摘只支持负载适应的 speculative length 与停用；当前摘要新增的 MAB/offload 不冒称早期 v1 实现。FUSCO 的 layout/communication fusion 与端到端倍率分开；Agent2World 的可执行测试仍受测试覆盖约束；预测未来画面不直接授无人机物理安全。必要首公开均未由 Submitted 赋时刻。

## 负侧与误判修正

实际读 [Pick and Spin v1](https://arxiv.org/html/2512.22402v1) 完整题摘与 Orchestration Problem、Framework、Experimental Evaluation 的决定准入部分。框架采用已有加权 score、Little's Law、warm pool/cooldown 与分类器，当前组合和整体指标本身不足形成新增长期机制。其 completion success 与 task correctness 不同，模型列表、指标/公式叙述存在不一致，不能采用统一收益或硬件无关 backend 优劣。保留局部关闭，不把所有组合或兼容修订排除。

独立定点打开 [HiFi-RAG v1](https://arxiv.org/html/2512.22442v1)，实际读 §2–§3.4。原先只据摘要“成熟组合且没有归因”关闭过早：Table2 有渐进组件对照；§3.4 报告 GEPA validation overfit、Checker 定性改善却自动分数下降、agent timeout/cost；§3.3 query rephrase 也会退步。应重开为局部评价/设计反证 potential，不据比赛名次采用普遍优势，也不因日期缺失删除。已向作者交付精确差额，待正式报告及 ADMISSION 同步后才授日级完成。

上述共 12 项 exact v1 完整题摘和 2 项必要核心正文检查不是全 16 项全文验证；普通领域标题排除按 SCAN 样本与理由核验，没有逐项读应用正文。

## 尚待同步

HiFi-RAG 改判与计数同步属普通可执行工作，不是外部缺失。本窗确认候选仍为 0；首公开、历史目录和失败主题原始窗口的终态保留不支持正面证据、Books 或无遗漏断言。恢复条件是对应源历史原始分页或逐 ID 官方首次公告/完全落窗首公开范围，只重开对应材料。

结论：未通过

只剩上述已读证据的正式处置同步；没有 Books 写入后待办。

## 修正后的最终核验

实际重读作者更新的README §1–5、SCAN与ADMISSION：HiFi-RAG已恢复为potential，计数为15潜在/1关闭；必要正文位置、自动评分冲突和validation过拟合均明确保留。原始待同步项已关闭，不重新认证未读附件。日期、历史目录和失败主题仍为具名终态保留，不评分、不正面采用、不进Books；只有对应原始入口/逐ID首公告或完全落窗首公开范围到达才重开。正式metadata和§6由本非作者更新；普通可执行待办0。

复核者：主线程（独立于报告作者 Feynman）。
结论：通过
