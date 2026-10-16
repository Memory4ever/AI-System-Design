# SoCE 单一Ch35段落／本人note逐字PRE提案

## 1. 已发生层与本次范围

作者Noether已实际完整读回Ohm本日独核§1–5及root转交：SoCE官方Meta publication **2025-11-18 date-only事件**、精确arXiv2511.13254v1必要Source/5分与唯一`TRAIN-CHECKPOINT`当前Ch35差额通过。只该机构披露事件，不认证论文最早公开，不以Submitted补日；旧两正式完整row/日期/score/原window/连续§4保持。Gemini另Research Nov18公告同family，按Ohm4在旧行外说明，不重复评分。

本次为**逐字PRE提案，尚未写Books/未获窄锁**。已实际加载PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、此前fresh完整ROADMAP与State当前本日路由，并读Ch35开头/374–485及末65行、Ch34 423–462、Ch36 1–58与Ch66 169–190。确认现有task-vector双mask/overlap分支与转换后重验没有承载平均前类别互补的子集/系数联合选择；Ch66已有公开开发反馈/独立holdout权限分离，不再建第二owner或重算成熟原则为新机制。

当前共享Ch35有既有/并发cached修改，原内容与索引保护，不认领或回退。root最新总92/132，本日未接纳；本人不写State/index、不stage/commit/push。原方法/Source层直接复用Ohm3/5，不重PDF/所有owner或全Source。

## 2. 正文插入锚点

只在`books/part-04-training-system/35-checkpoint.md`的“Checkpoint转换与发布”内，现有ReasonAny task-vector自然段及其source-family注之后、下面完整原句之前插入**一个自然段**，不改ReasonAny或相邻现有文字：

> 第 66 章将进一步要求 equivalence Evaluation 绑定 source/target artifact、转换配置、runtime、dataset 与 scorer identity。只有证据可追溯到实际被部署的 target artifact，Registry 和 release gate 才能消费它。

## 3. 拟插正文（逐字）

```markdown
对同一基座、架构与张量坐标兼容，且均已完成后训练与对齐的最终 checkpoints，统一平均是成本和语义都容易解释的起点，但总体分数接近不等于各能力类别互补。另一条受限分支是在类别评分矩阵中寻找低相关的能力切片，从各切片选择 checkpoint experts，再搜索非均匀平均系数；因此“平均哪些模型”和“用什么权重平均”必须与用于选择的类别样本、评分及搜索过程一起成为 artifact build 的输入，而不能只记录最终权重文件。[同基座 checkpoint 的受限对照](https://arxiv.org/pdf/2511.13254v1)区分全体均匀平均、选定子集均匀平均与选定子集加权平均，支持这个选择分支，不证明任意架构、任务或弱互补类别都获益；其公开榜单分数参与选择和调权，独立开发集只是后续建议，不能把所报结果当测试独立的泛化证据。候选加载、类别评价、系数搜索及目标验收仍有费用，“不再训练”不等于零成本。由此推导的发布要求是保留 source checkpoints、子集与系数、选择人口和 scorer lineage，再按第 66 章分离开发反馈与独立最终验收；类别样本不足以分辨互补、回归不稳或验收失败时，保留均匀方案、单一已验模型或不合并，而不是让搜索结果直接取得 release 资格。<!-- source-family:SF-2025-ARXIV-2511-13254 -->
```

## 4. 本人Review note（逐字）

只在Ch35末尾`Review notes`的现有最后一条ReasonAny note之后新增本人的**一条note**；不改其他notes/trace：

```markdown
- `SF-2025-ARXIV-2511-13254` — Daily `2025-11-19`补充窗口Nov18；[Meta官方publication](https://ai.meta.com/research/publications/souper-model-how-simple-arithmetic-unlocks-state-of-the-art-llm-performance/)明确Nov18日期，仅作机构披露事件；[SoCE精确v1 PDF](https://arxiv.org/pdf/2511.13254v1) §3/Algorithm1、§4.1三对照/§4.2.3条件及§7.1支持同base、架构/张量坐标兼容且均已完成后训练与对齐的最终checkpoint的类别互补子集/系数选择分支；张量兼容不代替posttraining/alignment资格。公开榜参与选择，独立dev仅后续建议，不能授测试独立泛化/普遍鲁棒性；选择人口、artifact lineage、独立最终验收及回退是受此边界约束的工程推断，不冒原论文已验证release流程。晚v2的precision-collapse叙述不回填v1；未运行代码或复现实验，不授生产效果。
```

## 5. PRE需要核的最小差额与写入门

请root转Ohm逐字核§3/4：同基座/对齐前提、低相关类别到expert子集/系数、三对照/弱互补边界和§7.1公开榜限制、全成本及“由此推导”的发布/退路权限；与前面的ReasonAny calibration-mask分支及后面的equivalence lineage承接。只有这一个自然段/一条本人note，无新小标题/表/第二owner，不把默认均匀平均写成过时错误。

PRE通过仍不是写批准；仅root明确授此正文位置与本人末注窄锁后，作者才按通过的逐字稿实际写入并读回，随后Ohm非写入者作actualPOST，root再接纳/释放。任何同锚点并发变化先读当前片段，不替换整章/旧cached，不借其他lane锁。当前未写Books、未POST、不预签整合或DAY；其它本日有限来源/arxiv/六节普通继续。

## 6. 已实际读回Ohm§7／仅人口限定修正

作者实际读Ohm逐字PRE§7：其它域已通过，仅“对齐”会把张量坐标兼容与后训练alignment混同。现§3正文开头及§4本人note均已明确“均已完成后训练与对齐的最终checkpoint”，张量/架构兼容另列；不再涵盖未对齐或不同训练阶段模型。只这一个人口限定及对应note消歧，原其余逐字稿不变，交root转Ohm定点核，不重Source/owner/PDF。当前仍无root窄锁、未写Ch35、无actualPOST，不以PRE其余域通过代写批准。

## 7. root窄锁后实际保存／作者自读与POST交包

2026-10-15 14:08 BJT后，作者实际读回[root写前批准§1](ROOT_INDEPENDENT_REVIEW_20261015.md)、Ohm修订PRE§10及后续§13的窄锁交接，并再次读Ch35当前转换发布段/ReasonAny后锚点/末note与相关邻接。上述§1/5/6的“未获窄锁/未写”是当时状态；本节是后续真实动作，不改写历史层。root当前93/132，本日尚未接纳。

已按§3/4逐字实际保存至`books/part-04-training-system/35-checkpoint.md`：L443单一自然段，在ReasonAny source注之后、L445 equivalence句之前；L644本人末note，在既有ReasonAny note之后。无新小标题/第二owner，不改原ReasonAny、equivalence、其他正文或他人note。作者实际顺读新增全文及两侧、本人末note，确认后训练alignment人口与张量兼容分开，三对照/公开榜选择限制、全成本与工程推断/退路仍在近文；这里是作者自读，不冒独立POST。

写前unstaged为空，cached为外部6新增；写后本次unstaged仅4新增/0删除（正文、note及两空行），cached仍6新增/0删除，index blob仍`b297d7a0a0de01d97cd8a3b74d6c9944cd7ba4d8`。结构对比确认两新增字符串与§3/4 fenced逐字稿完全相同，移除这两处后与写前完整文件逐字相同；限定`git diff --check`通过。该结构检查只证明本次差额与范围，不代替语义审阅。未stage/commit/push，未写State/index/其他Books或README完成态。

请root转Ohm实际POST：完整读L439–445的前段/旧source注/新增/后句，以及末Review notes本人note及前注；复用已通过Source/PRE，不重PDF/所有owner。由Ohm非写入者实际保存POST后，root实际读回接纳/释放本锁；作者不自行释放、不预签整合或日级DAY/FINAL。内部send_input不可用，仅保存此包并返回root，无普通chat/UI替代或新task。

## 8. 实际POST15／root接纳释放后的本人注行政同步

作者已实际完整读回Ohm§15及ROOT_INDEPENDENT_REVIEW§2：非写入者真实POST、root正文/两侧/本人注及前注/完整diff实际读回通过，本项整合接纳并释放Ch35窄锁。按root仅本人注授权，在L644末追加这句行政事实：“Ohm独核§15真实非写入者POST通过；root独核§2实际读回接纳本项整合并释放Ch35窄锁，不代表Nov19日级验收。”正文及该note原研究/日期/版本/边界文字未变，未改他注或State/index；请root只读回该行政差额，不重Source/PRE/正文。93/132不变，Nov19未计入，继续本日Source/arxiv/date/six。
