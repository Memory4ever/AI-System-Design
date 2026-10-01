# 2604.24809v1 Nautile-370M：谱状态的受限机制与印刷定理核

本项原在旧 60 完整题摘的潜在线索中；以下是 **作者侧**必要原文核，不新增 `106=69 潜在+37 前闭` 工作题摘，不签首公开或日 Gate。官方 [exact-v1 HTML](https://arxiv.org/html/2604.24809v1) §2.1–2.3/Theorem 1/Corollary 3–4/Algorithm 1、§4.1–4.5/Table 1、§5/Table 2、§6；[v1 身份页](https://arxiv.org/abs/2604.24809v1)。HTML 页眉 `27 Apr 2026` 与论文内印 `August 24, 2026` 冲突；页内日期只作不可靠排版字段，首公开依本日 checkpoint 的官方公告/边界 ID/DOI 代理**联合批次链**另核，不能由 v1 submitted 或页内 August 孤证。

## 项目关系与有效机制

论文研究的是 LLM 核心 sequence operator，并非因为模型只有 371M 就排除。SCA 让历史 token 的复数相位/值经正权重与有限 `K×M=16×2=32` 谱位置累加，query 从固定维状态读出；训练可作 causal prefix scan，推理更新长度不随前缀增长。每三层保留一层显式 Transformer attention，是对固定状态难以精确选择旧 token 的可核 fallback。若能在匹配训练成本与检索质量下成立，它会改变 Ch17/22 对 recurrent state 与 attention 的容量—执行取舍；但作者 §2.3 明说 `2:1` 是资源限制下依前人经验选取、未做 ratio 消融，不能把比例或“全部可检索”写成通用架构处方。`O(1)` 指每步 state update 对历史长度的阶数，不是零算力、总体训练 wall-clock 或任意上下文精确读回。

## 中央印刷“精确检索”证明的最小反例

§2.2.2 Theorem 1 定义 `S(θ)=(i/t)∑h_k exp(i〈θ,h_k〉)`，对目标 `j` 取 `w_j(θ)=it/(2π)^d exp(i〈θ,h_j〉)`，声称在 `L²(R^d)` 做 Hermitian 内积即精确得到 `h_j`。取最小 `d=t=1, h_1=1`：`S(θ)=i exp(iθ)`、`conj(w_1)=−i/(2π) exp(−iθ)`，乘积对每个实数 `θ` 都是常数 `1/(2π)`；`∫_R 1/(2π)dθ` **发散**，不等于 `h_1=1`。两纯指数也不属于 `L²(R)`，不能把所写积分当通常 Hilbert 内积。印刷推导以 Fourier 的**分布**恒等式得到 `δ(h_k−h_j)`，但在 `k=j` 处这是 `δ(0)`，不是可直接替换成有限 `1` 的 Kronecker 指示。若想用频域体积归一化/平均或核正则化取极限，须重新给出归一化和误差条件；那不是当前印刷 Theorem 1。这个反例不声称所有特征函数表示都不能编码原分布，也不声称实测模型代码崩溃；只隔离本文所写“该 L² query 精确检索”的证明与由其推出的无条件 softmax 替代保证。

另一个独立限制是 `w_j` 的构造直接包含欲检索的 `h_j`，所以即使修好积分，也没有展示未知未来 query 如何按**位置 `j`**从压缩前缀生成该 query。Corollary 4 再令 `w=∑α_kw_k`，但 `α_k` 是已选定的任意系数，并未证明当前 token 从固定大小状态无需访问旧 K/V 就可构造 softmax 的 query-dependent `α_k`。标准 attention 的 `V_k` 也可以与输入 embedding `h_k` 不同。§2.2.3 自己承认实际每 head 仅两谱点，在 `t≫K×M` 时不能复现任意 convex combination；§2.3 以周期性 attention 层补精确 pairwise route。故上述理论保证不能迁移给有限实现，连连续印刷证明本身也须修正。

## 评价边界与实际 owner

§4 Table 1 是**累积**三阶段单模型链：SFT 后 GSM8K `27.98`，Dr.GRPO `28.96`，gradient-balanced GRPO `31.36`，scored self-distillation `33.43`，不能把末值单因果归于 SCA 或单独 GRPO。作者承认 Stage3 的“正确轨迹再训练”与已有 STaR 核心机制相同；§4.1 的“72% 错误 ⇒ 负 advantage 梯度必主导”也不是仅由样本比例推出，组内 reward 全零会给全零 relative advantage，梯度大小还取决于 log-prob gradient。§5 Table 2 与同尺寸模型的训练 token 数从约 `0.8T` 到 `28T` 不匹配且多任务有退步（如 MATH500 `2.4` 对 Qwen2.5 `18.8`），不识别谱层的独立效应或长上下文收益；该模型 context=1024，无长前缀精确回读实验证据。

`ROADMAP.md` 的 `MODEL-SELF-ATTENTION`→[Ch14](../../../../../books/part-02-model/14-self-attention.md) 保留 Q/K/V 各异与内容路由，`MODEL-TRANSFORMER-LAYER`→[Ch17](../../../../../books/part-02-model/17-transformer-layer.md) 已区分有限 recurrent/basis state 与完整 KV 的精确 recall，[Ch22](../../../../../books/part-02-model/22-long-context.md) 已要求在质量、训练成本、服务状态三者上验证 hybrid 比例。作者侧拟 `Design Delta 3 + System Reach 2 + Durability 3 = 8/9`、`Deep`，对 Theorem 1→Corollary 4 的**中央表达性保证**作窄 `Disputed`；其实际有限谱＋周期性 attention 的设计和受限 benchmark 可保留，但不能自动成为 Books 正面机制。Ch14/17/22 的现有有限容量命题足以防错误采用，Books 暂缓；需非作者定点复核上述 `d=t=1` 反例、真实 owner 与任何未读正则化前提。重开材料为给定归一化/空间的严格定理、从可用 query 到输出的构造及有限 `M` 下精度—成本实测，不要求整篇附件或完整实现复现。
