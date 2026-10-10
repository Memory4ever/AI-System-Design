# 11653 必要证据与 owner 差额

作者 root。精确材料为 [v1 HTML](https://arxiv.org/html/2603.11653v1)（本日 `SUP_CORE_11653.raw/.txt`）；实际读取 §3、§4.1–4.3 的协议/关键结果与扰动范围、§5.1 Table3 及相关解释、§5.2–5.4、§6、AppendixB/D/E 的指标、任务选择与消融差额。未逐行读全部消融曲线、全附录或代码，不授复现。v2/v3不搬入本窗；本日已有日期门复用，提交时刻不另当公开证明。

## 必要结果与反侧

共享 camera/state/action schema，语言直接提供 task identity；顺序训练不能访问旧任务环境，Expert Replay 对照额外有旧专家演示。三种 base VLA、五个模拟 benchmark，在任务上先少量 SFT 得非零成功，再 GRPO+rank32 LoRA；这不是零示教从头学习。AppendixD明确任务选择避免近零/饱和初始成功，ManiSkill统一背景与有限初始位姿，均约束外推。三 seeds mean±SE；多数 CRL 参数另局部扫，SeqFT不扫，异方法人口/成本不能叫完全相等。

NBT是每个旧任务从刚学完到最后的成功率差再平均，可能以正负转移相抵；AVG是末态训练任务平均，ZS是未进入持续训练的 held-out tasks，三者不互相认证。Table3在libero-spatial删RL、换12M policy、去LoRA均反退，但AppendixE不同示教量、初始成功、batch与数据人口，不纯粹证明参数规模的单因果。on-policy梯度由当前策略采样加权是实际机制，不证明与初始策略KL必小、概率support永不外移或所有参数不干扰旧任务；随机高维向量近正交也不证明训练梯度独立。§5.3承認零样本优势解释未定。§5.4加倍最低任务 episodes 可补AVG差距，以更多交互付费，不是同预算追平oracle或通用无遗忘。

结论只支持：在这个已预训练、可适配、有可观测任务身份和有限共享schema条件下，先测试简单顺序RL+单adapter，并把plasticity/旧技能/heldout/成本分账；不是宣布replay/隔离方法过时。实机/新embodiment是未来方向；不授physical safety、终身retention或控制SLO。性能硬件/精度/并发不用于本轮速度主张，未做端到端测量。

## 评分与实际 owner

2+1+2=5，标准最低；实际差额修正“必须复杂CRL才可持续”的局部设计前提，深入以上受影响局部，不读无关附件。Owner `MULTIMODAL-EMBODIED-VLA` / Ch26，邻接Ch25 observed/imagined 与Ch27 数据合同入口已读；Ch26完整“Continual VLA 的 Adapter Timescale 与 Replay Frontier”三段及前后 grounding→pool commissioning 已实际顺读。已有正文有双timescale/cache身份成本，但没有先验收简单SeqFT的条件分支与AVG/NBT/ZS区分，因此不是主题已有覆盖。

拟在“完整replay/joint retraining…单adapter覆盖”之后、fast/slow分支之前插两段，经非作者必要Source/PRE通过再由root写入：

不过，“持续任务”本身不意味着必须先加 replay、router 或多个 adapter。若预训练 policy 已具备相关动作、任务身份由语言给出、sensor/action schema 共享且低秩更新有足够容量，可以先验收单 adapter 的顺序 on-policy RL：只与当前任务交互，逐任务保存 policy 与成功矩阵，分别检查新任务可塑性、已学技能保持和未参与适配的 held-out 任务。这是低维护成本的替代分支，不是 LoRA 或 on-policy 天然免疫遗忘；on-policy 对当前策略动作的采样加权不等于对初始 policy 的固定 KL 约束，高维容量也不保证真实更新彼此正交。

[有限 VLA 对照](https://arxiv.org/html/2603.11653v1)支持这条简单基线，但先用示教建立非零初始成功，再选择有限模拟任务，并不能外推到从零技能、未知 task identity、换 embodiment 或实机长期运行。最终训练任务均值、平均负向迁移与 held-out 成功率要分账；平均遗忘小仍可能掩盖个别任务回退。去掉 RL/LoRA 或换小模型的反侧支持联合条件值得检查，却未隔离所有数据、初始化与 batch 差异；增加交互补齐训练差距也不等同预算。先测旧技能逐项退步、质量与交互成本；简单更新失败或分布变化超出已验范围时，再采用下面的回放/双时间尺度/隔离分支，保留离线再训练与独立控制安全层。

实际写入与 nonwriter POST 尚未完成，不授日级 Gate。
