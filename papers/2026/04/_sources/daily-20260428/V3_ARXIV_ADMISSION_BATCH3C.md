# 04/28 arXiv 贡献准入：第三批后十项

本批是旧 V2.1 `retained` 队列第 81–90 个身份 `2604.24038`～`2604.24300`。已逐项读原始身份 receipt 的完整标题与摘要；后发摘要污染、官方首次公告时刻和章节真实增量都尚须独立核。`继续`/`继续核贡献`是有限审查线索，不是冻结候选。

| ID | 题摘判断 | 当前理由 / 最小消歧 |
| --- | --- | --- |
| 2604.24038 | 前分母关闭 | AgentPulse 把 benchmark、采纳、社区情绪与生态健康聚成产品采用榜；GitHub stars/Stack Overflow 问答和 SWE-bench 排名差异说明它测的是不同对象，不能当 Agent 行为正确性、系统可靠性或部署安全的证据。分析数据集可作行业背景，但不改变本项目 evaluation contract。 |
| 2604.24040 | 继续核贡献 | 等语义 CSV/TSV/HTML/Markdown/DDL 序列化使表检索 embedding 漂移，centroid 与冻结 encoder residual adapter 可能改变 RAG store 的多视图身份合同；需核同表语义等价人工验证、稀疏 lexical 退步、单视图在线开销与 Ch76 现有 source identity/serialization 论点。不能把 centroid 当 canonical truth。 |
| 2604.24074 | 继续 | 固定 judge model 的 12 个 prompt 配置使 HarmBench 有害率移动最高 24.2pp、类别敏感度差异，可能修正“judge 配置只是实现细节”并改变安全验收的 slice。需核 400 behavior×六模型×prompt 的独立样本/人类金标、同 rubric 语义保持与 Ch66 已有 judge-instability 段；不是证明哪一个 prompt 最准确。 |
| 2604.24086 | 继续 | cloud VLA 迟到意图经本地 pose buffer/kinematic transform 对齐，再由 LiDAR 的安全约束作实时裁决，可能补“模型预测与执行时物理状态所有权分离”的长期机制。需核安全约束是否硬保证、定位漂移、网络/设备边界及真实机器人结果，不把 CMDP 解法或零样本称一般安全。 |
| 2604.24088 | 继续核贡献 | TP 中间张量 FP8、Hadamard/dual-scale 和 fused compression 的通信—压缩开销共同优化，可能改 Ch36 的 exact collective 与有损数据传输边界；需核训练 loss 同预算、各分量消融、DP/PP/TP 的端到端配置、是否只在受测 GPU/shape 1.87×。摘要“near-lossless accuracy”不是数值等价保证。 |
| 2604.24118 | 继续核贡献 | “untrusted guest” Agent 与可信 semantic visor 拦 tool call，看似跨 prompt/effect 的执行权限分层；需核 visor 自身是否 LLM、审计协议与外部工具 authority、是否在违规 effect 前强制阻断，与 Ch72 既有 policy-as-data/effect guard 有何新增。0.65% 攻击成功与 1.45% utility 损失只属受测集，不能推出安全证明。 |
| 2604.24198 | 继续核贡献 | 动态数据分析中 PRM 误把探索当错、漏掉 silent error，环境交互 verifier + 反思三值 reward 可能改变 Agent step evaluation 的证据/行动分工；但 ScienceAgentBench 与 8K 合成训练易与 AIforScience 范围混杂。须核 DABench/TableBench 的通用数据分析贡献、verifier 的实际观察权限、真假错误金标与 Ch66/78 现有 witness/verification 机制差异。 |
| 2604.24203 | 继续核贡献 | TEE 内 LLM Auditor 为私有代码提供有限二元问答、硬件根哈希链记录审计轨迹，可改变“执行证明与语义判断”分权；必须核 attestation 覆盖的是代码/数据/模型/提示哪一层，TEE 不保证 Auditor 判断正确，21 artifact/五高层属性样本有限，并与 Ch72/66 既有 witness/evidence 合同比较。 |
| 2604.24273 | 前分母关闭 | BitNet b1.58 权重与 frozen-backbone policy-gradient 的组合声称端侧 1-bit RL，但摘要未标模型/设备/任务/基线能耗测量合同，10–16× 内存与3–5×能效无法归到新增机制；探索稳定性亦只有笼统叙述。当前不能以“Edge RL”名称扩充 AI Infra 候选，若 v1 给出具体新条件再定点重开。 |
| 2604.24300 | 继续 | 视频 VLM 的 QA 标注源自 point-cloud 3D 真值，但实际输入只有16/32/64帧，致可见性/几何错误；重新标注 381 场景并按可见帧预算切片，可能补评价真值与模型实际观察窗口对齐的合同。须核人工复标一致性、问题可答性的 oracle 和 Ch66/23 现有可见性评价是否已完整承载；不把新 benchmark 数量本身当贡献。 |

本批 **3 项继续、5 项继续核贡献、2 项前分母关闭**；八项开放线索仍须按贡献差异剪枝，不自动送全文。
