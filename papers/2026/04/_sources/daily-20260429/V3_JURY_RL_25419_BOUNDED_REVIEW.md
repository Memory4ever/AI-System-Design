# 2604.25419v1 JURY-RL：投票提案、证明门控与未证实回退的权限

- 官方首版：[JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR](https://arxiv.org/html/2604.25419v1) §3–5、Appendix A.2–A.3/B.1/C.3–C.4/G.4–G.5；本日 arXiv 窄公告批次支持 04/29 08:00 北京归属，单篇 early-public 例外与独立日级 Gate 仍未过。只读必要段、主表和反证，不读全附件/后稿、不复现实验。

## 原文机制与保留的受限实证

§4.1/Algorithm 1 每题取 `G=8` rollouts，按 `ans(y)` 的 plurality 只提出一个答案，Lean pipeline 判 `δ=1` 时仅给相同答案的 rollout 正奖励；`δ=0` 时不强化未验证 plurality，而用 ResZero 维持组内相对优势。这个**proposal 与 reward authority 分离**是真实增量；但 Lean 的 soundness 只保证被形式化的 Lean statement，不能自动证明自然语言题目/答案被无误翻译。

§4.2 Eq6 在未证实分支给 `r_i=α·1[i∈R]·(z_i−ū)−cα·1[i∈M]+γ`，`γ=cα²` 使组和为零。Appendix A.2 的单 dissent 例子明确：`|R|=1` 时该 dissent 得 `cα²>0`，多数各得 `cα(α−1)<0`。故 **即使未证明任何答案，仍可能给另一个错误答案正 reward/advantage**；这是探索代理，不是 verified truth。组均值在 GRPO Eq2 本来就被减掉，整体加同一 `γ` 不改变标准化后 advantage；零均值不是独立的跨 optimizer 稳定性定理。全同答案时 residual 为空且奖励全零，不能声称每个 inconclusive group 都有非零梯度。

受限实证：Table 1 三 backbone 的 label-free 比较可保，但 Qwen3-1.7B 的 JURY 平均 `35.40` 低于 GT `35.56`，不能说各模型均胜有标签 oracle；math 训练后的 code/instruction 分数不是这些任务中也有 Lean 正确性。Appendix G.4 在一条 Qwen2.5-7B/G8 run 中，proof-gated 步比例 `53.0→70.7%`，错误 plurality 但存在正确 minority 的组仍 `7.6→5.4%`、中途 `9.3%`；只验证 top1 会错过这些候选。Appendix C.4 的 128题/步冷启成本：GT 约100s，Lean 增约200s 为300s，judge 增约80s 为180s；缓存使后期趋近 GT 是作者机制解释，本核未见同运行完整命中率/端到端成本曲线，不把它写成已证生产零开销。

## 中央保证的窄隔离

作者 §1/§4.1 等把系统称为“只为可证明正确发正 reward”及 truth-aligned。该说法若仅指 **`δ=1` 分支**，可成立，但不适用于含 ResZero 的完整训练。Appendix C.3 的 consistency checker 在 MATH500 precision `87.7%`、两 held-out 数据 `80.1%/82.1%`；Appendix G.5 又直接报告整体 Lean verification signal precision 约 `85%`，解释为上游 autoformalization/semantic checks 的缺陷。§H 所称“一旦通过 autoformalization 和 consistency checks，Lean proof 有零 false positives”只能限定为**形式命题**，不能据此写成自然语言任务零假阳性。隔离的是印刷的整条 reward truth 保证，不是否定 Lean kernel soundness、受限训练曲线、或断言代码已出错。

## 实际 Books owner 与作者提案

已对读 [Ch33 GRPO](../../../../../books/part-04-training-system/33-grpo.md)约 399–430 的零优势组/补样、约 453–500 的 verifier 是 specification／group error 相关与独立真值、约 850–860 的 selector/teacher 与 outcome authority。现章说明外部 verifier 拥有 correctness、group 多样性与零方差，但尚无“未标注 plurality 只作一次形式验证 proposal；若拒证，继续训练的残余奖励必须标成 exploration proxy 而非 proof”的具体分支。Ch33 为唯一 owner，Ch66 的 evaluator 校准是邻接，不新开第二 owner。

拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，因中央理论/训练安全保证存在印刷边界冲突而做 **窄 Deep 纠错**；Books 拟最小 Integrate，但须非作者 source→actual-owner 审与共享 Ch33 写锁，真实写后再审。建议插在 Ch33 Verifiable Reward 前后：

> 无标签多数票可便宜地产生候选，但不能签奖励真值。在可形式核的任务中，可先冻结 rollout group/答案抽取/投票策略，仅对 plurality 候选做一次形式证明；证明成功时才给匹配 rollout verified outcome reward。拒证也可能是形式化或搜索失败，不是该答案已证伪，更不能把其他少数答案自动当正确。若仍要更新，可给 residual 一个居中、受限的探索信号，并在状态中标 `unverified-proxy`，与 proof-backed reward、零信号 fallback 和未来的更高预算补证分账。
>
 这节省逐个候选证明但会漏掉正确 minority，并把 autoformalizer/semantic checker 的错译带进 proof gate；ResZero 的正分量不是“只奖励已证明正确”。预算或形式化保真不足时，应回退可信答案标注、确定性 task verifier、增加证明候选或暂停该组更新，而不是让 cache hit/多数一致性获得 truth authority。受限三模型数学训练及有限迁移不支持开放任务、零 false-positive reward 或无额外训练成本。

本篇原在 106 份完整题摘的潜在工作池，不改 `64+41+1` 或冻结正式候选；上述仅作者侧普通工作，非单篇独立/Books/日期/整日 Gate。
