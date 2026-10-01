# 04/23 最后两项：04/20 非作者有界 source→owner 核

复核人：`apr20_resume`。仅核 `2604.20156v1` 与 `2604.20289v1` 的必要方法、主表/直接反证及当前真实正文；不代替 04/23 日期、来源、全集或最终日 Gate，也不写共享 Books。原文均为官方 exact-v1 HTML；04/23 作者工作提案见同目录 `V3_EVIDENCE_REVIEW.md` 最后两节。当前 04/23 旧表的 8 分、`Existing` 和自动选 Top 3 痕迹是尚未按 V3 作者重写的记录，不用其结论回推本次裁决。

## 2604.20156v1：不能整项判 Existing；Ch21 有窄缺口

[官方 v1](https://arxiv.org/html/2604.20156v1) §2.2/§4 将 **每层跨 token 持续的允许 expert mask** 作为 option：原 Top-k router 只在 mask 内选实际激活专家；termination/selection heads 决定何时换 mask，以 deliberation cost 把换组压力纳入训练目标。这不等于仅靠 runtime 预测下一专家。当前 `books/part-02-model/21-moe.md` 的“Router 连续性必须与 Expert Residency 共同设计”（约 L724–728）已经拥有基础命题：时间连续性偏好、真实 residency 仍属 runtime、质量/热点漂移/全驻留回退。但正文没有区分**训练出的 option mask 与每 token 实际 Top-k 激活**，也没有 termination 与换组代价的具体模型控制分支，故不能说该整项机制已完整覆盖；最窄 Books owner 是 `MODEL-MOE` Ch21，该差异可以作为条件性正文增量，非新增结构。

[Table 2–3](https://arxiv.org/html/2604.20156v1) 对 `gpt-oss-20b`、每基准200题、`k̂=16,η=.02` 的 MATH/MMLU/MMMLU 给 base `71.5/79.5/67.5`，controller `64.0/72.5/59.5`，换组率从约 `54–59%` 到约 `4%`；`k̂=8` 的质量损失更大。作者明说每配置单训练 run；[§10](https://arxiv.org/html/2604.20156v1) 未实现或测量 offloading/真实专家换入与端到端延迟，且 per-layer option 与跨层同时装卸未统一。因此只能说**学到更连续的可用集合且有质量代价**，不能把 switch proxy 写成实测 weight traffic/serving speedup。对作者拟 `2+2+2=6` 的证据与窄 Ch21 增量判 `PASS（需正文写前另授锁/写后另核）`；若作者选择 `Only` 也须承认此真缺口，不能以完整 Existing 理由关闭。

## 2604.20289v1：Ch24 窄机制可采用，Table 3 数值方向争议隔离

[官方 v1](https://arxiv.org/html/2604.20289v1) §2 在少步 AR 视频中按 `(denoising step, DiT block)` 跨**相邻生成 chunk**复用 residual，不是旧的相邻 denoising step 缓存；结构/动作 fingerprint 双门控决定跳算。持久 KV 写入所用 clean latent pass 强制完整计算，近似 residual 与下一 chunk 的权威历史状态由此分开。当前 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 约 L70–78 已有视频 clean-pass 才提交 recurrent memory、约 L739–765 已有 condition-prefix KV 与 trajectory 近似 cache，但没有**跨 chunk residual 复用 + 持久 KV 更新 pass 强制 full compute**的组合分支。`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 是生成执行/commit owner；Ch25 仅管 environment-state/预测因果，不因论文叫 world model 就成为主 owner。作者提出的窄 Ch24 增量 `PASS（待 literal/写锁/实际写后）`，旧表 Ch25 `Existing` 须改判，不自动沿用。

[Table 3 与 §4.2](https://arxiv.org/html/2604.20289v1) 确有直接冲突：默认 `skip 71.3% / DiT 1.406s / 2.59× / PSNR 53.384`，去 KV-update protection 后 `62.8% / 1.670s / 2.18× / PSNR 21.461`，却称 skip “improving ... 9 percentage points”。不能据此采用去保护后吞吐方向/增益，也不能把矛盾数字用于 Ch24；保留**该单 clip 画质显著恶化**与该模式应避免污染持久 KV 的窄观察，并将 skip/DiT 数字矛盾具名 `Disputed`，重开条件是作者勘误或可核实现解释。§3只测内部同训练分布13条约22秒轨迹、七相机12 FPS、四步去噪，BF16 单 PPU **DiT 部分**计时，未含 VAE/I/O/端到端交互、OOD/长程/真实 policy-in-loop。若争议标签按整篇计算，须明确只隔离上述方向性速度子主张；不剥夺可独立支持的机制与负面画质证据。

## 20156 后续实际写后复核

root 在本次写前核通过后实写 Ch21“Router 连续性必须与 Expert Residency 共同设计”原两段与本章交接之间。复核人 `apr20_resume` 已重新顺读 `books/part-02-model/21-moe.md` 约 L716–752 和章末 `SF-2026-ARXIV-2604-20156` Review note，且复用上面已实读的官方 v1 §2.2/§4/Table2–3/§10：新增两段明确跨 token **允许集合**与原 Router 的**实际激活集合**不同，控制头/Runtime 各有责任；代价段保集合过窄、各层不同时换组、单一模型质量退步及未测卸载/传输/端到端延迟。原逐 token Top-k 在全驻留或稳定小模型仍为回退，未把 switch rate 当 load latency。前文 dispatch/aggregation 与后文知识树交接未被静默覆盖。Review note 的硬件、样本、单训练 run 与未复现实验范围准确，但其中“尚待非作者写后复核”是本复核前工作态，需改成通过。路径级 `git diff --check` 通过。**结论：仅此 Ch21 机制实写、相邻衔接和来源边界的非作者写后 PASS；不签 04/23 整日 Gate。**

## 20289 后续实际写后复核

root 随后在 Ch24“并行与少步生成必须声明依赖、轨迹和状态边界”中、Salt 的 AR 视频历史段后实写两段。复核人 `apr20_resume` 已顺读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 约 L274–296、章末 `SF-2026-ARXIV-2604-20289` Review，并对照上面已实读的官方 v1 §2/§4.2/Table3/§5。正文确实把**跨 chunk 同 `(step,block)` residual 近似复用**与**持久 KV 的 clean forward 全算**分开，未把计算缓存变成环境状态或动作授权；前接历史质量/训练，后接生成目标误差与 Ch25/26 责任交接通顺。代价段明确只保留单模型短时画质反证，说明表文 skip 方向冲突，没有使用冲突的吞吐数字、2.6×普适收益或真实控制安全保证。Review note 写明 Table3 的 `71.3%→62.8%` 与 §4.2 的反向文字、仅 DiT 部分计时和未覆盖 SLO；其“实际正文仍待非作者写后核”是本核之前的工作态，需同步为通过。路径级 `git diff --check` 通过。**结论：仅此 Ch24 实写与 Review 的非作者写后 PASS；中央数值矛盾保持具名隔离，非 04/23 全日报 Gate。**
