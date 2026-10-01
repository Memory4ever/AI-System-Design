# 2604.15549v1 范围／贡献定点重开（作者工作态）

本文件记录 15549 的前分母理由重开与作者必要原文。原始记录见 `v3-reopen-notes.md:82` 与 `V3_NEGATIVE_SIDE_SCREEN_LEDGER.md` 的范围外层。原理由把“未显示大模型计算、模型状态”用作主要排除依据，误触当前研究合同 §3 不以模型大小或是否写明 LLM 划范围的约束。后续 root 已有界独立核准准入、标准审阅与仅报告；本文件不代表 Books 写入或日级 Gate。

## 必要原文与可能增量

- [官方 exact-v1](https://arxiv.org/html/2604.15549v1) 摘要、§1.2、§2.2–2.5、§4.4、§6.1–6.2：作者在 decentralized federated learning 的参数混合中，把 D-PSGD 对称双随机矩阵／双向图与 SGP 非对称混合／有向图分开；优化目标不是孤立的通信次数或谱间隙，而是达到训练收敛条件所需的 transmission slots。§4.4 式(19)以最大入／出度与图直径构造可算上界，§5 在强连通约束下设计有向图。此为训练优化与通信拓扑的实际联合选择，不是仅把既有 FL 搬到另一应用。
- §6.1 的任务是 33 节点 random geometric / Roofnet 无线图上的 CIFAR-10、1.5M 参数 ResNet-50、batch 64，停止条件是连续五个 epoch 的平均测试准确率达 80%；§6.2 Table 1 在其时隙模型下 proposed 对 BASS optimized 为 RG 179,712 vs 228,528 slots、Roofnet 170,688 vs 192,528 slots。Vanilla SGP 比 D-PSGD 更差，支持“拓扑与 mixing 联合设计”而非“换 SGP 自然更快”的有限区分。
- §2.3–2.4 假设 smoothness、有界随机梯度方差、数据异质性、每 B 轮强连通及同步更新；半双工全向广播、冲突边不能同一时隙、每时隙完成参数传输是其成本代理。噪声、重传、计算、模型状态/optimizer、GPU fabric、任意大模型的 wall-clock 或 end-to-end 收敛均未由 Table 1 建立。§6.1 的“real dataset”不是实际 33-node wireless deployment 证据。

## 实际 owner 对读与待独立问题

`ROADMAP.md` 的 `TRAIN-DISTRIBUTED-TRAINING` / Ch36 将训练语义、collective 与物理 topology 作为共同设计问题。现有 [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) 开头及去中心化段已区分固定连通 mixing、local drift、压缩/通信与 checkpoint lineage；它没有把“必须对称 gossip 图”写成普遍前提，也没有用无线 collision-free slots 推导 GPU fabric 排名。若准入，可能是 `2+1+2=5` 的仅报告，或极窄条件的 Existing，而非自动新增 Books。这里的实质判断是：无线 broadcast 下的有向 mixing + 图参数成本界，是否足以改变本书分布式训练读者的受限设计选择，还是只是一类域内优化、缺乏本项目主线的直接桥。不能以“不是 LLM”单独关闭，也不能以 Ch36 提到 topology 就自动保留。

root 在独立消息中确认其实际打开 exact-v1 摘要/§1.2 与 Ch36:65–81，并以 Table 1 同成本代理比较核准：旧前闭理由不成立，按无线 broadcast 冲突时隙下的有向 mixing 和拓扑/收敛联合设计，`2+1+2=5`、Standard、Only；不得外推 GPU fabric、LLM 集群或端到端 SLO。作者随后复核 §2.3–2.4、§4.4、§6.1–6.2 的假设、成本和反证，独立准入与作者必要证据共同支持正式处置。具名 first-public 的官方公告/OAI/边界联合链见[日期记录](./V3_DATE_RECONCILIATION.md)；v1 页眉 Apr16 提交值不作公开证据。正式统计同步后为 88 候选、39 潜在、22 前闭、1 日期隔离；整日来源和分母 Gate 仍未通过。
