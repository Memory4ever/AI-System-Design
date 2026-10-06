# 12222 HiAP：独立必要 Source / 预算争议复核

复核者：mar13_admission_review（非准备者；本项仅处理 03-14 补充窗口 2026-03-13，北京时间自然日）。2026-10-10。

## 范围与身份

恢复时实际重读 AGENTS、当前 Research / Report / Prompt、Sources 使用说明与 Daily / arXiv 范围、ROADMAP、LEARNING_STATE 本日路由及本日 README 开头停点。原窗口、原候选和原 §4 前缀不动；本 ID 已有效的题摘准入和日级日期独核复用，不重新由 submitted 推公开日，也不引入其他日期材料。

先读准备者 [必要证据包](./SUP_EVIDENCE_12222.md)，再实际回读 [exact-v1 原 HTML](./SUP_NECESSARY_12222.raw) 的 §3–4（直接解析原件正文及 MathML alttext，非仅提案摘要），并读其 [文本投影](./SUP_NECESSARY_12222.txt) 325–1545 中核心方法、完整 Proposition 2 与 proof、§5.1–5.4 / Tables 2–3 和 §6 直接限制。Appendix B 必要成本分解已读至显式求和式与期望步骤；没有扩读全部附录、图像、代码或 v1/v3 diff。

[manifest](./SUP_STOP_GATE_MANIFEST_RESULT.json) 记录 exact URL `https://arxiv.org/html/2603.12222v1`，GET 200 / 198650 bytes，检查时间 2026-10-10T02:27:13.855359+00:00；ABS exact-v1 同为 200 / 42838 bytes。实际 [ABS 原件投影](./SUP_ABS_12222.txt) 显示标题 *HiAP: A Multi-Granular Stochastic Auto-Pruning Framework for Vision Transformers*、四名具名作者及 v1/v2/v3 history；View PDF 副文却写 Andy Li 与另两人，保留此显示差异，不据副文改写作者数。可见 Comments 没有撤回/纠错文字；latest v3 信号已见，但本项不采用 v3 机制或吞吐宣传，不声称完成全部版本审查。

## 必要原证判断

**实际增量仍成立为待证贡献，评分 2+1+2=5 合理。** 单粒度剪枝及事后恢复难以联合分配结构 → 宏 head/FFN 与微 value 维度/neuron 门共同训练，拆宏固定与微联合门成本并导出静态子网 → 需要核实软训练预算如何交接到硬结构。Design Delta 2 只计这一组合的预算/结构接口与所声称有效边界，System Reach 1 是局部 ViT 组件，Durability 2 是可复用的软/硬交接约束；不借 Gumbel、STE、残差或成熟期望线性性抬分。中心主张出现直接反证，因此必要受影响内容已深入，不能为了争议或 Books0 降分缩池。

Eq5 / Proposition 1 的线性期望身份在声明的成本账本内成立：联合变量包括 `g`、`g*d`、`b*c`，并不要求各门独立。Eq3 明确只在 V-path 乘微门，QK logits 仍使用原 head dimension；§3.4 却说物理导出同时截断 Q/K/V。因此不能由该训练式认证导出算子与原 masked 算子等价。Appendix B 用 `w_attn*g*d` 简写成本，未显式保留 Eq5 的独立 head 固定项 C1；这不否定期望线性性，但不能把两个账本静默视为同一物理成本。

Eq7 是 task / KD 加宏微期望成本罚项；原文明确不用 global squared-error budget target。Eq8 的有限 ReLU 罚项也不是硬约束投影或可认证预算求解器。可以描述实际损失和作者局部结果，不能由罚项本身签发所有训练轨迹均满足 quota、任意 C_target 可达或无结构塌缩保证。

## Proposition 2：独立反例及精确限定

原文 Prop2 把温度趋零、variance collapses、期望成本趋于硬化成本以及固定 0.5 接近 C_target 连起来；proof 未补训练 logit 饱和、噪声消失或预算修复条件。**二值化不等于跨采样方差归零。** 按 Eq6 的标准 Logistic 噪声与固定有限 `α=log(3)`，

```text
zhat_tau = sigmoid((α+ε)/τ)
tau -> 0: zhat_tau -> 1{α+ε>0}
P(z=1)=sigmoid(α)=3/4; Var(z)=3/16.
```

这反驳“只靠温度退火即可方差塌缩”的充分条件，不是声称实际训练中所有 logit 必然有限。若作者另将 variance collapse 作为额外假设，而非退火结论，该假设也须另证；而从硬/软成本对齐到 **C_target** 仍缺优化解、误差或 repair 桥接，因为 Eq7 没有目标预算项或给出 λ 与该目标的保证关系。

按 Prop2 明写的 **gate probabilities** 固定阈值读法，考虑固定打开的父结构内十个同价微单元，均取上述 α；共同固定开销可从软、硬两侧同时扣除。零温期望微成本为 7.5 个单位，概率均 >0.5 的确定性硬化保留十个，差 2.5；单元成本步长为 1，最近可达整数 7 或 8 仅离目标 0.5。因此该差额不只离散量化误差。此为分析反例，非实验复现、非代码执行检查，也不否定存在其他训练轨迹能满足预算。

对提案有两处最小准确修正：原命题只写 **small tolerance**，不强化成原文保证“任意小 ε”；§3.4 记 `zhat>0.5`，但 Eq6 的同一符号是随机样本，究竟在导出时去噪、取 sigmoid(α) 还是如何取样未明确。上述十单元例严格对应 Prop2 的概率阈值读法，不冒充已核实现。若仍以 noisy sample 硬化，它可以导出某个采样结构，但温度本身同样不消除结构随机性或提供每次硬预算保证。

## 保留的评价与反侧

Table2：ImageNet-1K / DeiT-Small，dense 4.6G / 79.85，HiAP 3.1G / 79.10 或 2.5G / 77.95。3.1G 的 S2ViT / ViT-Slim 分别为 79.22 / 79.90，GOHSP 3.0G 为 79.98；不能称统一 Pareto 支配或无损。表头 FLOPs、正文 MACs 的原口径保留，不自行换算。

Table3：CIFAR-10 / 定制六层 ViT-Tiny，同附近 MACs 下 HiAP 的 87.56 / 87.25 高于所列均匀或 l1 对照；这些是局部作者实验，可保留而不替代理论。§5.4 报 batch1 / 50 inference runs 的 5.57→3.86ms，GPU 型号和 precision **Not Disclosed**，不授跨硬件速度或端到端训练费用节省。§5.1 ImageNet 为 200 epochs、batch256、AdamW 5e-5、dense DeiT-Small KD teacher（αKD=.7，T=4）；温度实际 2→.5，不是已经执行 τ→0。匹配总训练开销、重复 seed 与不确定性未披露。§6 本人明确 expected MACs 目标不等于已校准 latency / energy，kernel/hardware 会改变收益；受测点达到某预算不能验证 Prop2 对所有目标或配置的保证。

## Owner 与受限终态

实际顺读 [Ch17](../../../../../books/part-02-model/17-transformer-layer.md) 开头至 175 的问题、Residual / Norm、完整 shape 流邻接，并读 Ch16/18 入口：MODEL-TRANSFORMER-LAYER 能承载宏微结构及 residual shape 约束，但 identity 路径不认证删除后的质量或预算；没有因主题相似授具体 NC。[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 核心问题与执行计划入口，以及静态 shape / adapter 局部说明的是经过验证模型语义的执行交接，不接管本稿训练剪枝发明，也不代预算证明。

**独立裁决：必要 Source 复核通过其受限描述与反证；2+1+2=5，中心预算保证争议 / 暂缓，Books0。** 不是强保证通过，不称所有论文/实验无效，也不是具体已有覆盖或贡献 EX。只保留联合门 recipe、有效线性期望身份与绑定配置的作者实验；Prop2、全 quota 保证、V-only 到 QKV 删除的语义同一及精确硬预算结论均隔离，不作为 Books 正面证据。

重开仅需官方明确的 Prop2 条件/更正，或精确停噪与硬化规则、可达目标与预算 repair / 误差界，以及训练账本与导出算子一致性证据；回到 Eq3/6/7、§3.4 和 Prop2 定点核。当前没有 Books proposal / 写锁，不授 PRE、实际 POST 或 DAY；本有限单项到此停止。
