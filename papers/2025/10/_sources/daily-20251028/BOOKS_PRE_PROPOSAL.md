# 2025-10-28 Books 窄 PRE 提案

作者Curie，原提案时间2026-10-05T07:20:31+08:00。以下拟文本保留为未采用的历史提案；root与Peirce已实际裁定具体已有覆盖 / No Change，见末尾root最终裁定。最终采用新差额0、实际写入0，无需POST；本文件不代整日DAY。

## 原证与唯一差额

[OpenAI官方Hub](https://deploymentsafety.openai.com/gpt-5-sensitive-conversations) §1/2.1–2.4及表4；本日openai-card.raw/必要正文实际已读，200原请求身份未变。Peirce FIRST通过最小准入2+2+2=6：新emotional/mental指标对旧版的retrospective测量，不是历史发布时已经存在的原始分数；专家/自动困难集/线上估计人口不能合并。表1 extremism .933→.925及表4 SimpleQA .46→.44/.49→.52反侧仍保留。未授线上伤害率、医学保证、公开训练机制或单一改善原因；不新增性能主张，硬件等Not Disclosed。

实际owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 95起EvalSpec已有taxonomy、population、scorer与比较规则，开篇要求版本化对象/环境；330–332已分enriched gold、predicted positives和自然人口，528起已有rare-failure audit floor。这些不再写。实际相邻Ch65末尾确有Scheduler只负责资源admission/placement→Ch66将workload/artifact/环境/scorer/结果绑定的直接交接；旧稿“只承载scheduler比较/版本”不准确，已按实际正文纠正。Ch67:14–16负责observed health，不定义quality。

潜在差额限：旧模型身份不变但测量spec后来变化时，回溯重测与旧时刻原评价是不同证据事件，不能静默覆盖历史分数或把跨spec差异归因模型。根若认为现有版本化论证已足够，可明确No Change；不得为提案强造diff。

## 拟写位置与文本

在Ch66 EvalSpec代码块之后、现“如果目标没有被写清楚”段之前，仅一个条件段，保留后面的proxy/metric对象论证：

> 即使模型版本不变，后来新增的failure taxonomy或scorer也会改变测量对象。对旧模型按新spec回溯重测，可以在同一测量合同下比较版本，却不等于它当时发布的原始分数；应同时保存模型事件时间、测量执行时间、spec/数据/scorer版本与重测标记，不静默改写历史结果。重测增加标注和调用费用，且同一新spec不自动修正困难集与部署人口差异；无法匹配输入人口或旧输出时，保留冻结旧评价作其原条件下的证据，另列新测量与Unknown，不合并跨spec数值或由差值推断训练改进原因。[官方回溯测量案例](https://deploymentsafety.openai.com/gpt-5-sensitive-conversations)只支持披露人口与模型版本，不提供生产安全保证。

“应同时保存”字段与回退是作者工程推断；retrospective事实与评价人口/反侧由原源支持。无新增章、无新owner，不加模型排行榜。若root接受，只落实本段及必要末注；实际写入后Peirce读正文、完整前后邻接与原源支持范围作POST，再同步最终Books处置。没有锁定写入任务前日报保持暂缓/进行中。

## root 最终裁定

root实际读取本提案、当前ROADMAP owner路径、Books适用三文档、Ch66 L75～120/330～365、相邻Ch65结尾与Ch67开篇，结论为**已有覆盖 / No Change**。Ch66开篇同时版本化对象、输入、执行与scorer；EvalSpec定义人口、分类与比较；“数值可复算不等于复现了同一个实验”正文明确任何身份变化生成新的evidence revision、不得沿用旧排名/效果声明。将后来新增spec下的回溯测量另存而不覆盖历史，是这条既有机制的具体应用，当前材料未形成需新增段落的长期差额。精确测量事件与非单调数字保留日报，不把厂商安全评价写成全书保证。

共享Books本次不修改，不制造POST收据。原提案保留为决策过程，最终提议采用的新差额0、实际写入0；日报应同步具体已有覆盖，而非继续等待写入。Ch65确有admission/placement→Ch66评估的交接，原“只承载scheduler比较”说法以本段纠正，不改其正文。
