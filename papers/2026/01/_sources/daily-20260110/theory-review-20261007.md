# Jan10 三项必要理论与优化证据复核

复核者：`audit_supp_jan06`（非本日日报作者）；检查日期：2026-10-07（北京时间）。范围仅 `2601.04537v1`、`2601.04670v1`、`2601.05002v1`，服务本轮补充窗口 `2026-01-09 ～ 2026-01-09`。日期落窗及原候选归属由日作者的原始日期证据负责；本文不另授日期/来源覆盖、日级完成或 Books 写后验收，不搬移原材料。

已重读 AGENTS、当前研究/Report 合同、来源使用说明及每日组、统一 Prompt，并核 ROADMAP 的 `TRAIN-RLHF`、`TRAIN-PPO`、`TRAIN-GRPO` owner。完整题摘后，只深入本次采用命题的核心方法、必要推导、关键对照及限制；未比较旧版、未遍历全部附录、未核代码或复现实验。以下评分是增量建议，不替日报作者/协调者的最终决定。

## [Not All Steps are Informative: On the Linearity of LLMs’ RLVR Training — 2601.04537v1](https://arxiv.org/html/2601.04537v1)

实际范围：§3.1–3.3、§4.1–4.3、A.1/Table1–3，以及直接有关的 A.2 LayerNorm 反侧。exact-v1 HTML 使用上述标题；其他入口的后续标题不改变家族身份，不据改名重评分。

证据限定：§3 的 sampled-weight/固定 prefix log-prob 线性诊断不是全参数或新轨迹定律；A.2 的 LayerNorm 反侧也须保留。§4 Eq2 用两个 checkpoint 的权重差外推；Eq3 交替真实 RL 与外推，前者恢复 reward-grounded 方向，后者不消费新的梯度。Fig5 支持有限外推半径，不支持无限延长。logit 外推是另一种两模型生成分支，不等于生成一个单模型 checkpoint。

关键反证：§4.3 的全面胜出/零额外 GPU 费用措辞不采用。A.1 Table3 的 LCB 在 200 与 1200 实际 RL 步时分别从基线 `.2714/.2857` 降到 `.2619/.2762`；`6.1×` 是特定 AIME24 质量下的实际 RL 步数比，不是端到端墙钟或总计算比。A.1 是 DeepSeek-R1-Distill-Qwen-1.5B/DeepScaleR、无 KL/entropy regularization 的受限配置；硬件、完整调参/存读写预算及外推时 Adam moments 的处理未充分披露。

**自己的设计判断：**未来 checkpoint 是训练 proposal，不能凭几何拟合取得质量权限。两份 checkpoint、插值系数/跨度、优化器状态处理和校验集均应版本化；真实 RL、checkpoint I/O、外推与搜索/评价各自计价。固定 probe 失配、跨度失稳或代码质量退步时回普通真实 RL。现有旧方案仍购买真实 reward-grounded 更新，而不是无信息冗余。

评分建议 `2 + 2 + 2 = 6`：具体替代更新机制横跨 checkpoint、真实 rollout/update 与质量预算；不为相关性或 headline 加分。受影响反证已深入，必要证据完成。

Books 提案：唯一 owner [`TRAIN-GRPO / Ch33`](../../../../../books/part-04-training-system/33-grpo.md)，在“RL Recipe 必须绑定 Optimizer Transform 与 Sharding Layout”后窄接有限 checkpoint-extrapolation 分支。已实际读该段及训练-loop 邻接；现文有 optimizer/router/shard identity 和普通 clipped updates，没有 RL-Extra 的 checkpoint 差向量外推及真实 RL 校正机制，故不是仅主题已有覆盖。Ch31“RLHF 的系统成本”只用于交接，不复制机制；Ch35 不新建重复 owner。未写 Books，需 root 落实及非写入者 POST。

## [Learning Dynamics in RL Post-Training for Language Models — 2601.04670v1](https://arxiv.org/html/2601.04670v1)

实际范围：§3、§4.1–4.3、§5.1–5.4、A.1 的 Taylor/目标梯度/NTK 分解、A.2 的必要 argmax 证明、B.1–B.3 必要实验口径。为公式矛盾定点核 [exact-v1 PDF](https://arxiv.org/pdf/2601.04670v1) 第14页，不扩读其他附件。

机制：§4.3 先冻结 feature extractor、仅更新 unembedding classifier，再恢复全参 RL；不是 classifier-only 替代全程 RL。§5.3 的初段单独 reward 改善很小，后段才有局部增益。§5.4 不支持“减少 feature distortion/增大 classifier norm”解释。理论由小步长 gradient-ascent 的局部 Taylor/empirical-NTK 分解说明传播；不等实际 Adam/GRPO 的全程收敛保证。

必要纠错：§3.2 的 KL 定义、A.1 Eq23 的 `log(pi)/log(pi_ref)` 与随后 Eq25–30 按 sample-logratio 的求导不一致；exact-v1 PDF 第14页也出现同一 log/log 表达，不能默默改成作者已证的一般 KL 定理。仅 reward-only（lambda=0）的局部分解可隔离讨论。Prop2 非负 inner-product 在等于零时所有分量相等，argmax 不唯一；严格正值的单项方向也不证明含负 reward、其他 component 及优化器的全更新必降 entropy。Table1/B.3 仅 prompt features 的有限样本不能验证所有 continuation 上假设。

自己的采用边界：Pythia-2.8B、AlpacaFarm→UltraFeedback、ArmoRM 的受限三次训练支持一个 head-warmup 替代分支；ArmoRM 不因作者称 ground-truth 就成为人类价值真值。B.1 额外 classifier epoch、6 个 RL epochs、Adam 与 512-token 人口须计价；Grace–Hopper/H100 平台不补出等墙钟/总预算匹配。增加一个 warmup 阶段可改善后段 reward 曲线，尚不证明净成本降低或泛化/多样性保持；无增益时保留从原 SFT checkpoint 直接 full RL。

评分建议 `2 + 1 + 2 = 5`：新增为单模型的分阶段参数更新权限，不给成熟 NTK/LP-FT 概念加分。公式矛盾触发的受影响理论已深入；正面采用限 CF-RL 机制，不采用争议 KL 定理。

Books 提案：唯一 owner [`TRAIN-RLHF / Ch31`](../../../../../books/part-04-training-system/31-rlhf.md)，在“RLHF 的系统成本”邻接加入 head-warmup→full-RL 分工及额外阶段费用。已读“改变输出分布”、mode/sharpening、系统成本及相关邻接；现文覆盖 distribution sharpening/能力边界和回路成本，却未覆盖 classifier-first 参数权限。不要因已有 mode-collapse 描述而拒绝实际替代分支，也不重复写泛化 entropy 叙述。Ch32/33 保留具体 policy objective owner。未写 Books，需 root 处置；争议公式保持明确不采用。

## [On the Hidden Objective Biases of Group-based Reinforcement Learning — 2601.05002v1](https://arxiv.org/html/2601.05002v1)

实际范围：§3–6、B.1–B.2、C.1–C.4、D.1–D.2 及必要 tail 定量公式。原 HTML theorem 文本实际恢复，不以页面抽取漏掉 proposition 当正文缺失。

核心证据：B.2/Eq17–18 的共享 prefix 梯度由同一 score gradient 乘 `sum_i omega_i A_i` 决定；完整 G 都共享且 effective weights 相同才由 centered advantages 消去，子集、长度权重及 active clip masks 不具该保证。C.3–C.4 的 Adam 尺度不变性需要正的全历史 global multiplier、同初始/一致缩放 moments、无未同比缩放的 reward-independent KL、epsilon 可忽略，且 alpha 不因 reward std/阈值变化；不能推为任意 group normalization 或奖励形状无效。

D.2 在此前梯度方向持久、随后 advantage 梯度为零且忽略其他驱动力的条件下，旧 first moment 仍递减但非零；其大 T、epsilon 可忽略的尾步比例约为 `(beta1/sqrt(beta2))^(k+1)`。这是 loss-gradient clip 不是硬参数边界的具体反例，不证明任意共享网络的 ratio 都单向越界，也不授安全移除 clipping。正文 Eq4–6 与附录 canonical Adam 写法存在符号/修正口径差异，不作为可执行 optimizer 配方；只用可核 canonical recurrence 的有限代数。没有从这些条件推出普遍 collapse 或净收益保证。

自己的设计判断：组中心化、loss reduction、active clipping 和 optimizer state 应分层诊断，保存 prefix-sharing 人口、实际权重及 moments；不能用 clip fraction 签发硬 trust-region。未来 momentum-aware actuator 是提案，不是本文已验证修复。只有尺度足够大且条件匹配时，global reward scaling 与 Adam 的局部不变性才适用；其他配置保留 KL/epsilon/真实 outcome 检查。

评分建议 `2 + 2 + 2 = 6`：新增为 group estimator→prefix aggregate→optimizer-state 三者的具体接口条件，不为“surrogate 非真值”或成熟 Adam 原理重复加分。关键推导/反证已深入，必要证据完成。

Books 提案：唯一 owner [`TRAIN-GRPO / Ch33`](../../../../../books/part-04-training-system/33-grpo.md)，在 clipped objective 与 “Loss Reduction 也在重写 Credit 权重”邻接窄补 prefix 消项条件、clip 后 momentum tail。已实际读这两段、“Relative Advantage 还要保留数值尺度与平移身份”及 [`Ch32 KL/clipping 交接`](../../../../../books/part-04-training-system/32-ppo.md)；长度偏差、optimizer scale 风险已有覆盖，不能重述为新增。增量是 effective-weight 消项条件与 clip 无硬边界的 optimizer-state 反例。主机制不复制到 PPO 章；未写 Books，需 root 落实及 POST。

## 本次停点

三项必要证据均完成并已发 root / 日作者；新增普通证据待办为零。04670 的争议公式已定点定位、隔离，恢复条件是同版本必要公式的明确原始更正/解释，不能用于正面一般 KL 定理；不要求整份论文/版本史补读。下述实际 Books 写后复核仅授这三项窄写入；不授日期、日级验收、来源无遗漏或实现复现。

### 实际非写入者 POST — 2026-10-07T15:42:04+08:00

结论：**三项窄写入通过**。书稿写入者为 root；复核者 `audit_supp_jan06` 只写本证据笔记，未写 Books。实际顺读下列新增正文、完整前后邻接与各自章末 source note；原 exact-v1 必要证据、身份与采用命题未变，按研究合同 §7 定点复用上文已读原证，不扩读其他章节/日期或未采用附录。

- `04670 / TRAIN-RLHF`：实际核 Ch31“RLHF 的系统成本”首两段、前一 Outcome/Trace 分支、后一完整成本列表/rollout identity 交接及末注。classifier-only warmup→full-RL、额外 epoch/阶段状态、Pythia/ArmoRM 三次有限结果、无净收益回普通 full-RL 均落实；没有采用争议 A.1 KL 定理、全程 Adam/GRPO 保证或熵普降/能力全在 head 的断言。模型评分与人类价值真值明确分离，段落与原成本链衔接通过。
- `04537 / TRAIN-GRPO`：实际核 Ch33 recipe 尾两段、前方 optimizer-transform/外部 evidence authority 交接、后方完整 RL-loop 及末注。两 checkpoint 差向量/有限跨度/真实 RL 校正已落；固定 prefix 与抽样诊断不替全轨迹定律、logit 外推不等单模型 checkpoint、LCB 反退、步数比非总 GPU/墙钟、I/O/评价与 moments 处理费用/披露限制及普通真实 RL 退路均保留，未默默宣告未来 checkpoint 等同已训练能力。
- `05002 / TRAIN-GRPO`：实际核 Ch33 Loss Reduction 尾两段及前方 Balanced Aggregation/后方 Comparison Pair，另核 Relative Advantage 尾段及前方 scale 风险/后方 rollout-budget 分支和末注。共享 prefix 的消项仅限全 G+相同 effective weights，clipping 活跃分支不遗漏；clip 后残余 moments 的有限反例不授所有 ratio 越界或移除 clip。全历史正倍率、初始状态一致缩放、epsilon/KL/权重边界没有抹去已有实际尺度风险；未照录不一致的正文 Adam 配方，不授一般 collapse 或修复保证。新增机制不静默覆盖原归一化/长度分支。

已通知 root 与日作者；各书稿 source note 当时仍写 POST 待验收，由 root 按本实际结论同步即可，复核者不自行改书稿状态。三项普通 POST 待办为零；此记录不是 Jan10 DAY pass，未检查本日其他新候选。
