# 2602.09416v1 必要审阅（作者准备，Source待独立）

[Are Language Models Sensitive to Morally Irrelevant Distractors?](https://arxiv.org/html/2602.09416v1)，root完整AB准入、Feb11包络核验。采用命题为价值评价对无关上下文的局部敏感性，不把作者道德框架当普遍规范真值；2+1+2=5。

必要原件 valuecore.json §3–4 L99–216：30 text/30 image、各positive/neutral/negative情绪valence；人工移除直接道德教训等混杂，MoralChoice 687低歧义/680高歧义场景，A/B顺序对调平均。MMAP是两候选token概率条件归一化，不是真实动作、安全约束或内部稳定价值。AITA250条、5判决、temperature .2/max256各条件单次采样，context放system；MoralChoice distractor放场景前、max3tokens/logits，不把两协议变化合并为统一效应量。视觉只Gemma/MoralChoice，不授四家族跨模态普遍成立。

§4 Table1–3/Fig2、L173–204：多受测模型negative上下文改变偏好，但GPT4.1与Qwen高歧义部分无显著下降，AITA GPT4.1 null p=.314；MFT dimensions约1–2%变化不显著。Gemma小模型有反向效应，reasoning抑制只在局部低歧义成立，不授通用修复。方法中Llama3.2 4B与结果3B身份数字不一致，不采用精确该型号recipe或规模趋势。数字只作者该fixture描述，无独立复现实验。

valuelimit.json §5–7 L214–230：预训练概率/伦理稀有性仅解释假说，无训练因果操纵；没有交互多轮、distractor顺序/强度/数量变化，只有English两规范框架。局部选择扰动足以反证“静态价值标签会自动保持于不同上下文”，不足证明道德人格、所有alignment失效或human等效心理机制。MoralChoice token控制避免多余输出混杂，但AITA只一次采样、配对依赖与各统计协议不同，不授精确人口级CI。API运行配置/费用/latency Not Disclosed；local两RTX3080Ti只是实验资源，不是部署SLO。

Source后拟 PLATFORM-EVALUATION-SYSTEM 的context-sensitive stress test与value/action proxy交接；必须实际对比owner是否已有同一命题，未授已有覆盖/Books写入。必要正文与直接限制足，停止无关附录完整心理例子。
