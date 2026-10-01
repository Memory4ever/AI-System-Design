# 2604.24957v1 CAT：算子对齐训练的有界证据与 Ch33 命题

状态：04/29 V3 作者侧必要证据；待非作者核首公开例外、数学冲突及 Books 判断。此记录不是日级 Gate，也不授权共享 Books 写入。

## 身份、日期与贡献

- [官方 exact-v1](https://arxiv.org/html/2604.24957v1)题名 *Compute Aligned Training: Optimizing for Test Time Inference*；[v1 身份页](https://arxiv.org/abs/2604.24957v1)保留 `[v1] 2026-04-27 19:52:38 UTC` 原 submitted 字段。它位于本日 checkpoint 所记官方 04/29 08:00 北京公告窄 ID 批内；submitted 不是首公开的单独证明，若有更早的独立正式公开须按家族重判。HTML-v1 正文顶部另印 `August 24, 2026`，与 v1 身份页及已有 v2 2026-05-19 版本历史不能同作公开日期，隔离为稿内日期矛盾，不从它反推事件时刻。
- 准入命题：单输出 SFT/RL 可与部署时 Pass@N、majority vote 或 Best-of-N 的选择目标错配。相比已有 Pass@N/DCO 局部目标，原文 §2 给出把测试时算子写成 `T(π,φ)`、从有效分布的目标梯度导出候选权重的统一形式，并试图延伸至 SFT 与 RL。若这个条件机制成立，训练应按预定测试时聚合策略、预算及当前候选分布重配更新权重，而不是把单样本 reward/likelihood 提升当作唯一目标。这是贡献候选，不是仅因题名映射 Ch33 而留。

## 已读必要原文及反证

- §2.1 Eq(1)–(7)：SFT 真梯度需整输出空间 Jacobian，实际标量化要求 off-diagonal 可忽略或有界；Pass@N 的正确答案二值存在概率是可解析特例。Majority vote 的胜出概率依赖竞争答案分布，§2.1 把 `k` 固定成阈值近似；SFT 实作又在 Appendix A.5 以一条金标准 CoT trace 的 likelihood 代替正确最终答案的边际概率。故不能把所有算子写成精确、零额外成本或对任意搜索策略可得的训练目标。
- §3.1 Tables 2–3 的 MATH 切片：Pass@64 训练在测试 @64 为 `67.6%` 对 SFT `59.8%`，但 @1 为 `13.5%` 对 `15.8%`；多数投票 N=64 模型在测试 @4 为 `22.7%`，低于 SFT `22.9%`，其 @1 `21.4%` 亦低于 `21.9%`。不能把作者正文“all models show improved performance when TTS applied”外推每预算严格提高。Table 3 多数投票 N=16 的 @64 为 `26.2%` 对 SFT `23.9%`，标准误分别 2.0 与 1.9 个百分点，不作无 CI 的显著性声明。
- §3.2 Tables 4–5 是一次短 SFT warmup 后一轮 strategy-aligned GRPO 的 MATH 实验：Pass@16 在测试 @32 为 `40.0%` 对 standard `35.8%`，但 @1 均约 `8.3%`；Maj@4 在测试 @16 为 `23.0%` 对 `19.2%`，而 @1 为 `10.9%` 对 `11.1%`。只说明此模型/任务/预算下的 trade-off；不能说单次准确率无损、部署成本不变或所有 controller 都有效。
- §3.3 蛋白任务是作者自定 hydrophobicity reward 的 ProtGPT2 模拟优化；它可作为非语言算子形态的例子，AI for Science 领域任务本身不恢复本项目阶段范围，也不证明真实蛋白功能、湿实验或普遍 Best-of-N 优越。Table 6 条件任务 BoN-2 的 N=1 为 `5.36`、standard `7.26`，N=8 则 `9.48` 对 `8.31`，明确有单样本 search tax。§4 自承认梯度方差膨胀、竞争答案依赖与更复杂多步搜索不能直接用该标量化。
- 两处**印刷层有限争议**需非作者定点核，不能据此推代码实际使用错误公式：§2.1 Eq(7)/Appendix A.3 Eq(16) 的 SFT majority 权重为 `k·Binom(N,k)·p^k(1-p)^(N-k) / Pr(count≥k)`，但 Table 1 同栏只印 `Binom(N,k)·p^k(1-p)^(N-k)`；若不是另行说明的不同量，两者不等。Best-of-N Appendix B.2 Eq(55)–(57) 的 `N·P_<^(N-1)`需要在增加 `p(y)` 时从较差答案移走同量概率、令 `P_≤` 固定，而 Appendix B.3 Eq(60) 又给独立 partial `N·P_≤^(N-1)`；这两个导数是在不同扰动路径下，不能无说明互换。B.3 在同一论证的 Eq(63) 后先称 diagonal 是 safe underestimate/fail-safe descent，随后的 Uncompetitiveness 段却称它 overestimates true gradient 且建议降学习率。只隔离“统一近似必然安全下降／精确梯度系数”强保证，不吞掉 Pass@N 的解析特例和受限实验。

## 真实 owner、最小处置提案

- [ROADMAP](../../../../../ROADMAP.md) 的 `TRAIN-GRPO` 属 [Ch33](../../../../../books/part-04-training-system/33-grpo.md)。现有 Ch33 `训练目标必须包含部署时 Inference Controller` 明确要求在 rollout 中**实际运行** reranker/verifier/search/sampling controller 后，对模型+controller 的最终行为训练，并保留 revision/预算、controller-free slice 与回退。这已持有一般的训练/部署错配合同。CAT 的非同义点是：对预先可解析的聚合算子，尝试不完整执行目标算子/不遍历所有输出就用边际效用重配梯度；预算 N、阈值 k 与竞争答案分布/近似必须成为训练目标身份。它不是所有 controller-aware GRPO 的替代，更不能凭局部 MATH 与蛋白表格替代真实 rollout 的正确性验证。
- 作者侧拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9`、标准审阅；印刷中央保证冲突触发**受影响公式有限 Deep**。当前处置拟 `Disputed`，仅隔离上段印刷统一近似/安全下降主张，保留有条件的算子权重机制及表内受限结果。Ch33 可能有最窄 Books gap：在现有“实际运行 Controller”段之后，区分「controller 可重放时直接 rollout」与「算子可解析时用边际权重近似」两种训练路径，写明精确/近似边界、目标预算版本、single-shot/coverage/mode-retention 联验和近似失效回退；但在非作者 source→actual-owner 核和共享窄锁之前**不写 Books、不计 Integrate**。如非作者认定现有段已具体承载这一区分，则改 `No Change — Existing Coverage`，不是为论文名加注。

最小同行核：官方 exact-v1 §2.1 Eq(3)–(7)/Table 1、§3.1–3.2 Tables 2–5、Appendix A.3/A.5 与 B.2–B.3 的上述印刷冲突，Ch33 `训练目标必须包含部署时 Inference Controller` 与两侧交接；不需蛋白附件或其它版本全文。
