# 12/02 Mill 所指十二项的局部补齐

执行：2026-10-02，北京时间18:39后。仅处理既有cs.LG首25中的11项及已发现GR-RL，不扩月库存。本记录复用[Mill实际独立读取的完整v1题摘和必要正文](./ROOT_ADMISSION_REVIEW.md)，明确不冒称作者重新读完全部论文；作者本轮另外定点打开00242/00293完整v1摘要、BioArc v1摘要与§4.2–4.5设计原则、00163 §3方法、00307正文的保护单位与§4.1。准入处置是作者判断，仍待Mill局部闭合，不改其§6或metadata。

| 精确材料 | 原有约束 → 实际增量 → 处置与采用边界 |
| --- | --- |
| [2512.00163v1](https://arxiv.org/abs/2512.00163v1) | 自解释不一定忠实于行为 → LLM给出的特征方向与对其预测函数计算的SHAP存在分歧 → 保留评价反证潜在准入，日期隔离。作者定点§3确认被解释量是JSON输出的正类概率；PermutationExplainer对每数据集250实例、k-means五中心masker及四次排列。三个任务正类比例不一致，不能把SHAP当因果真值，也不能把accuracy或合理语言解释当部署充分证据。不是财务建议或普遍因果结论。 |
| [2512.00170v1](https://arxiv.org/abs/2512.00170v1) | 高维BO常默认复杂结构先验更好 → 几何变换后的线性kernel构成简单模型反证 → 保留优化/表示选择潜在准入。复用Mill题摘结果，不因molecule实例排除；未采用优势数字，比较预算、几何变换和任务边界要在公开归属恢复后围绕命题审阅。 |
| [2512.00229v1](https://arxiv.org/abs/2512.00229v1) | OOD检测依赖外部异常样本与阈值选择 → classifier inversion/exclusion形成不使用外部OOD数据集的闭环 → 保留模型失效识别的替代设计潜在准入。不是因为MNIST才收/拒；约0 FPR是作者局部实验，不等于通用误报控制或无OOD风险。 |
| [Polynomial Neural Sheaf Diffusion 2512.00242v1](https://arxiv.org/abs/2512.00242v1) | dense restriction/SVD归一化随stalk维数增加重建和梯度负担 → 谱缩放算子上的三项多项式递推、凸混合谱响应与对角restriction将K-hop范围和stalk维数解耦 → 保留学习表示的计算/稳定性取舍潜在准入，不把非Transformer自动排除。它挑战的是边感知聚合必须靠大stalk容量的选择，不证明LLM Attention可被直接替换；尚未授长期owner或资源收益，日期恢复后再核SVD、同质/异质图对照与梯度边界。 |
| [2512.00249v1](https://arxiv.org/abs/2512.00249v1) | 官方admin标记与[2408.13333](https://arxiv.org/abs/2408.13333)大量文本重叠；Mill实际打开同作者旧文，2024已有high-level RL/low-level scripts。当前题摘未呈现改变该机制的修订 → 按来源家族/重复事件关闭，不是按wargaming领域关闭，不指称撤稿或抄袭；有具名改变命题的修订证据才重开。 |
| [2512.00251v1](https://arxiv.org/abs/2512.00251v1) | CTGAN与Sinkhorn loss用于DDoS不平衡样本，题摘给出组合和领域指标，未新增可迁移的训练、安全威胁或系统正确性约束 → 贡献前关闭。不把zero-day宣传当系统安全保证；日期不影响该处置，不另追首公开。 |
| [BioArc 2512.00283v1](https://arxiv.org/html/2512.00283v1) | 不以biology标题直接排除。作者实际题摘与§4.2–4.5：Hyena→Transformer→CNN次序、任务族架构相似、pretraining非必增益、1-mer与BPE依赖训练策略，均由DNA/蛋白任务及生物语法验证；Agent预测的知识库/监督与transfer也针对生物架构。框架的通用NAS/weight sharing和模块组合未给出独立于该科学路线的新基础模型设计条件。当前可支持增量是生物基础模型的经验设计规则，按ROADMAP暂缓AI for Science关闭本次范围；不经Ch11/22/Agent绕回科学应用，不采用25倍宣传。若有真正通用模型机制证据，再定点重开，不说论文没有学术价值。 |
| [FiCoTS 2512.00293v1](https://arxiv.org/abs/2512.00293v1) | 文本语义与连续时间信号存在错位，LLM直接充当预测骨干并非必然合理 → LLM仅编码文本补强时序分支，通过动态图token对齐、global cross-attention及决策gate作三级交互 → 保留跨模态角色/融合替代设计潜在准入。改变“所有模态先塞进LLM再预测”的选择，而不是收时序排名；七任务结果不证明任意非文本模态都适用，跨模态语义和文本信息来源必须保留。 |
| [2512.00303v1](https://arxiv.org/abs/2512.00303v1) | 联邦RL的TD梯度不能唯一确定轨迹 → state/reward/dynamics priors约束梯度反演伪解 → 必要安全侧潜在准入。复用Mill实际引言/method阅读，不承诺任意梯度可恢复；威胁需攻击者能见何种梯度、模型与环境先验，不把监督学习梯度反演条件直接搬来。 |
| [Adversarial Signed Graph Learning with Differential Privacy 2512.00307v1](https://arxiv.org/html/2512.00307v1) | 节点共享依赖与符号翻转导致敏感度和级联错误，edge扰动并不等价于node保护 → 正负子图分离、判别器梯度扰动和限制路径数/长度的BFS-tree降低依赖 → 保留训练隐私/依赖单位潜在准入。作者定点确认声称node-level而非edge-level DP；移除节点可同时移除关联边，不能拿独立样本DPSGD预算直接套节点。作者的privacy proof与具体敏感度尚未作为已证实保证采用，不能外推LLM token/document隐私。 |
| [2512.00311v1](https://arxiv.org/abs/2512.00311v1) | teacher-student-teacher提取学生解题过程，题摘呈现KT领域的中间信号与预测增益，没有新LLM系统机制或迁移成立条件 → 贡献前关闭，不按education标签关闭。日期不影响处置，不增材料请求。 |
| [GR-RL 2512.01801v1](https://arxiv.org/abs/2512.01801v1) / [Seed原题摘](https://seed.bytedance.com/en/public_papers/gr-rl-going-dexterous-and-precise-for-long-horizon-robotic-manipulation) | noisy/suboptimal demonstrations限制离线模仿 → offline Q-progress筛选、morphological symmetry与online latent-noise适配 → 保留长程VLA/控制训练的潜在准入，不采用鞋带成功率作可靠性保证。补齐原记录缺失的ID和具体增量；Dec2日编码及Dec1 submitted都未证明个体首公开。 |

局部结果：11遗漏项中7项潜在准入、4项明确关闭，另GR-RL精确身份/题摘已补。它们不是已确定本窗候选或Evidence完成项。潜在项缺少个体first-public，沿已有有限恢复停点隔离，不反复探同一接口；可接受恢复是具名v1历史new公告/RSS/email或可核实原始首次正文公开，随后只恢复受影响日的必要证据审阅/Books。安全侧与反证不删除。Books无写入、无已整合声明；日期隔离不冒充已有覆盖。
