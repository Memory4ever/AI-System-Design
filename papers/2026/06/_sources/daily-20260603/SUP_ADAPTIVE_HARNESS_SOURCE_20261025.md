# 01770：构造可选Harness与选中可用分支是两种能力

仅06-03补Jun02，当前AGENTS/Research与Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP及本日停点有效加载。R62完整v1题摘/联合Jun02日证复用；[当前abs](https://arxiv.org/abs/2606.01770)有Jun03 v2但无所见撤回/勘误，版本号不单独触发比较。[exact-v1](https://arxiv.org/html/2606.01770v1)本次实际读§3–6核心方法/主评价/限制及B完整执行/成本/temporal/branch说明、G完整routing人口/对照与直接反侧；未读所有task logs/prompt、图像像素/代码，未运行容器/实验。访问2026-10-25 BJT。

## 必要机制与反侧

固定LLM参数，演化对象是prompt/skills/tools/infra而非权重。按Analyze/parallelResearch/Build/Verify分工，evolver workspace持久保task board、已试假设、测试和架构；solver workspace另保版本化harness branches。构造分支发生在evolution阶段，solve时router只看当前任务与branch metadata/文件再选分支执行，不读取目标标签或事后各branch结果。Git在此是版本/lineage工具，不由checkout字样推完整并发隔离/凭据继承/权限正确性。

Temporal-reveal只在resolution后把outcome给evolver，未解任务保无label轨迹；已完成任务标签可成为后轮训练信号，不得倒灌当前router。API凭据/新source可由具名human hook补，不能把人类输入泛称已排除人工影响。原文仅有限100-task HITL例，而非随机人群普遍收益。执行时间过滤也不能自己证明闭源模型权重没有未来知识；本次不把forecast分数当历史真实部署无泄漏证明，不扩假想全部模型pretrain调查。

§3.2 regret拆分是插入oracle再相减的会计式；容量约束sup没有构造出真实可达oracle或同预算重建算法，L_evo/L_adapt未直接测量。历史缺信号不使已有加减恒等式失效；不能照文把该句提升为证明两个loss之外有第三定理，更不由树结构推非零gap必存在。只采用两接口分别验收的设计，不用oracle公式签可部署最优。

主实验三chronological streams（5075/261/503任务、51/14/26cycles），Sonnet4.6 solver/Opus4.6 evolver、温度0，不训练权重。主表Full并非每项最高：FutureX Multi49.5高于Full47.3，PolyReturn Adaptive高于Full；不能把三个variant各自胜处拼成单一系统普胜。三角色/反馈/记忆局部消融改变上下文预算和组织，未证唯一multiagent因果。温度0仍是点估计，不代表训练/服务完全确定或无provider drift。

§4.5说Adapt为category-based routing，而G细化为live LLM router的actual choice；本次按G保其披露的人口，不拼成单一已核实现。nav 100/60/80与complete replay 80/40/58不同，早batch没有全部后建branch，不能将后期全branch oracle当当时可用线上选择。G原文对oracle-naive称empirical L_adapt，§6同时说oracle losses未直接估，故只作所选有限branch-set的posthoc headroom，不等§3全capacity oracle。Replay的FutureX Adapt34.5低于main39.7；所有nav上允许main fallback却一次未用，因此只“配置了回退”不等已验证会回退。低branch pass率有任务难度选择混杂，不能只按branch均分删分支。G区间/paired检验是作者有限subset协议，不授未来流保证。

B给solver max80turn、evolver128K tokens、3researchers、3build/verify retries、confidence threshold.7、worker24/8/10，task batch相同不等总费用。表5仅solver input/output token；evolver tokens未持久化，wallclock为逐任务耗时求和且排orchestration，不能当并发makespan或完整evolution成本。API模型precision/硬件/参数数、完整provider版本锁/服务SLO未披露不补。历史制备、演化/测试、分支驻留/路由读取、全部solver与人工/权限回归均计费；不是去微调所以免费，未复现实现。

## 正式拟分/actual owner与最小稿

拟2+2+2=6：长期持久构造与当次选择两个控制接口/不同失效和验证人口，跨harness资产/evolution→solver消费；不借数学oracle或多bench/数量给分。唯一`AGENT-PLATFORM` Ch84，非Ch81执行流程或Ch77记忆第二owner。

精确family/Adaptive Harness定点查Books，仅Ch84旧Daily06-02 trace称NC，本次不搬该旧字段，也不将marker一行当已覆盖。实际完整读“版本化Harness Controller”两基础段、紧接demonstration定位/提交两段、“Context Assembly Selection Probability不是Outcome Confidence”三段、“自适应Harness只能提交保持成功约束的干预”两段。现文已有版本控制/独立release、选配置概率非成功概率、shadow/canary和反馈门，但没有构造branch集合与router选用两个状态、available-at-time完整replay人口与configured-but-unused fallback分验的具体接口。因此提案小gap；若独核找到实际充分正文则具体NC，不为trace推翻有效旧研究或重跑旧日。Ch83连接协议与Ch84收束在ROADMAP中分工明确，不在那里重复路由实现。

拟在“可训练harness…exact-v1只覆盖三个domain与两个provider…”完整第二段及2607-25415独立marker之后、现demonstration-guided semantic-body-binding组之前，仅以下两段：

> 面对持续变化的任务，还可把“构造可选harness”与“当前任务选用哪版”分成两个状态：演化器保留跨轮经验、测试与多个带lineage的prompt/skill/tool分支，solver只读取当时可用分支，由router按当前任务选择，不把最新一版无条件覆盖所有旧路径。[受限harness-tree实现](https://arxiv.org/html/2606.01770v1#S3)将演化workspace与求解workspace分开，延迟outcome只在真正揭示后交回演化器；分支metadata、任务上下文和可见反馈须随版本保存。选择某分支的信心不是结果正确概率，配置了main fallback也不说明实际会使用它。
>
> 验证这条分支时，应分别测分支集合提供的有限headroom、router实际捕获多少，以及演化和求解的全部费用；事后让每题跑完所有branch再取最好，只是诊断参照，不是线上可用oracle。该实现的有限replay中，某任务流的路由仍弱于固定main，较完整系统也未处处优于只做演化；局部收益不能由不同variant拼成普遍胜出。新增经验、分支驻留、路由读取、全部演化/测试与人工介入都付费，只有solver tokens或逐任务耗时和不代表总成本/并发时延。分支支持、反馈时间或质量预算失配时，保留已验静态harness、固定main与独立release/权限门，不由更大的树或一次路由高分批准发布。<!-- source-family:SF-2026-ARXIV-2606-01770 -->

首次必要/评分/actualowner与原两段PRE待唯一独核，未写Book/Report，不预I/DAY。支持与直接反侧足够即停止，不为假想最优扩全日志/代码。
