# Qwen3.5-4B MLX LoRA：结构化 AI System 回答

- **Run ID:** `2026-08-20-qwen35-4b-lora`
- **Status:** 30-step smoke completed
- **Base model:** `/Users/apple/Downloads/Qwen3.5-4B`
- **Runtime:** Unsloth Desktop `0.1.800-beta`, Apple Silicon MLX
- **Hardware:** Apple M1 Max, 64 GB unified memory

## Hypothesis

在保持 base checkpoint 不变的条件下，使用 100 条高质量 demonstration 对七类 Attention/MLP projection 注入 Rank-16 LoRA，可以提高 held-out AI System 问题的六段结构完整率，而不会让通用回归问题全部退化成固定模板。

目标结构固定为：

```text
问题 -> 原理 -> 机制 -> 权衡 -> 系统连接 -> 演进
```

本实验只验证行为与表达结构，不声称 100 条样本能增加可靠的新知识。

## Artifact Layout

```text
dataset/source.py          reviewed source records and split definitions
dataset/train.jsonl        100 training demonstrations
dataset/validation.jsonl   20 held-out demonstrations
dataset/test.jsonl         20 prompts with expected concepts
dataset/regression.jsonl   10 general prompts that must not inherit the six-section template
evaluation/score_outputs.py
baseline/                  base-model generations
candidate/                 adapter generations
adapter/                   LoRA artifact produced by Unsloth
experiment-config.yaml     intended training contract
report.md                  evidence and conclusion
```

## Execution Gates

1. Dataset JSONL、sample count、role order、heading contract 全部通过检查。
2. 在相同 decoding 参数下保存 base outputs。
3. 先运行 30-step smoke training；出现 OOM、NaN 或 backend error 时停止。
4. Adapter 能重新加载后，使用同一 test prompts 生成 candidate outputs。
5. 只有 held-out structure score 改善且 regression prompts 未明显退化，才进入更长训练。

## Reproduce Dataset

```bash
python3 dataset/source.py
python3 evaluation/score_outputs.py --validate-dataset
```

## Evidence Boundary

本次是单机、单模型、单 seed 的 E1 smoke experiment。Adapter 已独立重载并完成 held-out A/B evaluation。结果证明该 MLX/Unsloth/model/dataset 组合可以学习稳定的回答结构；不能外推到 NVIDIA backend、其他模型、知识注入或生产质量。
