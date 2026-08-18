# Lab 01 — Learning from Data

## Lab Question

模型怎样通过 objective 和 gradient 从有限数据中形成可泛化行为，而不是记住训练样本？

## Why This Lab Exists

手写规则在边界稳定、特征明确时可解释且可靠；当输入组合扩大时，规则维护转化为 representation 与 search 问题。
学习参数解决特征组合，却引入 data distribution、objective mismatch、optimization 与 generalization failure。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `WORLDVIEW-WHY-MODELS-LEARN` | Ch4 | 学习与 optimization 原理 |
| `WORLDVIEW-REPRESENTATION` | Ch5 | 表示与可分性 |
| `TRAIN-DATA` | Ch27 | 数据身份、split 与质量 |
| `TRAIN-PRETRAINING` | Ch28 | objective 如何生产能力 prior |

## Prerequisites

- 完成 Lab 00。
- 理解向量、矩阵乘法、导数、loss 与 train/validation/test split。

## System Under Test

一个可控的合成分类或回归问题；规则、线性模型与小型 MLP 消费相同数据合同。训练循环拥有 parameter update，
evaluation split 拥有泛化判断。

## Baseline

先实现显式规则或线性边界。它在生成分布与规则匹配时仍是低成本、可审计方案。

## Step-by-Step Experiments

1. 构造能控制 noise、class balance、spurious feature 与 distribution shift 的数据生成器。
2. 对照手写规则、线性模型与 MLP，固定 split 和 parameter budget。
3. 手工展开一次 forward、loss、backward 与 update，再与 PyTorch autograd 对齐。
4. 改变 width、depth、learning rate 和 data size，绘制 train/validation gap。
5. 注入 label noise、spurious correlation 与 OOD shift，比较模型信心和真实错误。
6. 保存 model/data/objective identity，说明哪种能力来自 representation、data 还是 optimization。

## Expected Artifacts

- 可控数据生成器、最小训练循环、reference gradient test 和 learning curves。
- 一个带 data/objective/parameter identity 的小 checkpoint，供 Lab 02 复用实验纪律。

## Invariants

- Train/validation/test 数据不泄漏。
- 手工 gradient 与 autograd 在 tolerance 内一致。
- 每次比较只改变声明的变量，parameter/data budget 可追溯。

## Failure Injection

- 翻转标签、改变 class prior、删除关键 feature、让 spurious feature 在 test 反向。
- 使用过大 learning rate 或错误 normalization，观察 loss 与 gradient failure。

## Measurements

- Train/validation/test loss、accuracy、calibration、gradient norm、sample efficiency。
- 参数量、step time、memory，以及 shift 前后的性能差。

## Acceptance Criteria

- [ ] 手工 update 与 autograd 结果对齐。
- [ ] 能定位 underfit、overfit、optimization failure 和 distribution shift 的不同证据。
- [ ] 至少展示一个训练指标改善但测试能力下降的反例。
- [ ] 报告说明规则、线性模型和 MLP 各自成立条件。

## Trade-offs and Alternatives

更大模型提高表示能力，也扩大数据需求、optimization surface 与不可解释性。规则在约束稳定、安全边界明确时继续
成立；线性模型在表示已足够时比深网络更容易校准和维护。

## Reflection Questions

1. 模型“学到特征”和“记住样本”怎样通过实验区分？
2. Objective 与真正任务不一致时，扩大模型能解决问题吗？
3. 哪些错误应归 data owner，哪些应归 optimizer/model owner？

## Next Lab Handoff

向 Lab 02 交付训练循环、data split、checkpoint identity 和 gradient correctness 习惯；下一步把标量/固定向量输入
扩展为离散 token sequence。

