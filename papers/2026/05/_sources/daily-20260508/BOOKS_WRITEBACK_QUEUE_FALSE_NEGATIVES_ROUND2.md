# 2026-05-08 Books writeback queue — post-write false negatives

本文件保留 root 最小写回合同；以下 5 项现已修改 Books。仍须由未参与本轮作者修复和 root 写回的 reviewer 做 proposition-level 验收。

## 1. `SF-2026-ARXIV-2605-05715` → `PLATFORM-EVALUATION-SYSTEM`

- **目标：** `books/part-06-ai-infrastructure/66-evaluation-system.md`
- **插入位置：** uncertainty sensor → calibrated risk/coverage → abstention 段，紧邻“probe 是 sensor 不是 truth”的命题。
- **最小语义增量：** 明确拆开 `decodability`、`intervention efficacy` 与 `decision authority`。failure direction 可被线性 probe 读出，仍可能与 task-critical computation entangle，固定线性 steering/erasure 会无效或伤害；此时 probe 只可支持校准后的 abstention/escalation，不能拥有 correction authority。保留 nonlinear/local intervention 作为待独立验收的条件分支。
- **边界：** Llama-3.1-8B、Qwen2.5-7B，主要 MedQA，29 fixed-linear configs；`AUROC 0.610` 与 60% coverage 结果不外推；self-consistency 约 10× cost；nonlinear adapter 有 `8.2%` damage。
- **Primary:** https://arxiv.org/html/2605.05715v1

## 2. `SF-2026-ARXIV-2605-05750` → `TRAIN-RLHF`

- **目标：** `books/part-04-training-system/31-rlhf.md`
- **插入位置：** 多目标 reward / reward model aggregation 与 hard constraint 交接处；短 handoff 到 `TRAIN-GRPO` 的 optimizer implementation。
- **最小语义增量：** 算术均值允许高分目标补偿低分 must-have，mean reward 不能证明所有约束满足。risk-sensitive SoftMin/variance penalty 是条件分支：它提高 bottleneck adherence，却由 criterion difficulty 而非声明优先级驱动，并可能放大 noisy reward channel；真正 hard safety/schema constraint 仍需分项报告与 deterministic gate。
- **边界：** HealthBench/GPQA/tool-calling、Qwen2.5、17/2 reward channels；`k`、group size 与 schedule 敏感，静态高 `k` 和 aggressive start 可 collapse。
- **Primary:** https://arxiv.org/html/2605.05750v1

## 3. `SF-2026-ARXIV-2605-06036` → `TRAIN-RLHF`

- **目标：** `books/part-04-training-system/31-rlhf.md`
- **插入位置：** preference data provenance/noise → reward-model training → downstream policy handoff；短 handoff 到 `TRAIN-DATA`。
- **最小语义增量：** preference admission 不应默认 strict mass conservation。partial OT 可以拒绝与 semantic consistency 冲突的 noisy mass，避免 reward model 被强迫拟合 outlier；但 clean-more-consistent 是前提，不是事实，systematic/adversarial noise 可击穿。保存原始 preference、selection mask、embedding/reward-model revision 与 dispute path。
- **边界：** HelpSteer/UltraFeedback/PKU-SafeRLHF、Qwen2.5/LLaMA2 7B–72B、DeepSeek-V3 judge；理论上界只约束 selected subset；`O(N²)` cost 与 online scale 未解决。
- **Primary:** https://arxiv.org/html/2605.06036v1

## 4. `SF-2026-ARXIV-2605-06078` → `TRAIN-GRPO`

- **目标：** `books/part-04-training-system/33-grpo.md`
- **插入位置：** trajectory-level terminal reward → typed/local credit → counterfactual credit 的演进链。
- **最小语义增量：** milestone boundary 是一种比整轨迹 reward 更细、比逐 action causal credit 更弱的中间粒度。Environment/harness 必须冻结 milestone identity；segment shaping 与 dual-scale advantage 可保留已完成 subgoal 的学习信号，但不能把 heuristic milestone 冒充因果 credit。粒度过稀退回 terminal reward，过密或不可验证时退回 critic/verifier/counterfactual branch。
- **边界：** ALFWorld/WebShop/ScienceWorld、离散 action/text、最多 15/30 steps；未覆盖 continuous control、multi-Agent 与无显式 transition 的任务。
- **Primary:** https://arxiv.org/html/2605.06078v1

## 5. `SF-2026-ARXIV-2605-06200` → `TRAIN-GRPO`

- **目标：** `books/part-04-training-system/33-grpo.md`
- **插入位置：** hierarchical/state-aware grouping 后，作为“turn index 只是受限 comparison key”的条件分支。
- **最小语义增量：** pooled turn normalization 会混合不同 context distribution；`(prompt, turn-index)` group、sqrt-depth rescaling 与 turn-level clipping 可对齐 process-credit unit，但 turn index 不等于真实 state equivalence，且 similarity 随深度下降。Group builder 持有 membership；optimizer 只消费冻结的 turn credit；group size≤1 或无 ground-truth answer 时回退 outcome reward/其他 signal。
- **边界：** 7 个 QA benchmarks、3 个 Qwen backbones、本地 Wikipedia retrieval、8×H20/VeRL；IG forward 增加成本，production async trajectory 未验证。
- **Primary:** https://arxiv.org/html/2605.06200v1

## Cross-day reconciliation

- `SF-2026-ARXIV-2605-05250` 的 canonical owner 是 05-08 official batch；该 family 只存在于 05-06 的 legacy screening ledger，05-06 当前 V3 活动账本没有此条，因此无需改变已冻结分母，且不得把 legacy 条目误当作第二个 owner。
- `2605.06225`、`2605.06241` 属于 05-12 official batch；`2605.05686` 未进入 05-08 canonical 619。三者均不塞入 05-08。

## 写回后验收

1. 每个机制只有上述 canonical owner；相邻章节只做短 handoff。
2. 正文包含旧方案为何合理、约束变化、机制/owner、证明与未证明、trade-off、failure mode 与 fallback。
3. 同步 05-08 README 与 canonical ledger 中 `Integrate — Applied`，再重算 Books disposition。
4. 新 reviewer 不复用作者判断，必须打开 exact-v1 与目标正文逐命题比对。
