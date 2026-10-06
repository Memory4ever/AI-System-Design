# 2025-11-02 首批校准 ready

作者范围仅 `papers/2025/11/02/README.md` 与本目录。窗口 BJT `[2025-11-01T09:00:00+08:00, 2025-11-02T09:00:00+08:00)`。启动已重读 AGENTS、当前 V3 两合同、来源使用说明/每日/arXiv主题、Prompt、ROADMAP 和最新相关 checkpoint；本日此前无停点。未读取旧 Weekly 或其他日候选。

## 请 root 实际校准的首批集合

当前确定当窗拟入选 0，工作分母未冻结。不是全网零事件断言。校准请先核入口范围与下列具体关闭理由，不把目录库存变为全文队列。

| 身份 | 实际读取与判断 | 当前处置/校准问题 |
| --- | --- | --- |
| [PlotCraft, 2511.00010v1](https://arxiv.org/abs/2511.00010v1) | 已完整读取精确 v1 题摘和当前版本页。原字段 `Submitted on 15 Oct 2025`，history `Wed, 15 Oct 2025 10:14:39 UTC`；latest v2 为 2026-01-15。题摘主要新增复杂可视化任务集、合成代码数据和小模型，未说明可迁移执行机制或足以修正通用评价判断的具体混杂/失效边界。 | 拟贡献关闭，不评分、不入 Books；不是因日期 hold 关闭。请核多轮 refinement 评价是否已构成具体评价盲区，而非仅增加任务复杂度。若改判只定点补该篇方法/评价和首公开证据；不得因 v1 October submission 断言归属 October，也不因 2511 ID 补造 November announcement 时刻。 |
| Seed `A Multi-Resolution Systematically Improvable Quantum Embedding Scheme for Large-scale Surface Chemistry Calculations` | `seed-type1-p0.json` 原标题明确为表面化学计算，非 foundation-model systems；无需强制摘要/全文。 | 范围关闭：ROADMAP 暂缓 AI for Science；不借 TRAIN-DATA 或 Evaluation owner 重新引入。 |
| Seed `ByteDance Seed and BYD Lithium Battery Partner to Launch AI Lab for Battery R&D`, ID261 | `seed-type2-p20.json` 原标题明确是电池研发合作发布。 | 范围关闭：领域应用/机构合作，不是模型训练或推理机制增量；未建立必要日期请求。 |
| [Kimi K2 Thinking 官方目录](https://platform.kimi.com/blog) | 官方公开列表标 `2025年11月06日`，前后有 11/07 和 09/16 条目，完整单页已读。 | 本日窗外线索，未作为重复审阅完成，也不加载其正文或继承到后日候选池。 |
| [MiniMax M2 & Agent 官方目录](https://www.minimax.io/blog) | 英文目录原日期 `2025-10-27`，中文同日期；列表跨到 12/23。 | 旧发布不构成当窗版本事件；本日只查是否有新的机制/纠错说明，不为名称或宣传数字准入。 |

## 实际普通工作与外部问题

- 可继续普通工作：OpenAI RSS 已 HTTP200 保存，需解析目标邻接日期；DeepMind 11 月页两项可能相关标题需核文章原日期；ERNIE 第2页已打开需写明停止；Qwen迁移页/Z.ai查看更多、Hunyuan旧Research及Meta动态目录尚需有限恢复后决定终态。完成这些才能冻结本日集合。
- Hunyuan：web入口无提取文本；隐藏 browser 一次30秒超时、kernel reset。改走用户线索接口 POST，HTTP200/code0，`totalNum=9`，9个en条目最早时间字段为2026年；这是当前博客列表身份，不是2025年11月Research覆盖。尚缺旧Research历史切片；不可把9条返回当作本窗零命中。
- Seed：GET type1/type2各 p0/p20已实际取得，原 `PublishDate` 毫秒、`IsPinned`、`next_page_token`/`has_more` 全保留。置顶与历史编辑可能影响顺序；当前仅以返回切片为有限依据，不能由page0宣称全年完整。
- arXiv：官方 availability 说明 Sun–Thu20ET、Fri/Sat无常规公告。02窗口没有常规公告，仅支持常规公告检查边界。11/02 DST结束，后续09BJT截点必须含起点不含终点；schedule不能补造单篇实际公开时刻，submission/month ID不作当窗正面证据。非标准提前公开仍要实际作者/官方证据。
- 没有 Books 写入/共享修改；若 root 改准入后出现长期增量，将按要求补context/owner/邻接比较再交root具体采用命题。

## 原始依据

[arXiv边界/v1](RAW_ARXIV_BOUNDARY.json)、[机构入口](RAW_NATIVE_01.json)、[中英文/迁移入口](RAW_NATIVE_02.json)、[定点恢复](RAW_NATIVE_RECOVERY.json)、`seed-type1-p0.json`/`seed-type1-p20.json`、`seed-type2-p0.json`/`seed-type2-p20.json`、`hunyuan-p1.json`及同名receipt，有限搜索 `RAW_WEB_01.json`～`RAW_WEB_04.json`。搜索返回零不支持目录无遗漏；community用户投诉不作OpenAI官方研究证据。

本文件 ready 只表示作者准备好校准，不代表独立校准或整日验收通过。§6待实际非作者验收。

## root实际首批校准追加（2026-10-04，root独立复核反馈）

独立复核者root实际读PlotCraft exact-v1完整题摘及HTML Introduction，判作者拟关闭理由过窄。原文不只增加题集，§1指出functional correctness/simple Text2Vis不能验收composite layout，新增multilevel metrics和multi-turn refinement用户feedback，并有简单benchmark强不保证复杂可视化的负侧信号。

仅重开PlotCraft，作者定点补§3.1/3.4、§5.2/5.4，核code执行正确不等于视觉目标正确、multi-turn改进的可支持边界；不因新benchmark自动收，也不因已有通用evaluation原则自动关。必要日期仍是普通有限恢复，Oct15 Submitted不等October public，2511 ID不补造November时刻。此反馈不是当窗准入、日级或Books通过。

root确认其余两个science/合作title范围关闭，以及Kimi/MiniMax旧发布非当窗新事件的处理可继续。不存在共同理由导致的全列表重开；03及后日不得继承PlotCraft为自身候选。

## 定点恢复后再次ready（2026-10-04）

原表PlotCraft拟关闭已被上述root独立复核反馈否决，不能沿用。作者已完成指定四节定点读取；[必要证据、日期恢复和owner差额](PLOTCRAFT_POINT_REVIEW.md)可交root继续核验。当前改判为有具体评价盲区/负侧证据的潜在贡献，不是新benchmark自动准入。首公开仍未确认完全落窗，未评分、未列本窗确定候选、未进入Books。

前文“实际普通工作”是首批交付时历史停点；现已完成那些有限入口/邻接日期恢复，终态范围见日报§2/5。当前可执行点为root核上述定点结论与日期隔离、实际六部分验收；作者继续未受影响日期来源工作，不扩大PlotCraft阅读或全年库存。
