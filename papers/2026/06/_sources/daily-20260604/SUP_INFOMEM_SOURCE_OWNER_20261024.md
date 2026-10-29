# InfoMem 03329 — necessary Source / actual owner / PRE

作者supp_20260604_author；R2准入/Jun03日期已过。2+1+2=5，具体memory reward边界深入。exact-v1完整TEXT72554chars实存，作者必要读§3–6/Limitations/A1–3，支持与反侧足够停止；未核实现或复现。

## 必要证据

§3.3明确不是distribution MI，而single-sample model-induced pointwise surrogate。§4 Eq6用teacherforced gold answer逐token平均logP(x,M)-logP(x,null)，只训练期需gold；matching成功子集S上加gain，同组成功内先zscore再与outcome组合，与GRPO后续groupnorm分开。S0不给gain，S1保原raw fallback，不称每组都标准化。reward detached，最终advantage给memoryupdate与answer全部tokens，不是局部memoryspan归因/每step evidence打分。正常boxed matching只取最后300chars并规范化，成功标签资格绑定此parser，不天然答案真实/完整。

§5：Qwen2.5-1.5B，RULER-HotpotQA512/128，200docs；n8/120steps/lr1e-6/chunk5000/maxmemory1024/beta.2，同data/model/rollout/budget vsoutcome-only；16H20约440GPUh每run。四evalbenchmark不同指标：MRCR100下采样sequence-match/CorpusQA128K与LongMemEval115K KimiK2.6judge/RULER F1，不能合平均当统一质量；主绝对数仍低，MRCR0.279百分比不改写27.9%。ReMemR1 callback自身架构不同，不把全部差额归reward。

§6错/双侧gain中期collapse、去precompose norm退，QueryPMI更易复制query且任务分更低；只限此recipe，不证明全部失败轨迹都无信息或query-conditionedobjectives都不可用。无outcome诊断仍用outcome定义successside，所以不是无监督。SQuAD合成幻觉区分只诊断labelled三context，不授开放事实验证。因同query null-memory baseline常数，在|S|≥2同组zscore中常数相消，不能以此单项识别nullbaseline独立因果（本项目代数观察，不改原实现）。额外gold双前向、长context rollout、norm与独立判分均计费；无gold/评分器漂移或可靠性不足保原始episode/outcome-only/内容核验。

## actual owner / PRE

三context/ROADMAP已读，唯一AGENT-MEMORY Ch77。actual“从OutcomeReward到Content-levelCredit”完整MemPO两段（182–184）与后VideoEMem完整段+marker已读；原方案比较压缩memory与完整轨迹并仅memoryspan加credit，本项比较null memory、successgate/precompose norm却把advantage给全部生成tokens，不能当同一局部归因或因为同likelihood给NC。GRPO通用optimizer仍Ch33，不在此复制推导。

完整上锚：

这个分支需要额外答案评分与 memory 边界，且不同 step/rollout 已观察的工具信息不等价，baseline 修正并未消除全部状态偏差；提高答案似然也可能固化模型先验。[MemPO 的受限对照](https://arxiv.org/html/2603.00680v1)在同 backbone、环境与 memory 设定下比较辅助 reward，但跨方法完整/截断上下文不同，token 数也不包括全部训练评分成本。它不证明开放任务保真或永久丢弃原始轨迹安全。缺少 gold、scorer 漂移或必要证据被压掉时，应保留原始 episode，回退 outcome-only/可靠内容核验，再由独立 held-out 评价决定是否采用学习出的 memory 策略。<!-- source-family:SF-2026-ARXIV-2603-00680 -->

拟增两段：

终态记忆还可以用另一份训练代理评价：在同一问题上，比较模型对 gold answer 的逐 token 平均似然在有最终记忆与空记忆时的差额，再只对已通过答案匹配的轨迹区分其记忆支持度。一条[受限奖励分支](https://arxiv.org/html/2606.03329v1)先在同组成功轨迹内归一这一分数，再与 outcome reward 组合；这一步不是 GRPO 对最终奖励的组归一。没有成功项时不加此分数，只有一项时保留 raw 值，故不能称所有组都受到同等尺度控制。奖励虽然读取最终记忆，产生的轨迹 advantage 却作用于记忆更新和答案的全部生成 token，不提供逐条记忆或逐步写入的因果信用。<!-- source-family:SF-2026-ARXIV-2606-03329 -->

这里测得的是带 gold、模型与提示条件的点似然代理，不是分布级 mutual information 或事实真值；仅用 query 似然甚至可能奖励复制问题，而不是保存答案证据。局部错侧监督退化、成功侧更稳的对照也不证明所有失败轨迹都无学习价值，更不能把训练期的正确答案偷带进部署。长 Context rollout、额外答案评分、归一与独立任务验证均需计费；gold、匹配规则或评分器资格不可靠时，应保留原 episode、outcome-only 与可靠内容检查，不让较高 likelihood 或受选成功人口批准无损压缩、永久删除与线上事实写入。<!-- source-family:SF-2026-ARXIV-2606-03329 -->

完整下锚：

未来query未知时，writer还可先按source保留而非开发QA成功来演化：逐级压缩caption并回查遗漏、另选与text互补的原帧，冻结memory后才用QA失败调整reader的定位和组织。[Video-EMem的受限控制](https://arxiv.org/html/2610.24537v1#S3.SS4)把memory缺失与reader漏读分开，前者不能算后者的定位错误；但caption和语义match仍是proxy，source未观察到的事实不能由更多压缩容量补回。分阶段优于jointQA的局部差额未独自证明overfit因果，query-time或持久payload变小也未包含全部构建/演化费用。caption、原帧、全部候选/审核、索引和query调用都计费；source保留、版本或后query回归不合时保原episode、curatedmemory与完整读取，不由writer分数或低存储批准完整事实和任意未来可答。
<!-- source-family:SF-2026-ARXIV-2610-24537 -->

Review note拟：`SF-2026-ARXIV-2606-03329`：2+1+2=5；exact-v1 §3–6/Limitations/A1–3，goldanswer/nullmemory似然代理、successside/precompose norm与S0/S1、alltoken trajectorycredit分责；保boxed parser资格、1.5B/512样本/16H20每run440GPUh、异指标/低绝对分与callback差异，QueryPMI复制/失败侧非普遍定律及全部费用。未核实现或复现。待实际写后复核。
