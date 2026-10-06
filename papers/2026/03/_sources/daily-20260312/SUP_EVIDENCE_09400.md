# 2603.09400 — 目标/状态因子化的搜索评分（ready）

[Reward Prediction with Factorized World States exact-v1](https://arxiv.org/html/2603.09400v1)。作者实际完整§2–4/Table1–2、AppendixB、C.4/C.6（含prompt/单步与初步案例）。未核Fig5像素、全部data generation/训练代码或复现，不遍历引用。原batch3完整AB准入保留；current仍v1/comment空、未见撤回/纠错/先公开信号。原owning arxiv.content findable registeredMar11UTC02:12:43已可发现上界与official noadvance最终ID/DOI/最早Mar11BJT08下界同日夹证；SubmittedMar10UTC09:12:20不单独作公开。

范围：采用LM驱动的跨文本环境状态/目标表示及搜索评分机制，直接非科学领域AlfWorld/BlocksWorld/TextWorld/WebShop亦有证据；不将ScienceWorld实验机制或领域科学结论重新引入AIforScience，不用其收益为主线背书。2+1+2=5，具体状态—目标因子化score gap必要深入；唯一AGENT-PLANNING，不把state语言就当可控worldmodel。

## 必要机制与数学边界

§3先根据真实observation、历史state及action抽取object identity及attribute/value；goal从任务及当前上下文提解释/实例化。逐goal object对每个state object计算identity相似度×所需属性值相似度平均，先以key最大相似找对应属性，再取object最大分，最后平均所有goal object。不是先唯一确定实体再判全部约束；identity与attribute score联合竞争。AppendixB Eq10–12确认各goal独立hardmax，无跨goal injective assignment/唯一属性对齐，也未认证所有约束真值。单state object可以同时成为两个不同goal object的max；缺少匹配或goal/key空集合退路未闭合，平均可让部分失败被别处相似补偿，不使用“joint probability/soft logic正确性”标签。

C.4 actual ModuleA要求observation/历史证据、禁止copy目标，未再见对象默认沿用旧state；B按task relevance过滤；C要求Task是intent来源。它们是prompt约束，不是可信校验器：未重新观察仍可能陈旧、relevance filter可漏阻塞条件。C既要求step0完整immutable又允许later milestone addition，不能修成绝对静态goal实现。goal anchoring/解释变化须单独保存，不能由两路LM内容更相似批准外部状态已发生。

§2 Eq3是trajectory reward序列Pearson相关的EPIC简式。正仿射变换保相关，不能认证绝对值校准或终态阈值；例如pred=.1+.8*truth，非恒定truth下rho1/distance0，truth1时pred.9。原expert中r=t/T加边界随机native奖励，negative常0，constant-sequence Pearson退路/最终聚合计数未披露。不是将全部environment-native reward称逐步gold成功，也不由此metric认证所有MDP policy-invariance；本轮无需读原EPIC全文来证这份具体实现的限制。

## 关键评价、直接反侧及费用

S4/C4：gpt-oss20b medium、all-MiniLM-L6-v2、vLLM/T.01/context8192。Table1总体distance.297低于samebackbone judge medium.322，但TextWorld .201高于judge.115，BlocksWorld.427高于judge.363，非每域优势；不同backbone/trainingpopulation不授60%为结构唯一因果。Fig5正文仅有限granularity/oraclegoals说明，不采精确曲线或triplet correlation→因果的断言。encoder按该ablation选择，未独证所有模型/embedding适用。

§4.4/Table2 AlfWorld34.33→55.97、BlocksWorld85→93为作者有限在线结果；C6增强还给admissible actions、topK3 proposals、预测/评分、差分gain和重复惩罚再注入ReAct，不能只归representation或称与单路reactive同总预算。System2 d1/MCTS与WM只是初步案例，不采普遍长horizon/可靠规划或policy-invariance。seedCI/硬件precision/并发SLO/整体latency未披露；状态抽取/过滤/goal解释多LM调用、所有embedding pair/驻留、proposal及预测WM、judge、真实执行与回归付费，zero-shot不等无预制/低费用。

## actual owner 与逐字 PRE

作者actual完整Ch79 42–102、261–291及Ch78/80开篇；Ch25开篇仅核handoff：本项reward similarity不是transition真实性。原Ch79已有belief/observed分离、transition proposal权与root/verifiedsuccess potential，但没有将goal/state分别factor到object/attribute并独立softmatch成score的具体分支。拟只在LaPha两完整段后、Physics-informed几何regularizer前插两段，保留全部原critic/verifiedsuccess/真实outcome。

拟段1：

目标已能用语言表达，也不必让同一个 judge 直接给整段 history 打进度分。另一条搜索评分分支把已观察事实与目标要求分别整理成 object、attribute 和 value：状态随真实 observation 更新，目标解释保留任务来源；再为每个目标实体比较候选实体的 identity 与属性值相似，聚合成可供候选排序的连续 proxy。它把信息抽取、实体/属性对齐与最终打分拆成接口，便于检查哪条要求没有匹配，但 LM 抽取和 relevance filter 仍可能漏事实，历史属性也会陈旧；目标与当前状态更像，不表示目标已经实现。

拟段2：

[受限因子化状态对照](https://arxiv.org/html/2603.09400v1)支持这一替代评分接口，不提供完整约束或环境真值证书。各目标独立选最大相似，可能重复占用同一实体或把不同属性错配；均值也不是全部条件同时满足，须另验对象数量、关系、否定、时序和真实 terminal outcome。轨迹相关型评价不认证绝对 reward 校准，部分非科学文本任务的误差仍高于直接 judge，在线增强又增加候选提案与预测/评分调用，不能单独归结构或继承同预算收益。状态/目标抽取、所有 embedding 比较、候选与 world-model forward、真实工具和回归均计费；匹配失准、事实不可核或预算不足时，保留直接 judge、原 critic、可信 symbolic check 与真实 outcome backup，不让语义 proxy 提交环境事实。<!-- source-family:SF-2026-ARXIV-2603-09400 -->

root必要Source/date/PRE与Ch79实际两段非writer POST通过：作者写282/284及自身474，root实际273–302完整LaPha→新分支→Physics与本人末注回对必要原证，旧段保留，窄锁释放。计新增第31，不授DAY。采用方法受限分支，不因局部标量评价缺口抹掉已支持机制，也不授全benchmark/匹配实现。
