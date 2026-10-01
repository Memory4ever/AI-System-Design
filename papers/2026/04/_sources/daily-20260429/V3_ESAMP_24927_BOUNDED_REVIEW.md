# 2604.24927v1 ESamp：在线 latent 探索与逐步最优印刷保证的窄隔离

本项属于旧 60 中已读完整题摘的潜在线索，不增加当前 `106＝70 潜在＋36 具名前闭` 工作集合。仅读[官方 exact-v1 HTML](https://arxiv.org/html/2604.24927v1) §3–5、Appendix A.2、C.2/C.8/C.10 的决定性方法、评价和反证，并对照真实 [Ch20 Parallel Sampling](../../../../../books/part-02-model/20-sampling.md) 的前后论点；未遍历附件、代码或版本史。官方 v1 页眉的 `27 Apr 2026` 是文稿标识，不作为首公开时间；当窗归属仍须使用本日公告窄批链和更早独立公开例外检查，尚非日期 Gate。

## 贡献与实际机制

现有 Ch20 已把多样采样的 `coverage`、候选选择、query-local 状态和端到端预算分开，明确 `pass@N` 只是正确候选出现的上界；温度、top-p、pairwise/hidden selector 各有共存条件。但它尚未解释：并行候选可否在**生成期间**用同一个、持续更新的内部状态，降低后来候选重复先前 latent pattern 的概率。ESamp 在冻结 LLM 的第一层表示 `h¹` 到末层表示 `hᴸ` 之间，在线训练小型 Latent Distiller `fφ`；经同一个 LM head 投影，形成 `πref` 和 `qdist`，将 token 分布改为 `πnew(z|s) ∝ πref(z|s)^(1+β)/qdist(z|s)^β`（§4.1–4.2 Eq. 3–9）。Distiller 从批内各轨迹更新，是跨并行候选的共享探索状态，而非外部正确性 verifier；当前实现依赖可取中间层、额外参数训练、同步和 async overlap 的 slack。§4.4 自认 GPU 完全饱和时重叠优势可能下降。这是值得审阅的受限生成设计分支，不能因 Ch20 有一般“采样多样性”而直接称完全已有覆盖。

作者侧拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9`，正常最低为 Standard；但以下附录中央理论保证存在精确可复核的印刷反例，按当前合同的实际纠错/冲突 override 对**受影响保证**深入审阅。暂定 `Books：Ch20 可能窄 gap，待非作者 source→actual owner 核后决定；不得把争议定理作为正面依据`。没有共享 Books 写锁，也没有据本篇预记真实整合或日级完成。

## 印刷 Proposition A.2 的最小反例与隔离范围

Appendix A.2 Definition A.1/Eq. 19 只说 `r_t=0 ⇒ 所有未来 r=0`；Proposition A.2 却声称该条件足以得逐步 `Q*(s_t,z_t)=r_t(s_t,z_t)`。其证明 Case 2 在 `r_t>0` 时以“当前 region 探索后归零”推导全部后续 reward 为零，这不是 Eq. 19 的前件，也未排除下一步进入**另一个**新 region。取两步确定性链 `r₁=1,r₂=1`，其余后续奖励全零，折扣 `0<γ≤1`：它满足 Eq. 19（前两步无 `r=0`；末尾为零后永远零），但 `Q*(s₁,z₁)=1+γ>1=r₁`。这是印刷命题的充分条件缺失，不需运行代码即可定位。即使补进“同一 region 归零”，也不能自动推其它 region 未来不能获正奖励。论文又在同节明说在线 Distiller **并不严格满足** Definition A.1，故不能把 Proposition 当实际 sampler 的已证最优性或安全保证。

隔离只覆盖“该定义足以保证逐步最优等于即刻 reward／在线实现继承此证明”的宣称，不吞掉 §4 可执行 logit 机制、受限探索实验或本章可能需要的设计分支；也不推断作者代码崩溃或真实部署失败。非作者应定点核 Eq. 19 的量词、Case 2 的额外假设和上述两步链，而非复现全部附件。

## 评价、成本和反向证据

- §5.1 的测试是 Qwen2.5-7B/32B、Qwen3-8B（no-thinking）和 GPT-OSS-20B（low effort），AIME24/25、GPQA-Diamond、LiveCodeBench v5 与写作代理；GPQA 只是模型推理评价，不是本项目暂缓的 AI-for-Science 应用准入。`pass@k` 衡量候选集合覆盖，不证明投票、selector 或上线 acceptance 可实现该上界。
- Appendix C.2 Tables 5–6 中 Qwen2.5-7B 的 AIME25 `pass@1 6.6→6.0`、AIME24 `10.7→9.5`，而 C.5 Table 12 的 Qwen3-8B/AIME25 `pass@8 51.4→46.2`、`pass@64 58.9→67.8`；“探索增加”与单样本/低预算正确率不可混作单向收益。C.8 Table 16 的 self-consistency `Maj@8 50.3→50.0`、`Maj@32 53.7→54.5` 更说明选答器不是免费的。
- Appendix C.10 Table 18：AIME24 shared LD 的 `pass@16/64 64.7/76.6` 低于 per-prompt `70.0/80.0`，AIME25 `55.3/63.3` 低于 `57.0/63.9`；但 LCB v5 `25.8` 略高于 `24.1`。批间共享状态会受 prompt 异质性影响，不能称它普遍优于隔离状态；上线须记录 distiller 训练身份、批组成、共享范围和回退。
- §5.4 Table 3 的 RTX4090/Qwen3-8B token throughput 为 `B1K1 55.1→54.9`、`B32K1 1215.2→1193.2`、`B32K16 4557.7→4364.0`，作者给 .3%、1.81%、4.25% 开销；这是受限吞吐比较，不是每请求延迟、tail SLO、跨硬件或生产多租户保证。§5.2 写作的 embedding/Vendi、另一个小模型 PPL 只是代理，不能证真语义路径与人工品质全面提高。

非作者下一步只需回答：上述有限反例是否确实击穿**印刷条件到等式**，而非仅实际 LD 未满足理想条件；Ch20 目前是否已有与“共享在线 latent 探索状态”同义的机制，若无，这项机制在保留反向成本与 selector 分账后应最小落在何处。首公开日期、来源覆盖、全日候选分母和整体独立 Gate 仍另审。
