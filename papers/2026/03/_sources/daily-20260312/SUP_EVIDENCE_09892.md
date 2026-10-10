# 2603.09892：顺序适配中的重放时间、数量与样本身份

root作者必要Source、supplement_20260312非作者Source/date/PRE及实际POST通过。[MSSR exact-v1](https://arxiv.org/html/2603.09892v1)，实际读取§2–4/Algorithm1、Appendix A（loss归一化、lazy hazard、consolidation clipping）、B.1与E完整训练/重放设置及Tables1–8相关正反侧。不采用未核B最优控制证明、图像精数、实现/复现。

原SUP_EXACT_BATCH3身份：v1 Submitted Mar10UTC16:49:44不作公开；arxiv.content owning/findable registered Mar11UTC02:24:24上界与已实读官方最终ID/DOI不能预先取得、最早公告下界同BJT03-11，使用已校准日夹证。current仍v1、题摘同原、comments空、无已见撤回/纠错或先公开信号；不因null证明全网无先稿。评分2+1+2=5，具体重放控制与代理边界缺口深入，唯一TRAIN-SFT。

## 必要机制、可采用与未采用

§3样本m/S/上次review cursor、当前loss的EMA/quantile人口、hazard及review后reset与consolidation形成重放状态。m是设计的指数衰减代理，不是held-out能力或真实保留概率；A.5另外明确S clip至[Smin,Smax]、default noise0。quantile分母退化与m^-ζ下溢数值退路未完整披露，不补代码。piecewise hazard/lazy只减少状态更新，不消除获取loss及维护排序的费用。

Dataset-level间隔Δ=1+η exp(-ρk)在给定参数下有上界，不是无限间隔；ratioλ0exp(-βt)+λmin与样本inverse-m优先级是不同控制。§3.3另给(1-m)^β exp(ρΔt)口径，Alg1引用Eq10 inverse-m，E.2/Table12亦inverse-m；不修成唯一可执行实现。正hazard下指数范围与定点threshold的代数只描述surrogate，不证明有限LoRA更新不会遗忘。

## 评价、直接反侧与总费用

LoRA/LLaMAFactory，3-task AlpacaGPT4→GSM8KRFT→CompetitionMath及11-task不同任务；T1列Mistral7B/Llama3.1-8B/Qwen2.5-7B，T2列Gemma2-9B/Qwen/Llama，E称后三个，不合并为一个相同模型人口。E rank8/alpha16/q,v、AdamW2e-4、cos/warmup.05、max2048/effectivebatch256/2000steps每阶段/100steps eval/bf16(fp16fallback)/seed42；正文A10080G DDP但卡数/推理length/concurrency/SLO及独立seedCI未披露。步数相同不是累计replay tokens与墙钟相同；微batch依backbone、训练收敛描述与固定steps并存。

T1多数局部提高但Qwen MMLU full59.2<Accu59.5；T2 Gemma MATH1 full.867<Fixed.873/MATH4 .412<None.425，Qwen MATH1 full.864<None.873，Llama AGNews full.787<Loss.794；这些人口不全占优。Table4正文称最低forget却列Fixed0.0/Geometric2.6/MSSR4.5，不能采用其对应宣传；Table8 ForgetDrop名及数与prose关系不修成确定减幅，未核D定义就不授该指标结论。T7作者归一化wallclock1.05/peakmemory1.06/throughput.98只支持受限7B对照，不授跨卡/端到端成本优势。所有historical buffers、loss/状态刷新、采样、实际replay训练及旧任务回归付费；作者称无additional forward/backward不作为所有fresh-history-loss免费的保证。

## actual owner差额及逐字PRE

root实际Ch29 755–820包含capability-budget与mixture stopping、886–909包含trainable-subspace，Ch28/30开篇已在本日实读。现有random mixture/rollback、旧任务参数保护与replay fallback未解释顺序数据中“何时/多少/哪条”三项控制及memory proxy身份。拟只在mixture stopping完整段后/tool-use监督前插两段，不破坏原peak回滚主线。

拟段1：

若新任务只能顺序到达，无法一次混合所有历史数据，重放旧样本就是另一条保留能力的分支。固定比例的均匀 replay 状态简单，旧任务较少、分布稳定时仍合理；预算紧或样本变化较大后，可以把“何时重放”“每次用多少旧样本”和“选哪些样本”分开控制。一个受限方案为每条旧样本保存上次训练时间、loss 平滑统计与衰减/稳定性代理，再由间隔与比例安排批次、由代理决定采样偏好。这里的 memory strength 是人为维护的训练调度状态，不是模型内部记忆，也不认证旧任务真实能力；buffer 人口、loss 归一化、更新时间与采样规则共同定义这份状态。

拟段2：

这种自适应安排减少盲目均匀重放，却增加历史 buffer、代理校准、状态维护和实际 replay 训练的费用。[受限顺序微调对照](https://arxiv.org/html/2603.09892v1)在部分模型/任务提高保持指标，其他切片仍退步，间隔、采样与遗忘指标的内文口径也未完全一致，不能照录为通用最优或无遗忘配方。Lazy update 只减少代理更新，不抵掉新 loss 取得、重放 tokens 和旧任务回归；相同 optimizer steps 也不等相同累计工作。高 loss 可能来自噪声，衰减代理会陈旧或数值退化，须以独立的新旧任务质量及总预算验收；代理失配、历史样本受访问限制或成本不合算时，保留固定均匀 replay、较小更新或独立 adapter，而不是让代理分数自签保留能力。<!-- source-family:SF-2026-ARXIV-2603-09892 -->

两段逐字PRE已写Ch29新780/782及本人1245；root作者实际顺读766–800完整mixture→replay→tool-use邻接，supplement_20260312非writer实际顺读766–820完整局部及末注并回对有效必要原证，POST通过。旧mixture/tool-use/scaffold段完整，Ch29本项窄锁释放；仅本项，不授DAY。
