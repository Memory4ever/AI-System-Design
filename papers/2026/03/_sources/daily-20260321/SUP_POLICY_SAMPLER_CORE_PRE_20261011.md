# PolicySampler18428：必要原证与采样控制 PRE

root准备，仅03-21补03-20自然日。已有准入/日级夹证复用，不迁旧候选。2+1+2=5：拟保留的是冻结基座之外以逐prefix状态提议temperature/top-p的学习控制器，不给PPO本身或摘要写作领域新分。具体采样接口缺口定点深入，未写/未授DAY。

## 必要 exact-v1 与证据边界

[原HTML](https://arxiv.org/html/2603.18428v1)实际§3.1–3.3/Eqs1–2、4.1–4.2/Tables1–2及5。完整方法/评价/反侧已够本命题，不遍references/代码或旧版。

- §3每prefix将mean-pooled finalhidden、top50logits、prefixlength与normalizedentropy线性投影/归一，2层256-GELU MLP输出Gaussian两action，再sigmoid/affine到T .2–1.2/p .8–1；改sampling processor而非改LLM参数或额外知识。状态接口须可访问白盒，概率比为controller动作policy，不是LLM的on-policy token比；不复制PPO算法owner。
- §4.1各dataset100训练prompts，每prompt完成summary、计算reward并periodic PPO update；within-episode状态自适应与across-training controller学习是不同事实。没有证明每条线上轨迹中更新controller参数或无需reference的即时自改进，不把test-time headline当实际weight更新时间保证。
- Granite3.3 2BBase与Qwen2.5 .5B、BookSum/arXiv/WikiHow；Greedy与唯一fixedT .3基线，static top-p配置未给。不是最优调参基线。reward ROUGE-L .5、长度.2、coverage.1/repetition/句尾punctuation及linear normalization，RAW_MIN/MAX和全部reward系数未完全给；这些proxy不能证明faithfulness/事实正确性。
- Table1组合reward所有最终RL高于所列Greedy/static，但Early→Late Granite/arXiv−4.38%、Qwen/WikiHow−43.60%；Table2 ROUGE-only PPO .169低于static .170、core−4.56%、sigmoid−4.27%。否定总是稳定/无退步，与主文总结张力保留。不同reward标度不能跨variant直接比绝对质量；单reward上涨不排除静态策略坍缩，没控制状态无关但充分调好的policy。
- 每token MLP/hidden读取/feature、100prompt候选生成/reference评价与PPO均付费；正文‘negligible’没有walltime/硬件/precision、输入输出长度、batch/concurrency、repeatseed/CI或SLO，全部Not Disclosed。没给部署日志、自由对话/代码/推理/OOD迁移或安全对照，不授无成本/低风险普遍收益。关闭controller可回原sampling，不等撤回已产生文本/工具effect。

## 实际 owner 与差额

`MODEL-SAMPLING` Ch20实际1–195完整sampling顺序与artifact、233–249局部校准/BoK、260–289轨迹budget反馈；Ch19/21开篇读。现有hidden control/预算机制不能覆盖**controller直接消费prefix状态并学习T/top-p、基座权重冻结但实际采样分布改变**。唯一owner仍Ch20，PPO/训练算法只短handoff不另写Ch32。本段放完整decoding-config段后、Random seed标题前，承接固定参数与处理次序→条件选择→随机数消费。

## 两段逐字 PRE

参数的顺序固定后，数值本身还可以由一个独立的学习控制器决定：先保持基座权重冻结，读取当前 prefix 的 hidden state、logits、长度和 entropy，再为下一步提议 temperature 与 top-p。小型 policy 在有界动作区间内调节采样分布，而不是生成新知识或取代原 grammar、停止与资源约束；基座没变也不意味着输出分布没变。训练这份 controller 可以使用完整回答的任务 reward，部署时则按不断变化的 prefix 执行已学策略；状态自适应不等于一条线上轨迹中持续更新参数。<!-- source-family:SF-2026-ARXIV-2603-18428 -->

[受限摘要任务对照](https://arxiv.org/html/2603.18428v1)只将这种接口与 greedy、单一固定温度比较，组合 reward 上涨不证明事实正确、更好的参数搜索已被排除或学习始终稳定。Hidden/logit 特征、逐 token controller、离线生成和 reference 评价均有成本；controller、特征编码、动作边界与 processor 次序也须同 decoding config 一起版本化。信号不可得、任务迁移失配或质量/完整成本无净收益时，关闭 controller、回固定 temperature/top-p 或 greedy，并用独立任务评价，而不让可回退的参数接口自签安全与零开销。

## 静态注 PRE

- `SF-2026-ARXIV-2603-18428` — [exact-v1](https://arxiv.org/html/2603.18428v1) §3–5/Eqs1–2/Tables1–2；只采用冻结基座外的prefix-state→T/top-p控制接口。periodic离线controller更新≠线上逐轨迹学习；小模型摘要/单fixedT基线、reward代理、负early→late与ROUGE-only反侧及全部费用保留；不授通用稳定、事实正确、低风险或零开销，未核实现/复现。

待resume_mar18非准备者必要Source/actualowner/PRE一次窄核。未写Books或计safe/DAY。

## 非准备者必要 Source / actual owner / PRE：正式有限通过

resume_mar18 fresh仅本03-21补03-20上下文后，实际打开 exact-v1 HTML §3.1–3.3/Eqs1–2及§4.1–4.2/Tables1–2/§5（L71–245），核支持与直接反侧；actual Ch20 1–195及233–289、Ch19/21开篇实际读取，参数组合完整配置段后/Random seed前的两段逐字PRE和静态注均已回对。2+1+2=5按实际采样控制器的单组件差额成立，不把PPO或泛自改善名计新分。正式有限 Source/PRE PASS；未写入/未actualPOST/未计safe或DAY，写锁仍由root协调。

有限采用可与headline的同episode学习外推独立：原§4.1明确每完整summary后reward并periodic PPO更新，§3.1只证明prefix依赖动作，不披露线上每轨迹权重即时更新；PRE已将训练参数更新与已学policy的状态自适应分开。控制器直接改变T/top-p，基座冻结不能称生成分布不变。Gaussian动作policy比率非基座token likelihood比率，算法不在此owner重复。

独立回核T1 Qwen/WikiHow early→late −43.60%、Granite/arXiv −4.38%，T2 ROUGE-only .169<static .170、core −4.56%、sigmoid −4.27%，不能沿“稳定/无退步”文字。单fixedT=.3、static top-p/完整reward归一常数与评测prompt人口/重复不确定性未闭合，不采用最优静态baseline已排除、泛faithfulness或状态非退化的因果证明。小MLP参数不是隐藏读取/逐token处理/reference生成训练的端到端费用，硬件/SLO等ND保留。两PRE及静态注准确限定上述差额和反侧，无需修正文；只可据root新窄锁写原稿，再一次nonwriter完整正文/邻接/本人静态注actualPOST。

## nonwriter actual POST：正式有限通过

resume_mar18（非writer）实际顺读Ch20完整165–207：固定processor次序/完整config→新增178/180→Random seed及EOS交接，末五行含两邻注与本人701静态注逐字回对已正式通过PRE和必要exact-v1 §3–5。当前两正文与原literal一致，基座冻结≠生成分布不变、已学policy的prefix动作与periodic训练更新分开；单fixedT、proxy/稳定反侧、白盒特征与训练/reference全费、版本化config和固定/greedy退路均保留。marker/static各唯一，限定diffcheck空；实际POST正式有限PASS，可送root接纳释放Ch20窄锁并归并实际I，不授DAY，不修改静态注验收身份。
