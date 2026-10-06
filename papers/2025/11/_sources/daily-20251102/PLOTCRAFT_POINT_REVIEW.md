# PlotCraft exact-v1 定点重开

身份：[2511.00010v1](https://arxiv.org/abs/2511.00010v1)，[精确HTML](https://arxiv.org/html/2511.00010v1)。本日窗口BJT `[2025-11-01T09:00:00+08:00,2025-11-02T09:00:00+08:00)`。原始HTML为 `plotcraft-v1.html`，同名receipt记录HTTP200、891111 bytes、实际检查时间。源稿标CC BY 4.0；以下为作者对证据边界的分析，未复现实验。

## 受影响判断与读取停止

root独立复核反馈已实际读取完整v1题摘/Introduction，否决“主要只增加题集”这一过窄关闭理由。作者只恢复§3.1/3.4、§5.2/5.4；读取其直接引用Tables 2/3，并用邻接§3.3的multi-turn样本构造、§5.1评价配置及§5.3人审分母核必要边界。未扩读§4训练机制、完整附录、代码实现或其他月材料。

改判：潜在贡献明确。可支持的增量不是榜单本身，而是将可执行图代码、复合视觉目标遵循和视觉质量分开测量，并展示简单Text2Vis成绩不能直接授权复杂图任务能力。此前拟关闭撤销；首公开未确认，不先授本窗准入或评分。

## 指定四节的必要证据

- §3.1：目标是依据指令、元数据和原始数据生成代码，使渲染结果满足指令；single-turn从零生成与multi-turn基于既存代码/历史和修改请求是两个任务条件，不能互换。
- §3.4：成功执行并产生有效非空图只是进入后续评价的门槛，失败输出计零；随后由Gemini-2.5-Pro分别判断任务遵循和图质量。任务遵循包括布局、图型、局部要求和完整任务；质量另测重叠/清晰度、布局、颜色、文本及格式。由此支持“无异常/有图不充分保证视觉目标正确”，不证明judge能识别所有数据语义错误。
- §5.2/Tables 2–3：作者观察Kimi-K2、GPT-4o在简单Text2Vis较好而复杂PlotCraft较弱。协议和分数定义不同，不能把跨表百分比直接解释成统一能力跌幅，也不能证明某个单一因素造成退化。
- Table 2的multi-turn反侧：GPT-4o的Task-Comp由1.60变1.51，而Quality由3.33变4.23；Kimi-K2分别为1.52→1.49和3.36→4.05。它们是不同任务条件的均值，不是同一初始产物逐轮前后配对。足以反对“refinement各项能力必然同时更好”，不足以声称用户feedback造成任务遵循下降。表中Pass Rate保留原标签，不擅自改称“完整视觉任务通过率”。
- §5.4：代码/渲染错误、未满足任务要求、图质量缺陷分为三类；错误布局/图型属于任务遵循，重叠与不可读文本属于质量。三类不能全归成编译/执行正确性，也不能把审美得分当成数据事实真值。

## 多轮与评价可信度边界

§3.3的491个multi-turn条件由弱模型初稿、人为加入常见错误和人工修改请求构造；不是每个受测模型自己的single-turn输出接着真实用户迭代。因此Tables 2的两列没有建立matched-initial-state/no-feedback对照，也没有证明任意多轮单调改善、闭环收敛或反馈的独立因果收益。

§5.1披露greedy、最大输出131072 tokens（不支持时按模型上限）、三次运行平均、闭源官方API与开源vLLM；未核硬件/精度/并发及端到端预算，不能授等成本比较。GPT-oss的ChatML对harmony适配限制由作者明确指出，不能把该模型反侧外推成固有refinement能力不足。§5.3的人审一致性来自500张PlotCraftor输出、三位标注者多数票；不授所有模型、所有失败类型或生产图表上的judge准确率。无需为这些较窄结论读完整附录。

## 首公开有限恢复：具名终态隔离P02-PlotCraft-Date

实际原证据保留如下，不把它们拼成虚构时刻：

| 材料 | 原字段/实际结果 | 支持与不支持 |
| --- | --- | --- |
| arXiv v1 history | `Wed, 15 Oct 2025 10:14:39 UTC` | Submitted，仅说明提交。 |
| 官方题名检索 `plotcraft-search-title.html` | `v1 submitted 15 October, 2025; originally announced November 2025` | 真实官方announcement月精度，仍不能分配02窗口。 |
| 官方11月标题切片 `plotcraft-month-title-slice.html` | show25/skip0，含2511.00010；无单篇日期 | 仅定位材料；未扩月表为题摘队列。 |
| DataCite `plotcraft-date.json` | created=`2025-11-04T03:48:23.000Z`、registered=`2025-11-04T03:48:24.000Z`；Available/v1=`2025-11`；Updated/v1=`2025-11-04T16:55:07Z` | 注册/更新不是首次公开；登记上界在窗后，不能证明窗内，也不独自证明此前从未作者公开。 |
| 作者项目API `plotcraft-project-meta.json` / `plotcraft-project-commits.json` | created_at=`2025-10-14T15:40:40Z`；完整当前6commit页最早10/14，10/29为eval scripts | 仓库创建/commit时刻不等public transition，不证明论文正文首公开。 |
| 作者10/29 README精确commit `plotcraft-readme-oct29.json` | 原contents API成功；是评测脚本说明，无论文正文/首公开公告 | 支持历史artifact身份，不分配论文事件。未把artifact和论文公开混为一个事件。 |

有限失败也保留receipt：两个历史list URL HTTP404；两个raw README网络失败后仅对10/29用contents API恢复；官方advanced announcement查询题名/ID的11/01–02、11/03–04及11月范围均无结果，然而无日期题名查询有该篇。实际表单确有`announced_date_first`字段，但范围查询未通过正对照，不能把零结果当公开日排除证据。有限外部检索没有返回作者精确首公开公告。

本次不再继续猜接口或展开全文队列。需要：带精度/时区的实际官方首次公开公告，或作者论文正文首次公开记录及可证明的上下界；只有范围完全落窗才授本窗候选。收到后只重开2511.00010v1日期及依赖准入，不重读已有效的四节。此保留不支持Coverage/Evidence通过、Books或无遗漏；不是重新以日期hold替代贡献判断。

## 给root的具体owner对读（只读，不授采用）

已先读取PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、ROADMAP及LEARNING_STATE相关checkpoint，再对读owner和邻接。唯一拟owner为 `PLATFORM-EVALUATION-SYSTEM`，Ch66 `books/part-06-ai-infrastructure/66-evaluation-system.md`；不另外在Reflection重复拥有视觉评价机制。

现有正文实际覆盖：Ch66“HTTP成功只是质量判断的第一道门”区分runtime/contract/semantic/outcome；“Evaluation Identity必须包含Harness与Environment”保留adapter条件；“第二个不变量”要求分布和scorer匹配。Ch65收尾将资源事实交给评价，Ch67开头只负责趋势而不定义质量，交接已有，不需要共享结构调整。Ch80“Stopping Policy”已要求可核修正和停止，不应把本篇两条件均值写成反馈收敛定理。

具体剩余差额是**可执行且非空的复合图产物，还应分别验收指令布局/图型和可读性/格式；修订条件下两个维度可能不同向**，而不是抽象“执行成功不等于正确”或论文名缺位。若root判有必要保留实例，位置是Ch66上述第一道门段落之后、转入“从目标到证据”之前，以一个受限实例承接现有success交集，并就近保留固定faulty-code条件与judge分母限制。若认为现有论证足以承载，已有覆盖/仅报告亦成立，不能因此反向恢复原贡献关闭。

由于P02日期未核，本日实际处置仅隔离潜在贡献，无Books采用/写入/POST。root尚未核本定点证据与owner差额，不能写Books或日级通过。
