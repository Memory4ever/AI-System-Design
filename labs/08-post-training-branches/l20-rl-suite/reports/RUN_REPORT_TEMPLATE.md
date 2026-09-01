# L20 Post-training Run Report

- **Run ID:** `YYYY-MM-DD-stage-profile-seed`
- **Stage:** `SFT | Reward | DPO | PPO | RLOO | GRPO`
- **Process status:** `Not Run | Process Running | Process Failed | Process Exited 0`
- **Experiment Gate:** `Not Evaluated | Pending Evaluation | Accepted | Rejected`
- **Evidence level:** `E0 | E1 | E2 | E3 | E4`

## Hypothesis

写明唯一变化、预期方向和成立条件。不要写“某算法更好”。

## Workload Contract

| Dimension | Value |
| --- | --- |
| Git revision / dirty state | |
| OpenRLHF / container / driver | |
| Dataset digests and split | |
| Base / SFT / RM / reference identity | |
| GPU model, count and topology | |
| Precision / quantization | |
| Prompt / output length | |
| Batch / samples per prompt | |
| Seed | |
| Reward mode and verifier revision | |

## Correctness Gates

- [ ] Dataset validation passes and train/eval prompts are disjoint.
- [ ] Checkpoint can reload independently.
- [ ] Baseline and candidate use the same evaluation and decoding contract.
- [ ] NaN/Inf, reward distribution, KL, entropy and generation length are recorded.
- [ ] Online stages record rollout-policy and update-policy checkpoint revisions.

## Results

| Variant | Exact | Strict JSON | OOD Exact | Reward | KL | Entropy | Step Time | Peak HBM |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Base | Not Run | Not Run | Not Run | N/A | N/A | N/A | Not Run | Not Run |
| Candidate | Not Run | Not Run | Not Run | Not Run | Not Run | Not Run | Not Run | Not Run |

## Failure Injection

| Injection | Expected signal | Observed result |
| --- | --- | --- |
| Flip preference pairs | RM/DPO objective and held-out exact diverge | Not Run |
| `REWARD_MODE=shortcut` | Reward rises while exact accuracy does not | Not Run |
| Reduce samples per prompt | RLOO/GRPO advantage variance or zero groups change | Not Run |
| Stale rollout checkpoint | policy-lag/KL signal changes | Not Run |
| OOD expressions | in-distribution improvement may not transfer | Not Run |

## Interpretation

分别写清：观测事实、受支持的判断、尚未证明的内容、新增系统债务、旧路径仍适用的条件。

## Handoff

列出 checkpoint、optimizer、critic、reference、reward/verifier、rollout trace、metrics 和恢复状态的 owner 与 identity。
