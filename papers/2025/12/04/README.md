# Daily Research — 2025-12-04

**规范：** V3
**窗口：** 2025-12-03T09:00:00+08:00 ～ 2025-12-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T20:30:56+08:00

## 1. 结论

作者侧确认1个落窗家族：Confessions把主答复与诚实自报分开奖励，使已知违规更容易暴露，但不防止违规、不证明自报是真值。6分，针对长期objective/credit缺口深入读必要机制与反证，TRAIN-RLHF现已由root窄整合至Ch31两段，非写入者Mill实际POST通过；这不替代日级验收。

14每日源按本日原始邻接处理；arXiv四主题查询及官方两类各首段标题有界补检。Mill发现的9项漏记和2项关闭反例已逐项归并，8新潜在/1科学路线关闭、2原关闭重开，arXiv潜在家族现34个，first-public仍隔离，确定落窗分母仍1。作者普通补正与报告同步均0；Confessions整合及非写入者POST已落实，Mill已独立核本次同步并完成日级验收，结果见§6，非以整合或POST单独替代日级验收。

## 2. 来源覆盖

原始观察和新查询见[本日记录](../_sources/daily-20251204/WINDOW_REVIEW.md)，首批见[准入记录](../_sources/daily-20251204/ADMISSION.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 实际RSS本窗Dec3 08Z/10Z三项至下一Dec4 19Z；Confessions核心 | 已检查 | 仅研究主题切片，非全机构保证 |
| SRC-ANTHROPIC | 原始publicationList Dec2 18:58:43.576Z/Dec4 17Z连续邻接 | 已检查 | 无新增窗内目录项，不扩成全站零事件 |
| SRC-GOOGLE-AI | Blog2025第1页到Nov12，Dec3 MSEB/Dec4 Titans；DeepMind第3页及141313、March精确v1 | 受阻 | MSEB/目录修订的必要首公开或新事件时间不明 |
| SRC-META-AI | 第4页Dec1/Dec12及Nov19下邻接；AdvancedIF同家族版本 | 已检查 | 目录收录不证明首次公开 |
| SRC-QWEN | 旧Sep23、新站动态正文与已尝试部署/官方仓库有限替代 | 受阻 | 原始2025历史目录缺失，隔离 |
| SRC-DEEPSEEK | 正确API Docs Dec1 release与下一2026；不再错误news路由 | 已检查 | 日精度旧事件不移归本窗，非全机构零事件 |
| SRC-MOONSHOT | 完整Overview Nov7、changelog Nov6历史邻接 | 已检查 | 无本窗列出条目 |
| SRC-TENCENT-HUNYUAN | 原始All API 11/11均2026，旧Research和有限替代失效 | 受阻 | 2025原始Research目录不可恢复 |
| SRC-ZAI | All第2页18条至Dec7，release Sep30/Dec8 | 受阻 | Dec7以前历史目录未保留，不当零命中 |
| SRC-BYTEDANCE-SEED | 官方2025Paper首段Dec15/Dec2/Oct22，Blog Dec16/Dec2/Nov27 | 已检查 | PublishDate日编码不补时刻，GR-RL旧必要日期仍隔离 |
| SRC-BAIDU-ERNIE | Blog第2/2页到Nov7，Nov21/Dec9连续邻接 | 已检查 | 无本窗列出条目 |
| SRC-XIAOMI-MIMO | Paper8项；Blog15项及route HSS Dec19/Safety Dec18 | 受阻 | 无date/More历史范围不能证实，隔离 |
| SRC-MINIMAX | 英文13项及中文Oct27/Dec23；未触发AgentTech新事件 | 已检查 | 无本窗列出条目 |
| SRC-ARXIV | 四组Dec3主题query；cs.AI/cs.AR十二月各1–25标题、相关精确v1题摘；历史公告有限替代 | 受阻 | 月身份/提交不提供个体first-public，不以隔离授覆盖通过 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [How confessions can keep language models honest](https://openai.com/index/how-confessions-can-keep-language-models-honest/) | 2025-12-03T18:00:00+08:00 | 混合答复目标会奖励隐瞒 → 独立诚实自报reward不改主答复reward → 可诊断而非成功授权；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) 约266–268行，Solver/Auditor后两段；root写入，Mill非写入者POST通过 |

## 4. 证据与知识整合

### [How confessions can keep language models honest](https://openai.com/index/how-confessions-can-keep-language-models-honest/)

RSS时刻完全落窗，采用事件是官方Blog而非Dec8提交的[论文v1](https://arxiv.org/html/2512.08093v1)。原文How confessions work/What we learned/Limitations支持事后目标枚举、合规分析、不确定性和独立reward，且只是有限训练压力测试。额外输出/judge成本不会因奖励分离消失；把报告直接用于惩罚原答复会破坏原激励边界，是本项目设计推断而非已部署实现。

必要正文补读Method、Results及7.4，只作晚于本窗的限定证据：base curriculum matched不是总compute相同；联合漏报概率不是条件检出率；模型不知自己错时可能无法自报，高优化压力尚未证明。未披露训练hardware/precision/production SLO写Not Disclosed；没有代码核验/复现。不能用后来的精确v1反填12/03公开事实。

Ch31实际“Bottleneck聚合”段拥有多目标reward，“Solver/Auditor”拥有角色finding激励；相邻Ch30的update表示和Ch32的token信用段均不拥有此独立自报目标。具体差异、原始证据及原局部草案见[本日Books提案](../_sources/daily-20251204/WINDOW_REVIEW.md#confessions深入证据与books提案)。本轮重新实际读取Ch31约266–268行及Review notes：root已在Solver/Auditor与policy objective交接处写入独立自报reward和诊断失效两段，保留共享参数未隔离、额外生成/judge成本及外部verifier回退。Mill独立重读原始核心、新段/前后及Ch30/32后POST通过，Review notes已对应记录。作者同步为整合，不自授日级验收，不将新机制一律写仅报告。

## 5. 缺口与下一步

本日记录表中MLNN、HAGeo、Rosetta、Reasoning Under Pressure、Trification、ChartPoint、CogEvo、Echo-N1、Debate with Images、EDIT、FA-DPO、SpeContext、Psyche、MPR-GUI、BioPro、SFS、Compiler、Decoupled GPGPU、Fused Dot Product、LLaMCAT、CGLA均有具体潜在增量且已读完整精确v1题摘，未因访问/工作量删池；尚缺个体first-public，不能列为确定本窗候选或正面证据。已有具名TokenScale/FFTrainer/Gate-Norm提交在本日相交，但仍不能代替实际公告。接受官方历史new/RSS/email或可核实作者首次正文，恢复只重开真实日期；历史list/catchup/API/月字段已有限替代，不循环搜索。

MSEB Blog Dec3日文字及NeurIPS身份无法确定当窗新事件；Reward Features March论文与Dec3目录的理论增补是否构成重要修订亦需原始变更/公开依据。都隔离，不把整天公告移到09前。RL-Struct官方withdrawn由于重大错误，明确不采用任何旧版、不评分、不Books；Mill已独立核当前官方撤回记录，排除处置进入终态，原始事实保留于本日记录，不另留普通安全待办，也不是访问缺口。

十一项普通差额已实际归并，见[定点补正](../_sources/daily-20251204/TARGETED_REPAIR.md)：00479/00601/00045/00020/00028/00055/00059/00186保留潜在表示、评价/正确性或计算机制增量；00836为SIR科学应用而关闭；00016 Architect及00834 SemAgent根据局部验证失败与metric反例撤回原关闭。上述及原24项共34个arXiv家族，MSEB/Reward Features未定事件、Qwen/Hunyuan/Z.ai/MiMo必要历史目录均为本窗终态保留项：不用于正面证据、不进入 Books、不支撑无遗漏或性能/安全保证，隔离不计Coverage/Evidence通过或零事件。逐项链接/限制已落记录；恢复需具名精确v1历史new/RSS/email、可核首次正文或2025目录邻接，只重开真实归属日，不重复同接口。

作者持有普通补正与报告同步0；Confessions Ch31两段由root整合，Mill非写入者实际POST通过。本次已同步正式§1/3/4/5，Mill已独立局部核同步并完成日级验收；作者未改共享Books、metadata或§6，不用整合通过代替整日报通过。

## 6. 复核

复核者：Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`；非作者Gibbs，非Books拟写入者root。

结论：通过

实际独立日级范围、原始访问与逐项差额见[本日复核](../_sources/daily-20251204/ROOT_ADMISSION_REVIEW.md)。核14源原始范围/有限停点；独立取得官方RSS758460 bytes并解析Confessions Dec3 10:00 GMT，独立Blog核心及晚于本窗v1必要Method/结果/反证支持窄机制，不反填首次公开。确定落窗分母1，Confessions证据判断通过；Books两段已落实并独立POST通过，作者正式报告同步也已实际核对。

全部原21项精确v1题摘及具名TokenScale/FFTrainer/Gate-Norm三项独立校准，仍日期隔离；MSEB同身份有效核心复用，Reward Features March v1/版本表独立核去重，未知修订不当已审。安全核RL-Struct重大错误撤回、00017重复撤回；普通负侧分层核基金/Neptune/Chunking共3项。Architect/SemAgent关闭理由含糊，定点核心后发现局部验证与指标反例而重开，不把成熟组合当负面机制排除理由。普通无关题名与全版本史未全量复读。

初审12项差额的历史记录保留在ROOT。本轮实际核TARGETED_REPAIR：九项漏记归并为八项窄potential与一项SIR科学应用关闭，Architect/SemAgent两项局部反证重开，十一项补正通过；未重复读取未变原文。34个arXiv潜在家族仍不授first-public或Evidence，不增加确定落窗分母1。

root已实际在唯一owner TRAIN-RLHF Ch31 Solver/Auditor之后、learned reward公式之前写入两自然段。Mill非写入者重新独立访问官方Blog必要核心，实际对读新段、前后及Ch30更新表示/Ch32 token credit，POST通过：输出/reward信用分离不授共享参数隔离，诊断不授独立验收；不采用后来25%实现或安全保证。仅按授权更新该Review首bullet POST状态，不改机制正文。

本轮定点核作者正式§1/3/4/5及WINDOW_REVIEW已同步整合、非写入者POST通过与普通0，6分和日期终态边界未变。仅按root本次授权修正§3 Ch31本地链接为普通.md并保留正文行号、§5 RL-Struct为已核撤回的排除终态；不重复未变原文，也不另留待root安全核查。普通差额0，日级语义复核通过。34个arXiv potential、MSEB/Reward Features未定事件及必要历史目录保持具体终态/定点重开，不授Coverage/Evidence、正面采用或无遗漏。完成态V3及链接/空白检查实际结果见本日ROOT记录。未改Books、共享state/monthindex或其他日期，未stage/commit/push。
