# Jun03 增量 — SkillRevise 单家族必要证据与 Books PRE

准备者：`jun03_skillrevise`；执行检查：2026-10-24 10:59 BJT。仅处理既有 Jun03 Daily 的 Jun02 BJT 自然日补窗中的 `2606.01139v1`；不搬动旧候选日期、评分、小时窗或连续旧§4，不扫描其他家族或日期。本文件是待独立 reader 核验的单元准备，不授 Source/Books/DAY 已通过，不修改 Books、Report、State 或 index。

## 1. 当前合同与有效层复用

已完整读取当前 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、ROADMAP；Sources 使用说明/每日/arXiv/材料恢复与 State 仅2026补查块。另实际读取 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE，以及下述具体 owner 正文和完整相邻段。using-agent-skills 用于限定研究阶段与修改范围，无代码实施或新任务分派。

贡献准入与日期复用[独立 R13](./SUP_INDEPENDENT_20261023.md#r13--jun03_exclusion_calibration三项拟排除独立准入校准2026-10-23非day)的这一家族有效层，不重审另两家族：一次执行失败不足以授权改写可复用 skill；原文以缺陷归因、保护既过行为、锚定编辑、重新执行及择优输出改变更新门控。公开归属为 **2026-06-02**：R13记录唯一v1提交 May31 10:19:13Z、精确 DOI 的 arxiv.content/findable registered Jun02 04:08:17Z，与适用公告日程联合限制在 Jun02 BJT；不是把提交日或 registered 改称实际公告时刻，也不授全球首次正文保证。已核身份/题摘/history/有限风险信号仍有效；不因当前存在后版本而对比版本、不以后版补v1。

## 2. 精确原件、采用命题与评分

原文：[SkillRevise exact-v1 HTML](https://arxiv.org/html/2606.01139v1)。HTML-first 可正常取得，持久原件为 [SUP_SKILLREVISE_2606.01139v1_20261024.html](./SUP_SKILLREVISE_2606.01139v1_20261024.html)，SHA256 `1a2486f4ad0c752f158f2f087a8d25fc29fdcc2e372e7d85021a0a54c62b09c9`；未以 PDF、latest 或代码替代。实际读取§3.1–3.4/式1–9、§4.1–4.2/T1、§5.1–5.3/T2–4、Limitations、Appendix E；为 no-skill 反侧定点读 Appendix C，为泄漏声明权限定点读 Appendix D。§5.4仅用其设置及结论限制，不以其外部排行榜采性能。未遍历全附件、全代码或复现。

拟采用的最小命题：**已有 skill 的修订权限要先由执行诊断支持 skill-level defect，再把修改绑定到当前证据、保持约束与可观察执行动作；继续搜索所用候选和最终返回的 best-observed artifact 是两种状态。** 不是新发明反思循环，也不采用“结构化修订普遍优于自由重写”或“局部 utility 证明可迁移”。

评分 **Design Delta 2 + System Reach 1 + Durability 2 = 5**：新增的是程序记忆维护中的具体修订/保留接口；影响本地 skill artifact 与其执行反馈，不把能关联平台/训练/工具等章节当跨层贡献；缺陷门控与状态分责可复用，但未形成普遍理论。按5分先标准审阅；因实际 Ch77 确认缺少该更新接口，按研究合同§4对拟整合命题深入读取关键机制与反证。评分不因 Books 选择或访问成功上调。

## 3. 必要方法与关键反证

### 原文实际机制

- §3.1：Diagnosis由 verification specification、failure attribution、preservation constraints 组成；不仅存错误，还存已经通过的检查及可能支撑它们的选择。归因没有 skill-level defect 证据时，§3.4 明确 abstain，不因任务失败就自动编辑。
- §3.2–3.4：固定 Principle Memory 存通用修复模式而非任务答案；检索先取候选，再按当前诊断的证据要求及 transfer constraints 绑定，检索命中不等实际可用规则。七条初始化原则不构成通用 taxonomy。
- §3.3：revision trace保存 evidence-to-edit mapping；execution anchor说明执行者要做什么、查看什么 artifact/evidence、指令置于何处。它约束修订提案的可检查性，不证明生成模型必然遵从，也不是执行授权。
- §3.4：有限预算默认B=3；候选重新执行。下一轮搜索可以继续用新候选，即使它不是当前 best；最终从初始skill加全部已评价候选中按utility选择，并非返回最后版本。式9的 success、efficiency、transfer、interference 是一般部署 utility 表达，不是声称所有实验都测齐四项；二值verifier分支只在成功后给予效率信用，防止早退/跳步被当节省。
- optional absorption是评价后维护；主benchmark固定原则库，没有从测试任务在线吸收以改善后续测试的设置。不能把episode更新候选等同长期库自动晋升或永久可信。

### 评价条件、收益与替代解释

§4.1：三组 verifier-driven 任务，SkillsBench主要可比切片86，SkillLearnBench-Random标称50，SWE-Skills-Bench-Hard标称70；五executor，author/reviser通常GPT-5.5，executor identity和Codex/Claude Code harness见T1。T1中若干行实际分母不是标称任务数，不能合并成统一人口或跨模型净收益；例如Kimi的Skill v0在两个suite仅11/41和23/54。每个candidate会额外重执行，maxrev3的best-observed与一次no-skill/one-shot不是等总预算的算法优越性证明。

作者T1在GPT-5.5/Codex条件报告31/86 no-skill、34/86 Skill-Creator、35/86内部v0、53/86修订返回；这些只说明该任务集合/selector下的作者结果。Opus-4.7在SWE-Hard修订31/70仍低于no-skill 32/70，不可写成五模型三套全优。§5.1迁移在GPT-5.5已成功的57任务子集上，不是全任务独立跨域泛化；executor-specific通常更好，不能把固定artifact可迁移写成executor无关。

关键归因对照是§5.3/T4：同一86任务切片，排除non-runnable fuzzing和GitHub-API依赖任务；controlled variants在可用时复用初始S0、executor、verifier与maxrev3。完整53/86，去Diagnosis28/86，去Preserve42/86，去Anchors44/86，去Principles45/86，但 **Free-form Revision 52/86，几乎持平完整方法**。因此可采用诊断/保持/锚的可审计接口，不得把所有增益归因结构化原则库、宣称每个模块独立因果成立或显著胜自由改写。这里没有披露足以支持本文统计显著性结论的重复/不确定性控制，本次不作该断言。

§5.2/T2–3按best-observed计分：增加预算扩候选集，收益递减；maxrev5仍有38/86选择v0。它支持“最终版本不是最后版本”的实现语义，不证明任意新任务不退步或自适应停止已解决。§5.4的ALFWorld原则吸收另用25 calibration tasks和cleaned100 valid-seen/unseen、Qwen3-8B，且改变有无principle bank；外部方法表是不同backbone/预算的contextual positioning，不当同协议比较。

### 限制与停止位置

Limitations/Appendix E：visible verifier稀疏或错位会让诊断修错对象、过拟合可见断言、保护错误假设；best只在已观察候选与固定utility内。Appendix C明确maxrev3 **没有no-skill fallback**：存在no-skill能成功、Skill-Creator和SkillRevise均失败的任务，不能把“保留旧skill”改写成“至少不差于无skill”。程序记忆退回旧版、冻结、人工规则或no-skill是项目部署建议，不是作者已实现fallback。

额外author/reviser调用、诊断、原则检索/绑定、全部candidate执行、verifier、token/tool/step/wall-clock、artifact版本与后续独立任务回归均需计费；成功候选也可能因更长/更贵流程降低总体utility。本文未给可外推的统一硬件、precision/quantization、batch/concurrency、latency SLO或完整长程端到端成本，记Not Disclosed；输入/输出长度依具体任务，不是统一benchmark条件。未核实现、计时或实验复现。Appendix D只是作者对抽样artifact的人工泄漏audit、未见答案泄漏，未给足样本量及独立性以认证全池无泄漏；filter声明不等无hidden requirement过拟合。上述证据已足以支持受限接口及关键反侧，到此停止，不为追求全套结果审全附件。

## 4. 唯一 owner 与真实差额

唯一owner `AGENT-MEMORY`，[Ch77](../../../../../books/part-07-agent/77-memory.md)。实际读取本章开篇/上下文边界、Memory Write下failure receipt段完整邻接、§从原始轨迹到派生策略（729–866，含PolicyBank、D2Skill、Ctx2Skill及memory-policy交接）、Failure Trace/Rule/正例过滤段、Search-derived Skill held-out段、Verifier评估边界、marginal credit、Propose-Probe-Commit与章末交接；并读取相邻Ch76、Ch78的职责开篇，避免让skill文本取得工具执行权限。

已有覆盖不是泛主题：failure receipt段已覆盖反思pending与writer接纳；PolicyBank段已分遵从错误/规范缺陷；D2Skill段已分policy进步与skill效用；Ctx2Skill段已明确统一probe评价历史版本而不只发布最后文件；held-out段已拒绝仅凭search结果发布skill。这些不重写。**尚缺的单一差额**是：在已有skill的本地修订episode中，诊断缺陷→保持ledger/锚定动作→候选重执行的更新资格，以及search-base可前进但返回best的双状态。它与Ctx2Skill的跨历史probe选择为条件分支/原理复用，非直接谱系、替代或新层级owner。

决定：建议一处最小整合，尚未写入。只在Ctx2Skill完整段之后、Memory policy段之前插入下述单段和唯一marker，不新建章节、不重复best-selector机制或加实验数字。待reader必要证据/owner/PRE通过与root明确新授窄位后，root方可写Books；本准备者不申请整章锁。

## 5. 逐字 PRE（当前原文；只提案不写Books）

完整上锚：

```markdown
即使policy权重冻结，持续追加的context-specific skill也可能被后期更难的自造任务带偏，因此最新版本不自动优于历史版本。一个受限选择接口保留每轮成功与失败的代表性probe，循环结束后冻结同一组probe，让各历史skill版本重新作答，再共同检查困难项收益与原有容易项保持；选中版本绑定context、policy和judge身份，而非只发布最终文件。[Ctx2Skill的局部回放对照](https://arxiv.org/html/2604.27660v1)支持比较这条分支，不使其乘积选择分数成为无退步保证；由同一模型系统生成并判分的probe仍可能共享偏差，也不能认证未见任务或独立事实。候选保存、跨版本重答、判分和部署skill额外prefill均计费，原context并未因此消失；标签、任务人口或版本兼容失配时，回到已验证旧skill、固定人工规则或无skill基线，不让一次自评胜出直接获得执行权限。<!-- source-family:SF-2026-ARXIV-2604-27660 -->
```

拟插入完整单段：

```markdown
选择历史版本之前，还要界定本次是否有资格修订已有 skill：任务失败若没有支持 skill-level defect 的执行证据，就保持该 artifact，不把一次失败直接翻译成长期规则。一个局部修订分支把 verifier 要求、失败归因和已经通过的行为分别记录，只将满足当前证据与迁移条件的修复原则绑定到修改，并用“要执行的动作—应检查的产物—指令位置”锚定编辑；候选重新执行后，后续搜索可以沿新候选继续，但最终返回的仍是已观察 utility 最佳者，而非最后生成者。[SkillRevise 的有限对照](https://arxiv.org/html/2606.01139v1#S3)支持这种接口组织，自由修订却接近完整方法，不能据此宣称结构化修订普遍更强；保持约束与 best-observed 都只受可见 verifier 限定，原实现也没有无 skill 回退。诊断、检索、全部候选执行和独立新任务回归均有成本；反馈错位、修订净效用不足或旧行为受损时，应冻结修订、保留旧 artifact 与原 trace，再由当前 workflow 选择已验证旧 skill、人工规则或无 skill 路径，不让局部择优代签迁移、安全或执行授权。<!-- source-family:SF-2026-ARXIV-2606-01139 -->
```

完整下锚：

```markdown
Memory policy 本身也可能成为可学习、可版本化的 procedural asset。固定 write/update rule 易审计，却难适应不同 interaction pattern；直接让 Agent 自由改写 memory 又会放大偶然成功、prompt injection 与自确认。中间路线是把每项 memory skill 拆为 applicability condition、extract/update procedure、source episodes 与验证结果：
```

建议本人Review note（仅root写入时随同，不在本准备写Books）：

```markdown
- `SF-2026-ARXIV-2606-01139` — Daily2026-06-03补Jun02；SkillRevise exact-v1 §3/式1–9、§4/T1、§5.1–5.3/T2–4、Limit/A.C–E必要域，2+1+2=5，具体修订门控gap深入；仅skill缺陷证据/保持与anchor、search-base和best-return分责。保free-form近持平、可见verifier过拟合、无no-skill fallback及全执行费；不采普遍胜出、无退步、独立迁移或安全，不核实现/复现。准备与独立PRE/实际POST状态以本日SUP/REVIEW为准，不预Source/Books/DAY。
```

## 6. 剩余验收

必要Source、评分与具体owner/PRE交独立 `jun03_checkpoint_reader`。本文件不充当独立审阅。若root采用，仍须实际写入后由非writer完整检查新增段/完整直接两侧/本人注与限定差额，再更新报告和2026 State停点；不预记整合或增加153/279日级数。其他家族/发现/来源工作不在此单元验收，亦不由本文件关闭。
