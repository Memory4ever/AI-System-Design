# `2609.22170v1` — 单模型重复偏好比较的聚合边界

- 来源：[arXiv v1 全文](https://arxiv.org/html/2609.22170v1)；访问：2026-09-23。官方 `cs.LG /new` 2026-09-22 公告批次归入本日报的 2026-09-23 08:00 北京时间事件。摘要页的 `Submitted`/v1 字段为 2026-08-26，不把该字段冒充公开时间；若取得更早公开正文的作者材料，应回拨真实 owner。
- 拟改变的判断：Ch66 已要求校准 judge 的 pairwise 比较，并按语言、领域或人群切片保留异质性；但**固定同一模型**的重复选择也可能呈结构化非传递性。只给一个 aggregate Bradley–Terry/Elo score，可能把这种行为异质性当作独立噪声。Ch31 的人类 rater 分群是相邻类比，不等同于已证明模型内部存在多个偏好电路。
- 机制：作者在固定模型、候选集上重复做 pairwise forced choices，交换选项次序、prompt wording 与伪标签；用 strong stochastic transitivity 缺口检验单一随机效用排序。其 noise-augmented mixture Bradley–Terry 为每次比较引入潜在成分、各成分的 item score/随机选择率，并从观测到的 win/loss 拟合混合权重。组件是**行为统计模型**，不是可直接定位的模型内部状态。
- 评价：七个 open-weight LLM、四组各 50 个 item 的价值与事实判断任务；每个 unordered pair 在多种 prompt 与两种展示顺序下重复采样。五折交叉验证按 item pair 整组留出，比较单一 BT、带噪单一 BT 与最多五成分的 mixture；后者在多数模型/任务组合的 held-out pairwise MSE 持平或更好，价值困境与困难事实任务更明显。固定 prompt/order 控制不能消除观测到的非传递性。这里只采用“单一聚合排序可能漏掉可预测的行为结构”，不把作者模型优越性或 `k_eff` 当作普遍定律。
- 关键反证/限制：§9 明确相关噪声尚未与混合偏好识别开；推断成分缺独立验证，部分 HMC 拟合不收敛；模型形式和最多五成分的先验可能影响分解，样本只覆盖所测模型、50-item 集与强制二选一协议。不能宣称模型有真实多个内部价值系统，也不能直接推导 RLHF 应采用 mixture reward。需要重复采样、配置与成分稳定性/外部行为验证后，才可能升级发布决策。
- Books Decision：`PLATFORM-EVALUATION-SYSTEM` Ch66，在现有 judge ranking 与跨群体切片之间加入固定模型重复选择的有界诊断；旧单一排序在重复选择近单峰、条件稳定且误差校准有效时仍成立。训练侧 `TRAIN-RLHF` 只作相邻关联，不重复拥有评测机制。
