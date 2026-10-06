# 10291：标准审阅与具体已有覆盖，待独立复核

root 准备；只处理03-13补查的03-12自然日。本ID有效题摘与日级归属复用本日准入/日期独核，不移动旧候选。实际重新打开官方 https://arxiv.org/html/2603.10291v1 ，读缓存 SUP_CORE2_10291.txt §3.1–3.3/4.1/4.3.1–4.3.3/6–7及Table2–4相关行，完整官方题摘、五作者和当前说明已核。未检查代码或复现，不追旧revision。

## 实际增量与边界

HyMEM在GUI经验中把离散策略/属性与连续轨迹embedding组合；共享属性提供图边，视觉+query向量提出种子、邻域扩展后重新排序。新成功轨迹由VLM对邻居判断Add/Merge/Replace；同一任务内，另一路比较前后截图及当前guidance，保留goal/约束、丢弃过时takeaway，再检索并刷新工作记忆。两种更新不应混为一个持久写入事件；VLM所谓information gain和阶段转移都是启发式，不是事实或授权证明。连续轨迹编码明确复用CoMEM，不将该成熟机制重新计分。

主设置2883成功轨迹归并1858节点、超过百万边，取5相似seed+5邻居，编码器Q-Former/LoRA适配约1.2%参数；模型、API与额外grounding fallback也影响总开销。三个web benchmark（WebVoyager/Mind2Web/MMInA）的VLM/LM判成功不是独立执行安全或真实事实核验。总体表的受限收益不意味着各domain支配，Qwen3-VL8B在MMInA Entertainment的HyMEM6.9低于baseline10.3；Table3 Amazon在5000→8000轨迹65.9→63.4，也不支持单调scale。Self-evolving只对Amazon/GoogleMaps局部对照，VLM写入启发式和大模型未测是§6直接限制。没有披露在本次必要原证可确认的完整precision/硬件/并发/尾SLO或净全生命周期成本，不授生产收益、无污染或自动长期改进。

## 评分与 Books

1+2+2=5：GUI经验图的局部组合1，持久写入与任务工作记忆两侧接口2，可复用读写/刷新取舍2。实际增量是具体实现及局部验证，不借一般memory/graph/持续学习原理抬分；标准审阅已达到拟保留范围。

实际顺读Ch77 85–128 typed write/target/evidence/version与冲突/派生身份，375–415 query-conditioned construction、静态latent bank→动态working state、query-local graph邻域/未覆盖实体与更新版本。这些正文具体承载持久写入与动态读状态分责、邻域扩展/重读及错误更新回退，并非只因主题相似判NC。Ch76/78开篇交接已读：检索证据及真正tool effect分别拥有责任。没有需要重复写入的长期命题；5分标准完成/已有覆盖，owner AGENT-MEMORY（Ch77，legacy Ch73），Books新写0。原文的属性/5+5配置、GUI人口与收益留报告作为受限实现，不将作者启发式变成库中事实权威。

非作者仍需实际复核上述Source/具体正文覆盖；本文件不自授独核或DAY。
