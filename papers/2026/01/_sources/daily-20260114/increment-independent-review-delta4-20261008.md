# Jan14：四项必要 PRE 独立复核

复核者：`/root/review_jan15_delta`。本记录仅属于 2026-01-14 Daily 的遗漏补充，补充窗口固定为 BJT 2026-01-13 完整自然日；不改变原 17 项、原窗口或评分。2026-10-08 是复核时间，不是报告窗口。没有修改 Report、Books、LEARNING_STATE、索引，未 stage/commit/push。

## 范围与证据级别

恢复时重新完整读取 AGENTS、当前研究/报告合同、Research Prompt、ROADMAP；RESEARCH_SOURCES 仅使用说明与 Daily 分组，本日停点仅 `supplement-20261007.md`。开始 Books 判断另读 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE 和实际 owner/邻接。本组只核作者 `/root/supp_jan10_close` 具名 prepared 的 06377、06799、06860、07782；旧 124 AB 校准只复用准入，不代必要原文或 actual Books。

作者提案：`increment-owner-proposals-20261007.md` 前部四个 ID 节，不是末尾其他候选。实际完整阅读必要原件：

- `increment-necessary-core-2601.06377v1-20261008.json`：§2/3/4/5。
- `increment-necessary-core-2601.06799v1-20261008.json`：§3/4。
- `increment-necessary-core-2601.06860v1-20261008.json`：§3/4/5。
- `increment-necessary-core-2601.07782v1-20261008.json`：§3/4。

日期原件定点核 `increment-date-bounds-rest-20261007.json` 四个对应 rows，结合本日既核官方 announcement 日界，只记 BJT Jan13，不以 submitted 时间重分窗口。四个当前官方 abs 另实际轻读：[HiMem](https://arxiv.org/abs/2601.06377)、[CIRAG](https://arxiv.org/abs/2601.06799)、[ET-Agent](https://arxiv.org/abs/2601.06860)、[ToolQP](https://arxiv.org/abs/2601.07782)。06377/06799/07782 current v1，06860 current v2；未见明确撤回/纠错说明。本次方法/评价仍采用上述 exact-v1；版本变化不自动触发全版本史审阅。作者另存 `increment-current-identity-ready6-20261008.json` 前四观察，与实际轻读相符。

## 06377 HiMem：5 分具体 Existing PASS

实际读 Ch77:78–153、344–386、1655–1667、1738–1751。原提只在 typed transition 邻近寻找 gap，遗漏本章已有的具体读写链：379 的 query sufficiency controller→source pointers 升级 raw→核验后有 provenance 的 derived 回填且不覆盖 raw；1661 的 immutable episodic source、consolidator proposal 与 promotion 反例；1746 的 retrieval-derived mutation proposal→一致性/冲突/回归检查→commit。90–148 的 target/evidence/expected-version 门负责实际修改。

因此拟采用的长期判断已有承载，不新增正文。这里不是声称现有正文逐字实现了 Note-insufficient AND Episode-sufficient 两个 binary flags；该双旗标是局部 routing 配方，不是新的写入权限。

必要负侧：Adversarial 被排除，不能授不可回答检测；Open 54.86 低于 SeCom 60.07、Temporal F1 22.05 低于 Mem0 56.37；Notes/KA/ME 消融不证明所有层级或双 gate 独立必要。只测 retrieval latency 不含 LLM inference，answerability/extraction/conflict/maintenance 额外费用保留。Optional forgetting 不贡献本文 performance，不授无限增长保证。准入保持 5，不因回归降为贡献前排除。

## 06799 CIRAG：5 分具体 Existing PASS

实际读 Ch76:542–620，包括 relevance/sufficiency/faithfulness、不足扩大 context、仍不足 abstain 与 rater 非真值（552–593），以及 successive negative windows/first-positive exposure 的边界。采用的长期判断是“不同粒度回读与 early-stop gate 分权”，现有正文可承载；triples→supporting sentence→document 的级联属于具体局部实现，不强写新通则。

Eq5/6 是指定 refusal-template 匹配，全部 refuse 仍默认 document 输出，不授可靠 abstain 或首 non-refusal 即充分正确。三任务各 1000 validation，T3 颗粒度收益依任务而变；T1 2Wiki 69.5 与 T2/T3 full 68.1 等数值不拼为最高值。离线 triples 抽取/维护、teacher distillation、reader 费用仍在；不采用未实际读 plot 的数字或通用 E2E 胜出。准入保持 5，无 Books 差额。

## 06860 ET-Agent：5 分最小 Integrate PRE PASS，未 POST

实际读 Ch33:113–153，并确认现有过滤/统计相关段。当前 139–141 的 warm-up reward/PPL estimator 是生成前 admission；尚不含“已支付每题 K=16 轨迹，correctness std 与 tool-count std 两轴→non-dominated fronts/crowding 选择 prompt”的后验训练人口接口。

允许的最小差额：零方差/既有过滤分支邻近一短段＋自身末注，解释前验估计与后验观测的分工、人口与预算变化；不是新 NSGA-II、advantage/credit 定义或 reward recipe。保 ordinary outcome/uniform sampling、随机 coverage 与 actor/tool/statistics identity。

决定性边界：工具次数方差不是真实 reward/gradient 方差保证。按 §4.2.3 Eq3，all-incorrect 且 format 正确时，组内 rewards 全 0，即使 tool-count std 很大；这样的 prompt 仍可能在两轴非支配前沿。因此不采用“front 必保 reward differential/必防 gradient decay”。Pareto 局部消融支持有限启发式，但不能授等总预算或全任务优胜；MATH 81.6 低于 ToRL 84.6、MuSiQue 28.0 低于 AutoTIR 30.9，Effi 的 correctness/toolcalls 不是 runtime，零分母接口不能自行补配方。K16 probes、排序、弃样、teacher/flywheel/tool 与训练全费保留。

共享 Books 锁由 root 授予；未写入，不可计 actualPOST。

## 07782 ToolQP：5 分最小 Integrate PRE PASS，未 POST

实际读 Ch78:592–637。当前 611–622 的 set-level/hyperedge discovery 与 execution authority 分权尚不含跨 query ranking aggregation。

允许的最小差额：该 discovery 分支附近一短段＋自身末注，解释同一 tool 用多个查询中最好一次 rank 汇总，避免重复同一命中被加性累计权重。必须收窄作者提案的“消 attemptcount bias”：best-of-many 仍有尝试次数带来的极值机会偏差。作为独立推论，单次独立 hit 概率 p 时 n 次至少一次 hit 的概率为 `1-(1-p)^n`，并非 paper 已证明 subtask 公平。

绑定原始 query/subtask、尝试预算、retriever/catalog identity；所有 query 前向/检索、teacher/训练/汇总费用保留。Ranking 只是 discovery proposal，不授 schema/prerequisite correctness、authorization 或 execution success。Table4 peak 53.9/59.9 低于 multiview 54.1/60.2 和 reranker 58.2/62.2，不称 universally best/高效；Format 转移 Code 22.6 低于 base 29.7。保 ordinary Top-k/RRF 与确定性 dependency expansion 回退，不自行补 Alg1 的未初始化变量。

共享 Books 锁由 root 授予；未写入，不可计 actualPOST。

## 组级结论

四项均完成本组必要 PRE：2 个具体 Existing、2 个最小 Integrate；均保持 5 分，无整体争议或贡献前排除。强保证反侧作为采用边界保留，不把局部贡献整篇排除。仅此四项，不自扩下一组、附件或版本史。本组完成不是 Jan14 READY/DAY；两个 Integrate 尚待锁、作者实际写入和独立 POST。
