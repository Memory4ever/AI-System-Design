# 04/20 八项反向准入的非作者裁决

复核者：root，非本日日报作者。范围仅限作者把八项原候选移入贡献前关闭、但已有非作者逐篇必要原文复核结论与之相反的冲突。按《研究合同》§3，准入看在明确条件下是否新增值得本项目保存的机制/选择/反证；实验有限会限制采用范围，不自动抹掉准入。复用未变化的 exact-v1 必要原文与负对照记录；本裁决不替代八项最终评分、日级来源/日期/负侧 Gate、Books Decision 或整日 Complete。

| Source Family | 非作者裁决与最窄可保留增量 | 不得外推及与作者前关闭理由的关系 |
| --- | --- | --- |
| [2604.15351v1 Aletheia](https://arxiv.org/html/2604.15351v1) | **恢复候选、标准仅报告**。在 LoRA 微调可选择执行层时，短梯度画像选择 layer chunk 是固定全层更新之外的具体成本/支持集选择。 | 不存在同预算随机/深度选层强对照，不能把报告收益唯一归因于梯度排名；但这不使选择接口变成单纯词汇关联。沿用 apr01 的逐篇必要审读。 |
| [2604.15451v1 Weak-to-Strong KD](https://arxiv.org/html/2604.15451v1) | **恢复候选、标准仅报告**。弱而适配的 frozen teacher 只在 early student phase 生效，两次 validation 越过 teacher 后撤去 KD；teacher gap × active lifetime 是可检查的训练策略条件。 | 原文实验为视觉训练，不能写成 LLM 已验证的训练收益；未计完整 teacher forward/构建成本，不采 universal speedup。项目包含多模态训练，不能仅因不是 LLM 将其关在分母外。沿用 apr01 的逐篇必要审读。 |
| [2604.15614v1 E-BoN](https://arxiv.org/html/2604.15614v1) | **恢复候选、标准仅报告**。固定候选预算内以 entmax 形状和目标状态缩放改变 action-selection 探索/利用，是具条件的 embodied policy 采样分支。 | 实验为 off-policy locomotion，不推 Foundation/VLA 或全链路时延；额外 transition/marginal model 成本与特殊目标病态须保留。Ch26 的行动闭环给其受限 owner，不以应用负载小为唯一排除条件。沿用 apr01 的逐篇必要审读。 |
| [2604.16076v1 PGCM](https://arxiv.org/html/2604.16076v1) | **恢复候选、标准仅报告**。part→离散可视原型→concept-only task 是不同于全隐空间分类的可编辑表示接口。 | 原型不自动是因果/人类语义，segmenter 已消费完整输入，且存在负迁移；不称 MLLM 已验证。现有多模态表示 owner 可容纳此受限分支，不能只因视觉数据集将接口判断删除。沿用 apr01 的逐篇必要审读。 |
| [2604.15705v1 CPO++](https://arxiv.org/html/2604.15705v1) | **恢复候选、标准仅报告**。多模态偏好数据的概念图文字替换、视觉近邻取负与逆匹配过滤是训练支持集的具体替代设计。 | 潜在 D 未识别、双分支消融不证严格正交或医疗/驾驶安全；这限制因果/部署结论，不消灭训练数据选择。沿用 apr01 的逐篇必要审读。 |
| [2604.15706v1 NAG](https://arxiv.org/html/2604.15706v1) | **恢复候选、标准仅报告**。用跨层干预的 activation proxy 选择目标预训练数据，改变的是数据筛选指标及其昂贵的特征提取成本。 | Top-K 重叠不是唯一功能骨架；MMLU 分支反退，不能称全面更好。仍是可检查的预训练选择分支。沿用 apr01 的逐篇必要审读。 |
| [2604.16079v1 Flow Matching Stability](https://arxiv.org/html/2604.16079v1) | **恢复候选、标准仅报告**。同 seed 输出近似与内部 vector field 不同、若干删数选择 FID 反退，为“映射稳定即可无损剪枝”提供受限负例。 | 只覆盖 CelebHQ/共用 VAE 等条件，不签跨数据稳健性或新通用删数法。负结果可修正已有代理判断，不能因缺通用新算法而自动初筛关闭。沿用已有 root 独立逐篇核验。 |
| [2604.16135v1 Motion-Adapter](https://arxiv.org/html/2604.16135v1) | **恢复候选、标准仅报告**。结构 mask 与 late fusion 在文本到复合动作生成中提供 action-composition 的局部替代接口。 | 训练/benchmark 交集不明，不能签真实物理控制、安全、training-free 整体收益；MotionDiffuse baseline 相比本模型也不能混算。仅限多模态生成/embodied 表征案例，不强行写 Books。沿用已有 root 独立逐篇核验。 |

八项均恢复的是**本窗候选资格**，不是升级 `Integrate`、Deep、无争议普遍结论或整个 04/20 Gate。作者应将八项从 pre-denominator closure 恢复到正式 §3/§4，保留既有必要证据和反证，逐项同步 Score V2 与仅报告边界；由新的日级独立复核检查最终分母、漏收/误收样本及来源窗口。此次恢复使工作态 91 候选／58 前关闭／1 日期隔离，变为 **99 候选／50 前关闭／1 日期隔离**；这不是日报已冻结的最终数字。
