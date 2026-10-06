# 02/20 Security PRE：15945 / PCAS 16708

`books/part-06-ai-infrastructure/72-security.md` 的现有 `Prompt Injection 与 Tool Boundary` 之执行器管线和第78交接后、固定GUI执行图前的两项窄增量已经落实：15945一段、PCAS两段及各末注。root已实际核必要原源/owner PRE，并于实际1215–1245正文完整邻接与末注POST确认通过、释放窄锁；不授日级完成。已实际加载 Books 指定上下文，重用未变；owner实际读625–651、874–909、1207–1252、2278–2287，71/73开篇交接及83授权/program提案段。仅针对实际差额，不把整个已脏 Security 归本日。

## 15945：exception-mediated capability corruption

精确 [v1](https://arxiv.org/html/2602.15945v1) §2.2/4 是代码执行减少中间context；§6.1为10servers/20single+10two+4three任务、三GPT模型、三GPT4o judges，受限performance解释不作跨系统归因证明。§6.3四受控攻击，GPT4o/4.1，attack4 `inspect_db` valid schema后抛异常，verbatim反馈使re-generated code调用已有admin/write工具，sandbox没有escape。没有各攻击重复次数/variance的公开精确计数；§8.3未adaptive stress-test，防御并不认证完整覆盖。原文“exclusive CE-MCP”只对应其两代理实现，不泛称传统tool agent无法被异常反馈注入。

已有覆盖：正文有untrusted context→action、scope/独立policy及固定execution图不能保证effect，83有program proposal/effect/budget/continuation；但尚未指明exception被回灌re-generation后，在沙箱允许的合法工具内扩大authority这一具体路径。

拟一自然段：业务程序失败需要错误反馈/重试，旧方案合理；错误是untrusted data，不因runtime产生就成指令。再生成是新的program proposal，须重新验typed/effect/parameter权限，exception schema/provenance与counter/resource预算保留；sandbox隔离不阻止既有合法write能力滥用；受控反例不授传统代理免责或semantic gate普遍防住。更严格feedback/重验证增加恢复成本，低风险typed errors/单步endpoint仍共存。

## 16708：exact-v1 PCAS，不借后来 FORGE 身份

精确 [v1](https://arxiv.org/html/2602.16708v1) 标题 **Policy Compiler for Secure Agentic Systems**。§3Alg1是每action执行前独立monitor与backward causal slice；§4.1 TCB/infrastructure可信且complete mediation为前提，旁路code/socket/sharedmemory未覆盖；§4.2政策由ClaudeCode辅助+手工review，自动合成/完整性验证未来；§4.4 authenticated principal+event dependencies→Datalog facts增量engine→allow/deny trace；§4.5 recursiveDepends追溯跨agent因果，不只单call属性；§5 prompt与instrumented对照，5trials/task，重复denial产生recover overhead，reasoning/task失败仍可能。§6.1覆盖和规格正确性限制、§6.3机器compiler correctness proof future。仅采用机制/条件，不授源码已验或全部action绝对零违规。

已有覆盖：独立policy/refmonitor、label传播已有，2278静态facts/Datalog proposal审计有abstraction completeness；差额是运行时动态事件因果图以recursive provenance授action，和它的“完整观测+手写规格”两前提，不是补一个Datalog名字。

拟两自然段：静态逐call属性在短链合理，跨agent approval/untrusted+sensitive组合需要在可信runtime记action/message edges与authenticatedprincipal，policy查询transitive backward slice，deny反馈不变成新authority；观测graph只facts、决策policy、effectcommit执行器。成本在graph/incremental查询与retry；complete mediation/TCB/规格完整性是负载条件，未捕获侧通道/任意code不能被声明guarantee，machineproof尚未来，信息缺失需隔离并保持leastprivileged/人工批准/简单allowlist。

以上保留原PRE论证与采用边界；实际写入及POST已通过，不以PRE或POST授日级完成。未核实现或复现实验。
