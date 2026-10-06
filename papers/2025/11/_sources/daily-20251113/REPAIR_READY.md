# 2025-11-13 三项局部返修：交 Ohm / root

作者：Planck。检查时间：2026-10-04T16:22:44+08:00，来自实际 clock。报告仍进行中，日级仍未通过；本文件不是独立复核结论。

以上为送审时快照。最新：Ohm已在[独立Notes §7](./INDEPENDENT_REVIEW_NOTES.md)实际局部回核三项通过；root实际读取最终六部分后通知作者同步完成态，见[正式日报](../../13/README.md) §6。普通待办0，不等待月计数；本文件不代写独立结论。

2026-10-04T16:34:41+08:00实际收口检查：正式完成态V3通过；8份Markdown/44本地引用、直接空白与46份JSON解析通过，限定diff-check通过。下面送审时的进行中测试和局部复核请求仅保留历史；不再是当前待办。root可重跑最终validator纳入验收，不修改共享state。

仅响应 [INDEPENDENT_REVIEW_NOTES](./INDEPENDENT_REVIEW_NOTES.md) §5。Project Fetch 的日期/准入/必要证据/具体 Existing，以及追加12项准入和3D4D关闭均复用独立通过，未重读其已通过附件。11/14停点已保存，未借其材料修13。

## 1. JAX-Privacy：博客本身的贡献筛选已作出

材料：[Differentially private machine learning at scale with JAX-Privacy](https://research.google/blog/differentially-private-machine-learning-at-scale-with-jax-privacy/)，官方日期原值 November 12, 2025，未披露时区/精确时刻。读原 [raw-web-07](./raw-web-07.json) 中该博客核心104–143行；本次一次定点补读同一官方博客和 [v1.0.0 README](https://raw.githubusercontent.com/google-deepmind/jax_privacy/v1.0.0/README.md)，实际结果保存为 [raw-web-32-repair](./raw-web-32-repair.json)。没有扩 JAX runtime 或历年目录。

有限对照：[release 原返回](./raw-jax-privacy-releases.json) 的 tag=v1.0.0、published_at=2025-07-10T15:34:35Z，仅证明该release事件在July，不单独决定博客贡献。

| 博客核心命题 | 已有材料与实际差额判断 |
| --- | --- |
| DP-SGD primitives、accounting、Keras/Gemma入口 | July release 已列 DP-SGD、Flax/Keras、examples、accounting；精确tag README 23–43行描述框架分层与Gemma示例入口。博客重述这些能力，未识别新增接口契约；tag中的例子链接指向main，不据此声称July具体示例代码已核。 |
| DP-FTRL、跨步相关噪声、matrix factorization | release列DP-FTRL算法，但tag高层API只明确DP-SGD、DP-FTRL仍列future，不能合成July完整高层DP-FTRL接口。博客介绍研究算法/组合能力，未给November新增接口差额或新的成立边界；不以成熟DP原则给新命题打分。 |
| distributed batching / microbatch / padding | 博客解释可扩展工程组合，但未辨认本次改变的批语义/算法约束或支持归因的对照；不是因为没有benchmark就关闭，而是原文未建立独立贡献命题。 |
| accounting与canary auditing结合 | auditing不在短release中，不能断言July已实现。博客指向既有审计研究，并概述canary/逐步metric用途；未提出新审计协议、威胁模型变化或有效性反证。当前文字不能建立本次新增安全约束。 |

处置：**博客核心贡献关闭，不评分、不写Books**。判断针对读到的增量：既有隐私机制及组件组合的发布说明，未建立独立改变设计选择的November命题；不是“DP成熟所以无价值”，也不是“July release所以整个博客重复”。不声称全部源码已核、所有能力July已有或生产保证成立。日期未核实不影响这个贡献关闭，停止追加日期恢复；将来若出现明确新增接口/方法或纠错，再只重开该差额。

## 2. 三份现存v1完整题摘：贡献保留，日期终态隔离

本次只抽取以下身份的完整题摘与原published/updated字段，不读整批92、不展开全文。前两项来自 [core-repair XML](./raw-arxiv-api-core-repair.xml)，第三项来自 [revisions XML](./raw-arxiv-revisions.xml)；后一文件名不赋予修订查询权限，原响应实际仍是submittedDate发现。

| 精确身份 / 完整原题 | 原字段 published=updated（提交元数据，不是public） | 具体准入命题与作者拟评分 |
| --- | --- | --- |
| [2511.07876v1](https://arxiv.org/abs/2511.07876v1), LoopLLM: Transferable Energy-Latency Attacks in LLMs via Repetitive Generation | 2025-11-11T06:24:49Z | 原先靠延迟终止符的资源攻击随输出增长失控 → 低熵重复生成形成另一耗时失效路径 → 资源治理不能只测试终止符延迟；2+2+2=6，安全命题在日期成立后必要深入。 |
| [2511.08487v1](https://arxiv.org/abs/2511.08487v1), How Brittle is Agent Safety? Rethinking Agent Risk under Intent Concealment and Task Complexity | 2025-11-11T17:27:27Z | 原子有害任务评价 → 意图隐藏与任务复杂度双轴、能力失败使难任务看似安全 → 必须分开安全拒绝与能力不足；2+2+2=6，安全/评价反证在日期成立后必要深入。 |
| [2511.08568v1](https://arxiv.org/abs/2511.08568v1), Machine Learning-Guided Memory Optimization for DLRM Inference on Tiered Memory | 2025-11-11T18:49:53Z | tiered memory中embedding访问模式限制placement → 分离cache/prefetch预测及可微loss缩小搜索 → 要核标签、placement代价和端到端条件，不能因DLRM不是LLM关闭模型内存机制；2+2+2=6。 |

题摘中的实验声明只用于判断潜在贡献，不是已核证据：LoopLLM的12开放/2商业模型、输出上限比例及迁移数字尚未核公平baseline、backend和重复条件；OASIS的Complexity Paradox尚未核sandbox、能力/拒绝标签及两轴控制；RecMG的fetch减少及upto43%尚未核tier容量、访问trace、训练/推断开销与质量目标。没有把摘要读完写成标准/深入审阅完成；也没有因缺实验细节排除。

三项是**本窗终态保留项**，不是§3确定落窗候选：现存精确v1已确认，但必要首公开下界缺失。沿用本日已有有限原源恢复（raw-web-29/30），其中空历史检索/未确认语义的日list路径不证明无发布，也不为这三项生成新的空路径。submitted、一般schedule或DataCite registered不能授落窗。**不用于正面证据、Books或无遗漏断言**。

定点重开条件：对应ID的实际历史官方公告/dated list与精确v1绑定，配合真实首公开上下界构成完全落窗范围，或作者带可核时刻的首次公开记录。恢复只核该家族日期；落窗后再核表中方法/反侧，不扩其他日期或整类。当前不请求基于日期未明材料的Books整合，不以owner名称缺位制造缺口。

## 3. 三个晚版信号：版本/日期处置

| 已发现身份 / 完整原题 | 原published / 当前updated | 处置与精确重开 |
| --- | --- | --- |
| [2511.07645v2](https://arxiv.org/abs/2511.07645v2), A Self-Improving Architecture for Dynamic Safety in Large Language Models | 2025-11-10T21:39:40Z / 2026-04-01T17:52:48Z | 当前v2窗外，不采用其SISF评估作为November证据；缺历史v1身份文本与真实首公开归属，不作v1贡献关闭或评分。 |
| [2511.08484v2](https://arxiv.org/abs/2511.08484v2), Patching LLM Like Software: A Lightweight Method for Improving Safety Policy in Large Language Models | 2025-11-11T17:25:44Z / 2026-04-27T17:07:15Z | 当前v2窗外，不用安全patch参数/结果反推v1；无已证明的重要本窗修订。 |
| [2511.08003v2](https://arxiv.org/abs/2511.08003v2), Sharp Eyes and Memory for VideoLLMs: Information-Aware Visual Token Pruning for Efficient and Reliable VideoLLM Reasoning | 2025-11-11T09:07:40Z / 2025-12-04T06:19:39Z | 当前v2窗外，不用SharpV当前题摘证明November的pruning/Flash兼容命题；published不赋予当前摘要v1身份。 |

前两份完整当前题摘在core-repair XML，第三份在 [memory XML](./raw-arxiv-memory.xml)，已读以核实实际信号/版本污染风险，而非历史准入。**本窗终态保留项，不用于正面证据、Books或无遗漏断言**；不是声称精确v1无法下载，也不是安全信号无价值。定点重开条件：精确历史v1与官方首公开链可核且归本窗，才定点筛该版本；若归其他日期则留真实归属日线索。不为当前晚版遍历全部历史revision或重开92项。

## 4. 报告同步与局部复核请求

Moonshot按独立核实的26条（链接0–25）纠正，Nov7/Nov6停止边界不变。作者有限来源检查已收束，确定落窗候选清单1家族；arXiv共22个潜在贡献日期保留家族（首批7+追加12+本次3），另3个晚版信号仅版本/日期隔离，不计历史准入。宽查询数字不成为本窗家族分母。

请Ohm只核本文件前三节、README同步的六部分与执行检查。复用原notes已通过部分，不重复Project Fetch/追加12项；所有外部保留不授正面Coverage/Evidence。日级仍待独立局部复核，实际Books写入0。

实际执行检查：进行中V3通过；本日8份Markdown/40本地引用、尾随空白与46份JSON解析通过；限定diff-check通过（新文件另作直接空白检查）。完成态测试仅在内存切换状态为完成，不改真实复核结论，且仅返回“完成报告需要已结束且通过的复核结论”；按预期阻止假完成，不是完成态验收通过。root/Ohm真正通过后再同步正式状态并运行实际完成态校验。未stage/commit/push，未写共享Books、索引或学习状态。
