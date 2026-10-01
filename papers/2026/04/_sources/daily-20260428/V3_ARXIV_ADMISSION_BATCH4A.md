# 04/28 arXiv 贡献准入：旧线索第 91–100 项

只读当日原始身份 receipt 中这十项的完整标题与摘要；旧 V2.1 `/9` 和 Books 标签不作准入。题摘能判清的具体关闭，不强制全文；潜在项只做必要 exact-v1 贡献消歧，仍非冻结候选。

| ID | 题摘判断 | 具体理由 / 最小后续 |
| --- | --- | --- |
| 2604.24320 | 继续核贡献 | 同一 Agent 每步并行交互多个环境、跨轨迹共享经验、用 diverse-action/state-transition reward 惩罚冗余，可能改变 rollout 样本/环境所有权；但 ALFWorld+ScienceWorld 与“效率相当”未说明等量交互数/环境成本。核 RL objective 是否仅重命名并行探索、SFT 训练责任及 Ch33 现有多 rollout 机制差异。 |
| 2604.24348 | 前分母关闭 | OS-SPEAR 将 safety/performance/latency/token/视觉文本扰动分为四子集并排序22个 OS Agent；摘要报告的效率—安全取舍没有同一机会集或受控预算，更多是已有 Ch66 多维评价原则的 GUI 实例，未提出新的动作后 outcome/effect witness。保留具体诊断，不因排名数量准入。 |
| 2604.24351 | 前分母关闭 | Template model/cache/pipeline 对扩散控制能力做统一插件接口，列 KV cache 与 LoRA 载体和十类模型 zoo；摘要未证明两载体在训练、版本、compose 冲突/失效上的共同 contract，也无受控工程代价，当前属软件封装与产品组合，不能自动扩大长期多模态生成知识树。 |
| 2604.24432 | 继续 | KSA 把长历史压为可学习 summary token，在 full attention KV 随长度线性增长与完全状态压缩之间取可解释 `O(n/k)` 点，可能改变 Ch22/45 的历史状态所有权。摘要是简短技术报告概述，须核 exact attention 路由、训练/推理更新、远距检索退步、同内存预算与现有 summary-memory 机制区别。 |
| 2604.24441 | 拟具名前分母关闭（exact-v1 定点核后，待非作者准入校准） | [官方 v1 §3.3–3.5、§4、Limitations](https://arxiv.org/html/2604.24441v1)：2,753 道题来自现有 GUI screenshot，region/element grounding 问框坐标，captioning 是“若点击会怎样”的静态多选；功能/选项由 VLM 提议、人工校框与复核，不以真实点击后环境 state/effect receipt 作动态真值。作者也承认只覆盖单步功能描述，未测能力如何影响长期规划。Ch66 的 GUI Workflow/branch evaluation 已把 perception、predicate、path-state、已观察 effect 与最终 outcome 分账；本稿增加的是六 OS 的局部功能理解题库和 hard negatives，不能替代 effect witness，也未给新的长期评价权责或与端到端成功的受控联系。保留 grounding 与功能推断可分离的领域诊断，不因 benchmark 数量或“动态状态预测”标题自动准入；若非作者发现 Ch66 缺此独立分母再重开。 |
| 2604.24447 | 继续 | VLA 在异构 edge 加速器上 VLM backbone 计算密集、Action Expert 内存密集的两相瓶颈，DP-cache/异步 fusion 改控制周期资源分配，可能改变机器人推理 phase 与硬件映射。需核 model-hardware pair、精度、控制率/成功率、实际 NPU/GPU 指标及 Ch49/25 相邻 owner，2.9×/6×仅在受测配置。 |
| 2604.24477 | 前分母关闭 | GAMMAF 合成多 Agent debate 图轨迹再评 graph anomaly detector，本身声明非新防御；MMLU-Pro/GSM8K 上早隔离恶意节点节省 token 属其模拟拓扑/基线情境，不证明真实 Agent 的可执行 effect authority 或通用安全收益。可作 Discovery/benchmark 背景，不作新安全机制。 |
| 2604.24479 | 前分母关闭 | 可执行 CAD 历史合成、百万序列和 CAD 重建是领域数据/应用能力；原始 B-Rep 缺过程历史的确有领域价值，但当前 AI-System-Design 暂停 AIforScience，且题摘无通用训练数据 ownership 或 Agent 执行验证新反例。 |
| 2604.24542 | 继续核贡献 | 不需 clean reference model/trigger/权重更新，仅以层间隐态差异 shrinkage Mahalanobis 和 200 clean 样本阈值监控多种攻击，可能补 Ch72 safety sensor 的 artifact 可观测性边界；需核 12–16% FPR、clean 校准集与攻击机会集、实际阻断是否由 detector 外部完成，不能把检测率叫防护保证。 |
| 2604.24579 | 继续核贡献 | Agent trace 拟合吸收 DTMC，将 pass@k/pass^k/RDC 归一到首次成功时间分布并给可信区间/拟合检验，可能改变 Ch66 的长期可靠性 estimand；需核状态聚类是否使用结果泄漏、50/50 fit/test、KS p>0.05 只是未拒绝而非链为真、与现有 trajectory/outcome protocol 的差异。 |

题摘初筛为 **2 继续、4 继续核贡献、4 前分母关闭**；对 `.24441` 做上述 pinned-v1/Ch66 定点核后，作者侧暂为 **2 继续、3 继续核贡献、5 拟前分母关闭**。本次改判待非作者准入校准，不冻结全日分母；其余五个开放线索仍须必要原文与 owner 对照。
