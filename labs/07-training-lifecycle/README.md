# Lab 07 — Training Lifecycle

## Lab Question

一次训练怎样从临时脚本演进为 data、objective、optimizer、precision 与 checkpoint identity 完整的可恢复模型资产？

## Why This Lab Exists

单机脚本在早期探索中最快，却把数据版本、sampler、seed、optimizer 和保存时点隐藏在进程里。训练时间与团队
规模扩大后，主要风险从“能否更新参数”变成“能否复现、恢复、比较和交付同一个模型”。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `TRAIN-DATA` / `TRAIN-PRETRAINING` | Ch27～28 | Data/objective owner |
| `TRAIN-SFT` | Ch29 | Supervised training branch |
| `TRAIN-CHECKPOINT` | Ch35 | Recoverable state owner |
| `PLATFORM-MODEL-REGISTRY` | Ch59 | Artifact identity handoff |

## Prerequisites

- 完成 Lab 01 和 Lab 02；使用小模型与可在 CPU 完成的 dataset baseline。

## System Under Test

数据读取、batch sampler、training step、optimizer、scheduler、mixed-precision policy、checkpoint/save-resume 和
evaluation。Trainer 拥有 update order，checkpoint writer 拥有 atomic snapshot，registry 只消费验证后的 artifact。

## Baseline

从头运行到结束，只保存最终权重。短实验中简单，但无法恢复 optimizer/sampler/random state 或解释中间差异。

## Step-by-Step Experiments

1. 固定 dataset manifest、split、transform、sampler、seed 和 objective identity。
2. 建立 deterministic small-run baseline，记录 loss、gradient、tokens 与 elapsed step。
3. 保存 model、optimizer、scheduler、scaler、sampler position 与 random states。
4. 在指定 step 中断并 resume，对齐 uninterrupted run 的参数与指标。
5. 注入 checkpoint partial write、schema/version mismatch 和 data drift，验证 fail-closed load。
6. 生成 artifact manifest，包含 lineage、evaluation 与可部署性声明。

## Expected Artifacts

- Reproducible training config、checkpoint schema、resume parity test 与 model artifact manifest。
- Lab 08 可复用的 base checkpoint，Lab 09 可复用的 logical state inventory。

## Invariants

- Global step、consumed samples/tokens、optimizer/scheduler 与 parameters 同一 snapshot boundary。
- Checkpoint 完整性先验证再发布；不兼容 schema 不静默加载。
- Resume 不重复或跳过 data，除非报告明确声明 at-least-once semantics。

## Failure Injection

- Mid-step crash、partial file、磁盘不足、错误 data manifest、world-size/precision 变化。
- 只加载权重不加载 optimizer，比较这是否仍能称为 continuation。

## Measurements

- Loss/parameter resume error、checkpoint size/time、recovery time、lost/repeated samples。
- Training throughput、data wait、memory 与 validation quality。

## Acceptance Criteria

- [ ] Interrupted/resumed run 与 uninterrupted reference 在声明 tolerance 内对齐。
- [ ] Partial/corrupt/incompatible checkpoint 被显式拒绝或迁移。
- [ ] Model artifact 可追溯到 data、objective、code 与完整训练状态。
- [ ] 报告区分 warm start、weights-only load 与 exact continuation。

## Trade-offs and Alternatives

完整 checkpoint 恢复最强，但保存成本高；weights-only 适合迁移学习，不适合 exact resume。更高保存频率降低
lost work，却增加 I/O 干扰。Atomic rename、distributed shards 与 remote object store 属于不同 durability 分支。

## Reflection Questions

1. 哪些训练状态缺失后仍能恢复“能力”，但不能恢复“同一轨迹”？
2. Checkpoint identity 应包含哪些 data 和 parallel layout 信息？
3. Artifact 何时才有资格进入 Model Registry？

## Next Lab Handoff

向 Lab 08 交付 base model、dataset/objective lineage 与 reproducible trainer；向 Lab 09 交付参数、gradient、optimizer、
activation 和 random/sampler state inventory。

