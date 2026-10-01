# 2604.25591v1 音频模型不确定性：按任务构念重选 sensor

04/29 作者侧单篇必要审阅；不是非作者证据、日期或整日 Gate。[官方 exact-v1 身份/题摘](https://arxiv.org/abs/2604.25591v1)和[官方 exact-v1 HTML](https://arxiv.org/html/2604.25591v1) §III–V、Tables I–IV、§VIII 是本项来源。身份处的 `submitted=2026-04-28T12:56:22Z` 仅为提交字段；已存的官方公告/邻 ID 窄链支持该 v1 所属 04/29 08 北京公告批，单家族更早首发例外与最终日期仍待独立 Gate。

先区分实验对象。§III-B 以 temperature 0.1 得最终答案 `ŷ`，另以 temperature 1.0 抽 K=10 回答估算 entropy/semantic entropy；P(True) 则要求同一模型对 `ŷ` 做二元自我验证，**不是外部音频事实裁判**。§IV 把 AUROC（正确/错误排序）与 AURAC（逐步拒掉高不确定样本后的平均准确率）分开，均不能直接当某个部署阈值的错误概率。模型仅 Qwen2.5-Omni-3B/7B 和 Audio Flamingo 3，单 RTX3090；主要任务答案空间受约束，§VIII 明说开放音频对话/描述未证，五种 sensor 也都沿用文本路径，未直接测音频感知内部歧义。

这篇的具体增量是**同一音频输入模态、同一模型，换可靠性任务构念时 sensor 排名反转**，不只是“多模态也要校准”。Table I 的 MMAU/Qwen2.5-Omni-7B：discrete semantic entropy AUROC .85、P(True) .82、normalized entropy .69；Table II 的 unanswerable AQUA／同一 7B：P(True) .79、discrete semantic entropy .70、normalized .62。AQUA／3B 又是 normalized .75、P(True) .52；Hallucination／Audio Flamingo 3 的 normalized .78、semantic .75、P(True) .44。这些都在作者的受限 benchmark 协议内，说明从一般音频 reasoning 上选定的“最佳 sensor”不能直接迁给 unanswerability/hallucination，更不能在不同模型共用阈值。感知与 reasoning 子任务也应保切片，但不从几项 AUROC 推一条普遍算法优劣。

§V-D 的 adaptive inference 只是固定阈值 .25 后走 caption-then-reason 的探索分支。Table IV 在 MMAR 上三个模型的 adaptive 准确率 `.58/.57/.53` 均低于各自 direct `.59/.58/.56`；作者仅报告相对 full reasoning 的 24–64% **token** 成本，不是 wall-clock 或部署价格，不能说不确定性路由必改善答案。该论文的 signal 有诊断价值而无直接放行 authority。

真实唯一 owner 是 [Ch66 EvalSpec／Calibration Slice](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：约 1580–1630 已将 semantic entropy/NLI sensor identity、claim type/domain×model scale×estimator access contract、独立标签校准与 abstain/action policy 分开；[Ch23 模态表示](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)只是输入表示邻接，不拥有阈值。上述 same-model rank reversal 是 Ch66 已有原则的一个可迁移音频**反证实例**，不是新 sensor 算法或非同义 Books 缺口。作者侧拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5/9`，Standard、`Report Only`；保潜在工作线索，待非作者准入/单篇有限核与日期 Gate。若同行认为 Ch66 当前命题已把此分层反例说尽、连 Report 新增证据也无，请具体指出覆盖段再裁前闭；不要仅以音频领域或方法来自文本为由机械拒绝。本项在旧 106 题摘外加有界反查批次时已计潜在，不因审阅重复加数。
