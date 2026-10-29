# SyTTA 最低事实门与直接反侧

作者Kierkegaard；只2510.10223v1必要[HTML](SUP_CORE_2510.10223_20261013.raw)，HTTP200/exit28，668421/预期1099138bytes部分body，不称全稿；实际完整读取§4.1–4.3/Algo1/Table1和§6.1–6.4主文节点，未依赖截断尾/完整附件。

**作者最低N→窄P提案**：参数θ'从θ初始化并按minibatch unlabeled questions的NLL/生成prefix entropy/base-reference KL更新；k=4是生成prefix长度而非四可训练token/部署总增费。Static-Ref把base prefix及logits缓存后适配，用固定producer证据；Dynamic-Ref希望适配模型生成prefix再以base同context logits作reference。固定记录与在线自产context是不同消费资格/漂移反馈，并非只PPL+entropy两个成熟名字，足以保留窄潜力。

不静默修原recipe或采用正确性/稳定性/费用保证：

- Eq3 Dynamic-Ref写GenPrefix(pθ')，Algo1 line10却写GenPrefix(pθ)，而text称不断更新自身prefix。固定base与liveadapted不是同规则，不能替作者选择或署为完成实现核。
- Eq7 OCS已包括λKL LKL，Algo1 line14又在wOCS LOCS之外额外加λKL LKL；Eq8只两项，三处权重口径不同，不自行消掉重复。
- Eq9的共同EMA分母在r_i/Σr_j中代数抵消，不能仅据公式接受“EMA govern weights”。Eq11权重和2也不保证梯度幅值有界；clip与λ基系数再缩放是否保原作用需实现事实，当前未核。
- Table1 Static-Ref每样本一forward只适配阶段，预生成base prefix/logits与缓存、backward/optimizer不在该count，不签全部训练/部署省费或只4额外token的端到端SLO。§6跨长度/mode平均与总体ROUGE提升不等每domain/每consumer稳定；k4与k16并非所有context最优。
- NLL gating/entropy较低都不是答案真值，KL锚旧model也非新domain正确。本文不采用农业/医疗效果、无collapse保证或声称vLLM缓存跨参数更新自动有效；未运行代码。

root本日[独核§9](SUP_INDEPENDENT_20261013.md)已实际读取§3.2/完整§4/Algo1/Table1/§6必要层，N→窄P通过，THIRD当前11P1C无N；上述四处recipe与全部制备费用限制保留。本包只决定事实/反侧，日期/正式score/完整Evidence/Books仍未授，不扩全部24全文。
