# 2604.24118v1 AgentVisor：安全准入的必要原文消歧

本页只审旧111开放线索中的一个 Source Family。固定日窗仍为 `[2026-04-27T09:00:00+08:00, 2026-04-28T09:00:00+08:00)`；[arXiv exact-v1](https://arxiv.org/html/2604.24118v1) 页眉 `27 Apr 2026` 是提交字段，归属尚需官方公告批次组合，不能单凭该字段定时。本条是作者侧必要证据与 owner 对读，**待非作者准入/反证复核，不计冻结候选、Books 或本日 Gate**。

## 可取的局部机制与中心反证

- v1 §4.1–4.3 把 Guest 的 tool-call proposal、只读结构化历史的 Visor、Suitability/Taint/Integrity 三层审核和 structured exception 分开。实验 §5.1 是 OpenPromptInjection 4,900 direct cases、AgentDojo 629 indirect cases；受测 benchmark 的 ASR/utility 是局部结果，不是开放环境 authorization 保证。§6.4 的 benign 约1.4×、attack 约1.7–2.3× latency 与 §8 的长上下文、模态限制不可删。
- **关键控制流缺口：** v1 §4.1 Eq(6)–(7) 写 `T′` 由 Guest 接 exception 重生后直接成为 executed action；§4.4 明说 regenerates once and executes immediately；Appendix A Algorithm 1 第 1 行只对原始 `T_raw` 作 `STI_Audit`，第 6–8 行在 exception 分支 request `T′` 后直接 `Execute T′`，没有展示对修订参数/目标重新执行 STI 审核。故即使首轮拦截有效，所披露的控制流**不能单独支持每个实际 effect 都经独立 reference monitor 授权**。这只是基于作者文字与算法的潜在协议反例，不是已验证实现漏洞；若具体代码另有不可绕过的最终检查，应在版本化实现处定点重开。
- Ch72 `PLATFORM-SECURITY` 已有 proposal→authorization→effect、value/sink binding 与执行前重验的长期权责（正文约 520、911–913、1033、1127）；AgentVisor 不提供新的权限 owner，但其“恢复分支绕开自己首轮 audit”的**具体设计反证**能改变对该安全声称的采信。静态 schema/permission 旧路径仍合理；semantic visor 是受限 sensor，exception 可改善 utility，却不能继承 reference-monitor 保证。不能因为 0.65%/1.45% 摘要数字把未经重验的动作提升为受权执行。

## 当前建议（待独立复核）

贡献准入：保留为 6 分安全候选的**工作提案**，`Design Delta 2 + System Reach 2 + Durability 2`，触发深入审阅；中心“semantic virtualization enforces security”的充分性暂作窄争议。Books 先不正面整合新 guard 机制，Ch72 是否已完整承载该反证交非作者 source→owner 判断。若归属、实现 final-check 或对照口径发生变化，只重开此家族；不以这一条扩张其他安全论文全文队列。
