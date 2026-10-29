# Agent libOS — necessary Source / concrete No Change

作者supp_20260604_author；R1准入/日期已通过。精确v1完整题摘/正文均在同日SUP_ABS/SUP_CORE_2606.03895v1_20261024.html，作者已读§3–7支持/反侧，未运行代码或测试。

2+2+2=6，权限边界变化深入受影响范围。§3.1区分模型工具schema visibility、ToolBroker invocation与primitive manager resource authority；§4.1 fork不默认继承filesystem-write、exec不自授新image所需caps；§4.3 point-of-use check/revoke与批准成功primitive一次消耗；§4.5–4.6 JIT Deno无默认host权限，只经绑定process-id syscall进入primitive，tools-as-wrapper不能绕权。只采用这条分层，不把OS类比、静态禁词或Deno权限当形式sandbox。

关键反侧：§4.2 payload仅volatile heap，SQLite只directory metadata，不称完整durable object restore；checkpoint重建metadata不回滚irreversible external effects。§6为作者123-test regression suite与deterministic demo，未报告end-task success/latency/cost/human workload，red-team仍future。§7无kernel-grade isolation/distributed scheduler/verified access control/transaction rollback；更强容器或microVM及具体policy hardening另需验证。

Books三context/ROADMAP已加载。actual owner为AGENT-PLATFORM/Ch84；已实际读完整§三个平面与primitive effect authority邻接（512–565），前后章交接核Ch83开篇，不向Ch78重复集成。当前Ch84 `### 快速演进的 Skill / Tool Layer 不能拥有 Primitive Effect Authority`（527起）已具体承载：可变skill/tool仅提案→typed primitive→caps/path/object/resource/informationflow/human→effect receipt；catalog存在≠principal权限、fork不能全继承；保治理成本/恶意proposal仍可能/拒绝或只读回退。549又明确exact2606.03895v1/123-test只支持架构非开放prompt injection解或生产SLO，551有`semantic-body-binding:SF-AGENT-LIBOS`，1356有同族末注。故本次**已有覆盖/No Change**，不是主题相同而收据自证；不新写、不改旧末注Daily Jun03日期、不计新I。待reader独立具体NC确认。
