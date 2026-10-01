# 04/23 `2604.20209v1` 有界证据与 Books 差异

作者：root；2026-09-28。只处理已在本日完整题摘准入池中的 *Scaling Self-Play with Self-Guidance*，不据此签整日 Gate。原始正文为 [arXiv exact-v1](https://arxiv.org/html/2604.20209v1)；实际复读 §3、§4.1–4.5、§5 与 Appendix 中本命题相关的算法/对照。当前网页另有 v2，本文不借其结果或文字回填 v1。v1 submitted `2026-04-22T05:50:23Z` 不是公开时刻；DataCite v1 Updated `04-23T00:29:45Z`、DOI created `02:00:05Z` 与正常周三 20:00 ET 公告槽相容，但注册晚于本窗终点不排除较早公告。当前 OAI header `08-12` 已由 v2 覆盖，不用它定 v1 日期。暂以 `04/23 08:00～09:00+08` 有界批次推断待日级复核，非逐篇日志。

## 需要保留的命题及边界

旧的自博弈只依据 Solver 对合成题的通过率奖励 Conjecturer，在短程可产生难度适中的新练习；长程可能把“难题”推成形式冗长或不服务未解目标的题，甚至让 Solver 的低熵状态使通过率集中在 0/1，Conjecturer 再拿不到区分性反馈。本文将未解目标 `x` 作为生成条件，对每个生成题 `x̃` 同时计算可验证通过率与冻结 Guide 对目标相关性/表述质量的评分；Conjecturer 的奖励为两者的乘积，Solver 仍由 Lean4 verifier 的二元结果更新。proposal、质量代理、verifier 与两个 policy update 因而分权，而不是让 Guide 裁判证明正确。

[§4.4](https://arxiv.org/html/2604.20209v1#S4.SS4) 的 No Guide/No Target Conditioning/Frozen Conjecturer 消融分别显示作者所测长期训练中表述退化、目标学习无进展、合成题分布被学完；[§4.5](https://arxiv.org/html/2604.20209v1#S4.SS5) 的 CISPO 条件出现 Solver entropy collapse、合成题通过率趋向 0/1，作者采用的 `REINFORCE^{1/2}` 条件保留较多区分信号。这里不是证明 CISPO 或所有组相对目标不适合自博弈，也不是 Guide 已学到因果有用性：它是同一模型家族衍生的冻结评分器，rubric 经长程人工观察与 2048 条 SFT 格式样本调过，可能共享偏差。正式验证器只检查 Lean4 证明，不检查合成题是否是通往目标的真正必要步骤。

实验在约 3,323 个经过 GPT-5-mini 排错筛选的 Lean4 目标上，8 proofs/problem/round，DeepSeek-Prover-V2-7B 初始化三个角色；图 4、6 的长程比较比短程最终点更有信息，但“渐近求解率”是有界训练曲线的 sigmoid 拟合，非无限计算实测。与 671B pass@4 的展示不等同算力、模型、推理预算或训练成本。正式数学以外的 environment/reward 生成、Guide 学习、不同模型规模皆是 §5 的未来工作。不能把该结果推广为开放自然语言/Agent 自博弈保证或生产训练效率。

## 与现有章节比较及拟处置

`TRAIN-GRPO` [Ch33](../../../../../books/part-04-training-system/33-grpo.md) 的自博弈段已区分 `curriculum/proposal owner != solver/update owner != verifier`，并提到 role collusion/self-confirmation；其前文已有 entropy、0/1 组与 reward 信息量。尚未把**目标相关性 Guide 与可验证难度奖励如何在长程互相制约，以及 Solver 熵坍塌会反向饿死 Conjecturer**接成同一反馈链。这是现有主线中的窄机制缺口，不是新增框架清单。

工作拟评分 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，标准审阅；因可能补足长期训练稳定性机制，按真实 Books gap 深入核必要反证。拟在 Ch33 现有自博弈段后仅加一条演进分支：旧通过率奖励合理→长程难度投机/反馈饥饿→目标条件与独立质量代理→冻结代理偏差、verifier/熵/成本门槛和旧路径共存。**此处尚未写 Books，也未计实际 Integration。** 请非作者先复核 source→owner/日期边界，再决定是否窄写；正式日报分母与整日 Gate 仍未冻结。

## 2026-09-30 有限非作者裁决（仅本家族）

复核者：`sep30_complement_review`，与上述作者 root 分开。独立窗口为 `2026-04-22T09:00:00+08:00`～`2026-04-23T09:00:00+08:00`。已重读当前 AGENTS、研究/Report 合同、每日来源使用与主题段、统一 Prompt、ROADMAP 和本日最新 checkpoint；仅实际打开 [exact-v1 题摘/正文](https://arxiv.org/html/2604.20209v1)、[v1 身份页](https://arxiv.org/abs/2604.20209v1)及[官方公告规则](https://info.arxiv.org/help/availability.html)，对读 Ch33 相关正文，不恢复全日来源或后续家族。

**准入与 owner 有限通过；日期采用暂不通过。** 原通过率奖励能提供可学习难度，但长程可能奖励形式投机；v1 增加目标条件、冻结 Guide 质量代理和 Solver 熵→通过率分布→Conjecturer 奖励饥饿的相互约束，改变的是同一训练反馈环的设计选择，而非只因 Lean 场景指标提高。工作命题评分仍为 `Design Delta 2 + System Reach 1 + Durability 2 = 5`：重要局部机制/边界、单一自博弈训练环、可复用约束。证据质量和能联想到多个角色不计入 Reach。最低标准审阅之外，因下述具体知识缺口，已深入必要方法、消融和反证；不为拟改书升分。日期未定前不将该工作评分写入正式本窗候选表。

### 实际原文核验及采用修正

- §3/Algorithm 1、Appendix G.2/G.5：只为未解目标生成 synthetic problem；难度奖励排除零通过率和批内最高 30%，余下取 `1-s`，再乘 Guide 分数并按批归一化更新 Conjecturer。Solver 的主要目标仅更新通过率不超过 0.5 的题中的正确轨迹；§4.1 另有过长惩罚和 `try` tactic 的零奖规则。“verifier 拥有正确性”不能改写为全部训练奖励只有未经 shaping 的二元值。
- §4.4/Figure 6 与 Appendix C/Table 1 要修正上文“分别显示”的归因理解：**No Problem Conditioning 同时移除目标条件和 Guide**，不是只移除目标条件的单因素实验；**Frozen Conjecturer 配置也没有 Guide**，相对完整 SGS 的差值不能全归于冻结。No Guide 相对 SGS 的控制较直接，支持作者设置下的质量代理作用，且 No Guide 本身仍高于 RL baseline，不应写成没有 Guide 就完全无法学习。
- §4.5/Figure 7、Appendix C/G：所测 CISPO Solver 条件下的低熵、通过率两端集中、Conjecturer 零奖励链可采用为受限失效路径；更换目标也改变更新/采样权重，不是保持一切不变的 entropy 因果干预，更不能推广为所有组相对目标必然失效。§5 明确保留其他熵管理方法的可能性。
- §4.1/Appendix E.3/§5：Guide 同模型来源、格式 SFT 和长程人工 rubric 调整不能证明独立、因果正确的 useful-subproblem oracle；“独立质量代理”只能指职责与更新路径分离，不指统计独立。§4.2/Appendix A 的拟合不等无限计算实测，也不等重复训练 seed 的不确定性；固定训练目标上的累计解题率不是 held-out 泛化保证。Appendix B 的 bf16/8192 tokens、异构生成/CPU 验证及 H200 训练、§4.1 的 3,323 目标和每题八次尝试限定证据，generation 计数不等全部训练/Guide/验证成本。没有复现或生产吞吐认证。

### 具体 Books 差异与日期停点

`TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md) 约 L1351–1355 的自博弈段已承载 proposal/solver/verifier 分责与串谋风险；约 L395–405 的 DAPO 段已解释 entropy collapse 和全对/全错组，约 L1842 后解释 pass-rate controller。它们尚未接成“Solver 分布两端化反向饿死任务生成器，同时质量代理防止难度奖励投机”的共同反馈链。支持作者提出的**窄缺口**，而非重复分责原则或新增框架介绍；拟写时须带上述混合消融限制、代理共偏差、熵/成本门槛和固定题库回退。此轮不写 Books、不计实际整合，也不验收尚未发生的写后。

身份页实际确认 v1 submitted `2026-04-22T05:50:23Z`、v2 为 08/11，未见当前页面撤回/纠错标签；不借 v2 回填。官方正常日程换算支持周三公告→04/23 08:00 北京的条件推断，但也允许延期。上文 DataCite 原字段和已被修订覆盖的 OAI 记录只是作者保留的元数据证据，本轮没有把它们重命名为公开时钟或声称已独立重抓。因此 `04/23 08:00～09:00+08` 目前仍是**待确认的公告槽**，不据此确认首公开完整落窗；暂不进入正式本窗分母、不采用 Books。下一步只定点恢复本 ID 的当期官方公告身份/日志或可信原始全文首次公开记录，再核是否存在窗前正文，不能扩成全站日期考古。此日期核仍是后续具体工作，本轮未尝试所有替代入口，不称已穷尽或外部 blocked。

本次唯一历史 checkpoint 到此停止。有限 source→owner 结论不计 04/23 整日完成，不更新月度完成数。仅署名追加本文件，保留作者原文；未改 Books/正式 Report/索引，未 stage、commit、push。
