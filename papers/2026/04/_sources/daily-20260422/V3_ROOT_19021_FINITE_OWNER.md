# FG²-GDN `2604.19021v1` 有限非作者来源→owner 裁决

复核者 root，2026-09-28。核[官方 exact-v1](https://arxiv.org/html/2604.19021v1) §2.2–3.5/Eqs8–14、§4/Tables1–4，当前 Ch22 的 GDN→状态写入几何→GDN-2 相邻论证，以及 ROADMAP 的 `MODEL-LONG-CONTEXT` owner。仅针对本 Source Family，不代替 04/22 整日 Gate或复现实验。

**裁决：有限 Integrate / Ch22 写前 PASS。** 现有 Ch22 已说明统一 scalar decay/update、GDN-2 的 channel-wise decay 与 erase/write 分权，却没有讲清“让 `β` 从标量变为 channel vector，何以在训练 chunk algebra 下仍可行”的中间约束。可在当前 GDN 后补短机制桥：天真左乘 `Diag(β)kkᵀ` **仍是 rank-one**，但不再是原对称 `uuᵀ` generalized-Householder 形式；以 `sqrt(β)` 同时缩放 key/write value，使 transition 保持原形式可复用既有 WY/chunk lowering。再说明 `β^k/β^v` 分离 erasure/write 与后文 GDN-2 的语义相邻，不写成后者必由前者演进，也不把论文类比 Adam 误写成实际用了 Adam 的二阶状态。

受限证据：作者 340M/1.3B、15B/100B token、8K train length 与 SlimPajama/有限任务；1.3B Table4 的 vector-β alone LongBench 16.0 低于 KDA 16.4，FG+ LM avg 53.4 低于 plain FG 54.0。H800-80G BF16 的 prefill 图、固定 32,768 token budget 与特定 batch/length 只支持局部执行成本，不能推出任意部署 throughput/tail SLO；hybrid 比例和 Table1/4 的列/均值口径要保留差异，避免把所有指标组成单一“全胜”。旧 scalar gate/KDA 在实现简单、具体任务或已有 kernel 优先时继续成立。

写入后仍需独立实际正文与相邻交接复核，方可将对应 Daily 的 Books Decision 标记已落实。
