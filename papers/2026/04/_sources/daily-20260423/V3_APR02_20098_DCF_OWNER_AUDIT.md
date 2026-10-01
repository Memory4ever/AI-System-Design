# 2604.20098v1 DCF：有限非作者 Source→Owner 审核

范围：仅核 [官方 exact-v1](https://arxiv.org/html/2604.20098v1) §2.2–3.6、§4.1–4.3 与 Limitations，以及当前 `books/part-06-ai-infrastructure/66-evaluation-system.md` 中 claim graph、claim calibration 与 conformal release 条件的实际正文。未遍历附件、未复现实验，也未核本日报的日期、全部来源或其他候选；本记录不是日级 Gate 或 Books 实际写后通过。

## 写前结论：窄幅 Integrate 提案成立

Ch66 现已明确 typed claim graph 的依赖、按 claim/结论区分的 estimand、按 deployment slice 用真实标签校准 scorer、exchangeability 失效回退；这些一般原则不能算缺失，也不能把 DCF 的整套算法写成首次引入 claim graph。实际尚缺的选择是：当图上祖先闭包与 conformal 阈值/最大可保留子图是离散且耦合的，训练 scorer 时可按**筛选→祖先闭包→校准分位数→预测选择**的顺序建立可微代理；发布/推理时仍用原始 hard CF 算法和独立 held-out calibration，而不是把 soft membership 当有保证的最终判定。由此把“训练目标可导”与“部署保证的所有者”分开；这是真实的长期 Evaluation scorer 设计分支，非只因论文提到 conformal 而增加方法摘要。

原文依据：§3.1 将 threshold filtering、ancestor coherence、argmax 列为耦合离散步骤；§3.2 Eq1–2 用 sigmoid 与祖先加权几何均值近似；§3.3 Eq3–6 对假 claim 形成 soft violation/supremum 和 soft quantile；§3.4 Eq7–8 是带阈值 gate 的 soft prediction；§3.5 在训练中分离 calibration/prediction 子集并回传到 scorer。Theorem 3.1/3.2 只论温度按规定顺序取极限恢复 hard CF，不能证明任意有限温度或有限训练自动保持 coverage。§4.1.3 明言测试时部署原始 hard CF；测试保证依赖独立校准及 exchangeability，不属于所学 scorer 单独的性质。当前 Ch66 的 claim graph 段（约1460起）、Atomic Claim/Raw Score 校准段（约1609–1745）与 conformal/coverage 段（约3017起）可承接这条分支；建议唯一 canonical owner 为 `PLATFORM-EVALUATION-SYSTEM` / Ch66，在“Raw Score 只有经过标签校准才是概率”的 scorer/calibrator 段后、answer-level 结论合成前，插入两个短段落，不新建章节。

关键反证与采用边界：§4.1.2 仅 MATH 202题与 FELM 710题，MATH claim/依赖边人工双标，FELM 图较浅；§4.1.3 为20-fold、70/15/15训练/验证/测试且训练内部再分 calibration/prediction。§4.1.5 的 coverage 是保留 claims 形成 coherent factual graph 的样本比例，retention 是平均保留 claim 数，不能直接解释成“每条 claim 正确概率”或线上用户效用。Limitations 指 α≤0.02 的 MATH、α=0.01 的 FELM 会拒绝全部 claims，FELM中频率已较有判别力时相对收益下降。保证为所述交换性条件下的边际统计性质，不保证单条 claim、所有子群、图依赖边是真值、分布漂移后的持续覆盖或生产 SLO。标题/摘要的 retention 百分比不应独立于这些分母和零保留条件进入 Books。

## 实际写后非作者复核：PASS

root 已将两段落在 Ch66 现有 claim scorer/calibrator 段后、候选空间/answer-level 合成段前（当前约1731–1733行），并在该章 Review notes 保留 `SF-2026-ARXIV-2604-20098`。本审阅者重新对照上述官方 exact-v1 §3.1–3.5、§4.1.2–4.1.5、Limitations，顺读新段两侧：正文将图上阈值筛选、祖先闭包、校准分位数、子图选择按原顺序交给训练期可微代理；把部署时 hard CF 与独立标注集校准交还 Evaluation owner。它没有把有限温度代理误写为覆盖定理，也没有将 coherent graph 的边际 coverage 改名为逐 claim 概率或单次答案保证。MATH/FELM、有用 claim 保留、低 α 零保留、频率强时小收益、图标注/交换性/漂移回退均在邻近正文或 Review note，且与后文 answer-level 估计/候选空间条件连贯。该窄写入不把作者百分比当生产收益。`git diff --check -- books/part-06-ai-infrastructure/66-evaluation-system.md` 本次实际通过。

故 2604.20098v1 的 Ch66 实际写后独立 PASS；未复现实验，也不代表 Apr23 来源、日期、分母或整日报 Gate 已通过。
