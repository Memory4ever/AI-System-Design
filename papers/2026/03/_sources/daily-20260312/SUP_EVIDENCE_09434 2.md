# 2603.09434 — 叙事人口、提示目标与检出代理（Source/date/具体NC通过）

[Common Sense vs. Morality exact-v1](https://arxiv.org/html/2603.09434v1)。作者实际完整§3–8及Table2文字；完整AB/current信号见SUP_EXACT_BATCH3.json。仍v1、Accepted LREC2026、未见withdraw/纠错。精确标题有限补检实际取得[ELRA正式页](https://lrec.elra.info/lrec2026-main-835)，同题/同四作者、日期11–16May2026及DOI10.63317/23hsqksy9475，仅用于发表身份轻核，不把接受、会议日期或搜索crawl当首次公开，不扫全venue；未出现具体窗前先稿证据。

arxiv.content owning/findable registeredMar11UTC02:13:31已可发现上界，原Mar10UTC09:47:18 Submitted仅配已实际官方no-advance最终ID/DOI和最早Mar11BJT08下界，夹证arxiv03-11；不是注册或Submitted单独public。拟采用的具体评价人口/提示目标边界2+1+2=5标准审阅，不由道德主张抬分。

## 必要机制、对照与直接反侧

§3先人工88种矛盾，用Llama70B instruct每种生成5primary/5secondary故事。两英文流利CS毕业annotator按三项1–5评分，任一<3排除、差≥2讨论后仍异议再排除；880→840→802，最终475primary/327secondary。筛选改变人口与类别构成，并非每个相同事实只随机改变叙事角色的matched intervention。Temporal大量排除；所报alpha不能认证全部label真值或所有文化常识。

§4 implicit仅答故事问题，explicit额外要求找矛盾，两者改变任务目标/elicitation，不是相同目标上的内部道德—常识因果比较。GPTOSS120B scorer只判断是否提及预设矛盾；检出不等道德正确、真belief或guardrail成功。10个0.5–8B instruct模型跨Llama/Qwen/Gemma版本，不含同基座unaligned对照；无法把行为差异归因alignment训练、attention机制或内部优先级。解码预算、重复seed/CI、硬件/precision/latency及完整计算费未披露，不补实现。

Table2与§4.2 overall固定人口定义有明确冲突：Qwen7 implicit overall.135，而primary.057/secondary.078，任何两子群正权重均值不能超过.078；按475/327应约.06556。Llama1 explicit overall.261小于两子群.263/.270也不满足凸组合。其他若干项与475/327加权差额非末位rounding；保留原值，不推断实际使用macro平均/不同subset来修原文。因此不采用精确总体提升幅度或严整模型排名，需要原scorer的聚合人口/计数及更正才能重开。这个局部指标争议不使真实评价接口/人口设计消失，也不标签整篇无效。

§5.2/5.3实际描述类别特例，Unreal explicit下primary可相当或更高，不能把“all categories/always secondary better”写成普遍规律。§8也承认理论解释未建立和模型/领域规模限制。核心可支持范围只是受限故事人口中的提示条件与角色切片需要分别报告；非paired故事结果不单独识别叙事角色因果，明显目标提示不认证完整常识能力恢复。合成故事、两annotator筛选、双prompt多模型调用、GPTOSS判断及必要独立标签/复测均付费。

## actual owner 与具体NC

作者actual完整Ch66 210–237、282–313及Ch65/67开篇。210当前自然行为/elicited lower bound/supervisor ceiling分离；216–220显著特征非任务真值及规范用途Unknown；222–227同压力配对与方向翻转审计明确冻结baseline/matchedcue、完整分母、可见理由classifier非内部真值；229条件人口分母；285–309完整model×benchmark×harness×environment×scorer identity与comparison/realized treatment而非成功run。已实际承载本项采用的提示目标、角色/类别人口、judge检出proxy、matched attribution与完整费用边界，具体NC，不为此新增benchmark段。

root非作者实际完整S3/S4含T2、batch3当前版本/日期夹证、Ch66 210–237和282–304必要正文独核通过；接纳具体NC第8项，确认新增第29项。没有Books新写，不授全图/代码/复现或DAY；停止无关参考文与附件，精确Table2效果继续隔离。
