# 2604.24842v1 Co-Director：旧潜在线索反向准入

这是 2026-04-29 V3 作者侧的**具名前分母关闭**，待非作者负侧抽核，不是对 video-agent 领域的普遍否定。官方 [exact-v1](https://arxiv.org/html/2604.24842v1) §3.1–3.3、§4–5/Table1–4、Appendix F 的决定性段已读；[v1 身份页](https://arxiv.org/abs/2604.24842v1)用于同一公告批次联合链，不把 `submitted` 孤字段当首公开。旧 V2.1 的 9 分/深入完成/No Change 不继承。

## 原文实有贡献与反向门槛

《Co-Director: Agentic Generative Video Storytelling》在 12 秒、四镜头虚构广告上，把 creative strategy、narrative mode、aesthetic archetype 三个预设轴组成配置；orchestrator 在四次完整生成预算中用 MAB/LLM warm start 选择配置，storyline/keyframe 用判分-重写局部循环，Veo/Nano Banana/Gemini 等后端生成镜头/音频。它不是空的“多 Agent 协作”名称。Table1 在同 `T=4` 下相对 random search 的自家 MLLM judge 平均 `81.4 vs 75.7`，Table4 的 cold start/scalar reward/去 keyframe refinement 对照也显示该广告工作点的变化；50 场景×五人 MOS 表中完整系统 `3.96`，Veo 3.1 `3.71`，不能否认其局部实验。

但 §3 的职责与状态是成熟的 centralized creative brief → storyboard → keyframe/clip/audio → judge/repair 组合；MAB 的三轴为广告创意 taxonomy，四次 pull、LLM warm start 与 factor reward 都由同一 MLLM 的主观评分驱动，没有隔离出新的跨任务 budget/authority/state consistency 条件。Appendix F 明说三轴各自更新以规避 36 种组合的穷举，并未测三轴相互作用、全局最优或常见生成器能力变化；`T=4` 的相对随机优势不能支持“快速收敛到全局最优”。§5.1 Table1 的完整均值 `81.4` 与 §5.3 Table4 `Ours 79.0` 并非同一个可直接拼接的数值分母，原文在相邻描述未交代差异；不将消融的差额接成跨表精确因果量。50 场景人评仅校准某些视觉/广告维度，Table2 的 VQ MLLM-human Spearman `0.317`、human-human `0.675`，并不足以把主评分器作为独立真值；同一 judge 用于搜索和最终表格还有适配偏差。与其它 pipeline 的生成预算、输入脚本适配、人工评测范围也不等价于所有多 Agent 系统同成本比较。

已对读 `books/part-07-agent/82-multi-agent.md` 的 orchestration、预算/探索与 verifier 权责，及 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的视频跨段一致性、keyframe/validator/fallback：受限证据可作为广告视频 workflow 实例，却没有指出这些真实 owner 尚缺哪条可迁移设计分支或受控反例。不能仅因 400 个 fictional product 场景、四维指标及 ROADMAP 可路由就入选。因此作者侧从旧 60 潜在集合中**前分母具名关闭**；不评分、不进 Books，也不再为关闭扩全附件。若非作者发现可跨广告/后端迁移且现有 owner 未持有的预算、全局—局部 credit 或 evaluator 独立边界及匹配反证，则按具体命题重开，不用论文名恢复高分。

**工作账影响（待同行负侧抽核）：**本日已处置 106 个唯一论文完整题摘不变；接续 BARRED、25200 和 KinDER 后的作者工作账从 `68 潜在／38 前闭` 调为 **`67 潜在／39 前闭`**。这篇属于旧 60，故旧子集从 `39／21` 调为 **`38／22`**。作者终态不等于本窗最终候选分母或独立日级 Gate；非作者若指出可迁移新条件，按上文具体反例重开，原判断链不覆盖或删除。
