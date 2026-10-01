# 2604.22778v1 的受限贡献准入（作者侧）

仅为旧 111 中的开放线索作决定性原文→当前 owner 对读，不是日期 Gate、评分、完整 Evidence Review、Books 写前授权或正式分母。窗口仍为北京时间 `[2026-04-27 09:00, 2026-04-28 09:00)`；官方 v1 页眉 `03 Apr` 为稿件/投稿字段，不单独证明首公开。

[官方 exact-v1](https://arxiv.org/html/2604.22778v1) §3–4 把训练中权重矩阵的 stable rank 与幂律谱指数 α 分开：前者出现随深度传播且会反转的短期压缩，后者形成较持久的分层谱形；Q/K 与 V/O 的轨迹也不同。这是真实的**诊断对象差异**，不能把“rank 低”直接当作某层可删、某训练阶段已收敛。§7.2 在 GPT-2/Pythia 的有限层删除实验中，α/边界保护的排序有时胜 Last-N，说明位置启发式不能独占剪枝提案；但 Table 5 的 GPT-2 Medium 删 4 层时，谱排序 ΔPPL +9.65 虽好于 Last-N +25.06，却差于 Random +5.62，非普遍最佳。§7.3 的随机奇异向量、目标奇异值初始化只在 D8/5K step 出现 val loss 5.307 vs 常规 3.720，不能由此断言所有模型的信息“绝大多数”都由方向承载。§8 还披露 D8 层重要性相关 p=.11、D16 未达到计划的 10K step、完整 SVD 不能直接扩到多十亿参数。

[Ch28](../../../../../books/part-04-training-system/28-pretraining.md) 当前训练诊断段已有 activation covariance 与 per-sample **gradient** spectrum 的风险传感器身份，未等价表达训练期 **weight** stable-rank transient 与 α shape persistent 的不同读数；[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的稀疏/剪枝段已有重构损失、经验 Fisher、结构化 artifact 和 runtime kernel 验收，不自动保证 α 排序可部署。因此作者侧保留一个受限候选线索：权重谱可提出离线层删除的另一个代理，必须以同等层数、相同 checkpoint/预算下的质量与完整执行收益验收，不能让谱指标持有提交剪枝或停训权。是否足以改变 Ch28 诊断选择、还是只作论文证据/Only，待非作者按上述 GPT-2 Random 反例定点校准。暂不写 Books、不评分、不把旧 8 分继承为本日判断。
