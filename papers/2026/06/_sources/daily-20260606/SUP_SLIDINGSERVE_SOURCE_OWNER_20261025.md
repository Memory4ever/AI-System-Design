# SlidingServe 05933首次必要／评分／actual owner与两段PRE

作者jun06_continue，2026-10-25，仅Daily2026-06-06补Jun05。已恢复当日AGENTS/当前研究合同/每日来源、Report合同/Prompt/ROADMAP与本日A29/R24。R19完整AB、Jun05组合日证与准入直接复用，不第三恢复日期，不借别日材料池；旧Ch56 trace标DailyJun05只作精确family去重线索，不覆盖本日归属或正文证据。

首次拟2+2+2=6：从当前最大可行chunk转两轮预算/批内风险subset为设计2，预测器与scheduler/执行时限交接reach2，可复用可行性与跨轮效率/整体batch截止分责durability2；不为幅度、机构或已有通用SLO原则加分。实际最小gap需深入受影响必要，非强制全部附件。

## 必要证据与直接反侧

实际读[exact-v1](https://arxiv.org/html/2606.05933v1)§2.2–5.5、式2–22/Algorithm1–2/表1–5及直接caption、§7；未读图像素、源码或复现。§3.2分别为pure-decode/prefill/mixed拟合7feature线性latency model，offline初始化与可选异步online calibration/hot-swap；feature含token/context与attention交互。平均预测高R²不是尾部误差上界，也不免漂移后重校准。原式5索引j=0..7与7维x1..7不完全齐，不照录唯一执行recipe。

§3.3先保decode每轮一token基础预算，prefill/waiting按(g safeguard、归一化剩余work/slack是否紧急、剩余tokens)lex排序；优先短剩余并非无饥饿保证，过期请求降级会改变总体tail。§3.4先用当前decode最紧slack与下一轮TBT估TimeToBudget，当前/下一轮token和Bsum固定作近似，两轮预测总时搜索每轮滚动一次。Algorithm1三分收缩后仅看原端点和中点，未给目标unimodal或TimeToBudget单调证明；未来batch composition仍由当前队列模拟，不能升格任意arrival/完成下全局最优或硬SLO可行证明。

§3.5对fullbatch预测会违反TTFT者逐一作anchor：以该anchor slack换token capacity，扣decode，强制包含anchor并只选slack不早于它的其他prefill，用剩余tokens为weight、归一化slack/work的函数为value做0/1 knapsack；anchor自身做不完则不可行。选中prefill分完整剩余tokens，故不是每个候选都只需拿到少量chunk即可达TTFT。跨anchor Comparer先最多完成数、再总value、最后budget；innerknapsack最大value与outer最多数不是同一全局目标，不宣称全局最优或公平。前提依赖TimeToBudget/预测且未在伪码证明所有实际GPU时限，保守余量/最终校验属项目采用边界，不冒充作者已实现鲁棒保证。

§4为vLLM扩展request TTFT/TBT元数据和batch模拟器；声称兼容SGLang/TensorRT-LLM不等这些后端已验证。§5模型Llama3-8B/Qwen2.5-7B、RTX3090 TP2；表5 A6000 TP2/A100只predictor配置不搬成全部end-to-end。ShareGPT与arxiv两组mean/P90长度在表2，mixed-v1/2按3:1/5:1混合。SLO为dialogue TTFTslowdown5×/TBT40ms，summarization10×/80ms；goodput允许1%violation，不是严格零违约。precision、全部并发/到达seed与重复CI、统一scheduler overhead及profiling完整费用未披露，不补。

关键反侧：§5.2承认部分tail更高，已超时请求降级保护尚可达标者，不能只看成功人口；文字p50/p95/p99与后文p50/p90/p95口径不同，不采唯一tail数。§5.3 transient每2分钟在QPS1与2.5间变、20分钟；原“1.5×peak/trough”与比值2.5不符。图6文本表57.78/51.30/27.56对应所述30.22/23.74是百分点差，不照录相对下降百分比。§5.4 sequential SC→SC+MLPS→完整BC只Qwen/mixed-v1，组件不能独立归因；表4高负载完整仍50.5%violation。§5.5 MAE2.52–2.72ms/RMSE4.12–4.33只平均，不认证40ms TBT下所有误差、预测器runtime开销或online适应已闭。正文不采headline幅度/硬保证，支持/反侧足而停止图像/附件扩读。

采用只保两轮机会成本与batch共同完成时刻、有限anchor subset选择的责任链。Profile/预测、队列模拟、多次搜索/DP、在线更新、KV状态与全请求等待/尾延迟全部付费；predicted feasible不等实际ready/KV可分配，不绕runtime最终资源资格。Fairness/过载与保守fallback仍独立。

## actual owner与最小gap

actual读Ch56 SLOadmission完整预算/预测margin/共享实例两门段，IterationScheduling开头两段、QBA长请求晋升完整段、SuperInfer完整两段和OmniServe完整两段，后接FlowPrefill完整两段；Ch46 chunk例及policy边界，Ch55/57开篇交接已核。Ch56有本family旧dailytrace（仅一句泛称sliding-window changes batch/fairness），没有两轮预算或anchor-knapsack的真实机制正文；trace不授I/NC。现有admission的下一轮模拟、影子价格未来机会成本与QBA公平性有效复用，但不承载固定总预算在当前/下一轮分配，也未解释“已入batch仍会因整体完成太晚而超TTFT”后的anchor/完整剩余work选择。唯一`INFER-SCHEDULING` Ch56有最小gap，Ch46继续拥有batch/iteration基本机制，不重复推导策略。

## 原两段PRE（尚未SAVE）

拟位Ch56 Iteration Scheduling开头“输出长度未知…公平性信号，但会牺牲部分吞吐。”完整段后、QBA“预测短请求优先能改善均值…”完整段前；只原两段/唯一marker/本人注，需独立首次必要/6/actualgap/PRE和root本轮fresh窄授。

每轮还须区分“当前能放多少”与“跨轮怎样分配更合算”：较大的Prefill chunk虽能用满本轮Decode slack，也可能挤掉下一轮预算，使两轮都落在低效batch区间。一条[受限两轮展望分支](https://arxiv.org/html/2606.05933v1#S3)先从当前队列与各类batch的延迟预测估算当前/下一轮预算，再搜索两轮预测总成本，执行一轮后重算；它不预知未来到达，有限搜索也不是全局最优或硬截止证明。Profile/预测器版本、队列/context、预算与真实batch完成时间须共同留存，不能把当前最大可行chunk当跨轮效率最优。

请求进入batch也不表示其TTFT已获保护：它仍需等整批结束。若预测整批会让部分请求超时，可逐个以风险请求作anchor，用其slack约束总容量、扣除Decode工作后强制完成anchor的剩余Prefill，再从不更早到期者选择有价值的可完成子集；这与简单按顺序填满token预算不同。预测/队列模拟、预算搜索与组合选择均有费用，均值误差不提供尾部上界，保护尚可达标者还可能恶化已超时者尾延迟。因此必须连同全部请求、KV资格、过载与公平性另验；不从较高达标数签硬SLO。预测漂移、搜索收益不抵控制成本或尾部不合时，保固定/单步chunk、保守EDF/admission与独立公平队列，不让优化器替runtime确认资源。<!-- source-family:SF-2026-ARXIV-2606-05933 -->

本人注拟：`SF-2026-ARXIV-2606-05933` — jun06_continue，Daily2026-06-06补Jun05；R19AB/date/准入复用，2+2+2=6/唯一INFER-SCHEDULING Ch56。exact-v1 §2.2–5.5/Alg1–2/式2–22/表1–5必要，只两轮预算与批整体完成/anchor subset分责。保搜索无全局保证、inner/outer目标不同、tail/过期降级、百分点/峰谷比/分位口径差额与全费；未核图像素/代码/复现，硬件predictor与端到端范围不混，不授硬SLO/公平或完整后端兼容。PRE/rootfresh/真SAVE/唯一POST按后到事实记，不预I/DAY。

## 既成采用（2026-10-25，仅行政同步）

R25首次必要/正式6/actualCh56原两PRE通过，root本轮fresh窄授后A31逐字真实SAVE及完整新增/直接双侧/本人注自读；[R26唯一actualPOST](SUP_REVIEW_20261025.md#r26--slidingserve-05933唯一actual-post)实际通过，I10生效/窄位释放。以上未SAVE/拟态只保历史过程，不再表示普通未完，不第三必要/正文，不授DAY。
