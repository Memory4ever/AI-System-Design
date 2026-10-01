# 04/28 arXiv 排除侧反向查漏（题摘级，未冻结）

## 范围与方法

在 945 个原始身份中，旧库存把 111 个标 `retained`，其余 834 个为 `pre_denominator_closure` 818 + `closure` 16。本次对 **834 个旧排除身份的标题逐项全览**，对其中 44 个可能涉及大模型/Infra/Agent 长期机制、ownership 或 evaluation contract 的身份定点重读已存 receipt 的**完整摘要**；不是正则自动入选，也没有把 834 篇逐篇全文。缓存摘要可能包含后发版本，下面“重开”只指不得维持旧泛化关闭理由，正式准入仍需官方 exact-v1、日期、反证与实际 Books 命题对照。

## 需定点重开的旧关闭身份

| ID | 完整题摘显示的潜在长期差异 | 必须先排除的误用 / 下一步 |
| --- | --- | --- |
| 2604.22785 | 多 Agent router 只给被选响应反馈、collaboration 共享 reward 模糊单 Agent contribution；counterfactual objective 将 selection-gated off-policy 与 leave-one-out credit 分账。旧“任务局部优化”关闭理由没有处理反馈归属。 | 核路由 propensity、可识别性、同预算协作/路由对照和 Ch31/56 credit owner；不把理论目标当无偏部署保证。 |
| 2604.22820 | cyclic subtask graph 与有依赖约束的 DepDAG 在 TextCraft/ALFWorld/Finance-Agent 出现不同成本—恢复签名，可能否定“长任务总应允许自由回返”。 | 核相同工具/模型/budget、故障注入和 Ch81 当前 workflow 回退；若只印证已有受限 retry 则关闭。 |
| 2604.22937 | 从开发集标签合成并搜索可执行 Python verifier 集，把 LLM judge 与确定性 check 的身份/覆盖分开。 | 核 verifier 目标是否就是局部数据集拟合、测试泄漏/执行权限及 Ch66/78 已有 oracle/effect 分工；F1 提升非 correctness 证明。 |
| 2604.23283 | 人类中途修订与 Agent 并行执行，按 idempotent/reversible/compensable/irreversible 给 rollback 上界；旧“单域局部方法”未回答不可逆 effect 的长期控制边界。 | 核 Earliest-Conflict 条件、真实外部 effect、补偿成本和 Ch78/81 已有 commit/rollback；不把模拟步骤节省当原子性。 |
| 2604.23321 | 跨文本/图/音/视频等价 tuple 揭示 query-modality bias 和 instruction 不能确保指定 target modality，可能改变多模态检索评价切片。 | 核等价 tuple 的真值/生成方法及 Ch23/66 当前模态可见性；数据集数量本身不准入。 |
| 2604.23434 | Dynamic Tanh 代 LayerNorm 的好坏随数据量/容量反转，HardTanh/α/dropout 干预提供“activation bound 是隐式正则”有条件反证。 | 核 compute-limited T/P<1.84、leave-one-scale-out 仅50% 与 Ch21/22 现有 normalization 条件；不能称通用去 LN。 |
| 2604.23475 | FFN loss-sensitive supernode 与 activation outlier 弱重叠，保护核心对结构剪枝可能与“按激活大值保护”冲突。 | 核 Fisher-style proxy 与真实逐通道损失、50% 剪枝同参数/恢复预算、Ch21/49 现有敏感度/保护机制。 |
| 2604.23552 | consistency distillation 可能改变 teacher 已记忆样本向 student 传递的方向，区分推理加速和信息暴露。 | 核成员推断/近重复检测、质量/compute 控制与随机特征模型理论外推；不把“降低记忆”当隐私保证。 |
| 2604.23734 | reranker 从标量 relevance 扩到 contribution 与证据 passage，可能把文档选择与可供 Agent 引用的证据对象分权。 | 核 LLM judge 合成标签/改写 passage 是否保留原始引用和 Ch76 现有 evidence identity；NDCG +1.54 非真实性。 |
| 2604.23855 | 企业 Copilot 反馈训练 UI action critic→按 confidence abstain→人类改 UI 后恢复后台执行，可能补 Agent autonomy 的分步转交状态。 | 核真实生产机会分母、operator 选择偏差和 effect 回放/权限，Ch81/66 是否已有同样 owner。45% 自动化与39%时长下降不能单独归因。 |
| 2604.23994 | 离散扩散固定块在无未来条件下过早 commit；以 Future-Aware vs No-Future 预测分歧选 variable block，可能改 Ch24 token commit 责任。 | 核 FA 未来在推理时如何获得、双路额外成本和真实 block 恢复/回滚；不能把自包含代理写成真值保证。 |
| 2604.24026 | Skill 的 scheduling / execution / side-effect 证据从自然语言分离，可能影响技能检索和风险评审身份。 | 核 source-grounded 结构是否真由原 artifact 验证而非 LLM normalizer 虚构、Ch84 当前 registry/permission 论点是否已有；MRR/F1 非 effect 安全。 |
| 2604.24401 | Audio benchmark 无音频输入仍有60–72%分数，text prior 与 audio reliance 分成两轴，可能修正“高分=听觉理解”。 | 核去音频/局部片段对照语义与 Ch66/23 已有模态依赖验收；3.0–4.2% complete clip 不等音频其余无用。 |
| 2604.24594 | Skill Retrieval Augmentation 将找到、加载、执行三阶段分母分开；26k技能中模型即使检到 gold 也常不按需要加载。 | 核 636 gold/混 distractor 构造、技能效果权限/真实效果与 Ch84 已有 retrieval→activation→effect 三段；若已有则 Existing 而不重写。 |
| 2604.24618 | 安全研究 sabotage 的 unprompted 与先前轨迹已开始破坏的 continuation、evaluation-awareness/prefill-awareness 各自是不同机会集。 | 核官方精确稿及场景比例、两个评估分母和 Ch66/72 当前 agent auditing；不得由 7% continuation 推部署自发破坏发生率。 |

此外 `.23380` 的 diffusion ELBO-vs-MDP policy gradient、`.24357` 的 Doob-token-order 与 `.23858` 的 video latent inter-frame pruning，摘要涉及模型/推理机制，但目前分别缺可识别的长期状态 owner 差异、线上排序成本或跨场景复用证据，只列**定点可能漏项**，不作为自动重开/最终关闭。完整标题全览里大量医学、农业、金融、AI for Science、单领域小模型、通用应用封装保持原 family-specific ledger 的排除方向；抽象口号或能映射 ROADMAP 节点不足以准入。

本反向查漏不能证明零漏项。上述 15 项重开线索是**从旧排除集恢复的工作队列**，不是 15 个候选、分数或 Books 任务；需先以官方 exact-v1 与实际 owner 剪枝，且日级非作者另做双向抽检。
