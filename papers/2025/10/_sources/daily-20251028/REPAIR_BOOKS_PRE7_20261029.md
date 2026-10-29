# I50 private PO：完整受限稿

待sole先校准W29准入/受限Evidence，再整体PRE以下一段/独立marker/本人注。writer已实际比较Ch72 DP单位/packing、发布ledger、single-pass release后处理等具体段：已有静态贡献映射不承载on-policy改变后续采样时fresh-unit adaptive parallel composition的成立条件。完整两侧见context7，非全章授权。

文件：`books/part-06-ai-infrastructure/72-security.md`；VaultGemma sequence单位完整段后、2025 layering表前。

```markdown
On-policy训练还会让后续采样依赖当前policy，不能把已经固定的`(prompt,response)`数据集邻接直接搬入：一条[受限private policy-optimization分支](https://arxiv.org/html/2510.21060v1#S3)把各出现一次的fresh prompt/user当单位，每批只消费新单位，由私有更新和adaptive parallel composition约束最终policy。这里“user”仍是item-level名字，不覆盖同一真实用户的多条记录，也不自动覆盖multi-pass/重复prompt。隐私代价较低阶依赖相应horizon、维数、epsilon与光滑/梯度、Fisher或回归coverage条件；general private oracle可能计算不高效，表面无维数的界也可能经更新范数重新依赖维数。Bandit主理论与小CartPole实验不授LLM PPO实用配方。全部fresh数据/rollout、reward、私有求解和独立效用/会计回归均付费；单位复用、支持或数值条件失配时，保按实际贡献重新会计、原私有训练与较窄发布，不由one-pass定理批准生产用户级隐私或免费RL。

<!-- source-family:SF-2025-ARXIV-2510-21060 -->
```

```markdown
- `SF-2025-ARXIV-2510-21060`：Daily2025-10-28补Oct27；exact-v1§2–6/H/I必要、2+2+2=6/隐私深入，W29待sole校准。仅fresh-unit one-pass/on-policy邻接与parallel composition，不采真实user多贡献/multi-pass/普遍lower-order或dimension-free；保bandit/CartPole三seed/全费，未核实现/accountant/LLM复现。完整PRE/SAVE/自读/solePOST仅本日后到实际层。
```

作者已自读完整新增/marker/本人注，实际读完整两侧及其2025 layering表；未获PRE不写。
