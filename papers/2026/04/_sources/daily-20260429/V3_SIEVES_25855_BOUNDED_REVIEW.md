# 2604.25855v1 SIEVES：可见视觉证据的选择性回答边界

本项是 04/29 作者侧必要审阅，非独立 Gate。来源为[官方 exact-v1 HTML](https://arxiv.org/html/2604.25855v1) §3–5、Tables 1–3、Appendix 0.A–B；它已经在[第三批题摘反查](./V3_REVERSE_TITLE_ABSTRACT_BATCH3.md)由旧“单任务 VQA 指标”误拒恢复为潜在线索，**不再次改变**同一 106 篇已读题摘工作集合。官方 [v1 身份页](https://arxiv.org/abs/2604.25855v1) 的提交字段是 04/28T16:57:29Z，不独证公开时刻；本日 checkpoint 的官方公告机制＋相邻 ID/DOI 窄批次链支持其所属的北京 04/29 08:00 公告批次，仍需独立日级日期 Gate。

**早发例外定点消歧：** [作者主页](https://hector.gr/)当前给此条写着 `arXiv preprint, 2025`，乍看早于本窗；但作者自己的 [主页源代码提交 `551faef`](https://github.com/hector-gr/hector-gr.github.io/commit/551faefd58f3afaaa08cba633d5bb6cb3140ed6e) 的 `committer.date=2026-04-30T13:27:22Z` 才首次把 SIEVES 标题、摘要与这个 `2025` 文本加入 `index.html`，其[前一版本](https://github.com/hector-gr/hector-gr.github.io/blob/7aba80db344ba9ff10e23c36e39294e93ce75a1a/index.html)没有 SIEVES；作者的 [SIEVES 代码仓库](https://github.com/hector-gr/SIEVES) 官方 API `created_at=2026-04-30T12:08:32Z`，也在本窗后。由此 `2025` 是 04/30 加入时的标签，不是 2025 已公开论文的时间证据；不能反过来说已证明互联网没有更早副本。此窄链只排除已触发的具名主页/代码早发疑点，不扩大版本史。

## 机制、评价与直接反证

Reasoner 先用 zoom-in tool 产生 crop 轨迹与回答；Gemma-3-4B selector 消费问题、原图、含 crop 的轨迹和答案，不需 reasoner logits/hidden states。它分别训练正确性 `c_corr`、定位 `c_loc` 与 crop—答案连贯性 `c_coh` 三个 head，再加权成弃答分数。定位目标是预测 crop 对标注框的平均 IoGT 是否至少 .75；连贯性训练标签由 Qwen2.5-VL-7B 判定，并在未正确定位时置零。训练轨迹只来自 Pixel-Reasoner 在 Thyme/TAT-DQA；Thyme 的 750 题 MC holdout 用于 checkpoint/risk-level model selection，所测 OOD 五数据集与 o3、Gemini-3-Pro 无专门适配。故可迁移的是**有可见 crop 轨迹时，额外评估证据质量的 selector 分支**，不是任意黑盒 VLM 的免校准置信概率。

Table 2 在受测多数切片支持与 correctness-only selector 的覆盖/排序改善，例如有定位的 Pixel-Reasoner 在 V* C@5 为 9.7 对 1.4；但 HR-Bench 的 C@1 为 2.3 对 1.4，不能据摘要“至多三倍”统一推全部数据集、风险点或 reasoner。Table 3 的“排除任一目标均有害”也不是逐指标普遍成立：Pixel-Reasoner ID 平均覆盖 full .6/.3/.1 为 26.6、correctness-only 为 26.7；Pixel OOD full 27.0、去掉 coherence 也是 27.0；Gemini OOD full 53.4、.6/.2/.2 为 54.7。它保留受限多信号设计方向，不证明这组权重或三个 head 对任一分布都必要。VizWiz/AdVQA 用 validation，开放答案由与训练同一 LLM judge 作 hard accuracy；重复采样共用问题，并非同数独立问题。

最重要的发布边界在 §4.3 与 Appendix 0.A Eqs 9–12：论文的 `C@r` 在**目标测试集真值**上选 `max_tau C(tau)`，约束同一集的经验错误率 `R(tau)≤r`；pooled 阈值亦由目标集合的答错标签计算。它是事后 risk–coverage 曲线/排序汇总，不是事先独立 calibration set 得到的部署阈值，更没有给 OOD 风险的有限样本上界。Thyme holdout 选模型不能替代每个目标切片的阈值校准。受测闭源模型可不提供权重/logits，但仍要给相容的 crop/trace；高风险业务不能用这里的 `C@1` 当逐响应或未来流量 1% 错误保证。Appendix Table 4 的 V* Pixel 五重复均值 `16.3±9.1` 与 pooled `9.7` 也提示小集低风险工作点不稳。

## 作者侧准入与真正 owner

具体贡献是把**可见定位质量和 crop—回答连贯性**作为黑盒多模态选择性回答的附加传感器，并把它与最终答案正确性分账；相较只读语气或内部 logit，它改变可用证据接口。拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9`，标准审阅；中央“给定用户风险可可靠部署”只能窄隔离为尚未验证的阈值/保证，若正式 Disputed 应保留其余实测排序，不把整篇当无效。首公开尚待核，不提前记正式日报候选。

[ROADMAP](../../../../../ROADMAP.md) 的 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在“从 Raw Score 到可定位、可校准的 Claim Sensor”已经要求 sensor 与 truth、部署切片 calibration、risk–coverage、abstention 分开，但原段落主要是文本 claim/内部 hidden-state probe，并在内部不可得时给多样本/检索回退；[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 拥有视觉 crop/证据获取，但把最终风险与弃答交 Ch66。真正最窄 Books gap 因而在 Ch66：**黑盒视觉 reasoner 若暴露带坐标的 crop 轨迹，可把定位/证据—答案一致性作为独立观察量训练风险 selector；其分数仍须在独立部署切片校准，离线同集最优 `C@r` 不能变成 release guarantee。** 不复制 SIEVES 三 head 配方或论文倍率到长期正文。root 已对官方必要 §3/§4.3/Appendix 0.A 与实际 Ch66 命题完成非作者写前 PASS，按独占窄锁在 Ch66 原内部 probe 回退段后实际写入两段和章末 Review note；root 随后顺读实际正文、前后邻段和注记并在[独立写后记录](./V3_ROOT_25855_CH66_WRITE_AFTER.md)给出 PASS。因此本项 **Books 最窄整合已真实通过**，但首公开、全来源与 04/29 独立日级 Gate 仍待核，不能把它计作本日 Complete。
