# 11214：长程安全能力评价必要Source / 具体已有覆盖提案

mar14_supplement。精确[2603.11214v1](https://arxiv.org/html/2603.11214v1)本地`SUP_NECESSARY_11214.raw`，请求UTC/200/bytes在`SUP_NEXT_SOURCE_MANIFEST_RESULT.json`。完整题摘校准已通过；14作者，当前abs列v1/v2/v3，轻量说明未识别具名撤回、纠错或重要变化，不为版本号遍历diff。官方日级夹证见`SUP_DATE_SECOND.md`/`SUP_DATE_11214.raw`：v1Wed18:30:17UTC明确晚截止，owning arxiv.content/findable精确DOI与URL、registeredMar13 01:50:24UTC为公开上界；下界依已核官方发布/ID规则，不拿提交或注册单独作first-public。未见具名提前正文信号。

## 实际必要Source / 评分

实际精确v1 §2完整必要结果/Table1、§3.1–3.3方法/计分/实验设计、§5–6直接限制；不读AppendixC攻击战术链/提示模板、代码或每条攻击轨迹。这里只保留评价机制、条件和反证，不提供攻击执行指导。**2+1+2=5标准完成拟**：新增局部证据把孤立CTF/单预算的能力判断推到可延续长程任务，不计ReAct/compaction等成熟原理为新机制；SystemReach1仅两靶场评价人口，不因网络跨host或安全标签授2；Durability2为预算与能力/自治测量分责。具体安全评价反侧必要深入此有限范围，不机械要求全附件。

两purpose-built VM范围32/7步骤，无active defender，alerts记录但不阻挡/惩罚；只有两个环境，vulnerability与artifact密度不等生产。一个step一个programmatic flag：企业链观察到后段flag就计此前全部完成，依赖“后段不可达但前段未做”的假设；另一环境仅计实际观测flag，因为依赖更独立且出现非预期路径。该假设/计分区别不能由名字相同的step或log直接继承，线性step也不等线性完整自治。本文14/15h human估计是专家判断，未做计时humantrial，best22/32对应6h不是模型达到6h人类完整任务的实测。

七模型API/不同release与10M/100M **总token**预算，不是输出token或实际硬件compute等价。标准agent+context约80%时同模型总结/重开上下文，全history每次输入与compaction都产生调用成本；未实际核counter，不认证完整budget-accounting实现。compaction重置输入cache，$80是当时作者假定价格/cache下估算，不当当前价格、全VM/tool成本或TCO。硬件、权重precision/完全运行配置、全tool/wallclock费用未充分披露，线上SLO不适用；未核artifact或复现。

Table1企业平均Sonnet4.5 6.1→9.4、Opus4.6 9.8→15.6；固定预算不同谱系不严格单调，5.3Codex10M 7.2低于5.1的8，100M同11。100M每最新模型5attempts，高variance best22 vs平均15.6，sample/SE只限所测。GPT4o存在step2 plateau，与全体“无plateau”摘要分开；两range/有限预算不支持普遍log law或1B一定更好。ICS100M最优平均1.4/7，依赖与difficulty不能和32步直接等比。一般capability进展不是真实defendednetwork危险概率。

§2.4额外high-level提示与prefill示例未显著增益；tool error缓解没带来给定token下显著进展，较长prompt开销是未隔离的解释；关联行为模型被attacklength混杂。Alerts未给robustbaseline，不能认证stealth或防守有效。较少longrun还是较多独立尝试的固定预算最佳分配仍open，不能把本实验写成已解optimal allocation。最后公开场景会损害后续heldout，作者canary/exclude请求不证明未知训练数据无污染。

## 实际owner比较 / NC提案

实际读取`PLATFORM-EVALUATION-SYSTEM` Ch66完整2134–2204（攻击风险曲线→时间轴→Security Agent cost-success-refusal及前后）、4587–4622 threat profile完整邻接、569–603投入控制/限额与EvalSpec人口、934–1001 final-pass/trajectory/executable verifier、1658–1675预算形状、1720–1742到达状态与从状态求解、4186–4222native-runtime workload局部；Ch65/67入口与Ch72 857–884 security trace/predicate交接。当前actual正文已承载拟采用命题：

- 2140风险曲线绑定model/sampler/attack distribution/budget/uncertainty，并要求高风险大预算验证；2168节把budget/API工具费/refusal/policy/contamination与success同curve，offensive与defensive不共享success，peak不是能力。
- 1663完整预算shape区分width与depth、matchedtotalcompute/seed/停止；573分清effort与hardcap/实际token；4186/4190保存cachehit/KVlifetime/toolpause/真实长时trace，非staticprompt。
- 934完整finalpass节保存尝试/恢复/独立executable outcomes，1724冻结同checkpoint后的conditional求解，不将中间状态视为任务完成；4587实际profile包含access/adaptiveness/coverage/真实harm与未测维度，高风险局部失败不签发最坏安全。

本稿无active defender/有限靶场的长程预算证据支持这些现有设计选择，不改变上述责任分层；flag前置闭包是其特定environment假设，未作为新的通用计分定理得到独立证明，不能为补章节diff将它推广成新score协议。真实human计时、defence/alert baseline、long-vs-reset最佳shape仍未证。**已有覆盖/Books新写0**，保留新增局部评价证据在报告，不只因主题映射NC，不新增32步数字或“1B增长”宣传。独立reviewer mar13_admission_review在本日fresh context实际必要原证+对应完整正文独核通过；其counter精度建议已收窄，不声称实现复现。无书写锁/PRE写入请求，不授DAY。
