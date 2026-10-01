# 04/28 早段三项 exact-v1 必要贡献消歧

只核决定贡献准入所需的官方 v1 方法、关键反证和现有知识 owner；不等于首次公开归属、正式分母、评分、Books 采用或非作者 Gate。固定时间窗为 `[2026-04-27 09:00, 2026-04-28 09:00)` 北京时间。

| Family | 官方 v1 必要证据与限制 | 实际 owner 差异和作者侧暂定处置 |
| --- | --- | --- |
| `2604.22891v1` | [官方 v1](https://arxiv.org/html/2604.22891v1) §3.1–3.6、§4.4：两位 benchmark judge 为 20 模型×100 问题的响应评分，Spearman `ρ=.658`、同答评分绝对差均值 `.54`；`ε` 邻域构造“等质量”对子，另用高对比对子先验收 judge 区分能力，再按自身响应/第三方 null 对子的双顺序选择差定义 self-preference。人工 cluster 对刻意挑选的边界困难对子一致率 `79.8%`，不是全分布真值；结构化多维 rubric 只在四个高偏模型测试，平均 β 降 `31.5%`，不能推无偏或消除共享 judge 误差。 | Ch66:221 已明确 judge self-preference、position bias 与发布权分离，Ch66:1955 也列 bias；但目前未把**生成质量/高对比判别能力与同质量自偏好**分为三个实验对象，第三方 null 与顺序交换是具体评价合同。暂继续受限评价机制消歧，primary Ch66；若非作者核现有 Judge Audit 已含同分母控制，则降 Existing/Only。不得把两位 LLM judge 平均当无 gold 客观质量，也不按论文模型标签部署固定 judge。 |
| `2604.22985v1` | [官方 v1](https://arxiv.org/html/2604.22985v1) §3–4/Table 2–3：在 BFCL 的 Simple/Multiple/Parallel/Parallel-Multiple 与组合、irrelevance 切片比较 8 个模型。单次 greedy NLL 通常不弱于十次抽样 semantic entropy；AST 归并对十个设置中的八个有小幅 AUROC 提升，却仍不足以超过单次方法，且多采样成本约随样本数增。按函数名/参数等语义 token 计算分数有局部提升；但排除不可 AST 解析输出（组合中均值 `3.4%`），输出 correctness 是 AST-match 而非 effect correctness。§3.2 指出混合 AUROC 非各切片加权均值，单一 threshold 必须按实际任务混合验收。 | Ch66:944 已拥有 function-call schema/argument exact-match，Ch66:1916 已拥有 uncertainty sensor 的 slice 校准与 abstain；论文给**同一工具调用 gate 的任务混合分母、AST 表示与生成成本**一个受限实例，但现有长期验收原则已能承载，暂倾向标准 Only/已有原则的局部实证，不新增 Books。若非作者认为 AST-match 与真实 effect 分权或混合 AUROC 是尚缺的独立长期条款，再窄提 Ch66，不以“首个 benchmark”自动准入为强 Books gap。 |
| `2604.23046v1` | [官方 v1](https://arxiv.org/html/2604.23046v1) §3.3–4.2、§5：ONS 的状态 `A_t=λI+Σg_sg_sᵀ` 保存历史，作者在 `d=2` 线性凸在线任务、`T=400`、删除时 `τ=200`、20 seeds 比较参数轨迹、regret 与 state geometry；谱 reset/decay 会大改状态而外部 regret 未同步变化。图注又写到 `t=1000`，与 §4.1 `T=400` 不一致，不能把恢复时长数字当可复算事实；也没有 LLM 实际优化器、隐私攻击或从头重训参照。 | Ch72:2157–2171 已明确删除请求时只读 forget set **不等于**未用全训练数据、离线曲率 artifact 要绑定 checkpoint/data/阻尼，近似与永久删除须分账；本文用二维 ONS 说明同一状态责任，并未改变已立的 artifact/evaluation Gate。作者侧拟**具名前分母关闭**，保留原始身份与此局部反例线索；不能泛称论文无贡献。须非作者核此具体 owner 对照后才调正式漏斗。 |

这三项不扩大 845 官方分类唯一 ID 成全文队列。当前只有 `.23046` 提出前分母关闭，属于待非作者校准提案；其余是未评分、未冻结的贡献消歧。
