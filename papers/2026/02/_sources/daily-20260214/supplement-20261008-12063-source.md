# VLAW：root 必要证据采用包

范围仅为 Daily 2026-02-14 的补查家族 `SF-2026-ARXIV-2602-12063`。root 在本项是证据包作者，不是独立复核者；本包不授整日完成。日期准入沿用本日已核的当窗关系，提交时间和 DOI created 不单独充当首次公开证据，不移动旧候选。

## 实际审阅与最小命题

[exact-v1](https://arxiv.org/html/2602.12063v1) 原件在 [core-2](./supplement-20261008-core-2.json)，实际读完整 Introduction、Preliminaries、Method、Experiments、Conclusions/Impact。2+2+2=6，拟补具体训练人口分工，标准审阅后对可能的 owner 差额定点深入；不采用附录理论、全部代码或生产保证。

示教 BC 在少量成功数据下合理，但当前 policy 的真实失败接触可能不在示教支持中。§4 将当前真实 rollout 的成功与失败共同用于 world model 更新，并混合原 DROID 数据；policy 的 flow-matching 更新则只消费真实成功与 reward model 筛过的 imagined success。这是同一真实交互进入不同学习目标的分工，不是让 policy 模仿所有失败动作，也不让 imagined label 成为真实 outcome。§4.1 明确 reward model 首轮以真实 binary success 标签训练；算法简写不能扩为每轮均重新训练的已证实实现。Qwen3-VL-4B-Instruct 的 yes 概率阈值仅为成功筛选代理，与 learned world model 可以共同犯错。

§4.3 的正则 RL/闭式权重只是解释分支，本包不采用收敛、全局最优或 flow-matching 等于实际 KL 的保证。两轮共改模型与训练数据，不证明无限迭代单调提升。

## 对照、反侧与成本

π0.5 policy、Ctrl-World，DROID 设置的 Franka Panda/Robotiq、两外部相机和一腕相机；五类接触/可变形任务。每类25 expert demonstrations warm-start，每轮每类50真实 rollout；world model 50K steps，每类500合成 rollout，policy 2K steps/batch256，两轮。FilteredBC、DSRL 匹配真实 rollout 数，不等于匹配全部计算、合成生成、奖励筛选和实机 reset 成本。

Table1 的256段 replay/5秒图像评价不是闭环成功；50段 interaction clips 的成功人口30、失败人口20。加入 online rollouts 后 FP 11→1，但 FN 2→4、TP 28→26，不能称所有判别误差下降或物理真实性已获认证。Figure9 仅 drawing 的500→250 synthetic 及去掉 real-success 对照，不能推广为每任务的唯一归因。未实际核 Figure7 图片百分数，不采用摘要39.2/11.6收益数字。必要主文没有足够硬件、精度、控制频率、动作 horizon、生成时延、重置人工成本或端到端 SLO；相关字段写 Not Disclosed，不能借低模型误差授部署安全。没有复现实验、核 artifact 或真实安全能力。

## 实际 owner 比较与待复核改动

root 实际读 `MULTIMODAL-WORLD-MODELS` Ch25 的 Imagined rollout 主线、失败人口 RaWMPC、真实 replay 与 dynamics 目标偏置、WIMLE synthetic 权重、Reflection 的失败动作证据，以及 Ch24/26 的具体交接。现有正文已有失败转移应参与 dynamics、模型预测不拥有 action commit 的原则；没有在这条训练分支中明确“dynamics 需要成功与失败、BC policy 不能照抄失败、reward 筛选仍可漏/误拒”这三个目标的分工。拟只在 Imagined rollout 的失败人口段后补一段，把成本、共同错误与回退写在正文；模型/实验名和数字留本包及末注。先由非作者独立 Source/PRE 检查，未通过前不写 Books。

## 待独立 PRE 的逐字拟文

失败人口还可以帮助训练模型，却不必成为策略的模仿目标。在一个迭代分支中，当前 policy 的真实成功与失败共同更新 dynamics，并混合原 DROID 数据以约束漂移；行为克隆则只消费真实成功和 reward model 筛过的 imagined success。两种目标需要不同样本：失败 transition 能教会预测器“这样行动会失败”，把同一失败动作当成要复现的答案却可能损伤 policy。reward model 的真实成功标签与阈值必须另行校准，不能由生成模型与判分器相互同意认证成功。[受限实机对照](https://arxiv.org/html/2602.12063v1)在五类任务、两轮训练中支持这条分工，但世界模型的交互结果预测减少误报同时增加漏报，部分消融只覆盖单一任务；它不是无限迭代单调改进或物理安全保证。真实采集与重置、dynamics 更新、合成生成、筛选和 policy 训练均付费，相同真实 rollout 数不等相同总预算。模型与 judge 共同失配、真实支持不足或费用不合算时，保留真实成功 BC、较短想象与真实结果验收，不继续用想象标签放大自证循环。<!-- source-family:SF-2026-ARXIV-2602-12063 -->
