# Apr17 V3：最后九项有限独立语义复核

## 范围与边界

仅复核 14702、14722、14727、14769、14799、14808、14877、14888、14910，使用作者必要原文定位，独立打开 exact-v1 方法与关键反证，比较实际 Books owner。未扩展 536 raw / 88 candidates，未复审已通过批次、遍历附件或核版本史。两项 `2+2+2=6`，七项 `2+1+2=5`，保留作者分值。

PASS 仅表示此单篇限定 source→owner 裁决可用；窄 gap 是待实际写入的提案，不计实际 Integration。没有替代整日 first-public / coverage / denominator / final semantic Gate，亦不宣称 Apr17 Complete。局部正确性反例仅限制相关命题，不否定全文。

| ID | 独立裁决 | Score | 实际 owner / 连接 |
| --- | --- | --- | --- |
| 14702 | PASS — Report Only | 5 | Ch14 `MODEL-SELF-ATTENTION` 为连接 |
| 14722 | PASS — No Change / Existing Coverage，修正百分比口径 | 5 | Ch14 `MODEL-SELF-ATTENTION` |
| 14727 | PASS — Report Only，隔离温度缩放与有限温精确性过述 | 5 | Ch14 `MODEL-SELF-ATTENTION` 为连接 |
| 14769 | PASS — Narrow Gap Proposal | 6 | Ch28 `TRAIN-PRETRAINING` |
| 14799 | PASS — Report Only | 5 | Ch66 `PLATFORM-EVALUATION-SYSTEM` 为连接 |
| 14808 | PASS — Report Only，隔离方向支配过述 | 5 | Ch72 `PLATFORM-SECURITY` 为连接 |
| 14877 | PASS — Narrow Gap Proposal，T 单调需要额外前提 | 6 | Ch66 `PLATFORM-EVALUATION-SYSTEM` |
| 14888 | PASS — No Change / Existing Coverage | 5 | Ch66 `PLATFORM-EVALUATION-SYSTEM` |
| 14910 | PASS — Report Only | 5 | Ch24 / Ch29 为连接，不假称全部接口已有覆盖 |

## 1. 14702：固定 Value 的仿射系数流形不是任意 Attention

[exact-v1](https://arxiv.org/html/2604.14702v1) §2、Theorem 3.1 / 3.5 及 §4：固定 value vectors，系数张成 convex hull 相对内部，unit-covariance Gaussian decoder 下的仿射坐标 metric 确实平坦；multiplicative gate 可以构造曲面族。这个受限对象不等同所有输入变化时 Q/K/V 共同变化的现代 attention，也不证明 gate 是唯一非零曲率来源。

C² function-space 的 genericity 不是有限参数可学习性或优化可达性。§4 的 seq8 / proj64 / 二维 synthetic 任务使用有限差分二阶变化 proxy，原文明确它不是 invariant Riemannian / sectional curvature，不能用该经验相关性证明内在 Gaussian 曲率是任务提升唯一因果。

实际 [Ch14](../../../../../books/part-02-model/14-self-attention.md)把 attention 的条件聚合与执行/门控机制分开。本文有受限几何贡献，但不足把门控升级为通用必要条件；Report Only，不虚写“无机制贡献”，也不把整套理论标为 Existing。未核无关独立证明或复现实验。

## 2. 14722：GPT-2 特定 Sink 电路不能变成普适归因

[exact-v1](https://arxiv.org/html/2604.14722v1) §3.1–3.2.6 / Table 1：query bias bQ、第一层 MLP 形成的 effective absolute-position 成分与 Wk 的协调路径提高首位置 score；null/transplant 与对照支持 GPT2-124M 的特定电路。EPE 是实际 residual contribution 的近似，不是完整 nonlinear 第一层的解析等价。

必须纠正 Table 1 口径：bQ 归零后 BOS attention 为 **.251，baseline .563，保留基线的 44.7%**，不是 absolute attention 44.7%。现象没有消失，所以“必要”只限这个强首-token路径，而非任何 sink 存在的必要条件。300 样本、三域、40 tokens、layers4–11 的 attention 变化不是下游质量；缺少该组件的其他架构仍有 sink，也不代表本文重测了所有架构。

实际 [Ch14](../../../../../books/part-02-model/14-self-attention.md)“Sink 与 Outlier 需要跨 Token、跨深度共同诊断”已经要求逐层 attention/residual 与受控干预对齐，保留结构假设、off-distribution 干预与不同层结论不一致时的回退，并明确不证明每个 sink 同一原因。采用边界真实存在，Existing，不添 GPT-2 案例摘要。

## 3. 14727：零温 Skeleton 与有限温近似不是同一个对象

[exact-v1](https://arxiv.org/html/2604.14727v1) §III-D、IV.3–IV.5、V.2/V.5、VI.1：fixed-context keys 下 top1 零温 query 区域形成 power-diagram 类划分；固定 values 时原输出 piecewise constant，log-lift 又引入依赖 τ 的正值参数，是不同分析对象。全输入 Q/K 耦合已被作者限定，不能把条件 query 区域数称完整 Transformer tight 容量。

有限 τ 的 LSE gradient/Hessian 在给定 logit margin 下可接近极限，不等 cell interior 精确 affine。两 key logistic 在 τ>0 的一般点仍有非零二阶导数。这只限制“exact/严格保持分区”的过述，不否认条件化近似几何。

新增必要纠错：§III-D 写 `softmax(q·k/τ)`，Q/K 是原始投影，却把 standard τ 设为 `1/√dk`；普通 scaled dot-product 对应该表达式的 **τ=√dk**。因此 VI Example 的 dk64、τ=.125 与 e^-16 数值不能直接证明真实 Transformer engineering approximation；除非另行声明已经缩放 Q/K，但该处没有这样的声明。不把此局部错误升级为全部理论失效。

实际 [Ch14](../../../../../books/part-02-model/14-self-attention.md)采用原始 conditional aggregation，不需要吸收未充分成立的容量/有限温工程结论。Report Only，保留假设化理论与上述窄反例，不遍历全部附录。

## 4. 14769：为可复用初始化主动训练 Template

[exact-v1](https://arxiv.org/html/2604.14769v1) §III / Eqs 6–13：预训练时以 Kronecker `W=ΣT⊗S` 间接更新共享 templates 与 size-specific scalers，结构化 prefix masks 暴露 depth/width 变化。目标 shape 先固定 templates，按 width 截断或重复拼接、初始化 scalers，用一小部分数据优化 scalers，再进入无约束普通训练。这不是对任意已有 checkpoint 免费事后分解，也不是零数据迁移或取消目标训练。

有限 ImageNet / ViT、DiT 与 CNN 等实验支持初始化分支，不给任意异构 operator 或 LLM 全规模迁移保证。FID 下降是改善，不应误记负面；预训练、target adaptation 和后续训练成本仍要合计，分钟级 target scaler 成本不能等同统一总预算优势。

实际 [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)受控扩容段已经包含 shape-aware mapping、optimizer moments、activation-scale、new-state reset / asymmetric rewarm 与 rollback，尚缺预先为多目标 shape 训练可复用 templates 的并存分支。

最窄提案紧接既有扩容边界：目标形状不确定且会重复派生时，可把 transfer interface 作为预训练约束主动学习；template artifact、reconstruction、target scalers/data 与解除约束后的训练分别承担状态。新增表达瓶颈、异构 operation 不兼容与校准成本；单目标已知或约束损害能力时，从头训练/常规 checkpoint 迁移仍合理。不新增框架清单，不照录速度数。

## 5. 14799：拒答的收益必须与 Answerable 代价同测

[exact-v1](https://arxiv.org/html/2604.14799v1) §3–6、G.1/G.4、J：2,079 个 MMMU / MMLongBench 派生任务，用 missing / corrupt / contradictory 等 22 类变换、模型/人工 filtering 构造；过滤不等全数据真值。三 VLM、有限 MAS 轮数、self-consistency N10 的 AAC/UAC 要联合看，关键词拒答 extractor 与 heuristic gold 可能误分。

G.4 同 test set 扫 τ 是 oracle upper bound，不是部署时已固定的可靠 controller；human oracle MCC .83 来自引用人类成绩与 UAC 假设计算，不是本文新的人类实测。不能从这些 prompt 对照证明所有 prompting 无效或 abstention-aware training 必然是唯一办法；未知 hardware/precision/SLO 不补猜测。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已有 typed predicates、conditional slices、sensor calibration 与 risk–coverage / abstention 分权。具体 multimodal 数据构造与受限负面结果有贡献，但不足改一般拒答设计结论，Report Only；不是把整个具体 benchmark 偷称 Existing。

## 6. 14808：局部 Retain 方向不等擦除或 Utility 保证

[exact-v1](https://arxiv.org/html/2604.14808v1) §3.3–3.5：module PCGrad 仅负内积冲突时投影；SAGO 同号坐标用 forget gradient，异号坐标用 retain gradient。非负 retain 内积只支持局部一阶方向，在噪声/有限步/非线性 loss 下不保证完整 retained utility，更不能证明参数知识被删除。

原文“同权重 SAGO 总比 PCGrad alignment 更高”不成立：g_r=(1,1)、g_f=(100,.01) 时无冲突，SAGO=(100,.01)，PCGrad=(101,1.01)，后者与 g_r cosine 更大。§3.5 还把仅冲突时投影误写为普遍正交。只隔离 dominance 过述，保留经验优化分支。

WMDP Zephyr7B、RWKU Llama3-8B、50 targets/neighbors、MMLU 和 ROUGE probes 不证明全部旁路知识不可恢复。实际 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)分账 parameter influence、behavioral withholding、relearning 与 retained utility；这条采用边界已有，但不假称 SAGO 更新接口整套已有。Report Only，不从 bio/cyber 安全测试扩展 AI-for-Science 范围。

## 7. 14877：重采样预算与交互深度要正交扫描

[exact-v1](https://arxiv.org/html/2604.14877v1) §2.2–2.4 / §3 / §4.1：同 Qwen2.5-7B policy / deterministic BM25 distractor harness 下，分别扫 k 个独立尝试与每次 T 轮 interaction。200 个同训练题对比 privileged-gold SFT 与 binary-EM GRPO；三类各100测试题，n64、temp .7、T={0,1,2,3,5}。更多浅层重采样不等反馈依赖深层 query，但 64 次未命中不是 policy support 为零；以观测 p=0 的 Bernoulli bootstrap 也不能恢复未见成功。

新增前提修正：§2.4 的 T 单调不是任意 budget-conditioned policy 保证。作者实际每(q,T)独立 rollout，并非同长轨迹截断；Table2 base/B k64 的 T1=.840、T2=.820 也不能作形式单调证明（有限采样噪声不推翻可能有的耦合定理，但该实际合同未提供耦合）。只有策略嵌套、可保持原成功轨迹并允许早停，或比较 best-feasible controller，才可以赋予相应 T 单调含义。

first-success trajectory 交换带 selector conditioning；同训练题不等总 compute 相同，有限结果不证明 exploration 唯一因果或无限 capability expansion。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已有 finite pass@k、interactive 与未命中≠绝不支持，但缺在同 policy/harness 下正交扫 k×T 的具体测量分支。最窄 gap 补 EvalSpec：绑定 seed/selector、horizon-conditioned policy、早停/coupling、每轴与总 token/tool/time 成本；把 budget effect 与 support/causal claim 分开。新增二维测量成本，单次确定性回归仍是低成本基线；不写无限能力保证。

## 8. 14888：已知 Hint Detector 与未知 Modality Attribution 不同

[exact-v1](https://arxiv.org/html/2604.14888v1) §4 / §5.1–5.2：18 模型的 reasoning dynamics 与四 Qwen 变体 hint intervention 分开。MathVerse Vision-Only 只留 baseline-correct>50% 的题，每条件10 generations，统一 Qwen3-VL32B-Instruct monitor。hint-aware monitor 与 image/text attribution 的可见信息不同，会改变排名；长 CoT 流畅不能保证来源 faithful。

hint 的 behavioral total effect 不识别全部内部 causal mechanism，selection 限制外推；training paradigm 对比还含 architecture/recipe 混杂。rewardhack 的弱效应没过 causal threshold 时不给可靠 monitorability 值，不把未测值当零或完美安全。也不照录“训练 reasoning 总能纠错”的普遍结论。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Model Self-report 不能拥有输入来源真值”已经要求 authoritative provenance / controlled cue intervention / self-report 分权，权威来源 owner 与 sensor 明确分开。该采用命题有真实正文承载，Existing；日报保留具体 monitor 视图反证，不另添新排名段。hardware、precision、SLO 无完整合同。

## 9. 14910：Sigma 对齐的轨迹引导仍依赖 Teacher 与 Reward

[exact-v1](https://arxiv.org/html/2604.14910v1) §3.1–3.4 / §4.4：相同初始 noise/prompt 的少步 student 与多步 EMA teacher 按 sigma horizon 对齐，x0 cosine/L2 shaping 与 terminal reward 合用；reward difference 经 stop-gradient sigmoid 调权。相等时 gate=.5、teacher 较差仍非零，不是硬拒绝，也不能照录“只在有益时指导”保证。

有限 FLUX-dev / Wan2.1-T2V1.3B、video BF16 / 400steps / rankbatch1×accum8 与作者不同指标的对照支持受限轨迹适配。额外50步 teacher 是 training 成本；部署不加 teacher 仅相对相同 student schedule，不能当无成本。Table2 作者明确3-NFE ImageReward 低于 SenseFlow，未全面支配；同 reward scorer 上变好也不等独立真实质量或生产 SLO。

实际 [Ch29](../../../../../books/part-04-training-system/29-sft.md) Distillation 已分 alignment 与 utility、teacher cadence 和误差继承，[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)承载连续生成主线，但不假称具体 sigma-horizon/gate 接口完全已有覆盖。本文训练 recipe 暂不足推进通用设计结论，Report Only，保留可迁移机制和受限反证，不新增孤立框架段。

## 结果与后续

本批两个窄 gap（14769、14877）、两个实际 Existing（14722、14888）、五个 Report Only。新增三处必要修正已发作者：14722 absolute attention 与 baseline 保留比例、14727 温度缩放例、14877 T 单调的策略耦合前提。提案须作者实际落实 Books，再经相邻衔接与来源绑定验收；这里只写本独占 audit，不修改 Daily、Books 或全局进度，不代替整日 Gate。
