# 26274/26779：安全状态机与 RL rollout 的两个写前有限包

本包是作者依据官方 exact-v1 与实际章节形成的 source→owner 提案；非作者采用、共享锁和写后复核尚未发生，不能把文字预案计入 Books Integrate。本批归属仍是官方公告时隙、连续编号和相邻批次的有据推断，不用 Submitted/Updated 单证。

## 2604.26274v1 Praetor → Ch72

[官方 §4.1–4.3、§5、§7–8](https://arxiv.org/html/2604.26274v1)将经过确认的良性 tool-call 轨迹按有限最近工具上下文编译为 pDFA，转移边携参数约束；运行时每个 session 保持当前节点，在**执行前**核下一条 tool/参数，不合法即拒绝且状态不前进。原 Ch72 约 505–530 行已把检测、authorizer、executor 分权，约 1300–1339 行已要求跨动作累计风险/effect-time 审查；新差额不是“从单步变为轨迹安全”，而是低熵、稳定任务里把经审批的良性序列编译为低延迟的**正向准入状态**，profile 的重编/版本迁移本身也是权限变更。建议只在 Ch72 cumulative-effect 段后接一小段，不复制 Ch81 workflow state。

拟正文：在工具集合与任务流程稳定时，还可把经人工确认的良性调用轨迹编译成带参数 guard 的有限状态 profile；gateway 为每次 run 维护节点，在提交下一次 tool effect 前同时查工具转移、参数范围和当前授权。相对于逐次语义扫描，这把可执行路径收窄到该部署已审过的行为 envelope，但 profile 只提出**结构性允许**，不能代替 IAM、资源 ACL、敏感字段白名单或 effect-time policy。新工具、prompt、上下文或 schema 上线时需冻结旧 profile、审查增量并迁移版本；无可核良性轨迹、流程高熵或状态漂移时，旧逐步 guard/人工审批反而更可靠。

边界：§4.1 明说 profiling corpus 须可信，不能拿 live 未审轨迹自学习；§8 的 profile poisoning、合法循环泄漏和连续 string 同义改写都是反例。§7 仅五 ASB 场景，三个结构化场景 ASR 2.2% 与总体 5.6% 分母不同，开放 Research/Travel 为 12.6%/8.6%；14 个跨过结构筛的攻击 0 成功的 95% CI 上界仍 23.2%。`O(1)` 是结构查表相对工具数，不含 string embedding/参数扫描，2.2ms per call 非完整安全 SLO。非作者若认为现 Ch72 已写同一“审核 trace→pDFA→pre-effect state gate”条件，应判 Existing 而不是机械贴段。

## 2604.26779v1 NeMo RL Speculation → Ch33

[官方 §2–4/Tables 1–5](https://arxiv.org/html/2604.26779v1)把 target-law exact speculative decoding 放进 RL rollout generation。现 Ch48 已有 exact verifier/target distribution，Ch33 约 1130–1175 行已有 rollout policy version、buffer admission 和 staleness；新差额是从当前 policy 的 verifier/GRPO forward 复用 hidden state 与 logprobs，**detach 后**训练 draft head，使辅助 draft loss 不改 actor 的 policy-gradient 路径。Verifier 的接受与 KL/GRPO loss 仍按 current target policy；这把 proposal 计算、policy law、训练梯度和版本身份分开，而非称任意草稿天然 on-policy。建议 Ch33 rollout lifecycle gate 后、已有异步 overlap 成本分账前一小段；Ch48 只交接 exact law，不重复 RL 训练合同。

拟正文：训练 rollout 即使采用 lossless speculative decoding，也须把草稿网络和生成策略的权力拆开：draft 只提候选，当前 policy 的 verifier 决定实际 token 分布、logprob 与 RL loss。若用同一次 policy forward 的 hidden state 在线训练 draft，应把草稿辅助目标在 policy trunk 前 stop-gradient，并绑定 actor/draft/accepted trace 的版本；否则降低生成成本的分支会悄悄修改被优化的 policy gradient，或把旧版本接受轨迹当当前 on-policy 样本。旧自回归路径在 acceptance 低、draft 更新成本高、rollout 已被训练并行隐藏或严格可验证性优先时仍是安全回退。

边界：Table 1 RL-Think/RL-Zero generation `1.54/1.77×` 对整步只有 `1.35/1.41×`；n-gram 虽有正接受率仍可慢于 AR。草稿长度 `3→7` 时 RL-Zero acceptance `3.32→5.06`，speedup 反从 `1.77→1.21`；RL-Think `2.77→3.48`、`1.53→0.71`。同步 Qwen3-8B 的结果和异步 235B/GB200 的 2.5× **模拟投影**不可混作同一实测训练收益；本文不能证明任意动态 draft、跨版本复用或最终收敛不变。若现 Ch33 已明确这条 stop-gradient/target-law 双身份，应判 Existing/Only。
