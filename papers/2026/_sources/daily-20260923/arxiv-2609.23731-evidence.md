# `2609.23731v1` — 模块边际校准不等于组合风险校准

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.23731)、[精确 v1 全文](https://arxiv.org/html/2609.23731v1)，访问 2026-09-23；官方 09-22 New 公告归本窗，09-20 投稿标记不单独证明首公。
- 问题与旧方案：分别验收位置和速度估计使模块可独立开发；若 planner 使用两者组合的未来位置，边际校准不能识别误差相关性。
- 机制与状态：`p_H=p+H v` 的误差方差含 `2H Cov(e_p,e_v)`；接口只给两项方差时，两个同边际但不同 coupling 的系统会给不同 future risk。估计 owner 要发布联合协方差或未知相关上界，规划器消费组合分布，safety controller 仍拥有行动提交。独立假设简单但可能错误；joint estimate 需校准样本，robust bound 会变保守。
- 评价边界：受控 crossing 模拟固定 position/velocity 边际 95% 校准，只变相关结构，独立接口的 future coverage 可落到 86.46% 或升到 99.98%；300,000 held-out 预测样本和 30,000 闭环 trials 是模拟，不是硬件安全认证。joint covariance 是已有方法，论文贡献是接口缺口与后果，不是新 fusion 算法。
- Books Decision：`MULTIMODAL-EMBODIED-VLA` Ch26 原有校准与控制分权，但未指出边际置信区间合成的依赖缺口，已在坐标/传感器接口之后补系统级复核。V2 评分 2 + 2 + 2 = 6/9；独立写后复核通过。
