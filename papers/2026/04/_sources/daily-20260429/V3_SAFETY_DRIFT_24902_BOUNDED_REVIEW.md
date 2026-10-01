# 2604.24902v1：微调后安全漂移的证据边界与现有 owner

状态：04/29 V3 作者侧标准必要证据，待非作者核准入/真实 Existing；非日期或整日 Gate。

## 身份与贡献入口

- [官方 exact-v1](https://arxiv.org/html/2604.24902v1)题名 *Safety Drift After Fine-Tuning: Evidence from High-Stakes Domains*；[v1 身份](https://arxiv.org/abs/2604.24902v1)须与 checkpoint 的官方公告窄链合用，不能把 submitted 孤字段当首次公开。若有独立更早正式公开，按家族另核。本记录不复述论文讨论中的法规阈值为当下法律事实。
- 已有安全发布逻辑要求改动后的 artifact 独立回归，但一个仍有价值的受限反证是：**base 的安全评测、LoRA/QLoRA/全参类别和参数移动量，均不能替代派生模型在不同安全构念上的实测**。若成立，低改动量/温和数据不能给发布 Gate 豁免；同时测量器切片彼此矛盾时，不能从多数指标投票产生未定义的统一“安全”。这直接支撑模型生命周期 release identity，不是因为医疗或法律应用名准入。

## 决定性原文与不成立的外推

- §3.1 的生态观察是英文、metadata 选出的 **31 个 fine-tune**（16 医、15 法）与可识别 base 配对；下载量不是独立实验个数。模型 data、训练步骤与 lineage 文档不同，不能从这一层单独识别安全变化的原因。§3.2 的受控层只用四个 7–9B instruction base、每领域一个固定数据集，比较 LoRA/QLoRA/FFT；一 epoch、同学习率 `2e-5`，其余框架默认。故“100 models”是整个 heterogeneous 分析库存，不是 100 个同预算独立随机微调对照，也不能把某一数据集代表所有 benign adaptation。
- §3.3 同时使用 HEx-PHI、MLCommons、MedSafetyBench、CARES、SafeLawBench、SORRY、Trident；GPT-4o-mini rubric、LlamaGuard classifier、拒答检测器与 pairwise judge 不是同一真值测量。§4.1 医疗生态样本 81% 在至少一项升、一项降，但 CARES dispersion、15 条 lineage/部分 benchmark CI 的大小和方向不同；§4.1 法律样本纳入拒答/遵法构念后 mixed-sign 93%，若只看直接 unsafe benchmarks 为 60%。不能把 93% 写成同一安全构念上的退化率。
- §4.2 在受控医疗层 83% 的配置改善所列 in-domain 医疗 benchmark，而 100% 在 MLCommons 退化；QLoRA/Gemma 的 CARES `-36pp` 与 MLCommons `+45pp` 分向。法律层 MLCommons 平均 `+19.8pp`、SafeLawBench 92% 退化，但 SORRY 经常改善；限制到三个直接 unsafe 指标时 mixed-sign 从全部构念的 83% 降到 42%。这支持**评价构念与下游行为分账**，不证明所有 benign fine-tuning 普遍变危险或某一种 PEFT 必然较安全。
- §4.2 Figure 4 用同 base 的 normalized weight `L2` 作参数移动代理，报告多数比较 `|ρ|<0.25,R²<0.1`；法律 HEx-PHI 有反向相关 `ρ<-0.64,p=.02`，所以精确结论是该有限套件中**移动量不是可靠放行代理**，不是“参数大小永不影响安全”。§4.3 保持模型输出不变，仅给 HEx-PHI judge prompt 加等级示例，医疗结果 25% 方向翻转；这是 EvalSpec 敏感度，不可直接解释为模型真实行为变化。§5 自承认不同 benchmark 可测不同有效构念，也可能不可靠，缺专家或真实伤害外部校准时不能选一个为真值。

## Books 决策提案

- [ROADMAP](../../../../../ROADMAP.md) `PLATFORM-SECURITY` 的 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)已有 benign preference 更新可改 refusal boundary、base/adapter/update identity 与分布外 safety slice 的发布前比较、每次 remediation 后旧 Gate 作废和完整 safety regression；[Ch31](../../../../../books/part-04-training-system/31-rlhf.md)已明确平均 KL 不能证明各 safety slice 保持。[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已有 EvalSpec 构念、judge revision 与 slice 权责。本文的**配对实证**补强这些既有命题；目前没有非同义新权责或控制机制需要再写一段，作者侧拟 `No Change — Existing Coverage`，不是说论文无价值或结果已由旧书稿测出。
- 拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9`、标准审阅、`Existing`（若非作者认为受限研究不足以改变已有判断，可具名修正到前分母关闭；不能仅因医疗/法律任务局部排除）。所采用命题限“按派生 artifact 与构念切片重验，不能用 base 分数/方法类别/参数距离放行”；不采论文治理建议中的法律归责推论或跨模型普遍发生率。独立核只需 §3.1–3.3、§4.1 mixed-sign 分母、§4.2 Figure4、§4.3 与 Ch72/31/66 上述实际段，不读完整引用史。
