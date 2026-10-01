# 04/20 两项无单独同行文件的受限 Evidence→Owner 复核

复核者 root；日报作者 apr20_resume。2026-09-28。本核仅补正式 §4 中的两项，实际重新打开官方 exact-v1 方法、评价与限制，并对读现有 Books 论点；不是这两篇实验的复现，也不替代整日来源、日期及准入 Gate。

| 家族 | 必要证据与真实 owner | 裁决 |
| --- | --- | --- |
| [2604.16004v1 AgentV-RL](https://arxiv.org/html/2604.16004v1) | §3.1–3.3 的 forward/backward verifier 沿前提与结论反向检查、工具辅助、两路分数融合是特定验证策略；两路可以共享模型/工具/数据，不能因此升格为独立 truth。§4.3.4 Table 5 单 A100、vLLM、batch128 将 base 2560 tokens/119s 与 full 8349 tokens/323.4s 分开，约3.3倍 token、2.7倍时间；不含生产 p99 或工具真实 effect。Ch66 已将 proposal、外证、judge、成本和最终 outcome 分账；Ch79 工具动作也不能以评分代替授权与完成。 | **6分标准、仅报告 PASS。** 保受限双向验证/成本选择，不新增通用真值或生产吞吐断言，不修改 Books。 |
| [2604.16007v1 MemExplorer](https://arxiv.org/html/2604.16007v1) | §2/4/5 用解析和时序近似联合探索 SRAM、HBM/HBF、mapping、算子流量与 prefill/decode；§5.6/Table 9 对 PLENA emulator 的 814.14ms，作者模型 731.11ms，仅为 Llama-3.3-70B/4096 输入下选取的 transformer block 比较，不是芯片制造或整机性能。§7 明言未建 C2C/多设备共享内存和混合精度，并计划以后实机验证。Ch54 `Memory hierarchy 设计必须寻找 phase-specific working-set knee` 已具体要求 operator trace、层级流量、mapping、cycle、phase-specific knee 与实机 profile 回退。 | **6分标准、窄已有覆盖 PASS。** 只覆盖设计期 evaluator 与真实验证分责，不说现章已有其具体技术枚举、Pareto 数字或芯片实测。 |

日期仅复用本日官方公告规则、OAI/相邻 ID 的联合归属链，不把 HTML 页眉或上述评价段当逐篇首公开证明。两项的旧聊天口头判断在此落为可查的有限非作者记录；完整日级 Gate 另签。
