# 2025-11-05 有限补检增量校准ready

作者Carver，窗口BJT `[2025-11-04T09:00:00+08:00,2025-11-05T09:00:00+08:00)`。首批Anthropic/Suncatcher见FIRST_CALIBRATION_READY，不继承04判断。仅有限主题线索回10篇精确v1完整题摘；DDCL范围有歧义另定点Introduction/Preliminaries，没有展开其他论文方法/附件。当前均未证明论文首公开完全落窗，不评分、不计确定候选；请root可先校准具体机制/代表性关闭，日期层独立推进。

原记录：[六篇精确题摘](RAW_SIX_EXACT_V1.json)、[RAG完整题摘/月标题查漏](RAW_RAG_AB_TITLE_CHECK.json)、[四篇原页及DDCL定点](RAW_FOUR_EXACT_AB_DDCL_POINT.json)、[三个完整题摘最终](RAW_THREE_FULL_AB_FINAL.json)。辅助索引标题与ID错位已纠正，以原源为准：Simia=01824、Context=01805、RLAC=01758、DDCL=01554、SmartMLOps=01850；不把错位索引摘要作为证据。原生成记录曾有shell引用错误，已从未变工具原返回完整重存并JSON解析校验；这是已修普通保存错误，不是原源故障。

## 潜在贡献，尚未日期准入

| 精确家族 | 具体原增量与独立核验点 | 原submission，不是public |
| --- | --- | --- |
| [Simulating Environments with Reasoning Models for Agent Training](https://arxiv.org/abs/2511.01824v1) | 实作环境/API工程重且脆弱 → Simia-SFT从小seed合成轨迹、Simia-RL由LLM模拟环境反馈 → 训练环境可用性与反馈真实性的替代边界；需核模拟器输入权限、real-env验证、训练/搜索预算和泄漏，不能由超GPT-4o宣传授真实环境普适性。 | 2025-11-03T18:29:57Z |
| [Accumulating Context Changes the Beliefs of Language Models](https://arxiv.org/abs/2511.01805v1) | 长上下文/自主文本积累不仅增知识 → talking/reading改变stated belief并有tool-choice关联 → 会话/记忆管理需要考虑行为漂移；不是把“belief”当意识或固定安全失效概率。需核prompt/人口/对照、tool-task代理与因果。当前v2 submitted11/04不证明重要修订，需具体变更才重开版本层。 | v1=2025-11-03T18:05:57Z；v2=11/04T17:41:28Z |
| [RLAC](https://arxiv.org/abs/2511.01758v1) | 开放生成的rubric多且组合prompt-dependent → critic动态找可能失败点、external validator核并联合优化generator/critic → 可能改变验证预算与reward设计；external validator不被critic替代，需核game/validator可靠性、固定critic与全量验证预算对照，不由摘要授更少验证必然同质量。 | 2025-11-03T17:15:05Z |
| [RAGSmith](https://arxiv.org/abs/2511.01386v1) | 模块独立调优忽略交互 → genetic full-pipeline search与joint retrieval/generation objective → 具体任务混合与组合选择条件可能修正配置判断。请核是否仅成熟模块recipe，或真实搜索/条件负侧有增量；compression从未选中不是普遍无效，+3.8%与0.2%空间不是已核成本收益。 | 2025-11-03T09:36:27Z |
| [Efficient Test-Time RAG](https://arxiv.org/abs/2511.01059v1) | 全响应投票有decode成本 → partial generation用于semantic consensus与majority vote → 前缀长度/候选数的质量-计算边界；需核是否前缀足以保持投票与完整答案质量、检索/生成成本，不按三任务提升照录。 | 2025-11-02T19:32:39Z |
| [Beyond Single Embeddings / AMER](https://arxiv.org/abs/2511.02770v1) | 单query vector难覆盖分离目标模态 → autoregressive多query embeddings → 目标间距离下的表示/召回限制；需核匹配训练、独立向量/多query对照与生成/检索预算。4x只synthetic，不外推LLM最终质量或延迟。 | 2025-11-04T17:57:20Z |
| [XR-1](https://arxiv.org/abs/2511.02776v1) | 高维观察到低层动作/跨embodiment差额 → dual-branch VQ-VAE的Unified Vision-Motion Codes与三段训练 → joint表示相对单模态latent可能改变迁移。需核表示/规模归因、action误差与异质数据条件；14000rollouts不授安全/所有机器人泛化。当前v2/v3为2026，不替代v1。 | 2025-11-04T17:59:12Z |
| [Cache Mechanism for Agent RAG / ARC](https://arxiv.org/abs/2511.02919v1) | per-agent corpus cache更新不足 → 历史query distribution与embedding geometry联合维护小cache → 工作负载漂移与召回/存储/延迟取舍；需核更新/回退、分布变化及等质量对照。0.015%存储与80%检索延迟不是端到端Agent收益。 | 2025-11-04T19:02:29Z |

以上8个方向当前原页未显示撤回/纠错说明，未遍历完整版本史；不授深审完成。

## 范围歧义与代表性关闭

- [Learning what to say and how precisely / DDCL 2511.01554v1](https://arxiv.org/abs/2511.01554v1)：完整题摘与HTML Introduction/Preliminaries实际读。原增量是可学习离散通信扩展至unbounded/signed signals，非仅通信gate；共享随机量重参数化与可微bit-cost可以涉及learned representation的训练/通信边界。但实证对象是一般MARL合作策略，不能只因Transformer/Agent关键词重命名为LLM-agent机制或GPU collective压缩。请root核有无直接支持当前主线的知识链，若只有系统类比则范围关闭；不因小模型或不是LLM名字自动排除理论机制。submitted=2025-11-03T13:16:57Z，日期未核。此项不预授结构候选/评分。
- [SmartMLOps Studio 2511.01850v1](https://arxiv.org/abs/2511.01850v1)：完整题摘实际读，拟贡献关闭。LLM代码/调试/配置助手与data validation、feature store、drift、retrain、CI/CD集成在IDE，UCI Adult/M5原型时间/复现率/漂移率改善；未给新的执行/状态/权限机制或可归因机制的有效条件。不是标题范围外，也不因原型小排除；摘要的百分比与“new paradigm”不足以改变设计解释。没有所见纠错/安全标记，submission=2025-11-03T18:56:59Z不当public，日期未确认不影响贡献关闭，不另开日期请求。

## 日期与普通停点

## 17:08增量：系统相关标题补检

有效DC月skip0/show25本日native200，338总条目仅读25标题作查漏，停next25。定点4篇exact-v1完整题摘见[原返回](RAW_SYSTEM_TITLE_EXACT_AB.json)，未看方法或附件，尚未证落窗，不评分、不增确定候选。请root与前8方向一起校准：

- [AReaL-Hex 2511.00796v1](https://arxiv.org/abs/2511.00796v1)：异构GPU下rollout的HBM与训练compute需求不一致，MILP策略/负载搜索加图分区共同选择硬件/互连并限制staleness；不是只把成熟异步RL改名。需核等预算、同步成本和训练质量边界，摘要1.50x/1.46x不是已核性能。
- [FREESH 2511.00807v1](https://arxiv.org/abs/2511.00807v1)：地域/时段碳强度与GPU功率吞吐异质，联合并行/路由、DVFS及LLF形成SLO/公平/资源取舍；需核长度预测、跨地域成本、1小时trace及切换损失，不能由百分比授生产泛化。当前库cold-switch示例明确未实现LLF，不当论文E2E复现。
- [EdgeReasoning 2511.01866v1](https://arxiv.org/abs/2511.01866v1)：模型大小、reasoning token预算、并行test-time scaling在edge严格latency下可能改变相对选择；完整题摘是具体Pareto表征潜力，非自动按“只有benchmark”关闭，也未证明特定反侧。submittedOct21不是public；Updated11/05 01:00:13Z跨截止，不采。
- [Learned Cost Model 2511.01872v1](https://arxiv.org/abs/2511.01872v1)：reconfigurable ML dataflow placement需要昂贵测量，learned throughput predictor对比analytic heuristic且去performance annotations仍保持；有compiled-graph收益，可能直接支持ML编译计划成本边界。请核直接主线关系/具体增量还是通用成本模型关联；DAC2022 style不当旧公开证明。submittedOct21不是public，Updated跨截止。

13项DataCite原字段、作者有限恢复与精确重开已落[DATE_RECOVERY](DATE_RECOVERY.md)。只是日期层终态保留，不关闭潜在贡献；本日仍有可做的2公告和独立准入/日级普通待办。

原官方advanced search明确announcement date只支持年/月，排序也只给v1公告年月；带日查询失败不能说官方历史日级批次不存在。native daylist路径HTTP400也是无效/不可用入口结果，不认证本窗无论文。CL月skip0/show25只相关标题查漏，DC入口本次web InternalError，月库存不成为全部题摘/全文队列。

有限日期恢复继续具名DataCite/作者项目原事件，保留所有原字段与版本；真实官方announcement或可证明完全落窗首公开上下界可准入，不能用一般schedule补精确时刻。当前没证首公开，不反向关贡献，也不先深审所有date-hold正文。首批两公告正常可做仍推进，余源有限历史片段收口后写六部分进行中日报。Books实际0，未写共享文件；没有日级通过。
