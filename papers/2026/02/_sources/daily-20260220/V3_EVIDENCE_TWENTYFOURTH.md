# 02/20 第二十四有限证据包：Persistent E-Graph

## 2602.16707v1 — E-Graphs as a Persistent Compiler Abstraction

**2+1+2=5；跨pass equality-state生命周期差额深入，拟Ch49窄整合，待root必要源/actual owner PRE。** 既有首题摘准入不因PDF访问降格。v1 HTML404，官方[21页PDF](https://arxiv.org/pdf/2602.16707v1)实际必要页读：§4.1 p8–9、§4.2 p10–13、§5 p14–18；不借Aug3v2/Tamagoyaki收益。事件页轻核无可见撤回/勘误。沿已独核日期桥，lower2026-02-19T09:00:00+08:00，same-ID DOI Registered `2026-02-19T02:52:56.000Z` +1秒upper10:52:57+08:00，非精确公告点。

实际原生eqsat.eclass/egraph/const_eclass/yield把候选等式保在SSA graph region，constructive rewrite不毁旧候选，rebuilding恢复congruence；selection与replacement分开且可partial extraction，供下个cost model继续用未抽取eclass。实现只pure straight-line，不授sideeffects/controlflow/scope已解决；浮点rewrite需前置条件，不由real-arithmetic等价授bitwise等价。Herbie单round/禁series与regime、31FPBench、4000enode每例截断，规则及precision不同；Threadripper单core/Python3.13.1，fixed1024bit MPFR导致大额evaluation成本。combinedmatcher局部2.57x不等整编译加速，整体较Herbie约401x慢，不能从复用IR认定降时延。缓存候选、分析与验证成本不可省；完整performance/LLM kernel效果未证明。

Actual INFER-TENSORRT-LLM Ch49:18–28现有typed equality space→硬件schedule及egraph膨胀，尚未承载**跨lowering/analysis pass持续携带候选、partial extraction只提交部分实现**。拟在原typed-equality段后补一窄分支：原生IR保多层等式，constructive pass保候选，阶段cost model只select/replace已决部分，余状态继承；pure/controlflow与numeric semantics身份必须同行，候选不是任意pass可破坏后仍有效。增长/匹配/高精度check与编译费用近文，不授tensor性能收益；不兼容pass/预算不足回到显式extract+既有pipeline，保该旧路径合理。请求Ch49一段+own末注锁，尚未写。

## 当前停点

作者必要证据完成不等root通过。本项仍普通待办，README84/普通12未动；16545/16664另在必要方法/评价处理中，不在此借整包终态。无stage/commit/push。

## 独立处置追加（2026-10-05）

16707 Ch49 body26/18–38完整邻接/自身末注root实际POST通过；仅跨pass persistent equality-state/partial extraction，原84为历史停点，不授日级。
