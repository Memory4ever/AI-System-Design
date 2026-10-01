# Apr22 三项必要来源到当前 owner 的非作者裁决

复核者 root，不是 Apr22 Daily 作者；仅检查具名候选的官方 v1、真实章节与邻接，不代替写后或日级 Gate。采用理由是具体长期机制缺口，不是 ROADMAP 可映射性。

## 2604.18933 → Ch26：写前窄采用

[官方 v1](https://arxiv.org/html/2604.18933v1) §III-B/Fig3、VIII-E/F：两套 memory-off/on policy 在训练分割上拟合，以另一分割的 action-prediction error ratio 生成 gate label；冻结 binary gate 后重训最终 policy。Ch26 已分清 episode memory 与行动有效性，但未说明“是否读历史”的 controller 如何独立校准。允许补两段；proxy label 不是最终 policy 的反事实必要性证明，保留校准成本、噪声/缓存条件、短任务无记忆基线与物理安全边界。原 `2+2+2=6` 不据此升级。

## 2604.18963 → Ch29：写前窄采用

[官方 v1](https://arxiv.org/html/2604.18963v1) §5–6/Algorithm1：冻结原 teacher 与 calibration target，另外更新 teacher 以联合 task reward、原分布 KL anchor 与可改变符号的兼容性项，然后再评价 student。当前 Ch29 有 teacher 强度、表示匹配与监督时机，但缺 teacher 自身成为可校准资产的选择分支。允许在 teacher 选择段补两段，teacher utility 与 student learnability 分别验收；跨 tokenizer sequence score 不等逐 token 可比，有限错误轨迹结果不构成一般 IP 防护。原 `2+2+2=6`。

## 2604.19033 → Ch28：有限条件分支

[官方 v1](https://arxiv.org/html/2604.19033v1) §3–5/Appendix B：先规定函数/采样动作 log-prob 的目标变化，再沿已选方向近似反解参数步长，eligibility trace 与对角归一化增加状态。Ch28 当前 batch-Jacobian 残差反解与参数组学习率之间可补“参数单位 vs 输出单位”的短对照；必须限定 streaming RL，不宣称 LLM 预训练改善、hard KL cap 或无偏 policy gradient，并保留分母不稳、action-dependent reweighting、非线性大步和 AdamW/SGD 回退。若无法与现有主线自然衔接，则改 Weekly Only，不为已有评分强写正文。原 `2+2+2=6`。

三项仅写前 PASS；实际正文、相邻衔接与报告最终状态必须另经非作者复核。
