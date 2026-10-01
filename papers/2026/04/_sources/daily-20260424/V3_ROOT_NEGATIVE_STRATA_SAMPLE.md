# 2026-04-24：负侧分层反查（有限样本）

复核日：2026-09-29；独立复核者 root。选择三条**已有具体前分母关闭**且来自不同误收风险的条目：安全术语容易被借用、生产 telemetry 容易被误认 AI Platform 机制、视频生成容易因 Part III 名称被宽收。实际重新打开三份 arXiv exact-v1 的标题/摘要与决定准入的机制段；这些样本不是全部负侧，也不以三条没有误漏证明完整召回。日期只在决定本窗准入时深追；明确贡献前关闭的不为排除它追完整公开史。

- [CSC 2604.21416v1](https://arxiv.org/html/2604.21416v1)：§2.1限定为图像像素输入、离散类别与 classifier head；§4由 early-epoch latent cluster 检出疑似投毒样本，再改虚拟类重训 head。安全问题真实，但其保证与评价只在图像分类器训练管线内建立，未给大模型/多模态生成、LLM 数据资产或推理服务可移交的防护机制。本项目现阶段不能仅靠“数据投毒也重要”类比准入；原具名关闭维持。若未来提供对大模型训练/资产的实际桥接证据，只重开这一族。
- [ARFBench 2604.21199v1](https://arxiv.org/html/2604.21199v1)：750题与真实软件事故 telemetry 是有价值的领域评价资源，但任务是 time-series QA；model–expert best-of-two 使用事后 oracle，并非能部署的独立选择器或 AI System observability/release contract。混合 TSFM/VLM 和内部事件分层没有分离出改变本项目平台设计的具体机制。维持具名贡献前关闭，不把“production incidents”误作 AI 模型生命周期的直接证据。
- [Reshoot-Anything 2604.21776v1](https://arxiv.org/html/2604.21776v1)：单目视频多裁剪轨迹形成 pseudo multi-view triplet，forward-warp anchor 配合扩散模型做动态视频重拍；有局部数据构造/镜头控制贡献。但训练目标是指定 reshooting 任务，遮挡/视角条件并未建立 action-conditioned environment transition、物理状态预测或通用跨模态生成边界。不能因为涉及 4D/DiT 就将其归入本项目 World Model 主线；维持前分母关闭，保留原证据。

三样本覆盖安全、Observability 应用与生成类比，未发现应恢复的直接主线增量。反向抽检范围仍有限：剩余负例需按来源、主题和关闭理由继续审计；一旦发现共享误排理由，只重开受影响组。本文不认证整日准入或 Coverage Gate。

## 第二组：检索、表示、Agent 记忆和工具目录

再次打开以下四份官方 exact-v1 完整题摘，分别检查“与章节名称高度匹配却只有成熟组合”“小模型局部机制是否被不当地一概排除”“已有记忆方案的新应用指标”“模拟工具节约是否足以改变系统合同”。这仍是分层抽样，不是对所有负例的逐项审计。

- [AtomicRAG 2604.20844v1](https://arxiv.org/abs/2604.20844v1)：其原子事实与实体边、个性化 PageRank、relevance filter 针对 chunk 粒度和关系抽取误差；该题摘没有隔离哪项新取证/恢复保证相对现有原子 claim 与图检索分支成立。五个检索基准的作者结果不能自动改变 Ch76 的 evidence/provenance 判断。维持具名贡献前关闭，但不是声称原子化没有实际产品价值。arXiv v1 的 Submitted 为 02/10；这不是 first-public 证明，贡献关闭不依赖本日报日期归属。
- [JEPAMatch 2604.21046v1](https://arxiv.org/abs/2604.21046v1)：确实在 FlexMatch 伪标签目标旁加入 LeJEPA latent regularizer，并在 CIFAR-100、STL-10、Tiny-ImageNet 声称收敛收益；小模型或图像分类本身不是拒绝理由。该题摘没有独立分离可移交到基础模型预训练的几何约束机制、类别失衡有效性条件或改变本书现有表示/训练判断的受控反证，故维持当前项目贡献前关闭。若其具体消融或后续基础模型证据改变这一点，可定点重开，不把当前标题筛选当永久否定。
- [Thinking with Reasoning Skills 2604.21764v1](https://arxiv.org/abs/2604.21764v1)：作者把探索后的推理轨迹摘要存为 skill，检索回新代码/数学题，报告 token 减少和任务准确率提高。题摘没有区分其方案与已有“经验提炼→索引→按题检索”在 freshness、验证、权限或跨任务迁移条件上的新合同；不能用“更省 token”把成熟 Agent memory 技术再作为长期增量计一次。维持具名关闭，若出现独立可靠性/状态有效性实验再恢复。
- [Tool Attention 2604.21816v1](https://arxiv.org/abs/2604.21816v1)：intent–schema embedding、前置范围门控和 lazy schema loading 属于已有工具发现/最小暴露方案的组合。论文自行明确 120-tool/6-server 为模拟，任务成功、延迟、成本、推理质量数字是据 token 计数投影而非真实 Agent 测量；95% schema-token 降低只证明这个受限模拟的传输节省，不独立改变 Ch78/83 的工具权限或完整 schema 验收判断。维持具名关闭；不会把作者投影写成实测性能。

本轮四条均维持具体前分母关闭，没有凭章节映射、好看的指标或小模型标签自动决定；同时查了是否有负结果/评价边界被漏收，暂未见足以改判的受控增量。七条抽样覆盖面仍小于全体负例，尤其未检查机构公告重复、更多理论和安全纠错的关闭组，不能据此宣称整日准入 Gate 已通过。

## 第三组：保护信号、World Model 类比和生产 incident

这三项分别复查官方 exact-v1 的完整题摘及决定准入的必要方法/评价片段，检查是否因安全、代数结构或真实生产字样而误收或误拒。仍是有限抽样。

- [Breaking Bad 2604.20945v1](https://arxiv.org/html/2604.20945v1)：§3 Algorithm 1 在已知 white-box steering/RepE/US 之上，先搜 refusal/gibberish 边界，再在其间网格找 judge 判定的 compliance 最大点；§4 的八模型混合 model family、规模与量化，不能据排序推出“规模越大越脆弱”的单因素结论。它是严肃的保护测试实例，但本次未隔离与旧白盒 steering 不同的权限、作用机制或可迁移发布有效性条件。维持具名前分母关闭；若提供独立的新 threat model 或安全门槛反证，再定点重开，而非把安全材料一概拒绝。
- [Inter-Object Relationships 2604.20925v1](https://arxiv.org/html/2604.20925v1)：§III 沿用 group-homomorphism/variance 约束并增加 object segmentation、相对变换到一维加法 latent；§IV 的追逐/逃避模拟只显示受限关系可读出，没有 action-conditioned transition、真实环境反馈或控制可用性实验。它给世界表示的局部构造实例，但不能因“world structure”措辞推成 World Model 主线的长期状态/因果接口，也不支持它所对比的非交换复杂交互已被解决。维持贡献前关闭，不否定其 representation 研究价值。
- [TingIS 2604.21889v1](https://arxiv.org/abs/2604.21889v1)：题摘中的实时生产量级与 P90/发现率是真实报告的受限部署结果；系统做 customer incident 索引、LLM 辅助事件合并、cascade 业务路由及多维降噪。这里的服务是用 LLM 处理一般企业事件，不是模型训练、推理服务或 AI Platform 的 observability/evaluation contract；未隔离能改变本书 AI 模型生命周期监控设计的新机制。维持前分母关闭，不把“企业级”和生产数字自动计作项目贡献。

本组三项无准入改判。十个负侧样本跨已知检索组合、安全、理论类比、领域 benchmark、Agent 工具、生产应用及生成场景；仍未覆盖所有关闭理由和机构来源。独立日级 Gate 必须继续核源范围、其他负侧理由和正侧反查，不能仅凭十个样本声明全量无遗漏。
