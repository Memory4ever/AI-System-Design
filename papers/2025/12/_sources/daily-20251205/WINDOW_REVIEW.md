# 12/05 原始窗口与作者判断

启动2026-10-02T18:28:12+08:00，无本日checkpoint；本轮必要读至18:32:40。已重读AGENTS、研究/Report合同、每日组与主题说明、Prompt、ROADMAP。窗口Dec4 01Z至Dec5 01Z。

## 来源邻接

实际独立重读[固定原始目录](../daily-20251201/RECOVERY_NOTES.md)的14源邻接，只复用原始入口/字段，不沿用前日报结论。OpenAI本轮重新解析RSS，Dec4/5只返回Dec4 19Z OpenAI for Australia：国家合作/基础设施承诺，没有披露新的训练或推理机制，贡献关闭；不以data-center名词准入。

Anthropic本轮原生340420 bytes正文，`article:published_time`与`datePublished`均`2025-12-04T17:00:00.000Z`，完全落本窗；modified July8 2026只说明现页维护，不替代公开字段，不将后改时间当新事件。Method、Augmentation versus automation、Conclusions and limitations、Appendix必要部分已实际读。

Google 2025Blog第1页相邻Dec3 MSEB/Dec4 Titans+MIRAS/Dec10；本轮原生186939 bytes核心说明。MSEB日期请求已隔离不重复；Titans/MIRAS分别[2501.00663v1](https://arxiv.org/abs/2501.00663v1)和[2504.13173v1](https://arxiv.org/abs/2504.13173v1)完整题摘/版本实际读取。neural memory与四项memory/objective/retention/algorithm核心机制均旧家族，无本次新机制或重要修订说明；博客介绍/宣传不重记首次论文。Ch22约611–620“将写入变成学习过程”实际已承载该具体机制，不因主题已覆盖而排除新的反证；本次原文未给这样的新事件。DeepMind原始第3页Dec3/Jan9，下个无本窗条目。

其余逐源按本窗比对：Meta第4页Dec1/Dec12、DeepSeek正确API Docs Dec1/下一2026、KimiOverview26项最新Nov7/changelog Nov6、ERNIE2/2页Nov21/Dec9、MiniMax英13项和中文Oct27/Dec23，入口范围内未见窗内新条目。Seed2025paper首段Dec15/Dec2/Oct22与Blog Dec16/Dec2/Nov27夹本窗，官方PublishDate字段不补日编码精度。Qwen动态历史、HunyuanAll11项2026/旧Research、Z.aiAll第2页Dec7终点、MiMo无date/旧More仍为历史外部缺口；不再重复失败端点、不授Coverage或零事件证明。

## arXiv

实际四条`site:arxiv.org "4 Dec 2025"`分别加transformer training optimization、GPU inference cache kernel、multimodal world model VLA、agent reinforcement evaluation。命中设计Conductor May2026、SALP Dec25、weather radar Dec20等越窗/范围外；检索未严格落实日期，停止。SpatialReasoner具名摘要定点打开，不按索引归日。

官方cs.PL月首段1–25实际标题查漏，一页跨到Dec17提交的具名材料，停止，不翻75项或把宽列表变待关闭库存。只读八个可能相关题名的精确v1完整摘要：

- [Tensor accelerators 2512.02371v1](https://arxiv.org/abs/2512.02371v1)：Halide equality-saturation tensor指令选择且与fusion共存，潜在编译执行机制；不把非LLM图像kernel数字外推。first-public隔离。
- [Lumos 2512.02966v1](https://arxiv.org/abs/2512.02966v1)：graph上的probabilistic DSL、IID prompt抽样与statistical certifier分工；潜在可证评价协议，不用90%安全标题作保证。first-public隔离。
- [Beyond Code Pairs 2512.03086v1](https://arxiv.org/abs/2512.03086v1)：外部compiler/runtime反馈验证的多轮翻译训练数据，对数据单位/功能一致性有潜在增量；first-public隔离。
- [SpatialReasoner 2512.03284v1](https://arxiv.org/abs/2512.03284v1)：按文本问题调用空间工具、adaptive exploration reward抑制冗余观察，潜在主动感知机制；first-public隔离，不采用最高分/图数速度结论。
- 2512.05516v1 reduced precision/AoS–SoA提交Dec5 08:19:43Z；2512.06442v1 MLIR abstract transformers提交Dec6 14:09:51Z；2512.14805v1共享程序状态Dec16 18:41:50Z；2512.15766v1 LOOPRAG Dec12 11:09:48Z；2512.15834v1工具调用speculation Dec17 18:22:44Z。完整题摘用于身份/边界，不按月号归日；均本窗之后提交且无更早正文证据，仅窗外线索。MLIR的transformer是抽象解释算子，不是attention，不能关键词准入；AoS研究对象为粒子模拟，不当AI System性能采用。

必要个体公告权限有限替代沿用已实验证据：abs提交、月身份、announced年月/OAI与失败的历史日list/catchup/API均不能授first-public。当前接受具名历史new/RSS/email或作者首发正文，一项一次请求，不不断查同端点。上述四潜在贡献不评分、不正面采用，不因外部日期删池。

## Anthropic Interviewer准入、证据与Books

原文：[Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI](https://www.anthropic.com/research/anthropic-interviewer)。日志只见聊天输出 → 访谈触及输出后加工且自动化口径与日志不同 → 测量人口/边界不同不能合成实际自治能力。此窄增量已通知root待校准，不以“新访谈工具”名称或三阶段流程准入。2+1+2=5，作者标准审阅。

Method的planning含人类review、interview自适应提问、analysis人类与LLM主题归纳，1250人来自crowdworker招募，不是随机全体用户；访谈10–15min。Augmentation段65/35自报与47/49日志属于不同样本/渠道，可能为聊天后编辑、provider不同、回忆/社会期待偏差，不能证明日志错了或同一任务发生质量变化。Limitations明确selection/demand characteristics、静态截面、自报非objective、text-only漏情绪、研究者解释、西方样本和非实验因果限制。本文不采用scientist领域研究结论，也不外推生产率/主观满意为模型机制性能。模型版本、hardware/precision、数据分析scorer完整版本、运行成本/SLO为Not Disclosed；没有实现验证或复现。

Books实际对读：PLATFORM-EVALUATION-SYSTEM Ch66“从目标到证据”约79–110：eligible population、slice、metrics/scorers、标签生成链/轨迹粒度/缺失标签与人/模型分工；相邻Ch65 Queue/Fair share谈资源政策不是语义成功，Ch67开头持续observed health不定义质量。已有正文实际覆盖这条测量对象/人口/结果口径边界；采用为已有覆盖，不改书，不将未披露instrument模型机制写成长知识。

普通扫描/筛选/必要阅读待办0。上述first-public和旧目录隔离不支持完整覆盖；root仍需准入、证据和具体已有覆盖核验。本日作者ready，继续12/06。
