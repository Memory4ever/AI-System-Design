# Handoff Debt — necessary Source → owner proposal

作者：supp_20260604_author。Reader R1已通过准入/Jun03日期；本文待独立必要Source/owner/PRE，未写Books。

## 必要证据与评分

精确版本[2606.02875v1](https://arxiv.org/html/2606.02875v1)，完整HTML实存SUP_CORE_2606.02875v1_20261024.html；已读§2–6、Limitations、Appendix B runtime/note generation，支持与关键反侧已足够，不遍历其余无关附件。2+2+2=6；具体知识gap触发受影响深入，非机构/章节映射计分。

- §2/§3 intervention：固定同一predecessor checkpoint repo、同一handoff point与successor，仅换repo-only/rawtrace/summary/structured视图。中断点来自observable source edit/validation/post-failure edit，不看官方solution；successor把交接文本当historical evidence需复核，非真值。
- §4：SWE-bench Verified固定seed选75源任务，181 handoff points；每successor724 runs，3successors2172。Qwen3.6-27B单一主predecessor；Qwen/Gemma4-31B-it/Devstral-Small2-24B successors。OpenHands-style textual tool protocol，provider-native calling disabled；local vLLM/RTX PRO6000 Blackwell Max-Q，dtype auto/max-num-seqs16/mem0.95，4h timeout/500steps，不强制统一context。仅此受限runtime，不模型总榜。
- §5/T2/T3：相同checkpoint下context-bearing views减median agent events20–59%、累计prompt tokens42–63%；rawtrace起始prompt较大仍可降后继累计，events不是walltime。matched bootstrap95% CI均below0；同一handoff/view主实验单run，40point×3attempt补充保持43–59%events减。181points来自75task，不能叫181独立源问题。
- §5.2/§6：note-based solved gains在Qwen/Gemma不显著、Devstral显著；Gemma Needs-completion切片notes还可小幅退。raw/summary/structured无普遍排序；already-solved-preserve与needs-completion必须分账，不能以总体pass掩盖继承未完成工作的问题。
- Appendix B：summary/structured由predecessor侧temperature0、1600token cap生成；生成notes成本明确**不计入successor events/prompt tokens**。所以只支持交接后的rediscovery effort，不作全流程token/费用、latency、GPUhours净收益。Completion tokens/wallclock保日志但不作cross-view比较。无实际复现、任意生产可靠性或可维护性证明。

## owner与差额

已读Books三context，ROADMAP owner PLATFORM-EVALUATION-SYSTEM/Ch66；实际正文开头与末节交接、4310–4388完整相关邻接、上下行共享source markers；Ch65/67开头交接用于确认评价不是scheduler/monitoring。Ch66体量7221行，未声称通读全章；本次只读受影响论证与精确缺口。exact Handoff/02875查无现有身份；4345–4350的Long-session Stamina讲同session连续request的状态积累与恢复成本，**没有固定checkpoint、切换后继与handoff视图来隔离resumability**，不可因词相似给NC。

拟在该stamina两段与原end marker之后、下一24124 start marker之前插入下列两段，无新标题、不改旧段。root唯一实际writer；以下不是授权或实际整合。

## PRE逐字段段落提案

上锚完整段：

长会话更接近真实 workload，也引入任务顺序效应、提前终止删失、环境漂移和昂贵 replay；一次较晚失败不能自动归因于 Context 长度或模型遗忘。作者实验只支持其任务序列、工具与 evaluator，不能外推为生产可靠运行时长；短生命周期 Agent、独立 issue 或状态可完全重建时，普通单任务回归仍是更清晰的基线。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19613:end -->

拟增正文：

任务还可能交给另一个执行者，而不只由原 Agent 持续运行。此时应固定同一中断点的 repository snapshot、原任务和后继模型，仅改变可见的交接视图，分别比较只见文件、完整历史与压缩笔记；否则后继能力、已有修改和上下文质量会混成一个“可恢复”分数。最终功能通过与交接后的再发现代价应分账，已解决状态的保持也不能与未完成工作的续做共用一个成功解释。[受限 takeover 对照](https://arxiv.org/html/2606.02875v1)支持这条评价接口，不使交接文本成为事实真值；接手者仍须核对文件与验证证据。<!-- source-family:SF-2026-ARXIV-2606-02875 -->

更长的初始交接可能减少后续探索，但不保证整个工作流更便宜：笔记生成、状态冻结、隔离重放和独立验证均需计费，后继累计 prompt tokens 不能替代包含这些成本的端到端账。原实验中减少交互比提高 solved rate 更稳定，压缩笔记在部分后继与未完成切片还会退步，因而不能宣布一种交接格式普遍最优。完整 trace 过大或笔记证据不可信时，应保留必要验证记录、明确未知与原 repository 回归，让后继重新检查，而不是用“有 checkpoint”批准无损恢复。<!-- source-family:SF-2026-ARXIV-2606-02875 -->

下锚：

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24124:start -->
将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24124:end -->

Review notes拟增一条：`SF-2026-ARXIV-2606-02875`：2+2+2=6；exact-v1 §2–6/Limitations/AppB，fixed checkpoint×handoff view×successor分离恢复代价与最终pass；notes生成费用不含在successor账，model-dependent/有限runtime与单run主实验边界。未复现实验。实际写后需另一reader核。
