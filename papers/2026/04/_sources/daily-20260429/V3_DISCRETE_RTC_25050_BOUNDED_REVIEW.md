# 2604.25050v1 DiscreteRTC：受限原文与 Ch26 owner 审阅

此为 04/29 作者侧单篇必要审阅，非正式冻结候选、Books 写前独立核或整日 Gate。[官方 exact-v1](https://arxiv.org/html/2604.25050v1) 题名为 *DiscreteRTC: Discrete Diffusion Policies are Natural Asynchronous Executors*；旧库存后来版本中的 hockey defend／65%／30% 不属于本次 v1 证据。arXiv 本窗公告须与同家族更早公开例外分开；本文未找到可证明更早完整正文的具名记录，不能由 v1 页首日期或 `submitted` 字段单独断言首次公开时刻。

## 具体机制与现有 owner

Ch26 的 [Action chunk](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已说明 chunk 隐藏模型延迟但扩大 open-loop/stale-action 暴露；同章「Serving + Control Loop」已有异步 `execute chunk k while producing chunk k+1`、sequence/lease/deadline/cancellation 和 tail/jitter/stale-action-rate 合同。这并未具体回答**已提交的前缀怎样成为下一 chunk 的条件、剩余部分怎样重算而不改已执行动作**。论文 §2–4 的增量是把 RTC 的 `d` 个 committed action 固定为已解码前缀：flow-matching 原训练同噪声水平 action chunk，RTC 的混合噪声需逐步 ΠGDM 修正、soft-mask 权重和 VJP；离散 diffusion 原训练已在随机 mask 条件下补全，用已解码 prefix 原生 inpaint，下一 `s` 个必须执行的 action 解码完即可提前停止，未解码 token 作为后续 proposal 状态带入下一轮。这里「无额外实现」仅指该作者 policy 的 inpainting correction path，不是整个机器人控制栈零代码、零训练成本或免验证。

拟 `2+2+2=6` Standard 候选；若日期归属与非作者 source→actual-owner 核通过，Ch26 可能有一处窄长期增量：在异步 overlap 的已有段后，将 action chunk 分成 immutable committed prefix、可继续补全 suffix 和部分 mask/proposal 三种状态；提交门须保证下一段可执行 action 已解码且未越过 controller 的 lease/deadline/safety 检查。离散 diffusion 的原生 masked-prefix 补全是受限实现例，flow RTC 的逐步 correction 是仍有效的对照。共享 Ch26 未写、未获锁；不能只凭评分宣称 Integrate。

## 评价与反证

- §5.1 / Appendix C：Kinetix 对照沿用 RTC 数据、相同 MLPMixer 骨干规模，512-bin 离散动作、5 unmask/denoise steps、每点 2,048 trials；但附录明确 flow 为 constant LR + velocity MSE，离散为 cosine LR + CE/L1，action 表示/输出头亦变。因此不能把 solve-rate 差单独归因于「原生 inpainting」一个变量，也不能称训练 recipe 完全 matched。其额外 hard-mask 平行评测不是自然 schedule 全链优势证明。
- §5.2 / Table 1 / Appendix D：同一 UR5e/Robotiq、Qwen2.5-VL-3B、RTX 4090，20 次/任务。Dynamic Place：ContinuousRTC 90%、DiscreteRTC 100%；Dynamic Pick：45% 对 95%，即 **+50 个百分点**，不是摘要“50% higher”的相对增幅（相对为约 111%）。两 sync 基线在这两任务均 0%，只支持所测动态协议。平均推理时间连续 `151→256 ms`、离散 `303→206 ms`（各自 sync→RTC），跨 action head 比较不能归作单变量算法加速；无尾延迟、抖动、部署安全率。
- §7 / Appendix B.1：naive 512/256-bin tokenization 无时间结构且 action token 串长；模块化 VLM 不参与迭代 unmask。max-confidence 路径没有按期望先解近端 action，常耗尽全部 8 步并降低下一轮未定 proposal 的自由度；因此论文早停/自然 schedule 的计算收益有实施条件，不可概称无条件 `0.7×`。

**暂定处置：** 本窗论文潜在线索中的具名 `6` 分 Standard；Ch26 最小 Books 提案待非作者源→实际 owner 核、日期 Gate 和 root 共享锁。论文原文可作为受限实现证据，不把两个 robot task 的均值变成广义实时性或物理安全保证。
