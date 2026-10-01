# 2026-04-24 四项 Memory、Agent 与 Probe 的有限非作者核

复核者 root。以下对读官方 exact-v1 的必要方法、评价与边界，以及当前 Books owner 的实际命题；只验这四项的准入后处置，不替代本日来源、日期、否定侧和争议项 Gate。

## `2604.21229v1` EngramaBench：Graph 的局部收益不成为默认 Memory 结构

[官方 §3–7 与 Appendix](https://arxiv.org/html/2604.21229v1)将同一 GPT-4o answerer 放在 full-context、Mem0 top-20 和 Engrama 后面，五个合成 persona、100 段对话、150 个 query。Graph 在 cross-space 30 问为 0.6532、full-context 为 0.6291，但全局 composite 分别 0.5367、0.6186；去掉 query planner/typed answer 的消融还呈现局部与总分的反向取舍。相同 answerer 仅固定了末端生成器，不代表 memory extraction、index、prompt 与检索预算相同。文中的美元费用只计 online query，不含写时构建；作者没有披露内部 scoring heuristics，emergent slice 用 token F1。

[Ch77](../../../../../books/part-07-agent/77-memory.md) 已明确先拆 construction/retrieval/answerer，再按关系压力决定是否采用 Graph，并保留 flat/full-context、vector 的成立条件。本文提供有限的 workload 反例而不改变该长期结论；维持 `2+1+2=5`、标准审阅、仅报告。若未来独立数据/预算匹配实验显示跨空间关系持续改变默认策略，再定点重开，不以这 30 问排序写入 Books。

## `2604.21255v1` Tool-use 相似度：轨迹 sensor 不拥有蒸馏来源真值

[官方 §3–5、Limitations](https://arxiv.org/html/2604.21255v1)的 RPS 在共同 stage 比语言行为，AGS 把 tool nodes、顺序和依赖编码成图；所谓 mandatory tool 由所测成功模型的交集定义，不能证明逻辑上必要。18 个模型、英语客服三域相对一个 Claude 参考的相似度，只是该 harness 下的行为关联。受控 teacher trajectory LoRA 实验能显示局部趋近，但不能认证其它封闭模型实际训练来源；论文自己承认缺少有已知蒸馏关系的公开部署模型验证。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已把被测对象、harness、provenance 与行为观察分权。此文新 metric 可以作为受限诊断案例，但若写成“相似即蒸馏”会破坏现有边界；维持 `2+1+2=5`、标准审阅、仅报告。要用于 lineage 认证，需独立训练来源或泄漏证据，不能由 AGS 阈值生成事实。

## `2604.21268v1` GUI CoPC：候选覆盖不等于执行成功

[官方 §4–5、Limitations](https://arxiv.org/html/2604.21268v1)中 proposer 一次给 K 个坐标，标记后由同一 MLLM 的另一 prompt 作 critic 排序；训练奖励分别为候选精度/空间覆盖和 top-1/排序。Oracle@5 是集合内是否命中 GT box，Top-1 才是 critic 选择的坐标；两者都不是 GUI 任务完成或动作授权。Qwen3-VL-4B 的静态权重消融比完整设置低，但只识别该训练配方内的贡献；对照的几何策略使用八次独立生成，不能凭 token 较少推端到端时延。作者承认两段推理比单次回归更慢，密集 UI 中 marker 可能遮挡小目标。

[Ch33](../../../../../books/part-04-training-system/33-grpo.md) 已拥有 group/role credit 与 verifier 身份边界；[Ch78](../../../../../books/part-07-agent/78-tool-calling.md) 区分工具动作的提议和实际提交。该论文只扩展 GUI grounding operating point，不改变通用训练或执行保证；维持 `2+2+2=6`、标准审阅、仅报告。不能把局部 top-1 改善吸收成 Agent 的闭环可靠性定理。

## `2604.21286v1` Energy probe：温度实验是受限比较，不是模型自知

[官方 §2–6](https://arxiv.org/html/2604.21286v1)预注册 TinyConv 2.1M、CIFAR-10、10 paired seeds，对比 CE/MSE/bPC 条件下的 energy probe 与 softmax AUROC2。预设的 latent movement 操作检查未达到 10 倍，故 bPC 相对优势不能归因于双向 settling。作者按向量 logits 缩放后重算 softmax margin，AUROC 从 0.841 到 0.789；这不是对原 scalar score 作单调变换，因此不违反 AUROC 排名不变性，但“66% 由 logit scale 因果解释”仍仅是本组温度干预的描述分解。bPC 的 +0.008 很小，且同时改变输出目标和动力学。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求比较时固定 scorer、输出条件与 calibration identity。本实验是一项窄的 baseline 公平性警告；它没有建立 LLM 内部置信度读取方法。维持 `2+1+2=5`、标准审阅、仅报告；不写 Books，也不把作者理论解释升格为通用 CE 结论。

四项当前均不改 Books；本日仍有其他候选与日级 Gate 待办。
