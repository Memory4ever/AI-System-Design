# 19118：采样预算内的错误排序与概率校准分开

root sole准备，只本03-21补03-20自然日；现存完整题摘准入与本批日级公开归属已核结果复用，不扩query/附件。拟2+2+2=6，新增是长推理负载中同预算信号互补的受限证据，不给成熟线性组合原则重新计分。

## 必要原证

[exact-v1](https://arxiv.org/html/2603.19118v1)与[官方abs](https://arxiv.org/abs/2603.19118)：七作者、仅v1，页面无明确撤回/纠错；Submitted03-19T16:42:05Z不是公开日期，沿本批已核日级夹证落03-20，不补公告时刻。实际读§2.1–2.4/Eqs1–3、Table2与§3.1–3.5直接限制：每题K条完整trace，答案多数票同票随机破局；SC为多数答案频率，VC仅平均支持被选中答案的样本自报分，SCVC等权线性组合。改变K也改变最终被评价答案及其支持样本，不是固定答案的同一个置信度被精确估计。

17任务、三个reasoning底座（gpt-oss-20b high、Qwen3-30B-A3B、DeepSeek-R1-0528-Qwen3-8B），vLLM，每样本最多60K且judge另可60K，温度/top-p分别1/1与.6/.95。硬件、precision、batch/concurrency、生产SLO及全成本未披露。作者比较AUROC错误排序，不验ECE/Brier或回答/拒答效用，不支持数值是成功概率。主结果每题R=10固定生成池，无放回抽K反复算AUROC；无合法格式样本被丢弃、无有效样本题<1%移除。该区间覆盖池内decoding波动，非独立任务/部署人口的泛化区间，格式失败不能在平台失踪。

同预算混合在作者macro人口上的排序增益比单信号继续加样本更强；域/提示与judge方法敏感，数学更强但未分离训练原因。§3.4相关性非因果独立；§3.5六种取分方法只在部分任务比较且不同域排名不同，额外judge不免费。两样本足够或不用单样本/SC的headline不采为通用policy；实际成本、目标任务校准或外部证据可能使原单样本/少调用路径更好。未核可选代码或复现实验。

## Actual owner与一段差额

`PLATFORM-EVALUATION-SYSTEM`/[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。actual完整690–766，Ch65/67未变开篇复用；现有样本聚类、forecast/action分账、局部校准与一致性邻域不拥有长trace负载中“SC＋多数答案成员VC”同预算比较的人口。拟放Calibration标题之前，承接风险sensor/升级decision分责，后接隐藏regime，不重复概率与所有路径原则。

## One literal PRE（待非准备者）

判断置信信号是否值得多花采样预算，也应先固定它评价哪个答案：采 K 条完整推理、选多数答案后，答案一致性是支持该答案的频率，自报置信的聚合则可只平均支持该答案的成员；改变 K 会同时改变答案及成员人口。将两种信号组合是一条错误排序的替代分支，不是直接计算答案为真的概率。[长推理的受限比较](https://arxiv.org/html/2603.19118v1)显示少量样本的信号互补可能比单一路径继续加样本更划算，但结果依赖任务、提示和取分方式，不授“两次就够”或普遍拒答阈值。评价须固定答案规范化、同票处理、合法格式与失败分母、相同生成/额外judge预算，并把AUROC排序、概率校准和实际接受/升级效用分别验收；重复从固定生成池抽样的区间不等于新任务人口可靠性。长trace、置信调用和独立标签都付费，信号失配、格式失败或外部验证更有效时，保留单样本/原传感器、外部evidence与保守拒答，而不让混合分自签事实或发布权。<!-- source-family:SF-2026-ARXIV-2603-19118 -->

拟静态本人章末注：

- `SF-2026-ARXIV-2603-19118` — [Uncertainty sampling exact-v1](https://arxiv.org/html/2603.19118v1)，必要§2–3/Eqs1–3/Table2及§3.5；仅长trace同预算下的多数成员自报分/一致性互补诊断。保选答/格式人口、固定池波动、提示/域与全费用，不授概率校准、两次通用recipe或生产效用；未核代码/复现。

交resume_mar18非准备者必要Source/date/actualowner/onePRE裁；未锁未写、不计safe/DAY。

## root 实际窄写

非准备者原文/owner/PRE有限通过后，仅写Ch66原one PRE为748、本人静态注5959。writer实际完整738–764与本人注/末六行回读，升级决策→采样sensor预算→隐藏calibration regime交接保持；无动态验收身份。限定diff-check0；并发2025源注未覆盖。交resume_mar18一次非writer实际完整局部和本人注POST，未POST不计safe。

## 非准备者必要 Source/PRE 裁定

resume_mar18 独立恢复重读当前AGENTS、研究/Report合同、每日/arXiv来源、统一Prompt/ROADMAP与本日STOP后，实际核exact-v1 §2.1–2.4/Eqs1–3、Table2、§3.1–3.5（包括六种取分的任务子集与额外judge通道）及官方abs七作者/仅v1/header/history；本批03-20日级夹证身份不变复用，不补造时刻或“无其他先稿”。实际Ch66完整690–766与Ch65/67交接回对原one literal及静态注：多数选答成员VC与同K一致性的新受限预算接口成立，当前forecast/action分账和Calibration不能代替该成员人口比较，拟Calibration前位置合适。Source/actualowner/PRE有限PASS，2+2+2=6保持。

没有把K变化视为固定答案的精度改良，也未把AUROC当概率、低相关当因果独立或“两次就够”当通用policy。Table2区间标签与§2.4置信区间表述不统一，因此不采用具体区间recipe；固定池无放回、无效格式移除、§3.5部分任务人口、trace/judge全费及单任务反侧均由原PRE边界保留。正文与静态注无需修改；未核代码/复现，不授实际POST或DAY。交root协调sole Ch66窄写，再由非writer一次实际完整邻接及本人注POST。

## 非writer实际 POST

resume_mar18实际完整顺读Ch66 738–764（新增748）与末八行中本人静态5959及两侧邻注，逐字回对已核onePRE/static与必要原证；literal/static实际匹配、正文marker唯一，限定diff-check0。Forecast sensor/action/resolver分责后，新增同K多数选答成员的预算比较，随后交Calibration隐藏regime；未把混合排序当概率或发布权限，固定池/格式人口、任务与提示、judge全费和旧分支回退保留。非writer actualPOST正式有限PASS，可交root接纳释放本family Ch66锁并归并一I；不修改静态注验收身份，不授DAY，并发2025末注未动。
