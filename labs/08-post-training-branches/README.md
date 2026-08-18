# Lab 08 — Post-training Branches

## Lab Question

SFT、LoRA、DPO、PPO 与 GRPO 分别消费什么监督对象、保存什么状态，为什么不能被写成单向升级序列？

## Why This Lab Exists

SFT 用 demonstration shaping interface，简单稳定；参数高效适配减少写入成本；preference/offline objectives 避免
在线 rollout；PPO/GRPO 能消费 trajectory feedback，却引入 policy drift、sampling、credit 与 verifier coupling。
选择取决于监督和约束，而不是算法发布时间。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `TRAIN-SFT` / `TRAIN-LORA` | Ch29～30 | Demonstration 与 parameter-efficient branch |
| `TRAIN-RLHF` | Ch31 | Preference/reward signal contract |
| `TRAIN-PPO` / `TRAIN-GRPO` / `TRAIN-DPO` | Ch32～34 | Online trajectory 与 offline preference branches |
| `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Outcome/verifier evidence handoff |

## Prerequisites

- 完成 Lab 07，并保留同一个 base checkpoint 与 evaluation set。
- 理解 log probability、KL、advantage、reward 与 reference policy。

## System Under Test

同一个小模型、受控 demonstrations/preferences/tasks 和统一 evaluation。Dataset/reward/verifier 分别拥有监督证据，
algorithm 只拥有 update；最终能力判断归 evaluation contract。

## Baseline

Base checkpoint 与 full-parameter SFT。SFT 在高质量 demonstration 足够、online exploration 风险高时仍是主路径。

## Step-by-Step Experiments

1. 固定 base model、task split、evaluation 与 behavior contract，完成 full SFT baseline。
2. 用 LoRA 复现相同任务，比较 trainable state、merge/unmerge 与 base identity。
3. 构造 pairwise preference，完成 DPO-like offline update，检查 reference/KL effect。
4. 建立最小 rollout + reward/verifier loop，分别实现 value-based PPO-like 与 group-relative GRPO-like update。
5. 对齐 sample/token/compute budget，比较 quality、drift、variance 与 state cost。
6. 注入 noisy preference、reward hacking、group collapse、stale rollout 和 OOD prompts。

## Expected Artifacts

- 同一 base 上的 SFT、LoRA、DPO、PPO-like、GRPO-like checkpoints 与统一 evaluation reports。
- Algorithm state inventory，供 Lab 09 分析分布式成本。

## Invariants

- 所有分支从可追溯的同一 base 和 split 出发。
- Reward/verifier score 不等于真实 task correctness；final evaluation 独立。
- Rollout policy、update policy、reference policy 和 checkpoint revision 不混淆。

## Failure Injection

- 翻转 preference、制造 shortcut reward、降低 group diversity、延迟 rollout、修改 reference checkpoint。
- 比较训练目标改善但独立 evaluation 下降的情况。

## Measurements

- Task quality、reward、KL、entropy、win rate/calibration 与 held-out robustness。
- Trainable parameters、tokens、rollout calls、optimizer/checkpoint bytes、step time 与 variance。

## Acceptance Criteria

- [ ] 五个分支在同一 evidence contract 下完成，不用各自最有利指标比较。
- [ ] 每种算法的监督对象、state owner 与主要 failure mode 可定位。
- [ ] 至少复现 reward/preference proxy 改善但真实效果不改善的反例。
- [ ] 报告给出选择分支的条件，而不是生成算法排名。

## Trade-offs and Alternatives

LoRA 降低写入成本但引入 adapter/base compatibility；DPO 简化 Runtime 但受 preference coverage 限制；PPO 增加
value/trajectory state；GRPO 移除显式 value model，却依赖 group composition 与 verifier。SFT 不是被淘汰的旧方案。

## Reflection Questions

1. Offline preference 与 online trajectory 分别看不到哪些反馈？
2. Group-relative advantage 的 identity 包含哪些 sampler 条件？
3. 算法 state 增加后，checkpoint/recovery contract 怎样变化？

## Next Lab Handoff

向 Lab 09 交付各分支的 parameter/gradient/optimizer/rollout/reference/verifier state inventory；下一步研究这些状态
怎样跨设备分片、同步和恢复。

