# 2604.24955v1 BenchGuard：可执行 benchmark 工件互核

- 官方首版：[BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks](https://arxiv.org/html/2604.24955v1)，本日 arXiv 08:00 北京公告的窄批次链支持窗口归属，仍须日级 first-public 例外核；不能以首页 `27 Apr` submitted 字段单独定公开日。本文未核后稿、全附件或代码复现。
- 范围：只将其作为 Agent **evaluation infrastructure** 的机制/反证，不因 ScienceAgentBench 与 BIXBench 的科学/生信任务恢复 AI-for-Science 应用研究。

## 决定性原文与反证

官方 §3.1–3.3 的输入不是模型回答而是四种可执行 benchmark 工件：自然语言 task instruction、gold/reference program、evaluation script、environment configuration。定义层用同一任务的四者作 LLM/静态规则互核；有 Agent program/trace 时再附加执行层证据。其分类优先把 instruction/gold 两可归属问题先放 instruction，合并一个修复可消除的重复问题，输出带源位置的待人工确认 finding；审计器本身不获真值或自动修复权。这个发布前 cross-artifact check 与只对 Agent 输出做 judge 不同。

§4–5 的直接校准只覆盖两组 benchmark。ScienceAgentBench 有 102 tasks，作者报告找出并获原 benchmark 作者确认的 12 个缺陷；Table 2 的 recall **以这 12 个已确认缺陷为分母**，其 precision 仅在含已确认缺陷的 task 上计算，不能读成全部 102 task 的无条件误报率。BIXBench Verified-50 的 17 个被专家修订 task 被拆为 24 个 atomic issues；五模型 union 20/24 exact=83.3%、23/24 包含 partial=95.8%，不是 50 task 的真实性覆盖率。Table 3 的所谓 precision 是与旧专家修订的 alignment；§5.2 Case 6 又有未被专家修订记录却可能真实的缺陷，故 alignment 不等于真实 precision。即使 50-task 五模型 API audit 费用为 $14.38，也未计完整人工 adjudication/环境复验成本。§3.2 的 LLM 自报 confidence 分桶不是校准概率，§4.3 Gemini temperature 1 且单次运行也限制稳定性。

## 真实 owner 与作者侧处置

已对照 [Ch66 当前 Evaluation Identity](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)约 193–200、Agent Regression Testing 约 751–764、Benchmark 生成器约 919–936 与 executable alternative-path 段约 963–970。现文明确 task/evaluator revision、component receipt、stale/missing tests、生成器与 verifier lineage、alternative valid paths，却尚未把 **instruction × gold program × scoring code × environment 的跨工件一致性**定义为 benchmark 发布前的单独审计对象；尤其 reference program 与 task specification 的静态矛盾在 Agent 运行前即可发现，不能仅用后验成功率或 test revision 表代替。这里有窄长期缺口，不把 BenchGuard 整套 taxonomy、六步提示或五模型 ensemble 当必选架构。

拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，Standard；Ch66 真知识增量触发必要局部深入。Books 拟 **Integrate**，但必须先由非作者 source→actual-owner 核与共享 Ch66 锁，实际写后再核；在此前仅为作者侧提案，不能计整合或日级 Gate。建议插在 Ch66 benchmark 生成器段后：

> 生成任务的入口/筛选来源可信仍不足以保证题目可执行且评分正确。发布前对每个可执行 Agent task 同时版本化并交叉核对自然语言要求、reference program、scoring script 与 environment：先查要求与 gold 的隐含参数/数据处理差异，再查 scorer 是否接受规范允许的替代解、容差与随机性，最后核环境路径/依赖/资源能否执行；已有候选 Agent trace 可作为定点反例，而不能让同一模型自报“无问题”签通过。发现不一致应记录原始工件、最小复现、严重度与修订后重跑，由 benchmark owner/领域专家裁决。
>
 这道 audit 增加上下文加载、模型调用与人工确认成本，而且同源 LLM 可能共享盲点、把合理领域惯例误判成缺陷。确定性静态检查与小样本专家核仍是可回退基线；若任务无可执行 oracle、存在不可逆现实副作用或环境难以重放，不能套用该协议的检出率。作者的 12 个确认缺陷与 20/24 专家修订对齐只证明两套有限 benchmark 的查漏价值，既不是其他基准的缺陷流行率，也不是自动审计器的发布放行保证。

本篇原在 106 个完整题摘的潜在工作池，尚未改 `64 潜在+41 前闭+1 日期隔离` 或冻结正式候选分母；先完成非作者必要核与日级日期/来源 Gate。
