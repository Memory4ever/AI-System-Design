# `2609.22115v1` — 前向微调的自适应查询复用

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.22115)、[精确 v1 全文](https://arxiv.org/html/2609.22115v1)，访问 2026-09-23；官方 09-22 New 公告落入本窗。HTML 的 08-19 投稿历史不能单独当首次公开；匿名代码入口没有可核的更早公开时刻。
- 问题与旧方案：反向传播可直接拿梯度，是可微且状态预算充足时的优先方案；仅能前向评估时，固定零阶查询预算简单但忽略迭代难度，自适应方案的独立 pilot probe 又会消耗昂贵查询。
- 机制与所有权：保存扰动 seed 与函数 response，跨迭代重建方向并让旧/新查询同时进入候选估计及接受/扩张判据；EMA 方向一致性只是一种条件性可靠度代理。trainer 持有扰动历史、query budget、参数版本和接受决策；历史 response 变陈旧会引入偏差，不能把局部判据称为梯度真值。
- 评价边界：合成测试及黑盒攻击之外，LLM 部分只在 OPT-1.3B/13B 的四组前向微调设置、LoRA、四张 4090、fp16、三 seed 中比较 forward evaluations；43–46% 为相对固定 K=4 的调用节省，不是 wall-clock/显存/通用收敛收益。理论依赖光滑性、噪声和方向一致性条件，不证明非凸大模型训练全局最优。
- Books Decision：`TRAIN-SFT` Ch29 在 full/adapter 更新选择后补 forward-only query budget 分支，保留相同 SFT supervision、BP fallback 和 stale-response 风险。V2 评分 2 + 1 + 2 = 5/9；写后独立复核通过。
