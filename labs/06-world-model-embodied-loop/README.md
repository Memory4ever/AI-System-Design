# Lab 06 — World Model & Embodied Loop

## Lab Question

生成下一 observation 怎样演进为 action-conditioned environment transition，并进入可修正的闭环控制？

## Why This Lab Exists

视频或下一帧生成可以学习视觉连续性，却不保证 action controllability、causal state 或长期一致性。World Model
需要区分 observed、predicted 与 committed state；Embodied loop 还增加传感延迟、controller frequency、safety
envelope 与真实反馈。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `MULTIMODAL-WORLD-MODELS` | Ch25 | Action-conditioned state transition owner |
| `MULTIMODAL-EMBODIED-VLA` | Ch26 | Perception→action→feedback owner |
| `MULTIMODAL-REPRESENTATION` | Ch23 | Observation identity prerequisite |

## Prerequisites

- 完成 Lab 05；可使用离散 grid、简化物理环境或合成 trajectory。

## System Under Test

一个可重置、可回放的 toy environment。Environment 拥有 truth state，world model 拥有 predicted state，planner/policy
拥有 action proposal，controller 拥有 action commit 与 safety check。

## Baseline

无模型 reactive policy：只根据当前 observation 选择 action。它在 fully observable、低延迟、短 horizon 下简单可靠。

## Step-by-Step Experiments

1. 固定 observation/action/state schema、timestamp、episode 与 environment seed。
2. 训练 next-observation predictor，验证它可能生成连贯结果但不响应 action。
3. 加入 action-conditioned transition，比较 held-out action sequences 与 counterfactual rollouts。
4. 分离 latent predicted state、raw observation 和 persistent memory，支持 revise/supersede。
5. 用 imagined rollout 选择 action，再由 environment truth 验证并纠正 state。
6. 增加 high-level plan / low-level controller 分层、latency budget 与 safety envelope。

## Expected Artifacts

- Versioned trajectory、environment replay、world-state prediction 与 action/observation trace。
- Lab 14/15 可复用的 observed/predicted/committed state 区分。

## Invariants

- Predicted state 永不覆盖 environment truth；每条 state 有 source、valid time 与 supersession。
- Action proposal 通过 controller/safety gate 后才提交。
- Replay 使用相同 environment/version/seed，并能定位 divergence 首点。

## Failure Injection

- Observation delay/drop、action noise、environment drift、unseen action combination、错误 calibration。
- 让 imagined rollout 看似优良但违反 safety constraint，验证 commit gate。

## Measurements

- Prediction error、controllability、rollout drift、task success、correction frequency。
- Sensor-to-action latency、control frequency、safety intervention 与 recovery time。

## Acceptance Criteria

- [ ] 能实验证明“生成连贯”不等于“action controllable”。
- [ ] Observed、predicted、revised 与 committed state 可追溯且不混写。
- [ ] 至少一次 environment drift 或 sensor failure 能触发安全降级。
- [ ] Reactive、model-based 与 hierarchical control 的适用条件明确。

## Trade-offs and Alternatives

World Model 提供 planning lookahead，却增加 compounding error、state calibration 和模型成本。Reactive policy 在短
horizon、强反馈下继续成立；显式 simulator 在规则可知时可能比 learned dynamics 更可靠。

## Reflection Questions

1. World state 与 Agent Memory 的 truth authority 有何不同？
2. Rollout horizon 增加时，误差和决策收益怎样共同变化？
3. Safety controller 为什么不能由 world model 自行替代？

## Next Lab Handoff

向后续 Agent Labs 交付带 authority 的 environment state 和 action commit contract；主线返回 Lab 07，开始把模型
能力生产过程变成可恢复资产。

