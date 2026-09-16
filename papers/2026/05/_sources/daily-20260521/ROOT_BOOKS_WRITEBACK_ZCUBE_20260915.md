# 2026-05-21 Root Books Writeback — ZCube

## Scope

本次只落实作者冻结队列中的 ZCube `Integrate`，不重判其余候选。共享 Books 继续按日报日期顺序写入。

## Applied binding

- Source Family：`SF-2026-ZAI-ZCUBE-INFERENCE-NETWORK`
- Stable Node：`INFER-PD-DISAGGREGATION`
- Owner：`books/part-05-inference-system/55-pd-disaggregation.md`
- Binding：`semantic-body-binding:SF-2026-ZAI-ZCUBE-INFERENCE-NETWORK`
- 位置：`从共享链路调度到物理 Traffic-class Isolation` 内，位于首个 `## Review notes` 之前。

正文保留了 Clos/ROFT 与 ECMP 在通用、静态、近似对称流量下仍合理的原因，再引入 P/D 非对称时变流量对 topology/path ownership 的新约束。网络控制面拥有 topology/route revision，请求调度器只在受验证路径上 placement；故障或流量假设失效时回退多路径、ECMP、共置或带宽隔离。

官方厂商数字只作为 GLM-5.1 coding workload、披露集群与运行周期内的受限证据；缺少逐请求 telemetry 和独立复现，正文不把成本、吞吐或 P99 改善外推为通用结论。

## Remaining gate

Root 已验证 marker 成对且唯一、写入位于 Review notes 前、scoped `git diff --check` 通过。该记录不替代 fresh non-author 对来源日期、候选分母、Evidence、Books 比较和相邻语义的最终复核。
