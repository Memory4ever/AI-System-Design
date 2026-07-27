# Part IV Training System：从数据到可交付能力

## Part Question

数据、训练目标、优化状态与分布式执行怎样共同决定一个可交付模型？为什么算法上等价的目标，在不同数据、精度、并行和版本条件下会产生不同能力？

## 进入条件

Part II、III 已定义模型和多模态能力的语义。本 Part 接管能力生产：训练数据、objective、parameter update、checkpoint 和 distributed state；它不把训练 loss 直接解释为线上质量。

## 演进主线

```text
Governed data
→ Pretraining capability prior
→ SFT interface shaping
→ Parameter-efficient adaptation
→ Preference / reward signal
→ PPO / GRPO trajectory / DPO design branches
→ Recoverable training state
→ Multi-device execution
→ Validated deployment artifact
```

Post-training 不是单向版本序列。SFT、PPO、GRPO 与 DPO 接受的监督对象、保存的状态和 failure mode 不同；TP、PP、ZeRO、Megatron 与 DeepSpeed也分别属于并行维度、状态所有权和 Runtime 编排层。

## 章节分工

- [Ch27～30](27-data.md) 建立数据、Pretraining、SFT 与 LoRA 的能力生产入口。
- [Ch31～34](31-rlhf.md) 从偏好数据进入 RLHF，并比较 PPO、GRPO trajectory lifecycle 与 DPO 的不同约束。
- [Ch35](35-checkpoint.md) 定义可恢复、可转换、可验证的训练状态。
- [Ch36～39](36-distributed-training.md) 依次拥有 collective contract、Tensor Parallel、Pipeline Parallel 与 ZeRO。
- [Ch40～41](40-megatron.md) 用 Megatron 与 DeepSpeed 展示多维并行和 state lifecycle 怎样进入 Runtime。

## 退出契约

读完后，应能把一个训练结果还原为 data、objective、optimizer、precision、parallel layout 与 checkpoint identity 的联合产物。Part V 只接收通过验证的模型资产，再讨论如何交付，不通过更快推理修复训练错误。
