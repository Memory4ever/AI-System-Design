# 12/11 首批准入材料（进行中）

窗口：[2025-12-10T09:00:00+08:00,2025-12-11T09:00:00+08:00)。实际检查开始于2026-10-02T18:23:49+08:00。这里只请求准入校准，不授日期、Evidence或Books Gate。

## 拟继续核验

- [GLM-TTS官方核心说明](https://www.zhipuai.cn/en/research/147)：原有纯文本G2P易误读多音字 → 随机局部G2P混合训练，并在推理用词典定点替换音素 → 可能补足“全局声音风格控制不等于局部发音控制”的表示边界。完整核心已读，位置Fine-grained Pronunciation Control / RL Alignment / Evaluation Results。多奖励GRPO本身不当新算法；更窄增量是Hybrid Phoneme+Text与不启用phoneme的评价边界。请校准这条具体准入理由。原字段`2025/12/10 16:00`没有时区；尚未授窗，不评分。官方仓库/模型产物日期继续定点恢复。
- [METRO 2512.09277v1](https://arxiv.org/abs/2512.09277v1)：token均衡可能激活更多专家权重、恶化memory-bound decode → 平衡激活专家并收集全局top-k → 改变EP负载指标。先保留潜在贡献，精确v1题摘与首公告继续核，不从Submitted授窗。

## 代表性负侧

- [Gemini 2.5 TTS更新](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-2-5-text-to-speech/)：完整核心说明已读。风格、节奏和多说话人一致性有产品改进，但本篇只给演示/客户引语，未披露新训练机制、可比评价或能修正已有机制解释的负侧证据；不因版本更新或多模态主题进入候选。May原始发布已包含多说话人/24语言/风格控制，不能把这些旧能力作本窗新设计。
- [Urania官方说明](https://research.google/blog/a-differentially-private-framework-for-gaining-insights-into-ai-chatbot-use/)：完整核心已读；DP聚类+DP关键词、仅私有关键词进入最终LLM总结有明确安全边界，不作普通负侧关闭。文章明确论文已在COLM2025，需判断这是新增公开机制还是旧论文解释事件；未假定首次公开，暂列身份/日期核验。

其余13源与arXiv普通发现继续，不等待校准。
