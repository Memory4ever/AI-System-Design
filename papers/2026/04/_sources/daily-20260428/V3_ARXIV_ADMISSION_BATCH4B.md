# 04/28 arXiv 贡献准入：旧线索第 101–111 项

逐项阅读当日原始身份 receipt 中这 11 项的完整标题与摘要；旧评分/Books 标签无效，摘要可能是后续版本，开放项须官方 exact-v1 复核。只评价当前大模型、多模态/Agent 和 Infra 的长期设计增量；不是大而全的相关性分类。

| ID | 题摘判断 | 具体理由 / 最小后续 |
| --- | --- | --- |
| 2604.24583 | 继续核贡献 | 把 VLM 输出中的图像事实 claim 与视觉证据逐项比较，给幻觉 span token advantage，并在推理时截错续写，可能连接 evidence witness 与训练 credit；需核感知 claim oracle、错 span 标签/GRPO 分母、是否只是既有 PRM/回退在 VLM 场景的组合。不能把检测器分数当视觉真值。 |
| 2604.24622 | 继续 | VLA action 生成由纯 Gaussian 起点改为条件 coarse action-aware endpoint velocity，再一轮局部 refinement，和纯缩短 solver NFE 不同；可能改控制周期中的初始化/修正职责。需核 CALVIN/LIBERO/真机同 NFE、不同预训数据和成功率/尾时延，不能用 75.4% 局部 sampling latency 推全链路。 |
| 2604.24625 | 前分母关闭 | 图像编辑 task/target/理解能力 triplet、五 meta-task 和 CoT-edit consistency reward 属受限训练任务分解；“任何单图操作均可分解”是未证的表达假设，摘要所列 21 编辑任务增益不能隔离出新的多模态系统状态或授权/评价合同。保留数据与任务方法学，不因 CoT 名称入主线。 |
| 2604.24647 | 拟具名前分母关闭（exact-v1 定点核后，待非作者准入校准） | [DepthKV 官方 v1 §4–7/Limitations](https://arxiv.org/html/2604.24647v1) 用单层 KV 剪枝消融及 InfoNCE 表征 proxy 估各层 sensitivity，在固定总 KV 预算下优先保护中层/敏感层；这是真实长上下文 LLM 证据，不因“只是另一种 pruner”拒绝。可是 Ch45 当前正文已明确 per-layer/head 非均匀容量、proxy 非因果、校准状态/漂移回退、逻辑 token 与物理页收益分账；本文的中层保护+InfoNCE 是此合同的受限实现和受测质量对照，没有新增长期状态/控制/验收责任。§7 GovReport 固定结构分配可退步，§9 承认预填阶段一次性、非 query-aware，head 差异未覆盖；不能写成所有层中部恒重要或部署吞吐收益。作者拟具名前关闭，若非作者发现独立重要反证再恢复。 |
| 2604.24657 | 前分母关闭 | AgentWard 的初始化→输入→记忆→决策→执行五层护栏及 OpenClaw 插件原型是现有 Ch72 跨阶段权限/污染传播链的组合，摘要无新的 effect 前强制点、明确独立对照或超出既有 owner 的失效条件。架构蓝图不能凭“lifecycle”命名成为新安全保证。 |
| 2604.24658 | 前分母关闭 | Agent-native research artifact 的逻辑/code/exploration/evidence 四层与自动 review 改善论文复现，是研究工作流和发表容器议题；RE-Bench 五任务的失败轨迹帮助也可能限制作答。它不直接改变当前大模型/Infra 系统机制或本项目 Books 的证据标准，不能把本项目采用的 provenance 原则反向当论文新技术增量。 |
| 2604.24686 | 前分母关闭 | Informational viability 的风险估计/容量余量、KL/z-test/sequential monitor 与 fail-secure pipeline 可作治理概念；作者明确量化实证待后续，P1–P3 “对已归档失败模式充分”是强假设下分类，不证明真实 Agent 的未知风险可界定或 monotonic restriction 可执行。现有 Ch72 sensor→authorization→effect 控制边界已承载该抽象。若 v1 给出实际不变量再定点重开。 |
| 2604.24708 | 继续核贡献 | 多 data-parallel replica 在 fan-out 独立学习率探索、周期参数聚合，再以相对 loss 更新基础 schedule，可能改变“副本必须计算同一梯度”的训练资源合同；但摘要未写模型/规模/非凸参数平均退步和与等 FLOPs sweep 比较。只核官方 v1 是否真有大模型实验和 T 步 merge 的稳定条件；不能因声称 drop-in OneCycleLR 就准入。 |
| 2604.24715 | 继续 | 现有 Transformer checkpoint 经 MLA+Mamba2/Gated DeltaNet 混合和 staged context/distillation upcycling，若以相近训练 tokens 同时保短窗与 2M 推理，可改变 Ch22 的 architecture migration+state ownership；需核 Qwen/Llama 1B/3B 受测对照、10B vs 400B 不等预算、vLLM 实现/质量退步及 90% KV 边界。 |
| 2604.24763 | 继续 | pixel patch embedding 统一视觉理解与生成，不用独立 VAE/representation encoder，可能改 Ch23 表示接口和训练可塑性与早期收敛取舍；需核原始 pixel token 率/算力、同预算 encoder 对照及生成质量/细粒度感知是否共同改进，不能把“encoder 不必要”推广所有规模或任务。 |
| 2604.24764 | 继续核贡献 | Flow-GRPO 用预训 3D/VLM 反馈改善文本→视频几何而不改 backbone，可能补世界模型几何约束与视觉代理真值分离；但纯文本专门数据、外部 3D 模型奖励和周期训练同时变化。须核评测 3D oracle、流动性退步与共同预算；视频几何一致不等物理世界状态可靠。 |

题摘初筛为 **3 项继续、4 项继续核贡献、4 项前分母关闭**；`.24647` pinned-v1/Ch45 定点核后，作者侧暂为 **3 项继续、3 项继续核贡献、5 项拟前分母关闭**。此项待非作者准入校准；旧 `111 retained` 至此仍非冻结候选分母，其他开放线索还须按日期/贡献/必要证据核。
