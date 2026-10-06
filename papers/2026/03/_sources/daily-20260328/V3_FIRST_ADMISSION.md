# 03/28 首批完整题摘与日期核验范围

2026-10-02T04:40:13+08:00实际urllib打开以下八个exact-v1官方abs，读取完整h1/blockquote.abstract/submission-history；本文件是作者阅读摘要与判断，不声称逐字原文存档或全文Evidence。bs4不可用的首次本地解析未执行请求，改用stdlib HTML提取；每项当前官方页面可见withdrawn/erratum信号为空，仅此页、不认证全版本史。API latest题摘未替代v1。注册字段来自DataCite，relationships.client另定点核为arxiv.content，state findable；created不当上界。

## 五个具名潜在增量及事件边界

1. [DFLOP2603.25120v1](https://arxiv.org/abs/2603.25120v1)：完整摘要指出data-blind distributed框架忽略text/image/audio数据计算差异，runtime profiling测stage/microbatch variance并作predictive scheduling。潜在改变按静态parallelism配置负载的选择；不采用up-to3.6x，不将“datadriven”标签当本身增量。Submitted2026-03-26T07:45:29Z；官方常规最早27BJT08、registered27T02:01:37Z+1秒上界跨本窗左界27T09，需实际官方公告/作者原event精度，不能补造exact08。
2. [GhostServe2605.00831v1](https://arxiv.org/abs/2605.00831v1)：完整摘要采用streamingKV erasure coding parity shards存hostmemory，设备故障后重建丢失KV，替代full recompute或state replication。故障域与写入/恢复cost可能改变KV保护设计；不采用checkpoint2.7x/recovery2.1x/median1.2x。SubmittedMar26T13:27:57Z与五月ID/Available2026-05、registeredMay5T02:57:33Z并不支持March首公开。arXiv官方ID不能倒日期，故该arXiv原事件窗外，不因早Submitted另造本窗家族；若以后有具体作者早公开原event，单独按其身份恢复。
3. [HybridMemory2603.25716v1](https://arxiv.org/abs/2603.25716v1)：完整摘要区分静态background归档与离开视野的动态subject motion continuity，HM-World解耦camera/subject trajectories与exit-entry events，HyDRA将memory压token并按spatiotemporal relevance retrieval。潜在修正静态记忆复用即等动态记忆有效的假设；不采用全面SoTA。SubmittedMar26T17:56:01Z；最早27BJT08、registered27T02:15:48Z+1秒跨本窗左界。v2SubmittedMar28T08:29:52Z在本窗后，不用revision反填。
4. [Registers2603.25803v1](https://arxiv.org/abs/2603.25803v1)：完整摘要复现原register artifact/globalinfo解释，DINO/DINOv2/OpenCLIP/DeiT3跨架构/size反例显示部分结论非普适并澄清术语。是具体representation有效条件潜在反证，不因复现排除；未核实际反证配置或先采用原结论。SubmittedMar26T18:09:12Z，已在Thu14ET截止后，最早Sun29T20ET即30BJT08晚于本窗右界，registeredMar30T01:45:59Z。该arXiv原事件窗外，不要求不存在的March28公告；无作者此前原event线索。
5. [FailureAttribution2603.25001v1](https://arxiv.org/abs/2603.25001v1)：完整摘要指出MAS failure可有多个合理rootcause而非唯一确定答案，MP-Bench与multi-perspective evaluation protocol可能修正模型归因差的旧判断。潜在评价盲区不是仅新增bench名；不凭AB采用“旧研究由benchmark限制驱动”的因果结论。SubmittedMar26T04:02:23Z；最早27BJT08、registered27T01:58:45Z+1秒跨本窗左界。

## 三个具名贡献前关闭样本

- [SelfImprovementOverview2603.25681v1](https://arxiv.org/abs/2603.25681v1)：完整题摘提出data acquisition/selection、optimization、inference refinement四阶段加autonomous evaluation的生命周期组织，回顾已有代表方法与futurevision；没有独立的新机制、可验证有效条件或修正既有设计的实验反证。不是因overview标题一律排除，日期不影响该处置。
- [OMIND2603.25105v1](https://arxiv.org/abs/2603.25105v1)：完整题摘用structuredknowledge retrieval/LLM pruning/review生成164k领域SFT，mental-health对话turn/conversation专家rubric；未识别改变知识使用、训练或评价validity的新条件，80%winrate仅领域组合结果。不是以医学自动范围关闭，不授安全效果；必要core若明确新通用失效反证才定点重开，不扩全部数据。
- [OfflineDecisionTransformerTSP2603.25241v1](https://arxiv.org/abs/2603.25241v1)：完整题摘把既有offline DT/Pointer/expectile return conditioning用于heuristic TSP轨迹，优于四heuristics是此应用结果；未建立foundation模型形成或其运行机制的新边界。传统组合优化任务范围与现有方法应用不足建立本项目主线贡献，不泛化所有优化理论范围外。

## 官方事件首批

- [SAM3.1更新](https://ai.meta.com/blog/segment-anything-model-3/)实际core49–63：March27日级Update，singleobject pass→最多16object共享forward与global reasoning是明确计算/表示跨对象增量，潜在准入。16→32fps只厂商H100数字且object数/所有端到端条件未核，不授效果。仅日字段不足落本窗；原linked [2511.16719v2](https://arxiv.org/abs/2511.16719v2)Submitted28T16:54:56Z窗后，不取后来paper修订反填launch正文。旧SAM3内容位于更新后66起，不能全部归本次release；新event精确日期只有限原page/artifact恢复一次，不代码考古。
- [STADLER](https://openai.com/index/stadler/)实际core54–111，RSSFri27Mar22GMT即28BJT06落窗：650员工、125customGPT、30–40%节省等为采用案例/自报结果，未来Agent验证审批仍方向；未披露新执行机制或改变系统设计的受控证据，贡献前关闭。未因制造业本身范围排除。

## 五项DOI字段原值

```json
[
  {
    "id": "2603.25120",
    "client": "arxiv.content",
    "state": "findable",
    "created": "2026-03-27T02:01:36.000Z",
    "registered": "2026-03-27T02:01:37.000Z"
  },
  {
    "id": "2605.00831",
    "client": "arxiv.content",
    "state": "findable",
    "created": "2026-05-05T02:57:32.000Z",
    "registered": "2026-05-05T02:57:33.000Z"
  },
  {
    "id": "2603.25716",
    "client": "arxiv.content",
    "state": "findable",
    "created": "2026-03-27T02:15:45.000Z",
    "registered": "2026-03-27T02:15:48.000Z"
  },
  {
    "id": "2603.25803",
    "client": "arxiv.content",
    "state": "findable",
    "created": "2026-03-30T01:45:58.000Z",
    "registered": "2026-03-30T01:45:59.000Z"
  },
  {
    "id": "2603.25001",
    "client": "arxiv.content",
    "state": "findable",
    "created": "2026-03-27T01:58:45.000Z",
    "registered": "2026-03-27T01:58:45.000Z"
  }
]
```

首批已送root独立准入校准；仍非分母冻结，不授日期未confirmed正面Evidence或Books。
