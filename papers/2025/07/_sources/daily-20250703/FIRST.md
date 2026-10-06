# 2025-07-03 首批准入校准（作者稿，未评分）

固定窗口：2025-07-02T09:00:00+08:00 ～ 2025-07-03T09:00:00+08:00。
查询提交时间只是发现池，不能证明公开时间。完整题摘原件：`v1-abstracts.raw`（30 个精确 v1），宽主题发现原件：`topic-model{,-p100,-p200}.raw`、`topic-system.raw`、`topic-multimodal.raw`。
当前均未确定当窗归属，故以下是拟保留贡献线索，不是已入选候选，不评分、不进入 Books。需要 root 独立准入校准。

## 拟保留的具体增量

| v1 身份 | 原有约束 → 摘要实际增量 → 值得核验的判断 |
| --- | --- |
| 2507.01154 FlashDP | 显式 per-sample gradient 占内存、GhostClip 重算 → per-layer 融合一次算梯度 → DP-SGD 内存/重算是否能同时消减；不是只保留 90% 吞吐数字。 |
| 2507.01201 JAM | 独立视觉/语言空间不对齐 → 冻结骨干、协调重建与 cross-modal alignment → 窄语义差异是否可由局部变换恢复；v1 与后续摘要差异需保持版本边界。 |
| 2507.01216 PAE MobiLLM | 移动侧 activation/label 传输受限 → cached activations、loss-token shortcut、prediction-difference additive side network → 通信与隐私的成立条件；作者“learn nothing”不能直接作保证。 |
| 2507.01241 Beyond First-Order | 固定随机梯度预算 → 用 sample-complexity 调整采样并用 conjugate subgradient 搜索方向 → 是否改变样本/更新成本取舍，须检查理论假设。 |
| 2507.01297 CompactDS | 简单 RAG 对推理问题看似无用 → 控制 datastore 覆盖与多样性后重验简单检索 → 失败可能是知识库条件而非一定需要复杂 Agent 流程。 |
| 2507.01299 LaRoSA | magnitude sparsity 不稳定且 recovery training 费时 → layerwise orthogonal rotation+固定 Top-K → 训练自由稀疏的质量/稳定实际速度取舍。 |
| 2507.01321 ICLShield | ICL 示范被投毒 → dual-learning 概念偏好比边界 → 不改权重也须评估示范污染；confidence/similarity 防御不是普遍保证。 |
| 2507.01368 Activation RM | 新偏好需要独立大样本 RM → steering activations 构造 few-shot reward → 不训练新 RM 的可行性和 reward-hacking 条件。 |
| 2507.01467 REG | REPA 训练对齐在生成时消失 → 图像 latent 与一个语义 token 联合去噪 → 语义辅助不仅训练蒸馏，而可参与生成路径。 |
| 2507.01513 SafePTR | multimodal jailbreak 泛化防御易过拒 → vulnerable layers 少量 token prune、后层恢复良性特征 → 可定位的攻击路径及效用损失边界。 |
| 2507.01551 SPRO | 独立 process RM 额外成本 → policy 内生 process reward+masked step advantage → outcome-only 与 process-supervised RL 的成本/归因边界。 |
| 2507.01598 Muon analysis | 优化器矩阵结构经验使用 → 四种变体收敛假设、decay/LR 关系、critical batch → Muon 理论有效性而不是再次宣称更快。 |
| 2507.01628 DaiFu | checkpoint-retry 对轻微程序错误过重 → 保留运行上下文、原地修补恢复 → 可恢复异常与一致性/重执行边界。 |
| 2507.01652 LASAD | 线性 attention 的一维序列距离损害图像空间依赖 → 由真实二维位置计算 decay → 图像 AR 的效率/空间质量边界。 |
| 2507.01663 AsyncFlow | RL task-separated 流水空闲与失衡 → streaming storage/scheduling+staleness-threshold 延后更新 → 吞吐与 policy freshness 的具体取舍。 |
| 2507.01693 SODA | 日志只给输出难做 incident forensics → next-token logits 的 exact inversion 与长输入失败 → logit 暴露/隐私边界，而非泛化为文本能逆推 prompt。 |
| 2507.01756 DisCon | 离散 token 损失信息、连续高维密度难学 → 将离散 token 改为连续生成条件 → tokenizer/生成目标角色分离。 |
| 2507.01786 Evaluation awareness | 评估可假设样本代表部署 → 内部可线性区分 testing/deployment → 评估环境真实性风险；不能推导有意欺骗。 |
| 2507.01790 Modality conflict | 多模态冲突下平均分掩盖路径 → modality preference 与 router heads 干预/迁移 → 指令指定模态和行为偏好可分离。 |
| 2507.01806 CPU LoRA meta-generation | 每任务 LoRA 需要梯度优化/GPU → 用 adapter bank 学 dataset-distribution→LoRA operator、CPU 组合 → 训练前置成本换推理生成更新的范围。 |
| 2507.01900 HARP | 全层头裁剪忽略位置与幅值 → 高层裁剪+adaptive rescaling → 裁剪后表示幅值是质量损失的额外变量。 |
| 2507.01915 GAPO | 单标量 preference 混合冲突目标 → multiple-gradient descent 调整方向并给用户 Pareto 权重 → 多目标保证的假设/代价。 |
| 2507.01921 NaturalThoughts | teacher trace 只看规模 → 难度与推理策略多样性对样本效率的比较 → 蒸馏数据选择边界；需控制预算。 |
| 2507.01961 AC-DiT | base/arm 同步动作忽略底座影响 → mobility-to-body conditioning、阶段感知 2D/3D 权重 → 物理联动条件；不只因机器人指标保留。 |

## 当前首批关闭（无需追查不影响处置的日期）

| 身份 | 完整题摘关闭理由 |
| --- | --- |
| 2507.01489 Agent-as-Tool | 拆 reasoning/tool agent 及去冗余是已知层级委派；少量训练和 Bamboogle 数字没有新增执行/可靠性机制或证明委派成立条件。 |
| 2507.01823 TD-MPC-Opt | 对 world-model agent 做 distillation 与 FP16 PTQ；模型缩小/指标改善没有揭示新 distillation 机制或复杂世界知识保留条件。 |
| 2507.01949 Keye-VL | staged pretraining/posttraining 与五模式 cold-start data 的 recipe；未指明相较成熟 reasoning/nonthinking 混合的机制新差异、有效性条件或模块贡献归因，不因模型规模和 benchmark 收录。 |

宽列表余下的领域应用、科学/医学任务、泛任务 survey 和普通 benchmark 只作查漏，不是逐项关闭队列。不存在保留数量或比例目标。

## 非作者 root 首批校准反馈

root 首批实际读完整精确 v1 题摘 14 项：FlashDP、JAM、HARP、SODA、Evaluation Awareness、SafePTR、AsyncFlow、AC-DiT，以及当时六项关闭（CARE-RAG、TriVLA、EdgeLoRA、Agent-as-Tool、TD-MPC-Opt、Keye-VL）。CARE/TriVLA/EdgeLoRA旧关闭已撤回，不在当前关闭表；本节仅留改判历史。其余16个v1题摘当时不在首批范围；后续已补全独立校准，见末节。

八项潜在机制/边界方向成立，宣传性能数字未被采用。六项关闭中重开两项，另一定点消歧：

- TriVLA：原排除理由只看模块组合过窄；当前静态观测与 video foundation 预测未来 dynamics 用作 policy conditioning 是实际设计分支，重开为潜在贡献（未落窗、不评分）。
- CARE-RAG：QA Repair 纠正过时/歧义答案可能是评价反证信号，定点读 benchmark 错误证据。普通过滤/摘要流程仍不单独足以准入。
- EdgeLoRA：只核 adapter selection 一处核心，若没有区别于成熟机制的具体设计即关闭，不由 4×或 adapter 数倒推。
- TD-MPC-Opt、Agent-as-Tool、Keye-VL 三个关闭理由可以保留。

这不是 DAY 验收，也没有确认任何材料的本窗公开时间。

## 定点补读后的改判（待非作者确认）

CARE-RAG v1 `care-v1.raw` §3 / Tables 1–2、Appendix B.3：作者给出每集随机 1,000 样本人工核查、旧答案/类型不符的具体数及修复前后指标，足以保留“标注时间与 reference set 改变评价”的潜在反证。中心收益还未审阅，且 B.3 有 `[current date/year of dataset repair]`、`using the notation from your paper`、`Please verify this table label` 等残留说明，WikiQA/2Wiki命名不一致，不能直接采纳错误比例或安全可靠性主张。日期未确定，隔离，不给正面性能结论。

EdgeLoRA v1 `edgelora-v1.raw` §3.2 / Algorithm 1、§4.1：不是只做缓存，先由 profile-trained 多标签 router 得 top-k、然后在 top-k 内选已缓存的最高分 adapter；无缓存才加载最高分。这具体改变“只按质量 argmax”到“质量候选集合内按 cache residency”的决策，故原成熟组合关闭撤回，保留质量/换入成本取舍；top-k质量损失及动态adapter扩池边界尚未证明。LRU/LFU正文不一致不能抹掉，宣传4×不采用。

TriVLA由root指出的未来预测状态conditioning作为潜在贡献保留；`trivla-v1.raw`仅作为定点机制恢复原件，不宣称全文审阅完成。

追加 Z.ai GLM-4.1V-Thinking：`glmv-v1-abstract.raw` 是精确v1完整题摘，RLCS curriculum sampling 是需检验的训练条件。2026-10-06T16:54:44Z 定点重核官方 [GLM-V repository](https://github.com/zai-org/GLM-V) Project Updates：`2025/07/01` 同时 released model and technical report，没有官方07/02 release字段。先前07/02线索撤回，不用于本窗归属。官方日历字段没有精确时刻/原始时区，不能确认09:00窗界。该家族不复用当前 GLM-4.5V 的v6摘要，也不因artifact release重复算论文首公开。

此时完整精确 v1 题摘检查31个家族；28个仍有潜在贡献但日期待核，3个关闭。31只指题摘检查集合，不是本日新论文数/候选数，也没有配额。

## 有界查漏后的追加题摘检查

`check-abstracts.raw` 22份精确v1题摘中 REG 与首批重复；仅追加21个家族，完整题摘均已读。由主题列表中的机制/反证标题触发，不是月目录余项逐项关闭。

| 身份 | 具体设计/有效性信号（全部公开时间待核，不评分） |
| --- | --- |
| 2507.01633 Global/Pairwise Scores | 全局分数对稀有严重错误/低置信强模型的偏差，与pairwise大量ties时的比较数量需求，改变评价协议成立条件。 |
| 2507.01955 Vision Understanding | text/API-compatible任务表达的约束、semantic vs geometric能力分离及prompt敏感性，不能由多模态平均分推断几何能力。 |
| 2507.01737 HOI-Dyn | 人驱动/物体响应的耦合模型，以residual dynamics loss缓解预测器错误梯度；训练期辅助而非推理调用。 |
| 2507.01271 PULSE | finetune遗忘成功不能推为pretrain知识遗忘；相同数据批量遗忘与拆成顺序请求的效用可不同，具体反证。 |
| 2507.01496 ReFlex | full inversion与可编辑性冲突，mid-step latent保结构、注入时适配attention，改变inversion深度选择。 |
| 2507.01887 MiCoTA | 直接大teacher长CoT可能不适合小student；中间teacher/中长度轨迹使数据更贴student分布，容量与长度需联验。 |
| 2507.01335 LEDOM | previous-token reverse AR训练与posterior rerank（Reverse Reward），不同于forward likelihood评价。 |
| 2507.01351 LTDR | 语言router均匀而视觉long-tail；视觉尾部激活更多expert，不宜共同load-balance假设。 |
| 2507.01844 Low-Perplexity | 低PPL长生成片段有相当部分未映射训练corpus，反对低PPL等于verbatim recall的解释；须核语料可见性。 |
| 2507.03019 Look-Back | 后期文本占优不必显式重注入视觉；引导模型自身attention回看视觉，需核何时/如何触发与对照。 |
| 2507.02135 FUSE | 独立CPU/GPU/Memory DVFS无法见联合能耗最优点，统一governor改变资源决策；不采速度百分比。 |
| 2507.01654 SPoT | 固定patch grid束缚稀疏token位置；continuous subpixel oracle给上界，不等于已实现低开销routing。 |
| 2507.01723 Spherical Diffusion Policy | 状态、动作和去噪同时进入spherical Fourier space，scene FiLM与temporal U-net保SE(3)等变，而非只输入编码等变。 |
| 2507.02199 Latent CoT | depth recurrent模型的latent CoT解释受layer/probe方法影响，深度增益有限；反对把深度复用直接称为可解释内部CoT。 |
| 2507.01516 Diffusion Loss Comparative Study | 摘要明确不同目标在条件改变时性能发散，以及sample quality与likelihood的目标差别；可改变扩散目标选择的判断，具体条件尚待核验，不能仅因overview关闭。 |

| 身份 | 完整题摘关闭理由（日期不影响处置，不新建日期请求） |
| --- | --- |
| 2507.01643 SAILViT | coarse-to-fine refinement/world knowledge infusion只到方法名称，未说明实际不同的alignment操作或初始化冲突如何消除；广泛benchmark更好不补这个缺项。 |
| 2507.01923 Decision-oriented Text Evaluation | 市场摘要与交易收益的领域协议；摘要没有给出控制混杂后的基础模型机制/评价有效性条件，不能将协作交易获益推广为通用LLM可靠性。 |
| 2507.01908 Reasoning to Edit | hypothetical instruction数据、MLLM guidance+diffusion、FRCE/CME模块命名；题摘没有具体如何取细节/缓解semantic loss的新操作或可证伪边界。 |
| 2507.01255 AIGVE-MACS | 九维标注、未定义的weighted loss/frame sampling及multi-agent refinement组成评价recipe，题摘未给出旧评价失效的具体可验证证据或新机制。 |
| 2507.01843 MoIRA | 成熟外部embedding/LLM router协调既有VLA专家和LoRA部署；题摘未给出路由可靠性或模块性成立条件的新结果，不因无需额外训练、机器人分数或robustness analysis标题准入。 |
| 2507.01785 MuRating | English pairwise labels经translation训练多语rater是具体recipe，但题摘未给translation fidelity/selection bias分析的实际结论，不能由17语言与知识题指标更高认定新有效性条件。 |

## 独立题摘校准收束

root已逐批实际完整读取初始30、GLM v1和追加22（含REG重复），合计52唯一家族题摘独立校准。后续明确PAE的learn nothing、SPRO reward hacking、DaiFu一致性没有正面保证；新增14个信号只是待验证命题，SPoT oracle不证明实用tokenizer。原追加七关闭中Diffusion Loss比较研究由root重开为目标选择有效性线索，无需日期门前再全文；另外六关闭理由可保留，其中finance不是自动排除标签，而是市场收益未改变本项目机制/控制有效性原则。

最终52个独立家族完整精确v1题摘检查、43个潜在贡献日期隔离、9个当前关闭。没有43篇本日论文、没有43篇完成证据审阅，没有全量source召回主张，也没有52篇全文审阅。核心补读仅CARE/EdgeLoRA；TriVLA仅恢复原件并据题摘改判，DAY另行复核。

DAY后停止：root完整读README/FIRST/SOURCE_NOTES与52题摘，定点读CARE §3 Tables1–2/B.3和EdgeLoRA §3.2 Algorithm1/§4.2。EdgeLoRA首页列MobiSys June23–27 2025、DOI10.1145/3711875.3729141；Crossref print June23、online September25、created October2互不等同实际首公开，ACM正文403。可能更早会议正文已公开，恢复该family真实首次公开身份后再判断事件，不把July2 arXiv上传重复记为首公开。此边界已在报告具体保留项补入。root授权本日安全终态通过，不是43项日期或证据通过；停止扩池/考古。
