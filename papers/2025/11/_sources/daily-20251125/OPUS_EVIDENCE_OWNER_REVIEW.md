# Nov25 Opus：单项证据与 owner 差额送审

作者 Aristotle，2026-10-04T15:28:30+08:00。已获 root 准入校准，2+2+2=6；本文件请求独立证据/Books 判断，不授日级通过。当前 ownership 为11/25～29，11/30未开始、没有文件写入。

## 事件与采用边界

[官方 Opus release](https://www.anthropic.com/news/claude-opus-4-5) 的 HTML published、JSON-LD datePublished、正文 time 一致为 `2025-11-24T19:00:00.000Z`，BJT11/25 03:00完全落窗。原始页面在 [native-opus.html](native-opus.html)，核心响应在 [raw-event-0.json](raw-event-0.json)。本项不是工具文章首公开；advanced-tool文章原字段仍为00Z，具体19Z API release另行处理。

系统卡采用官方目前可获取的 [153页 PDF](opus-system-card-current.pdf)，原 URL 为 [Claude Opus 4.5 System Card](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf)。p2明确列出Nov24、Nov25、Dec5 changelog，因此不声称下载的是Nov24逐字原版。只采用历史release所指能力与当前card的必要条件说明；Nov24纠错有明确历史标签，其具体公开时刻未披露，不独立造一个精确落窗纠错事件。后续已列修订未改变下列必要章节，仍不保证未列编辑不存在。

## 必要机制、对照与关键反证

- p9 §1.1.2：effort控制作用于thinking、function calls/results和user-facing blocks，不等于仅增加thinking budget；实际token量依赖问题难度与模型对所需token的估计。原文没有给出effort档位的硬token上限保证。采用的是控制接口区别，不推断未公开训练算法。
- p10 Fig1.1.2A实际渲染并核图内文字，见 [图页](opus-card-page10.png)：SWE-bench Verified n=500，extended thinking **off**；图内注明打开后平均output tokens增加5.4%。不能用系统卡一般64k-thinking配置替代这幅曲线的条件。release报告medium相对Sonnet4.5少76%输出token、high高4.3个百分点且少48%，只保留厂商此工作负载的相对数，不从图像反推精确坐标。
- p20 §2.4、Table2.4A：Verified为500个工程师核可解决问题，表中分数平均5次试验。该表并非提供了effort曲线每个点的独立重复方差。硬件、precision、batch/concurrency、端到端latency、工具运行成本与SLO为Not Disclosed，token减少不证明总计算、费用或尾延迟减少。未复现实验、未核实现。
- p20 §2.5：Terminus-2/Harbor中低资源限制引入最多13% flakiness，主要容器OOM；作者在失败时、杀pod前对**所有被测model**增加2×资源限制，infra errors降至<1%。这支持环境修正必须留身份，而不是固定环境下模型能力提高。Codex-Max条目使用不同CLI/hosting且作者未能复现，不能据此作同harness排名。无需扩读全部Terminal-Bench附件。
- p26～27 §2.8.1：basic-economy先升舱再修改的替代路径符合政策字面，但rubric预期直接拒绝而给失败；这不证明所有该路径符合企业意图。显式禁止任何路径达到该结果后，作者观察到该行为消失，且不推荐airline切片作跨模型或policy-adherence指标。不将模型自述共情当因果证据。p19脚注与p26 original-airline分数存在67.9/70.1差异，本次不采用数值修正幅度，不将两个协议混合。
- p2 Nov24 changelog与p28 §2.10：曾把公开test曲线替换为ARC Foundation semi-private结果；此前“只训练public train”说明错误，实际用public train+test重新划分，作者声明未训练reported semi-private测试集。训练公开test不等于半私有评测已污染，但原图不能继续作独立留出证据。p28当前称private validation与p2 semi-private名称并不完全一致，本次采用纠错后的身份/泄漏限制，不采用未核排名或智力保证。必要图页已查看 [p28](opus-card-page28.png)。本次不扩大到全部能力、安全或训练章节。

## 已实际读取的 Books 与相邻内容

先读ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、最新11月checkpoint。唯一拟长期 owner 为 `PLATFORM-EVALUATION-SYSTEM`，实际读取 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的开篇、L195～243、L390～401、L448～470、L695～738、L2662～2694、L4252～4274；并读 [Ch65收尾](../../../../../books/part-06-ai-infrastructure/65-kai-scheduler.md) 与 [Ch67开篇](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)。这是目标论点与交接比较，不是靠关键词未命中证明缺口。

已有覆盖的具体正文：Ch66 L234～240已经冻结model × benchmark × harness × environment × scorer；L399、L2687及L4260已经说明合法替代路径可能被误拒，process/outcome分账；L120明确public开发标签不能代替独立holdout。因此本次harness、τ2及ARC纠错作为新的局部证据保留在报告，**不申请重复扩写这些成熟原则**。

## 仅一项窄差额请 root 决定

Ch66 L456～460当前将per-call token budget作为独立变量并记录violation，但尚未在这段区分“改变生成倾向的控制档位”与“硬资源限额”。Opus原文具体体现了这个区别：相同effort档位的实际tokens随任务变化，甚至在extended thinking关闭时仍有质量/token曲线。拟采用命题是：**EvalSpec分别保存行为性投入控制、hard cap、extended-thinking开关及实际消耗；不能把档位当上限，亦不能把输出token曲线当总运行成本保证。**

建议整合位置仅为上述Resource Budget段：在L458现有per-call预算句之后补一个条件分支，随后承接L460 persistent identity。不新增章节、不加产品清单、不把effort名字未见作为理由。静态固定cap仍适合严格资源约束；行为档位需要按目标任务测质量/消耗曲线，额外多档试验有评估成本，未披露运行成本则保持Unknown/原硬cap。

root可判此区别已由现有完整预算语义承载而采用“已有覆盖”，或判接口版事实不足改变长期知识而“仅报告”；两者都有效，不为改书制造差额。若批准上述窄命题，实际写入由root协调，需非写入者POST实际正文与前后衔接。作者未写Books、无写锁请求。

## 独立核验点与当前停点

请独立核：p10图内thinking-off条件；p20资源2×是对所有model而非仅Opus；p26～27合法字面路径不等企业意图；p2/p28纠错不等semi-private已污染；上述owner具体差额是否必要。root已审release尾部不重复请求全文。

本项作者必要证据已准备好，Books仍待独立判断。Nov25普通工作继续：工具release兼容边界、MURMUR受影响安全、UI-CUBE限定负证据、拟贡献项有限日期恢复及来源边界。不因本项送审停工，不将本项ready称日报完成。

## Root 写前回传与非写入者 POST（2026-10-04T15:36:15+08:00）

root独立实际读取current PDF p2/9/10/20/26/27/28并视觉p10，核native release日期，确认必要证据与窄差额通过。root仅写Ch66 Resource Budget新增一段及Review notes首条，family=`SF-2025-ANTHROPIC-OPUS-4-5`；作者未参与共享Books写入。

非写入者Aristotle实际POST：读取当前Ch66 L450～476，包括原per-call budget L458、新段L460、persistent identity L462、Backend邻接；实际读Review notes首条L4416；实际读Ch65 L102～116交接和Ch67 L1～24。必要原源命题未变，复用此前已核p9/p10与反侧，不重复全部系统卡。

POST结论：通过，未发现需root修正的问题。新增段准确区分控制档位/硬上限/thinking开关/实际消耗，保留目标任务多档试验成本与严格hard-cap旧路径，不把thinking-off当整条生成投入冻结，也不把输出token效率签发总费用/尾延迟保证。前后预算与persistent身份顺读成立，Ch65 admission/placement及Ch67聚合监控的交接未越权。末注保留当前版本/未复现/曲线方差不明/ARC限制，没有自授日级完成。末注当时仍写“待非写入者检查”，请root按本POST事实更新该一句；作者不改共享Books。

本项处置更新为整合 `PLATFORM-EVALUATION-SYSTEM` Ch66 L460。单项证据与Books已处理，整日source/date/其他候选及非作者日级复核仍未完成。
