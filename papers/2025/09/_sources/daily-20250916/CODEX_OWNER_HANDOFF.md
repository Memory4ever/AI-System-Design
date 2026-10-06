# 16日 Codex source / core / owner 交接

作者Tesla，2026-10-06。最新裁决：root实际RSS/完整release核心及Ch81/75顺读通过，详`INDEPENDENT_CODEX_REVIEW.md`；正式准入2+2+1=5、标准完成、仅报告，新增Books正文0。下文原提案保留过程依据，建议自然段落不实施；发布未披露controller/recovery，不插Ch81长期机制，不按已有覆盖撤销准入。日级终核仍待，没有修改Books。

## Source

- 官方[release](https://openai.com/index/introducing-upgrades-to-codex/)，身份是2025-09-15发布正文；页面明确标注的Sep23 API更新排除本次事件。
- `openai-rss-recovery.xml`原pubDate `Mon, 15 Sep 2025 10:00:00 GMT`，即15日18:00北京时间，落16默认窗。card原00:00 GMT即08:00，独立窗外；不合并datehold。
- 新实际读取原文保存在`codex-final-core.json`。curl403原记录不删除；不由失败否定web完整核心读取，也不声称核了CLI实现或复现。
- Qwen新机械入口单次20秒上限HTTP200，`qwen-config-recovery.raw`原60个带date配置。只筛本窗UTC `[2025-09-15T01:00Z,2025-09-16T01:00Z)`，0命中；相邻原date为Next `2025-09-10T20:00:00.000Z`及TTS `2025-09-21T20:00:00.000Z`。没有将60条变成正文队列，亦不继承别日覆盖。

## Core与限定

原文GPT-5-Codex段落L54–64：任务复杂度条件化thinking；employee traffic短token十分位较GPT-5少93.7%，长十分位投入相反增加。L56评价分母477改500，不直接拼接旧分数；L59长运行个例不证明SLO。控制器、训练配方、硬件/precision、长度/batch/concurrency及独立置信区间Not Disclosed。

CLI L71只披露compaction/approval接口；cloud L80容器缓存的局部中位收益，配置与归因细节未披露；安全L93–97说明默认网络限制及人审，不授安全保证。它们不被包装为新cache算法、原子compaction或可靠恢复证明。

贡献：统一投入难兼顾交互和长任务→这次公开短/长负载相反的投入变化→应分别评价预算与质量，而非以单个节省数决定部署。root准入2+2+1=5、标准审阅通过；只采用版本局部观察，不推隐藏控制器因果。

## Actual Owner差额

主要owner建议`AGENT-WORKFLOW`，[Ch81](../../../../../books/part-07-agent/81-workflow.md#workflow-可见性也会改变-serving-优化空间)：实际L727–778解释workflow提示如何扩大跨调用复用/调度空间，identity兼容和engine admission仍由各owner控制；L879–900说明long-running保存外部事件与中断状态；L1176–1192区分checkpoint/replay与真实effect。本次材料不证明这些durability性质，却提供“同一发布中的短/长任务预算方向相反”的版本局部证据。不是因为通用原则未变而排除。

自然整合建议：若root认可局部验证应入书，在L749后、窄orchestrator–engine接口前，补一段任务预算与runtime权限分工：交互任务和长轨迹不宜用统一预算衡量；局部发布观察可验证这一选择，但自适应thinking不是engine资源准入，也不证明长期恢复。只加这条限定解释，不复制营销指标或把隐藏策略写成算法。若root认为现有论证已足以承载该局部观察，则仅报告这个版本事实，必须据实际差额裁决，不用“没改变通用原则”自动关闭。

相关而非重复owner：`AGENT-CONTEXT` [Ch75](../../../../../books/part-07-agent/75-context.md#context-compression-必须保留执行状态而不只是语义)实际L536–550要求恢复位置、约束及可回读引用；L321–347已解释不可变原文、派生摘要、compare-and-commit。release没有披露足以证明这些实现的材料，不拟在此添加机制。其前后交接已读[Ch74](../../../../../books/part-07-agent/74-prompt.md#本章在知识树中的位置)与Ch75 L589–593，RAG负责外部证据而非预算。Ch81相邻[Ch80](../../../../../books/part-07-agent/80-reflection.md#本章要回答的问题)明确反馈/停止policy，[Ch82](../../../../../books/part-07-agent/82-multi-agent.md#先建立单-agent-baseline)明确总调用/通信/关键路径成本；不把本次动态thinking归因为reflection或多Agent。

## Root入口

root单项工作已完成，不重复请求。剩余为16日其他安全/误排/来源和最终DAY；作者当前没有未执行的具名必要正文请求，外部缺项不用于正面论证；新返修只重开受影响命题。日报保持进行中，不自行宣告日级完成。
