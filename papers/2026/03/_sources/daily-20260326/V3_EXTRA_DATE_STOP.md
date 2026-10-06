# 03/26 有限相关标题补检与原日期停点

执行时间2026-10-02T04:29:26+08:00。root实际打开以下四个exact-v1页面的完整题摘及submission history；不是全文Evidence，也没有采用性能数字。当前页面没有可见withdrawn/erratum标记，不认证全版本史。三个早提交但登记较晚的标题只作查漏，不按arxiv编号当公开日期。

| 身份 | Submitted原UTC | DataCite Created / registered原UTC | Updated / Available |
| --- | --- | --- | --- |
| [PCR 2603.23049v1](https://arxiv.org/abs/2603.23049v1) | 2026-03-24T10:40:58Z | 2026-03-25T02:15:11Z / 2026-03-25T02:15:12Z | v1 Updated2026-03-25T00:50:15Z / Available2026-03 |
| [StepCache 2603.28795v1](https://arxiv.org/abs/2603.28795v1) | 2026-03-24T17:19:26Z | 2026-04-01T01:55:46Z / 2026-04-01T01:55:47Z | v1 Updated2026-04-01T00:00:42Z / Available2026-03 |
| [Lightning 2604.03279v1](https://arxiv.org/abs/2604.03279v1) | 2026-03-24T13:02:58Z | 2026-04-07T02:37:36Z / 2026-04-07T02:37:37Z | v1 Updated2026-04-07T00:01:16Z / Available2026-04 |
| [RobotFlywheel 2603.25583v1](https://arxiv.org/abs/2603.25583v1) | 2026-03-26T16:00:39Z | 本次不以未读登记字段认first-public | Seed1335 PublishDate1774454400000为BJT26整日字段，不证明26T00首公开正文 |

PCR完整题摘：prefill reuse受命中/CPU-GPU transfer/SSD约束；prefix tree lookahead LRU使用pending queue，layer load与compute跨CUDA stream重叠，queue预取SSD→DRAM。潜在queue/reuse联合边界，作者最大TTFT数字未采用。常规最早25BJT08到registered findable上界跨本窗左界，不能认26确定候选或25已审重复。

StepCache完整题摘：共结构但局部schema/变量/常量变化时，按ordered steps检索、task-aware verify、只patch失败区域；JSON提取/keys/one-shotrepair，semanticchanges conservative skip；linear equation boundedrepair+deterministicfallback。CPU microbenchmark三seed不证明泛任务semanticcorrectness或普遍p95收益。原登记迟至Apr1，需真实原公开范围，不能强认March。

Lightning完整题摘：连续波形/听觉敏感使TTS精度较LLM脆弱，precision-aware architecture与NoC/distributedSRAM/LoFi/BFP8联合设计可能构成明确质量/资源边界。标题成本倍数无完整预算/质量/evaluator合同不采用。v2Apr7不自动比较，v1登记Apr7与SubmittedMar24不等首次公开。

RobotFlywheel完整题摘：F-ACIL按object/action/environment分解factor spaces，用factor-wise collection与iterative training提升组合泛化；作者demo减少和performance数字不能代替可归因因子对照。目录Mar26整日与arxiv26T16Z并不能证明更早原正文在本窗，需Seed原事件语义/作者原稿公开范围。不是全文缺失请求。

上述四项均隔离，只有决定准入/日期事实到达才重开，不评分、不授Evidence或Books。没有开始无关旧版本diff/所有appendix/领域新队列。

