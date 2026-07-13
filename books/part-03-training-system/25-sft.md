# 第25章 SFT

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 监督微调如何把通用模型对齐到指令、任务和业务风格。

## 本章要回答的问题

Pretraining 已经让模型能够续写文本，为什么它仍可能不遵循指令、模仿错误角色或输出不合适的格式？Supervised Fine-Tuning 怎样用 demonstrations 改变条件分布？为什么 SFT 仍然使用 cross-entropy，却能显著改变模型行为？

本章的核心判断是：**SFT 用高质量 `(instruction, response)` demonstrations 重新加权模型的条件生成行为，使“用户请求后应该怎样回答”成为训练分布中的高概率模式。**它主要教模型模仿目标行为，不等于证明回答正确，也不能表达所有相对偏好。

本章使用 `x` 表示 prompt/context，`y=(y_1,...,y_T)` 表示目标 response，`theta` 表示待更新参数，`m_t` 表示第 `t` 个位置是否参与 loss，`B` 表示 batch size，`V` 表示 vocabulary size。

## Pretraining 接口为什么不等于产品接口

预训练数据中可能同时出现：

- 问题与正确答案。
- 问题与错误答案。
- 多人争论、引用和角色切换。
- 网页导航、广告、代码、日志与模板。
- 对指令的描述，而不是对指令的执行。

模型学到的是这些文本条件关系。用户输入“请总结这段文档”时，pretrained model 可能继续讨论“总结”这个词，也可能模仿网页结构，而不是稳定输出目标摘要。

一种朴素解法是只靠 prompt engineering，把每个产品规则写进 system prompt。Prompt 可以选择和组合已有行为，却无法保证所有目标行为在模型分布中都足够高概率，也会占用 context、增加维护与注入风险。

SFT 通过参数更新，把目标交互模式直接放进模型行为分布。

## Demonstration 数据定义了什么

一条 instruction-tuning 样本通常包含：

```text
system policy
user instruction
optional context / tool result
assistant response
```

它不是普通问答表。数据同时定义：

- 角色和 turn 边界。
- 对指令的解释方式。
- 回答格式、长度与语气。
- 拒答、澄清和安全边界。
- 工具调用或结构化输出协议。

因此 SFT data schema 是模型接口的一部分。训练时的 chat template 与 Serving 时不同，即使可见文字近似，也可能形成 special-token、role id 或 whitespace 的 training-serving skew。

## SFT 的数学仍是条件最大似然

给定 prompt `x` 和 response `y`：

```text
p_theta(y | x)
= product_(t=1)^T p_theta(y_t | x, y_<t)
```

Response-only SFT loss 为：

```text
L_SFT(theta)
= - sum_(t=1)^T log p_theta(y_t | x, y_<t)
```

在 packed batch 中可写成 masked token loss：

```text
L_SFT
= - (1 / sum_(b,t) m_(b,t))
  * sum_(b,t) m_(b,t)
  * log p_theta(y_(b,t) | prefix_(b,t))
```

Logits 仍是 `[B,T,V]`，loss 并没有换成新的模型输出类型。变化来自训练分布、哪些 positions 被 mask，以及更新通常从 pretrained checkpoint 而不是随机参数开始。

## 一个 loss mask 小例子

假设 token sequence 是：

```text
[SYSTEM, policy, USER, 2+2?, ASSISTANT, 4, EOS]
```

若只训练 assistant response，labels 与 mask 可抽象为：

```text
labels = [policy, USER, 2+2?, ASSISTANT, 4, EOS]
mask   = [   0,    0,    0,         0, 1,   1]
```

System 和 user tokens 仍进入 context，决定 assistant tokens 的条件概率，但它们对应的 next-token positions 不贡献 loss。

若 mask 错位一格，模型可能被训练去预测角色边界而漏掉答案 token；若把 padding 也计入 loss，模型会学习无意义的 PAD 分布。SFT correctness 首先是 token-level alignment correctness。

## 是否应该对 Prompt 也计算 loss

对完整 conversation 所有有效 tokens 计算 loss，可以增加监督 token 数，并让模型学习 user/system 文本分布；response-only loss 则把容量更集中在目标输出行为。

两者没有脱离场景的绝对答案：

- Continued pretraining 或 domain adaptation 可能希望训练所有文本。
- Instruction following 通常更关心 assistant positions。
- 多轮对话可能只训练部分 assistant turns。
- Tool traces 可能需要分别 mask arguments、results 和自然语言。

必须记录 loss mask policy。只保存原始 JSON 而不保存模板和 masking code，无法复现实际训练 objective。

## 为什么少量高质量数据也可能有效

SFT 通常不是从零创造语言能力。Pretraining 已经形成大量表示与生成模式，SFT 的任务更像是选择、组合和稳定目标行为。

因此 demonstration 的边际价值可能高于随机网页 token。但“少量数据足够”不能泛化为固定数量定律：

- 新领域是否已在基座能力范围内。
- 输出协议有多复杂。
- 目标行为与基座分布偏离多远。
- 数据是否覆盖困难和失败案例。
- 模型规模与更新方式。

重复大量同质 examples 可能快速降低 training loss，却造成 style collapse、过度拒答或对 prompt phrasing 过拟合。

## SFT 数据质量比格式整齐更难

高质量 demonstration 至少需要检查：

- Instruction 是否可解、信息是否充分。
- Response 是否正确，而不只是流畅。
- Style、verbosity 和格式是否与目标一致。
- Refusal 是否在正确边界触发。
- 多轮上下文与工具结果是否自洽。
- 不同 domains、语言与难度是否平衡。
- Synthetic data 是否经过 verifier 或抽样人工检查。

使用更强模型生成 synthetic demonstrations 可以扩大覆盖，却可能复制 teacher 的错误、偏好和措辞。过滤器与 judge model 也会引入自己的 selection bias。

## Full fine-tuning 与 parameter-efficient adaptation

Full SFT 更新全部参数：

```text
theta <- theta + Delta theta
```

它提供最大的更新自由度，也需要保存全部 gradients、optimizer states 和新模型权重。

第 26 章 LoRA 将更新限制为低秩 adapters：

```text
theta_base frozen
Delta theta represented by small trainable factors
```

两者可以使用相同 SFT data 与 token loss。LoRA 是参数化和训练状态选择，不是另一种 supervision objective。

## Catastrophic forgetting 与能力回退

若 SFT 数据分布很窄、learning rate 过大或训练过久，模型可能提高目标任务表现，却损伤通用能力。表现包括：

- 回答风格过度统一。
- 多语言或代码能力下降。
- 所有问题都触发相似模板。
- 事实知识被局部错误 demonstration 覆盖。
- 拒答边界过宽或过窄。

缓解方法可能包括混入部分 pretraining/domain data、降低 update magnitude、增加数据多样性、使用 adapters 或早停。但每种方法都重新定义训练分布，必须通过 multi-slice Evaluation 验证。

## SFT 能否注入知识

模型可能从 SFT examples 学到新事实或领域映射，但这不是可靠知识管理协议。少量参数更新可能：

- 只对相似 wording 有效。
- 与旧知识冲突。
- 造成无关行为变化。
- 难以追踪、更新或删除。

需要频繁更新、可引用或权限敏感的知识，通常还要考虑 Retrieval、tool 或外部 state。SFT 更稳定的角色是塑造行为和任务接口，而不是替代所有知识系统。

## SFT 不能表达“哪个回答更好”

Demonstration 只给出一个目标 response。它没有直接说明：

- 另一个回答差在哪里。
- 两个都可接受但哪个更好。
- Helpfulness 与 safety 冲突时怎样权衡。
- 输出偏离 reference 文本但仍正确时是否应奖励。

把唯一 reference 当作所有正确表达，会惩罚合理多样性。第 27 章从 preference pairs 和 reward modeling 开始处理相对判断；第 30 章 DPO 则直接用 chosen/rejected pairs 优化策略。

## 训练与 Serving 的接口一致性

上线前至少要核对：

- Tokenizer、special token ids 与 chat template。
- System/user/assistant role 顺序。
- BOS/EOS 的添加位置。
- Generation stop conditions。
- Tool schema 与 structured-output grammar。
- Adapter/base checkpoint 版本。

模型训练得到的是 token-level protocol。Serving 层若重新拼接字符串或重复添加 special tokens，会让模型面对训练中未见的 prefix。

## Evaluation 应分开能力与行为

SFT 后应同时比较：

- Instruction-following 与格式成功率。
- 任务正确率、事实性和代码执行结果。
- Safety、refusal precision/recall。
- 通用能力和多语言回归。
- 输出长度、verbosity 与 latency/cost。
- 对 prompt phrasing 和 system policy 的鲁棒性。

Training loss 只衡量对 demonstrations 的拟合。若 validation set 与训练模板高度相似，它也可能高估真实产品分布上的泛化。

## 本章在知识树中的位置

```text
pretrained checkpoint
+ instruction demonstrations
+ chat template / loss mask
-> SFT objective
-> instruction-following checkpoint
-> LoRA or full update
-> preference optimization
```

本章把第 24 章的通用 next-token learner 转成可交互模型。第 26 章改变更新的参数化成本，第 27～30 章加入相对偏好，Part VI 再把 prompt、tool 与 workflow 组织成运行时协议。

## 自检问题

1. Pretraining 能续写文本为什么不等于稳定遵循指令？
2. SFT 与 Pretraining 为什么可以使用同一种 cross-entropy？
3. Response-only loss 中 prompt tokens 发挥什么作用？
4. Loss mask 错位会产生什么训练错误？
5. Chat template 为什么属于 checkpoint 接口？
6. 少量 SFT 数据有效为什么不是固定规模定律？
7. Synthetic demonstrations 会引入哪些新偏差？
8. Full SFT 与 LoRA 的 objective 有什么关系？
9. 为什么 SFT 不是可靠的动态知识管理方案？
10. Demonstration 数据为什么不足以表达相对偏好？

## 小结

SFT 通过 demonstrations 和 loss mask，把 pretrained model 的开放续写分布收窄为目标交互行为。它仍然执行 token-level maximum likelihood，但数据 schema、角色协议与监督位置改变了模型被奖励的行为。

SFT 可以显著改善指令遵循、格式和风格，也可能导致过拟合、遗忘或错误行为固化。它需要和任务正确性、安全、通用能力回归以及 Serving protocol 一起评估。

## Review notes

本章将 SFT 定位为 demonstration imitation，明确 response-only masking、chat template、full/LoRA 参数化和 knowledge injection 边界。Preference ranking 与 reward optimization 留给第 27～30 章，Prompt 与 tool runtime 留给 Part VI。

Primary-source 校验入口：

- Jason Wei et al., "Finetuned Language Models Are Zero-Shot Learners", 2021: https://arxiv.org/abs/2109.01652
- Victor Sanh et al., "Multitask Prompted Training Enables Zero-Shot Task Generalization", 2021: https://arxiv.org/abs/2110.08207
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Hyung Won Chung et al., "Scaling Instruction-Finetuned Language Models", 2022: https://arxiv.org/abs/2210.11416
